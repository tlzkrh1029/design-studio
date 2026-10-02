
  /* ================= pictures =================
     scene(id, Korean name, focuses it can show (first = main one), data it needs, words in the headline
     that call for it, drawing). Each drawing returns the SVG and the caption shown under it. */
  function needHist(n){return function(D,F){return histN(D,F,9).length>=n;};}
  function needShare(D,F){return shareOf(D,F)!=null;}
  function needAll(D){return D.alt!=null;}
  function always(){return true;}
  function PLx(p,s,w,x){return '<polyline points="'+pts(p)+'" fill="none" stroke="'+s+'" stroke-width="'+w+'" stroke-linejoin="miter" stroke-miterlimit="6"'+(x||'')+'/>';}
  function onPaper(c,bgc){bgc=bgc||'#FFFFFF'; for(var t=0;t<=0.9;t+=0.06){var x=mixc(c,'#000000',t); if(cr(x,bgc)>=4.5) return x;} return '#17181A';}
  function inkOn(f){return cr('#FFFFFF',f)>=cr('#17181A',f)?'#FFFFFF':'#17181A';}
  function ball(x,y,r,c){return C(x,y,r,shade(c,.22))+C(x-r*.09,y-r*.09,r*.9,c)+E(x-r*.4,y-r*.42,r*.26,r*.15,'#FFFFFF',op(.38)+' transform="rotate(-35 '+at(x-r*.4)+' '+at(y-r*.42)+')"');}

  /* ---- BTC.D: how big bitcoin's share is and where it has been going ---- */
  scene('stairs','계단',['BTC','ALT'],needHist(2),/계단|내려앉|한 단|층계/,function(D,T,F){
    var H=histN(D,F,9), N=H.length, S=span(H,F==='ALT'?.4:.5), bw=6.4, gap=1.3, d=4.2, dx=d*DX, dy=d*DY, step=bw+gap;
    var total=N*step-gap+dx, x0=50-total/2, s=shadow(50,total+6,T), last=null;
    H.forEach(function(h,i){
      var hh=7+(h.v-S.lo)/S.rg*31, x=x0+i*step, y=FL-hh, L=i===N-1;
      s+=box(x,y,bw,hh,d,L?T.c3:mixc(T.c2,T.c1,N>2?i/(N-2):1));
      if(L) last={x:x,y:y};
    });
    s+=person(last.x+bw/2+dx/2,last.y+dy/2,T);
    return {svg:s,cap:capShare(D,F)};
  });

  scene('skyline','빌딩 숲',['BTC','ALT'],needHist(3),/대형주|빌딩|마천루|대형/,function(D,T,F){
    var H=histN(D,F,9), N=H.length, S=span(H,.5), W=82, gap=1.2, bw=(W-gap*(N-1))/N, x0=9, s='', top=1e9, ti=0, last;
    var hs=H.map(function(h){return 13+(h.v-S.lo)/S.rg*30;});
    hs.forEach(function(hh,i){ if(FL-hh<top){top=FL-hh; ti=i;} });
    s+=C(77,86,8,T.c2)+shadow(50,W+4,T);
    H.forEach(function(h,i){
      var hh=hs[i], x=x0+i*(bw+gap), y=FL-hh, L=i===N-1, f=L?T.c3:(i%2?T.c1:shade(T.c1,.14));
      if(i===ti&&!L) s+=Ln(x+bw/2,y,x+bw/2,y-6,f,.5)+C(x+bw/2,y-6.2,.6,T.c3);
      if(i%3===1&&!L) s+=R(x+bw*.25,y-2.4,bw*.5,2.4,f);
      s+=R(x,y,bw,hh,f);
      var cols=Math.max(1,Math.floor((bw-1.2)/2)), ox=x+(bw-(cols*2-1.05))/2, rows=Math.max(1,Math.floor((hh-3.6)/3.1)), wc=L?tint(T.c3,.75):T.bg;
      for(var r=0;r<rows;r++) for(var c=0;c<cols;c++){ if(D.r()<(L?.9:.72)) s+=R(ox+c*2,y+2.2+r*3.1,.95,1.6,wc,op(L?.95:.5)); }
      if(L) last={x:x,y:y};
    });
    s+=person(last.x+bw/2,last.y,T,{pose:'wave'});
    return {svg:s,cap:capShare(D,F)};
  });

  scene('mountain','산맥',['BTC','ALT','PRICE'],needHist(3),/고점|정상|봉우리|최고|최저|꼭대기/,function(D,T,F){
    var H=histN(D,F,7), N=H.length, S=span(H,.4), x0=3.2, x1=96.8, s='';
    var pk=H.map(function(h,i){return [15+70*(N===1?.5:i/(N-1)), FL-13-(h.v-S.lo)/S.rg*30];});
    var ridge=[[x0,FL]];
    pk.forEach(function(p,i){
      if(i>0){var q=pk[i-1]; ridge.push([(q[0]+p[0])/2+(D.r()-.5)*2, Math.max(q[1],p[1])+5+D.r()*5]);}
      else ridge.push([x0+4,FL-6-D.r()*3]);
      ridge.push(p);
    });
    ridge.push([x1-3,FL-7-D.r()*4]); ridge.push([x1,FL]);
    var back=[[x0,FL]]; for(var i=0;i<7;i++){ back.push([x0+4+i*14+D.r()*4, FL-20-D.r()*16]); back.push([x0+11+i*14+D.r()*3, FL-10-D.r()*6]); } back.push([x1,FL]);
    s+=C(80,85,6.5,T.c3)+PG(back,mixc(T.c2,T.bg,.35))+PG(ridge,T.c1);
    for(var j=1;j<ridge.length-2;j++){ var a=ridge[j], b=ridge[j+1]; if(b[1]>a[1]) s+=PG([a,b,[a[0]+(b[0]-a[0])*.35,FL]],shade(T.c1,.16)); }
    var snow=T.dark?tint(T.c1,.65):'#FFFFFF';
    pk.forEach(function(p){
      if((FL-13-p[1])/30<.45) return;
      var k=ridge.indexOf(p), l=ridge[k-1], r=ridge[k+1], t=.3;
      var L1=[p[0]+(l[0]-p[0])*t,p[1]+(l[1]-p[1])*t], R1=[p[0]+(r[0]-p[0])*t,p[1]+(r[1]-p[1])*t];
      s+=PG([p,R1,[(p[0]+R1[0])/2,R1[1]-1.3],[p[0]+.2,(p[1]+R1[1])/2+1.2],[(p[0]+L1[0])/2,L1[1]-1.1],L1],snow,op(.94));
    });
    var lp=pk[N-1], k=ridge.indexOf(lp), vl=ridge[k-1];
    s+=Ln(lp[0],lp[1]+.2,lp[0],lp[1]-8,T.ink,.36)+PG([[lp[0],lp[1]-8],[lp[0]+4.6,lp[1]-6.7],[lp[0],lp[1]-5.4]],T.c3);
    var fx=lp[0]+(vl[0]-lp[0])*.34, fy=lp[1]+(vl[1]-lp[1])*.34;
    s+=person(fx,fy+.3,T,{pose:'run',lean:20});
    return {svg:s,cap:F==='PRICE'?capPrice(D):capShare(D,F)};
  });

  scene('ladder','사다리',['BTC','ALT'],needShare,/사다리|올라서|올라섰|기어/,function(D,T,F){
    var v=shareOf(D,F), g=F==='ALT'?[28,35]:[56,63], t=clamp((v-g[0])/(g[1]-g[0]),0,1);
    var r=21, cx=31, cy=FL-r, s=shadow(42,54,T);
    s+=coinFace(cx,cy,r,T.c3,F==='ALT'?'ALT':'BTC',T.c3Ink);
    var bx=72, by=FL, tx=50.2, ty=FL-35, off=4.4, n=11;
    s+=Ln(bx,by,tx,ty,shade(T.c1,.12),.95);
    for(var i=1;i<=n;i++){var k=i/(n+.7), y=by+(ty-by)*k, x=bx+(tx-bx)*k; s+=Ln(x,y,x+off,y,T.c1,.62);}
    s+=Ln(bx+off,by,tx+off,ty,T.c1,.95);
    var k2=.1+.74*t, fy=by+(ty-by)*k2, fx=bx+(tx-bx)*k2+off*.5;
    s+=Ln(cx+r*.4,fy-4.7,fx-2.4,fy-4.7,T.ink,.28,' stroke-dasharray=".9 .9"'+op(.7));
    s+=person(fx+.4,fy,T,{pose:'climb',face:-1});
    return {svg:s,cap:capShare(D,F)};
  });

  var GR={BTC:[55,65],ALT:[27,35],STABLE:[7.5,11]};
  scene('gauge','계기판',['BTC','ALT','STABLE'],needShare,/교차|과열|계기|HMA|이동평균|속도/,function(D,T,F){
    var v=shareOf(D,F), d=dOf(D,F), g=GR[F], cx=50, cy=FL-9, R0=33, R1=25, s='', ink='#17181A';
    var ang=function(x){return 180+180*clamp((x-g[0])/(g[1]-g[0]),0,1);}, pt=function(a,r){var q=a*Math.PI/180; return [cx+r*Math.cos(q),cy+r*Math.sin(q)];};
    s+=shadow(52,80,T)+box(14,cy,72,FL-cy,5,T.n2);
    s+=P('M'+at(cx-R0-3)+' '+at(cy)+'A'+at(R0+3)+' '+at(R0+3)+' 0 0 1 '+at(cx+R0+3)+' '+at(cy)+'Z',T.c1);
    s+=P('M'+at(cx-R0-.6)+' '+at(cy)+'A'+at(R0+.6)+' '+at(R0+.6)+' 0 0 1 '+at(cx+R0+.6)+' '+at(cy)+'Z',T.paper);
    for(var i=0;i<5;i++){var a0=180+36*i+.8, a1=180+36*(i+1)-.8, o0=pt(a0,R0-1.5), o1=pt(a1,R0-1.5), i1=pt(a1,R1), i0=pt(a0,R1);
      s+=P('M'+at(o0[0])+' '+at(o0[1])+'A'+at(R0-1.5)+' '+at(R0-1.5)+' 0 0 1 '+at(o1[0])+' '+at(o1[1])+'L'+at(i1[0])+' '+at(i1[1])+'A'+R1+' '+R1+' 0 0 0 '+at(i0[0])+' '+at(i0[1])+'Z',mixc(T.c2,T.c3,i/4));}
    for(var j=0;j<=10;j++){var a=180+18*j, p0=pt(a,R1-1), p1=pt(a,R1-(j%5?2.6:4)); s+=Ln(p0[0],p0[1],p1[0],p1[1],ink,j%5?.25:.45);}
    s+=TX(cx-R1+5.6,cy-1.6,String(g[0]),2.6,ink,{ff:'n',w:500})+TX(cx+R1-5.6,cy-1.6,String(g[1]),2.6,ink,{ff:'n',w:500});
    if(d!=null){var pp=pt(ang(v-d),R1-3); s+=Ln(cx,cy,pp[0],pp[1],ink,.5,' stroke-dasharray="1 .8"'+op(.45));}
    var a2=ang(v)*Math.PI/180, tip=[cx+(R1-1.5)*Math.cos(a2),cy+(R1-1.5)*Math.sin(a2)], nx=-Math.sin(a2)*1.2, ny=Math.cos(a2)*1.2;
    s+=PG([[cx+nx,cy+ny],tip,[cx-nx,cy-ny],[cx-Math.cos(a2)*3,cy-Math.sin(a2)*3]],ink)+C(cx,cy,2.4,ink)+C(cx,cy,1,T.c3);
    s+=person(10.5,FL,T,{pose:'point'});
    return {svg:s,cap:capShare(D,F)};
  });

  scene('king','체스 킹',['BTC'],function(D){return D.btc!=null;},/왕좌|제자리|멈춰|지배|대장|왕/,function(D,T,F){
    var cx=36, dB=D.dB, tilt=dB!=null&&dB<-0.05?clamp(-dB*34,4,15):0, f=T.c1, s=shadow(52,82,T), k='';
    k+=cyl(cx,FL-4,11,2.8,4,f)+cyl(cx,FL-6.4,8.6,2.2,2.4,f);
    k+=P('M'+at(cx-7.4)+' '+at(FL-6.4)+'C'+at(cx-6.6)+' '+at(FL-14)+' '+at(cx-3.6)+' '+at(FL-20)+' '+at(cx-3.4)+' '+at(FL-27.5)+'H'+at(cx+3.4)+'C'+at(cx+3.6)+' '+at(FL-20)+' '+at(cx+6.6)+' '+at(FL-14)+' '+at(cx+7.4)+' '+at(FL-6.4)+'Z',f);
    k+=P('M'+at(cx+2.3)+' '+at(FL-6.4)+'C'+at(cx+3.2)+' '+at(FL-14)+' '+at(cx+1.8)+' '+at(FL-20)+' '+at(cx+1.5)+' '+at(FL-27.5)+'H'+at(cx+3.4)+'C'+at(cx+3.6)+' '+at(FL-20)+' '+at(cx+6.6)+' '+at(FL-14)+' '+at(cx+7.4)+' '+at(FL-6.4)+'Z',shade(f,.2));
    k+=cyl(cx,FL-29.4,6,1.5,1.8,f);
    k+=P('M'+at(cx-3.6)+' '+at(FL-29.4)+'L'+at(cx-5.4)+' '+at(FL-36)+'H'+at(cx+5.4)+'L'+at(cx+3.6)+' '+at(FL-29.4)+'Z',f)
      +P('M'+at(cx+1.6)+' '+at(FL-29.4)+'L'+at(cx+2.6)+' '+at(FL-36)+'H'+at(cx+5.4)+'L'+at(cx+3.6)+' '+at(FL-29.4)+'Z',shade(f,.2))+E(cx,FL-36,5.4,1.3,tint(f,.3));
    k+=R(cx-1,FL-43,2,7,T.c3)+R(cx-3.1,FL-40.9,6.2,2,T.c3);
    s+=tilt?G(k,'rotate('+at(tilt)+' '+at(cx+11)+' '+FL+')'):k;
    [[64,T.c2,1],[75,shade(T.c2,.12),.9],[85,T.c2,.8]].forEach(function(q){
      s+=G(cyl(0,-3,5.4,1.4,3,q[1])+P('M-3.6 -3C-3.2 -6 -1.8 -7.4 -1.6 -9H1.6C1.8 -7.4 3.2 -6 3.6 -3Z',q[1])+ball(0,-11,2.8,q[1]),'translate('+q[0]+' '+FL+') scale('+q[2]+')');});
    s+=person(cx-13.4,FL,T,{pose:tilt?'push':'stand'});
    return {svg:s,cap:capShare(D,'BTC')};
  });

  scene('coaster','롤러코스터',['BTC','ALT','PRICE'],needHist(4),/출렁|롤러|오르내|급등락|요동|널뛰/,function(D,T,F){
    var H=histN(D,F,8), N=H.length, S=span(H,.4), p=H.map(function(h,i){return [9+80*i/(N-1), scaleY(h.v,S,FL-40,FL-12)];}), s='';
    s+=shadow(50,84,T,T.dark?.25:.06);
    for(var x=11;x<=88;x+=5.5){var y=crY(p,x); s+=Ln(x,y+1,x,FL,T.n2,.55);}
    for(var x2=11;x2<83;x2+=5.5){var ya=crY(p,x2), yb=crY(p,x2+5.5); s+=Ln(x2,Math.max(ya,yb)+4,x2+5.5,FL-1,T.n2,.3);}
    var d=crPath(p);
    s+=SK(d,shade(T.c1,.25),2.6)+SK(d,T.c1,1.8)+SK(d,tint(T.c1,.5),.45,' transform="translate(0 -.55)"');
    var e=p[N-1], a=Math.atan2(e[1]-crY(p,e[0]-2),2)*180/Math.PI;
    var cart=fig(-.4,-1.6,{pose:'cheer',col:T.ink,s:.95})+R(-4.4,-4.4,8.8,3.8,T.c3,' rx="1"')+R(-4.4,-4.4,8.8,1.3,shade(T.c3,.12),' rx=".6"')+C(-2.6,-.4,.9,T.ink)+C(2.6,-.4,.9,T.ink);
    s+=G(cart,'translate('+at(e[0]-2)+' '+at(e[1]-1.2)+') rotate('+at(a)+')');
    return {svg:s,cap:F==='PRICE'?capPrice(D):capShare(D,F)};
  });

  var TR={BTC:[56,62],ALT:[28,34],STABLE:[8,11]};
  scene('thermo','온도계',['BTC','ALT','STABLE'],needShare,/과열|식었|식어|온도|열기|뜨거|차갑|달아/,function(D,T,F){
    var v=shareOf(D,F), d=dOf(D,F), g=TR[F], w=12, x=50-w/2, top=FL-47, br=9, by=FL-br-.5, jy=by-Math.sqrt(br*br-(w/2)*(w/2)), s=shadow(50,26,T);
    var outline='M'+at(x)+' '+at(top+w/2)+'A'+at(w/2)+' '+at(w/2)+' 0 0 1 '+at(x+w)+' '+at(top+w/2)+'V'+at(jy)+'A'+br+' '+br+' 0 1 1 '+at(x)+' '+at(jy)+'Z';
    s+=P(outline,T.paper);
    var lvl=function(val){return jy-2-(jy-2-(top+5))*clamp((val-g[0])/(g[1]-g[0]),0,1);}, ly=lvl(v);
    s+=R(x+3,ly,w-6,jy-ly+2,T.c3,' rx="3"')+C(50,by,br-2.6,T.c3)+R(x+3.6,ly+1,1.2,jy-ly-1,tint(T.c3,.4),' rx=".6"')+C(47.4,by-2.2,1.3,tint(T.c3,.4));
    s+=SK(outline,T.ink,.5);
    for(var i=0;i<=6;i++){var val=g[0]+(g[1]-g[0])*i/6, y=lvl(val); s+=Ln(x+w+.9,y,x+w+(i%2?2.2:3.4),y,T.ink,.3); if(i%2===0) s+=TX(x+w+4.6,y+.9,String(Math.round(val*10)/10),2.5,T.ink,{a:'start',ff:'n',w:500});}
    if(d!=null){var py=lvl(v-d); s+=PG([[x-.9,py],[x-3.3,py-1.3],[x-3.3,py+1.3]],T.ink,op(.7));}
    s+=person(x-10,FL,T,{pose:'point'});
    return {svg:s,cap:capShare(D,F)};
  });

  scene('stars','별자리',['BTC','ALT'],needHist(4),/관측|신호|빛|반짝|별/,function(D,T,F){
    var H=histN(D,F,7), N=H.length, S=span(H,.4), p=H.map(function(h,i){return [40+50*i/(N-1), scaleY(h.v,S,80,104)];}), s='';
    for(var i=0;i<18;i++) s+=C(7+D.r()*86,77+D.r()*32,.22+D.r()*.32,T.ink,op(.4));
    s+=C(13,82.5,4.2,T.c2)+C(14.8,81.3,3.6,T.bg);
    s+=PL(p,T.ink,.3,' stroke-dasharray="1 .9"'+op(.65));
    p.forEach(function(q,i){var L=i===N-1, r=L?3.6:1.5+D.r()*.7; if(L) s+=C(q[0],q[1],r*1.9,'none',' stroke="'+T.c3+'" stroke-width=".35"'+op(.8)); s+=star(q[0],q[1],r,L?T.c3:(i%2?T.c1:T.c2));});
    var tx=19.5, ty=FL-7.6, lp=p[N-1], a=Math.atan2(lp[1]-ty,lp[0]-tx)*180/Math.PI;
    s+=shadow(20,16,T)+Ln(tx,ty,tx-5,FL,T.n3,.55)+Ln(tx,ty,tx+4.4,FL,T.n3,.55)+Ln(tx,ty,tx+.4,FL,T.n3,.45);
    s+=G(R(-2.6,-1.3,2.6,2.6,shade(T.c2,.25))+R(0,-1.9,14,3.8,T.c2,' rx=".5"')+R(11.5,-2.4,3.2,4.8,shade(T.c2,.18),' rx=".4"')+R(3,-1.9,1.2,3.8,T.c3),'translate('+tx+' '+at(ty)+') rotate('+at(a)+')');
    s+=person(tx-3.9,FL,T,{pose:'hold'});
    return {svg:s,cap:capShare(D,F)};
  });

  scene('domino','도미노',['BTC','ALT'],function(D,F){var H=histN(D,F,9); return H.length>=4 && fallRun(H)>=2;},/연속|잇따|이틀|사흘|도미노|연거푸|갈아치/,function(D,T,F){
    var H=histN(D,F,9), N=H.length, S=span(H,.4), k=fallRun(H), gap=8.2, w=2.6, d=3.4, x0=46-((N-1)*gap+w)/2, s=shadow(48,N*gap+8,T);
    var hs=H.map(function(h){return 13+(h.v-S.lo)/S.rg*20;});
    for(var i=0;i<N;i++){
      var x=x0+i*gap, h=hs[i], falling=i>=N-1-k && i<N-1, L=i===N-1, f=L?T.c3:falling?T.c2:T.c1;
      var tile=box(0,-h,w,h,d,f)+C(w/2,-h*.74,.45,tint(f,.8))+C(w/2,-h*.26,.45,tint(f,.8))+Ln(.35,-h/2,w-.35,-h/2,tint(f,.6),.22);
      var ang=0; if(falling){var reach=gap-w; ang=reach>=h?80:Math.asin(reach/h)*180/Math.PI;}
      s+=G(tile,'translate('+at(x)+' '+FL+')'+(ang?' rotate('+at(ang)+' '+w+' 0)':''));
    }
    var o={pose:'push',face:-1}; s+=person(x0+(N-1)*gap+w+d*DX+.3-handOf(0,FL,o)[0],FL,T,o);
    return {svg:s,cap:capShare(D,F)};
  });
