import asyncio
from playwright.async_api import async_playwright
H='file:///home/claude/cover_design/h.html#'
P='file:///home/claude/cover_design/page/preview.html'
async def cap(b, url, out, scale, width, sel='#cap', clip=None, full=False, height=1200, prep=None):
    pg=await b.new_page(viewport={'width':width,'height':height},device_scale_factor=scale)
    errs=[]
    pg.on('pageerror', lambda e: errs.append(str(e)))
    await pg.goto(url); await pg.wait_for_selector('body[data-ready]')
    if prep: await pg.evaluate(prep)
    await pg.wait_for_timeout(500)
    if clip is not None:
        await pg.screenshot(path=out, clip=clip, full_page=True)
    elif sel:
        el=await pg.query_selector(sel); await el.screenshot(path=out)
    else:
        await pg.screenshot(path=out, full_page=full)
    if errs: print(out, errs)
    await pg.close()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        await cap(b, P, 'final/page_top.png', 2, 1440, sel=None, height=1120)
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        await pg.goto(P); await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(500)
        y=await pg.evaluate("document.querySelector('#shelf').getBoundingClientRect().top+window.scrollY-16")
        await pg.screenshot(path='final/mobile.png', clip={'x':0,'y':y,'width':390,'height':844}, full_page=True)
        await pg.close()
        await cap(b, H+'shelf&width=1004', 'final/shelf.png', 2, 1100)
        await cap(b, H+'row&w=400', 'final/covers.png', 2, 2300)
        await cap(b, H+'catalog&n=8&cw=220', 'final/scenes.png', 1.5, 2200)
        await cap(b, H+'schemes&cw=132', 'final/schemes.png', 2, 1400)
        await b.close()
asyncio.run(main())
