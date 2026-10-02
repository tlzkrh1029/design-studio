import asyncio, json, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        bad=[]
        for w in [132,160,190,220,236,260,300,340,400,420]:
            pg=await b.new_page(viewport={'width':2400,'height':1200})
            for mode in ['big&n=40&w=%d'%w, 'catalog&n=8&cw=%d'%w]:
                await pg.goto('file:///home/claude/cover_design/h.html#'+mode)
                await pg.reload()
                await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(150)
                r=await pg.evaluate('''()=>{var out=[]; document.querySelectorAll('.mz').forEach(function(c,i){var hb=c.querySelector('.m-hb'); c.querySelectorAll('.m-main,.m-lead').forEach(function(el){ if(el.scrollHeight>el.clientHeight+1) out.push([i,el.className,el.textContent.slice(0,20)]);}); if(hb.scrollHeight>hb.clientHeight+1) out.push([i,'hb-overflow',hb.textContent.slice(0,20)]);}); return out;}''')
                for x in r: bad.append((w,mode.split('&')[0])+tuple(x))
            await pg.close()
        print(len(bad)); print('\n'.join(map(str,bad[:40])))
        await b.close()
asyncio.run(main())
