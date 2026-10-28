"""Checks and captures for the issue-viewer drafts.

python3 shot.py pages    full-page captures of preview_base/a/b at 1440, 1300, 820, 390 (height 900):
                         horizontal overflow, cover headline overflow, console errors, hero markup vs base
python3 shot.py viewer [a b | adopted]   the viewer open on a rack cover at four window sizes, plus behaviour checks
"""
import sys, os, asyncio, json, re
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'screenshots')
os.makedirs(OUT, exist_ok=True)
URL = lambda f: 'file://' + os.path.join(HERE, f)

COVER_OVERFLOW = '''(sel)=>{var o=[]; document.querySelectorAll(sel).forEach(function(c,i){c.querySelectorAll('.m-main,.m-lead').forEach(function(el){if(el.scrollHeight>el.clientHeight+1) o.push(i);});}); return o;}'''


async def ready(pg):
    await pg.wait_for_selector('body[data-ready]', timeout=20000)
    await pg.wait_for_selector('.hero .hcover .mz', timeout=20000)
    await pg.wait_for_timeout(700)


def track(pg):
    errs = []
    pg.on('pageerror', lambda e: errs.append('ERR ' + str(e)))
    pg.on('console', lambda m: errs.append(m.type + ': ' + m.text) if m.type in ('error', 'warning') else None)
    return errs


HERO_HTML = '''()=>{var h=document.querySelector('.hero').cloneNode(true); var t=h.querySelector('.hl');
  if(t){t.removeAttribute('style'); t.removeAttribute('title'); t.classList.remove('clamp');}
  return h.outerHTML;}'''
HERO_BOX = '''()=>{var t=document.querySelector('.hero .htext'), h=document.querySelector('.hero'), k=[...t.children];
  var hr=h.getBoundingClientRect(), a=k[0].getBoundingClientRect().top, z=k[k.length-1].getBoundingClientRect().bottom, hl=t.querySelector('.hl');
  return {inside: a>=hr.top-0.5 && z<=hr.bottom+0.5, top:Math.round(a-hr.top), bottom:Math.round(hr.bottom-z), hl:hl.className+' '+(hl.style.fontSize||'')};}'''


async def pages():
    async with async_playwright() as p:
        br = await p.chromium.launch()
        heroes = {}
        for f in ['preview_base.html', 'preview_a.html', 'preview_b.html']:
            for w in [1440, 1300, 820, 390]:
                pg = await br.new_page(viewport={'width': w, 'height': 900})
                errs = track(pg)
                await pg.goto(URL(f)); await ready(pg)
                dims = await pg.evaluate('()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,h:document.documentElement.scrollHeight})')
                ov = await pg.evaluate(COVER_OVERFLOW, '.mz')
                hb = await pg.evaluate(HERO_BOX)
                heroes[(f, w)] = await pg.evaluate(HERO_HTML)
                await pg.screenshot(path=os.path.join(OUT, 'page_%s_%d.jpg' % (f.split('.')[0].replace('preview_', ''), w)), full_page=True, type='jpeg', quality=80)
                print(f, w, dims, 'cover-headline-overflow', ov, 'hero-text', hb, 'errors', errs[:6])
                await pg.close()
        for w in [1440, 1300, 820, 390]:
            print('hero markup same as base at', w, 'A:', heroes[('preview_a.html', w)] == heroes[('preview_base.html', w)],
                  'B:', heroes[('preview_b.html', w)] == heroes[('preview_base.html', w)])
        await br.close()


VIEW = '''()=>{var v=document.querySelector('.vw'); if(!v||v.hidden) return null;
  var r=function(s){var e=v.querySelector(s); if(!e) return null; var b=e.getBoundingClientRect(); return [Math.round(b.left),Math.round(b.top),Math.round(b.right),Math.round(b.bottom)];};
  var hl=v.querySelector('.hl');
  return {cls:v.className, name:v.querySelector('#vw-name').textContent, vz:v.style.getPropertyValue('--vz'), vcw:v.style.getPropertyValue('--vcw'),
    cover:r('.hcover,.vw-cv'), text:r('.htext,.vw-tx'), first:r('.kicker'), last:r('.acts'), prev:r('.vw-step.prev .o'), next:r('.vw-step.next .o'), close:r('.vw-x'),
    hl:hl?hl.className+' '+(hl.style.fontSize||'')+' clamp='+(hl.style.webkitLineClamp||''):null,
    accent:v.style.getPropertyValue('--accent'), focus:document.activeElement===v.querySelector('.vw-box')?'box':(document.activeElement||{}).className,
    lock:document.documentElement.classList.contains('vw-lock'), inert:document.getElementById('app').inert,
    boxScrollW:v.querySelector('.vw-box').scrollWidth, boxClientW:v.querySelector('.vw-box').clientWidth};}'''


async def open_slot(pg, id_):
    el = pg.locator('#rack [data-id="%s"]' % id_)
    await el.scroll_into_view_if_needed()
    await el.click()
    await pg.wait_for_selector('.vw:not([hidden]) .mz[data-fit]', timeout=5000)
    await pg.wait_for_timeout(900)


def inside(box, W, H):
    return box is None or (box[0] >= 0 and box[1] >= 0 and box[2] <= W and box[3] <= H)


def overlap(a, b):
    return a and b and not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


async def viewer(vs=('a', 'b')):
    sizes = [(1440, 900), (1300, 800), (820, 1180), (390, 844)]
    async with async_playwright() as p:
        br = await p.chromium.launch()
        for v in vs:
            for (w, h) in sizes:
                pg = await br.new_page(viewport={'width': w, 'height': h})
                errs = track(pg)
                await pg.goto(URL('preview_%s.html' % v)); await ready(pg)
                await open_slot(pg, '2026-09-23-1')
                s = await pg.evaluate(VIEW)
                ov = await pg.evaluate(COVER_OVERFLOW, '.vw .mz')
                await pg.screenshot(path=os.path.join(OUT, 'viewer_%s_%dx%d.jpg' % (v, w, h)), type='jpeg', quality=85)
                desk = w >= 1280
                ok = []
                if desk:
                    for k in ['cover', 'first', 'last', 'prev', 'next', 'close']:
                        if not inside(s[k], w, h): ok.append(k + ' outside')
                    for a_, b_ in [('cover', 'text'), ('prev', 'cover'), ('prev', 'text'), ('next', 'text'), ('close', 'text'), ('next', 'cover')]:
                        if overlap(s[a_], s[b_]): ok.append(a_ + '/' + b_ + ' overlap')
                else:
                    if s['boxScrollW'] > s['boxClientW']: ok.append('sheet scrolls sideways')
                    if s['text'][2] > w - 15 or s['cover'][2] > w - 15: ok.append('cover or text wider than the screen')
                print('viewer', v.upper(), w, h, json.dumps(s, ensure_ascii=False), 'cover-overflow', ov, 'problems', ok, 'errors', errs[:5])
                await pg.close()

        # behaviour, on A at 1440x900 (B shares the code)
        for v in vs:
            pg = await br.new_page(viewport={'width': 1440, 'height': 900})
            errs = track(pg)
            await pg.goto(URL('preview_%s.html' % v)); await ready(pg)
            await open_slot(pg, '2026-09-23-1')
            names = []
            for k in ['ArrowRight', 'ArrowRight', 'ArrowLeft', 'ArrowLeft', 'ArrowLeft']:
                await pg.keyboard.press(k); await pg.wait_for_timeout(120)
                names.append(await pg.evaluate("document.querySelector('#vw-name').textContent"))
            print(v.upper(), 'arrow steps', names)
            # click the next button, focus should stay on it
            await pg.click('.vw-step.next'); await pg.wait_for_timeout(150)
            print(v.upper(), 'after next click', await pg.evaluate("[document.querySelector('#vw-name').textContent, document.activeElement.className]"))
            # tab cycles inside the dialog
            seen = []
            for _ in range(9):
                await pg.keyboard.press('Tab')
                seen.append(await pg.evaluate("(document.activeElement.closest('.vw')?'in:':'OUT:')+(document.activeElement.className||document.activeElement.tagName)"))
            print(v.upper(), 'tab order', seen)
            await pg.keyboard.press('Escape'); await pg.wait_for_timeout(150)
            print(v.upper(), 'after Esc', await pg.evaluate("({open:!document.querySelector('.vw').hidden, focus:document.activeElement.getAttribute('data-id'), lock:document.documentElement.classList.contains('vw-lock'), inert:document.getElementById('app').inert})"))
            # outside click closes
            await open_slot(pg, '2026-09-23-1')
            await pg.mouse.click(30, 860); await pg.wait_for_timeout(150)
            print(v.upper(), 'outside click closes', await pg.evaluate("document.querySelector('.vw').hidden"))
            # click inside the text does not close
            await open_slot(pg, '2026-09-23-1')
            tb = await pg.evaluate("(()=>{var b=document.querySelector('.vw .figs').getBoundingClientRect(); return [b.left+b.width/2,b.top+b.height/2];})()")
            await pg.mouse.click(tb[0], tb[1]); await pg.wait_for_timeout(150)
            print(v.upper(), 'text click keeps it open', await pg.evaluate("!document.querySelector('.vw').hidden"))
            await pg.keyboard.press('Escape')
            # like claude.ai's artifact frame, record every click on a link before the page sees it (capture phase);
            # the openers must give it nothing to open, while the viewer's own brief button stays a link
            await pg.evaluate("""()=>{window.__links=[]; document.addEventListener('click',function(e){
                var a=e.target.closest&&e.target.closest('a[href]'); if(a){window.__links.push(a.getAttribute('href')); e.preventDefault();}},true);}""")
            n_open = await pg.evaluate("document.querySelectorAll('#rack [data-id],.tl [data-id]').length")
            n_href = await pg.evaluate("[...document.querySelectorAll('#rack [data-id],.tl [data-id]')].filter(x=>x.hasAttribute('href')).length")
            el = pg.locator('#rack [data-id="2026-09-22-1"]')
            await el.scroll_into_view_if_needed()
            await el.click(); await pg.wait_for_timeout(300)
            r1 = await pg.evaluate("[!document.querySelector('.vw').hidden, document.querySelector('#vw-name').textContent, window.__links.slice()]")
            await pg.click('.vw .acts .btn-pri'); await pg.wait_for_timeout(100)
            r2 = await pg.evaluate("window.__links.slice()")
            await pg.keyboard.press('Escape'); await pg.wait_for_timeout(150)
            print(v.upper(), 'openers', n_open, 'with href', n_href, '| cover click: open, name, links', r1, '| brief button links', r2)
            await el.click(modifiers=['Control']); await pg.wait_for_timeout(300)
            print(v.upper(), 'ctrl-click', await pg.evaluate("[!document.querySelector('.vw').hidden, window.__links.length]"), 'pages', len(pg.context.pages))
            await pg.keyboard.press('Escape'); await pg.wait_for_timeout(150)
            # keyboard: Enter and Space on a rack cover open it without scrolling the page; focus comes back on close
            for key in ['Enter', 'Space']:
                await el.focus(); y0 = await pg.evaluate('scrollY')
                await pg.keyboard.press(key); await pg.wait_for_timeout(300)
                st = await pg.evaluate("[!document.querySelector('.vw').hidden, document.querySelector('#vw-name').textContent]")
                await pg.keyboard.press('Escape'); await pg.wait_for_timeout(150)
                print(v.upper(), key, 'opens', st, 'scrolled', (await pg.evaluate('scrollY')) - y0,
                      'focus back on', await pg.evaluate("document.activeElement.getAttribute('data-id')"))
            # timeline: one tab stop, an arrow moves, Enter opens that day
            tc = pg.locator('.tl a.tc.latest')
            await tc.scroll_into_view_if_needed(); await tc.focus()
            await pg.keyboard.press('ArrowLeft'); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(300)
            print(v.upper(), 'timeline arrow+Enter', await pg.evaluate("[!document.querySelector('.vw').hidden, document.querySelector('#vw-name').textContent, window.__links.length]"))
            await pg.keyboard.press('Escape'); await pg.wait_for_timeout(150)
            print(v.upper(), 'timeline focus back on', await pg.evaluate("[document.activeElement.className, document.activeElement.getAttribute('data-id'), document.activeElement.tabIndex, document.querySelectorAll('.tl a.tc[tabindex=\"0\"]').length]"))
            # a timeline day opens the viewer; the last day is today's issue
            tc = pg.locator('.tl a.tc.latest')
            await tc.scroll_into_view_if_needed(); await tc.click()
            await pg.wait_for_selector('.vw:not([hidden]) .mz[data-fit]', timeout=5000); await pg.wait_for_timeout(500)
            print(v.upper(), 'timeline latest', await pg.evaluate("[document.querySelector('#vw-name').textContent, document.querySelector('.vw .kicker').textContent, document.querySelector('.vw-step.next').disabled]"))
            await pg.screenshot(path=os.path.join(OUT, 'viewer_%s_latest_1440x900.jpg' % v), type='jpeg', quality=85)
            await pg.keyboard.press('Escape')
            # the longest past headline, at a short window
            await pg.set_viewport_size({'width': 1440, 'height': 780}); await pg.wait_for_timeout(400)
            await open_slot(pg, '2026-10-14-1')
            s = await pg.evaluate(VIEW)
            print(v.upper(), '10-14 at 1440x780', json.dumps({k: s[k] for k in ['cover', 'first', 'last', 'hl', 'vz', 'vcw']}, ensure_ascii=False))
            await pg.screenshot(path=os.path.join(OUT, 'viewer_%s_long_1440x780.jpg' % v), type='jpeg', quality=85)
            # resize while open: desktop -> narrow -> desktop
            await pg.set_viewport_size({'width': 900, 'height': 780}); await pg.wait_for_timeout(500)
            s1 = await pg.evaluate(VIEW)
            await pg.set_viewport_size({'width': 1440, 'height': 900}); await pg.wait_for_timeout(500)
            s2 = await pg.evaluate(VIEW)
            print(v.upper(), 'resize while open', s1['name'], s1['vz'], s1['vcw'], '->', s2['name'], s2['vz'], s2['vcw'], s2['hl'])
            print(v.upper(), 'errors', errs[:6])
            await pg.close()

        if 'a' not in vs:
            await br.close(); return
        # the review page: the switch changes the open viewer
        pg = await br.new_page(viewport={'width': 1440, 'height': 900})
        errs = track(pg)
        await pg.goto(URL('draft.html').replace('draft.html', 'draft_local.html'))
        await ready(pg)
        await open_slot(pg, '2026-09-23-1')
        a1 = await pg.evaluate("document.querySelector('.vw').className")
        await pg.click('.rv-b[data-v="B"]'); await pg.wait_for_timeout(400)
        a2 = await pg.evaluate("document.querySelector('.vw').className")
        await pg.screenshot(path=os.path.join(OUT, 'review_switch_1440x900.jpg'), type='jpeg', quality=85)
        print('review switch', a1, '->', a2, 'errors', errs[:5])
        await pg.close()
        await br.close()


asyncio.run(pages() if sys.argv[1] == 'pages' else viewer(tuple(sys.argv[2:]) or ('a', 'b')))
