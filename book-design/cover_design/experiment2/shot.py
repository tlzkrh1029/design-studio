"""Render an experiment page: python3 shot.py <name> <out.png> [scale] [width]
Prints page height, covers whose headline overflows, and page errors."""
import sys, asyncio
from playwright.async_api import async_playwright
async def main(name,out,scale,width):
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':width,'height':1000},device_scale_factor=scale)
        errs=[]
        pg.on('pageerror', lambda e: errs.append('ERR '+str(e)))
        pg.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type in ('error',) else None)
        await pg.goto('file:///home/claude/cover_design/experiment2/%s.html'%name)
        try:
            await pg.wait_for_selector('body[data-ready]',timeout=20000)
        except Exception as e:
            errs.append('never ready: '+str(e)[:80])
        await pg.wait_for_timeout(300)
        h=await pg.evaluate('document.documentElement.scrollHeight')
        w=await pg.evaluate('document.documentElement.scrollWidth')
        await pg.screenshot(path=out, full_page=True)
        ov=await pg.evaluate('''()=>{var o=[]; document.querySelectorAll('.mz').forEach(function(c,i){c.querySelectorAll('.m-main,.m-lead').forEach(function(el){if(el.scrollHeight>el.clientHeight+1) o.push(i);});}); return o;}''')
        print(name,'size',w,'x',h,'overflow',ov,'errors',errs[:6])
        await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2],float(sys.argv[3]) if len(sys.argv)>3 else 1,int(sys.argv[4]) if len(sys.argv)>4 else 1440))
