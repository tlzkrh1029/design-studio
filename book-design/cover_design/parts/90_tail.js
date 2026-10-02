
  /* ---- fixed parts of every cover ---- */
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
  /* force: {scene, scheme, hue, focus} overrides the plan (used for previews) */
  function resolve(b,all,vol,force){
    force=force||{};
    var pl=planOf(all)[keyOf(b)]||{}, D=info(b,all,vol);
    var F=force.focus||pl.focus||focusOf(D);
    var sc=SCI[force.scene||pl.scene]; if(!sc||!sc.need(D,F)) sc=chooseScene(D,F,[]);
    var si=force.scheme!=null?force.scheme:(pl.scheme!=null?pl.scheme:pickScheme(D,[]));
    var H=force.hue!=null?force.hue:(pl.hue!=null?pl.hue:hueOf(b));
    return {D:D,F:F,sc:sc,si:si,H:H};
  }
  function html(b,all,vol,force){
    var Z=resolve(b,all,vol,force), D=Z.D, F=Z.F, T=palette(Z.si,Z.H), O=Z.sc.draw(D,T,F);
    var leadLines=D.lead?Math.min(2,linesAt(D.lead,3.55,87.2)):0, fit=fitMain(D.main,!!D.lead,leadLines);
    var sq=function(k,bgc,fg){return '<i style="background:'+bgc+';color:'+fg+'">'+k+'</i>';};
    var ph=D.ps.length>1?sq(D.ps[D.ps.length-2],T.c2,T.c2Ink)+sq(D.P,T.c3,T.c3Ink):D.ps.length?sq(D.P,T.c3,T.c3Ink):sq('?',T.n0,inkOn(T.n0));
    var kick=D.ps.length===1?'국면 '+D.ps[0]+' · '+PHN[D.ps[0]]:D.ps.length>1?'국면 '+D.ps.join('→')+' · 걸친 판정':'국면 미기록';
    if(D.b.seq>1) kick+=' <small>· '+D.b.seq+'회차</small>';
    if(D.b.lite) kick+=' <small>· 간략판</small>';
    var em=T.hl===T.ink?T.acc:T.ink;
    return '<div class="mz'+(T.dark?' m-dark':'')+' m-'+Z.sc.id+'" data-scene="'+Z.sc.id+'" style="'+vars({bg:T.bg,ink:T.ink,frame:T.fr,frameInk:T.frInk,accInk:T.acc,hl:T.hl,em:em})+'">'
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
    var hb=c.querySelector('.m-hb'), mn=hb&&hb.querySelector('.m-main'), ld=hb&&hb.querySelector('.m-lead');
    if(!hb||!mn||!c.offsetWidth) return false;
    /* Chrome drops text-wrap:balance on a clamped block that would overflow, so clamp only when the text really
       needs more lines than allowed; otherwise leave it unclamped and balanced */
    if(ld){ ld.style.webkitLineClamp='unset'; var llh=parseFloat(getComputedStyle(ld).lineHeight)||1; if(ld.scrollHeight>llh*2+1) ld.style.webkitLineClamp='2'; }
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
    if(fixedH+mn.scrollHeight>H+0.5) mn.style.webkitLineClamp=String(Math.max(1,Math.floor((H-fixedH+0.5)/(f*W*1.14))));
    c.setAttribute('data-fit','1');
    return true;
  }
  function fit(root,force){
    var list=(root||document).querySelectorAll('.mz');
    for(var i=0;i<list.length;i++){ if(force||!list[i].hasAttribute('data-fit')) fitOne(list[i]); }
  }
  function pick(b,all,force){
    var Z=resolve(b,all||[b],1,force); return Z.sc.ko+' · '+SCH[Z.si].n+' · '+Math.round(Z.H)+'°';
  }
  function grain(){
    try{
      var c=document.createElement('canvas'); c.width=c.height=170; var x=c.getContext('2d'), im=x.createImageData(170,170), d=im.data;
      for(var i=0;i<d.length;i+=4){var v=Math.random()<.5?0:255; d[i]=d[i+1]=d[i+2]=v; d[i+3]=Math.random()<.55?(Math.random()*34|0):0;}
      x.putImageData(im,0,0); document.documentElement.style.setProperty('--grain','url('+c.toDataURL('image/png')+')');
    }catch(e){}
  }
  return {html:html,pick:pick,grain:grain,fit:fit,
    scenes:SC.map(function(s){return {id:s.id,ko:s.ko,f:s.f.slice()};}),
    schemes:SCH.map(function(s){return s.n;}),
    plan:function(all){return planOf(all);},
    can:function(b,all,vol,id,F){var D=info(b,all,vol); return !!(SCI[id]&&SCI[id].need(D,F));},
    focus:function(b,all,vol){return focusOf(info(b,all,vol));},
    palette:palette, contrast:cr};
  })();
