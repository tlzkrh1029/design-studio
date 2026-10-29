#!/usr/bin/env python3
"""Render index.html at desktop and phone widths and check it (design principle 6).
Copied from ../beige-token-options/shot.py; only the demo and capture selectors differ.

  python3 shot.py [--fonts DIR]

DIR is a node_modules/@fontsource folder holding ibm-plex-sans-kr, noto-serif-kr and ibm-plex-mono
(npm install @fontsource/ibm-plex-sans-kr @fontsource/noto-serif-kr @fontsource/ibm-plex-mono).
With it, requests for Google Fonts are answered from those files, so the check also works offline.

Checks at 1440px and 390px: horizontal page scroll, console and page errors, web fonts loaded,
every element inside its stage, chrome text that overflows its box. Then it runs each row's
'같은 동작 보기' once (also with reduced motion) and saves screenshots to screenshots/.
"""
import argparse
import asyncio
import re
import sys
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).resolve().parent
OUT = HERE / 'screenshots'
FAMILIES = {  # Google Fonts family -> (fontsource package, weights)
    'IBM Plex Sans KR': ('ibm-plex-sans-kr', [400, 500, 600, 700]),
    'Noto Serif KR': ('noto-serif-kr', [700]),
    'IBM Plex Mono': ('ibm-plex-mono', [400, 500, 600]),
}


def local_font_css(fonts_dir):
    css = []
    for pkg, weights in FAMILIES.values():
        for w in weights:
            text = (fonts_dir / pkg / f'{w}.css').read_text(encoding='utf8')
            css.append(text.replace('url(./files/', f'url(https://fonts.gstatic.com/local/{pkg}/files/'))
    return '\n'.join(css)


async def check(page, width):
    return await page.evaluate('''(width) => {
      const doc = document.documentElement, out = {width};
      out.hscroll = doc.scrollWidth - doc.clientWidth;
      // Korean faces load per unicode-range chunk on demand, so count loaded faces instead of probing one glyph
      out.fonts = ['IBM Plex Sans KR', 'Noto Serif KR', 'IBM Plex Mono'].map(f => [f, [...document.fonts].some(ff => ff.family.replace(/["']/g, '') === f && ff.status === 'loaded')]);
      out.stages = [...document.querySelectorAll('.stage')].map(st => {
        const r = st.getBoundingClientRect(), el = st.querySelector('.ux').getBoundingClientRect();
        const inside = el.left >= r.left - 0.5 && el.right <= r.right + 0.5 && el.top >= r.top - 0.5 && el.bottom <= r.bottom + 0.5;
        const k = el.width / st.querySelector('.ux').offsetWidth;
        return {el: st.dataset.el, cell: st.closest('.cell').className.replace('cell ', ''), inside, k: +k.toFixed(3)};
      });
      out.overflow = [...document.querySelectorAll('.wrap *')].filter(n => {
        if (n.closest('.stage') || n.closest('.tbl')) return false;
        const cs = getComputedStyle(n);
        if (cs.display === 'inline' || cs.overflowX === 'auto' || cs.overflowX === 'scroll') return false;
        return n.scrollWidth > n.clientWidth + 1 && n.clientWidth > 0;
      }).map(n => n.tagName.toLowerCase() + '.' + n.className + ' "' + (n.textContent || '').trim().slice(0, 40) + '"').slice(0, 12);
      const tbl = document.querySelector('.tbl');
      out.tableScroll = tbl ? tbl.scrollWidth > tbl.clientWidth : null;
      return out;
    }''', width)


async def run(fonts_dir):
    OUT.mkdir(exist_ok=True)
    font_css = local_font_css(fonts_dir) if fonts_dir else None
    problems = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for width, height, tag in ((1440, 900, 'desktop'), (390, 844, 'mobile')):
            for reduced in (False, True):
                ctx = await browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=1,
                                                reduced_motion='reduce' if reduced else 'no-preference')
                page = await ctx.new_page()
                errors = []
                page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
                page.on('pageerror', lambda e: errors.append(str(e)))
                if font_css:
                    async def css_route(route):
                        await route.fulfill(status=200, content_type='text/css', body=font_css,
                                            headers={'Access-Control-Allow-Origin': '*'})
                    async def file_route(route):
                        m = re.search(r'/local/([^/]+)/files/([^?#]+)', route.request.url)
                        path = fonts_dir / m.group(1) / 'files' / m.group(2)
                        await route.fulfill(status=200, body=path.read_bytes(), content_type='font/woff2',
                                            headers={'Access-Control-Allow-Origin': '*'})
                    await page.route('https://fonts.googleapis.com/**', css_route)
                    await page.route('https://fonts.gstatic.com/local/**', file_route)
                await page.goto((HERE / 'index.html').as_uri())
                await page.evaluate('document.fonts.ready')
                await page.wait_for_timeout(600)
                res = await check(page, width)
                label = f'{tag}{" reduced-motion" if reduced else ""}'
                print(f'== {label}: hscroll {res["hscroll"]}px, table scrolls inside its box: {res["tableScroll"]}')
                print('   fonts:', ', '.join(f'{f} {"ok" if ok else "MISSING"}' for f, ok in res['fonts']))
                print('   stages:', ' '.join(f'{s["el"]}/{s["cell"]}:{"ok" if s["inside"] else "CLIPPED"}@{s["k"]}' for s in res['stages']))
                if res['overflow']:
                    print('   text overflow:', res['overflow'])
                if res['hscroll'] > 0: problems.append(f'{label}: page scrolls sideways by {res["hscroll"]}px')
                if any(not s['inside'] for s in res['stages']): problems.append(f'{label}: an element is clipped by its stage')
                if res['overflow']: problems.append(f'{label}: text overflows its box')
                if font_css and not all(ok for _, ok in res['fonts']): problems.append(f'{label}: a web font did not load')
                if not reduced:
                    await page.screenshot(path=str(OUT / f'{tag}-full.jpg'), full_page=True, type='jpeg', quality=82)
                # run every row's demo once; capture mid-run states on the desktop pass
                for row_id, at in (('023', 3200), ('042', 4300), ('072', 1300)):
                    btn = page.locator(f'[data-play="{row_id}"]').first
                    await btn.scroll_into_view_if_needed()
                    await btn.click()
                    await page.wait_for_timeout(at)
                    if tag == 'desktop' and not reduced:
                        await page.locator(f'.row[data-row="{row_id}"]').first.screenshot(
                            path=str(OUT / f'{tag}-{row_id}-demo.jpg'), type='jpeg', quality=85)
                await page.wait_for_timeout(9000)
                res2 = await check(page, width)
                if any(not s['inside'] for s in res2['stages']): problems.append(f'{label}: clipped after demos')
                # keyboard: the first switch in the first A cell shows a focus ring
                ring = await page.evaluate('''() => { const b = document.querySelector('.t-fix .u023-sw'); b.focus({focusVisible: true});
                  const cs = getComputedStyle(b); return cs.outlineStyle + ' ' + cs.outlineWidth + ' ' + cs.outlineColor; }''')
                print('   focus ring on 023 switch (fixed):', ring)
                if errors:
                    problems.append(f'{label}: console errors {errors[:3]}')
                    print('   errors:', errors[:5])
                if tag == 'desktop' and not reduced:
                    await page.evaluate('window.scrollTo(0, 0)')
                    for sel, name in (('.top', 'header'), ('#d1', 'tokens'), ('#d3', 'checks')):
                        loc = page.locator(sel).locator('xpath=..') if sel.startswith('#') else page.locator(sel).first
                        await loc.screenshot(path=str(OUT / f'{tag}-{name}.jpg'), type='jpeg', quality=85)
                await ctx.close()
        await browser.close()
    print('\nPROBLEMS:' if problems else '\nNo problems found.')
    for x in problems:
        print(' -', x)
    return not problems


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--fonts', type=Path, help='node_modules/@fontsource folder')
    args = ap.parse_args()
    sys.exit(0 if asyncio.run(run(args.fonts)) else 1)
