import asyncio
from playwright.async_api import async_playwright
S='/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':1000})
        errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('file:///home/claude/cover_design/experiment/calendar_json.html'); await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(300)
        shots=[]
        for d in ['2026-09-18','2026-10-01']:
            await pg.evaluate("d=>{document.querySelector('#cal [data-d=\"'+d+'\"]').click(); window.scrollTo(0,0);}", d)
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=S+'s2_'+d+'.png', clip={'x':1070,'y':70,'width':340,'height':980})
        print('errors',errs); await b.close()
asyncio.run(main())
