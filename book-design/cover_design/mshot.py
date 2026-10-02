import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        await pg.goto('file:///home/claude/cover_design/page/preview.html')
        await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(400)
        y=await pg.evaluate("document.querySelector('#shelf').getBoundingClientRect().top+window.scrollY-16")
        await pg.screenshot(path='out/mobile.png', clip={'x':0,'y':y,'width':390,'height':844}, full_page=True)
        await b.close()
asyncio.run(main())
