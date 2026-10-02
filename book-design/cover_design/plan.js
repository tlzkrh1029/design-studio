const fs=require('fs');
global.window={};
eval(fs.readFileSync('/home/claude/cover_design/data.js','utf8'));
eval(fs.readFileSync('/home/claude/cover_design/mz.js','utf8').replace('var BK=','global.BK='));
function num(v){if(v==null||v==='') return null; if(typeof v==='number') return isFinite(v)?v:null; var n=parseFloat(String(v).replace(/[−–]/g,'-').replace(/[,%p\s+]/g,'')); return isFinite(n)?n:null;}
const B=window.RAW.map(r=>{const x=r.data;return {id:r.id,date:x.date,seq:x.seq||1,phase:x.phase,headline:x.headline||'',btcd:num(x.btcd),stableD:num(x.stableD),stable1m:num(x.stable1m),btc1m:num(x.btc1m),lite:x.lite===true,note:x.note||''};}).sort((a,b)=>a.date<b.date?-1:a.date>b.date?1:a.seq-b.seq);
const plan=BK.plan(B), used={};
B.forEach((b,i)=>{const p=plan[b.id]; used[p.scene]=(used[p.scene]||0)+1; console.log(b.id.padEnd(13), p.focus.padEnd(6), p.scene.padEnd(10), BK.schemes[p.scheme].padEnd(9), String(Math.round(p.hue)).padStart(3)+'°', '|', (b.headline||b.note).slice(0,44));});
console.log('distinct', Object.keys(used).length, 'repeats', Object.entries(used).filter(e=>e[1]>1).map(e=>e.join('×')).join(' '));
const cnt={}; B.forEach(b=>{const s=BK.schemes[plan[b.id].scheme]; cnt[s]=(cnt[s]||0)+1;}); console.log(cnt);
