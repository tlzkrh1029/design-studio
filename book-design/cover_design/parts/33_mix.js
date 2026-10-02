
  /* ---- the three shares side by side ---- */
  function shareCols(T,hi){var o={}, other=[T.c1,T.c2], i=0; ['BTC','ALT','STABLE'].forEach(function(k){o[k]=k===hi?T.c3:other[i++%2];}); return o;}
  function colInk(T,c){return c===T.c3?T.c3Ink:c===T.c1?T.c1Ink:c===T.c2?T.c2Ink:inkOn(c);}

  scene('pie','동전 파이',['MIX','ALT','BTC','STABLE'],needAll,/점유율|몫|나눠|비중|파이/,function(D,T,F){
    var hiK=hiOf(D,F), cx=50, cy=101, rx=37, ry=15, th=6, k=Math.PI/180, CO=shareCols(T,hiK);
    var secs=[{k:'BTC',v:D.btc},{k:'ALT',v:D.alt},{k:'STABLE',v:D.st}], hi=['BTC','ALT','STABLE'].indexOf(hiK);
    var spans=secs.map(function(q){return q.v*3.6;}), mid=62, a0=mid-spans.slice(0,hi).reduce(function(s,v){return s+v;},0)-spans[hi]/2;
    var Pt=function(t,dy,ox,oy){return [cx+rx*Math.cos(t*k)+(ox||0), cy+ry*Math.sin(t*k)+(dy||0)+(oy||0)];};
    function wedge(t0,t1,ox,oy){var p0=Pt(t0,0,ox,oy), p1=Pt(t1,0,ox,oy), la=(t1-t0)>180?1:0;
      return 'M'+at(cx+ox)+' '+at(cy+oy)+'L'+at(p0[0])+' '+at(p0[1])+'A'+rx+' '+ry+' 0 '+la+' 1 '+at(p1[0])+' '+at(p1[1])+'Z';}
    function wall(t0,t1,ox,oy){
      var out='';
      [[0,180],[360,540]].forEach(function(r){var s0=Math.max(t0,r[0]), s1=Math.min(t1,r[1]); if(s1-s0<=0.2) return;
        var a=Pt(s0,0,ox,oy), b=Pt(s1,0,ox,oy), c=Pt(s1,th,ox,oy), d=Pt(s0,th,ox,oy), la=(s1-s0)>180?1:0;
        out+='M'+at(a[0])+' '+at(a[1])+'A'+rx+' '+ry+' 0 '+la+' 1 '+at(b[0])+' '+at(b[1])+'L'+at(c[0])+' '+at(c[1])+'A'+rx+' '+ry+' 0 '+la+' 0 '+at(d[0])+' '+at(d[1])+'Z';});
      return out;
    }
    var s=shadow(cx,rx*2+8,T), t=a0, geo=[];
    secs.forEach(function(q,i){var t0=t, t1=t+spans[i]; t=t1; geo.push([t0,t1]);});
    var em=(geo[hi][0]+geo[hi][1])/2, ex=Math.cos(em*k)*4.2, ey=Math.sin(em*k)*4.2*ry/rx-1.2;
    secs.forEach(function(q,i){ if(i===hi) return; var g=geo[i], c=CO[q.k];
      var w=wall(g[0],g[1],0,0); if(w) s+=P(w,shade(c,.22)); s+=P(wedge(g[0],g[1],0,0),c); });
    [geo[hi][0],geo[hi][1]].forEach(function(tb){var p=Pt(tb,0,0,0);
      s+=P('M'+cx+' '+cy+'L'+at(p[0])+' '+at(p[1])+'L'+at(p[0])+' '+at(p[1]+th)+'L'+cx+' '+(cy+th)+'Z',T.n2);});
    var g=geo[hi], acc=T.c3, w2=wall(g[0],g[1],ex,ey), p0=Pt(g[0],0,ex,ey), p0b=Pt(g[0],th,ex,ey);
    if(w2) s+=P(w2,shade(acc,.28));
    s+=P('M'+at(cx+ex)+' '+at(cy+ey)+'L'+at(p0[0])+' '+at(p0[1])+'L'+at(p0b[0])+' '+at(p0b[1])+'L'+at(cx+ex)+' '+at(cy+ey+th)+'Z',shade(acc,.4))+P(wedge(g[0],g[1],ex,ey),acc);
    s+=E(cx,cy,rx,ry,'none',' stroke="'+T.ink+'" stroke-width=".16"'+op(.28));
    s+=person(cx+ex+Math.cos(em*k)*rx*.55,cy+ey+Math.sin(em*k)*ry*.55,T);
    return {svg:s,cap:capShare(D,hiK)};
  });

  scene('orbit','궤도',['MIX','BTC','ALT'],needAll,/중심|주변|궤도|돌았|맴|위성/,function(D,T,F){
    var hi=hiOf(D,F), CO=shareCols(T,hi), k=2.05, rB=k*Math.sqrt(D.btc), rA=k*Math.sqrt(D.alt), rS=k*Math.sqrt(D.st), px=42, py=105, s='';
    for(var i=0;i<16;i++) s+=C(6+D.r()*88,76+D.r()*22,.2+D.r()*.3,T.ink,op(.35));
    s+=E(50,101,45,13,'none',' stroke="'+T.ink+'" stroke-width=".25" stroke-dasharray="1 1"'+op(.5)+' transform="rotate(-9 50 101)"');
    var ax=80, ay=88, sx=16, sy=113;
    s+=ball(ax,ay,rA,CO.ALT)+TX(ax,ay+1.2,'ALT',rA*.4,colInk(T,CO.ALT),{w:800});
    var rx=rB*1.75, ry=rB*.36, ring=shade(T.c2,.05);
    s+=G(P('M'+at(-rx)+' 0A'+at(rx)+' '+at(ry)+' 0 0 1 '+at(rx)+' 0','none',' stroke="'+ring+'" stroke-width="1.8"'),'translate('+px+' '+py+') rotate(-14)');
    s+=ball(px,py,rB,CO.BTC)+TX(px,py+1.6,'BTC',rB*.36,colInk(T,CO.BTC),{w:800});
    s+=G(P('M'+at(rx)+' 0A'+at(rx)+' '+at(ry)+' 0 0 1 '+at(-rx)+' 0','none',' stroke="'+ring+'" stroke-width="1.8"')+P('M'+at(rx-1)+' .3A'+at(rx-1)+' '+at(ry-.3)+' 0 0 1 '+at(-rx+1)+' .3','none',' stroke="'+tint(ring,.35)+'" stroke-width=".4"'),'translate('+px+' '+py+') rotate(-14)');
    s+=ball(sx,sy,rS,CO.STABLE)+TX(sx,sy+.8,'STABLE',Math.min(rS*.36,rS*1.5/3.7),colInk(T,CO.STABLE),{w:800});
    s+=person(px+1.2,py-rB+.3,T,{pose:'wave'});
    return {svg:s,cap:capShare(D,hi)};
  });

  scene('strata','지층',['MIX','STABLE','BTC','ALT'],needAll,/구조|층|바닥|지층|깔려|밑/,function(D,T,F){
    var hi=hiOf(D,F), CO=shareCols(T,hi), x=10, w=58, Ht=38, d=11, dx=d*DX, dy=d*DY, y0=FL-Ht, s=shadow(44,76,T);
    var L=[['STABLE',D.st],['ALT',D.alt],['BTC',D.btc]], yT=y0, B=[];
    L.forEach(function(q){var h=q[1]/100*Ht; B.push([q[0],yT,yT+h,q[1]]); yT+=h;});
    B.forEach(function(b){s+=P('M'+at(x+w)+' '+at(b[1])+'L'+at(x+w+dx)+' '+at(b[1]+dy)+'V'+at(b[2]+dy)+'L'+at(x+w)+' '+at(b[2])+'Z',shade(CO[b[0]],.24));});
    s+=P('M'+at(x)+' '+at(y0)+'L'+at(x+dx)+' '+at(y0+dy)+'H'+at(x+w+dx)+'L'+at(x+w)+' '+at(y0)+'Z',tint(CO.STABLE,.3));
    B.forEach(function(b,i){
      var d2='M'+at(x)+' '+FL+'V'+at(b[1]), ph=i*1.7;
      if(i===0) d2+='H'+at(x+w); else for(var xx=x;xx<=x+w+.01;xx+=2.9) d2+='L'+at(xx)+' '+at(b[1]+Math.sin(xx*.42+ph)*.75);
      d2+='L'+at(x+w)+' '+FL+'Z';
      s+=P(d2,CO[b[0]]);
    });
    for(var k=0;k<34;k++){var bx=x+2+D.r()*(w-4), by=B[2][1]+2.6+D.r()*(FL-B[2][1]-4); s+=C(bx,by,.3+D.r()*.35,shade(CO.BTC,.28),op(.7));}
    for(var k2=0;k2<14;k2++){var ax=x+2+D.r()*(w-6), ay=B[1][1]+1.8+D.r()*Math.max(1,B[1][2]-B[1][1]-3.2); s+=Ln(ax,ay,ax+1.6,ay,shade(CO.ALT,.25),.3);}
    B.forEach(function(b){var my=(b[1]+b[2])/2+dy/2; s+=TX(x+w+dx+2.2,my+1,b[0]+' '+f2(b[3],1)+'%',2.3,T.ink,{a:'start',w:700});});
    var o={pose:'hold'}, fx=x+22+dx*.5, fy=y0+dy*.5, hd=handOf(fx,fy,o);
    s+=Ln(hd[0],hd[1],hd[0]+2.6,fy+.3,T.n3,.45)+PG([[hd[0]+1.8,fy-.8],[hd[0]+3.8,fy-.8],[hd[0]+3.6,fy+1.2],[hd[0]+2,fy+1.2]],T.n3);
    s+=person(fx,fy,T,o);
    return {svg:s,cap:capShare(D,hi)};
  });

  scene('flags','깃발',['MIX','BTC','ALT','STABLE'],needAll,/앞장|선두|깃발|앞서|이끌|선봉/,function(D,T,F){
    var hi=hiOf(D,F), CO=shareCols(T,hi), Q=[['BTC',D.btc],['ALT',D.alt],['STABLE',D.st]], xs=[22,46,70], s=shadow(48,72,T), hx=46, htop=FL-20;
    Q.forEach(function(q,i){
      var x=xs[i], h=12+q[1]*.52, top=FL-h, f=CO[q[0]], fw=13.5, fh=7.6;
      s+=box(x-3,FL-2,6,2,3,T.n2)+R(x-.5,top,1,h-2,T.n3)+C(x,top-.4,.9,T.c3);
      var fl='M'+at(x+.5)+' '+at(top+.4)+'C'+at(x+4.5)+' '+at(top-1.2)+' '+at(x+9)+' '+at(top+2)+' '+at(x+.5+fw)+' '+at(top+.4)+'V'+at(top+.4+fh)+'C'+at(x+9)+' '+at(top+2+fh)+' '+at(x+4.5)+' '+at(top-1.2+fh)+' '+at(x+.5)+' '+at(top+.4+fh)+'Z';
      s+=P(fl,f)+TX(x+.5+fw/2,top+fh/2+1.5,q[0],q[0]==='STABLE'?2.2:2.9,colInk(T,f),{w:800});
      if(q[0]===hi){hx=x; htop=top;}
    });
    var o={pose:'pull',face:-1}, px=hx+4.2, hd=handOf(px,FL,o);
    s+=Ln(hx+.6,htop+8.2,hd[0],hd[1],T.ink,.18,op(.8))+person(px,FL,T,o);
    return {svg:s,cap:capShare(D,hi)};
  });

  scene('waffle','타일 100칸',['MIX','BTC','ALT','STABLE'],needAll,/가운데|하나도|마흔|열 개|비율|중에|절반/,function(D,T,F){
    var hi=hiOf(D,F), CO=shareCols(T,hi), nB=Math.round(D.btc), nS=Math.round(D.st), nA=100-nB-nS, a=3.75, b=1.9, ox=50, oy=FL-1.5, raise=2.6, s=shadow(50,80,T,T.dark?.2:.05);
    var grp=function(k){return k<nB?'BTC':k<nB+nA?'ALT':'STABLE';};
    var Pp=function(u,v){return [ox+(u-v)*a, oy-(u+v)*b];};
    var cells=[]; for(var j=0;j<10;j++) for(var i=0;i<10;i++) cells.push([i,j,grp(j*10+i)]);
    cells.sort(function(p,q){return (q[0]+q[1])-(p[0]+p[1]);});
    var standAt=null;
    cells.forEach(function(c){var u=c[0], v=c[1], g=c[2], up=g===hi?raise:0, e=.07;
      var p=[Pp(u+e,v+e),Pp(u+1-e,v+e),Pp(u+1-e,v+1-e),Pp(u+e,v+1-e)], t=p.map(function(q){return [q[0],q[1]-up];});
      if(up) s+=PG([t[0],t[1],p[1],p[0]],shade(CO[g],.24))+PG([t[3],t[0],p[0],p[3]],shade(CO[g],.1));
      s+=PG(t,up?tint(CO[g],.1):CO[g]);
      if(g===hi && (!standAt || u+v<standAt[2])) standAt=[(t[0][0]+t[2][0])/2,(t[0][1]+t[2][1])/2,u+v];
    });
    if(standAt) s+=person(standAt[0],standAt[1]+.2,T,{pose:'wave'});
    return {svg:s,cap:capShare(D,hi)};
  });

  scene('bubbles','비눗방울',['MIX','ALT','BTC','STABLE'],needAll,/거품|버블|부풀|터질|터졌|부푼/,function(D,T,F){
    var hi=hiOf(D,F), CO=shareCols(T,hi), k=2.2, Q=[['BTC',D.btc,63,99],['ALT',D.alt,31,94],['STABLE',D.st,40,115]], s='';
    var o={pose:'hold'}, hd=handOf(9.5,FL,o);
    s+=shadow(10,8,T)+Ln(hd[0],hd[1],hd[0]+4.6,hd[1]-3.2,T.n3,.4)+C(hd[0]+5.6,hd[1]-3.9,1.3,'none',' stroke="'+T.n3+'" stroke-width=".4"');
    [[21,115,1.1],[24.5,110,.7],[19,108,.5]].forEach(function(q){s+=C(q[0],q[1],q[2],'none',' stroke="'+T.ink+'" stroke-width=".2"'+op(.5));});
    Q.forEach(function(q){var r=k*Math.sqrt(q[1]), x=q[2], y=q[3], c=CO[q[0]];
      s+=C(x,y,r,c,op(.9))+C(x,y,r-.3,'none',' stroke="#FFFFFF" stroke-width=".3"'+op(.45))
        +SK('M'+at(x-r*.72)+' '+at(y-r*.2)+'A'+at(r*.75)+' '+at(r*.75)+' 0 0 1 '+at(x-r*.2)+' '+at(y-r*.72),'#FFFFFF',at(Math.max(.4,r*.06)),op(.75))+C(x+r*.42,y+r*.4,Math.max(.3,r*.05),'#FFFFFF',op(.6));
      var ik=colInk(T,c), fs=Math.min(r*.36,r*1.5/(q[0].length*.62)); s+=TX(x,y-.2,q[0],Math.max(1.8,fs),ik,{w:800})+TX(x,y+Math.max(2.4,r*.36),f2(q[1],1)+'%',Math.max(1.9,r*.26),ik,{ff:'n',w:500});});
    s+=person(9.5,FL,T,o);
    return {svg:s,cap:capShare(D,hi)};
  });
