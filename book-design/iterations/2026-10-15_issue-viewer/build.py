"""Build the issue-viewer previews and the review page.

preview_base.html  the 7th version (base_src.html) with the 10/15 data copy: 'before'
preview_a.html     this folder's src.html, viewer variant A (lamp and stand, like today's issue)
preview_b.html     this folder's src.html, viewer variant B (larger cover, no lamp)
draft.html         the review page to publish: Google Fonts, the same data copy and clock, and an A/B switch
preview_adopted.html  library_night/src.html after variant B was adopted, with the same data copy

All four read the same data copy (db_snapshot_1015.json, 46 briefs) and use the same fixed clock
(2026-10-15 12:00 KST), so the hero and the rack are the same in every file. The live database is not used:
the block that subscribes to window.claude is replaced by a loader that reads the copy.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
D = '/home/claude/cover_design/'

mzcss = open(D + 'mz.css', encoding='utf-8').read().rstrip('\n')
mzjs = open(D + 'mz.js', encoding='utf-8').read().rstrip('\n')
snap = json.load(open(os.path.join(HERE, 'db_snapshot_1015.json'), encoding='utf-8'))

GF = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@400;500;600;700;800'
      '&family=IBM+Plex+Mono:wght@400;500&family=Oswald:wght@500;600&family=Outfit:wght@700;800&display=swap">')
LOCAL = ''.join('<link rel="stylesheet" href="../../cover_design/node_modules/@fontsource/%s.css">' % f for f in
                ['gothic-a1/400', 'gothic-a1/500', 'gothic-a1/600', 'gothic-a1/700', 'gothic-a1/800',
                 'ibm-plex-mono/400', 'ibm-plex-mono/500', 'oswald/500', 'oswald/600', 'outfit/700', 'outfit/800'])
# the document skeleton the artifact host wraps around a page (same as library_night/build.py)
SKEL = ('<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#faf9f5;color:#141413}'
        'img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')

CLOCK_OLD = 'function kstNow(){var t=new Date(Date.now()+9*36e5);'
CLOCK_NEW = 'function kstNow(){var t=new Date(Date.UTC(2026,9,15,3,0)+9*36e5);'
LOADER = ('/* review copy: a fixed copy of the library database (2026-10-15 12:00 KST) instead of the live one */\n'
          'var SNAP=' + json.dumps(snap, ensure_ascii=False) + ';\n'
          "S.status='ready';\n"
          'setData(SNAP.briefs);\n'
          "S.related=SNAP.related.map(function(d){var x=d.data||{}; return {id:d.id,date:x.date?String(x.date).slice(0,10):'',"
          "title:x.title?String(x.title):'',url:safeUrl(x.url)};});\n"
          'render();\n')


def page(src_path):
    s = open(src_path, encoding='utf-8').read()
    assert s.count('/*<<MZCSS>>*/') == 1 and s.count('/*<<MZJS>>*/') == 1
    s = s.replace('/*<<MZCSS>>*/', mzcss).replace('/*<<MZJS>>*/', mzjs)
    assert s.count(CLOCK_OLD) == 1
    s = s.replace(CLOCK_OLD, CLOCK_NEW)
    a = s.index('var claude=window.claude;')
    z = s.index('\n})();\n</script>', a)
    s = s[:a] + LOADER + s[z + 1:]
    assert s.count(GF) == 1
    return s


def variant(v):
    return '<script>document.documentElement.setAttribute("data-vw","%s");</script>\n' % v


def preview(s, v=None):
    s = s.replace(GF, LOCAL)
    if v:
        s = s.replace('<div id="app"></div>', variant(v) + '<div id="app"></div>', 1)
    return SKEL + s + '\n</body></html>'


REVIEW = '''<style>
/* review switch: not part of the design, only for comparing the two viewer drafts */
.rv{position:fixed;left:calc(16px + env(safe-area-inset-left,0px));bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:300;display:flex;align-items:center;gap:4px;padding:4px;border-radius:12px;background:rgba(20,24,30,.94);box-shadow:inset 0 0 0 1px #39414C,0 12px 28px rgba(0,0,0,.5);font:600 13px/1 'Gothic A1',sans-serif;color:#B4B9C1}
.rv-t{padding:0 8px 0 10px;white-space:nowrap}
.rv-b{height:32px;padding:0 12px;border:0;border-radius:8px;background:none;color:#B4B9C1;font:inherit;white-space:nowrap;cursor:pointer}
.rv-b:hover{color:#F2F0EC;background:#1A1F26}
.rv-b[aria-pressed="true"]{background:#F2F0EC;color:#0C0E12}
.rv-b:focus-visible{outline:2px solid #F2F0EC;outline-offset:2px}
.rv-n{padding:0 10px 0 8px;font-weight:500;color:#8A919B;white-space:nowrap}
@media (max-width:1279px){html.vw-lock .rv{bottom:calc(84px + env(safe-area-inset-bottom,0px))}}
@media (max-width:699px){.rv{left:calc(8px + env(safe-area-inset-left,0px));right:calc(8px + env(safe-area-inset-right,0px));bottom:calc(8px + env(safe-area-inset-bottom,0px));justify-content:center}.rv-n{display:none}.rv-t{display:none}}
</style>
<div class="rv" role="group" aria-label="열람 창 시안 고르기"><span class="rv-t">열람 창</span><button type="button" class="rv-b" data-v="A" aria-pressed="true">시안 A · 오늘의 호처럼</button><button type="button" class="rv-b" data-v="B" aria-pressed="false">시안 B · 표지 크게</button><span class="rv-n">10월 15일 12시 데이터 사본</span></div>
<script>
(function(){
  var r=document.documentElement, bs=[].slice.call(document.querySelectorAll('.rv-b'));
  r.setAttribute('data-vw','A');
  bs.forEach(function(b){b.addEventListener('click',function(){
    var v=b.getAttribute('data-v'); r.setAttribute('data-vw',v);
    bs.forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});
    document.dispatchEvent(new Event('vw-variant'));
  });});
})();
</script>
'''


def out(name, text):
    open(os.path.join(HERE, name), 'w', encoding='utf-8').write(text)
    print(name, len(text))


base = page(os.path.join(HERE, 'base_src.html'))  # the 7th version, pinned
out('preview_base.html', preview(base))

mine = os.path.join(HERE, 'src.html')
if os.path.exists(mine):
    s = page(mine)
    out('preview_a.html', preview(s, 'A'))
    out('preview_b.html', preview(s, 'B'))
    title_old = '<title>크립토 브리핑 서고 ⭕</title>'
    assert s.count(title_old) == 1
    d = s.replace(title_old, '<title>서고 열람 창 시안</title>').replace('<div id="app"></div>', '<div id="app"></div>\n' + REVIEW, 1)
    out('draft.html', d)
    out('draft_local.html', preview(d))  # the review page with local fonts, for checking the switch

# after the owner chose B (2026-10-15 14:35): the adopted page with the same data copy, to compare with preview_b.html
adopted = D + 'library_night/src.html'
if 'issue viewer' in open(adopted, encoding='utf-8').read():
    out('preview_adopted.html', preview(page(adopted)))
