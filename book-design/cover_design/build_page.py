"""Build the candidate library page (final.html) and a local preview (preview.html) from the saved source."""
import re, json

SRC = '/home/claude/cover_design/page/src.html'
src = open(SRC, encoding='utf-8').read()
lines = src.split('\n')
mzcss = open('/home/claude/cover_design/mz.css', encoding='utf-8').read().rstrip('\n')
mzjs = open('/home/claude/cover_design/mz.js', encoding='utf-8').read().rstrip('\n')

def find_line(prefix, start=0):
    for i in range(start, len(lines)):
        if lines[i].startswith(prefix):
            return i
    raise SystemExit('not found: ' + prefix)

# 1. CSS: book covers block -> magazine covers block
c0 = find_line('/* ---------- book covers: one per daily brief ---------- */')
c1 = find_line('.t-ht .c-ft .c-imp{font-size:2.3cqw}', c0)
# 2. JS: BK module
j0 = find_line('  /* ---------- book covers ---------- */')
j1 = find_line('  return {html:html,pick:pick,grain:grain};', j0)
assert lines[j1 + 1] == '  })();', lines[j1 + 1]
new_lines = lines[:c0] + mzcss.split('\n') + lines[c1 + 1:j0] + ['  /* ---------- magazine covers ---------- */'] + mzjs.split('\n') + lines[j1 + 2:]
page = '\n'.join(new_lines)

def rep(old, new, count=1):
    global page
    n = page.count(old)
    assert n == count, (old, n)
    page = page.replace(old, new)

# fonts: add the weights the covers use, drop faces only the old book covers used
rep('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Gothic+A1:wght@400;500;700;800&family=Do+Hyeon&family=IBM+Plex+Mono:wght@400;500&display=swap">',
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Gothic+A1:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">')

# placeholder restyle: the next-issue slot uses the page's sans display face instead of the old serif
rep(".cover.c4 .ct{margin-top:16px; font-family:'Noto Serif KR','Noto Serif CJK KR','AppleMyungjo','Batang',serif; font-weight:600; font-size:30px; line-height:1.18; color:var(--ink-2)}",
    ".cover.c4 .ct{margin-top:16px; font-family:var(--display); font-weight:700; font-size:30px; line-height:1.18; letter-spacing:-.02em; color:var(--ink-2)}")
rep(".cover.c4{aspect-ratio:68/100; display:flex; flex-direction:column; padding:22px 20px 18px; border:2px dashed var(--line-2); border-radius:4px; background:rgba(255,255,255,.4); color:var(--muted)}",
    ".cover.c4{aspect-ratio:68/100; display:flex; flex-direction:column; padding:22px 20px 18px; border:2px dashed var(--lime); border-radius:2px; background:rgba(255,255,255,.4); color:var(--muted)}")
rep('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;400;600&family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Cormorant+Garamond:ital,wght@0,500;1,400;1,500&family=Oswald:wght@500;700&display=swap">',
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&display=swap">')

# wording: one brief = one issue of a magazine
rep('<p>브리핑 한 편을 한 권으로 보고 표지를 그린다. 그림은 그날 브리핑이 기록한 BTC·알트·스테이블 점유율과 BTC.D 흐름에서 나오고, 바탕색은 판정 국면을 따른다.</p>',
    '<p>브리핑 한 편을 잡지 한 호로 보고 표지를 그린다. 테두리 자리, 제호, 커버라인, 하단 띠는 매일 같고, 색은 배색 12종과 날짜마다 도는 기준 색상으로 호마다 바뀐다. 그림은 헤드라인이 다룬 주제와 낱말에 맞춰 44종 가운데 하나를 고르되, 최근 12호에 나온 그림은 다시 쓰지 않는다. 계단의 높이나 수조의 수위 같은 형태는 그날 기록된 수치에서 나온다.</p>')
rep("cov.appendChild(el('div','k','다음 권 · 제'+(B.length+1)+'권'));", "cov.appendChild(el('div','k','다음 호 · 제'+(B.length+1)+'호'));")
rep("sum.appendChild(el('small',null,groups[k].length+'권'));", "sum.appendChild(el('small',null,groups[k].length+'장'));")
rep("var msg=(nr&&nc)?nr+'건과 표지 '+nc+'권이 남았습니다. ':nr?nr+'건이 남았습니다. ':nc?'표지 '+nc+'권이 남았습니다. ':'일치하는 항목이 없습니다. ';",
    "var msg=(nr&&nc)?nr+'건과 표지 '+nc+'장이 남았습니다. ':nr?nr+'건이 남았습니다. ':nc?'표지 '+nc+'장이 남았습니다. ':'일치하는 항목이 없습니다. ';")
rep("box.appendChild(el('p','empty-note',S.status==='ready'?'아직 표지가 없습니다. 첫 브리핑이 등록되면 이 자리에 첫 권의 표지가 나타납니다.'",
    "box.appendChild(el('p','empty-note',S.status==='ready'?'아직 표지가 없습니다. 첫 브리핑이 등록되면 이 자리에 첫 호의 표지가 나타납니다.'")
rep("cov.appendChild(el('div','ct',S.status==='ready'?'첫 권 자리':'기록 없음'));", "cov.appendChild(el('div','ct',S.status==='ready'?'첫 호 자리':'기록 없음'));")

# headline fitting: after covers are in the page, when a month is opened, after search, after fonts load
rep("      var det=el('details','bm'); if(gi===0) det.open=true;",
    "      var det=el('details','bm'); if(gi===0) det.open=true;\n      det.addEventListener('toggle',function(){ if(det.open) BK.fit(det); });")
rep("    renderStatus(); renderVols(); renderBooks(); renderTimeline(); renderList(); renderCharts(); renderTable(); renderTiles(); renderReg();",
    "    renderStatus(); renderVols(); renderBooks(); renderTimeline(); renderList(); renderCharts(); renderTable(); renderTiles(); renderReg();\n    BK.fit(document);")
rep("  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}",
    "  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(function(){BK.fit(document,true); fit();});}")
rep("      hint.appendChild(b);\n    }\n    fit();", "      hint.appendChild(b);\n    }\n    BK.fit(document);\n    fit();")

open('/home/claude/cover_design/page/final.html', 'w', encoding='utf-8').write(page)

# ---- local preview: local fonts, local data, fixed clock ----
prev = page
prev = prev.replace('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Gothic+A1:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">',
    ''.join('<link rel="stylesheet" href="../node_modules/@fontsource/%s.css">' % f for f in
            ['outfit/400', 'outfit/500', 'outfit/600', 'outfit/700', 'gothic-a1/400', 'gothic-a1/500', 'gothic-a1/600', 'gothic-a1/700', 'gothic-a1/800', 'ibm-plex-mono/400', 'ibm-plex-mono/500']))
prev = prev.replace('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&display=swap">',
    ''.join('<link rel="stylesheet" href="../node_modules/@fontsource/%s.css">' % f for f in ['oswald/500', 'oswald/600']))
d0 = prev.index('  /* ---------- data ---------- */')
d1 = prev.index('})();\n</script>', d0)
prev = prev[:d0] + "  S.status='ready'; S.briefs=normalize(window.RAW); renderAll(); document.fonts.ready.then(function(){setTimeout(function(){document.body.setAttribute('data-ready','1');},200);});\n" + prev[d1:]
prev = prev.replace('<script>\n(function(){', '<script src="../data.js"></script>\n<script>\nDate.now=function(){return Date.UTC(2026,8,30,12,15);};\n(function(){', 1)
open('/home/claude/cover_design/page/preview.html', 'w', encoding='utf-8').write(prev)
print('final', len(page), 'preview', len(prev))
