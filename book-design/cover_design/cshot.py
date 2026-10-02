import sys, asyncio
from playwright.async_api import async_playwright
async def main(mode,out,scale):
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':2200,'height':1200},device_scale_factor=scale)
        await pg.goto('file:///home/claude/cover_design/h.html#'+mode)
        await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(300)
        el=await pg.query_selector('#cap'); await el.screenshot(path=out)
        await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2],float(sys.argv[3])))
