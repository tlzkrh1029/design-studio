import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':1000})
        await pg.goto('file:///home/claude/cover_design/experiment/paper_yaml.html'); await pg.wait_for_selector('body[data-ready]'); await pg.wait_for_timeout(300)
        await pg.click('#ltog'); await pg.wait_for_timeout(100)
        t=await pg.evaluate('''()=>{const rows=[...document.querySelectorAll('#ltab tbody tr')].filter(r=>getComputedStyle(r).display!=='none'); const g=document.querySelector('#ltab tr.gap'); const gb=g.getBoundingClientRect();
          return {visible:rows.length, gapH:gb.height, gapTxt:g.innerText.replace(/\\s+/g,' '), toggle:document.getElementById('ltog').innerText, top:gb.top+scrollY};}''')
        print(t)
        el=await pg.query_selector('#ltab'); bb=await el.bounding_box()
        await pg.screenshot(path='expanded.png', clip={'x':60,'y':t['top']-140,'width':1320,'height':300}, full_page=True)
        await b.close()
asyncio.run(main())
