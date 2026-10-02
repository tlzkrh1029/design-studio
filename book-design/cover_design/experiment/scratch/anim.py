import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for run in range(3):
            pg=await b.new_page(viewport={'width':1440,'height':1000})
            await pg.goto('file:///home/claude/cover_design/experiment/night_json.html')
            await pg.wait_for_selector('body[data-ready]',timeout=20000)
            t0=await pg.evaluate('performance.now()')
            await pg.wait_for_timeout(300)
            r=await pg.evaluate('''()=>{const s=document.querySelector('.spot'); const a=s.getAnimations()[0]; return {op:getComputedStyle(s).opacity, t:performance.now(), state:a?a.playState:'none', cur:a?a.currentTime:null};}''')
            print(run,'ready at',round(t0),'ms; at shot:',r)
            await pg.close()
        await b.close()
asyncio.run(main())
