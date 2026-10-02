import sys, asyncio
from playwright.async_api import async_playwright
async def main(name,out,scale):
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':1000},device_scale_factor=scale)
        errs=[]
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type in ('error','warning') else None)
        await pg.goto('file:///home/claude/cover_design/themes/%s.html'%name)
        await pg.wait_for_selector('body[data-ready]',timeout=20000); await pg.wait_for_timeout(300)
        h=await pg.evaluate('document.documentElement.scrollHeight')
        await pg.screenshot(path=out, full_page=True)
        ov=await pg.evaluate('''()=>{var o=[]; document.querySelectorAll('.mz').forEach(function(c,i){c.querySelectorAll('.m-main,.m-lead').forEach(function(el){if(el.scrollHeight>el.clientHeight+1) o.push(i);});}); return o;}''')
        print(name,'height',h,'overflow',ov, errs[:5])
        await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2],float(sys.argv[3]) if len(sys.argv)>3 else 1))
