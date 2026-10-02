import asyncio, json
from playwright.async_api import async_playwright
W = '/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/pj_work/'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1440, 'height': 1000})
        await pg.goto('file:///home/claude/cover_design/experiment/paper_json.html')
        await pg.wait_for_selector('body[data-ready]', timeout=20000)
        await pg.wait_for_timeout(300)
        await pg.fill('#s-q', '안전판'); await pg.wait_for_timeout(400)
        out = {}
        out['scrollY_after_fill'] = await pg.evaluate('scrollY')
        out['docH'] = await pg.evaluate('document.documentElement.scrollHeight')
        for y in [0, 300, 800]:
            await pg.evaluate("(y) => window.scrollTo({top: y, behavior: 'instant'})", y)
            await pg.wait_for_timeout(200)
            out['y%d' % y] = await pg.evaluate("() => { const h = document.querySelector('.masthead').getBoundingClientRect(); const n = document.querySelector('.navbar').getBoundingClientRect(); const s = document.getElementById('srbar').getBoundingClientRect(); return {sy: scrollY, head: [Math.round(h.top), Math.round(h.bottom)], nav: [Math.round(n.top), Math.round(n.bottom)], bar: [Math.round(s.top), Math.round(s.bottom)]}; }")
        await pg.screenshot(path=W + 'pj_state_search2.png')
        print(json.dumps(out, ensure_ascii=False))
        await b.close()
asyncio.run(main())
