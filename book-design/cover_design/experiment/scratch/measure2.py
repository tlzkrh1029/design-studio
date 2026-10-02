import asyncio
from playwright.async_api import async_playwright
JS = r'''()=>{
 const q=(s)=>document.querySelector(s), r=(e)=>{if(!e) return null; const b=e.getBoundingClientRect(); return [Math.round(b.left*10)/10, Math.round((b.top+scrollY)*10)/10, Math.round(b.width*10)/10, Math.round(b.height*10)/10];};
 const out={};
 [['topbar','.topbar'],['np','.np'],['nprow','.np-row'],['earL','.ear-l'],['earR','.ear-r'],['nameplate','.nameplate'],['tagline','.tagline'],['dbl','.dbl'],['nav','.nav'],['search','.search'],['scope','.scope'],['front','.front'],
  ['lead','.cv-lead'],['leadcap','.lead-cap'],['kicker','.kicker'],['flag','.flag'],['headline','#lead-h'],['btn','.btn'],['fbox','.fbox'],['fc2','.fc:nth-child(2)'],['prevh','.prev-h'],['teasers','.teasers'],['tz','.tz'],['mini','.cv-mini'],
  ['market','#market'],['sech','#market .sec-h'],['month','#market .month'],['trkph','.trk-ph'],['tc1','.tc'],['legend','.legend'],['charts','.charts'],['ch1','.chart'],['plot1','.plot'],
  ['covers','#covers'],['cvgrid','.cv-grid'],['cvrow','.cv-row'],['card','.card'],['cvt','.card .cv-t'],['cap','.card .cap'],
  ['list','#list'],['ltab','.ltab'],['thead','.ltab thead'],['tr1','.ltab tbody tr'],['toggle','.toggle'],['fn','.foot-note'],
  ['about','#about'],['aboutgrid','.about'],['cvmh','#covers .month-h'],['cvmeta','#covers .month-h .meta'],['cvmt','#covers .month-h .month'],['footrule','.foot-rule'],['footrow','.foot-row'],['end','.page-end']].forEach(([k,s])=>out[k]=r(q(s)));
 out.docH=document.documentElement.scrollHeight; out.docW=document.documentElement.scrollWidth;
 out.hlLines=Math.round(q('#lead-h').getBoundingClientRect().height/parseFloat(getComputedStyle(q('#lead-h')).lineHeight));
 out.tzClamp=[...document.querySelectorAll('.tz-h')].map(e=>[e.scrollHeight,e.clientHeight]);
 // any element wider than viewport or overflowing horizontally
 const wide=[]; document.querySelectorAll('body *').forEach(e=>{const b=e.getBoundingClientRect(); if(b.right>1440.5||b.left<-0.5) wide.push(e.tagName+'.'+e.className);});
 out.wide=wide.slice(0,10);
 // fonts actually used
 out.fonts=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight).filter((v,i,a)=>a.indexOf(v)===i);
 return out;}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':1000})
        await pg.goto('file:///home/claude/cover_design/experiment/paper_yaml.html'); await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(300)
        o=await pg.evaluate(JS)
        for k,v in o.items(): print(k, v)
        await b.close()
asyncio.run(main())
