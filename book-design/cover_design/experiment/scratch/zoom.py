"""Zoomed clips: python3 zoom.py <name> <out_prefix> x,y,w,h [x,y,w,h ...]  (page coords, scale 2)
Optional env ACTIONS: a JS snippet run before the shots (e.g. to click something)."""
import sys, os, asyncio
from playwright.async_api import async_playwright
async def main(name, pref, clips):
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':1000},device_scale_factor=2)
        errs=[]
        pg.on('pageerror', lambda e: errs.append('ERR '+str(e)))
        pg.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type in ('error','warning') else None)
        await pg.goto('file:///home/claude/cover_design/experiment/%s.html'%name)
        await pg.wait_for_selector('body[data-ready]',timeout=20000)
        await pg.wait_for_timeout(300)
        act=os.environ.get('ACTIONS')
        if act:
            await pg.evaluate(act)
            await pg.wait_for_timeout(600)
        for i,c in enumerate(clips):
            x,y,w,h=[float(v) for v in c.split(',')]
            await pg.screenshot(path='%s_%d.png'%(pref,i), clip={'x':x,'y':y,'width':w,'height':h}, full_page=True)
        print('errors',errs)
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2], sys.argv[3:]))
