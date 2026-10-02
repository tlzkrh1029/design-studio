import asyncio
from playwright.async_api import async_playwright
S='/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':900})
        await pg.goto('file:///home/claude/cover_design/experiment/night_json.html')
        await pg.wait_for_selector('body[data-ready]')
        await pg.click('.scope'); await pg.wait_for_timeout(100)
        await pg.keyboard.press('Tab')  # move focus to input to see focus ring
        await pg.wait_for_timeout(100)
        await pg.screenshot(path=S+'i_scope.png', clip={'x':940,'y':0,'width':500,'height':200})
        await b.close()
asyncio.run(main())
