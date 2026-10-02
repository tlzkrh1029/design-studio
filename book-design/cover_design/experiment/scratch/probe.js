const fs=require('fs');
const root='/home/claude/cover_design/';
global.window={};
eval(fs.readFileSync(root+'data.js','utf8'));
const src=fs.readFileSync(root+'mz.js','utf8')+'\n'+fs.readFileSync(root+'themes/common.js','utf8')+`
var pl=PLAN[L.id]; var ko=''; BK.scenes.forEach(function(s){if(s.id===pl.scene) ko=s.ko;});
console.log('L',L.date,vol(L),pl.scene,ko,pal(L).name);
console.log('stats',JSON.stringify(stats()));
var dm=dayMap(); console.log('multi',Object.keys(dm).filter(k=>dm[k].length>1).map(k=>k+':'+dm[k].length).join(' '));
['btcd','stable1m','btc1m'].forEach(k=>{var d=daily(k); var v=d.map(p=>p.v); console.log(k,d.length,Math.min(...v),Math.max(...v),d[0].d);});
console.log(B.map(b=>vol(b)+':'+b.date+'#'+b.seq+':'+runLabel(b)).join(' | '));
console.log(B[29].headline, '/', B[28].headline);
`;
eval(src);
