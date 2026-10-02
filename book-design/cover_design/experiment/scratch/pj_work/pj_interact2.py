import asyncio, json
from playwright.async_api import async_playwright
W = '/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/pj_work/'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1440, 'height': 1000})
        errs = []
        pg.on('pageerror', lambda e: errs.append('ERR ' + str(e)))
        await pg.goto('file:///home/claude/cover_design/experiment/paper_json.html')
        await pg.wait_for_selector('body[data-ready]', timeout=20000)
        await pg.wait_for_timeout(300)
        out = {}
        for sec in ['p2', 'p3', 'p4', 'p5']:
            await pg.evaluate("(s) => { const el = document.getElementById(s); window.scrollTo({top: el.getBoundingClientRect().top + scrollY - 76, behavior: 'instant'}); }", sec)
            await pg.wait_for_timeout(250)
            out['cur_' + sec] = await pg.evaluate("() => document.querySelector('.nav-link[aria-current]').dataset.sec")
            out['nav_' + sec] = await pg.evaluate("() => { const n = document.querySelector('.navbar').getBoundingClientRect(); return [Math.round(n.top), Math.round(n.bottom)]; }")
        await pg.screenshot(path=W + 'pj_state_sticky.png')
        await pg.evaluate("() => { const el = document.getElementById('p2'); window.scrollTo({top: el.getBoundingClientRect().top + scrollY - 76, behavior: 'instant'}); }")
        await pg.wait_for_timeout(250)
        ix = await pg.query_selector_all('a.ix-cell')
        await ix[7].hover(); await pg.wait_for_timeout(600)
        out['ixTip'] = await pg.evaluate("() => { const t = document.querySelectorAll('a.ix-cell')[7].querySelector('.tip'); if (!t) return 'none'; const r = t.getBoundingClientRect(); return {on: t.classList.contains('is-on'), left: Math.round(r.left), right: Math.round(r.right), top: Math.round(r.top)}; }")
        await pg.screenshot(path=W + 'pj_state_ixtip.png')
        out['errs'] = errs
        print(json.dumps(out, ensure_ascii=False))
        await b.close()
asyncio.run(main())
