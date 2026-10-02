import asyncio
from playwright.async_api import async_playwright
S='/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':900})
        await pg.goto('file:///home/claude/cover_design/experiment/night_json.html')
        await pg.wait_for_selector('body[data-ready]')
        await pg.evaluate("window.scrollTo({top:document.querySelector('.frows').getBoundingClientRect().top+scrollY-300,behavior:'instant'})"); await pg.wait_for_timeout(300)
        tl=await pg.query_selector('.tl'); bb=await tl.bounding_box(); cw=(1312-29*6)/30
        for i,name in [(23,'tip24'),(29,'tip30'),(0,'tip01')]:
            await pg.mouse.move(bb['x']+i*(cw+6)+cw/2, bb['y']+20); await pg.wait_for_timeout(120)
            t=await pg.query_selector('.tip'); tb=await t.bounding_box()
            print(name, [round(v) for v in (tb['x'],tb['y'],tb['width'],tb['height'])])
            await pg.screenshot(path=S+name+'.png', clip={'x':max(0,tb['x']-40),'y':tb['y']-20,'width':min(1440-max(0,tb['x']-40),tb['width']+80),'height':tb['height']+140})
        await b.close()
asyncio.run(main())
