
  /* ---- ΣSTABLECOIN.D: cash waiting on the side, and whether it is flowing out or in ---- */
  function lvS(v){return clamp((v-7.5)/(11-7.5),.1,.94);}
  scene('tank','수조',['STABLE'],function(D){return D.st!=null;},/수위|채워|차올|빠져|말라|고였/,function(D,T,F){
    var x=30, y=83, w=40, h=40, dx=7.4, dy=-4.8, base=123, f=lvS(D.st), ly=base-h*f, s=shadow(52,58,T), ink=T.ink;
    var acc=T.c1, top=tint(acc,.35), deep=shade(acc,.2);
    s+=P('M'+x+' '+y+'L'+at(x+dx)+' '+at(y+dy)+'H'+at(x+w+dx)+'V'+at(base+dy),'none',' stroke="'+ink+'" stroke-width=".22"'+op(.45))
      +P('M'+at(x+dx)+' '+at(y+dy)+'V'+at(base+dy)+'H'+at(x+w+dx),'none',' stroke="'+ink+'" stroke-width=".16"'+op(.25));
    s+=P('M'+at(x+w)+' '+at(ly)+'L'+at(x+w+dx)+' '+at(ly+dy)+'V'+at(base+dy)+'L'+at(x+w)+' '+base+'Z',deep,op(.92))
      +P('M'+x+' '+at(ly)+'L'+at(x+dx)+' '+at(ly+dy)+'H'+at(x+w+dx)+'L'+at(x+w)+' '+at(ly)+'Z',top)
      +R(x,ly,w,base-ly,acc,op(.94));
    if(D.dS!=null){var py=base-h*lvS(D.st-D.dS); s+=Ln(x-3,py,x+w,py,ink,.3,' stroke-dasharray="1 .8"'+op(.75));}
    if(D.dS!=null && D.dS<-0.03){
      var k=clamp(-D.dS/0.5,.25,1), sx=x+w+dx*.35, sy=base-3.2;
      s+=P('M'+at(x+w)+' '+at(sy-1)+'H'+at(sx+5)+'V'+at(sy+1)+'H'+at(x+w)+'Z',T.n3)
        +P('M'+at(sx+5)+' '+at(sy-.2)+'C'+at(sx+8)+' '+at(sy)+' '+at(sx+8.6)+' '+at(sy+2)+' '+at(sx+8.8)+' 124','none',' stroke="'+T.c3+'" stroke-width="'+at(.8+1.4*k)+'" stroke-linecap="round"')
        +E(sx+9.4,124.4,2+3.5*k,.9,T.c3,op(.85));
    } else if(D.dS!=null && D.dS>0.03){
      var k2=clamp(D.dS/0.5,.25,1), px=x+w*.3;
      s+=P('M'+(x-9)+' 79.4H'+at(px+1)+'V82H'+(x-9)+'Z',T.n3)+Ln(px-.1,82,px-.1,ly-.5,T.c3,at(.8+1.4*k2));
    }
    s+=P('M'+x+' '+y+'L'+at(x+dx)+' '+at(y+dy)+'H'+at(x+w+dx)+'L'+at(x+w)+' '+y+'Z',T.paper,op(.22))
      +R(x,y,w,h,'none',' stroke="'+ink+'" stroke-width=".38"')
      +P('M'+at(x+w)+' '+y+'L'+at(x+w+dx)+' '+at(y+dy)+'V'+at(base+dy)+'L'+at(x+w)+' '+base,'none',' stroke="'+ink+'" stroke-width=".3"')
      +P('M'+x+' '+y+'L'+at(x+dx)+' '+at(y+dy)+'H'+at(x+w+dx),'none',' stroke="'+ink+'" stroke-width=".3"')
      +R(x+2.2,y+2.4,1.1,h-6,'#FFFFFF',op(.42));
    s+=person(x-7.5,FL,T);
    return {svg:s,cap:capShare(D,'STABLE')};
  });

  scene('hourglass','모래시계',['STABLE'],function(D){return D.st!=null;},/멈췄|멈춰|시간|남은|하루 만에|기다|천천히/,function(D,T,F){
    var cx=44, t0=FL-41, b0=FL-4, nk=(t0+b0)/2, lvl=clamp((D.st-7.5)/3.5,.12,.92), s=shadow(cx+6,44,T);
    var top='M'+at(cx-11)+' '+at(t0)+'C'+at(cx-11)+' '+at(t0+12)+' '+at(cx-1.6)+' '+at(nk-4)+' '+at(cx-.9)+' '+at(nk)+'H'+at(cx+.9)+'C'+at(cx+1.6)+' '+at(nk-4)+' '+at(cx+11)+' '+at(t0+12)+' '+at(cx+11)+' '+at(t0)+'Z';
    var bot='M'+at(cx-11)+' '+at(b0)+'C'+at(cx-11)+' '+at(b0-12)+' '+at(cx-1.6)+' '+at(nk+4)+' '+at(cx-.9)+' '+at(nk)+'H'+at(cx+.9)+'C'+at(cx+1.6)+' '+at(nk+4)+' '+at(cx+11)+' '+at(b0-12)+' '+at(cx+11)+' '+at(b0)+'Z';
    s+=box(cx-17,t0-3.4,34,3.4,6,T.c2)+R(cx-15.6,t0,1.8,b0-t0,T.n3)+R(cx+13.8,t0,1.8,b0-t0,T.n3);
    s+=P(top,T.paper,op(T.dark?.2:.6))+P(bot,T.paper,op(T.dark?.2:.6));
    var sy=nk-(nk-t0)*lvl, heap=(1-lvl)*13+3;
    s+=clip(top,R(cx-12,sy,24,nk-sy+.5,T.c3)+E(cx,sy,11,1.2,tint(T.c3,.3)));
    s+=clip(bot,P('M'+at(cx-12)+' '+at(b0)+'Q'+at(cx)+' '+at(b0-heap*2)+' '+at(cx+12)+' '+at(b0)+'Z',T.c3));
    if(D.dS!=null&&D.dS<-0.01) s+=Ln(cx,nk,cx,b0-heap+.6,T.c3,clamp(-D.dS*3,.35,1.1));
    s+=SK(top,T.ink,.38)+SK(bot,T.ink,.38)+box(cx-17,b0,34,FL-b0,6,T.c2);
    s+=box(66,FL-3.6,7,3.6,4,T.n2)+person(69,FL-3.6,T,{pose:'sit',face:-1});
    return {svg:s,cap:capShare(D,'STABLE')};
  });

  scene('faucet','수도꼭지',['STABLE','BTC','ALT'],function(D){return D.st!=null&&D.dS!=null;},/쏟아|흘러|받았|유입|나오|나왔|빠져나|새어/,function(D,T,F){
    var dS=D.dS, out=dS<-0.02, wv=out?clamp(-dS*5,.8,3.4):0, recv=(F==='BTC'||F==='ALT')?F:null, s=shadow(49,48,T);
    var pipe=T.n3, lab=inkOn(pipe);
    s+=R(3.2,83.2,34,5.6,pipe)+R(3.2,83.2,34,1.3,tint(pipe,.22))+R(24.4,82,2.6,8,shade(pipe,.25))+TX(13.6,87.5,'현금',3.2,lab,{ff:'g',w:800});
    s+=P('M37 83.2H45Q51 83.2 51 89.2V93H45.6V89.6Q45.6 88.8 44.8 88.8H37Z',pipe)+R(44.9,92.2,6.8,1.6,shade(pipe,.3),' rx=".5"');
    s+=R(39.5,79.6,1.4,3.8,shade(pipe,.2))+R(36.1,78.3,8.2,1.5,T.c3,' rx=".7"');
    var tubTop=FL-18, bottom=recv?tubTop+1:FL-.6;
    if(out) s+=R(48.3-wv/2,93.6,wv,bottom-93.6,T.c1,op(.92))+R(48.3-wv/2+wv*.2,93.6,wv*.2,bottom-93.6,tint(T.c1,.4),op(.8));
    else s+=E(48.3,95.6,.45,.75,T.c1)+E(48.3,99.2,.45,.75,T.c1,op(.7));
    if(recv){
      s+=PG([[33,tubTop],[63.6,tubTop],[60.6,FL],[36,FL]],T.c2)+PG([[55,tubTop],[63.6,tubTop],[60.6,FL],[53.6,FL]],shade(T.c2,.12));
      s+=E(48.3,tubTop,15.3,2.4,shade(T.c2,.3))+E(48.3,tubTop+.35,13.9,1.9,T.c1);
      if(out) s+=E(48.3,tubTop+.3,2.4+wv,.8,tint(T.c1,.5));
      s+=TX(48.3,FL-6.4,recv,5.2,T.c2Ink,{w:800});
    } else if(out) s+=E(51,FL-.2,6+wv*3,1.2,T.c1,op(.9));
    s+=person(31,83.2,T,{pose:'hold'});
    return {svg:s,cap:recv?capShare(D,recv):capShare(D,'STABLE')};
  });

  scene('dam','댐',['STABLE'],function(D){return D.st!=null;},/댐|막혔|수문|가뒀|묶|쏟아/,function(D,T,F){
    var wy=FL-6-lvS(D.st)*32, s='';
    s+=R(3.2,wy,41,FL-wy,T.c1)+R(3.2,wy,41,1.1,tint(T.c1,.45));
    for(var i=0;i<4;i++) s+=SK('M'+at(7+i*9)+' '+at(wy+4+i*5.2)+'q2 -1 4 0t4 0',tint(T.c1,.35),.35);
    if(D.dS!=null){var py=FL-6-lvS(D.st-D.dS)*32; s+=Ln(3.2,py,43,py,T.ink,.3,' stroke-dasharray="1 .8"'+op(.6));}
    s+=R(57,FL-1.5,39.8,1.5,tint(T.c1,.25));
    if(D.dS!=null&&D.dS<-0.02){
      var k=clamp(-D.dS*2.2,.45,1.4);
      [FL-9,FL-17].forEach(function(gy,j){var gx=50+(gy-(FL-41))/41*13; s+=SK('M'+at(gx)+' '+at(gy)+'C'+at(gx+7)+' '+at(gy-1)+' '+at(gx+11)+' '+at(gy+4)+' '+at(gx+12+j*3)+' '+at(FL-.8),tint(T.c1,.3),at(k*(2-j*.5)));
        for(var q=0;q<4;q++) s+=C(gx+11+j*3+(D.r()-.5)*5,FL-1.2-D.r()*1.6,.5+D.r()*.8,'#FFFFFF',op(.85));});
    }
    s+=PG([[44,FL-41],[50,FL-41],[63,FL],[44,FL]],T.n1)+PG([[50,FL-41],[63,FL],[57.5,FL]],shade(T.n1,.12));
    for(var g=0;g<3;g++){var yy=FL-10-g*8; s+=R(46,yy,2.4,2.4,shade(T.n1,.35));}
    s+=R(42.6,FL-42.4,8.8,1.6,shade(T.n1,.18))+Ln(42.8,FL-45,51.2,FL-45,T.n3,.3);
    [43,45.8,48.6,51.2].forEach(function(x){s+=Ln(x,FL-45,x,FL-42.4,T.n3,.3);});
    s+=person(47.6,FL-42.4,T,{face:-1});
    return {svg:s,cap:capShare(D,'STABLE')};
  });

  scene('vault','금고',['STABLE'],function(D){return D.st!=null;},/금고|잠겼|잠가|묶인|보관|지켰/,function(D,T,F){
    var open=D.dS!=null&&D.dS<-0.02, bx=12, by=FL-40, bw=46, bh=40, cx=bx+bw/2, cy=by+bh/2, s=shadow(40,62,T);
    s+=box(bx,by,bw,bh,10,T.c1)+R(bx+2,by+2,bw-4,bh-4,'none',' stroke="'+shade(T.c1,.2)+'" stroke-width=".4"')+C(cx,cy,15.4,shade(T.c1,.22));
    if(open){
      s+=C(cx,cy,13.6,shade(T.c1,.62));
      for(var i=0;i<3;i++) s+=box(cx-8+i*5.4,cy+5,4.6,2.6,3,T.c3);
      for(var j=0;j<2;j++) s+=box(cx-5.3+j*5.4,cy+2.4,4.6,2.6,3,T.c3);
      var dxp=cx+15.4;
      s+=E(dxp+4.4,cy,4.4,15.2,shade(T.c1,.32))+E(dxp+3.6,cy,3.4,13.6,tint(T.c1,.1))+Ln(dxp+3.6,cy-7.5,dxp+3.6,cy+7.5,T.c3,.9)+C(dxp+3.6,cy,1.3,T.c3);
      [[66,0],[71.5,.4],[64,1]].forEach(function(q){s+=coinFlat(q[0],FL-1.6-q[1],2.4,.8,.7,T.c3);});
      var o={pose:'hold',face:-1}, hd=handOf(84,FL,o);
      s+=person(84,FL,T,o)+coinFace(hd[0]-1.4,hd[1]-.8,1.7,T.c3);
    } else {
      s+=C(cx,cy,13.6,tint(T.c1,.12));
      for(var b=0;b<8;b++){var a=b*45*Math.PI/180; s+=C(cx+Math.cos(a)*11.6,cy+Math.sin(a)*11.6,.7,shade(T.c1,.3));}
      for(var k=0;k<3;k++){var a2=(k*60+15)*Math.PI/180; s+=Ln(cx-Math.cos(a2)*7.5,cy-Math.sin(a2)*7.5,cx+Math.cos(a2)*7.5,cy+Math.sin(a2)*7.5,T.c3,.95);}
      s+=C(cx,cy,2.2,T.c3)+C(cx,cy,.9,shade(T.c3,.3));
      s+=person(76,FL,T,{pose:'point',face:-1});
    }
    return {svg:s,cap:capShare(D,'STABLE')};
  });

  scene('piggy','돼지 저금통',['STABLE'],function(D){return D.st!=null;},/저축|모아|모았|적립|쌓아|저금|아껴/,function(D,T,F){
    var cx=46, cy=FL-17.5, f=T.c1, s=shadow(cx,48,T);
    [[31,1],[39,0],[53,1],[60,0]].forEach(function(q){s+=R(q[0],FL-8,4.6,8,shade(f,q[1]?.14:.26),' rx="1"');});
    s+=SK('M66.4 '+at(cy-2)+'q3 -1.4 2.6 -3.6q-.4 -1.8 -2 -.8q-1.2 1 .8 2',shade(f,.15),.7);
    s+=E(cx,cy,21,14,shade(f,.12))+E(cx-.8,cy-1.4,20,12.4,f)+E(cx-8,cy-7.4,6.5,2.4,'#FFFFFF',op(.22)+' transform="rotate(-16 '+at(cx-8)+' '+at(cy-7.4)+')"');
    s+=PG([[30.5,cy-10.5],[32.6,cy-18.6],[37,cy-12.4]],shade(f,.16))+PG([[36.4,cy-12.8],[40.2,cy-19.8],[43,cy-13.4]],f);
    s+=E(25.6,cy+.4,3.4,4.6,shade(f,.1))+E(24.8,cy-1,.55,1,shade(f,.5))+E(24.8,cy+1.9,.55,1,shade(f,.5));
    s+=C(31.6,cy-4.4,.95,T.ink)+C(31.3,cy-4.7,.3,'#FFFFFF');
    s+=R(43.4,cy-14,9,1.2,shade(f,.55),' rx=".6"');
    if(D.dS!=null&&D.dS>0.01) s+=E(47.9,cy-17.6,1.1,3.2,T.c3)+E(47.6,cy-17.6,.5,2.6,tint(T.c3,.3));
    else if(D.dS!=null&&D.dS<-0.01) [[38,0],[43.5,.3],[55,.1]].forEach(function(q){s+=coinFlat(q[0],FL-1.4-q[1],2.3,.8,.7,T.c3);});
    var o={pose:'hold',face:-1}, hd=handOf(80,FL,o);
    s+=person(80,FL,T,o)+coinFace(hd[0]-1.3,hd[1]-.8,1.7,T.c3);
    return {svg:s,cap:capShare(D,'STABLE')};
  });

  scene('umbrella','우산',['STABLE'],function(D){return D.st!=null;},/피난|대피|안전|방어|피신|버텼|비가|쏟아지/,function(D,T,F){
    var cx=50, hw=clamp(17+(D.st-8)*3.4,16,27), top=FL-45, rim=FL-28, s=shadow(cx,hw*2+4,T), rc=T.dark?T.n0:shade(T.c2,.25);
    for(var i=0;i<38;i++){var x=6+D.r()*88, y=76+D.r()*46; if(Math.abs(x-cx)<hw+1.5 && y>top-1) continue; s+=Ln(x,y,x-.8,y+2.4,rc,.32,op(.8));}
    var n=6, P2=[]; for(var k=0;k<=n;k++){var t=k/n; P2.push([cx-hw+2*hw*t, rim-Math.sin(t*Math.PI)*1.8]);}
    var dome='M'+at(cx-hw)+' '+at(rim)+'C'+at(cx-hw)+' '+at(top+3)+' '+at(cx-hw*.45)+' '+at(top-.4)+' '+at(cx)+' '+at(top)+'C'+at(cx+hw*.45)+' '+at(top-.4)+' '+at(cx+hw)+' '+at(top+3)+' '+at(cx+hw)+' '+at(rim);
    for(var k2=n-1;k2>=0;k2--){var a=P2[k2+1], b=P2[k2]; dome+='Q'+at((a[0]+b[0])/2)+' '+at(Math.max(a[1],b[1])-2.4)+' '+at(b[0])+' '+at(b[1]);}
    s+=Ln(cx,top-3,cx,FL-4.4,T.n3,.75)+C(cx,top-3.2,.6,T.n3);
    s+=P(dome+'Z',T.c1);
    for(var g=1;g<n;g+=2){var a1=P2[g], b1=P2[g+1];
      s+=P('M'+at(cx)+' '+at(top)+'Q'+at(cx+(a1[0]-cx)*.95)+' '+at(top+(rim-top)*.3)+' '+at(a1[0])+' '+at(a1[1])+'Q'+at((a1[0]+b1[0])/2)+' '+at(Math.max(a1[1],b1[1])-2.4)+' '+at(b1[0])+' '+at(b1[1])+'Q'+at(cx+(b1[0]-cx)*.95)+' '+at(top+(rim-top)*.3)+' '+at(cx)+' '+at(top)+'Z',T.c2);}
    s+=SK('M'+at(cx)+' '+at(FL-4.4)+'Q'+at(cx)+' '+at(FL-1.6)+' '+at(cx+2.2)+' '+at(FL-1.6)+'Q'+at(cx+4.2)+' '+at(FL-1.8)+' '+at(cx+4.2)+' '+at(FL-3.6),T.n3,.8);
    var o={pose:'hold'}, hd=handOf(0,FL,o);
    s+=person(cx-hd[0]-.2,FL,T,o);
    return {svg:s,cap:capShare(D,'STABLE')};
  });
