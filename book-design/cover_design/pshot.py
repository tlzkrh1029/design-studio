import sys, asyncio
from playwright.async_api import async_playwright
async def main(out, width, height, scale, full, clip_sel=None, open_all=False):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':width,'height':height}, device_scale_factor=scale)
        msgs=[]
        pg.on('console', lambda m: msgs.append(m.type+': '+m.text))
        pg.on('pageerror', lambda e: msgs.append('ERR '+str(e)))
        await pg.goto('file:///home/claude/cover_design/page/preview.html')
        await pg.wait_for_selector('body[data-ready]')
        if open_all:
            await pg.evaluate("document.querySelectorAll('details.bm').forEach(function(d){d.open=true;})")
        await pg.wait_for_timeout(500)
        if clip_sel:
            el = await pg.query_selector(clip_sel)
            await el.screenshot(path=out)
        else:
            await pg.screenshot(path=out, full_page=full)
        for m in msgs: print(m)
        await b.close()
out=sys.argv[1]; w=int(sys.argv[2]); h=int(sys.argv[3]); sc=float(sys.argv[4]); full=sys.argv[5]=='full'
sel=sys.argv[6] if len(sys.argv)>6 and sys.argv[6]!='-' else None
oa=len(sys.argv)>7 and sys.argv[7]=='open'
asyncio.run(main(out,w,h,sc,full,sel,oa))
