"""Make this iteration's src.html from the adopted page (cover_design/library_night/src.html is not changed).

Two separate changes, applied in order so either can be taken alone:
  1. headline fit (a defect fix): long headlines no longer push the kicker, the date and the buttons out of the
     hero. The hero headline steps down 36 -> 30 -> 26 -> 24px until the text column fits, and is cut with an
     ellipsis only when even 24px does not fit.
  2. issue viewer (the design change): a rack cover or a timeline day opens that issue over the page,
     laid out like today's issue. Variant A keeps the lamp and stand; variant B shows a larger cover without them.
     The variant is read from <html data-vw="A|B"> (A when absent).
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = '/home/claude/cover_design/library_night/src.html'
s = open(SRC, encoding='utf-8').read()


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:80])
    s = s.replace(old, new)


# ---------------------------------------------------------------- 1. headline fit
rep('''function fitHeadline(){
  var h=$('.hl:not(.note)'); if(!h) return;
  h.classList.remove('sm');
  var lh=parseFloat(getComputedStyle(h).lineHeight)||1;
  if(Math.round(h.offsetHeight/lh)>=(MODE.narrow?6:4)) h.classList.add('sm');
}''', '''function fitHeadline(){
  var h=$('.hero .hl:not(.note)'); if(!h) return;
  if(MODE.narrow) fitHl(h,null,0);
  else fitHl(h,$('.hero .htext'),$('.hero').offsetHeight*.9);
}
/* headline size. The usual rule stays: 44px, or 36px from four lines (24px from six lines when narrow).
   When a column and a limit are given, a long headline then steps down until the column fits the limit
   (the column stays centred on the cover, so it may use the room above and below it), and only when even
   24px does not fit are the last lines cut with an ellipsis; the full text is then kept in the title. */
function fitHl(h,col,lim){
  h.classList.remove('sm','clamp'); h.style.fontSize=''; h.style.webkitLineClamp=''; h.removeAttribute('title');
  var lh=parseFloat(getComputedStyle(h).lineHeight)||1;
  if(Math.round(h.offsetHeight/lh)>=(MODE.narrow?6:4)) h.classList.add('sm');
  if(!col||!lim) return;
  var keep=col.style.height; col.style.height='auto';
  var cur=h.classList.contains('sm')?36:44, steps=[36,30,26,24].filter(function(x){return x<cur;}), i=0;
  while(col.offsetHeight>lim+.5&&i<steps.length) h.style.fontSize=steps[i++]+'px';
  if(col.offsetHeight>lim+.5){
    lh=parseFloat(getComputedStyle(h).lineHeight)||1;
    h.style.webkitLineClamp=String(Math.max(2,Math.floor((lim-(col.offsetHeight-h.offsetHeight))/lh)));
    h.classList.add('clamp'); h.title=h.textContent;
  }
  col.style.height=keep; if(!col.getAttribute('style')) col.removeAttribute('style');
}''')
rep('''.hl.note{font-size:32px;font-weight:700}
''', '''.hl.note{font-size:32px;font-weight:700}
.hl.clamp{display:-webkit-box;-webkit-box-orient:vertical;overflow:hidden}
''')

# ---------------------------------------------------------------- 2. issue viewer: styles
VW_CSS = r'''
/* ===== issue viewer: a past issue opened over the page, laid out like today's issue =====
   Desktop: a 1440-wide box scaled with zoom to the window, over a dark veil. A keeps the lamp and stand of
   today's issue (cover 400px); B drops them for a larger cover (360-520px, from the window height).
   Narrow: a full-screen sheet with a title bar and the previous/next buttons at the bottom. */
html.vw-lock{overflow:hidden}
.vw{position:fixed;inset:0;z-index:200;display:flex;align-items:center;justify-content:center;overflow:hidden;
  --glow:color-mix(in srgb,var(--accent) 16%,transparent);--wash:color-mix(in srgb,var(--accent) 12%,transparent);--accent-line:color-mix(in srgb,var(--accent) 45%,transparent)}
.vw[hidden]{display:none}
.vw-veil{position:absolute;inset:0;background:rgba(8,9,12,.9);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.vw-box{position:relative;flex:none;width:1440px;height:var(--vh,840px);zoom:var(--vz,1);overflow:hidden}
.vw-box:focus,.vw-box:focus-visible{outline:none}
@keyframes vwFade{from{opacity:0}to{opacity:1}}
@keyframes vwRise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.vw-veil{animation:vwFade 200ms ease-out both}
.vw:not(.still) .vw-box{animation:vwRise 260ms ease-out both}
.vw.still .vw-stage,.vw.still .vw-wrap{animation:vwFade 180ms ease-out both}
.vw.still .halo,.vw.still .beam,.vw.still .lamp .bulb,.vw.still .pool{animation:none}
.vw-name{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.vw-bar,.vw-navs{display:contents}
.vw-go{display:none}
.vw-x{position:absolute;right:20px;top:20px;z-index:10;display:flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:50%;color:var(--t1);background:color-mix(in srgb,var(--s1) 85%,transparent);box-shadow:inset 0 0 0 1px var(--line-strong);transition:background-color var(--ease),box-shadow var(--ease)}
.vw-x:hover{background:var(--s2);box-shadow:inset 0 0 0 1px var(--t3)}
.vw-step{position:absolute;top:50%;z-index:10;display:flex;flex-direction:column;align-items:center;gap:8px;width:72px;margin-top:-24px;color:var(--t2);cursor:pointer}
.vw-step.prev{left:4px}
.vw-step.next{right:4px}
.vw-step .o{display:flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:50%;color:var(--t1);background:color-mix(in srgb,var(--s1) 85%,transparent);box-shadow:inset 0 0 0 1px var(--line-strong);transition:background-color var(--ease),box-shadow var(--ease)}
.vw-step .t{font:var(--ty-caption);color:var(--t2);white-space:nowrap}
.vw-step .d{margin-top:-4px;font:var(--ty-data-s);color:var(--t3);white-space:nowrap;text-align:center}
.vw-step .d b{display:block;margin-top:2px;font:inherit}
.vw-step:hover .o{background:var(--s2);box-shadow:inset 0 0 0 1px var(--t3)}
.vw-step:hover .t{color:var(--t1)}
.vw-step:disabled{opacity:.32;cursor:default}
.vw-step:disabled:hover .o{background:color-mix(in srgb,var(--s1) 85%,transparent);box-shadow:inset 0 0 0 1px var(--line-strong)}
.vw-step:focus-visible{outline:none}
.vw-step:focus-visible .o{outline:2px solid var(--accent);outline-offset:3px}
/* A: today's issue as it is (the text column is 40px narrower than the hero's, to clear the arrow) */
.vw-a .htext{width:600px}
.vw-a .vw-stage{position:absolute;left:64px;top:calc((var(--vh,840px) - var(--hero-h)) / 2);width:var(--content);height:var(--hero-h)}
.vw-cord{position:absolute;left:320px;bottom:100%;width:1px;height:1200px;background:var(--line-strong)}
/* B: a larger cover without the lamp */
.vw-b .vw-wrap{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:72px}
.vw-b .vw-cover{position:relative;flex:none;width:var(--vcw,480px)}
.vw-b .vw-spot{position:absolute;left:50%;top:46%;width:230%;height:150%;transform:translate(-50%,-50%);background:radial-gradient(closest-side,var(--glow),transparent);pointer-events:none}
.vw-b .vw-floor{position:absolute;left:-14%;right:-14%;top:100%;height:64px;margin-top:-8px;background:radial-gradient(closest-side,rgba(var(--lamp-rgb),.07),rgba(var(--lamp-rgb),0));pointer-events:none}
.vw-b .vw-cv{position:relative;z-index:2;display:block;box-shadow:var(--sh-cover-hero)}
.vw-b .vw-tx{position:relative;z-index:2;flex:none;width:600px}
.vw-b .vw-hint{position:absolute;left:0;right:0;bottom:22px;text-align:center;font:var(--ty-small);color:var(--t3)}
@media (max-width:1279px){
  .vw{display:block;background:var(--bg)}
  .vw-veil{display:none}
  .vw-box{position:absolute;inset:0;width:auto;height:auto;zoom:1;overflow-x:hidden;overflow-y:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;padding-top:env(safe-area-inset-top,0px);padding-bottom:calc(104px + env(safe-area-inset-bottom,0px))}
  .vw:not(.still) .vw-box{animation-name:vwFade}
  .vw-bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;display:flex;align-items:center;gap:12px;height:56px;padding:0 20px 0 32px;background:color-mix(in srgb,var(--bg) 94%,transparent);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);box-shadow:inset 0 -1px 0 var(--line-subtle)}
  .vw-name{position:static;width:auto;height:auto;min-width:0;clip-path:none;text-overflow:ellipsis;font:700 15px/1.3 var(--f-sans);color:var(--t1)}
  .vw-x{position:static;flex:none;margin-left:auto;width:40px;height:40px;border-radius:var(--r-button);background:none;box-shadow:none}
  .vw-x:hover{background:var(--s2);box-shadow:none}
  .vw-a .vw-stage{position:relative;left:auto;top:auto;width:auto;height:auto;margin:0;padding:24px 32px 0;overflow:hidden}
  .vw-cord,.vw-hint{display:none}
  .vw-b .vw-wrap{position:static;display:block;padding:32px 32px 0;overflow:hidden}
  .vw-b .vw-cover{margin:0 auto}
  .vw-b .vw-tx{width:auto;margin-top:40px}
  .vw-navs{position:fixed;left:0;right:0;bottom:0;z-index:20;display:flex;gap:8px;padding:12px max(32px,env(safe-area-inset-right,0px)) calc(12px + env(safe-area-inset-bottom,0px)) max(32px,env(safe-area-inset-left,0px));background:color-mix(in srgb,var(--bg) 96%,transparent);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);box-shadow:inset 0 1px 0 var(--line-subtle)}
  .vw .acts{display:none}
  .vw-a .htext{width:auto}
  .vw-go{display:inline-flex;flex:1 1 auto;min-width:0;height:48px;padding:0 16px}
  .vw-step{position:static;flex:0 0 auto;min-width:0;flex-direction:row;justify-content:center;gap:6px;width:auto;height:48px;margin:0;padding:0 14px;border-radius:var(--r-button);box-shadow:inset 0 0 0 1px var(--line-strong);transition:background-color var(--ease)}
  .vw-step .o,.vw-step:hover .o,.vw-step:disabled:hover .o{width:auto;height:auto;background:none;box-shadow:none}
  .vw-step .t,.vw-step .d b{display:none}
  .vw-step .d{margin-top:0;font:var(--ty-data-m);color:var(--t2)}
  .vw-step.next .o{order:3}
  .vw-step:hover{background:var(--s2)}
  .vw-step:disabled:hover{background:none}
  .vw-step:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .vw-step:focus-visible .o{outline:none}
}
@media (max-width:699px){
  .vw-bar{padding:0 8px 0 16px}
  .vw-a .vw-stage{padding-left:16px;padding-right:16px}
  .vw-b .vw-wrap{padding:24px 16px 0}
  .vw-b .vw-tx{margin-top:32px}
  .vw-navs{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
}
'''
rep('''
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}''', VW_CSS + '''
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .vw-veil,.vw .vw-box,.vw .vw-stage,.vw .vw-wrap{animation:none}''')

# ---------------------------------------------------------------- 2. issue viewer: markup helpers
rep('''function coverLabel(b){''', '''function coverLabel(b,act){''')
rep('''  s.push(hlOf(b).t); s.push('브리핑 열기');''', '''  s.push(hlOf(b).t); s.push(act||'브리핑 열기');''')
rep('''  close20:ic('<path d="M5 5l10 10M15 5L5 15"/>',20,20,1.5),''', '''  close20:ic('<path d="M5 5l10 10M15 5L5 15"/>',20,20,1.5),
  left20:ic('<path d="M12.5 4.5L7 10l5.5 5.5"/>',20,20,1.5),
  right20:ic('<path d="M7.5 4.5L13 10l-5.5 5.5"/>',20,20,1.5),''')

# hero(): same output, built from parts the viewer shares
HERO_OLD = s[s.index('function hero(){'):s.index('function heroEmpty(){')]
assert s.count(HERO_OLD) == 1
HERO_NEW = r'''function kickOf(b){
  return (b===L?(b.date===kstNow().date?'오늘의 호':'최신 호'):'지난 호')+' · 제'+vol(b)+'호'+(multi(b)?' · '+b.seq+'회차':'');
}
function datelineHTML(b){
  var r=run(b);
  return '<p class="dateline"><span class="dd">'+b.date.replace(/-/g,'.')+'</span><span class="dw">'+wdF(b.date)+(r?' · '+esc(r):'')+'</span></p>';
}
function hlHTML(b,tg,idA){
  var h=hlOf(b), o='<'+tg+(idA?' id="'+idA+'"':'')+' class="hl';
  if(!b.headline) return o+' note">'+(h.memo?tag('메모',true):'')+esc(h.t)+'</'+tg+'>';
  var i=b.headline.indexOf(', ');
  return i<0?o+'">'+esc(b.headline)+'</'+tg+'>'
        :o+'"><span class="l1">'+esc(b.headline.slice(0,i+1))+'</span><br><span class="l2">'+esc(b.headline.slice(i+2))+'</span></'+tg+'>';
}
function phlHTML(b){
  return '<div class="phl">'+badge(b.phase,MODE.narrow?'m':'l')+'<span class="phn">'+esc(phName(b.phase))+'</span>'
    +(b.provisional?tag('임시 기준'):'')
    +(b.prevPhase?'<span class="pv"><span class="vr" aria-hidden="true"></span><span class="prv">전날 국면</span>'+badge(b.prevPhase,'s')+'</span>':'')
    +'</div>';
}
function figsHTML(b){
  var ch=btcdChange(b);
  function fig(lb,v,chg,bs){
    return '<div class="fig"><span class="lb">'+mk(lb)+'</span>'
      +'<span class="v'+(v==null?' none':'')+'">'+(v==null?'—':v)+'</span>'
      +'<span class="ch">'+(chg==null?'':mk(chg))+'</span>'
      +'<span class="bs">'+(bs?esc(bs):'')+'</span></div>';
  }
  return '<div class="figs">'
    +fig('BTC.D', b.btcd==null?null:b.btcd.toFixed(2)+'%', b.btcd==null?'기록 없음':ch, '')
    +fig('ΣSTABLECOIN.D', b.stableD==null?null:b.stableD.toFixed(3)+'%', b.stable1m==null?'기록 없음':'1개월 '+sgnS(b.stable1m,3)+'%p', 'E 임시 기준 +1.0%p')
    +fig('BTCUSD 1개월', b.btc1m==null?null:sgnS(b.btc1m,2)+'%', b.btc1m==null?'기록 없음':'', '0 아래여야 D·E 판정 전제')
    +'</div>';
}
function briefBtn(b,cls){
  var c='btn btn-pri'+(cls?' '+cls:'');
  return b.url?'<a class="'+c+'"'+ext(b.url)+'>브리핑 펼치기'+IC.right+'</a>':'<span class="'+c+' off" aria-disabled="true">브리핑 펼치기'+IC.right+'</span>';
}
function hero(){
  var b=L;
  var acts='<div class="acts">'+briefBtn(b)+'<a class="btn btn-sec" href="#rack">지난 호 넘겨 보기'+IC.down+'</a></div>';
  var coverEl=b.url?'<a class="hcover"'+ext(b.url)+' aria-label="'+esc(coverLabel(b))+'">':'<div class="hcover" role="img" aria-label="'+esc(coverLabel(b))+'">';
  return '<section class="hero" id="today" aria-label="오늘 호"><div class="stage"><div class="art">'
    +'<div class="halo" aria-hidden="true"></div>'
    +'<div class="beam" aria-hidden="true"><i></i></div>'
    +LAMP
    +coverEl+'<div class="cv" aria-hidden="true">'+cover(b)+'</div>'+(b.url?'</a>':'</div>')
    +'<div class="stand" aria-hidden="true"></div>'
    +'<div class="pool" aria-hidden="true"></div>'
    +'<p class="stand-cap">'+esc(nextCaption())+'</p></div>'
    +'<div class="htext">'
      +'<p class="kicker">'+esc(kickOf(b))+'</p>'
      +datelineHTML(b)
      +hlHTML(b,'h1')+phlHTML(b)+figsHTML(b)+acts
    +'</div>'
  +'</div></section>';
}
'''
rep(HERO_OLD, HERO_NEW)

# timeline days and rack covers carry the issue id; their labels say they open the viewer
rep('''    return b.url?'<a class="'+cls+'"'+ext(b.url)+' tabindex="'+(lat?0:-1)+'" aria-label="'+esc(lab)+'" data-t1=''',
    '''    return b.url?'<a class="'+cls+'"'+ext(b.url)+' data-id="'+esc(b.id)+'" tabindex="'+(lat?0:-1)+'" aria-label="'+esc(lab+', 표지 크게 보기')+'" data-t1=''')
rep('''  return '<'+t+' class="slot"'+(b.url?ext(b.url):' role="img"')+' aria-label="'+esc(coverLabel(b))+'"><span class="sglow" aria-hidden="true"></span>\'''',
    '''  return '<'+t+' class="slot"'+(b.url?ext(b.url)+' data-id="'+esc(b.id)+'"':' role="img"')+' aria-label="'+esc(coverLabel(b,b.url?'표지 크게 보기':''))+'"><span class="sglow" aria-hidden="true"></span>\'''')
rep('''<p class="guide">표지를 누르면 그날 브리핑이 열립니다.</p>''', '''<p class="guide">표지를 누르면 그 호를 크게 펼쳐 봅니다.</p>''')

# ---------------------------------------------------------------- 2. issue viewer: behaviour
VW_JS = r'''/* ================= issue viewer ================= */
/* A rack cover or a timeline day opens that issue over the page. A click with a modifier key, or the middle
   button, still follows the link and opens the brief. Esc, the close button or a click beside the issue closes
   it; the arrow buttons and the left/right keys move to the previous or next issue in publishing order. */
var VW={id:null,opener:null,el:null,v:'A',down:null};
function byId(id){for(var i=0;i<B.length;i++) if(B[i].id===id) return B[i]; return null;}
function vwVariant(){return document.documentElement.getAttribute('data-vw')==='B'?'B':'A';}
function vwName(b){var p=ymd(b.date); return '제'+vol(b)+'호'+(multi(b)?' '+b.seq+'회차':'')+' · '+p.m+'월 '+p.d+'일 '+wdF(b.date);}
function vwCover(b,cls){
  var inner='<div class="cv" aria-hidden="true">'+cover(b)+'</div>';
  return b.url?'<a class="'+cls+'"'+ext(b.url)+' aria-label="'+esc(coverLabel(b))+'">'+inner+'</a>'
    :'<div class="'+cls+'" role="img" aria-label="'+esc(coverLabel(b))+'">'+inner+'</div>';
}
function vwText(b){
  return '<p class="kicker">'+esc(kickOf(b))+'</p>'+datelineHTML(b)
    +hlHTML(b,'h2','vw-title')+phlHTML(b)+figsHTML(b)
    +'<div class="acts">'+briefBtn(b)+'<button type="button" class="btn btn-sec" data-act="close">닫기</button></div>';
}
function vwStepBtn(b,d){
  var cls='vw-step '+(d<0?'prev':'next'), t=d<0?'이전 호':'다음 호', o='<span class="o">'+(d<0?IC.left20:IC.right20)+'</span>';
  if(!b) return '<button type="button" class="'+cls+'" disabled>'+o+'<span class="t">'+t+'</span><span class="d">없음</span></button>';
  return '<button type="button" class="'+cls+'" data-act="'+(d<0?'prev':'next')+'" aria-label="'+esc(t+', '+vwName(b))+'">'
    +o+'<span class="t">'+t+'</span><span class="d">'+mdot(b.date)+(multi(b)?'<b> '+b.seq+'회차</b>':'')+'</span></button>';
}
function vwEnsure(){
  if(VW.el) return VW.el;
  var el=document.createElement('div');
  el.className='vw'; el.hidden=true;
  el.setAttribute('role','dialog'); el.setAttribute('aria-modal','true'); el.setAttribute('aria-labelledby','vw-name');
  el.innerHTML='<div class="vw-veil" aria-hidden="true"></div><div class="vw-box" tabindex="-1"></div><div class="sr" id="vw-live" aria-live="polite"></div>';
  el.addEventListener('mousedown',function(e){VW.down=e.target;});
  el.addEventListener('click',vwClick);
  document.body.appendChild(el);
  VW.el=el; return el;
}
function vwRender(b,first){
  var el=vwEnsure(), v=vwVariant(), i=B.indexOf(b), box=el.querySelector('.vw-box');
  VW.id=b.id; VW.v=v;
  el.className='vw vw-'+v.toLowerCase()+(first?'':' still');
  var fr=null; try{var p=pal(b); fr=p&&p.fr;}catch(e){fr=null;}
  el.style.setProperty('--accent',accentFrom(fr));
  var hint='← → 키로 앞뒤 호를 넘겨 봅니다';
  var body=v==='A'
    ?'<div class="vw-stage"><div class="art">'
        +'<i class="vw-cord" aria-hidden="true"></i>'
        +'<div class="halo" aria-hidden="true"></div><div class="beam" aria-hidden="true"><i></i></div>'+LAMP
        +vwCover(b,'hcover')
        +'<div class="stand" aria-hidden="true"></div><div class="pool" aria-hidden="true"></div>'
        +'<p class="stand-cap vw-hint" aria-hidden="true">'+esc(hint)+'</p></div>'
      +'<div class="htext">'+vwText(b)+'</div></div>'
    :'<div class="vw-wrap"><div class="vw-cover"><div class="vw-spot" aria-hidden="true"></div>'+vwCover(b,'vw-cv')+'<div class="vw-floor" aria-hidden="true"></div></div>'
      +'<div class="vw-tx">'+vwText(b)+'</div></div>'
      +'<p class="vw-hint" aria-hidden="true">'+esc(hint)+'</p>';
  box.innerHTML='<div class="vw-bar"><p class="vw-name" id="vw-name">'+esc(vwName(b))+'</p>'
      +'<button type="button" class="vw-x" data-act="close" aria-label="닫기">'+IC.close20+'</button></div>'
    +body
    +'<div class="vw-navs">'+vwStepBtn(i>0?B[i-1]:null,-1)+briefBtn(b,'vw-go')+vwStepBtn(i<B.length-1?B[i+1]:null,1)+'</div>';
  box.scrollTop=0;
  vwLayout();
}
function vwLayout(){
  var el=VW.el; if(!el||!VW.id) return;
  var W=el.clientWidth||window.innerWidth, H=el.clientHeight||window.innerHeight;
  if(MODE.narrow){
    el.style.setProperty('--vz','1'); el.style.removeProperty('--vh');
    el.style.setProperty('--vcw',Math.floor(Math.min(W-(W>=700?64:32),420,Math.max(240,(H-184)*.68)))+'px');
  }else{
    var vz=VW.v==='A'?Math.min(1,W/1440,H/840):Math.min(1,W/1440), Hz=H/vz;
    el.style.setProperty('--vz',String(vz));
    el.style.setProperty('--vh',Hz.toFixed(1)+'px');
    el.style.setProperty('--vcw',Math.round(Math.max(360,Math.min(520,(Hz-112)*.68)))+'px');
  }
  BK.fit(el,true);
  var h=el.querySelector('.hl:not(.note)'); if(!h) return;
  if(MODE.narrow) fitHl(h,null,0);
  else if(VW.v==='A') fitHl(h,el.querySelector('.htext'),el.querySelector('.vw-stage').offsetHeight*.9);
  else fitHl(h,el.querySelector('.vw-tx'),el.querySelector('.vw-box').offsetHeight-112);
}
function vwOpen(b,opener){
  var el=vwEnsure(), first=!VW.id;
  if(first){
    VW.opener=opener||null;
    if(tip) tip.hidden=true;
    closePanels(); if(qres) qres.hidden=true;
    var sb=window.innerWidth-document.documentElement.clientWidth;
    document.documentElement.classList.add('vw-lock');
    if(sb>0) document.documentElement.style.paddingRight=sb+'px';
    app.inert=true; el.hidden=false;
  }
  vwRender(b,first);
  el.querySelector('.vw-box').focus({preventScroll:true});
}
function vwClose(){
  if(!VW.id) return;
  var id=VW.id, op=VW.opener;
  VW.id=null; VW.opener=null;
  VW.el.hidden=true; VW.el.querySelector('.vw-box').innerHTML=''; VW.el.querySelector('#vw-live').textContent='';
  document.documentElement.classList.remove('vw-lock');
  document.documentElement.style.paddingRight='';
  app.inert=false;
  if(computeMode().key!==MODE.key) render();
  if(!op||!app.contains(op)) op=$('[data-id="'+id+'"]',app);
  if(op) op.focus({preventScroll:true});
}
function vwStep(d){
  var b=byId(VW.id), n=b&&B[B.indexOf(b)+d]; if(!n) return;
  var onStep=document.activeElement&&document.activeElement.closest&&document.activeElement.closest('.vw-step');
  vwRender(n,false);
  var f=onStep&&VW.el.querySelector('.vw-step.'+(d<0?'prev':'next')+':not([disabled])');
  (f||VW.el.querySelector('.vw-box')).focus({preventScroll:true});
  VW.el.querySelector('#vw-live').textContent=vwName(n)+', '+phSpoken(n.phase);
}
function vwClick(e){
  var c=e.target.closest('[data-act]');
  if(c&&VW.el.contains(c)){
    var a=c.getAttribute('data-act');
    if(a==='close') vwClose(); else if(a==='prev') vwStep(-1); else if(a==='next') vwStep(1);
    return;
  }
  if(MODE.narrow) return;
  var keep='.hcover,.vw-cv,.htext,.vw-tx,.vw-step,.vw-x';
  if(!e.target.closest(keep)&&!(VW.down&&VW.down.closest&&VW.down.closest(keep))) vwClose();
}
function vwKey(e){
  if(e.key==='Escape'){e.preventDefault(); vwClose(); return;}
  if((e.key==='ArrowLeft'||e.key==='ArrowRight')&&!e.altKey&&!e.metaKey&&!e.ctrlKey&&!e.shiftKey){e.preventDefault(); vwStep(e.key==='ArrowLeft'?-1:1); return;}
  if(e.key==='Tab'){
    var f=$$('a[href],button:not([disabled])',VW.el).filter(function(x){return x.getClientRects().length>0;});
    if(!f.length) return;
    var i=f.indexOf(document.activeElement);
    if(e.shiftKey&&i<=0){e.preventDefault(); f[f.length-1].focus();}
    else if(!e.shiftKey&&(i<0||i===f.length-1)){e.preventDefault(); f[0].focus();}
  }
}
function vwFromLink(e){
  if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey) return;
  var a=e.target.closest('[data-id]'); if(!a||!e.currentTarget.contains(a)) return;
  var b=byId(a.getAttribute('data-id')); if(!b) return;
  e.preventDefault(); vwOpen(b,a);
}
function vwSync(){
  if(!VW.id) return;
  var b=byId(VW.id); if(!b){vwClose(); return;}
  var had=VW.el.contains(document.activeElement);
  vwRender(b,false);
  if(had) VW.el.querySelector('.vw-box').focus({preventScroll:true});
}

'''
rep('''/* ================= render ================= */''', VW_JS + '''/* ================= render ================= */''')
rep('''  BK.fit(app);
  fitHeadline();
}''', '''  BK.fit(app);
  fitHeadline();
  vwSync();
}''')
rep('''  /* metrics table */''', '''  /* rack covers and timeline days open the issue viewer */
  [$('#rack'),tl].forEach(function(el){ if(el) el.addEventListener('click',vwFromLink); });
  /* metrics table */''')
rep('''document.addEventListener('keydown',function(e){
  if(e.key==='/'&&q''', '''document.addEventListener('keydown',function(e){
  if(VW.id){vwKey(e); return;}
  if(e.key==='/'&&q''')
rep('''var rt=null;
window.addEventListener('resize',function(){''', '''var vt=null;
window.addEventListener('resize',function(){ if(!VW.id) return; clearTimeout(vt); vt=setTimeout(vwLayout,170); });
document.addEventListener('vw-variant',function(){ var b=VW.id&&byId(VW.id); if(b) vwRender(b,false); });
var rt=null;
window.addEventListener('resize',function(){''')

open(os.path.join(HERE, 'src.html'), 'w', encoding='utf-8').write(s)
print('src.html', len(s))
