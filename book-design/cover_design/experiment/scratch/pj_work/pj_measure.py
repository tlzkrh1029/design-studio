"""paper_json only: load experiment/paper_json.html and evaluate a JS file, print JSON."""
import sys, asyncio, json
from playwright.async_api import async_playwright
async def main(js):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1440, 'height': 1000})
        await pg.goto('file:///home/claude/cover_design/experiment/paper_json.html')
        await pg.wait_for_selector('body[data-ready]', timeout=20000)
        await pg.wait_for_timeout(300)
        r = await pg.evaluate(js)
        print(json.dumps(r, ensure_ascii=False))
        await b.close()
asyncio.run(main(open(sys.argv[1]).read()))
