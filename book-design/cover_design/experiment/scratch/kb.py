import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1440,'height':900})
        errs=[]
        pg.on('pageerror', lambda e: errs.append('ERR '+str(e)))
        pg.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type in ('error','warning') else None)
        await pg.goto('file:///home/claude/cover_design/experiment/calendar_yaml.html')
        await pg.wait_for_selector('body[data-ready]')
        # focus order
        seq=[]
        for i in range(24):
            await pg.keyboard.press('Tab')
            d=await pg.evaluate("""()=>{var a=document.activeElement; return (a.tagName+' '+(a.getAttribute('aria-label')||a.textContent||'').trim().slice(0,28)+' '+(a.getAttribute('data-date')||'')).trim();}""")
            seq.append(d)
        print('\n'.join(seq))
        # grid keyboard: focus grid cell, arrow left twice, Enter
        await pg.focus('#cal .grid [tabindex="0"]')
        await pg.keyboard.press('ArrowUp'); await pg.keyboard.press('Enter')
        await pg.wait_for_timeout(300)
        print('after grid up+enter:', await pg.evaluate("()=>[document.activeElement.getAttribute('data-date'), document.querySelector('.day .t-day').textContent, document.querySelector('.day .t-over').textContent]"))
        await pg.keyboard.press('ArrowLeft'); await pg.keyboard.press('ArrowLeft'); await pg.keyboard.press(' ')
        await pg.wait_for_timeout(300)
        print('after 2x left+space:', await pg.evaluate("()=>[document.activeElement.getAttribute('data-date'), document.querySelector('.day .t-day').textContent, document.querySelector('.day .t-over').textContent]"))
        # strip keyboard
        await pg.focus('#cal .strip [tabindex="0"]')
        await pg.keyboard.press('ArrowLeft'); await pg.keyboard.press('Enter')
        await pg.wait_for_timeout(300)
        print('strip:', await pg.evaluate("()=>[document.activeElement.getAttribute('data-date'), document.querySelector('.day .t-day').textContent]"))
        # prev issue button repeatedly
        for i in range(3):
            await pg.click('#day .dh-n [aria-label="이전 호"]')
        await pg.wait_for_timeout(300)
        print('prev x3:', await pg.evaluate("()=>[document.querySelector('.day .t-over').textContent, document.querySelector('.day .t-day').textContent, !!document.querySelector('.seqsw')]"))
        # anchor scroll
        await pg.click('a.pill[href="#indicators"]')
        await pg.wait_for_timeout(700)
        print('scrollY after 지표:', await pg.evaluate("()=>[window.scrollY, Math.round(document.getElementById('indicators').getBoundingClientRect().top)]"))
        await pg.click('.lrow[data-id="2026-09-27-1"]')
        await pg.wait_for_timeout(700)
        print('after row click:', await pg.evaluate("()=>[window.scrollY, document.querySelector('.day .t-day').textContent, document.querySelector('.lrow.sel').getAttribute('data-id')]"))
        await pg.click('[data-act="today"]')
        await pg.wait_for_timeout(300)
        print('today:', await pg.evaluate("()=>document.querySelector('.day .t-over').textContent"))
        print('errors', errs)
        await b.close()
asyncio.run(main())
