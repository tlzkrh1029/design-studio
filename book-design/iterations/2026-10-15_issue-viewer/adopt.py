"""Write the adopted page: this iteration's src.html with only variant B, into cover_design/library_night/src.html.

The owner chose variant B on 2026-10-15 at 14:35 ("시안 b로 가자. 착수하자."). Variant A's styles and markup and
the A/B switch (<html data-vw>, the 'vw-variant' event) are removed; B's rules move from `.vw-b .x` to `.vw .x`,
which keeps their specificity, so the page renders exactly like preview_b.html. The headline fit is kept as is.
Run patch.py first; build.py then makes preview_adopted.html for the comparison.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = '/home/claude/cover_design/library_night/src.html'
s = open(os.path.join(HERE, 'src.html'), encoding='utf-8').read()


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:90])
    s = s.replace(old, new)


# ---- styles
rep('''/* ===== issue viewer: a past issue opened over the page, laid out like today's issue =====
   Desktop: a 1440-wide box scaled with zoom to the window, over a dark veil. A keeps the lamp and stand of
   today's issue (cover 400px); B drops them for a larger cover (360-520px, from the window height).
   Narrow: a full-screen sheet with a title bar and the previous/next buttons at the bottom. */''',
    '''/* ===== issue viewer: a past issue opened over the page, laid out like today's issue =====
   Desktop: a 1440-wide box scaled with zoom to the window, over a dark veil. The cover stands larger than
   today's, without the lamp (360-520px, from the window height), with the same text column beside it.
   Narrow: a full-screen sheet with a title bar, and previous, open-brief and next at the bottom. */''')
rep('''.vw.still .vw-stage,.vw.still .vw-wrap{animation:vwFade 180ms ease-out both}
.vw.still .halo,.vw.still .beam,.vw.still .lamp .bulb,.vw.still .pool{animation:none}
''', '''.vw.still .vw-wrap{animation:vwFade 180ms ease-out both}
''')
rep('''/* A: today's issue as it is (the text column is 40px narrower than the hero's, to clear the arrow) */
.vw-a .htext{width:600px}
.vw-a .vw-stage{position:absolute;left:64px;top:calc((var(--vh,840px) - var(--hero-h)) / 2);width:var(--content);height:var(--hero-h)}
.vw-cord{position:absolute;left:320px;bottom:100%;width:1px;height:1200px;background:var(--line-strong)}
/* B: a larger cover without the lamp */
''', '''/* the cover with a soft light behind and below it, and the text column */
''')
rep('''  .vw-a .vw-stage{position:relative;left:auto;top:auto;width:auto;height:auto;margin:0;padding:24px 32px 0;overflow:hidden}
  .vw-cord,.vw-hint{display:none}
''', '''  .vw-hint{display:none}
''')
rep('''  .vw-a .htext{width:auto}
''', '')
rep('''  .vw-a .vw-stage{padding-left:16px;padding-right:16px}
''', '')
rep('''  .vw-veil,.vw .vw-box,.vw .vw-stage,.vw .vw-wrap{animation:none}''', '''  .vw-veil,.vw .vw-box,.vw .vw-wrap{animation:none}''')
rep('.vw-b ', '.vw ', 12)

# ---- script
rep('''var VW={id:null,opener:null,el:null,v:'A',down:null};''', '''var VW={id:null,opener:null,el:null,down:null};''')
rep('''function vwVariant(){return document.documentElement.getAttribute('data-vw')==='B'?'B':'A';}
''', '')
rep('''function vwCover(b,cls){
  var inner='<div class="cv" aria-hidden="true">'+cover(b)+'</div>';
  return b.url?'<a class="'+cls+'"'+ext(b.url)+' aria-label="'+esc(coverLabel(b))+'">'+inner+'</a>'
    :'<div class="'+cls+'" role="img" aria-label="'+esc(coverLabel(b))+'">'+inner+'</div>';
}''', '''function vwCover(b){
  var inner='<div class="cv" aria-hidden="true">'+cover(b)+'</div>';
  return b.url?'<a class="vw-cv"'+ext(b.url)+' aria-label="'+esc(coverLabel(b))+'">'+inner+'</a>'
    :'<div class="vw-cv" role="img" aria-label="'+esc(coverLabel(b))+'">'+inner+'</div>';
}''')
rep('''  var el=vwEnsure(), v=vwVariant(), i=B.indexOf(b), box=el.querySelector('.vw-box');
  VW.id=b.id; VW.v=v;
  el.className='vw vw-'+v.toLowerCase()+(first?'':' still');''', '''  var el=vwEnsure(), i=B.indexOf(b), box=el.querySelector('.vw-box');
  VW.id=b.id;
  el.className='vw'+(first?'':' still');''')
rep('''  var body=v==='A'
    ?'<div class="vw-stage"><div class="art">'
        +'<i class="vw-cord" aria-hidden="true"></i>'
        +'<div class="halo" aria-hidden="true"></div><div class="beam" aria-hidden="true"><i></i></div>'+LAMP
        +vwCover(b,'hcover')
        +'<div class="stand" aria-hidden="true"></div><div class="pool" aria-hidden="true"></div>'
        +'<p class="stand-cap vw-hint" aria-hidden="true">'+esc(hint)+'</p></div>'
      +'<div class="htext">'+vwText(b)+'</div></div>'
    :'<div class="vw-wrap"><div class="vw-cover"><div class="vw-spot" aria-hidden="true"></div>'+vwCover(b,'vw-cv')+'<div class="vw-floor" aria-hidden="true"></div></div>'
      +'<div class="vw-tx">'+vwText(b)+'</div></div>'
      +'<p class="vw-hint" aria-hidden="true">'+esc(hint)+'</p>';''', '''  var body='<div class="vw-wrap"><div class="vw-cover"><div class="vw-spot" aria-hidden="true"></div>'+vwCover(b)+'<div class="vw-floor" aria-hidden="true"></div></div>'
      +'<div class="vw-tx">'+vwText(b)+'</div></div>'
      +'<p class="vw-hint" aria-hidden="true">'+esc(hint)+'</p>';''')
rep('''    var vz=VW.v==='A'?Math.min(1,W/1440,H/840):Math.min(1,W/1440), Hz=H/vz;''', '''    var vz=Math.min(1,W/1440), Hz=H/vz;''')
rep('''  if(MODE.narrow) fitHl(h,null,0);
  else if(VW.v==='A') fitHl(h,el.querySelector('.htext'),el.querySelector('.vw-stage').offsetHeight*.9);
  else fitHl(h,el.querySelector('.vw-tx'),el.querySelector('.vw-box').offsetHeight-112);''', '''  if(MODE.narrow) fitHl(h,null,0);
  else fitHl(h,el.querySelector('.vw-tx'),el.querySelector('.vw-box').offsetHeight-112);''')
rep('''  var keep='.hcover,.vw-cv,.htext,.vw-tx,.vw-step,.vw-x';''', '''  var keep='.vw-cv,.vw-tx,.vw-step,.vw-x';''')
rep('''document.addEventListener('vw-variant',function(){ var b=VW.id&&byId(VW.id); if(b) vwRender(b,false); });
''', '')

import re
for gone in [r'\bvw-[ab]\b', r'VW\.v\b', 'data-vw', 'vw-cord', 'vw-stage', 'vwVariant', 'vw-variant']:
    assert not re.search(gone, s), gone
open(OUT, 'w', encoding='utf-8').write(s)
print('wrote', OUT, len(s))
