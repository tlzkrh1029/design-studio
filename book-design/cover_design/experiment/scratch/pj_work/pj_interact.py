"""paper_json only: exercise hover / fold / search states and save state crops into pj_work."""
import asyncio, json
from playwright.async_api import async_playwright
W = '/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/pj_work/'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1440, 'height': 1000})
        errs = []
        pg.on('pageerror', lambda e: errs.append('ERR ' + str(e)))
        pg.on('console', lambda m: errs.append(m.type + ': ' + m.text) if m.type == 'error' else None)
        await pg.goto('file:///home/claude/cover_design/experiment/paper_json.html')
        await pg.wait_for_selector('body[data-ready]', timeout=20000)
        await pg.wait_for_timeout(300)
        out = {}
        out['refSides'] = await pg.evaluate("() => Array.from(document.querySelectorAll('.pl-ref')).map(e => e.id + ':' + e.dataset.side)")
        out['current0'] = await pg.evaluate("() => document.querySelector('.nav-link[aria-current]').dataset.sec")
        # timeline hover on 9/30 (last cell) and on 9/18 (holiday)
        await pg.evaluate("() => document.getElementById('p3').scrollIntoView()")
        await pg.wait_for_timeout(400)
        out['current3'] = await pg.evaluate("() => document.querySelector('.nav-link[aria-current]').dataset.sec")
        cells = await pg.query_selector_all('.pm-hit')
        await cells[-1].hover(); await pg.wait_for_timeout(500)
        out['tipLast'] = await pg.evaluate("() => { const t = document.getElementById('pm-tip'); const r = t.getBoundingClientRect(); const w = document.querySelector('.wrap').getBoundingClientRect(); return {hidden: t.hidden, left: Math.round(r.left), right: Math.round(r.right), wrapR: Math.round(w.right), text: t.innerText}; }")
        await pg.screenshot(path=W + 'pj_state_tip.png')
        await cells[16].hover(); await pg.wait_for_timeout(500)
        out['tipHol'] = await pg.evaluate("() => document.getElementById('pm-tip').innerText")
        # keyboard: focus latest then ArrowLeft
        await pg.mouse.move(5, 5); await pg.wait_for_timeout(100)
        await pg.focus('.pm-hit[tabindex=\"0\"]')
        await pg.keyboard.press('ArrowLeft'); await pg.wait_for_timeout(100)
        out['kbd'] = await pg.evaluate("() => document.activeElement.getAttribute('aria-label')")
        await pg.keyboard.press('Escape')
        # index cell tooltip (rightmost column)
        await pg.evaluate("() => document.getElementById('p2').scrollIntoView()")
        await pg.wait_for_timeout(300)
        ix = await pg.query_selector_all('a.ix-cell')
        await ix[7].hover(); await pg.wait_for_timeout(500)
        out['ixTip'] = await pg.evaluate("() => { const t = document.querySelectorAll('a.ix-cell')[7].querySelector('.tip'); const r = t.getBoundingClientRect(); return {on: t.classList.contains('is-on'), left: Math.round(r.left), right: Math.round(r.right)}; }")
        await pg.screenshot(path=W + 'pj_state_ixtip.png')
        await pg.mouse.move(5, 5)
        # fold toggle
        h0 = await pg.evaluate('document.documentElement.scrollHeight')
        await pg.click('#il-more'); await pg.wait_for_timeout(200)
        h1 = await pg.evaluate('document.documentElement.scrollHeight')
        out['fold'] = [h0, h1, await pg.evaluate("() => document.getElementById('il-more').innerText"), await pg.evaluate("() => document.querySelectorAll('.il-row:not([hidden])').length"), await pg.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--page-h')")]
        await pg.click('#il-more'); await pg.wait_for_timeout(200)
        out['fold2'] = [await pg.evaluate('document.documentElement.scrollHeight'), await pg.evaluate("() => document.querySelectorAll('.il-row:not([hidden])').length")]
        # search
        await pg.evaluate("() => window.scrollTo(0,0)")
        await pg.fill('#s-q', '안전판'); await pg.wait_for_timeout(400)
        out['search1'] = await pg.evaluate("() => ({bar: document.getElementById('srbar-t').innerText, cells: document.querySelectorAll('.ix-cell:not([hidden])').length, rows: document.querySelectorAll('.il-row:not([hidden])').length, top: document.querySelector('.masthead').style.top})")
        await pg.screenshot(path=W + 'pj_state_search.png')
        await pg.fill('#s-q', '09.24'); await pg.wait_for_timeout(400)
        out['search2'] = await pg.evaluate("() => document.getElementById('srbar-t').innerText")
        await pg.fill('#s-q', 'zzzz'); await pg.wait_for_timeout(400)
        out['search3'] = await pg.evaluate("() => ({bar: document.getElementById('srbar-t').innerText, p2: !document.querySelector('#p2 .no-hit').hidden, p4: !document.querySelector('#p4 .no-hit').hidden})")
        await pg.select_option('#s-scope', '표지'); await pg.fill('#s-q', '9월 24일'); await pg.wait_for_timeout(400)
        out['search4'] = await pg.evaluate("() => ({bar: document.getElementById('srbar-t').innerText, rows: document.querySelectorAll('.il-row:not([hidden])').length})")
        await pg.click('#s-all'); await pg.wait_for_timeout(300)
        out['cleared'] = await pg.evaluate("() => ({bar: document.getElementById('srbar').hidden, cells: document.querySelectorAll('.ix-cell:not([hidden])').length, rows: document.querySelectorAll('.il-row:not([hidden])').length, scope: document.getElementById('s-scope').value})")
        # sticky header while scrolled
        await pg.evaluate("() => window.scrollTo(0, 2000)"); await pg.wait_for_timeout(300)
        out['sticky'] = await pg.evaluate("() => { const n = document.querySelector('.navbar').getBoundingClientRect(); return [Math.round(n.top), Math.round(n.bottom)]; }")
        await pg.screenshot(path=W + 'pj_state_sticky.png')
        out['errs'] = errs
        print(json.dumps(out, ensure_ascii=False, indent=1))
        await b.close()
asyncio.run(main())
