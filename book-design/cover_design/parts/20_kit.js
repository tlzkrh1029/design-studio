
  /* ---- drawing kit. viewBox 0 0 100 147 (1 unit = 1cqw), floor line at y=124, picture area y 75-124 ---- */
  function at(x){return n1(x);}
  function P(d,f,x){return '<path d="'+d+'" fill="'+f+'"'+(x||'')+'/>';}
  function R(x,y,w,h,f,x2){return '<rect x="'+at(x)+'" y="'+at(y)+'" width="'+at(w)+'" height="'+at(h)+'" fill="'+f+'"'+(x2||'')+'/>';}
  function C(cx,cy,r,f,x){return '<circle cx="'+at(cx)+'" cy="'+at(cy)+'" r="'+at(r)+'" fill="'+f+'"'+(x||'')+'/>';}
  function E(cx,cy,rx,ry,f,x){return '<ellipse cx="'+at(cx)+'" cy="'+at(cy)+'" rx="'+at(rx)+'" ry="'+at(ry)+'" fill="'+f+'"'+(x||'')+'/>';}
  function Ln(x1,y1,x2,y2,s,w,x){return '<line x1="'+at(x1)+'" y1="'+at(y1)+'" x2="'+at(x2)+'" y2="'+at(y2)+'" stroke="'+s+'" stroke-width="'+w+'" stroke-linecap="round"'+(x||'')+'/>';}
  function pts(p){return p.map(function(q){return at(q[0])+','+at(q[1]);}).join(' ');}
  function PL(p,s,w,x){return '<polyline points="'+pts(p)+'" fill="none" stroke="'+s+'" stroke-width="'+w+'" stroke-linecap="round" stroke-linejoin="round"'+(x||'')+'/>';}
  function PG(p,f,x){return '<polygon points="'+pts(p)+'" fill="'+f+'"'+(x||'')+'/>';}
  function SK(d,s,w,x){return '<path d="'+d+'" fill="none" stroke="'+s+'" stroke-width="'+w+'" stroke-linecap="round" stroke-linejoin="round"'+(x||'')+'/>';}
  var FF={w:"Outfit,Futura,'Avenir Next',sans-serif", g:"'Gothic A1','Apple SD Gothic Neo','Malgun Gothic',sans-serif", n:"Oswald,'Arial Narrow',sans-serif"};
  function TX(x,y,t,fs,f,o){o=o||{}; return '<text x="'+at(x)+'" y="'+at(y)+'" font-size="'+at(fs)+'" fill="'+f+'" text-anchor="'+(o.a||'middle')+'" font-family="'+FF[o.ff||'w']+'" font-weight="'+(o.w||700)+'"'+(o.ls!=null?' letter-spacing="'+o.ls+'"':'')+(o.x||'')+'>'+esc(t)+'</text>';}
  function G(inner,tr,x){return '<g'+(tr?' transform="'+tr+'"':'')+(x||'')+'>'+inner+'</g>';}
  function op(v){return ' opacity="'+v+'"';}
  function tint(c,t){return mixc(c,'#FFFFFF',t);}
  function shade(c,t){return mixc(c,'#000000',t);}
  function shadow(cx,w,T,o){return E(cx,FL+.5,w/2,1.3,T.shadow,op(o!=null?o:(T.dark?.32:.09)));}
  var CLIP=0;
  function clip(d,inner){var id='mzc'+(++CLIP); return '<clipPath id="'+id+'"><path d="'+d+'"/></clipPath><g clip-path="url(#'+id+')">'+inner+'</g>';}
  /* extruded rectangle: front face at (x,y,w,h), depth d towards the back right */
  var DX=.62, DY=-.42;
  function box(x,y,w,h,d,f,o){
    o=o||{}; var dx=d*DX, dy=d*DY;
    return P('M'+at(x)+' '+at(y)+'L'+at(x+dx)+' '+at(y+dy)+'H'+at(x+w+dx)+'L'+at(x+w)+' '+at(y)+'Z',o.top||tint(f,.3))
      +P('M'+at(x+w)+' '+at(y)+'L'+at(x+w+dx)+' '+at(y+dy)+'V'+at(y+h+dy)+'L'+at(x+w)+' '+at(y+h)+'Z',o.side||shade(f,.22))
      +R(x,y,w,h,f);
  }
  /* upright cylinder: top ellipse centred at (cx,y), body height h */
  function cyl(cx,y,rx,ry,h,f,o){
    o=o||{}; var dk=shade(f,.2);
    return P('M'+at(cx-rx)+' '+at(y)+'V'+at(y+h)+'A'+at(rx)+' '+at(ry)+' 0 0 0 '+at(cx+rx)+' '+at(y+h)+'V'+at(y)+'Z',f)
      +P('M'+at(cx+rx*.42)+' '+at(y)+'V'+at(y+h+ry*.907)+'A'+at(rx)+' '+at(ry)+' 0 0 0 '+at(cx+rx)+' '+at(y+h)+'V'+at(y)+'Z',dk)
      +E(cx,y,rx,ry,o.top||tint(f,.3));
  }
  /* coin standing on its edge, seen from the front; thickness shows on the right */
  function coinFace(cx,cy,r,f,label,lc){
    var th=r*.17, rim=shade(f,.28);
    return C(cx+th,cy,r,rim)+R(cx,cy-r,th,2*r,rim)+C(cx,cy,r,f)
      +C(cx,cy,r*.8,'none',' stroke="'+shade(f,.14)+'" stroke-width="'+at(r*.05)+'"')
      +(label?TX(cx,cy+r*.19,label,r*.52,lc||tint(f,.62),{w:800,ls:'-.02em'}):'');
  }
  /* coin lying flat: top face centred at (cx,y) */
  function coinFlat(cx,y,rx,ry,th,f){
    return P('M'+at(cx-rx)+' '+at(y)+'V'+at(y+th)+'A'+at(rx)+' '+at(ry)+' 0 0 0 '+at(cx+rx)+' '+at(y+th)+'V'+at(y)+'Z',shade(f,.26))
      +E(cx,y,rx,ry,f)+E(cx,y,rx*.7,ry*.7,'none',' stroke="'+shade(f,.12)+'" stroke-width=".22"');
  }
  function star(x,y,r,f,x2){return P('M'+at(x)+' '+at(y-r)+'Q'+at(x)+' '+at(y)+' '+at(x+r)+' '+at(y)+'Q'+at(x)+' '+at(y)+' '+at(x)+' '+at(y+r)+'Q'+at(x)+' '+at(y)+' '+at(x-r)+' '+at(y)+'Q'+at(x)+' '+at(y)+' '+at(x)+' '+at(y-r)+'Z',f,x2);}
  function cloud(x,y,s,f,x2){return G(C(0,0,3.2,f)+C(3.6,-1.4,3.8,f)+C(7.6,.2,2.9,f)+R(0,0,7.6,2.9,f),'translate('+at(x)+' '+at(y)+') scale('+s+')',x2);}
  /* smooth curve through points (Catmull-Rom as cubic Bezier) and its height at x */
  function crPath(p){
    var d='M'+at(p[0][0])+' '+at(p[0][1]);
    for(var i=0;i<p.length-1;i++){var p0=p[i-1]||p[i], p1=p[i], p2=p[i+1], p3=p[i+2]||p2;
      d+='C'+at(p1[0]+(p2[0]-p0[0])/6)+' '+at(p1[1]+(p2[1]-p0[1])/6)+' '+at(p2[0]-(p3[0]-p1[0])/6)+' '+at(p2[1]-(p3[1]-p1[1])/6)+' '+at(p2[0])+' '+at(p2[1]);}
    return d;
  }
  function crY(p,x){
    for(var i=0;i<p.length-1;i++){ if(x<=p[i+1][0]){var p0=p[i-1]||p[i], p1=p[i], p2=p[i+1], p3=p[i+2]||p2, t=clamp((x-p1[0])/(p2[0]-p1[0]),0,1);
      var c1=p1[1]+(p2[1]-p0[1])/6, c2=p2[1]-(p3[1]-p1[1])/6, u=1-t; return u*u*u*p1[1]+3*u*u*t*c1+3*u*t*t*c2+t*t*t*p2[1];} }
    return p[p.length-1][1];
  }
  function scaleY(v,s,top,bot){return bot-(v-s.lo)/s.rg*(bot-top);}

  /* ---- a small person. Feet at (x,y); `face` -1 turns left; poses move the limbs ---- */
  var ST=[[[.36,-2.95],[.46,-1.5],[.5,0]],[[-.36,-2.95],[-.46,-1.5],[-.5,0]]];
  var POSE={
    stand:{a:[[[.74,-5.15],[.98,-3.95],[1.04,-2.95]],[[-.74,-5.15],[-.98,-3.95],[-1.04,-2.95]]], l:ST},
    point:{a:[[[.74,-5.15],[1.75,-5.85],[2.75,-6.6]],[[-.74,-5.15],[-.98,-3.95],[-1.04,-2.95]]], l:ST},
    hold:{a:[[[.7,-5.1],[1.35,-4.25],[2.25,-4.3]],[[-.62,-5.1],[.45,-4.45],[1.75,-4.5]]], l:ST},
    wave:{a:[[[.74,-5.15],[1.5,-6.2],[1.55,-7.5]],[[-.74,-5.15],[-.98,-3.95],[-1.04,-2.95]]], l:ST},
    cheer:{a:[[[.74,-5.15],[1.3,-6.4],[1.7,-7.6]],[[-.74,-5.15],[-1.3,-6.4],[-1.7,-7.6]]], l:ST},
    look:{a:[[[.66,-5.1],[1.35,-5.0],[1.15,-6.25]],[[-.6,-5.1],[.55,-5.45],[.95,-6.3]]], l:ST, prop:1},
    balance:{a:[[[.74,-5.15],[1.8,-5.3],[2.8,-5.7]],[[-.74,-5.15],[-1.8,-5.1],[-2.8,-4.8]]], l:[[[.36,-2.95],[.95,-1.5],[1.25,0]],[[-.36,-2.95],[-.95,-1.5],[-1.25,0]]], lean:6},
    climb:{a:[[[.66,-5.2],[1.0,-6.45],[1.35,-7.55]],[[-.6,-5.2],[.1,-6.2],[.75,-6.85]]], l:[[[.36,-2.95],[1.2,-2.3],[1.05,-.95]],[[-.36,-2.95],[-.3,-1.5],[-.2,0]]]},
    pull:{a:[[[.66,-5.1],[1.6,-4.75],[2.55,-4.55]],[[-.55,-5.1],[.75,-4.8],[2.05,-4.65]]], l:[[[.36,-2.95],[1.3,-1.5],[1.9,0]],[[-.36,-2.95],[-.5,-1.5],[-.55,0]]], lean:-20},
    push:{a:[[[.66,-5.1],[1.6,-5.25],[2.6,-5.35]],[[-.55,-5.1],[.85,-5.3],[2.1,-5.4]]], l:[[[-.36,-2.95],[-1.1,-1.55],[-1.9,0]],[[.36,-2.95],[.75,-1.55],[.65,0]]], lean:24},
    run:{a:[[[.66,-5.1],[1.45,-4.35],[1.15,-3.5]],[[-.6,-5.1],[-1.35,-4.55],[-1.95,-5.0]]], l:[[[.36,-2.95],[1.5,-2.15],[1.35,-.55]],[[-.36,-2.95],[-.95,-1.55],[-2.05,-1.05]]], lean:14},
    sit:{sit:1, a:[[[.66,-2.15],[1.1,-1.05],[1.75,-.35]],[[-.6,-2.15],[.2,-1.05],[1.05,-.4]]], l:[[[.3,0],[1.8,0],[1.85,2.9]],[[-.3,0],[1.5,-.1],[1.45,2.85]]]},
    sitback:{sit:1, a:[[[.62,-2.15],[.1,-1.2],[-.9,-.5]],[[-.62,-2.15],[-1.2,-1.1],[-1.6,-.1]]], l:[[[.3,0],[1.8,-.25],[3.4,.1]],[[-.3,0],[1.6,.1],[3.2,.35]]], lean:-12}
  };
  function fig(x,y,o){
    o=o||{}; var p=POSE[o.pose||'stand'], s=o.s||1, fc=o.face||1, col=o.col, sh=p.sit?2.95:0, lean=o.lean!=null?o.lean:(p.lean||0);
    var legs=p.l.map(function(q){return PL(q,col,.7);}).join('');
    var body=PL(p.a[1],col,.54)
      +'<path d="M-.8 '+at(-5.3+sh)+'Q0 '+at(-5.74+sh)+' .8 '+at(-5.3+sh)+'L.6 '+at(-2.8+sh)+'L-.6 '+at(-2.8+sh)+'Z" fill="'+col+'"/>'
      +C(0,-6.42+sh,.8,col)+PL(p.a[0],col,.54);
    if(p.prop) body+=R(.62,-6.95,1.25,.8,col,' rx=".25"');
    if(o.tie) body+=P('M-.16 '+at(-5.28+sh)+'H.16L.1 '+at(-3.7+sh)+'L0 '+at(-3.45+sh)+'L-.1 '+at(-3.7+sh)+'Z',o.tie);
    if(lean) body=G(body,'rotate('+lean+' 0 '+at(-2.95+sh)+')');
    var inner=legs+body+(o.extra||'');
    if(o.rot) inner=G(inner,'rotate('+o.rot+' 0 -3)');
    return G(inner,'translate('+at(x)+' '+at(y)+') scale('+at(s*fc)+' '+at(s)+')');
  }
  /* world position of the front hand (which=0) or the back hand (which=1) */
  function handOf(x,y,o,which){
    o=o||{}; var p=POSE[o.pose||'stand'], s=o.s||1, fc=o.face||1, sh=p.sit?2.95:0, q=p.a[which||0][2], lx=q[0], ly=q[1];
    var lean=o.lean!=null?o.lean:(p.lean||0);
    if(lean){var a=lean*Math.PI/180, cy=-2.95+sh, dx=lx, dy=ly-cy; lx=dx*Math.cos(a)-dy*Math.sin(a); ly=cy+dx*Math.sin(a)+dy*Math.cos(a);}
    return [x+lx*s*fc, y+ly*s];
  }
  function person(x,y,T,o){o=o||{}; o.col=o.col||T.ink; if(o.tie===undefined) o.tie=T.c3; return fig(x,y,o);}
