"""Make canvas artboards that show a spec file as text. Measures the height with local fonts first."""
import sys, re, html, json, asyncio
from playwright.async_api import async_playwright
ROOT='/home/claude/cover_design/experiment/'
def highlight(text, fmt):
    out=[]
    for line in text.split('\n'):
        e=html.escape(line)
        if fmt=='yaml':
            if re.match(r'^\s*#',line):
                e='<span class="c">'+e+'</span>'
            else:
                e=re.sub(r'^(\s*(?:-\s+)?)([A-Za-z_][A-Za-z0-9_]*)(:)', r'\1<span class="k">\2</span>\3', e)
        else:
            e=re.sub(r'^(\s*)(&quot;[A-Za-z_][A-Za-z0-9_]*&quot;)(:)', r'\1<span class="k">\2</span>\3', e)
        out.append(e)
    return '\n'.join(out)
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
def body(title, sub, pre, w, h, cols):
    return ('<div class="sb" style="width: %dpx; height: %dpx; box-sizing: border-box; padding: 40px 48px; overflow: hidden; background: #FBFAF7">'
            '<div class="hd"><b>%s</b><span>%s</span></div>'
            '<pre style="column-count: %d">%s</pre></div>')%(w,h,html.escape(title),html.escape(sub),cols,pre)
async def measure(page_html):
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':3000,'height':1200})
        open(ROOT+'boards/_m.html','w',encoding='utf-8').write(page_html)
        await pg.goto('file://'+ROOT+'boards/_m.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
        h=await pg.evaluate("(function(){var p=document.querySelector('.sb pre'); return p.getBoundingClientRect().height;})()")
        await b.close(); return h
def make(name, fmt, title, w, cols):
    text=open(ROOT+'specs/%s.%s'%(name,fmt),encoding='utf-8').read().rstrip('\n')
    lines=len(text.split('\n')); size=len(text.encode('utf-8'))
    sub='%s 명세 · %d줄 · %.1fKB'%(fmt.upper(), lines, size/1024)
    pre=highlight(text, fmt)
    # measure: content height with unbounded height
    probe='<!doctype html><html><head><meta charset="utf-8">'+CSS_LOCAL+'<style>'+STYLE+'</style></head><body>'+body(title,sub,pre,w,20000,cols).replace('height: 20000px','height: auto')+'</body></html>'
    ph=asyncio.run(measure(probe))
    H=int(ph/cols*1.0)  # columns balance: pre height is already the balanced height
    H=int(ph)+40+80+60   # padding + header
    return text, sub, pre, H
if __name__=='__main__':
    for name,fmt,title in [(a,b,c) for a,c in [('night','밤의 가판대'),('paper','편집국 1면'),('calendar','달력 벽')] for b in ['yaml','json']]:
        for w,cols in [(1440,2),(2160,3)]:
            t,sub,pre,H=make(name,fmt,title,w,cols)
            print(name,fmt,w,cols,'height',H)
