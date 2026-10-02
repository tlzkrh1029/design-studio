import asyncio
from playwright.async_api import async_playwright
W='/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/night_yaml_private/'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':900})
        errs=[]; pg.on('pageerror',lambda e: errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
        await pg.goto('file:///home/claude/cover_design/experiment/night_yaml.html')
        await pg.wait_for_selector('body[data-ready]',timeout=20000); await pg.wait_for_timeout(300)
        # "/" focuses search, type a date
        await pg.keyboard.press('/'); await pg.keyboard.type('9/24')
        print('date 9/24 ->', await pg.inner_text('#qlive'), '| rows', await pg.eval_on_selector_all('.rs-row','e=>e.length'))
        await pg.screenshot(path=W+'ny_search.png', clip={'x':900,'y':0,'width':540,'height':260})
        await pg.fill('#q','2026-09-05'); print('2026-09-05 ->', await pg.inner_text('#qlive'))
        await pg.fill('#q','09.03'); print('09.03 ->', await pg.inner_text('#qlive'))
        await pg.fill('#q','현금'); print('현금 ->', await pg.inner_text('#qlive'))
        await pg.select_option('#qscope','국면'); await pg.fill('#q','D'); print('phase D ->', await pg.inner_text('#qlive'))
        await pg.fill('#q','C'); print('phase C ->', await pg.inner_text('#qlive'))
        await pg.select_option('#qscope','전체'); await pg.fill('#q','zzz'); print('zzz ->', await pg.inner_text('#qlive'), await pg.inner_text('#qres'))
        await pg.fill('#q','알트'); await pg.click('#qall'); await pg.wait_for_timeout(900)
        print('list mode:', await pg.inner_text('#lhead'), '| rows', await pg.eval_on_selector_all('#lbody .lrow','e=>e.length'), '| marks', await pg.eval_on_selector_all('#lbody mark','e=>e.length'))
        await pg.click('#qclear'); print('cleared:', await pg.inner_text('#lhead'), '| visible rows', await pg.eval_on_selector_all('#lbody .lrow','e=>e.filter(x=>x.offsetParent).length'))
        await pg.click('#lmbtn'); print('expanded rows', await pg.eval_on_selector_all('#lbody .lrow','e=>e.filter(x=>x.offsetParent).length'), await pg.inner_text('#lmbtn'))
        await pg.click('#tbtn'); print('table rows', await pg.eval_on_selector_all('#mtable tbody tr','e=>e.filter(x=>x.offsetParent).length'), await pg.inner_text('#tbtn'))
        await pg.hover('.tc.latest'); print('tip:', await pg.inner_text('#tltip'))
        await pg.hover('.tc.split'); print('tip split:', await pg.inner_text('#tltip'))
        # nav spy after scrolling to list
        await pg.evaluate("document.getElementById('list').scrollIntoView()"); await pg.wait_for_timeout(900)
        print('nav on:', await pg.eval_on_selector('.nav a.on','e=>e.textContent'))
        print('errors', errs)
        await b.close()
asyncio.run(main())
