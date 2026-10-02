
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
  /* what a clause is about. Share indicators first (earliest mention wins), then policy events, then price */
  var KW={
    BTC:/BTC\.?D|도미넌스|비트코인 점유율|계단|내려앉|밀렸|밀리|대형주/,
    ALT:/알트|꼬리|종목|계열|중소형|점유율/,
    STABLE:/현금|스테이블|STABLE|유동성|자금/i,
    MACRO:/연준|FOMC|금리|\d+bp|법안|표결|클로처|SEC|규제|의회|상원|하원|정책|대통령|관세/,
    PRICE:/\d[\d,]*달러|사이클선|숏|반등|되밀|급등|급락|신고가/
  };
  function kwFocus(t){
    if(!t) return null; var best=null, at=1e9;
    ['BTC','ALT','STABLE'].forEach(function(k){var m=KW[k].exec(t); if(m && m.index<at){at=m.index; best=k;}});
    if(best) return best;
    if(KW.MACRO.test(t)) return 'MACRO';
    if(KW.PRICE.test(t)) return 'PRICE';
    return null;
  }
  function info(b,all,vol){
    var ps=parts(b.phase), P=ps.length?ps[ps.length-1]:'X';
    var a=b.date.split('-').map(Number), wdi=new Date(dnum(b.date)*864e5).getUTCDay();
    var pv=prevOf(b,all), btc=b.btcd, st=b.stableD, alt=(btc!=null&&st!=null)?100-btc-st:null;
    var dB=(pv&&btc!=null&&pv.btcd!=null)?btc-pv.btcd:null, dS=(pv&&st!=null&&pv.stableD!=null)?st-pv.stableD:null;
    var dA=(dB!=null&&dS!=null)?-(dB+dS):null;
    var sp=split(b.headline), noteParts=String(b.note||'').split(/\s·\s/).map(function(s){return s.trim();}).filter(Boolean);
    var lead=sp.lead, main=sp.main;
    if(!main){ main=noteParts[0]||(ps.length?'국면 '+ps.join('→'):'첫 기록'); }
    var cache={};
    return {b:b, P:P, ps:ps, vol:vol, y:a[0], m:a[1], d:a[2], wd:WDK[wdi], wdi:wdi,
      btc:btc, st:st, alt:alt, dB:dB, dS:dS, dA:dA, b1m:b.btc1m, s1m:b.stable1m,
      lead:lead, main:main, noteParts:noteParts, headline:b.headline||'', note:b.note||'',
      r:rng(hash(b.date+'#'+b.seq)), id:'mz'+(++UID),
      hist:function(key,n){var k=key+'/'+n; return cache[k]||(cache[k]=histOf(b,all,key,n));}};
  }
  /* what the picture is about: the indicator the headline names, else the one that moved most since the previous brief */
  function focusOf(D){
    var has={BTC:D.btc!=null, ALT:D.alt!=null, STABLE:D.st!=null, MACRO:true, PRICE:D.b1m!=null};
    var src=[D.main, D.lead]; if(!D.headline) src.push(D.note);
    for(var i=0;i<src.length;i++){var f=kwFocus(src[i]); if(f&&has[f]) return f;}
    var c=[['BTC',D.dB],['STABLE',D.dS],['ALT',D.dA]].filter(function(q){return q[1]!=null;})
      .sort(function(x,y){return Math.abs(y[1])-Math.abs(x[1]);});
    if(c.length && Math.abs(c[0][1])>=0.15) return c[0][0];
    if(D.alt!=null) return 'MIX';
    if(D.btc!=null) return 'BTC';
    return 'TYPE';
  }
  var LAB={BTC:'BTC.D',ALT:'ALT',STABLE:'ΣSTABLECOIN.D'};
  function keyF(F){return F==='ALT'?'alt':F==='STABLE'?'stableD':F==='PRICE'?'btc1m':'btcd';}
  function shareOf(D,F){return F==='BTC'?D.btc:F==='ALT'?D.alt:F==='STABLE'?D.st:null;}
  function dOf(D,F){return F==='BTC'?D.dB:F==='ALT'?D.dA:F==='STABLE'?D.dS:null;}
  function mover(D){
    var c=[['BTC',D.dB],['STABLE',D.dS],['ALT',D.dA]].filter(function(q){return q[1]!=null;})
      .sort(function(x,y){return Math.abs(y[1])-Math.abs(x[1]);});
    return c.length?c[0][0]:(D.btc!=null?'BTC':null);
  }
  /* the share the picture points at: the named one, or for mixed pictures the one that moved most */
  function hiOf(D,F){return (F==='BTC'||F==='ALT'||F==='STABLE')?F:(mover(D)||'ALT');}
  function histN(D,F,n){return D.hist(keyF(F),n);}
  function span(H,min){var vs=H.map(function(h){return h.v;}), lo=Math.min.apply(null,vs), hi=Math.max.apply(null,vs); return {lo:lo,hi:hi,rg:Math.max(hi-lo,min||.3)};}
  /* consecutive declines up to the latest value */
  function fallRun(H){var k=0; for(var i=H.length-1;i>0;i--){ if(H[i].v<H[i-1].v) k++; else break; } return k;}

  /* ---- captions under the picture ---- */
  function capShare(D,F){
    var v=shareOf(D,F), d=dOf(D,F); if(v==null) return capAny(D);
    var tail=d!=null?chg(d,2,'%p'):(F==='STABLE'&&D.s1m!=null?'1개월 '+sgn(D.s1m,2)+'%p':'첫 기록');
    return '<span>'+LAB[F]+'</span><b>'+f2(v,2)+'%</b><i>'+tail+'</i>';
  }
  function capPrice(D){return D.b1m==null?capAny(D):'<span>BTCUSD</span><b>'+sgn(D.b1m,2)+'%</b><i>1개월 등락</i>';}
  function capNote(D){return D.noteParts.length?'<span>'+esc(D.noteParts.slice(0,2).join(' · '))+'</span>':'<span>지표 기록 전</span>';}
  function capAny(D){var m=mover(D); return m?capShare(D,m):capNote(D);}
  function capFor(D,F){
    if(F==='BTC'||F==='ALT'||F==='STABLE') return capShare(D,F);
    if(F==='PRICE') return capPrice(D);
    if(F==='MIX') return capShare(D,hiOf(D,F));
    return capAny(D);
  }

  /* ---- picture registry and the plan for the whole shelf ---- */
  var SC=[], SCI={};
  function scene(id,ko,f,need,kw,draw){var s={id:id,ko:ko,f:f,need:need,kw:kw,draw:draw}; SC.push(s); SCI[id]=s;}
  function kwScore(s,D){
    if(!s.kw) return 0; var v=0;
    if(s.kw.test(D.main)) v+=6;
    if(D.lead && s.kw.test(D.lead)) v+=4;
    if(!D.headline && D.note && s.kw.test(D.note)) v+=3;
    return v;
  }
  /* candidates: pictures that can show this focus with the data at hand. A picture used in the last
     12 issues is skipped unless the headline names its subject and it is at least 7 issues back. */
  function chooseScene(D,F,used){
    var cands=SC.filter(function(s){return s.f.indexOf(F)>=0 && s.need(D,F);});
    if(!cands.length) cands=[SCI.letters];
    var n=used.length, best=null, bs=-1e9;
    cands.forEach(function(s){
      var last=used.lastIndexOf(s.id), ago=last<0?1e9:n-last, k=kwScore(s,D);
      var blocked=ago<=12 && !(k>0 && ago>=7);
      var sc=(blocked?-100+Math.min(ago,99)*0.5:0)+k+(s.f[0]===F?2:0)+(last<0?1.5:0)+hash(D.b.date+'/'+D.b.seq+'/'+s.id)/4294967296;
      if(sc>bs){bs=sc; best=s;}
    });
    return best;
  }
  function keyOf(b){return b.id||(b.date+'#'+b.seq);}
  var PLAN=typeof WeakMap==='function'?new WeakMap():null;
  function planOf(all){
    var m=PLAN&&PLAN.get(all); if(m) return m;
    m={}; var used=[], schs=[];
    all.forEach(function(b,i){
      var D=info(b,all,i+1), F=focusOf(D), s=chooseScene(D,F,used), si=pickScheme(D,schs);
      m[keyOf(b)]={scene:s.id, focus:F, scheme:si, hue:hueOf(b)};
      used.push(s.id); schs.push(si);
    });
    if(PLAN) PLAN.set(all,m);
    return m;
  }
