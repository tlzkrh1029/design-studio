import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for vw in [1440, 1024, 390]:
            pg=await b.new_page(viewport={'width':vw,'height':900})
            msgs=[]
            pg.on('console', lambda m: msgs.append(m.type+': '+m.text))
            pg.on('pageerror', lambda e: msgs.append('ERR '+str(e)))
            await pg.goto('file:///home/claude/cover_design/page/preview.html')
            await pg.wait_for_selector('body[data-ready]')
            await pg.evaluate("document.querySelectorAll('details.bm').forEach(function(d){d.open=true;})")
            await pg.wait_for_timeout(400)
            r=await pg.evaluate('''()=>{var out=[], n=0; document.querySelectorAll('.mz').forEach(function(c,i){n++; if(!c.offsetWidth) return; var hb=c.querySelector('.m-hb'); c.querySelectorAll('.m-main,.m-lead').forEach(function(el){ if(el.scrollHeight>el.clientHeight+1) out.push([i,c.offsetWidth,el.className,el.textContent.slice(0,20)]);}); if(!c.hasAttribute('data-fit')) out.push([i,c.offsetWidth,'not-fit']);}); return {n:n,bad:out};}''')
            print(vw, r['n'], r['bad'][:10], [m for m in msgs if 'ERR' in m or 'error' in m][:5])
            await pg.close()
        await b.close()
asyncio.run(main())
