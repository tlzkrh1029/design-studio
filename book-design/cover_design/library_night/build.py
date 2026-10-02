"""Build the library page (final.html) and a local preview (preview.html) from src.html."""
import json
D='/home/claude/cover_design/'
src=open(D+'library_night/src.html',encoding='utf-8').read()
mzcss=open(D+'mz.css',encoding='utf-8').read().rstrip('\n')
mzjs=open(D+'mz.js',encoding='utf-8').read().rstrip('\n')
assert src.count('/*<<MZCSS>>*/')==1 and src.count('/*<<MZJS>>*/')==1
page=src.replace('/*<<MZCSS>>*/',mzcss).replace('/*<<MZJS>>*/',mzjs)
open(D+'library_night/final.html','w',encoding='utf-8').write(page)

SKEL=('<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">'
      '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
      'html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#faf9f5;color:#141413}'
      'img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')
GF='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Oswald:wght@500;600&family=Outfit:wght@700;800&display=swap">'
assert page.count(GF)==1
local=''.join('<link rel="stylesheet" href="../node_modules/@fontsource/%s.css">'%f for f in
  ['gothic-a1/400','gothic-a1/500','gothic-a1/600','gothic-a1/700','gothic-a1/800','ibm-plex-mono/400','ibm-plex-mono/500','oswald/500','oswald/600','outfit/700','outfit/800'])
db=json.load(open(D+'library_night/db_snapshot.json',encoding='utf-8'))
mock=('<script>\nDate.now=function(){return Date.UTC(2026,9,1,3,30);};\nwindow.__DB='+json.dumps(db,ensure_ascii=False)+';\n'
 'window.claude={use:function(name){return new Promise(function(res){setTimeout(function(){'
 'if(name==="db") res({collection:function(c){return {onSnapshot:function(cb,err){setTimeout(function(){cb({docs:(window.__DB[c]||[]).map(function(r){return {id:r.id,exists:true,data:function(){return r.data;}};})});},40); return function(){};}};}});'
 'else if(name==="downloads") res({save:function(o){window.__saved=o; return Promise.resolve();}});'
 'else res(null);},20);});}};\n</script>\n')
prev=SKEL+page.replace(GF,local).replace('<div id="app"></div>','<div id="app"></div>\n'+mock,1)+'\n</body></html>'
open(D+'library_night/preview.html','w',encoding='utf-8').write(prev)
print('final',len(page),'preview',len(prev))
