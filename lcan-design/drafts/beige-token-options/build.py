#!/usr/bin/env python3
"""Build index.html, the beige token comparison page, from the lcan-design sources.

Run from anywhere:  python3 lcan-design/drafts/beige-token-options/build.py

Inputs (relative to the repository root):
  lcan-design/upstream/lucian-uxui-prompt/tokens.css   upstream tokens; the light block styles the original column
  lcan-design/upstream/lucian-uxui-prompt/NNN-*.html   the three upstream elements, pasted into the page unchanged
  lcan-design/base.css                                  token defaults and the .ux base rules
  artifact-design/lcan-theme.css                        documented beige values
  <this folder>/common.css, option-a.css, option-b.css, option-c.css, warn-orange.css
Output: <this folder>/index.html (one self-contained page; fonts come from Google Fonts)

Each theme is written as a class (.t-orig, .t-a, ...) holding the custom properties, so the same element can
sit in several cells with different values. The build stops if a beige theme leaves an upstream colour token
undefined, so no cell silently falls back to an upstream colour.
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
UP = REPO / 'lcan-design' / 'upstream' / 'lucian-uxui-prompt'
COMMIT = '7e339fa'

ELEMENTS = [  # id, upstream file, title, natural height (px), what to look at, colours written into the element
    ('023', '023-settings-switch-list.html', '펼쳐지는 알림 설정', 420,
     '위쪽의 ‘2개 켜짐’ 배지(강조 바탕), 켜진 스위치(완료색), 주기 고르기의 흰 칸(그림자)을 보시면 됩니다. ‘모두 끄기’에 마우스를 올리면 글자가 위험색으로 바뀝니다.',
     '왼쪽 아이콘 칸 세 개의 그라디언트와 스위치 손잡이의 흰색은 요소 코드에 적혀 있어서, 네 칸에서 모두 같습니다.'),
    ('042', '042-wizard-stepper.html', '단계 진행 마법사', 400,
     '현재 단계 동그라미(강조 테두리와 옅은 강조 번짐), 지난 단계 동그라미(강조색 채움), 진행선을 보시면 됩니다. 마지막 단계에서는 큰 체크와 ‘시작하기’ 단추가 완료색으로 바뀝니다.',
     '셋째 단계에 있는 프로필 동그라미 두 개의 색은 요소 코드에 적혀 있습니다.'),
    ('072', '072-inline-alert-dismiss.html', '접히는 인라인 알림', 470,
     '네 알림 줄의 색(위로부터 위험, 경고, 강조, 완료)과 첫 줄의 ‘자세히’ 글자(위험색)를 보시면 됩니다. 카드 둘레의 그림자도 안마다 다릅니다.',
     '직접 적은 색은 없습니다. 다만 ‘자세히’를 펼치면 나오는 기록의 글꼴은 요소 코드에 시스템 고정폭 글꼴로 적혀 있습니다.'),
]

THEMES = {  # class: (label, sub-label, stack of theme files)
    't-orig': ('원본', 'Lucian 기본값', None),
    't-a': ('안 A', '먹 강조, 평면', ['artifact-design/lcan-theme.css', 'common.css', 'option-a.css']),
    't-b': ('안 B', '먹 강조, 그림자', ['artifact-design/lcan-theme.css', 'common.css', 'option-b.css']),
    't-c': ('안 C', '보라 강조, 평면', ['artifact-design/lcan-theme.css', 'common.css', 'option-c.css']),
    't-wg': ('금색 경고', '#866500 · 바탕은 안 A', ['artifact-design/lcan-theme.css', 'common.css', 'option-a.css']),
    't-wo': ('주황 경고', '#A05616 · 바탕은 안 A', ['artifact-design/lcan-theme.css', 'common.css', 'option-a.css', 'warn-orange.css']),
}


# ---------- CSS custom properties ----------
def root_props(text, first_only=True):
    text = re.sub(r'/\*[\s\S]*?\*/', '', text)
    blocks = re.findall(r'(?<![\w-]):root\s*\{([^}]*)\}', text)
    props = {}
    for block in blocks[:1] if first_only else blocks:
        for decl in block.split(';'):
            m = re.match(r'\s*(--[\w-]+|color-scheme)\s*:\s*(.+?)\s*$', decl, re.S)
            if m:
                props[m.group(1)] = re.sub(r'\s+', ' ', m.group(2))
    return props


def read(rel):
    p = REPO / rel if '/' in rel else HERE / rel
    return p.read_text(encoding='utf8')


upstream = root_props((UP / 'tokens.css').read_text(encoding='utf8'))
UX_COLOUR_TOKENS = [k for k in upstream if k.startswith('--ux-') and k not in ('--ux-ease', '--ux-spring')]

# base.css must carry the upstream light values unchanged
base_props = root_props((REPO / 'lcan-design' / 'base.css').read_text(encoding='utf8'))
for k, v in upstream.items():
    assert base_props.get(k, '').replace(' ', '') == v.replace(' ', ''), f'base.css differs from upstream for {k}'

theme_props = {}
for cls, (_, _, stack) in THEMES.items():
    if stack is None:
        props = {k: v for k, v in upstream.items()}
    else:
        props = {}
        for rel in stack:
            props.update(root_props(read(rel)))
        missing = [k for k in UX_COLOUR_TOKENS if k not in props]
        assert not missing, f'{cls} leaves {missing} undefined'
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
    """Text contrast at the places in the three elements where an open token is used as text."""
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


def surfaces(props, name):
    c = tok(props, name)
    return [ratio(c, tok(props, s)) for s in ('--ux-page', '--ux-surface', '--ux-surface-2')]


# ---------- elements ----------
def split_element(src):
    m = re.search(r'<script>([\s\S]*?)</script>\s*$', src)
    return src[:m.start()].rstrip() + '\n', m.group(1)


def demo_steps(el_id):
    # The upstream @demo lines live in src/elements, which this folder does not copy; the steps are restated here
    # (taps and waits only) from commit 7e339fa.
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
for el_id, fname, title, height, look, fixed in ELEMENTS:
    raw = (UP / fname).read_text(encoding='utf8')
    assert raw.startswith(f'<!-- Lucian UX/UI Prompt #{el_id} · MIT License'), f'{fname}: license line missing'
    head, js = split_element(raw)
    sources[el_id] = {'html': head, 'js': js, 'steps': demo_steps(el_id)}
    snippets[el_id] = raw


# ---------- page parts ----------
E = html.escape


def chip(swatch, name, value):
    return (f'<span class="chip"><i class="sw" style="background:{swatch}" aria-hidden="true"></i>'
            f'<code>{E(name)}</code><span class="v">{E(value)}</span></span>')


def cell(cls, el_id, height):
    label, sub, _ = THEMES[cls]
    return (f'<figure class="cell {cls}">'
            f'<figcaption><b>{E(label)}</b><span>{E(sub)}</span></figcaption>'
            f'<div class="stage" data-el="{el_id}" style="--h:{height}px" role="group" aria-label="{E(label)}: {el_id}">'
            f'<div class="fit">\n{snippets[el_id]}</div></div></figure>')


def row(el_id, fname, title, height, look, fixed, classes, heading='h3'):
    cells = ''.join(cell(c, el_id, height) for c in classes)
    return (f'<article class="row" data-row="{el_id}">'
            f'<div class="row-head"><div class="row-title"><{heading}><span class="num">{el_id}</span>{E(title)}</{heading}>'
            f'<p class="look">{E(look)}</p><p class="fixed">{E(fixed)}</p></div>'
            f'<div class="row-ctl"><button type="button" class="btn btn-ink" data-play="{el_id}">같은 동작 보기</button>'
            f'<button type="button" class="btn" data-reset="{el_id}">처음 상태로</button></div></div>'
            f'<div class="cells cells-{len(classes)}">{cells}</div></article>')


OPTIONS = [
    ('t-a', 'A', '먹 강조, 평면',
     [('--ux-accent', '#1A1916'), ('--ux-accent-soft', '먹 7%'), ('--ux-shadow-strong', '없음')],
     ['베이지 시안과 말투가 같습니다. 시안처럼 강한 표시는 먹색으로 칠하고, 카드는 그림자 없이 선으로 나눕니다.',
      '강조색과 진행선은 시안의 먹색을 그대로 썼고, 그림자는 시안처럼 쓰지 않았습니다. 옅은 강조 바탕(먹 7%)만 새로 정한 값입니다.'],
     ['강조색이 본문 글자색과 같아서, 042의 현재 단계처럼 강조색으로 상태를 알리는 곳이 덜 눈에 띕니다.',
      '023의 주기 고르기에서 선택된 흰 칸처럼 떠 보여야 할 조각이, 바탕과 선으로만 구분됩니다.',
      '072의 ‘새 버전’ 알림처럼 강조색으로 칠하는 알림은 회색이 됩니다.']),
    ('t-b', 'B', '먹 강조, 그림자',
     [('--ux-accent', '#1A1916'), ('--ux-shadow-strong', '먹 30%'), ('--ux-shadow', '먹 14%')],
     ['원본 요소가 전제한 깊이를 살립니다. 카드와 떠 있는 조각이 바탕에서 분명하게 떨어져 보입니다.',
      '그림자의 진하기는 원본 값 그대로이고, 그림자 색만 원본의 보라 계열에서 먹색으로 바꿨습니다.'],
     ['베이지 시안에는 그림자를 쓴 곳이 없어서, 시안 화면에 함께 놓으면 이 요소들만 떠 보일 수 있습니다.']),
    ('t-c', 'C', '보라 강조, 평면',
     [('--ux-accent', '#4A3AA7'), ('--ux-accent-soft', '보라 12%'), ('--ux-shadow-strong', '없음')],
     ['선택, 현재 단계, 초점 표시가 본문과 다른 색이어서 바로 구분됩니다.',
      '보라 #4A3AA7은 베이지 시안의 차트 선에 있던 색이고, 오름(빨강), 내림(파랑), 근접(노랑), 완료(초록)와 겹치지 않습니다. 옅은 강조 바탕은 원본처럼 강조색의 12%입니다.'],
     ['베이지 스타일에 브랜드 색이 하나 늘어납니다.',
      '차트에 보라 선을 쓰는 화면에서는 강조색과 차트 선이 같은 색이 됩니다.']),
]


def option_card(cls, letter, name, chips, pros, cons):
    p = theme_props[cls]
    chip_html = ''.join(chip(p[t] if v not in ('없음',) else 'transparent', t, v) for t, v in chips)
    li = lambda xs: ''.join(f'<li>{E(x)}</li>' for x in xs)
    return (f'<section class="opt {cls}" aria-labelledby="opt-{letter}">'
            f'<div class="opt-head"><span class="tag">안 {letter}</span><h3 id="opt-{letter}">{E(name)}</h3></div>'
            f'<div class="opt-spec"><div class="chips">{chip_html}</div>'
            f'<div class="depth" aria-hidden="true"><span></span></div></div>'
            f'<dl class="pc"><dt>좋은 점</dt><dd><ul>{li(pros)}</ul></dd><dt>아쉬운 점</dt><dd><ul>{li(cons)}</ul></dd></dl>'
            f'</section>')


def fmt(x):
    return f'{x:.2f}'


def ratio_cell(x):
    flag = '' if x >= 4.5 else '<span class="miss">기준 미달</span>'
    return f'<td class="n">{fmt(x)}{flag}</td>'


# contrast table: where an open token is used as text
check_cols = ['t-orig', 't-a', 't-b', 't-c']
check_html = []
for items in zip(*[checks(theme_props[c]) for c in check_cols]):
    label = items[0][0]
    check_html.append(f'<tr><th scope="row">{E(label)}</th>' + ''.join(ratio_cell(v) for _, v in items) + '</tr>')

# shared values table
A = theme_props['t-a']
shared = [
    ('--ux-surface-3', A['--ux-surface-3'], '시안(지표 트리)의 막대 바탕입니다.', None),
    ('--ux-mint', A['--ux-mint'], '시안(대화형 분석)의 차트 초록 #138A62를 글자로도 쓸 수 있게 어둡게 했습니다.', '--ux-mint'),
    ('--ux-warn', A['--ux-warn'], '시안의 근접 막대 #9A7400을 같은 방법으로 어둡게 했습니다. 결정 2에 따라 바뀝니다.', '--ux-warn'),
    ('--ux-danger', A['--ux-danger'], '오름 빨강 #B8322A를 조금 어둡게 했습니다. #B8322A 그대로면 023의 ‘모두 끄기’에 올렸을 때 글자 명암비가 4.30:1입니다.', '--ux-danger'),
    ('--ux-accent-2', A['--ux-accent-2'], '보조 글자색과 같습니다. 원본 요소 400개 가운데 6개가 쓰고, 이번 세 요소는 쓰지 않습니다.', '--ux-accent-2'),
    ('--ux-glass, --ux-glass-line', 'rgba(255,253,248,.62), .88', '카드 색을 반투명하게 했습니다. 원본 요소 가운데 쓰는 요소가 없습니다.', None),
]
shared_html = []
for name, value, why, t in shared:
    sw = value if value.startswith('#') else 'rgba(255,253,248,.62)'
    nums = f'<td class="n">{" / ".join(fmt(x) for x in surfaces(A, t))}</td>' if t else '<td class="na">글자에 쓰지 않습니다</td>'
    shared_html.append(f'<tr><th scope="row"><code>{E(name)}</code></th><td class="val"><i class="sw" style="background:{sw}" aria-hidden="true"></i><code>{E(value)}</code></td>'
                       f'<td>{E(why)}</td>{nums}</tr>')

# warning colour notes
W = {cls: theme_props[cls]['--ux-warn'] for cls in ('t-wg', 't-wo')}
warn_ratios = {cls: ' / '.join(fmt(x) for x in surfaces(theme_props[cls], '--ux-warn')) for cls in W}

CHROME_CSS = r'''
/* Layout: a specimen sheet. The two decisions sit at the top; each element then gets one row that sets the
   original look and the options side by side; the shared values and the limits close the page.
   The page uses the artifact-design beige style, which has no dark values yet, so it commits to one light look. */
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
.decide { display: grid; gap: 12px; margin: 8px 0 0; }
@media (min-width: 760px) { .decide { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.decide > div { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px; display: grid; gap: 4px; min-width: 0; }
.decide dt { font-weight: 700; font-size: 15px; }
.decide dt mark { background: linear-gradient(transparent 58%, var(--hl) 58%); color: inherit; padding: 0 2px; }
.decide dd { margin: 0; color: var(--ink-2); }
.meta { margin: 0; font-size: 12.5px; color: var(--ink-3); }
section.part { margin-top: 56px; }
.part > h2 { margin: 0 0 6px; font-size: 20px; font-weight: 700; letter-spacing: -.01em; }
.intro { margin: 0; max-width: 72ch; color: var(--ink-2); }
.opts { display: grid; gap: 12px; margin-top: 18px; }
@media (min-width: 980px) { .opts { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
.opt { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 16px; display: grid; gap: 12px; align-content: start; min-width: 0; }
.opt-head { display: flex; align-items: center; gap: 10px; }
.opt-head h3 { margin: 0; font-size: 16px; font-weight: 700; }
.tag { display: inline-flex; align-items: center; height: 24px; padding: 0 10px; border-radius: 999px; background: var(--ink); color: var(--card); font-size: 12px; font-weight: 700; white-space: nowrap; }
.opt-spec { display: flex; gap: 12px; align-items: center; justify-content: space-between; }
.chips { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.chip { display: flex; align-items: center; gap: 8px; font-size: 12.5px; min-width: 0; }
.chip code { color: var(--ink-2); }
.chip .v { font-family: var(--mono); font-size: 12px; color: var(--ink); white-space: nowrap; }
.sw { flex: none; width: 14px; height: 14px; border-radius: 3px; box-shadow: inset 0 0 0 1px rgba(26,25,22,.18); }
.depth { flex: none; width: 92px; height: 64px; border-radius: 10px; background: var(--ux-page); display: grid; place-items: center; }
.depth span { width: 56px; height: 34px; border-radius: 8px; background: var(--ux-surface); box-shadow: 0 0 0 1px var(--ux-line), 0 14px 26px -14px var(--ux-shadow-strong); }
.pc { margin: 0; display: grid; gap: 4px; }
.pc dt { font-size: 12.5px; font-weight: 700; color: var(--ink-2); }
.pc dd { margin: 0 0 6px; }
.pc ul { margin: 0; padding-left: 1.1em; display: grid; gap: 3px; }
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
.btn:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.btn[disabled] { opacity: .55; cursor: default; }
.cells { display: grid; gap: 12px; margin-top: 16px; }
@media (min-width: 640px) { .cells { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1180px) { .cells-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); } }
.cells-2 { max-width: 960px; }
.cell { margin: 0; min-width: 0; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; background: var(--ux-page); }
.cell figcaption { display: flex; align-items: baseline; justify-content: space-between; gap: 8px; padding: 9px 12px; background: var(--card); border-bottom: 1px solid var(--line); font-size: 12.5px; }
.cell figcaption b { font-size: 13.5px; }
.cell figcaption span { color: var(--ink-3); text-align: right; }
.stage { position: relative; overflow: hidden; height: calc(var(--h) + 52px); }
/* inherited text settings as in the upstream gallery, so the elements see the same defaults */
.fit { position: absolute; left: 50%; top: 50%; width: max-content; transform: translate(-50%, -50%); transform-origin: 50% 50%;
  font-size: 16px; font-weight: 400; line-height: normal; letter-spacing: -.01em; text-align: left; white-space: normal; word-break: normal; overflow-wrap: normal; color: var(--ux-ink); }
.warn-notes { display: grid; gap: 12px; margin-top: 16px; max-width: 960px; }
@media (min-width: 640px) { .warn-notes { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.warn-notes .opt { gap: 8px; }
.ratio { margin: 0; font-size: 12.5px; color: var(--ink-2); }
.tbl { margin-top: 16px; overflow-x: auto; border: 1px solid var(--line); border-radius: 12px; background: var(--card); }
.tbl table { width: 100%; border-collapse: collapse; min-width: 640px; }
.tbl th, .tbl td { padding: 10px 12px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; font-size: 13px; }
.tbl tr:last-child > * { border-bottom: 0; }
.tbl thead th { font-size: 12.5px; color: var(--ink-2); font-weight: 700; background: var(--sub); }
.tbl th[scope="row"] { font-weight: 600; }
.tbl th code { white-space: nowrap; }
.tbl .na { color: var(--ink-3); white-space: nowrap; }
.scroll-hint { display: none; margin: 8px 0 0; font-size: 12.5px; color: var(--ink-3); }
@media (max-width: 700px) { .scroll-hint { display: block; } }
.tbl .n { font-family: var(--mono); font-size: 12.5px; white-space: nowrap; font-variant-numeric: tabular-nums; }
.tbl .val { white-space: nowrap; }
.tbl .val .sw { display: inline-block; vertical-align: -2px; margin-right: 6px; }
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
})();
'''


def scoped_theme_css():
    out = []
    for cls, props in theme_props.items():
        body = ';'.join(f'{k}:{v}' for k, v in props.items())
        out.append(f'.{cls}{{{body}}}')
    return '\n'.join(out)


base_css = (REPO / 'lcan-design' / 'base.css').read_text(encoding='utf8')
el_rows = ''.join(row(e[0], e[1], e[2], e[3], e[4], e[5], ['t-orig', 't-a', 't-b', 't-c']) for e in ELEMENTS)
e072 = [e for e in ELEMENTS if e[0] == '072'][0]
warn_row = row('072', e072[1], e072[2], e072[3],
               '둘째 줄(저장 공간 72% 사용 중)의 아이콘, 왼쪽 막대, 진행 막대가 경고색입니다. 바로 위 줄의 위험색과 얼마나 구분되는지 보시면 됩니다.',
               '두 칸의 바탕은 모두 안 A이고, 경고색만 다릅니다.', ['t-wg', 't-wo'])
src_json = json.dumps(sources, ensure_ascii=False).replace('</', '<\\/')

page = f'''<title>베이지 토큰 3안</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans+KR:wght@400;500;600;700&family=Noto+Serif+KR:wght@700&display=swap">
<!-- Built by lcan-design/drafts/beige-token-options/build.py from upstream commit {COMMIT}. Do not edit by hand. -->
<style>{CHROME_CSS}</style>
<style>
/* lcan-design/base.css */
{base_css}
/* themes, one class per cell */
{scoped_theme_css()}
</style>
<div class="wrap">
<header class="top">
  <p class="kicker">lcan-design 첫 실험 · 2026년 10월 29일</p>
  <h1>베이지 테마의 남은 값</h1>
  <p class="lead">Lucian UX/UI Prompt의 요소 세 개에 artifact-design의 베이지 스타일을 적용했습니다. 요소 코드는 원본 그대로 두고, 토큰 값과 글꼴만 바꿨습니다. 아래 두 가지를 골라 주시면, 고르신 값으로 베이지 테마 파일을 완성하겠습니다.</p>
  <dl class="decide">
    <div><dt><mark>결정 1</mark> 강조와 깊이</dt><dd>안 A, B, C 가운데 하나를 고릅니다. B는 A에 그림자를 더한 안이고, C는 A의 강조색을 보라로 바꾼 안이므로, C의 강조에 B의 그림자를 더하는 식으로 섞어서 고르셔도 됩니다.</dd></div>
    <div><dt><mark>결정 2</mark> 경고색</dt><dd>금색과 주황 가운데 하나를 고릅니다. 두 색 모두 바탕과 카드와 보조 면 위에서 글자 명암비가 4.5:1 이상입니다.</dd></div>
  </dl>
  <p class="meta">원본은 Lucian UX/UI Prompt 커밋 <span class="mono">{COMMIT}</span>입니다. 베이지 스타일에는 아직 다크 값이 없어서, 이 화면은 라이트로만 보입니다.</p>
</header>

<section class="part" aria-labelledby="d1">
  <h2 id="d1">결정 1. 강조와 깊이</h2>
  <p class="intro">세 안은 안 A를 기준으로 한 가지씩만 다릅니다. 칸 안의 요소를 직접 눌러 볼 수 있고, ‘같은 동작 보기’를 누르면 네 칸이 같은 순서로 움직입니다.</p>
  <div class="opts">{''.join(option_card(*o) for o in OPTIONS)}</div>
  {el_rows}
</section>

<section class="part" aria-labelledby="d2">
  <h2 id="d2">결정 2. 경고색</h2>
  <p class="intro">경고색은 이번 세 요소 가운데 072에서만 쓰입니다. 경고와 위험이 나란히 놓이는 화면이어서, 두 색이 얼마나 구분되는지 보기에 좋습니다.</p>
  <div class="warn-notes">
    <section class="opt t-wg" aria-labelledby="w1"><div class="opt-head"><span class="tag">금색</span><h3 id="w1"><span class="mono">{W['t-wg']}</span></h3></div>
      <p class="ratio">글자 명암비(바탕 / 카드 / 보조 면) {warn_ratios['t-wg']}</p>
      <dl class="pc"><dt>좋은 점</dt><dd><ul><li>베이지 시안에서 ‘근접’을 노랑과 금색(#9A7400)으로 그린 방식과 이어집니다.</li><li>위험색(빨강)과 색상 차이가 커서, 두 알림이 나란히 있어도 잘 구분됩니다.</li></ul></dd>
      <dt>아쉬운 점</dt><dd><ul><li>글자로 쓸 수 있게 어둡게 하면서 올리브빛 갈색이 되었습니다. 흔히 보는 경고 주황과 달라서, 경고라는 뜻이 바로 읽히지 않을 수 있습니다.</li></ul></dd></dl></section>
    <section class="opt t-wo" aria-labelledby="w2"><div class="opt-head"><span class="tag">주황</span><h3 id="w2"><span class="mono">{W['t-wo']}</span></h3></div>
      <p class="ratio">글자 명암비(바탕 / 카드 / 보조 면) {warn_ratios['t-wo']}</p>
      <dl class="pc"><dt>좋은 점</dt><dd><ul><li>흔히 쓰는 경고색이어서 뜻이 바로 읽힙니다.</li><li>원본 요소의 경고색 #D6731E와 색상이 같고, 명도만 낮췄습니다.</li></ul></dd>
      <dt>아쉬운 점</dt><dd><ul><li>위험색 빨강과 색상이 가까워서, 두 알림이 나란히 있으면 금색보다 덜 구분됩니다.</li><li>베이지 시안의 ‘근접’ 표현(노랑)과는 다른 계열입니다.</li></ul></dd></dl></section>
  </div>
  {warn_row}
</section>

<section class="part" aria-labelledby="d3">
  <h2 id="d3">글자 명암비 점검</h2>
  <p class="intro">요소 안에서 이번에 정하는 토큰이 글자색으로 쓰이는 곳의 명암비입니다. 기준은 디자인 원칙 3의 4.5:1입니다.</p>
  <div class="tbl"><table>
    <thead><tr><th scope="col">위치</th><th scope="col">원본</th><th scope="col">안 A</th><th scope="col">안 B</th><th scope="col">안 C</th></tr></thead>
    <tbody>{''.join(check_html)}</tbody>
  </table></div>
  <p class="scroll-hint">표를 옆으로 밀면 나머지 열이 보입니다.</p>
  <p class="note">원본 칸은 Lucian 기본값(라이트)으로 계산했습니다. 그림자는 글자 명암비에 영향을 주지 않아서 안 A와 안 B의 값이 같습니다.</p>
</section>

<section class="part" aria-labelledby="d4">
  <h2 id="d4">세 안에 공통인 값</h2>
  <p class="intro">아래 값은 세 안에서 같습니다. 베이지 시안에 있던 값을 그대로 쓰거나, 시안의 색을 글자로도 쓸 수 있게 어둡게 했습니다. 바탕, 카드, 보조 면, 선, 글자색 세 단계, 단추 글자색, 오름과 내림의 색, 글꼴은 artifact-design/HANDOFF.md 2절의 값 그대로입니다.</p>
  <div class="tbl"><table>
    <thead><tr><th scope="col">토큰</th><th scope="col">값</th><th scope="col">근거</th><th scope="col">글자 명암비(바탕 / 카드 / 보조 면)</th></tr></thead>
    <tbody>{''.join(shared_html)}</tbody>
  </table></div>
  <p class="scroll-hint">표를 옆으로 밀면 나머지 열이 보입니다.</p>
</section>

<section class="part" aria-labelledby="d5">
  <h2 id="d5">이번 비교로 알 수 없는 것</h2>
  <ul class="limits">
    <li><b>모서리와 굵기</b>세 요소의 카드 모서리(28~30px)와 제목 굵기(760~850)는 요소 코드에 적혀 있어서 토큰으로 바뀌지 않습니다. 베이지 시안의 카드 모서리는 10~14px이고, 굵기는 대부분 600과 700입니다. 다만 IBM Plex Sans KR에는 700까지만 있어서, 700보다 굵게 적은 글자는 화면에서 700으로 보입니다.</li>
    <li><b>요소에 직접 적은 색</b>원본 요소 400개 가운데 242개는 흰색과 검은색이 아닌 색을 요소 코드에 직접 적어 두었습니다. 그런 요소는 토큰만 바꿔서는 베이지 스타일에 맞출 수 없습니다. 이번 세 요소는 그런 색이 적은 요소로 골랐습니다.</li>
    <li><b>오르내림 색</b>세 요소는 오르내림을 표시하지 않습니다. 원본은 내림을 위험색으로 칠하므로, 오르내림을 쓰는 요소는 요소 코드를 따로 고쳐야 합니다.</li>
    <li><b>다크 화면</b>베이지 스타일에 다크 값이 없어서 라이트 화면만 비교했습니다.</li>
    <li><b>원본 칸의 글꼴</b>원본 갤러리처럼 웹 글꼴을 불러오지 않았습니다. 기기에 Pretendard가 없으면 원본 칸은 기기의 기본 한글 글꼴로 보입니다.</li>
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
for cls in check_cols:
    print(cls, ' '.join(f'{fmt(v)}' for _, v in checks(theme_props[cls])))
