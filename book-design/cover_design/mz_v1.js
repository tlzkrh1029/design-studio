  /* Magazine covers for daily briefs. One fixed frame for every issue (lime border, masthead,
     three cover lines, bottom strip) so the shelf reads as one publication; inside it the day's
     headline in a kicker-lead-main hierarchy and one data object drawn from the brief's own numbers. */
  var BK=(function(){
  var PHN={A:'BTC!',B:'알트시즌?',C:'선별적',D:'STICKY BTC.D',E:'튀어?'};
  var FRAME='#9BCF4E';
  /* acc: object fill, accInk: text on the cover ground, phBg/phInk: the square phase mark (same as the page's marks) */
  var PAL={
    A:{acc:'#CB8242',accInk:'#99561C',phBg:'#CB8242',phInk:'#141B0F',dark:false},
    B:{acc:'#A96CAF',accInk:'#80468A',phBg:'#A96CAF',phInk:'#141B0F',dark:false},
    C:{acc:'#1E7B2C',accInk:'#056F15',phBg:'#056F15',phInk:'#FFFFFF',dark:false},
    D:{acc:'#8E84E0',accInk:'#B3ABF2',phBg:'#594D99',phInk:'#FFFFFF',dark:true},
    E:{acc:'#4DA8FF',accInk:'#8CC7FF',phBg:'#2B97FF',phInk:'#141B0F',dark:true},
    X:{acc:'#7D7A70',accInk:'#5E5B52',phBg:'#EEF3E2',phInk:'#56614B',dark:false}
  };
  /* paper per object type (light) and the dark ground for warning phases */
  var PAPER={stairs:'#F3F0E8',tank:'#EBF0F1',coin:'#EFEEE9',type:'#F2F0EA'};
  var LIGHT={ink:'#16181A',g0:'#E4E0D5',g1:'#CFCABD',g2:'#ABA699',g3:'#8B867A',glass:'#FFFFFF'};
  var DARK={bg:'#16181E',ink:'#F3F2EE',g0:'#626874',g1:'#4E535E',g2:'#3C404A',g3:'#30343D',glass:'#FFFFFF'};
  var WDK=['일','월','화','수','목','금','토'];
  var UID=0;

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
  function mixc(a,b,t){var x=parseInt(a.slice(1),16), y=parseInt(b.slice(1),16); var r=Math.round((x>>16)*(1-t)+(y>>16)*t), g=Math.round(((x>>8)&255)*(1-t)+((y>>8)&255)*t), bl=Math.round((x&255)*(1-t)+(y&255)*t); return '#'+((1<<24)+(r<<16)+(g<<8)+bl).toString(16).slice(1);}
  function vars(o){var s=''; for(var k in o){s+='--'+k+':'+o[k]+';';} return s;}

  /* ---- data ---- */
  function prevOf(b,all){
    var p=null;
    all.forEach(function(x){ if((x.date<b.date||(x.date===b.date&&x.seq<b.seq)) && x.btcd!=null) p=x; });
    return p;
  }
  function valOf(x,key){ if(key==='alt') return (x.btcd!=null&&x.stableD!=null)?100-x.btcd-x.stableD:null; return x[key]; }
  function histOf(b,all,key,n){
    var m={}, order=[];
    all.forEach(function(x){
      var v=valOf(x,key);
      if((x.date<b.date||(x.date===b.date&&x.seq<=b.seq)) && v!=null){ if(!(x.date in m)) order.push(x.date); m[x.date]=v; }
    });
    return order.slice(-n).map(function(d){return {d:d,v:m[d]};});
  }
  /* headline: the clause after the last ', ' or ' — ' is the punchline (main), the part before it the lead */
  function split(h){
    h=String(h||'').trim(); if(!h) return {lead:'',main:''};
    var best=-1, sep='';
    [', ',' — ',' – '].forEach(function(s){var i=h.lastIndexOf(s); if(i>best && h.length-i-s.length>=6 && i>=4){best=i; sep=s;}});
    if(best<0) return {lead:'',main:h};
    return {lead:h.slice(0,best)+(sep===', '?',':''), main:h.slice(best+sep.length)};
  }
  /* numbers with a unit are the one emphasis inside a headline */
  function emph(t){return esc(t).replace(/([+−\-]?\d[\d,.]*\s?(?:%p|%|bp|달러|배))/g,'<em>$1</em>');}
  function textWidth(s){
    var w=0; for(var i=0;i<s.length;i++){var c=s.charCodeAt(i);
      if(c>=0xAC00&&c<=0xD7A3) w+=0.97; else if(c===32) w+=0.26; else if(c>=48&&c<=57) w+=0.6;
      else if(c>=65&&c<=90) w+=0.68; else if(c>=97&&c<=122) w+=0.55; else if(c===37) w+=0.86; else w+=0.36;}
    return w;
  }
  function linesAt(s,fs,width){return Math.max(1,Math.ceil(textWidth(s)*fs*1.1/width));}
  function fitMain(main,hasLead,leadLines){
    var budget=33.4-(2.9*1.1+1.5)-(hasLead?(leadLines*3.55*1.34+1.5):0), W=87.2, sizes=[9,8.4,7.8,7.2,6.6,6,5.4,4.9,4.5];
    for(var i=0;i<sizes.length;i++){var f=sizes[i], L=linesAt(main,f,W); if(L<=4 && L*f*1.14<=budget) return {fs:f,lines:L};}
    var f0=4.5; return {fs:f0,lines:Math.max(1,Math.floor(budget/(f0*1.14)))};
  }
  var KW=[
    ['BTC',/BTC\.?D|도미넌스|비트코인 점유율|계단|내려앉|밀렸|밀리|대형주/],
    ['ALT',/알트|꼬리|종목|계열|중소형|점유율/],
    ['STABLE',/현금|스테이블|STABLE|유동성|자금/i]
  ];
  function kwFocus(t){
    if(!t) return null; var best=null, at=1e9;
    KW.forEach(function(k){var m=k[1].exec(t); if(m && m.index<at){at=m.index; best=k[0];}});
    return best;
  }
  function info(b,all,vol){
    var ps=parts(b.phase), P=ps.length?ps[ps.length-1]:'X', pal=PAL[P];
    var a=b.date.split('-').map(Number), wdi=new Date(dnum(b.date)*864e5).getUTCDay();
    var pv=prevOf(b,all), btc=b.btcd, st=b.stableD, alt=(btc!=null&&st!=null)?100-btc-st:null;
    var dB=(pv&&btc!=null&&pv.btcd!=null)?btc-pv.btcd:null, dS=(pv&&st!=null&&pv.stableD!=null)?st-pv.stableD:null;
    var dA=(dB!=null&&dS!=null)?-(dB+dS):null;
    var sp=split(b.headline), noteParts=String(b.note||'').split(/\s·\s/).map(function(s){return s.trim();}).filter(Boolean);
    var lead=sp.lead, main=sp.main;
    if(!main){ main=noteParts[0]||(ps.length?'국면 '+ps.join('→'):'첫 기록'); }
    return {b:b, P:P, ps:ps, pal:pal, vol:vol, y:a[0], m:a[1], d:a[2], wd:WDK[wdi],
      btc:btc, st:st, alt:alt, dB:dB, dS:dS, dA:dA, b1m:b.btc1m, s1m:b.stable1m,
      lead:lead, main:main, noteParts:noteParts, headline:b.headline||'',
      r:rng(hash(b.date+'#'+b.seq)), id:'mz'+(++UID),
      hist:function(key,n){return histOf(b,all,key,n);}};
  }
  /* what the picture is about: the indicator the headline names, else the one that moved most since the previous brief */
  function focusOf(D){
    var has={BTC:D.btc!=null, ALT:D.alt!=null, STABLE:D.st!=null};
    var f=kwFocus(D.main); if(f&&has[f]) return f;
    f=kwFocus(D.lead); if(f&&has[f]) return f;
    if(!D.headline){ f=kwFocus(D.b.note); if(f&&has[f]) return f; }
    var c=[['BTC',D.dB],['STABLE',D.dS],['ALT',D.dA]].filter(function(q){return q[1]!=null;})
      .sort(function(x,y){return Math.abs(y[1])-Math.abs(x[1]);});
    if(c.length && Math.abs(c[0][1])>=0.15) return c[0][0];
    return has.BTC?'BTC':null;
  }
  /* each indicator has two pictures; the second is used when the previous issue already used the first */
  var WAYS={BTC:[['stairs','btcd'],['coin','BTC']], ALT:[['coin','ALT'],['stairs','alt']], STABLE:[['tank','stableD'],['coin','STABLE']]};
  function usable(w,D){
    if(w[0]==='coin') return D.alt!=null;
    if(w[0]==='tank') return D.st!=null;
    if(w[0]==='stairs') return D.hist(w[1],9).length>=2;
    return false;
  }
  var PLAN=typeof WeakMap==='function'?new WeakMap():null;
  function planOf(all){
    var m=PLAN&&PLAN.get(all); if(m) return m;
    m={}; var prevKind=null;
    all.forEach(function(b,i){
      var D=info(b,all,i+1), f=focusOf(D), pick=['type',null];
      if(f){
        var ws=WAYS[f].filter(function(w){return usable(w,D);});
        if(ws.length){ pick=ws[0]; if(ws.length>1 && ws[0][0]===prevKind) pick=ws[1]; }
      }
      m[b.id||(b.date+'#'+b.seq)]={kind:pick[0], arg:pick[1], focus:f};
      prevKind=pick[0];
    });
    if(PLAN) PLAN.set(all,m);
    return m;
  }
  /* ---- drawing ---- */
  function figure(x,y,s,col){
    /* a small standing person with a briefcase, feet at (x,y) */
    return '<g transform="translate('+n1(x)+' '+n1(y)+') scale('+s+')" fill="'+col+'">'
      +'<circle cx="0" cy="-6.35" r=".74"/>'
      +'<path d="M-1.12 -5.28Q0 -5.72 1.12 -5.28L1.02 -2.74L-1.02 -2.74Z"/>'
      +'<path d="M-.94 -2.8L-.12 -2.8L-.26 0L-.88 0Z"/><path d="M.12 -2.8L.94 -2.8L.88 0L.26 0Z"/>'
      +'<rect x="1.12" y="-2.66" width="1.34" height="1.02" rx=".16"/><path d="M1.42 -2.66V-2.98H2.16V-2.66" fill="none" stroke="'+col+'" stroke-width=".2"/>'
      +'</g>';
  }
  function floorShadow(cx,w,col,op){return '<ellipse cx="'+n1(cx)+'" cy="124.6" rx="'+n1(w/2)+'" ry="1.5" fill="'+col+'" opacity="'+op+'"/>';}

  function objStairs(D,T,key){
    key=key||'btcd';
    var H=D.hist(key,9), N=H.length, bw=6.4, gap=1.3, dx=2.6, dy=-1.7, step=bw+gap;
    var total=N*step-gap+dx, x0=50-total/2, base=124;
    var vs=H.map(function(h){return h.v;}), lo=Math.min.apply(null,vs), hi=Math.max.apply(null,vs), rg=Math.max(hi-lo,.5);
    var s=floorShadow(50,total+6,T.ink,.07), last=null;
    H.forEach(function(h,i){
      var hh=7+(h.v-lo)/rg*31, x=x0+i*step, y=base-hh, L=i===N-1;
      var f=L?D.pal.acc:T.g1, tp=L?mixc(D.pal.acc,'#FFFFFF',.32):T.g0, sd=L?mixc(D.pal.acc,'#000000',.28):T.g2;
      s+='<path d="M'+n1(x)+' '+n1(y)+'L'+n1(x+dx)+' '+n1(y+dy)+'H'+n1(x+bw+dx)+'L'+n1(x+bw)+' '+n1(y)+'Z" fill="'+tp+'"/>'
        +'<path d="M'+n1(x+bw)+' '+n1(y)+'L'+n1(x+bw+dx)+' '+n1(y+dy)+'V'+n1(base+dy)+'L'+n1(x+bw)+' '+base+'Z" fill="'+sd+'"/>'
        +'<rect x="'+n1(x)+'" y="'+n1(y)+'" width="'+bw+'" height="'+n1(hh)+'" fill="'+f+'"/>';
      if(L) last={x:x,y:y};
    });
    s+=figure(last.x+bw/2+dx/2,last.y+dy/2,1,T.ink);
    var lab=key==='alt'?'ALT':'BTC.D', val=key==='alt'?D.alt:D.btc, dv=key==='alt'?D.dA:D.dB;
    var cap='<span>'+lab+'</span><b>'+f2(val,2)+'%</b>'+(dv!=null?'<i>'+chg(dv,2,'%p')+'</i>':'<i>최근 '+N+'회</i>');
    return {svg:s,cap:cap};
  }

  function objTank(D,T){
    var x=30, y=83, w=40, h=40, dx=7.4, dy=-4.8, base=123;
    var lv=function(v){return clamp((v-7.5)/(11-7.5),.1,.94);};
    var f=lv(D.st), ly=base-h*f, s=floorShadow(52,58,T.ink,.07);
    var acc=D.pal.acc, top=mixc(acc,'#FFFFFF',.35), deep=mixc(acc,'#000000',.2);
    /* back edges of the glass */
    s+='<path d="M'+x+' '+y+'L'+n1(x+dx)+' '+n1(y+dy)+'H'+n1(x+w+dx)+'V'+n1(base+dy)+'" fill="none" stroke="'+T.ink+'" stroke-width=".22" opacity=".45"/>'
      +'<path d="M'+n1(x+dx)+' '+n1(y+dy)+'V'+n1(base+dy)+'H'+n1(x+w+dx)+'" fill="none" stroke="'+T.ink+'" stroke-width=".16" opacity=".25"/>';
    /* liquid: side, top, front */
    s+='<path d="M'+n1(x+w)+' '+n1(ly)+'L'+n1(x+w+dx)+' '+n1(ly+dy)+'V'+n1(base+dy)+'L'+n1(x+w)+' '+base+'Z" fill="'+deep+'" opacity=".9"/>'
      +'<path d="M'+x+' '+n1(ly)+'L'+n1(x+dx)+' '+n1(ly+dy)+'H'+n1(x+w+dx)+'L'+n1(x+w)+' '+n1(ly)+'Z" fill="'+top+'"/>'
      +'<rect x="'+x+'" y="'+n1(ly)+'" width="'+w+'" height="'+n1(base-ly)+'" fill="'+acc+'" opacity=".92"/>';
    /* previous level */
    if(D.dS!=null){
      var py=base-h*lv(D.st-D.dS);
      s+='<line x1="'+(x-3)+'" y1="'+n1(py)+'" x2="'+(x+w)+'" y2="'+n1(py)+'" stroke="'+T.ink+'" stroke-width=".3" stroke-dasharray="1 .8" opacity=".75"/>';
    }
    /* flow: out of a spout when cash leaves, into the tank from a pipe when it comes in */
    if(D.dS!=null && D.dS<-0.03){
      var k=clamp(-D.dS/0.5,.25,1), sx=x+w+dx*.35, sy=base-3.2;
      s+='<path d="M'+n1(x+w)+' '+n1(sy-1)+'H'+n1(sx+5)+'V'+n1(sy+1)+'H'+n1(x+w)+'Z" fill="'+T.g3+'"/>'
        +'<path d="M'+n1(sx+5)+' '+n1(sy-.2)+'C'+n1(sx+8)+' '+n1(sy)+' '+n1(sx+8.6)+' '+n1(sy+2)+' '+n1(sx+8.8)+' 124" fill="none" stroke="'+acc+'" stroke-width="'+n1(.8+1.4*k)+'" stroke-linecap="round"/>'
        +'<ellipse cx="'+n1(sx+9.4)+'" cy="124.4" rx="'+n1(2+3.5*k)+'" ry=".9" fill="'+acc+'" opacity=".85"/>';
    } else if(D.dS!=null && D.dS>0.03){
      var k2=clamp(D.dS/0.5,.25,1), px=x+w*.3;
      s+='<path d="M'+(x-9)+' 79.4H'+n1(px+1)+'V82H'+(x-9)+'Z" fill="'+T.g3+'"/>'
        +'<path d="M'+n1(px-.1)+' 82V'+n1(ly-.5)+'" stroke="'+acc+'" stroke-width="'+n1(.8+1.4*k2)+'" stroke-linecap="round"/>';
    }
    /* front glass outline and a highlight */
    s+='<path d="M'+x+' '+y+'L'+n1(x+dx)+' '+n1(y+dy)+'H'+n1(x+w+dx)+'L'+n1(x+w)+' '+y+'Z" fill="'+T.glass+'" opacity=".22"/>'
      +'<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="none" stroke="'+T.ink+'" stroke-width=".38"/>'
      +'<path d="M'+n1(x+w)+' '+y+'L'+n1(x+w+dx)+' '+n1(y+dy)+'V'+n1(base+dy)+'L'+n1(x+w)+' '+base+'" fill="none" stroke="'+T.ink+'" stroke-width=".3"/>'
      +'<path d="M'+x+' '+y+'L'+n1(x+dx)+' '+n1(y+dy)+'H'+n1(x+w+dx)+'" fill="none" stroke="'+T.ink+'" stroke-width=".3"/>'
      +'<rect x="'+n1(x+2.2)+'" y="'+n1(y+2.4)+'" width="1.1" height="'+n1(h-6)+'" fill="#FFFFFF" opacity=".42"/>';
    s+=figure(x-7.5,124,1,T.ink);
    var cap='<span>ΣSTABLECOIN.D</span><b>'+f2(D.st,2)+'%</b>'+(D.dS!=null?'<i>'+chg(D.dS,2,'%p')+'</i>':'<i>첫 기록</i>');
    return {svg:s,cap:cap};
  }

  function objCoin(D,T,which){
    var cx=50, cy=101, rx=37, ry=15, th=6, k=Math.PI/180;
    var secs=[{k:'BTC',v:D.btc,d:D.dB,c:T.g2},{k:'ALT',v:D.alt,d:D.dA,c:T.g1},{k:'STABLE',v:D.st,d:D.dS,c:T.g0}];
    var hi={BTC:0,ALT:1,STABLE:2}[which];
    if(hi==null){ var best=-1; secs.forEach(function(q,i){ if(q.d!=null && Math.abs(q.d)>best){best=Math.abs(q.d); hi=i;} }); if(hi==null) hi=1; }
    var spans=secs.map(function(q){return q.v*3.6;}), mid=62, a0=mid-spans.slice(0,hi).reduce(function(s,v){return s+v;},0)-spans[hi]/2;
    var P=function(t,dy,ox,oy){return [cx+rx*Math.cos(t*k)+(ox||0), cy+ry*Math.sin(t*k)+(dy||0)+(oy||0)];};
    function wedge(t0,t1,ox,oy){var p0=P(t0,0,ox,oy), p1=P(t1,0,ox,oy), la=(t1-t0)>180?1:0;
      return 'M'+n1(cx+ox)+' '+n1(cy+oy)+'L'+n1(p0[0])+' '+n1(p0[1])+'A'+rx+' '+ry+' 0 '+la+' 1 '+n1(p1[0])+' '+n1(p1[1])+'Z';}
    function wall(t0,t1,ox,oy){
      /* the rim between top and bottom for the part of [t0,t1] that faces the viewer (0..180 deg, mod 360) */
      var out='';
      [[0,180],[360,540]].forEach(function(r){var s0=Math.max(t0,r[0]), s1=Math.min(t1,r[1]); if(s1-s0<=0.2) return;
        var a=P(s0,0,ox,oy), b=P(s1,0,ox,oy), c=P(s1,th,ox,oy), d=P(s0,th,ox,oy), la=(s1-s0)>180?1:0;
        out+='M'+n1(a[0])+' '+n1(a[1])+'A'+rx+' '+ry+' 0 '+la+' 1 '+n1(b[0])+' '+n1(b[1])+'L'+n1(c[0])+' '+n1(c[1])+'A'+rx+' '+ry+' 0 '+la+' 0 '+n1(d[0])+' '+n1(d[1])+'Z';});
      return out;
    }
    var s=floorShadow(cx,rx*2+8,T.ink,.08), t=a0, geo=[];
    secs.forEach(function(q,i){var t0=t, t1=t+spans[i]; t=t1; geo.push([t0,t1]);});
    var em=(geo[hi][0]+geo[hi][1])/2, ex=Math.cos(em*k)*4.2, ey=Math.sin(em*k)*4.2*ry/rx-1.2;
    var acc=D.pal.acc;
    secs.forEach(function(q,i){ if(i===hi) return; var g=geo[i];
      s+='<path d="'+wall(g[0],g[1],0,0)+'" fill="'+mixc(q.c,'#000000',.2)+'"/><path d="'+wedge(g[0],g[1],0,0)+'" fill="'+q.c+'"/>'; });
    /* the cut faces left by the lifted slice */
    [geo[hi][0],geo[hi][1]].forEach(function(tb){var p=P(tb,0,0,0);
      s+='<path d="M'+cx+' '+cy+'L'+n1(p[0])+' '+n1(p[1])+'L'+n1(p[0])+' '+n1(p[1]+th)+'L'+cx+' '+(cy+th)+'Z" fill="'+T.g2+'"/>';});
    var g=geo[hi];
    s+='<path d="'+wall(g[0],g[1],ex,ey)+'" fill="'+mixc(acc,'#000000',.28)+'"/>'
      +'<path d="M'+n1(cx+ex)+' '+n1(cy+ey)+'L'+n1(P(g[0],0,ex,ey)[0])+' '+n1(P(g[0],0,ex,ey)[1])+'L'+n1(P(g[0],th,ex,ey)[0])+' '+n1(P(g[0],th,ex,ey)[1])+'L'+n1(cx+ex)+' '+n1(cy+ey+th)+'Z" fill="'+mixc(acc,'#000000',.4)+'"/>'
      +'<path d="'+wedge(g[0],g[1],ex,ey)+'" fill="'+acc+'"/>';
    s+='<ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="none" stroke="'+T.ink+'" stroke-width=".16" opacity=".28"/>';
    var fx=cx+ex+Math.cos(em*k)*rx*.55, fy=cy+ey+Math.sin(em*k)*ry*.55;
    s+=figure(fx,fy,1,T.ink);
    var q=secs[hi];
    var cap='<span>'+q.k+'</span><b>'+f2(q.v,2)+'%</b>'+(q.d!=null?'<i>'+chg(q.d,2,'%p')+'</i>':'<i>점유율</i>');
    return {svg:s,cap:cap};
  }

  function objType(D,T){
    var txt=D.ps.length?D.ps.join('→'):String(D.vol<10?'0'+D.vol:D.vol);
    var fs=D.ps.length>1?33:44;
    var s=floorShadow(50,70,T.ink,.06)
      +'<text x="50" y="123.2" text-anchor="middle" font-family="Outfit,Futura,sans-serif" font-weight="700" font-size="'+fs+'" letter-spacing="-1" fill="none" stroke="'+T.ink+'" stroke-width=".42">'+esc(txt)+'</text>';
    s+=figure(D.ps.length>1?85:79,124,1,D.pal.acc);
    var cap=D.noteParts.length?'<span>'+esc(D.noteParts.slice(0,2).join(' · '))+'</span>':'<span>지표 기록 전</span>';
    return {svg:s,cap:cap};
  }

  function barcode(seed){
    var r=rng(hash(seed)), x=0, s='';
    while(x<96){var w=r()<.5?1.2:r()<.7?2.4:3.6; if(r()<.62) s+='<rect x="'+n1(x)+'" y="0" width="'+n1(w)+'" height="'+(x<4||x>90?44:40)+'"/>'; x+=w+(r()<.5?1.2:2.2);}
    return '<svg class="m-bc" viewBox="0 0 100 44" preserveAspectRatio="none" aria-hidden="true"><g fill="#16181A">'+s+'</g></svg>';
  }
  function glyph(){return '<svg class="m-gl" viewBox="0 0 24 22" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8.5" cy="8.3" r="6"/><circle cx="15.5" cy="8.3" r="6"/><circle cx="12" cy="14.3" r="6"/></g></svg>';}

  function coverLines(D){
    var L=[];
    if(D.btc!=null) L.push('<p><b>BTC.D</b>'+f2(D.btc,2)+'%'+(D.dB!=null?'<i>'+chg(D.dB,2,'%p')+'</i>':'')+'</p>');
    if(D.st!=null) L.push('<p><b>ΣSTABLE.D</b>'+f2(D.st,2)+'%'+(D.s1m!=null?'<i>1개월 '+sgn(D.s1m,2)+'%p</i>':'')+'</p>');
    if(D.b1m!=null) L.push('<p><b>BTCUSD</b>1개월 '+sgn(D.b1m,2)+'%</p>');
    var np=D.headline?D.noteParts:D.noteParts.slice(1);
    for(var i=0;L.length<3 && i<np.length;i++) L.push('<p>'+esc(np[i])+'</p>');
    if(!L.length) L.push('<p>지표 기록 전</p>');
    return L.join('');
  }

  function html(b,all,vol,force){
    var D=info(b,all,vol), pl=planOf(all)[b.id||(b.date+'#'+b.seq)]||{kind:'type'}, kind=force||pl.kind, dark=D.pal.dark, T=dark?DARK:LIGHT;
    var bg=dark?DARK.bg:PAPER[kind], ink=T.ink;
    var O=kind==='stairs'?objStairs(D,T,force?null:pl.arg):kind==='tank'?objTank(D,T):kind==='coin'?objCoin(D,T,force?null:pl.arg):objType(D,T);
    var leadLines=D.lead?Math.min(2,linesAt(D.lead,3.55,87.2)):0, fit=fitMain(D.main,!!D.lead,leadLines);
    var ph=D.ps.length?D.ps.slice(0,2).map(function(k){return '<i style="background:'+PAL[k].phBg+';color:'+PAL[k].phInk+'">'+k+'</i>';}).join('')
      :'<i style="background:'+PAL.X.phBg+';color:'+PAL.X.phInk+'">?</i>';
    var kick=D.ps.length===1?'국면 '+D.ps[0]+' · '+PHN[D.ps[0]]:D.ps.length>1?'국면 '+D.ps.join('→')+' · 걸친 판정':'국면 미기록';
    if(D.b.seq>1) kick+=' <small>· '+D.b.seq+'회차</small>';
    if(D.b.lite) kick+=' <small>· 간략판</small>';
    return '<div class="mz'+(dark?' m-dark':'')+' m-'+kind+'" style="'+vars({bg:bg,ink:ink,frame:FRAME,accInk:D.pal.accInk})+'">'
      +'<svg class="m-art" viewBox="0 0 100 147" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'+O.svg+'</svg>'
      +'<div class="m-L m-tag">SINCE 2026.09 · 매일 아침 06:10</div>'
      +'<div class="m-L m-kb">크립토</div>'
      +'<div class="m-L m-cl">'+coverLines(D)+'</div>'
      +'<div class="m-L m-wm">BR<span>I</span>EF</div>'
      +'<div class="m-L m-iss"><b>'+D.b.date.replace(/-/g,'.')+'</b>'+D.wd+'요일<small>제'+D.vol+'호'+(D.b.seq>1?' · '+D.b.seq+'회차':'')+'</small></div>'
      +'<div class="m-L m-ph'+(D.ps.length>1?' m-two':'')+'">'+ph+'</div>'
      +'<div class="m-L m-hb"><div class="m-k">'+kick+'</div>'
        +(D.lead?'<p class="m-lead">'+emph(D.lead)+'</p>':'')
        +'<p class="m-main" data-f="'+fit.fs+'" style="font-size:'+fit.fs+'cqw;-webkit-line-clamp:'+fit.lines+'">'+emph(D.main)+'</p></div>'
      +'<div class="m-L m-cap">'+O.cap+'</div>'
      +'<div class="m-L m-strip">'+barcode(b.date+'#'+b.seq)+'<div class="m-sx">크립토 브리핑 서고 · 제'+D.vol+'호<small>'+D.y+'년 '+D.m+'월 '+D.d+'일 발행 · 매일 06:10</small></div>'+glyph()+'</div>'
      +'<div class="m-frame"></div>'
      +'</div>';
  }
  /* after the cover is in the page: shrink the main headline until kicker, lead and main fit the block */
  function fitOne(c){
    var hb=c.querySelector('.m-hb'), mn=hb&&hb.querySelector('.m-main');
    if(!hb||!mn||!c.offsetWidth) return false;
    var W=c.offsetWidth/100, H=hb.clientHeight, gap=parseFloat(getComputedStyle(hb).rowGap)||0;
    var fixedH=0, kids=hb.children; for(var i=0;i<kids.length;i++){ if(kids[i]!==mn) fixedH+=kids[i].offsetHeight+gap; }
    var f=Math.min(9.2,parseFloat(mn.getAttribute('data-f'))+1.2);
    mn.style.webkitLineClamp='unset';
    for(var n=0;n<40;n++){
      mn.style.fontSize=f+'cqw';
      var lh=f*W*1.14, lines=Math.round(mn.scrollHeight/lh);
      if((fixedH+mn.scrollHeight<=H+0.5 && lines<=4) || f<=4.2) break;
      f=Math.round((f-0.2)*100)/100;
    }
    mn.style.webkitLineClamp=String(Math.max(1,Math.round(mn.scrollHeight/(f*W*1.14))));
    c.setAttribute('data-fit','1');
    return true;
  }
  function fit(root,force){
    var list=(root||document).querySelectorAll('.mz');
    for(var i=0;i<list.length;i++){ if(force||!list[i].hasAttribute('data-fit')) fitOne(list[i]); }
  }
  function pick(b,all){var p=planOf(all||[b])[b.id||(b.date+'#'+b.seq)]; return p?p.kind+(p.arg?':'+p.arg:''):'type';}
  function grain(){
    try{
      var c=document.createElement('canvas'); c.width=c.height=170; var x=c.getContext('2d'), im=x.createImageData(170,170), d=im.data;
      for(var i=0;i<d.length;i+=4){var v=Math.random()<.5?0:255; d[i]=d[i+1]=d[i+2]=v; d[i+3]=Math.random()<.55?(Math.random()*34|0):0;}
      x.putImageData(im,0,0); document.documentElement.style.setProperty('--grain','url('+c.toDataURL('image/png')+')');
    }catch(e){}
  }
  return {html:html,pick:pick,grain:grain,fit:fit};
  })();
