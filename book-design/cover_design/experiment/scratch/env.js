global.window={}; global.document={documentElement:{style:{setProperty(){}}}};
const fs=require("fs");
eval(fs.readFileSync("/home/claude/cover_design/data.js","utf8"));
const src=fs.readFileSync("/home/claude/cover_design/mz.js","utf8")+"\n"+fs.readFileSync("/home/claude/cover_design/themes/common.js","utf8")+"\n;globalThis.E=({B,L,pal,BK,stats,daily,dayMap,runLabel,vol,deltas,prevOf});";
(0,eval)(src);
module.exports=globalThis.E;
