import sys, asyncio
from playwright.async_api import async_playwright
async def main(mode, out, width=1400, scale=2, clip=None):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':width,'height':900}, device_scale_factor=scale)
        msgs=[]
        pg.on('console', lambda m: msgs.append(m.text))
        pg.on('pageerror', lambda e: msgs.append('ERR '+str(e)))
        await pg.goto('file:///home/claude/cover_design/h.html#'+mode)
        await pg.evaluate('document.fonts.ready')
        await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(300)
        await pg.screenshot(path=out, full_page=True)
        for m in msgs: print(m)
        await b.close()
mode=sys.argv[1]; out=sys.argv[2]; width=int(sys.argv[3]) if len(sys.argv)>3 else 1400; scale=float(sys.argv[4]) if len(sys.argv)>4 else 2
asyncio.run(main(mode,out,width,scale))
