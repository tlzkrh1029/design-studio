"""Make canvas artboards for round 2: spec text boards (md, xml) and result image boards."""
import re, html, json, asyncio, shutil
from playwright.async_api import async_playwright
E2='/home/claude/cover_design/experiment2/'
SP='/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/'
PROJ=SP+'canvas/project/'
CSS_LOCAL='''<link rel="stylesheet" href="../../node_modules/@fontsource/ibm-plex-mono/400.css"><link rel="stylesheet" href="../../node_modules/@fontsource/ibm-plex-mono/600.css"><link rel="stylesheet" href="../../node_modules/@fontsource/gothic-a1/400.css"><link rel="stylesheet" href="../../node_modules/@fontsource/gothic-a1/700.css"><link rel="stylesheet" href="../../node_modules/@fontsource/gothic-a1/800.css">'''
CSS_GF='''<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&amp;family=Gothic+A1:wght@400;700;800&amp;display=swap">'''
STYLE='''body{margin:0;background:#FBFAF7}
.sb{font-family:'IBM Plex Mono','Gothic A1',monospace;color:#1E2227}
.sb pre{margin:0;font-family:inherit;font-size:13px;line-height:1.55;white-space:pre-wrap;word-break:break-all;column-gap:44px;column-rule:1px solid #E3E0D8}
.sb .k{color:#1D4ED8;font-weight:600}
.sb .c{color:#7A776F}
.sb .hd{display:flex;align-items:baseline;gap:18px;padding-bottom:18px;margin-bottom:22px;border-bottom:2px solid #1E2227;font-family:'Gothic A1',sans-serif}
.sb .hd b{font-size:30px;font-weight:800;letter-spacing:-.01em}
.sb .hd span{font-size:15px;color:#5A5850}'''
def highlight(text, fmt):
    out=[]; in_code=False
    for line in text.split('\n'):
        e=html.escape(line, quote=False)
        if fmt=='md':
            if line.strip().startswith('```'):
                in_code=not in_code; e='<span class="c">'+e+'</span>'
            elif not in_code and line.startswith('#'):
                e='<span class="k">'+e+'</span>'
            elif in_code:
                e=re.sub(r'(/\*.*?\*/)', r'<span class="c">\1</span>', e)
                e=re.sub(r'^(\s*)(--[A-Za-z0-9_-]+)(:)', r'\1<span class="k">\2</span>\3', e)
        else:
            e=re.sub(r'(&lt;/?[A-Za-z_][A-Za-z0-9_]*(?:\s[^&]*?)?&gt;)', r'<span class="k">\1</span>', e)
            e=re.sub(r'(/\*.*?\*/)', r'<span class="c">\1</span>', e)
        out.append(e)
    return '\n'.join(out)
def body(title, sub, pre, w, h, cols):
    return ('<div class="sb" style="width: %dpx; height: %dpx; box-sizing: border-box; padding: 40px 48px; overflow: hidden; background: #FBFAF7">'
            '<div class="hd"><b>%s</b><span>%s</span></div>'
            '<pre style="column-count: %d">%s</pre></div>')%(w,h,html.escape(title),html.escape(sub),cols,pre)
async def measure(page_html):
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':3000,'height':1200})
        open(E2+'boards/_m.html','w',encoding='utf-8').write(page_html)
        await pg.goto('file://'+E2+'boards/_m.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
        h=await pg.evaluate("(function(){var p=document.querySelector('.sb pre'); return p.getBoundingClientRect().height;})()")
        await b.close(); return h
def dc(title, helmet, inner, w, h):
    return ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n%s\n</helmet>\n%s\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":%d,"height":%d}}\'>\nclass Component extends DCLogic {\nrenderVals() {\nreturn {};\n}\n}\n</script>\n</body>\n</html>\n')%(html.escape(title),helmet,inner,w,h)
THEMES={'night':('Night','밤의 가판대'),'paper':('Paper','편집국 1면'),'calendar':('Calendar','달력 벽')}
FMT={'md':('Md','브리프 + 토큰'),'xml':('Xml','XML 태그')}
BLOB=json.load(open(E2+'boards/blobs.json'))
SIZES={}
for t,(T,ko) in THEMES.items():
    for f,(F,fko) in FMT.items():
        text=open(E2+f'specs/{t}.{f}',encoding='utf-8').read().rstrip('\n')
        lines=len(text.split('\n')); size=len(text.encode('utf-8'))
        sub='%s 명세 · %d줄 · %.1fKB'%(fko, lines, size/1024)
        title='%s · %s 명세'%(ko,fko)
        pre=highlight(text,f)
        probe='<!doctype html><html><head><meta charset="utf-8">'+CSS_LOCAL+'<style>'+STYLE+'</style></head><body>'+body(title,sub,pre,1440,20000,2).replace('height: 20000px','height: auto')+'</body></html>'
        ph=asyncio.run(measure(probe)); H=int(ph)+180
        helmet=CSS_GF+'\n<style>\n'+STYLE+'\n</style>'
        name=f'Exp{T}{F}Spec.dc.html'
        open(PROJ+name,'w',encoding='utf-8').write(dc(title,helmet,body(title,sub,pre,1440,H,2),1440,H))
        SIZES[name]=H; print(name,H,lines)
    for c,(C,cko) in {'direct':('Direct','명세 없이 바로'),'md':('Md','브리프 + 토큰'),'xml':('Xml','XML 태그')}.items():
        from PIL import Image
        Image.MAX_IMAGE_PIXELS=None
        im=Image.open(E2+f'renders/{t}_{c}.png'); W,H=im.size
        title=('명세 없이 바로 만든 결과 · %s'%ko) if c=='direct' else ('%s로 만든 결과 · %s'%(cko,ko))
        alt=('%s를 명세 없이 바로 만든 서고 페이지 전체 화면.'%ko) if c=='direct' else ('%s %s 명세를 따라 만든 서고 페이지 전체 화면.'%(ko,cko))
        inner='<div style="width: %dpx; height: %dpx; background: #FFFFFF; overflow: hidden">\n<img src="%s" alt="%s" style="display: block; width: %dpx; height: %dpx">\n</div>'%(W,H,BLOB[f'{t}_{c}'],html.escape(alt),W,H)
        name=f'Exp{T}{C}Result.dc.html'
        open(PROJ+name,'w',encoding='utf-8').write(dc(title,'<style>\nbody{margin:0;background:#FFFFFF}\n</style>',inner,W,H))
        SIZES[name]=H; print(name,H)
json.dump(SIZES,open(E2+'boards/sizes.json','w'),indent=1)
