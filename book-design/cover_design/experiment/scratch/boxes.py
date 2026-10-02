import asyncio, json, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':1000})
        await pg.goto('file:///home/claude/cover_design/experiment/night_json.html')
        await pg.wait_for_selector('body[data-ready]')
        await pg.wait_for_timeout(300)
        r=await pg.evaluate('''()=>{
          const q=(s)=>{const e=document.querySelector(s); if(!e) return null; const r=e.getBoundingClientRect(); return [Math.round(r.left),Math.round(r.top+scrollY),Math.round(r.width),Math.round(r.height)];};
          const out={};
          ['.top','.hero','.stage','.info','.hl','.chips','.figs','.actions','#shelf','.shelves','#flow','.frows','.tl','.legend','#tbl-btn','#list','#lrows','#lmore','#guide','.guide','.foot'].forEach(s=>out[s]=q(s));
          out.shelfRows=[...document.querySelectorAll('.shelf')].map(e=>{const r=e.getBoundingClientRect(); return [Math.round(r.top+scrollY),Math.round(r.height)];});
          out.caps=[...document.querySelectorAll('.cap')].map(e=>{const l=e.querySelector('.cl'), m=e.lastElementChild; return [e.scrollWidth, e.clientWidth, l?Math.round(l.getBoundingClientRect().width):0];}).filter(x=>x[0]>x[1]);
          out.cwraps=[...document.querySelectorAll('.cwrap')].map(e=>{const r=e.getBoundingClientRect(); return [Math.round(r.top+scrollY),Math.round(r.height)];});
          out.hlLines=Math.round(document.querySelector('.hl').getBoundingClientRect().height/(46*1.28));
          out.fonts=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight).filter((v,i,a)=>a.indexOf(v)===i);
          out.scrollW=document.documentElement.scrollWidth;
          // any element wider than viewport or overflowing its box horizontally
          out.wide=[...document.querySelectorAll('#app *')].filter(e=>{const r=e.getBoundingClientRect(); return r.right>1440.5 && !e.closest('.glow')}).slice(0,5).map(e=>e.className);
          return out;}''')
        print(json.dumps(r,ensure_ascii=False,indent=0))
        await b.close()
asyncio.run(main())
