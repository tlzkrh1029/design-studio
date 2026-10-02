"""Render the preview at several widths: python3 shot.py out_prefix w1 w2 ..."""
import sys, asyncio
from playwright.async_api import async_playwright
async def main(prefix,widths):
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for w in widths:
            pg=await b.new_page(viewport={'width':w,'height':900},device_scale_factor=1)
            errs=[]
            pg.on('pageerror', lambda e: errs.append('ERR '+str(e)))
            pg.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type in ('error','warning') else None)
            await pg.goto('file:///home/claude/cover_design/library_night/preview.html')
            try:
                await pg.wait_for_selector('.hero .hcover .mz',timeout=20000)
                await pg.wait_for_selector('body[data-ready]',timeout=20000)
            except Exception as e:
                errs.append('wait: '+str(e)[:100])
            await pg.wait_for_timeout(900)
            dims=await pg.evaluate('''()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,h:document.documentElement.scrollHeight,z:getComputedStyle(document.documentElement).getPropertyValue('--z')})''')
            ov=await pg.evaluate('''()=>{var o=[]; document.querySelectorAll('.mz').forEach(function(c,i){c.querySelectorAll('.m-main,.m-lead').forEach(function(el){if(el.scrollHeight>el.clientHeight+1) o.push(i);});}); return o;}''')
            await pg.screenshot(path='%s_%d.png'%(prefix,w), full_page=True)
            print(w,dims,'headline-overflow',ov,'errors',errs[:8])
            await pg.close()
        await b.close()
asyncio.run(main(sys.argv[1],[int(x) for x in sys.argv[2:]]))
