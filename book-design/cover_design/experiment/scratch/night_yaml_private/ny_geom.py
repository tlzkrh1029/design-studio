import asyncio, json
from playwright.async_api import async_playwright
JS=r'''()=>{
 const r=(el)=>{if(!el) return null; const b=el.getBoundingClientRect(); return [Math.round(b.left*100)/100,Math.round((b.top+scrollY)*100)/100,Math.round(b.width*100)/100,Math.round(b.height*100)/100];};
 const q=(s)=>document.querySelector(s), qa=(s)=>[...document.querySelectorAll(s)];
 const o={};
 o.top=r(q('.top')); o.logo=r(q('.logo')); o.nav=r(q('.nav')); o.navFirst=r(q('.nav a')); o.search=r(q('.search')); o.scope=r(q('.scope'));
 o.hero=r(q('.hero')); o.hcover=r(q('.hcover')); o.stand=r(q('.stand')); o.cap=r(q('.stand-cap')); o.lamp=r(q('.lamp'));
 o.kicker=r(q('.kicker')); o.dateline=r(q('.dateline')); o.hl=r(q('.hl')); o.phl=r(q('.phl')); o.figs=r(q('.figs')); o.acts=r(q('.acts'));
 o.btns=qa('.acts .btn').map(r);
 o.band=r(q('.band')); o.bandHead=r(q('.band .shead')); o.tl=r(q('.tl')); o.cell0=r(q('.tc')); o.cellLast=r(qa('.tc').pop()); o.ncells=qa('.tc').length;
 o.tdays=r(q('.tdays')); o.legend=r(q('.legend'));
 o.rack=r(q('#rack')); o.rackHead=r(q('#rack .shead')); o.ghead=r(q('.ghead')); o.rows=qa('.rrow').map(r); o.plank=r(q('.plank')); o.slot0cv=r(q('.slot .cv')); o.slotLab=r(q('.slot .lab')); o.nslots=qa('.slot').length; o.empty=qa('.slot.empty').map(r);
 o.metrics=r(q('#metrics')); o.cards=qa('.card').map(r); o.plots=qa('.plot svg').map(r);
 o.list=r(q('#list')); o.lhead=r(q('.lhead')); o.lrows=qa('.lrow').filter(e=>e.offsetParent).map(r).slice(0,3); o.nvisible=qa('.lrow').filter(e=>e.offsetParent).length; o.lmore=r(q('#lmbtn'));
 o.about=r(q('#about')); o.doc=r(q('.doc')); o.foot=r(q('.foot')); o.sib=r(q('#sib'));
 o.hlLines=Math.round(q('.hl').getBoundingClientRect().height/parseFloat(getComputedStyle(q('.hl')).lineHeight));
 o.accent=getComputedStyle(document.documentElement).getPropertyValue('--accent');
 o.fonts=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight).filter((v,i,a)=>a.indexOf(v)===i);
 o.docW=document.documentElement.scrollWidth;
 return o;}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':900})
        await pg.goto('file:///home/claude/cover_design/experiment/night_yaml.html')
        await pg.wait_for_selector('body[data-ready]',timeout=20000); await pg.wait_for_timeout(300)
        o=await pg.evaluate(JS)
        for k,v in o.items(): print(k, json.dumps(v, ensure_ascii=False))
        await b.close()
asyncio.run(main())
