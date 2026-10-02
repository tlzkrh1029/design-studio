
  /* ---- ALT: everything that is neither bitcoin nor stablecoins ---- */
  scene('balloons','풍선',['ALT','PRICE'],function(D,F){return F==='PRICE'?D.b1m!=null:D.alt!=null;},/올랐|부풀|띄|떠올|가벼|날아/,function(D,T,F){
    var d=F==='PRICE'?(D.b1m!=null?D.b1m/12:null):D.dA, lift=d!=null&&d>0?clamp(d*20,2.5,11):0;
    var o={pose:'wave'}, fx=50, fy=FL-lift, h=handOf(fx,fy,o), s=shadow(50,lift?6:9,T,T.dark?.25:.07);
    var cols=[T.c1,T.c2,T.c3,tint(T.c1,.3),shade(T.c2,.12),tint(T.c3,.3),shade(T.c1,.12),T.c2];
    var B=[[-10,4],[0,-1],[10,3.5],[-5,9.6],[5.5,9],[-14,12.5],[14.5,12],[0,15.5]], cx=h[0], cy=85.5;
    B.forEach(function(q){var bx=cx+q[0], by=cy+q[1]+5.6; s+=SK('M'+at(bx)+' '+at(by)+'Q'+at((bx+h[0])/2+(q[0]>0?1.5:-1.5))+' '+at((by+h[1])/2)+' '+at(h[0])+' '+at(h[1]),T.ink,.16,op(.7));});
    B.forEach(function(q,i){var bx=cx+q[0], by=cy+q[1], c=cols[i%cols.length];
      s+=E(bx,by,4.2,5,c)+PG([[bx,by+4.8],[bx-.9,by+5.9],[bx+.9,by+5.9]],shade(c,.12))+E(bx-1.5,by-2,1,1.6,'#FFFFFF',op(.38)+' transform="rotate(-24 '+at(bx-1.5)+' '+at(by-2)+')"');});
    s+=person(fx,fy,T,o);
    return {svg:s,cap:F==='PRICE'?capPrice(D):capShare(D,'ALT')};
  });

  scene('sprout','새싹 화분',['ALT'],needHist(3),/새싹|늘었|자라|싹|처음|피어/,function(D,T,F){
    var H=histN(D,F,5), N=H.length, S=span(H,.4), gap=12.5, x0=46-(N-1)*gap/2-4, s=shadow(46,N*gap+8,T);
    H.forEach(function(h,i){
      var cx=x0+i*gap, L=i===N-1, ph=6+(h.v-S.lo)/S.rg*20, top=FL-9.2-ph, lc=L?T.c3:T.c1;
      s+=SK('M'+at(cx)+' '+at(FL-9.2)+'C'+at(cx-1.2)+' '+at(FL-9.2-ph*.4)+' '+at(cx+1.4)+' '+at(FL-9.2-ph*.7)+' '+at(cx+.3)+' '+at(top),shade(lc,.12),.75);
      var nl=Math.max(1,Math.round(ph/7));
      for(var j=1;j<=nl;j++){var ly=FL-9.2-ph*j/(nl+.8), sd=j%2?1:-1; s+=E(cx+sd*2.1,ly,2.3,1,lc,' transform="rotate('+(sd*-28)+' '+at(cx+sd*2.1)+' '+at(ly)+')"');}
      if(L){for(var q=0;q<5;q++){var a=(q*72-90)*Math.PI/180; s+=C(cx+.3+Math.cos(a)*1.7,top+Math.sin(a)*1.7,1.3,T.c3);} s+=C(cx+.3,top,1,T.c2);}
      else s+=E(cx+.3,top,1,1.6,lc);
      s+=PG([[cx-4.6,FL-8],[cx+4.6,FL-8],[cx+3.4,FL],[cx-3.4,FL]],T.c2)+R(cx-5.1,FL-9.6,10.2,1.8,shade(T.c2,.14))+E(cx,FL-9.6,4.5,.7,shade(T.c2,.5));
    });
    var o={pose:'hold',face:-1}, fx=x0+(N-1)*gap+12, hd=handOf(fx,FL,o);
    s+=person(fx,FL,T,o);
    s+=G(R(-4.4,-1.6,4.6,3.4,T.n3,' rx=".6"')+Ln(-4.2,-.6,-7.6,-3.4,T.n3,.7)+SK('M-.6 -1.6Q-1.8 -3.8 -3.4 -1.6',T.n3,.45),'translate('+at(hd[0]+.4)+' '+at(hd[1])+')');
    for(var k=0;k<3;k++) s+=E(hd[0]-7.6-k*.8,hd[1]-1.4+k*2.3,.35,.6,T.c1,op(.85));
    return {svg:s,cap:capShare(D,'ALT')};
  });

  scene('stacks','동전 탑',['ALT','BTC','STABLE','MIX'],needAll,/쌓였|쌓아|적립|모았|모아|동전 탑/,function(D,T,F){
    var hi=hiOf(D,F), Q=[['BTC',D.btc],['ALT',D.alt],['STABLE',D.st]], xs=[26,50,74], th=1.7, rx=8, ry=2.5, s=shadow(50,72,T), other=[T.c1,T.c2], oi=0;
    Q.forEach(function(q,i){
      var f=q[0]===hi?T.c3:other[oi++%2], n=Math.max(1,Math.round(q[1]/2.8)), x=xs[i], top=FL;
      for(var k=0;k<n;k++){ var y=FL-th-ry-k*th; s+=coinFlat(x+(D.r()-.5)*.9,y,rx,ry,th,k%2?f:shade(f,.05)); top=y; }
      s+=TX(x,top-ry-2.4,q[0],2.5,T.ink,{w:700})+TX(x,top-ry-5.7,f2(q[1],1)+'%',3.2,T.ink,{ff:'n',w:500});
    });
    s+=person(89,FL,T,{pose:'point',face:-1});
    return {svg:s,cap:capShare(D,hi)};
  });

  scene('tug','줄다리기',['ALT','BTC'],function(D){return D.dA!=null;},/줄다리기|당겼|끌어|맞섰|힘겨루|버텼/,function(D,T,F){
    var dA=D.dA, sh=clamp(dA*22,-9,9), r=15, cx=21, cy=FL-r, s=shadow(42,84,T);
    s+=Ln(50,FL-2.4,50,FL+.8,T.ink,.35,' stroke-dasharray="1 .8"'+op(.6));
    var tilt=dA>0.05?clamp(dA*20,3,9):0;
    s+=G(coinFace(cx,cy,r,T.c1,'BTC',T.c1Ink),tilt?'rotate('+at(tilt)+' '+at(cx+r)+' '+FL+')':'');
    if(tilt) for(var i=0;i<3;i++) s+=C(cx+r-1+i*2.2,FL-.9-i*.4,.9+i*.3,T.n1,op(.8));
    var o={pose:'pull',face:-1}, xs=[63,72.5,82], hs=xs.map(function(x){return handOf(x,FL,o);});
    var ax=cx+r+2.4, ay=cy+3.5, ex=hs[2][0]+3.6, ey=hs[2][1]+.6;
    s+=SK('M'+at(ax)+' '+at(ay)+'Q'+at((ax+ex)/2)+' '+at((ay+ey)/2+1.4)+' '+at(ex)+' '+at(ey),shade(T.c2,.2),.9);
    var mx=50+sh, tt=(mx-ax)/(ex-ax), my=(1-tt)*(1-tt)*ay+2*(1-tt)*tt*((ay+ey)/2+1.4)+tt*tt*ey;
    s+=Ln(mx,my,mx,my+3.4,T.c3,.35)+PG([[mx,my+.6],[mx+3.2,my+1.7],[mx,my+2.8]],T.c3);
    xs.forEach(function(x){s+=person(x,FL,T,o);});
    return {svg:s,cap:capShare(D,'ALT')};
  });

  scene('beakers','비커',['ALT','STABLE','MIX','BTC'],needAll,/실험|농도|섞|분리|희석|녹아|갈라/,function(D,T,F){
    var hi=hiOf(D,F), Q=[['BTC',D.btc],['ALT',D.alt],['STABLE',D.st]], xs=[26,47,68], w=13, h=38, s=shadow(47,66,T), other=[T.c1,T.c2], oi=0;
    Q.forEach(function(q){
      var x=xs[Q.indexOf(q)], f=q[0]===hi?T.c3:other[oi++%2], lh=q[1]/66*(h-4), ly=FL-1.6-lh;
      var gl='M'+at(x-w/2)+' '+at(FL-h)+'V'+at(FL-1.6)+'A'+at(w/2)+' 1.4 0 0 0 '+at(x+w/2)+' '+at(FL-1.6)+'V'+at(FL-h);
      s+=E(x,FL-.3,w/2+2.2,1.5,T.n2)+P(gl+'Z',T.paper,op(T.dark?.18:.55));
      s+=P('M'+at(x-w/2+.5)+' '+at(ly)+'V'+at(FL-1.6)+'A'+at(w/2-.5)+' 1.2 0 0 0 '+at(x+w/2-.5)+' '+at(FL-1.6)+'V'+at(ly)+'Z',f)+E(x,ly,w/2-.5,1.2,tint(f,.28));
      if(q[0]===hi) for(var b=0;b<6;b++) s+=C(x-3.4+D.r()*6.8,ly+2+D.r()*Math.max(1,lh-3.4),.35+D.r()*.5,tint(f,.55));
      s+=SK(gl,T.ink,.4)+E(x,FL-h,w/2,1.4,'none',' stroke="'+T.ink+'" stroke-width=".4"');
      for(var k=1;k<6;k++){var ty=FL-1.6-k*(h-4)/6; s+=Ln(x+w/2-.6,ty,x+w/2-(k%2?2:3.2),ty,T.ink,.26);}
      s+=TX(x,FL-h-3,q[0],2.6,T.ink,{w:700});
    });
    s+=person(88,FL,T,{pose:'point',face:-1});
    return {svg:s,cap:capShare(D,hi)};
  });

  scene('hotair','열기구',['ALT','PRICE'],function(D,F){return F==='PRICE'?D.b1m!=null:D.alt!=null;},/떠올|띄|상승|날아|하늘|높이/,function(D,T,F){
    var d=F==='PRICE'?(D.b1m!=null?D.b1m/12:0):(D.dA||0), cx=56, cy=92-clamp(d*6,0,3), s='', cl=T.dark?mixc(T.bg,T.ink,.2):'#FFFFFF';
    s+=cloud(10,99,1.15,cl,op(.9))+cloud(73,114,.95,cl,op(.85))+cloud(80,84,.6,cl,op(.7));
    s+=shadow(cx,9,T,T.dark?.2:.05);
    var env='M'+at(cx-14)+' '+at(cy)+'C'+at(cx-14)+' '+at(cy-19)+' '+at(cx+14)+' '+at(cy-19)+' '+at(cx+14)+' '+at(cy)+'C'+at(cx+14)+' '+at(cy+8)+' '+at(cx+5)+' '+at(cy+13)+' '+at(cx+4)+' '+at(cy+17)+'H'+at(cx-4)+'C'+at(cx-5)+' '+at(cy+13)+' '+at(cx-14)+' '+at(cy+8)+' '+at(cx-14)+' '+at(cy)+'Z';
    function lens(k){return 'M'+at(cx)+' '+at(cy-14.25)+'C'+at(cx+k*19)+' '+at(cy-14)+' '+at(cx+k*19)+' '+at(cy+8)+' '+at(cx+k*5)+' '+at(cy+17)+'H'+at(cx-k*5)+'C'+at(cx-k*19)+' '+at(cy+8)+' '+at(cx-k*19)+' '+at(cy-14)+' '+at(cx)+' '+at(cy-14.25)+'Z';}
    s+=P(env,T.c1)+P(lens(.7),T.c2)+P(lens(.28),T.c3)+P(env,'none',' stroke="'+shade(T.c1,.25)+'" stroke-width=".3"');
    s+=E(cx-7.5,cy-7,2.2,4.2,'#FFFFFF',op(.22)+' transform="rotate(24 '+at(cx-7.5)+' '+at(cy-7)+')"');
    s+=Ln(cx-4,cy+17,cx-3.2,cy+21,T.ink,.25)+Ln(cx+4,cy+17,cx+3.2,cy+21,T.ink,.25);
    s+=person(cx-.6,cy+25.2,T,{pose:'wave',s:.8});
    s+=R(cx-3.6,cy+21,7.2,4.4,shade(T.c2,.42),' rx=".6"')+R(cx-3.6,cy+21,7.2,1,shade(T.c2,.58))+R(cx+3.7,cy+22.4,1.5,1.9,T.n3,' rx=".4"');
    return {svg:s,cap:F==='PRICE'?capPrice(D):capShare(D,'ALT')};
  });

  scene('honey','벌집',['ALT','MIX'],needAll,/계열|섹터|업종|벌집|분야|일부/,function(D,T,F){
    var hi=hiOf(D,F), v=shareOf(D,hi), r=4, w=Math.sqrt(3)*r, rows=5, cols=9, y0=85.5, cells=[], s='';
    var xs0=50-cols*w/2+w/2-w/4;
    s+=shadow(50,74,T)+Ln(19,117,17.4,FL,T.n3,.9)+Ln(81,117,82.6,FL,T.n3,.9);
    s+=R(13,y0-6.6,74,rows*1.5*r+8.2,T.n3,' rx="1.2"')+R(14.4,y0-5.2,71.2,rows*1.5*r+5.4,shade(T.c2,.52),' rx=".6"');
    for(var j=0;j<rows;j++) for(var i=0;i<cols;i++){var x=xs0+i*w+(j%2?w/2:0), y=y0+j*1.5*r; if(x+w/2>85.4||x-w/2<14.6) continue; cells.push([x,y]);}
    var n=Math.max(1,Math.round(v/100*cells.length)), c0=[57,y0+9];
    var order=cells.map(function(c,i){return [i,Math.hypot(c[0]-c0[0],(c[1]-c0[1])*1.3)+D.r()*3];}).sort(function(a,b){return a[1]-b[1];});
    var on={}, low=null; order.slice(0,n).forEach(function(o){on[o[0]]=1; var c=cells[o[0]]; if(!low||c[1]>low[1]||(c[1]===low[1]&&c[0]>low[0])) low=c;});
    cells.forEach(function(c,i){var hp=[]; for(var k=0;k<6;k++){var a=(60*k-90)*Math.PI/180; hp.push([c[0]+(r-.4)*Math.cos(a),c[1]+(r-.4)*Math.sin(a)]);}
      s+=PG(hp,on[i]?T.c3:(i%3?T.c2:tint(T.c2,.22)))+(on[i]?C(c[0]-1,c[1]-1.1,.8,'#FFFFFF',op(.4)):'');});
    if(low) s+=P('M'+at(low[0]-1)+' '+at(low[1]+r-.6)+'C'+at(low[0]-1)+' '+at(low[1]+r+2.5)+' '+at(low[0]-1.8)+' '+at(low[1]+r+3.6)+' '+at(low[0])+' '+at(low[1]+r+5.2)+'C'+at(low[0]+1.8)+' '+at(low[1]+r+3.6)+' '+at(low[0]+1)+' '+at(low[1]+r+2.5)+' '+at(low[0]+1)+' '+at(low[1]+r-.6)+'Z',T.c3);
    var bee=E(0,0,1.9,1.25,T.c3)+R(-.5,-1.2,.5,2.4,T.ink)+R(.6,-1.15,.45,2.3,T.ink)+E(-.3,-1.6,1.1,.7,'#FFFFFF',op(.8))+E(.6,-1.7,1,.6,'#FFFFFF',op(.7))+C(1.8,-.1,.35,T.ink);
    s+=G(bee,'translate(88 81) rotate(-12)')+SK('M78 88q3 -1 4 -4t5 -2',T.ink,.2,' stroke-dasharray=".6 .6"'+op(.5));
    s+=person(8.4,FL,T,{pose:'point'});
    return {svg:s,cap:capShare(D,hi)};
  });

  scene('kites','연날리기',['ALT'],needHist(3),/꼬리|연날리|바람|날렸|날아/,function(D,T,F){
    var H=histN(D,F,5), N=H.length, S=span(H,.4), o={pose:'hold'}, hd=handOf(14,FL,o), s=shadow(14,10,T), cols=[T.c1,T.c2];
    var K=H.map(function(h,i){return [36+52*i/(N-1), scaleY(h.v,S,84.5,103)];});
    K.forEach(function(k){s+=SK('M'+at(hd[0])+' '+at(hd[1])+'Q'+at((hd[0]+k[0])/2)+' '+at(Math.max(hd[1],k[1])-2)+' '+at(k[0])+' '+at(k[1]+3),T.ink,.16,op(.55));});
    K.forEach(function(k,i){var L=i===N-1, sc=L?1.6:1.25, f=L?T.c3:cols[i%2], rot=(i%2?10:-8), tl=L?13:9;
      var tail='M0 5.2'; for(var t=1;t<=6;t++){tail+='Q'+at(t%2?1.6:-1.6)+' '+at(5.2+tl*(t-.5)/6)+' 0 '+at(5.2+tl*t/6);}
      var bows=''; for(var b=1;b<=3;b++){var by=5.2+tl*b/3.4; bows+=PG([[-1,by-.6],[1,by+.6],[1,by-.6],[-1,by+.6]],b%2?T.c3:T.c2);}
      s+=G(SK(tail,T.ink,.22)+bows+PG([[0,-4.8],[3.4,-1],[0,5.2],[-3.4,-1]],f)+PG([[0,-4.8],[3.4,-1],[0,5.2]],shade(f,.14))+PG([[-3.4,-1],[0,-1],[0,5.2]],tint(f,.2))
        +Ln(0,-4.8,0,5.2,shade(f,.4),.2)+Ln(-3.4,-1,3.4,-1,shade(f,.4),.2),'translate('+at(k[0])+' '+at(k[1])+') rotate('+rot+') scale('+sc+')');});
    s+=person(14,FL,T,o);
    return {svg:s,cap:capShare(D,'ALT')};
  });

  scene('seesaw','시소',['MIX','ALT','BTC'],function(D){return D.dA!=null&&D.alt!=null;},/기울|무게|쏠|균형|시소|저울/,function(D,T,F){
    var ang=clamp(D.dA*30,-11,11), px=50, py=FL-11, s=shadow(50,86,T);
    s+=PG([[px,py+.6],[px-6.4,FL],[px+6.4,FL]],T.n3)+C(px,py+.6,1.1,shade(T.n3,.3));
    var pl=R(-39,-2.2,78,2.2,T.c2)+R(-39,0,78,.9,shade(T.c2,.3));
    pl+=coinFace(-30,-10.4,8.2,T.c1,'BTC',T.c1Ink);
    for(var i=0;i<5;i++) pl+=coinFlat(29.5+(i%2?.6:-.4),-5.4-i*1.5,5.2,1.7,1.5,T.c3);
    pl+=TX(29.5,-14.4,'ALT',3,T.ink,{w:800});
    s+=G(pl,'translate('+px+' '+py+') rotate('+at(ang)+')');
    s+=person(92.4,FL,T,{face:-1});
    return {svg:s,cap:F==='BTC'?capShare(D,'BTC'):capShare(D,'ALT')};
  });
