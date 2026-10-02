"""Measure layout boxes of the built page. usage: python3 measure.py <name> [js-file-with-extra-expression]"""
import sys, asyncio, json
from playwright.async_api import async_playwright
JS = r'''()=>{
  function R(sel){var e=document.querySelector(sel); if(!e) return null; var r=e.getBoundingClientRect(); return [Math.round(r.left*10)/10, Math.round((r.top+scrollY)*10)/10, Math.round(r.width*10)/10, Math.round(r.height*10)/10];}
  var o={};
  ['.tb','.tb-l','.tb-c','.tb-r','.srch','.mark','.tb-c h2','.cal','.cal-h','.legend','.strip','.rule','.wk','.grid','.day','.dh','.dcov','.dcov .cv','.hl','.btn-p','.chips','.dmeta','.dsep','.stats','.rec','.rrs','.ind','.panels','.pn','.chart','.lst','.lhd','.lrow','.more','.ft','.pg','.side']
   .forEach(function(s){o[s]=R(s);});
  o.cell=R('.grid .dc'); o.cell30=R('.dc[data-date="2026-09-30"]'); o.mz30=R('.dc[data-date="2026-09-30"] .mz');
  o.bigmz=R('.day .mz');
  o.sc30=R('.sc[data-date="2026-09-30"] .sb'); o.sc1=R('.sc[data-date="2026-09-01"] .sb');
  o.hlLines=(function(){var e=document.querySelector('.hl'); return e? Math.round(e.getBoundingClientRect().height/29*100)/100:null;})();
  o.scrollW=document.documentElement.scrollWidth; o.scrollH=document.documentElement.scrollHeight;
  /* text overflow check: elements whose content is wider than their box (excluding covers) */
  var ov=[]; document.querySelectorAll('#app *').forEach(function(e){ if(e.closest('.mz')) return; var cs=getComputedStyle(e); if(cs.display==='inline'||e.tagName==='svg'||e.closest('svg')) return; if(e.scrollWidth>e.clientWidth+1 && cs.overflow!=='visible' && cs.textOverflow!=='ellipsis') ov.push((e.className||e.tagName)+' '+e.scrollWidth+'>'+e.clientWidth); });
  o.hiddenOverflow=ov.slice(0,20);
  return o;
}'''
async def main(name, extra):
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':900})
        await pg.goto('file:///home/claude/cover_design/experiment/%s.html'%name)
        await pg.wait_for_selector('body[data-ready]',timeout=20000)
        await pg.wait_for_timeout(300)
        r=await pg.evaluate(JS)
        for k,v in r.items(): print(k, v)
        if extra:
            print(await pg.evaluate(open(extra).read()))
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None))
