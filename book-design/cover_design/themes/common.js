/* shared helpers for the theme mockups: real briefs, real covers */
function num(v){if(v==null||v==='') return null; if(typeof v==='number') return isFinite(v)?v:null; var n=parseFloat(String(v).replace(/[−–]/g,'-').replace(/[,%p\s+]/g,'')); return isFinite(n)?n:null;}
function normalize(list){
  return list.map(function(r){var x=r.data||{}; return {id:r.id,date:String(x.date||'').slice(0,10),seq:Math.max(1,parseInt(x.seq,10)||1),title:x.title?String(x.title):'',url:x.url||null,
    phase:x.phase?String(x.phase):null,prevPhase:x.prevPhase?String(x.prevPhase):null,provisional:x.provisional===true,headline:x.headline?String(x.headline):'',
    btcd:num(x.btcd),stableD:num(x.stableD),stable1m:num(x.stable1m),btc1m:num(x.btc1m),lite:x.lite===true,window:x.window?String(x.window):'',run:x.run?String(x.run):'',
    note:x.note?String(x.note):''};})
  .filter(function(b){return /^\d{4}-\d\d-\d\d$/.test(b.date);})
  .sort(function(a,b){return a.date<b.date?-1:a.date>b.date?1:a.seq-b.seq;});
}
var B=normalize(window.RAW), L=B[B.length-1], PLAN=BK.plan(B);
var WD=['일','월','화','수','목','금','토'];
var PHN={A:'BTC!',B:'알트시즌?',C:'선별적',D:'STICKY BTC.D',E:'튀어?'};
var PCOL={A:'#CB8242',B:'#A96CAF',C:'#056F15',D:'#594D99',E:'#2B97FF'};
var PINK={A:'#141B0F',B:'#141B0F',C:'#FFFFFF',D:'#FFFFFF',E:'#141B0F'};
function vol(b){return B.indexOf(b)+1;}
function dn(d){var a=d.split('-').map(Number); return Math.round(Date.UTC(a[0],a[1]-1,a[2])/864e5);}
function wd(d){return WD[new Date(dn(d)*864e5).getUTCDay()];}
function mdot(d){return d.slice(5).replace('-','.');}
function parts(p){if(!p) return []; return String(p).split(/→|->|>/).map(function(s){return s.trim().toUpperCase();}).filter(function(s){return /^[A-E]$/.test(s);});}
function lastPh(b){var p=parts(b.phase); return p.length?p[p.length-1]:null;}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function f(v,d){return v==null?'–':v.toFixed(d);}
function sg(v,d){if(v==null) return '–'; var s=Math.abs(v).toFixed(d); return (Number(s)===0?'±':(v>0?'+':'−'))+s;}
function cover(b){return BK.html(b,B,vol(b));}
function prevOf(b){var p=null; B.forEach(function(x){ if((x.date<b.date||(x.date===b.date&&x.seq<b.seq)) && x.btcd!=null) p=x; }); return p;}
function deltas(b){var p=prevOf(b); return {dB:(p&&b.btcd!=null)?b.btcd-p.btcd:null, dS:(p&&b.stableD!=null&&p.stableD!=null)?b.stableD-p.stableD:null};}
function pal(b){var p=PLAN[b.id]; return BK.palette(p.scheme,p.hue);}
/* one value per day (last issue of the day) */
function daily(key){var m={}, o=[]; B.forEach(function(b){var v=b[key]; if(v==null) return; if(!(b.date in m)) o.push(b.date); m[b.date]=v;}); return o.map(function(d){return {d:d,v:m[d]};});}
function dayMap(){var m={}; B.forEach(function(b){(m[b.date]=m[b.date]||[]).push(b);}); return m;}
function stats(){var days={}; B.forEach(function(b){if(b.btcd!=null) days[b.date]=1;}); return {n:B.length, days:Object.keys(days).length};}
function spark(pts,w,h,stroke,o){
  o=o||{}; var vs=pts.map(function(p){return p.v;}), lo=Math.min.apply(null,vs), hi=Math.max.apply(null,vs), rg=(hi-lo)||1, pad=o.pad||4;
  var xy=pts.map(function(p,i){return [pad+(w-2*pad)*i/(pts.length-1||1), pad+(h-2*pad)*(1-(p.v-lo)/rg)];});
  var d=xy.map(function(q,i){return (i?'L':'M')+q[0].toFixed(1)+' '+q[1].toFixed(1);}).join('');
  var last=xy[xy.length-1];
  var s='<svg viewBox="0 0 '+w+' '+h+'" width="'+w+'" height="'+h+'" aria-hidden="true">';
  if(o.ref!=null&&o.ref>=lo&&o.ref<=hi){var ry=pad+(h-2*pad)*(1-(o.ref-lo)/rg); s+='<line x1="0" x2="'+w+'" y1="'+ry.toFixed(1)+'" y2="'+ry.toFixed(1)+'" stroke="'+(o.refc||stroke)+'" stroke-width="1" stroke-dasharray="3 3" opacity=".5"/>';}
  if(o.area) s+='<path d="'+d+'L'+last[0].toFixed(1)+' '+h+'L'+xy[0][0].toFixed(1)+' '+h+'Z" fill="'+o.area+'"/>';
  s+='<path d="'+d+'" fill="none" stroke="'+stroke+'" stroke-width="'+(o.sw||2)+'" stroke-linejoin="round" stroke-linecap="round"/>';
  s+='<circle cx="'+last[0].toFixed(1)+'" cy="'+last[1].toFixed(1)+'" r="'+(o.r||3.5)+'" fill="'+(o.dot||stroke)+'"/></svg>';
  return s;
}
function ready(){BK.grain(); document.fonts.ready.then(function(){BK.fit(document,true); setTimeout(function(){document.body.setAttribute('data-ready','1');},150);});}
var RUN={'본실행':'06:10 본실행','안전판':'안전판','수동':'수동 실행'};
function runLabel(b){return RUN[b.run]||(b.run?b.run:(b.window?'지연 실행 '+b.window.split('~')[0]:'실행 기록 없음'));}
function phaseText(p){var ps=parts(p); return ps.length?'국면 '+ps.join('→')+' · '+(ps.length>1?'걸친 판정':PHN[ps[0]]):'국면 미기록';}
function chipsOf(b){var c=[phaseText(b.phase)]; if(b.provisional) c.push('임시 기준'); if(b.prevPhase) c.push('전날 국면 '+parts(b.prevPhase).join('→')); return c;}
