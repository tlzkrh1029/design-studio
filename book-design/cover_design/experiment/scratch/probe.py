import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':1000})
        await pg.goto('file:///home/claude/cover_design/experiment/night_yaml.html')
        await pg.wait_for_selector('body[data-ready]',timeout=20000)
        t1=await pg.evaluate('performance.now()')
        await pg.wait_for_timeout(300)
        r=await pg.evaluate('''()=>({now:performance.now(), anims:document.getAnimations().map(a=>({t:a.currentTime, st:a.startTime, ps:a.playState}))})''')
        print('ready at',round(t1),'shot at',round(r['now']))
        for a in r['anims'][:5]: print(a)
        await b.close()
asyncio.run(main())
