  /* Magazine covers for daily briefs. The frame stays the same on every issue (border, masthead, three
     cover lines, bottom strip) so the shelf reads as one publication. Inside it each issue gets its own
     colour scheme and hue, the day's headline in a kicker-lead-main hierarchy, and one of about forty
     pictures chosen from what the headline talks about and which indicators the brief recorded. */
  var BK=(function(){
  var PHN={A:'BTC!',B:'알트시즌?',C:'선별적',D:'STICKY BTC.D',E:'튀어?'};
  var WDK=['일','월','화','수','목','금','토'];
  var UID=0, FL=124;

  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function n1(x){return Math.round(x*100)/100;}
  function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
  function f2(v,d){return v==null?'–':v.toFixed(d);}
  function sgn(v,d){if(v==null) return '–'; var s=Math.abs(v).toFixed(d); return (Number(s)===0?'':(v>0?'+':'−'))+s;}
  function chg(v,d,unit){if(v==null) return ''; return Number(Math.abs(v).toFixed(d))===0?'전날과 같음':'전날 '+sgn(v,d)+unit;}
  function dnum(d){var a=d.split('-').map(Number); return Math.round(Date.UTC(a[0],a[1]-1,a[2])/864e5);}
  function parts(p){if(!p) return []; return String(p).split(/→|->|>/).map(function(s){return s.trim().toUpperCase();}).filter(function(s){return /^[A-E]$/.test(s);});}
  function hash(s){var h=2166136261>>>0; for(var i=0;i<s.length;i++){h^=s.charCodeAt(i); h=Math.imul(h,16777619)>>>0;} return h;}
  function rng(seed){var a=seed>>>0; return function(){a=(a+0x6D2B79F5)>>>0; var t=a; t=Math.imul(t^(t>>>15),t|1); t^=t+Math.imul(t^(t>>>7),t|61); return ((t^(t>>>14))>>>0)/4294967296;};}
  function mixc(a,b,t){var x=parseInt(a.slice(1),16), y=parseInt(b.slice(1),16); var r=Math.round((x>>16)*(1-t)+(y>>16)*t), g=Math.round(((x>>8)&255)*(1-t)+((y>>8)&255)*t), bl=Math.round((x&255)*(1-t)+(y&255)*t); return '#'+((1<<24)+(r<<16)+(g<<8)+bl).toString(16).slice(1).toUpperCase();}
  function vars(o){var s=''; for(var k in o){s+='--'+k+':'+o[k]+';';} return s;}

  /* ---- colour: OKLCH to sRGB, chroma lowered until the colour fits the sRGB gamut ---- */
  function toS(x){return x<=0.0031308?12.92*x:1.055*Math.pow(x,1/2.4)-0.055;}
  function toLin(x){return x<=0.04045?x/12.92:Math.pow((x+0.055)/1.055,2.4);}
  function okRGB(L,C,h){
    var hr=h*Math.PI/180, a=C*Math.cos(hr), b=C*Math.sin(hr);
    var l_=L+0.3963377774*a+0.2158037573*b, m_=L-0.1055613458*a-0.0638541728*b, s_=L-0.0894841775*a-1.2914855480*b;
    var l=l_*l_*l_, m=m_*m_*m_, s=s_*s_*s_;
    return [4.0767416621*l-3.3077115913*m+0.2309699292*s, -1.2684380046*l+2.6097574011*m-0.3413193965*s, -0.0041960863*l-0.7034186147*m+1.7076147010*s];
  }
  function hex3(c){return '#'+c.map(function(v){var x=Math.round(clamp(toS(clamp(v,0,1)),0,1)*255); return (x<16?'0':'')+x.toString(16);}).join('').toUpperCase();}
  function inG(c){return c[0]>=-1e-4&&c[0]<=1.0001&&c[1]>=-1e-4&&c[1]<=1.0001&&c[2]>=-1e-4&&c[2]<=1.0001;}
  function ok(L,C,h){
    h=((h%360)+360)%360; L=clamp(L,0,1);
    for(var i=0;i<60;i++){var c=okRGB(L,C,h); if(inG(c)) return hex3(c); C*=0.93;}
    return hex3(okRGB(L,0,h));
  }
  function lum(hx){var v=parseInt(hx.slice(1),16); return 0.2126*toLin((v>>16)/255)+0.7152*toLin(((v>>8)&255)/255)+0.0722*toLin((v&255)/255);}
  function cr(a,b){var x=lum(a), y=lum(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05);}
  /* move lightness away from the ground until text on it reaches the contrast `min` */
  function readable(t,bg,min){
    var up=lum(bg)<0.2, L=t[0], c=ok(L,t[1],t[2]);
    for(var i=0;i<60 && cr(c,bg)<min;i++){ L=up?Math.min(1,L+0.02):Math.max(0,L-0.02); c=ok(L,t[1],t[2]); }
    return c;
  }
  /* twelve schemes. Each role is [L, C, hue offset from the issue hue] or [L, C, 0, fixed hue].
     bg: cover ground, ink: text and figures, fr: frame and masthead block, c1-c3: picture colours
     (c3 is the one piece the data points at, and the phase mark). hl:'fr' sets the main headline in the frame colour. */
  var SCH=[
    {n:'보색 라이트', bg:[.955,.028,0], ink:[.22,.04,0], fr:[.63,.17,180], c1:[.57,.14,0], c2:[.80,.09,25], c3:[.66,.19,180]},
    {n:'딥 드라마', dk:1, bg:[.27,.075,0], ink:[.97,.012,0], fr:[.84,.14,165], c1:[.56,.12,0], c2:[.74,.08,0], c3:[.86,.15,165], hl:'fr'},
    {n:'파스텔 삼색', bg:[.92,.05,0], ink:[.27,.06,240], fr:[.66,.15,120], c1:[.74,.11,240], c2:[.80,.09,60], c3:[.62,.17,120]},
    {n:'무채색과 포인트', bg:[.94,.006,0], ink:[.19,.01,0], fr:[.63,.19,0], c1:[.78,.012,0], c2:[.64,.014,0], c3:[.62,.19,0]},
    {n:'유사색', bg:[.93,.045,0], ink:[.24,.06,0], fr:[.56,.16,35], c1:[.66,.14,15], c2:[.78,.11,-20], c3:[.55,.18,55]},
    {n:'강한 바탕', bg:[.74,.14,0], ink:[.17,.03,180], fr:[.30,.07,180], c1:[.38,.10,180], c2:[.95,.025,0], c3:[.93,.11,60]},
    {n:'네온 나이트', dk:1, bg:[.19,.025,0], ink:[.98,0,0], fr:[.87,.19,100], c1:[.66,.17,100], c2:[.58,.19,280], c3:[.88,.20,100]},
    {n:'크림 인쇄', bg:[.945,.03,0,88], ink:[.22,.025,0,60], fr:[.52,.14,0], c1:[.57,.09,0], c2:[.73,.06,180], c3:[.60,.15,180]},
    {n:'밝은 삼색', bg:[.965,.015,0], ink:[.2,.03,0], fr:[.62,.17,120], c1:[.63,.16,0], c2:[.72,.15,240], c3:[.60,.19,120]},
    {n:'단색조', bg:[.89,.065,0], ink:[.2,.05,0], fr:[.44,.14,0], c1:[.6,.12,0], c2:[.73,.1,0], c3:[.34,.12,0]},
    {n:'한밤 금박', dk:1, bg:[.24,.06,0], ink:[.96,.02,0,85], fr:[.80,.14,0,85], c1:[.52,.10,0], c2:[.68,.07,0], c3:[.85,.15,0,85], hl:'fr'},
    {n:'블러시', bg:[.93,.04,0], ink:[.26,.08,0], fr:[.40,.13,0], c1:[.54,.15,0], c2:[.82,.07,0], c3:[.62,.16,200]}
  ];
  var DARKS=[1,6,10];
  /* one pass through all twelve schemes every twelve days, dark ones spread out (every fourth day) */
  var CYC=[0,5,1,8,3,2,6,9,7,4,10,11];
  function palette(si,H){
    var S=SCH[si], o={si:si, name:S.n, dark:!!S.dk, H:Math.round(H)}, R={};
    ['bg','ink','fr','c1','c2','c3'].forEach(function(k){
      var r=S[k], h=((((r.length>3?r[3]:H+r[2])%360)+360)%360), L=r[0], C=r[1];
      /* yellows go olive when they are dark: lift the bright picture colours near hue 100 */
      var dy=Math.abs(((h-100)%360+540)%360-180);
      if(k!=='bg'&&k!=='ink'&&C>=0.08&&L>=0.5&&dy<28) L=Math.max(L,0.76);
      R[k]=[L,C,h]; o[k]=ok(L,C,h);
    });
    /* picture colours must stand apart from the ground: darker on light grounds, lighter on dark ones */
    var bgL=R.bg[0];
    ['c1','c2','c3'].forEach(function(k){
      var r=R[k], L=r[0], up=o.dark||(bgL<0.85&&L>bgL), min=o.dark?2.1:1.55;
      for(var i=0;i<20&&cr(o[k],o.bg)<min;i++){ L=up?Math.min(.97,L+.03):Math.max(.2,L-.03); o[k]=ok(L,r[1],r[2]); }
      R[k]=[L,r[1],r[2]];
    });
    o.acc=readable(R.c3,o.bg,4.6);
    o.hl=(S.hl==='fr'&&cr(o.fr,o.bg)>=4.6)?o.fr:o.ink;
    o.frInk=cr('#FFFFFF',o.fr)>=cr('#17181A',o.fr)?'#FFFFFF':ok(.2,.03,R.fr[2]);
    o.c3Ink=cr('#FFFFFF',o.c3)>=cr('#17181A',o.c3)?'#FFFFFF':'#17181A';
    o.c2Ink=cr('#FFFFFF',o.c2)>=cr('#17181A',o.c2)?'#FFFFFF':'#17181A';
    o.c1Ink=cr('#FFFFFF',o.c1)>=cr('#17181A',o.c1)?'#FFFFFF':'#17181A';
    /* neutrals for poles, pipes, plinths: tinted with the ground hue, placed away from the ground lightness */
    var hb=R.bg[2], NL=o.dark?[.66,.58,.5,.42]:bgL<0.85?[.93,.87,.54,.38]:[.88,.79,.65,.46];
    o.n0=ok(NL[0],.014,hb); o.n1=ok(NL[1],.016,hb); o.n2=ok(NL[2],.018,hb); o.n3=ok(NL[3],.02,hb);
    o.paper=o.dark?ok(.92,.01,hb):'#FFFFFF';
    o.shadow=o.dark?'#000000':o.ink;
    return o;
  }
  function hueOf(b){return ((dnum(b.date)*137.508+(b.seq-1)*57)%360+360)%360;}
  function pickScheme(D,recent){
    var warn=D.P==='D'||D.P==='E', i=((dnum(D.b.date)+(D.b.seq-1)*5)%12+12)%12, last=recent.slice(-2);
    for(var k=0;k<12;k++){var s=CYC[(i+k)%12]; if(warn&&DARKS.indexOf(s)<0) continue; if(last.indexOf(s)<0) return s;}
    return CYC[i];
  }
