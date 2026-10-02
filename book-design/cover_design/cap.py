import sys, asyncio
from playwright.async_api import async_playwright
async def main(hashv,out,scale,width):
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':width,'height':1200},device_scale_factor=scale)
        msgs=[]
        pg.on('console', lambda m: msgs.append(m.type+': '+m.text))
        pg.on('pageerror', lambda e: msgs.append('ERR '+str(e)))
        await pg.goto('file:///home/claude/cover_design/h.html#'+hashv)
        await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(300)
        el=await pg.query_selector('#cap'); await el.screenshot(path=out)
        for m in msgs: print(m)
        await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2],float(sys.argv[3]) if len(sys.argv)>3 else 1,int(sys.argv[4]) if len(sys.argv)>4 else 2400))
