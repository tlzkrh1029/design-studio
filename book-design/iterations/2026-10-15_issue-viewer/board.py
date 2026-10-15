"""Before/after board: python3 board.py  ->  screenshots/board.jpg (and the panels it is made of)."""
import os, asyncio
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'screenshots')
URL = lambda f: 'file://' + os.path.join(HERE, f)
ID = '2026-09-23-1'


async def page(br, f, w, h):
    pg = await br.new_page(viewport={'width': w, 'height': h})
    await pg.goto(URL(f))
    await pg.wait_for_selector('body[data-ready]', timeout=20000)
    await pg.wait_for_timeout(700)
    return pg


async def to_rack(pg):
    await pg.evaluate("()=>{document.documentElement.style.scrollBehavior='auto'; var r=document.getElementById('rack'); window.scrollTo(0, r.getBoundingClientRect().top+window.scrollY-40);}")
    await pg.wait_for_timeout(400)


async def open_(pg):
    el = pg.locator('#rack [data-id="%s"]' % ID)
    await el.scroll_into_view_if_needed(); await el.click()
    await pg.wait_for_selector('.vw:not([hidden]) .mz[data-fit]'); await pg.wait_for_timeout(1000)


async def shots():
    async with async_playwright() as p:
        br = await p.chromium.launch()
        for w, h, tag in [(1440, 900, 'd'), (390, 844, 'm')]:
            pg = await page(br, 'preview_base.html', w, h)
            await to_rack(pg)
            await pg.screenshot(path=os.path.join(OUT, 'board_%s_now.jpg' % tag), type='jpeg', quality=85)
            if tag == 'd':
                await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(300)
                await pg.screenshot(path=os.path.join(OUT, 'board_hero_before.jpg'), type='jpeg', quality=85)
            await pg.close()
            for v in ['a', 'b']:
                pg = await page(br, 'preview_%s.html' % v, w, h)
                if tag == 'd' and v == 'a':
                    await pg.screenshot(path=os.path.join(OUT, 'board_hero_after.jpg'), type='jpeg', quality=85)
                await open_(pg)
                await pg.screenshot(path=os.path.join(OUT, 'board_%s_%s.jpg' % (tag, v)), type='jpeg', quality=85)
                await pg.close()
        # compose
        H = '''<!doctype html><meta charset=utf8>
<link rel="stylesheet" href="../../../cover_design/node_modules/@fontsource/gothic-a1/500.css">
<link rel="stylesheet" href="../../../cover_design/node_modules/@fontsource/gothic-a1/700.css">
<link rel="stylesheet" href="../../../cover_design/node_modules/@fontsource/gothic-a1/800.css">
<style>
body{margin:0;background:#08090C;color:#F2F0EC;font-family:'Gothic A1',sans-serif;padding:48px 56px 56px;width:2400px;box-sizing:border-box}
h1{margin:0 0 6px;font-size:34px;font-weight:800}
.sub{margin:0 0 40px;color:#8A919B;font-size:18px;font-weight:500}
h2{margin:44px 0 18px;font-size:22px;font-weight:700;color:#B4B9C1}
.row{display:flex;gap:28px;align-items:flex-start}
figure{margin:0}
figcaption{margin-top:12px;font-size:17px;font-weight:700}
figcaption span{display:block;margin-top:4px;font-size:15px;font-weight:500;color:#8A919B}
.d img{width:744px;display:block;border:1px solid #232932}
.m img{width:300px;display:block;border:1px solid #232932}
.h img{width:1130px;display:block;border:1px solid #232932}
</style>
<h1>서고 열람 창 시안</h1><p class="sub">가판대의 지난 호(9월 23일, 제23호)를 눌렀을 때 · 10월 15일 12시 데이터 사본</p>
<h2>데스크톱 1440 × 900</h2>
<div class="row d">
<figure><img src="board_d_now.jpg"><figcaption>지금<span>표지를 누르면 새 탭에서 브리핑이 바로 열립니다.</span></figcaption></figure>
<figure><img src="board_d_a.jpg"><figcaption>시안 A · 오늘의 호처럼<span>전등과 받침을 그대로 두고 표지 폭 400px</span></figcaption></figure>
<figure><img src="board_d_b.jpg"><figcaption>시안 B · 표지 크게<span>전등 없이 창 높이에 맞춰 표지 폭 360~520px</span></figcaption></figure>
</div>
<h2>휴대폰 390 × 844</h2>
<div class="row m">
<figure><img src="board_m_now.jpg"><figcaption>지금</figcaption></figure>
<figure><img src="board_m_a.jpg"><figcaption>시안 A<span>표지 240px</span></figcaption></figure>
<figure><img src="board_m_b.jpg"><figcaption>시안 B<span>표지 358px</span></figcaption></figure>
</div>
<h2>함께 고친 결함: 첫 화면 헤드라인이 길 때(10월 15일, 191자)</h2>
<div class="row h">
<figure><img src="board_hero_before.jpg"><figcaption>지금<span>'오늘의 호 · 제46호'와 날짜가 위로 잘리고 '브리핑 펼치기' 단추가 아래로 잘립니다.</span></figcaption></figure>
<figure><img src="board_hero_after.jpg"><figcaption>고친 뒤<span>헤드라인을 26px까지 줄여 모든 줄이 첫 화면 안에 들어갑니다.</span></figcaption></figure>
</div>'''
        open(os.path.join(OUT, 'board.html'), 'w', encoding='utf-8').write(H)
        pg = await br.new_page(viewport={'width': 2400, 'height': 1000})
        await pg.goto('file://' + os.path.join(OUT, 'board.html'))
        await pg.wait_for_timeout(800)
        await pg.screenshot(path=os.path.join(OUT, 'board.jpg'), full_page=True, type='jpeg', quality=85)
        await pg.close(); await br.close()


asyncio.run(shots())
