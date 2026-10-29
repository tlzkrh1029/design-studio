#!/usr/bin/env python3
"""Build index.html: the upstream look next to the upstream look with its contrast fixed.

Run from anywhere:  python3 lcan-design/drafts/original-contrast-fix/build.py

Inputs (relative to the repository root):
  lcan-design/upstream/lucian-uxui-prompt/tokens.css   upstream tokens; the light block styles both columns
  lcan-design/upstream/lucian-uxui-prompt/NNN-*.html   the three upstream elements, pasted into the page unchanged
  lcan-design/base.css                                  token defaults and the .ux base rules
  <this folder>/contrast-fix.css                        the six tokens changed for 4.5:1 text contrast
Output: <this folder>/index.html (one self-contained page; the chrome fonts come from Google Fonts)

Follows lcan-design/drafts/beige-token-options/build.py; the helpers are copied so each draft rebuilds on its own.
"""
import colorsys
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
UP = REPO / 'lcan-design' / 'upstream' / 'lucian-uxui-prompt'
COMMIT = '7e339fa'

ELEMENTS = [  # id, upstream file, title, natural height (px), what changes, colours written into the element
    ('023', '023-settings-switch-list.html', '펼쳐지는 알림 설정', 420,
     '작은 설명 글자, ‘2개 켜짐’ 배지의 글자, 켜진 스위치의 초록이 바뀝니다. ‘모두 끄기’에 마우스를 올렸을 때의 빨강도 바뀝니다.',
     '왼쪽 아이콘 칸 세 개의 그라디언트는 요소 코드에 적혀 있어서 두 칸에서 같습니다.'),
    ('042', '042-wizard-stepper.html', '단계 진행 마법사', 400,
     '작은 설명 글자와 아직 오지 않은 단계의 번호, 현재 단계의 보라, 마지막 단계의 큰 체크와 ‘시작하기’ 단추의 초록이 바뀝니다. 진행선의 그라디언트는 그대로입니다.',
     '셋째 단계에 있는 프로필 동그라미 두 개의 색은 요소 코드에 적혀 있습니다.'),
    ('072', '072-inline-alert-dismiss.html', '접히는 인라인 알림', 470,
     '네 알림 줄의 색(위로부터 위험, 경고, 강조, 완료)과 ‘알림 4개’ 같은 작은 글자가 바뀝니다.',
     '직접 적은 색은 없습니다.'),
]

THEMES = {  # class: (label, sub-label, files stacked on the upstream light values)
    't-orig': ('원본', 'Lucian 기본값 그대로', []),
    't-fix': ('보정판', '토큰 여섯 개만 보정', ['contrast-fix.css']),
}

# Elements of commit 7e339fa (all 400) whose CSS uses the token in a `color:` rule; counted from upstream src/elements.
TEXT_USE = {'--ux-ink-3': 222, '--ux-accent': 88, '--ux-mint': 30, '--ux-danger': 31, '--ux-warn': 6, '--ux-accent-2': 1}
ROLE = {'--ux-ink-3': '작은 설명 글자', '--ux-accent': '강조', '--ux-accent-2': '보조 강조',
        '--ux-mint': '완료', '--ux-warn': '경고', '--ux-danger': '위험'}


# ---------- CSS custom properties ----------
def root_props(text):
    text = re.sub(r'/\*[\s\S]*?\*/', '', text)
    block = re.search(r'(?<![\w-]):root\s*\{([^}]*)\}', text).group(1)
    props = {}
    for decl in block.split(';'):
        m = re.match(r'\s*(--[\w-]+|color-scheme)\s*:\s*(.+?)\s*$', decl, re.S)
        if m:
            props[m.group(1)] = re.sub(r'\s+', ' ', m.group(2))
    return props


upstream = root_props((UP / 'tokens.css').read_text(encoding='utf8'))
base_props = root_props((REPO / 'lcan-design' / 'base.css').read_text(encoding='utf8'))
for k, v in upstream.items():
    assert base_props.get(k, '').replace(' ', '') == v.replace(' ', ''), f'base.css differs from upstream for {k}'

fix_props = root_props((HERE / 'contrast-fix.css').read_text(encoding='utf8'))
assert set(fix_props) == set(TEXT_USE), f'contrast-fix.css changes {sorted(fix_props)}'
theme_props = {}
for cls, (_, _, stack) in THEMES.items():
    props = dict(upstream)
    for rel in stack:
        props.update(root_props((HERE / rel).read_text(encoding='utf8')))
    props['color-scheme'] = 'light'
    theme_props[cls] = props


# ---------- colour maths (WCAG 2.x) ----------
def parse_colour(v, bg=None):
    v = v.strip()
    if v.startswith('#'):
        h = v[1:]
        if len(h) == 3:
            h = ''.join(c * 2 for c in h)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.match(r'rgba?\(([^)]*)\)', v.replace(' ', ''))
    parts = [float(x) for x in m.group(1).split(',')]
    rgb, a = parts[:3], (parts[3] if len(parts) > 3 else 1)
    return tuple(a * c + (1 - a) * b for c, b in zip(rgb, bg))


def mix(a, b, t):  # color-mix(in srgb, a t, b)
    return tuple(x * t + y * (1 - t) for x, y in zip(a, b))


def lum(c):
    v = [x / 255 for x in c]
    v = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in v]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def tok(props, name, bg=None):
    return parse_colour(props[name], bg)


def checks(props):
    """Text contrast at the places in the three elements where a changed token is used as text."""
    surf, surf2 = tok(props, '--ux-surface'), tok(props, '--ux-surface-2')
    acc, dan = tok(props, '--ux-accent'), tok(props, '--ux-danger')
    return [
        ('작은 설명 글자(카드 위)', ratio(tok(props, '--ux-ink-3'), surf)),
        ('023 ‘2개 켜짐’ 배지', ratio(acc, tok(props, '--ux-accent-soft', surf))),
        ('023 ‘모두 끄기’에 올렸을 때', ratio(dan, mix(dan, surf2, .10))),
        ('042 현재 단계 번호', ratio(acc, surf)),
        ('042 ‘시작하기’ 단추 글자', ratio(tok(props, '--ux-accent-ink'), tok(props, '--ux-mint'))),
        ('072 ‘자세히’ 글자', ratio(dan, mix(dan, surf, .10))),
    ]


def lowest_on_surfaces(props, name):
    c = tok(props, name)
    return min(ratio(c, tok(props, s)) for s in ('--ux-page', '--ux-surface', '--ux-surface-2'))


def hls_drop(a, b):
    la = colorsys.rgb_to_hls(*[x / 255 for x in parse_colour(a)])[1]
    lb = colorsys.rgb_to_hls(*[x / 255 for x in parse_colour(b)])[1]
    return (la - lb) * 100


# ---------- elements ----------
def split_element(src):
    m = re.search(r'<script>([\s\S]*?)</script>\s*$', src)
    return src[:m.start()].rstrip() + '\n', m.group(1)


def demo_steps(el_id):
    # The upstream @demo steps (taps and waits only) of commit 7e339fa, restated from src/elements.
    return {
        '023': [['wait', 500], ['tap', '.u023-sw', 1], ['wait', 1100], ['tap', '.u023-opt', 0], ['wait', 900],
                ['tap', '.u023-opt', 2], ['wait', 1000], ['tap', '.u023-all'], ['wait', 1900], ['reset']],
        '042': [['wait', 700], ['tap', '.u042-next'], ['wait', 1200], ['tap', '.u042-next'], ['wait', 1200],
                ['tap', '.u042-next'], ['wait', 1300], ['tap', '.u042-prev'], ['wait', 1000], ['tap', '.u042-next'],
                ['wait', 1100], ['tap', '.u042-next'], ['wait', 1800]],
        '072': [['wait', 800], ['tap', '.u072-more'], ['wait', 1500], ['tap', '.u072-more'], ['wait', 700],
                ['tap', '.u072-x', 1], ['wait', 900], ['tap', '.u072-x', 0], ['wait', 800], ['tap', '.u072-x', 2],
                ['wait', 800], ['tap', '.u072-x', 3], ['wait', 1500], ['tap', '.u072-again'], ['wait', 1600]],
    }[el_id]


sources, snippets = {}, {}
for el_id, fname, *_ in ELEMENTS:
    raw = (UP / fname).read_text(encoding='utf8')
    assert raw.startswith(f'<!-- Lucian UX/UI Prompt #{el_id} · MIT License'), f'{fname}: license line missing'
    head, js = split_element(raw)
    sources[el_id] = {'html': head, 'js': js, 'steps': demo_steps(el_id)}
    snippets[el_id] = raw


# ---------- page parts ----------
E = html.escape


def fmt(x):
    return f'{x:.2f}'


def ratio_cell(x):
    flag = '' if x >= 4.5 else '<span class="miss">기준 미달</span>'
    return f'<td class="n">{fmt(x)}{flag}</td>'


def cell(cls, el_id, height):
    label, sub, _ = THEMES[cls]
    flip = ' flip' if cls == 't-fix' else ''
    return (f'<figure class="cell {cls}{flip}">'
            f'<figcaption><b>{E(label)}</b><span>{E(sub)}</span></figcaption>'
            f'<div class="stage" data-el="{el_id}" style="--h:{height}px" role="group" aria-label="{E(label)}: {el_id}">'
            f'<div class="fit">\n{snippets[el_id]}</div></div></figure>')


def row(el_id, fname, title, height, look, fixed):
    cells = ''.join(cell(c, el_id, height) for c in THEMES)
    return (f'<article class="row" data-row="{el_id}">'
            f'<div class="row-head"><div class="row-title"><h3><span class="num">{el_id}</span>{E(title)}</h3>'
            f'<p class="look">{E(look)}</p><p class="fixed">{E(fixed)}</p></div>'
            f'<div class="row-ctl"><button type="button" class="btn btn-ink" data-play="{el_id}">같은 동작 보기</button>'
            f'<button type="button" class="btn" data-reset="{el_id}">처음 상태로</button></div></div>'
            f'<div class="cells">{cells}</div></article>')


O, F = theme_props['t-orig'], theme_props['t-fix']
token_rows = []
for name in TEXT_USE:
    a, b = O[name], F[name]
    token_rows.append(
        f'<tr><th scope="row"><code>{E(name)}</code><span class="role">{E(ROLE[name])}</span></th>'
        f'<td class="val"><i class="sw" style="background:{a}" aria-hidden="true"></i><code>{a}</code></td>'
        f'<td class="val"><i class="sw" style="background:{b}" aria-hidden="true"></i><code>{b}</code></td>'
        f'<td class="n">−{hls_drop(a, b):.1f}</td>'
        f'<td class="n">{fmt(lowest_on_surfaces(O, name))} → {fmt(lowest_on_surfaces(F, name))}</td>'
        f'<td class="n">{TEXT_USE[name]}</td></tr>')

check_html = []
for (label, a), (_, b) in zip(checks(O), checks(F)):
    check_html.append(f'<tr><th scope="row">{E(label)}</th>{ratio_cell(a)}{ratio_cell(b)}</tr>')

CHROME_CSS = r'''
/* Layout: a specimen sheet. The decision and the six changed tokens sit at the top; each element then gets
   one row with the upstream look and the fixed look side by side; the contrast checks and the limits close the page.
   The chrome keeps the artifact-design beige style of the first comparison, which commits to one light look. */
:root {
  color-scheme: light;
  --paper: #F6F3EC;   /* screen */
  --card: #FFFDF8;    /* cards */
  --sub: #EFEAE0;     /* secondary surface */
  --line: #DCD5C6;    /* borders */
  --rule: #B9B0A0;    /* stronger lines, never text */
  --ink: #1A1916;
  --ink-2: #57534A;
  --ink-3: #6E695E;   /* small notes, 4.56:1 on --sub */
  --hl: #F4E27C;      /* the one highlight: what to decide */
  --miss: #B8322A;
  --sans: "IBM Plex Sans KR", "Apple SD Gothic Neo", "Noto Sans KR", system-ui, sans-serif;
  --serif: "Noto Serif KR", "AppleMyungjo", "Nanum Myeongjo", ui-serif, serif;
  --mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
}
html { background: var(--paper) }
body { background: var(--paper); color: var(--ink); font: 400 14px/1.6 var(--sans); }
.wrap { max-width: 1400px; margin: 0 auto; padding-block: 40px 64px; word-break: keep-all; overflow-wrap: break-word;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
@media (min-width: 720px) { .wrap { padding-left: max(32px, env(safe-area-inset-left, 0px)); padding-right: max(32px, env(safe-area-inset-right, 0px)); } }
.wrap code, .wrap .mono { font-family: var(--mono); font-size: .92em; }
.top { display: grid; gap: 14px; }
.kicker { margin: 0; font-size: 12.5px; font-weight: 600; color: var(--ink-2); letter-spacing: .02em; }
.top h1 { margin: 0; font: 700 30px/1.3 var(--serif); letter-spacing: -.01em; text-wrap: balance; }
.lead { margin: 0; max-width: 64ch; font-size: 15px; line-height: 1.75; }
.decide { margin: 8px 0 0; max-width: 960px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px; display: grid; gap: 4px; }
.decide dt { font-weight: 700; font-size: 15px; }
.decide dt mark { background: linear-gradient(transparent 58%, var(--hl) 58%); color: inherit; padding: 0 2px; }
.decide dd { margin: 0; color: var(--ink-2); }
.meta { margin: 0; font-size: 12.5px; color: var(--ink-3); max-width: 80ch; }
section.part { margin-top: 56px; }
.part > h2 { margin: 0 0 6px; font-size: 20px; font-weight: 700; letter-spacing: -.01em; }
.intro { margin: 0; max-width: 72ch; color: var(--ink-2); }
.part-ctl { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 14px; margin-top: 14px; }
.flip-state { font-size: 12.5px; color: var(--ink-2); }
.sw { flex: none; width: 14px; height: 14px; border-radius: 3px; box-shadow: inset 0 0 0 1px rgba(26,25,22,.18); }
.row { margin-top: 28px; padding-top: 22px; border-top: 1px solid var(--line); }
.row-head { display: flex; flex-wrap: wrap; gap: 12px 24px; align-items: flex-start; justify-content: space-between; }
.row-title { flex: 999 1 520px; min-width: 0; display: grid; gap: 4px; }
.row-title h3 { margin: 0; font-size: 17px; font-weight: 700; display: flex; align-items: baseline; gap: 10px; }
.num { font-family: var(--mono); font-size: 13px; font-weight: 600; color: var(--ink-2); }
.look { margin: 0; max-width: 80ch; }
.fixed { margin: 0; max-width: 80ch; font-size: 12.5px; color: var(--ink-3); }
.row-ctl { flex: 1 0 auto; display: flex; flex-wrap: wrap; gap: 8px; }
.btn { height: 44px; padding: 0 16px; border-radius: 999px; border: 1px solid var(--rule); background: var(--card); color: var(--ink); font: 600 13.5px/1 var(--sans); cursor: pointer; }
.btn:hover { background: var(--sub); }
.btn-ink { background: var(--ink); color: var(--card); border-color: var(--ink); }
.btn-ink:hover { background: #33312C; }
.btn[aria-pressed="true"] { background: var(--ink); color: var(--card); border-color: var(--ink); }
.btn:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.btn[disabled] { opacity: .55; cursor: default; }
.cells { display: grid; gap: 12px; margin-top: 16px; max-width: 960px; }
@media (min-width: 640px) { .cells { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.cell { margin: 0; min-width: 0; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; background: var(--ux-page); }
.cell figcaption { display: flex; align-items: baseline; justify-content: space-between; gap: 8px; padding: 9px 12px; background: var(--card); border-bottom: 1px solid var(--line); font-size: 12.5px; }
.cell figcaption b { font-size: 13.5px; }
.cell figcaption span { color: var(--ink-3); text-align: right; }
.cell.is-flipped figcaption b::after { content: " · 지금은 원본 값"; font-weight: 600; color: var(--ink-2); }
.stage { position: relative; overflow: hidden; height: calc(var(--h) + 52px); }
/* inherited text settings as in the upstream gallery, so the elements see the same defaults */
.fit { position: absolute; left: 50%; top: 50%; width: max-content; transform: translate(-50%, -50%); transform-origin: 50% 50%;
  font-size: 16px; font-weight: 400; line-height: normal; letter-spacing: -.01em; text-align: left; white-space: normal; word-break: normal; overflow-wrap: normal; color: var(--ux-ink); }
.tbl { margin-top: 16px; overflow-x: auto; border: 1px solid var(--line); border-radius: 12px; background: var(--card); max-width: 960px; }
.tbl table { width: 100%; border-collapse: collapse; min-width: 600px; }
.tbl th, .tbl td { padding: 10px 12px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; font-size: 13px; }
.tbl tr:last-child > * { border-bottom: 0; }
.tbl thead th { font-size: 12.5px; color: var(--ink-2); font-weight: 700; background: var(--sub); }
.tbl th[scope="row"] { font-weight: 600; }
.tbl th code { white-space: nowrap; }
.tbl .role { display: block; font-size: 12px; font-weight: 400; color: var(--ink-3); }
.tbl .n { font-family: var(--mono); font-size: 12.5px; white-space: nowrap; font-variant-numeric: tabular-nums; }
.tbl .val { white-space: nowrap; }
.tbl .val .sw { display: inline-block; vertical-align: -2px; margin-right: 6px; }
.scroll-hint { display: none; margin: 8px 0 0; font-size: 12.5px; color: var(--ink-3); }
@media (max-width: 700px) { .scroll-hint { display: block; } }
.miss { margin-left: 6px; padding: 1px 6px; border-radius: 999px; border: 1px solid var(--miss); color: var(--miss); font: 600 11px/1.4 var(--sans); }
.note { margin: 10px 0 0; font-size: 12.5px; color: var(--ink-3); max-width: 80ch; }
.limits { margin: 16px 0 0; padding: 0; list-style: none; display: grid; gap: 10px; max-width: 80ch; }
.limits li { padding: 12px 14px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; }
.limits b { display: block; margin-bottom: 2px; }
.foot { margin-top: 56px; padding-top: 16px; border-top: 1px solid var(--line); font-size: 12.5px; color: var(--ink-3); display: grid; gap: 4px; }
.foot a { color: var(--ink-2); }
.foot a:hover { color: var(--ink); }
'''

BOARD_JS = r'''
(function () {
  var SRC = JSON.parse(document.getElementById('lcan-src').textContent);
  var PAD = 20;
  function fit(stage) {
    var f = stage.querySelector('.fit');
    if (!f) return;
    var w = f.offsetWidth, h = f.offsetHeight;
    if (!w || !h) return;
    var k = Math.max(0.3, Math.min(1, (stage.clientWidth - PAD * 2) / w));
    f.style.transform = 'translate(-50%,-50%) scale(' + k.toFixed(4) + ')';
    stage.style.height = Math.ceil(h * k + PAD * 2 + 12) + 'px';
  }
  var stages = Array.prototype.slice.call(document.querySelectorAll('.stage'));
  if (window.ResizeObserver) {
    var ro = new ResizeObserver(function (entries) { entries.forEach(function (en) { fit(en.target); }); });
    stages.forEach(function (s) { ro.observe(s); });
  } else {
    window.addEventListener('resize', function () { stages.forEach(fit); });
  }
  stages.forEach(fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { stages.forEach(fit); });

  // A fresh copy of the element, mounted the way the upstream gallery mounts one
  function mount(stage) {
    var src = SRC[stage.getAttribute('data-el')], f = stage.querySelector('.fit');
    stage._run = (stage._run || 0) + 1;
    f.innerHTML = src.html;
    var s = document.createElement('script');
    s.textContent = src.js;
    f.appendChild(s);
    fit(stage);
  }
  function wait(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  // The upstream demo steps (taps and waits), run on one cell; a newer mount or run stops an older one
  function play(stage) {
    var steps = SRC[stage.getAttribute('data-el')].steps, i = 0;
    mount(stage);
    var token = stage._run;
    function next() {
      if (stage._run !== token || i >= steps.length) return Promise.resolve();
      var st = steps[i++], root = stage.querySelector('.ux');
      if (st[0] === 'wait') return wait(st[1]).then(next);
      if (st[0] === 'tap') { var el = root && root.querySelectorAll(st[1])[st[2] || 0]; if (el) el.click(); return next(); }
      if (st[0] === 'reset') { mount(stage); return Promise.resolve(); }
      return next();
    }
    return next();
  }
  function stagesOf(btn) { return Array.prototype.slice.call(btn.closest('.row').querySelectorAll('.stage')); }
  document.querySelectorAll('[data-play]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      btn.disabled = true;
      Promise.all(stagesOf(btn).map(play)).then(function () { btn.disabled = false; });
    });
  });
  document.querySelectorAll('[data-reset]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      stagesOf(btn).forEach(mount);
      var play = btn.parentNode.querySelector('[data-play]');
      if (play) play.disabled = false;
    });
  });

  // Alternate the fixed cells between the fixed and the upstream values, so small changes are easy to see
  var flipBtn = document.getElementById('flip'), flipState = document.getElementById('flip-state'), timer = null;
  var cells = Array.prototype.slice.call(document.querySelectorAll('.cell.flip'));
  function show(orig) {
    cells.forEach(function (c) { c.classList.toggle('t-orig', orig); c.classList.toggle('t-fix', !orig); c.classList.toggle('is-flipped', orig); });
    flipState.textContent = timer ? (orig ? '오른쪽 칸: 지금은 원본 값입니다.' : '오른쪽 칸: 지금은 보정판 값입니다.') : '';
  }
  if (flipBtn) flipBtn.addEventListener('click', function () {
    var on = flipBtn.getAttribute('aria-pressed') !== 'true';
    flipBtn.setAttribute('aria-pressed', String(on));
    clearInterval(timer); timer = null;
    if (on) { var orig = false; timer = setInterval(function () { orig = !orig; show(orig); }, 1200); show(false); }
    else show(false);
  });
})();
'''


def scoped_theme_css():
    return '\n'.join('.' + cls + '{' + ';'.join(f'{k}:{v}' for k, v in props.items()) + '}' for cls, props in theme_props.items())


base_css = (REPO / 'lcan-design' / 'base.css').read_text(encoding='utf8')
el_rows = ''.join(row(*e) for e in ELEMENTS)
src_json = json.dumps(sources, ensure_ascii=False).replace('</', '<\\/')
orig_miss = sum(1 for _, v in checks(O) if v < 4.5)
fix_low = min(v for _, v in checks(F))

page = f'''<title>Lucian 원본 명암비 보정</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans+KR:wght@400;500;600;700&family=Noto+Serif+KR:wght@700&display=swap">
<!-- Built by lcan-design/drafts/original-contrast-fix/build.py from upstream commit {COMMIT}. Do not edit by hand. -->
<style>{CHROME_CSS}</style>
<style>
/* lcan-design/base.css */
{base_css}
/* themes, one class per cell */
{scoped_theme_css()}
</style>
<div class="wrap">
<header class="top">
  <p class="kicker">lcan-design 둘째 비교 · 2026년 10월 29일</p>
  <h1>원본과 명암비 보정판</h1>
  <p class="lead">앞선 비교에서 세 요소 모두 Lucian 원본이 낫다고 하셨습니다. 그런데 원본 값은 디자인 원칙 3(글자 명암비 4.5:1)에 못 미치는 곳이 있습니다. 그래서 원본의 모양은 그대로 두고, 기준에 못 미치는 토큰 여섯 개만 고친 보정판을 만들어 원본과 나란히 놓았습니다. 보정판은 각 토큰의 색상과 채도를 그대로 두고, 밝기만 기준을 넘는 데까지 가장 적게 낮췄습니다.</p>
  <dl class="decide">
    <dt><mark>고를 것</mark> 보정판을 기본으로 쓸지, 원본을 그대로 쓸지</dt>
    <dd>이번에 점검한 여섯 곳에서 원본은 {orig_miss}곳이 4.5:1에 못 미치고, 보정판은 모두 4.5:1 이상입니다(가장 낮은 곳 {fmt(fix_low)}:1). 두 칸의 차이가 잘 보이지 않으면 아래의 ‘번갈아 보기’를 눌러 보세요.</dd>
  </dl>
  <p class="meta">원본은 Lucian UX/UI Prompt 커밋 <span class="mono">{COMMIT}</span>입니다. 두 칸 모두 원본 갤러리처럼 웹 글꼴을 불러오지 않아서, 기기의 글꼴로 보입니다. 라이트 화면만 비교합니다.</p>
</header>

<section class="part" aria-labelledby="d1">
  <h2 id="d1">바뀌는 토큰 여섯 개</h2>
  <p class="intro">나머지 토큰(바탕, 카드, 선, 본문 글자, 그림자, 그라디언트 등)은 원본 값 그대로입니다.</p>
  <div class="tbl"><table>
    <thead><tr><th scope="col">토큰</th><th scope="col">원본</th><th scope="col">보정판</th><th scope="col">밝기 변화(HLS)</th><th scope="col">가장 낮은 글자 명암비</th><th scope="col">글자로 쓰는 요소 수</th></tr></thead>
    <tbody>{''.join(token_rows)}</tbody>
  </table></div>
  <p class="scroll-hint">표를 옆으로 밀면 나머지 열이 보입니다.</p>
  <p class="note">가장 낮은 글자 명암비는 바탕, 카드, 보조 면 가운데 가장 낮은 값입니다. 글자로 쓰는 요소 수는 원본 요소 400개 가운데 그 토큰을 글자색(<code>color:</code>)으로 쓰는 요소의 수입니다.</p>
</section>

<section class="part" aria-labelledby="d2">
  <h2 id="d2">세 요소</h2>
  <p class="intro">왼쪽은 원본, 오른쪽은 보정판입니다. 칸 안의 요소를 직접 눌러 볼 수 있고, ‘같은 동작 보기’를 누르면 두 칸이 같은 순서로 움직입니다.</p>
  <div class="part-ctl"><button type="button" class="btn" id="flip" aria-pressed="false">번갈아 보기</button><span class="flip-state" id="flip-state" aria-live="polite"></span></div>
  {el_rows}
</section>

<section class="part" aria-labelledby="d3">
  <h2 id="d3">글자 명암비 점검</h2>
  <p class="intro">바뀌는 토큰이 세 요소 안에서 글자색으로 쓰이는 곳의 명암비입니다. 기준은 디자인 원칙 3의 4.5:1입니다.</p>
  <div class="tbl"><table>
    <thead><tr><th scope="col">위치</th><th scope="col">원본</th><th scope="col">보정판</th></tr></thead>
    <tbody>{''.join(check_html)}</tbody>
  </table></div>
</section>

<section class="part" aria-labelledby="d4">
  <h2 id="d4">이번 보정으로 다루지 않은 것</h2>
  <ul class="limits">
    <li><b>다크 화면</b>원본의 다크 값도 작은 설명 글자(<code>--ux-ink-3</code>)가 3.56~3.72:1로 4.5:1에 못 미칩니다. 이번에는 라이트 값만 보정했습니다.</li>
    <li><b>요소에 직접 적은 색</b>원본 요소 400개 가운데 242개는 흰색과 검은색이 아닌 색을 요소 코드에 직접 적어 두었습니다. 그런 색은 토큰 보정으로 바뀌지 않으므로, 요소를 들일 때 하나씩 확인해야 합니다.</li>
    <li><b>그림이나 아이콘의 명암비</b>스위치, 아이콘, 진행 막대처럼 글자가 아닌 표시는 이번 점검에 넣지 않았습니다.</li>
  </ul>
</section>

<footer class="foot">
  <p>요소 출처: Lucian UX/UI Prompt(MIT 라이선스, © 2026 Seokwoooo)의 <a href="https://lucianlabs.dev/uxui-prompt/#023">023</a>, <a href="https://lucianlabs.dev/uxui-prompt/#042">042</a>, <a href="https://lucianlabs.dev/uxui-prompt/#072">072</a>. 이 화면은 원작자와 관계없는 사본이며, 요소 코드 맨 위의 라이선스 주석을 그대로 남겨 두었습니다.</p>
</footer>
</div>
<script type="application/json" id="lcan-src">{src_json}</script>
<script>{BOARD_JS}</script>
'''

(HERE / 'index.html').write_text(page, encoding='utf8')
print(f'index.html written ({len(page.encode("utf8")) / 1024:.0f} KB)')
for (label, a), (_, b) in zip(checks(O), checks(F)):
    print(f'{label}: {fmt(a)} -> {fmt(b)}')
