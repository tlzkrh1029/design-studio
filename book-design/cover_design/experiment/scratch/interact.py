import asyncio
from playwright.async_api import async_playwright
S='/tmp/claude-0/-home-claude/f47e1d9e-dd33-5fd7-b5d7-0c1c192511c9/scratchpad/'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':1000})
        errs=[]
        pg.on('pageerror', lambda e: errs.append('ERR '+str(e)))
        pg.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type=='error' else None)
        await pg.goto('file:///home/claude/cover_design/experiment/night_json.html')
        await pg.wait_for_selector('body[data-ready]')
        # table toggle
        await pg.click('#tbl-btn')
        print('table rows', await pg.evaluate("document.querySelectorAll('#tbl tbody tr').length"), 'btn', await pg.inner_text('#tbl-btn'))
        el=await pg.query_selector('#tbl'); await el.screenshot(path=S+'i_table.png')
        await pg.click('#tbl-btn')
        # list expand
        await pg.click('#more-btn')
        print('visible rows', await pg.evaluate("[...document.querySelectorAll('#lrows .lrow')].filter(e=>e.offsetParent).length"), 'btn', await pg.inner_text('#more-btn'))
        el=await pg.query_selector('#lrows'); 
        await pg.evaluate("document.querySelectorAll('#lrows .lrow')[26].scrollIntoView()")
        await el.screenshot(path=S+'i_rows_all.png')
        await pg.click('#more-btn')
        # search word
        await pg.fill('#q','꼬리'); await pg.press('#q','Enter'); await pg.wait_for_timeout(700)
        print('stat:', await pg.inner_text('#sstat'), '| rows', await pg.evaluate("document.querySelectorAll('#lrows .lrow').length"), '| more hidden', await pg.evaluate("document.getElementById('lmore').hidden"))
        el=await pg.query_selector('#list'); await el.screenshot(path=S+'i_search.png')
        # date formats
        for qv in ['9/24','09.24','2026-09-24','24일','3일']:
            await pg.fill('#q',qv); await pg.press('#q','Enter'); await pg.wait_for_timeout(200)
            print(qv,'->', await pg.evaluate("document.querySelectorAll('#lrows .lrow').length"), (await pg.inner_text('#sstat')).replace('\n',' | '))
        # empty
        await pg.fill('#q','없는낱말'); await pg.press('#q','Enter'); await pg.wait_for_timeout(300)
        el=await pg.query_selector('#list'); await el.screenshot(path=S+'i_empty.png')
        print('empty:', (await pg.inner_text('#lempty')).replace('\n',' | '))
        await pg.click('#lempty [data-clear]')
        print('after clear rows', await pg.evaluate("[...document.querySelectorAll('#lrows .lrow')].filter(e=>e.offsetParent).length"))
        # scope menu
        await pg.evaluate("window.scrollTo(0,0)"); await pg.click('.scope'); await pg.wait_for_timeout(100)
        await pg.screenshot(path=S+'i_scope.png', clip={'x':900,'y':0,'width':540,'height':220})
        await pg.click('.scope-list li[data-v=text]')
        print('scope now', await pg.inner_text('#scope-val'))
        # flow hover
        box=await pg.evaluate("(()=>{const r=document.querySelector('.tl').getBoundingClientRect(); return [r.left,r.top+scrollY];})()")
        await pg.evaluate("document.getElementById('flow').scrollIntoView()"); await pg.wait_for_timeout(600)
        tl=await pg.query_selector('.tl'); bb=await tl.bounding_box()
        cw=(1312-29*6)/30
        await pg.mouse.move(bb['x']+23*(cw+6)+cw/2, bb['y']+20); await pg.wait_for_timeout(100)
        fr=await pg.query_selector('#flow'); await fr.screenshot(path=S+'i_hover.png')
        print('tip:', (await pg.inner_text('.tip')).replace('\n',' | '))
        await pg.mouse.move(bb['x']+29*(cw+6)+cw/2, bb['y']+20); await pg.wait_for_timeout(100)
        print('tip30:', (await pg.inner_text('.tip')).replace('\n',' | '), await pg.evaluate("document.querySelector('.tip').getBoundingClientRect().right"))
        # keyboard on timeline
        await pg.focus('.tl .tc[tabindex="0"]'); await pg.keyboard.press('ArrowLeft'); await pg.keyboard.press('ArrowLeft')
        print('focused', await pg.evaluate("document.activeElement.getAttribute('aria-label')"))
        print('errors', errs)
        await b.close()
asyncio.run(main())
