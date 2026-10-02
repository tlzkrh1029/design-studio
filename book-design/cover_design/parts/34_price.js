
  /* ---- BTCUSD: the price itself (1-month change) ---- */
  scene('rocket','로켓',['PRICE'],function(D){return D.b1m!=null;},/급등|치솟|숏|로켓|폭등|뛰었|솟/,function(D,T,F){
    var v=D.b1m, s='';
    if(v>=0){
      var t=clamp(v/25,0,1), rx=62, ry=FL-23-t*3, ang=24, sc=1.65, smoke=T.dark?T.n1:tint(T.n0,.35);
      s+=shadow(20,26,T)+box(8,FL-2.6,20,2.6,4,T.n2)+R(16.4,FL-15,1.4,12.4,T.n3)+R(13,FL-15.4,6,1.2,T.n3);
      var bx=rx-Math.sin(ang*Math.PI/180)*9*sc, by=ry+Math.cos(ang*Math.PI/180)*9*sc;
      for(var i=0;i<11;i++){var k=i/10, x=18+(bx-18)*k, y=FL-3-(FL-3-by)*Math.pow(k,1.6); s+=C(x+(D.r()-.5)*2.4,y+(D.r()-.5)*1.4,2.3+(1-k)*3.2,smoke,op(.92-k*.45));}
      var rk=P('M-2.6 6.2Q0 '+at(15+t*6)+' 2.6 6.2Z',T.c3)+P('M-1.3 6.2Q0 '+at(11.5+t*3)+' 1.3 6.2Z',tint(T.c3,.6))
        +PG([[-3.6,1.2],[-7.4,7.8],[-3.6,6.2]],T.c1)+PG([[3.6,1.2],[7.4,7.8],[3.6,6.2]],shade(T.c1,.18))
        +P('M-3.6 6.2V-6C-3.6 -11 -1.8 -14.4 0 -16.2C1.8 -14.4 3.6 -11 3.6 -6V6.2Z',T.paper)
        +P('M1.3 6.2V-6C1.3 -10.6 .7 -13.6 0 -16.2C1.8 -14.4 3.6 -11 3.6 -6V6.2Z',shade(T.paper,.1))
        +P('M-3.3 -8.6C-2.6 -12 -1.4 -14.6 0 -16.2C1.4 -14.6 2.6 -12 3.3 -8.6Z',T.c3)+R(-3.6,-.2,7.2,1.2,T.c2)
        +C(0,-4,1.9,T.c2)+C(0,-4,1.9,'none',' stroke="'+T.n3+'" stroke-width=".45"')+C(-.5,-4.5,.6,'#FFFFFF',op(.6))+R(-.6,1.6,1.2,6,T.c1);
      s+=G(rk,'translate('+rx+' '+at(ry)+') rotate('+ang+') scale('+sc+')');
      s+=person(33,FL,T,{pose:'look'});
    } else {
      var cy=87, cx=58;
      s+=shadow(cx,16,T,T.dark?.2:.05);
      s+=P('M'+(cx-17)+' '+(cy+2)+'Q'+cx+' '+(cy-19)+' '+(cx+17)+' '+(cy+2)+'Z',T.c1)+P('M'+(cx-6)+' '+(cy+2)+'Q'+cx+' '+(cy-16.6)+' '+(cx+6)+' '+(cy+2)+'Z',T.c2);
      [-17,-6,6,17].forEach(function(o){s+=Ln(cx+o,cy+2,cx+(o<0?-3:3),cy+19,T.ink,.2);});
      s+=box(cx-5,cy+19,10,8,5,T.c3)+TX(cx,cy+24.8,'BTC',2.8,T.c3Ink,{w:800});
      s+=person(24,FL,T,{pose:'look'});
    }
    return {svg:s,cap:capPrice(D)};
  });

  scene('arrow','큰 화살표',['PRICE','BTC','ALT'],needHist(3),/방향|되밀|반락|반등|꺾|돌아|전환/,function(D,T,F){
    var H=histN(D,F,6), N=H.length, S=span(H,.4), p=H.map(function(h,i){return [12+64*i/(N-1), scaleY(h.v,S,FL-36,FL-10)];}), s=shadow(48,82,T);
    var e=p[N-1], q=p[N-2], a=Math.atan2(e[1]-q[1],e[0]-q[0]), hl=8, bw=9.4;
    var tip=[e[0]+Math.cos(a)*hl*.85,e[1]+Math.sin(a)*hl*.85], base=[e[0]-Math.cos(a)*1.4,e[1]-Math.sin(a)*1.4];
    var nx=-Math.sin(a)*bw/2, ny=Math.cos(a)*bw/2, head=[tip,[base[0]+nx,base[1]+ny],[base[0]-nx,base[1]-ny]];
    var dx=1.6, dy=-1.1, line=p.slice(0,N-1).concat([base]), mv=function(z){return z.map(function(q){return [q[0]+dx,q[1]+dy];});};
    s+=PLx(mv(line),shade(T.c1,.35),5.2)+PG(mv(head),shade(T.c3,.35));
    s+=PLx(line,T.c1,5.2)+PLx(line,tint(T.c1,.32),.9,' transform="translate(0 -1.7)"')+PG(head,T.c3);
    var up=e[1]<q[1], fx=q[0]+(e[0]-q[0])*.35, fy=q[1]+(e[1]-q[1])*.35-2.6;
    s+=person(fx,fy,T,{pose:up?'run':'balance',rot:Math.atan2(e[1]-q[1],e[0]-q[0])*180/Math.PI*.35});
    return {svg:s,cap:F==='PRICE'?capPrice(D):capShare(D,F)};
  });

  scene('surf','파도타기',['PRICE','ALT'],function(D,F){return F==='PRICE'?D.b1m!=null:D.dA!=null;},/파도|출렁|되밀|밀려|쓸려|휩쓸/,function(D,T,F){
    var v=F==='PRICE'?D.b1m:D.dA*40, A=clamp(30+Math.abs(v)*.5,30,43), t=FL-A, s='', w=T.c1, dk=shade(T.c1,.3);
    s+=C(17,85,6,T.c3);
    s+=P('M3.2 '+(FL-8)+'C22 '+(FL-8)+' 36 '+(FL-11)+' 45 '+(FL-20)+'C52 '+(FL-27)+' 55 '+at(t+7)+' 64 '+at(t+1.5)+'C72 '+at(t-2)+' 83 '+at(t+4)+' 90 '+at(t+12)+'C94 '+at(t+18)+' 96 '+at(t+22)+' 96.8 '+at(t+24)+'V'+FL+'H3.2Z',w);
    s+=P('M58 '+at(t+5)+'C61 '+at(t+12)+' 60 '+at(t+19)+' 55 '+at(t+23)+'C51 '+at(t+26)+' 47 '+at(t+22)+' 46.4 '+at(t+14)+'C50 '+at(t+18)+' 54 '+at(t+14)+' 52.4 '+at(t+10)+'Z',dk);
    s+=P('M64 '+at(t+1.5)+'C56 '+at(t-1)+' 47.5 '+at(t+4)+' 46.4 '+at(t+11)+'C45.8 '+at(t+15)+' 49 '+at(t+16)+' 51.2 '+at(t+13.4)+'C50.4 '+at(t+9)+' 54 '+at(t+6)+' 60 '+at(t+6.2)+'Z',w);
    s+=SK('M90 '+at(t+12)+'C83 '+at(t+4)+' 72 '+at(t-2)+' 64 '+at(t+1.5)+'C56 '+at(t-1)+' 47.5 '+at(t+4)+' 46.4 '+at(t+11)+'C45.8 '+at(t+15)+' 49 '+at(t+16)+' 51.2 '+at(t+13.4),'#FFFFFF',1.2,op(.92));
    for(var i=0;i<12;i++) s+=C(44+D.r()*22,t-1+D.r()*8,.3+D.r()*.55,'#FFFFFF',op(.85));
    for(var j=0;j<5;j++) s+=SK('M'+at(6+j*9)+' '+at(FL-4.2+(j%2)*1.4)+'q2 -1 4 0t4 0',tint(T.c1,.35),.35);
    for(var k=0;k<3;k++) s+=SK('M'+at(70+k*7)+' '+at(t+18+k*6)+'q3 -1.4 6 0',tint(T.c1,.3),.35);
    var fx=38.5, fy=FL-15.6;
    s+=G(E(0,0,6.2,1.05,T.c3)+E(-.4,-.35,5.4,.5,tint(T.c3,.35))+fig(0,-.9,{pose:'balance',col:T.ink,tie:T.c3,rot:26}),'translate('+fx+' '+fy+') rotate(-30)');
    s+=SK('M'+(fx+5)+' '+(fy+3)+'q4 1.6 9 .4',T.paper,.6,op(.8));
    return {svg:s,cap:F==='PRICE'?capPrice(D):capShare(D,'ALT')};
  });

  scene('escalator','에스컬레이터',['PRICE','BTC','ALT'],function(D,F){return F==='PRICE'?D.b1m!=null:dOf(D,F)!=null;},/계속|꾸준|이어|에스컬|오르막|내리막/,function(D,T,F){
    var v=F==='PRICE'?D.b1m:dOf(D,F), up=v>=0, x0=24, y0=FL-4, x1=72, y1=FL-37, n=12, sdx=(x1-x0)/n, sdy=(y1-y0)/n, s=shadow(50,84,T);
    s+=PG([[8,FL-4],[x0,y0],[x1,y1],[92,y1],[92,y1+6.6],[x1+2,y1+6.6],[x0+5,FL],[8,FL]],T.c1)+PG([[x1+2,y1+6.6],[92,y1+6.6],[92,y1+8.4],[x1+2.6,y1+8.4],[x0+7,FL],[x0+5,FL]],shade(T.c1,.25));
    var st='M'+at(x0)+' '+at(y0); for(var i=0;i<n;i++) st+='V'+at(y0+sdy*(i+1))+'H'+at(x0+sdx*(i+1));
    s+=P(st+'L'+at(x0)+' '+at(y0)+'Z',T.n1)+P('M8 '+(FL-4)+'H'+x0+'V'+(FL-4.6)+'H8Z',T.n2)+P('M'+x1+' '+at(y1)+'H92V'+at(y1-.6)+'H'+x1+'Z',T.n2);
    var k=up?6:5, px=x0+sdx*(k+.55), py=y0+sdy*(k+1);
    s+=person(px,py,T,{face:up?1:-1});
    s+=PG([[8,FL-4],[x0,y0],[x1,y1],[92,y1],[92,y1-9],[x1,y1-9],[x0,y0-9],[8,FL-13]],T.paper,op(T.dark?.12:.32));
    s+=PL([[8,FL-13],[x0,y0-9],[x1,y1-9],[92,y1-9]],T.c3,1.3);
    var mx=(x0+x1)/2+2, my=(y0+y1)/2+5.4, ca=Math.atan2(y1-y0,x1-x0)*180/Math.PI+(up?0:180);
    for(var c=0;c<3;c++) s+=G(PL([[-1.2,-1.6],[.6,0],[-1.2,1.6]],inkOn(T.c1),.55,op(.85)),'translate('+at(mx+(c-1)*4.6*Math.cos(ca*Math.PI/180))+' '+at(my+(c-1)*4.6*Math.sin(ca*Math.PI/180))+') rotate('+at(ca)+')');
    return {svg:s,cap:F==='PRICE'?capPrice(D):capShare(D,F)};
  });

  scene('highjump','높이뛰기',['PRICE','ALT','BTC'],function(D,F){return F==='PRICE'?D.b1m!=null:shareOf(D,F)!=null;},/사이클선|넘|돌파|위로|넘어|뛰어넘/,function(D,T,F){
    var bar=FL-27, lx=30, rx=68, s=shadow(62,70,T);
    s+=box(55,FL-7.5,36,7.5,11,T.c2)+R(55,FL-7.5,36,1.3,tint(T.c2,.22))+R(55,FL-2.2,36,.6,shade(T.c2,.15));
    [lx,rx].forEach(function(x){s+=box(x-2,FL-1.4,4,1.4,3,T.n3)+R(x-.7,bar-8,1.4,FL-bar+6.6,T.n3)+R(x-1.2,bar+.9,2.4,1,shade(T.n3,.3));});
    s+=R(lx,bar-.8,rx-lx,1.6,T.c3); for(var i=0;i<6;i++) s+=R(lx+3.2+i*6,bar-.8,3,1.6,tint(T.c3,.7));
    s+=SK('M12 '+(FL-2)+'Q48 '+(bar-30)+' 80 '+(FL-10),T.ink,.3,' stroke-dasharray="1 1"'+op(.45));
    s+=person(48.4,bar-.6,T,{rot:96,pose:'stand',s:1.15});
    if(F==='ALT'){ s+=person(12,FL,T,{pose:'run'})+person(76,FL-7.5,T,{pose:'sitback'}); }
    if(/사이클선/.test(D.headline)) s+=TX(rx+2.2,bar+1,'사이클선',2.6,T.ink,{a:'start',ff:'g',w:800});
    return {svg:s,cap:F==='PRICE'?capPrice(D):capShare(D,F)};
  });

  /* ---- policy and events ---- */
  scene('gavel','의사봉',['MACRO'],always,/법안|부결|가결|SEC|규제|판결|선을 그|소송|승인|기각/,function(D,T,F){
    var s=shadow(52,56,T);
    for(var i=0;i<4;i++) s+=box(16+i*.5,FL-1.6-i*1.6,17,1.4,9,i%2?T.paper:tint(T.n0,.35));
    s+=cyl(60,FL-5.2,12.5,3.2,5.2,T.c2);
    var head=R(-1.2,-30,2.4,26,T.n3,' rx="1.2"')+R(-1.8,-31.5,3.6,3,shade(T.n3,.15),' rx="1.2"')+R(-10,-4,20,8,T.c1,' rx="1"')+R(-10,-4,20,2.2,tint(T.c1,.2),' rx="1"')+R(-7,-4,1.8,8,T.c3)+R(5.2,-4,1.8,8,T.c3)+E(10,0,1.8,4,tint(T.c1,.28));
    s+=G(head,'translate(57 '+(FL-17.5)+') rotate(38)');
    [[45,FL-9,41,FL-12.5],[44,FL-3.8,39,FL-3.8],[76,FL-10,80,FL-13.4],[77,FL-4,82,FL-4]].forEach(function(l){s+=Ln(l[0],l[1],l[2],l[3],T.c3,.65);});
    var o={pose:'hold'}, hd=handOf(9,FL,o);
    s+=person(9,FL,T,o)+G(R(-2,-2.8,4.2,5.6,T.paper)+Ln(-1.2,-1.4,1.4,-1.4,T.n2,.3)+Ln(-1.2,0,1.4,0,T.n2,.3),'translate('+at(hd[0]+1.2)+' '+at(hd[1]-1.5)+') rotate(8)');
    return {svg:s,cap:capAny(D)};
  });

  scene('columns','기관 건물',['MACRO'],always,/연준|FOMC|금리|중앙은행|의회|정부|기관|백악관|재무부/,function(D,T,F){
    var s=shadow(50,86,T), stone=tint(T.c1,.45), dk=shade(stone,.15);
    s+=box(10,FL-3,80,3,5,T.n1)+box(13,FL-6,74,3,5,T.n1)+box(16,FL-9,68,3,5,T.n1);
    s+=R(44,FL-31,12,22,shade(T.c1,.5));
    [21,31,41,59,69,79].forEach(function(x){s+=R(x-2.5,FL-10.4,5,1.4,dk)+R(x-2,FL-32.2,4,21.8,stone)+R(x+.7,FL-32.2,1.3,21.8,dk)+Ln(x-.8,FL-31.6,x-.8,FL-11,dk,.25)+R(x-2.9,FL-33.8,5.8,1.6,dk);});
    s+=R(16,FL-38.6,68,4.8,T.c1)+R(16,FL-38.6,68,1.2,tint(T.c1,.25))+R(16,FL-35,68,1.2,shade(T.c1,.15));
    s+=PG([[14,FL-38.6],[86,FL-38.6],[50,FL-48.4]],shade(T.c1,.12))+PG([[20,FL-39.8],[80,FL-39.8],[50,FL-46.4]],tint(T.c1,.22))+C(50,FL-42.2,2.3,T.c3)+C(50,FL-42.2,1,shade(T.c3,.3));
    s+=person(29,FL-3,T);
    return {svg:s,cap:capAny(D)};
  });

  scene('ballot','투표함',['MACRO'],always,/표결|투표|클로처|의결|상원|하원|찬성|반대/,function(D,T,F){
    var bx=22, bw=34, bh=26, d=16, by=FL-bh, dx=d*DX, dy=d*DY, s=shadow(44,56,T);
    s+=box(bx,by,bw,bh,d,T.c1);
    var sc=[bx+bw/2+dx/2, by+dy/2];
    s+=PG([[sc[0]-8,sc[1]+.5],[sc[0]+8,sc[1]+.5],[sc[0]+8.9,sc[1]-.4],[sc[0]-7.1,sc[1]-.4]],shade(T.c1,.6));
    s+=R(bx,by+7,bw,7,T.c3)+SK('M'+at(bx+bw/2-3)+' '+at(by+10.5)+'l2 2 4 -4',T.c3Ink,.9);
    var ballot=function(x,y,r){return G(R(-3,-3.8,6,7.6,T.paper)+R(-3,-3.8,6,7.6,'none',' stroke="'+shade(T.paper,.2)+'" stroke-width=".2"')+SK('M-1.4 0l1 1 2 -2.2',T.c3,.6)+Ln(-1.8,-2.4,1.8,-2.4,T.n2,.3),'translate('+at(x)+' '+at(y)+') rotate('+r+')');};
    s+=ballot(sc[0]+1,sc[1]-6.2,8)+ballot(sc[0]-6.4,sc[1]-14.6,-14);
    var o={pose:'hold',face:-1}, hd=handOf(78,FL,o);
    s+=person(78,FL,T,o)+ballot(hd[0]-1.8,hd[1]-2.6,-6);
    return {svg:s,cap:capAny(D)};
  });

  scene('calendar','달력',['MACRO','TYPE'],always,/이틀|이번 주|일정|주간|예고|달력|날짜|다음 주/,function(D,T,F){
    var x=19, y=77, w=52, h=44, s=shadow(46,62,T), dark='#17181A', sun=onPaper(T.c3,T.paper);
    s+=box(x-2,FL-3,w+4,3,7,T.n2)+R(x+1.2,y+1.2,w,h,shade(T.paper,.14))+R(x,y,w,h,T.paper)+R(x,y,w,9.4,T.c1);
    s+=TX(x+w/2,y+7,D.m+'월',5.2,T.c1Ink,{ff:'g',w:800});
    s+=R(x+11,y-2.2,2,4.4,T.n3,' rx="1"')+R(x+w-13,y-2.2,2,4.4,T.n3,' rx="1"');
    var first=new Date(Date.UTC(D.y,D.m-1,1)).getUTCDay(), days=new Date(Date.UTC(D.y,D.m,0)).getUTCDate(), rows=Math.ceil((first+days)/7), cw=w/7, ch=rows>5?4.7:5.6, gy=y+13.2;
    WDK.forEach(function(k,i){s+=TX(x+cw*(i+.5),gy,k,2.2,i===0?sun:dark,{ff:'g',w:700});});
    /* this week's row is marked and today's date circled; the event dates themselves are not in the data */
    var rT=Math.floor((first+D.d-1)/7);
    s+=R(x+.8,gy+4.8+rT*ch-3.7,w-1.6,ch-.3,T.c3,op(.18)+' rx="1"');
    for(var dd=1;dd<=days;dd++){var cell=first+dd-1, c=cell%7, r=Math.floor(cell/7), px=x+cw*(c+.5), py=gy+4.8+r*ch;
      if(dd===D.d) s+=C(px,py-.9,2.6,'none',' stroke="'+T.c3+'" stroke-width=".85"');
      s+=TX(px,py,String(dd),2.4,c===0?sun:dark,{ff:'n',w:500});}
    s+=person(83,FL,T,{pose:'point',face:-1});
    return {svg:s,cap:capAny(D)};
  });

  /* ---- no indicators yet: the phase itself ---- */
  scene('letters','글자 조형',['TYPE'],always,null,function(D,T,F){
    var two=D.ps.length>1, fs=two?30:42, y=FL-.4, ch=D.ps.length?D.ps.slice(-2):[String(D.vol<10?'0'+D.vol:D.vol)], adv=fs*.66, aw=two?fs*.62:0;
    var total=two?adv*2+aw:(ch[0].length*fs*.6), x0=50-total/2, s=shadow(50,total+10,T), items=[];
    if(two){ items.push([x0+adv/2,ch[0]]); items.push(['arrow',x0+adv+aw/2]); items.push([x0+adv+aw+adv/2,ch[1]]); }
    else items.push([50,ch[0]]);
    var draw=function(ox,oy,col){var out=''; items.forEach(function(it){
      if(it[0]==='arrow'){var ax=it[1]+ox, ay=y-fs*.35+oy; out+=PG([[ax-aw*.42,ay-1.6],[ax+aw*.08,ay-1.6],[ax+aw*.08,ay-4.6],[ax+aw*.46,ay],[ax+aw*.08,ay+4.6],[ax+aw*.08,ay+1.6],[ax-aw*.42,ay+1.6]],col===T.c1?T.c3:col);}
      else out+=TX(it[0]+ox,y+oy,it[1],fs,col,{w:700});}); return out;};
    for(var i=7;i>=1;i--) s+=draw(i*.42,-i*.3,shade(T.c1,.3+.02*i));
    s+=draw(0,0,T.c1);
    s+=person(items[0][0]-fs*.08,y-fs*.7-.2,T,{pose:'wave'});
    return {svg:s,cap:D.btc!=null?capAny(D):capNote(D)};
  });

  scene('signpost','이정표',['TYPE'],function(D){return D.ps.length>0;},/분류표|전환|국면|판정|갈림/,function(D,T,F){
    var cur=D.P, prev=D.ps.length>1?D.ps[0]:null, s=shadow(50,20,T);
    s+=R(48.8,FL-47,2.4,47,T.n3)+E(50,FL,6,1.2,shade(T.n3,.2))+C(50,FL-47,1.4,T.n3);
    'ABCDE'.split('').forEach(function(k,i){
      var y=FL-45+i*7.6, right=i%2===0, on=k===cur, pv=k===prev, f=on?T.c3:pv?T.c2:(i%2?T.c1:tint(T.c1,.25));
      var w=on?30:16, x0=right?51.2:48.8, x1=right?x0+w:x0-w, tip=right?x1+3.4:x1-3.4;
      s+=PG([[x0,y],[x1,y],[tip,y+2.9],[x1,y+5.8],[x0,y+5.8]],f)+PG([[x0,y+4.8],[x1,y+4.8],[tip-(right?1:-1)*1.1,y+4.8+.1],[x1,y+5.8],[x0,y+5.8]],shade(f,.15));
      var ink=on?T.c3Ink:pv?T.c2Ink:inkOn(f), tx=right?x0+2:x0-2;
      s+=TX(tx,y+4,on?k+'  '+PHN[k]:k,on?2.8:3.3,ink,{a:right?'start':'end',w:800,ff:on?'g':'w'});
    });
    s+=person(38,FL,T,{pose:'point'});
    return {svg:s,cap:D.btc!=null?capAny(D):capNote(D)};
  });

  scene('compass','나침반',['TYPE'],function(D){return D.ps.length>0;},/방향|어디로|갈림길|나침|향방/,function(D,T,F){
    var cx=46, cy=FL-23.5, r=22, s=shadow(cx,30,T), dark='#17181A';
    s+=C(cx,cy-r-2.2,2.4,'none',' stroke="'+T.c1+'" stroke-width="1.1"');
    s+=C(cx+1.4,cy+1,r,shade(T.c1,.3))+C(cx,cy,r,T.c1)+C(cx,cy,r-3,T.paper);
    var ang=function(k){return -90+72*'ABCDE'.indexOf(k);};
    for(var i=0;i<40;i++){var a=i*9*Math.PI/180, r0=r-4, r1=i%8===0?r-6.4:r-5; s+=Ln(cx+Math.cos(a)*r0,cy+Math.sin(a)*r0,cx+Math.cos(a)*r1,cy+Math.sin(a)*r1,dark,i%8===0?.4:.2);}
    'ABCDE'.split('').forEach(function(k){var a=ang(k)*Math.PI/180, on=k===D.P; s+=TX(cx+Math.cos(a)*(r-9.6),cy+Math.sin(a)*(r-9.6)+1.3,k,on?4.2:3.2,on?onPaper(T.c3,T.paper):dark,{w:800});});
    var needle=function(k,f1,f2,x){var a=ang(k)*Math.PI/180, L=9.6, w=1.9, tip=[cx+Math.cos(a)*L,cy+Math.sin(a)*L], tail=[cx-Math.cos(a)*L*.8,cy-Math.sin(a)*L*.8], n=[-Math.sin(a)*w,Math.cos(a)*w];
      return PG([tip,[cx+n[0],cy+n[1]],[cx-n[0],cy-n[1]]],f1,x)+PG([tail,[cx+n[0],cy+n[1]],[cx-n[0],cy-n[1]]],f2,x);};
    if(D.ps.length>1) s+=needle(D.ps[0],T.c2,T.n1,op(.55));
    s+=needle(D.P,T.c3,dark)+C(cx,cy,1.5,T.n3);
    s+=person(78,FL,T,{pose:'point',face:-1});
    return {svg:s,cap:D.btc!=null?capAny(D):capNote(D)};
  });
