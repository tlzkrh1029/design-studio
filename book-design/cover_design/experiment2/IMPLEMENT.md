# 구현 안내 (지시 → 페이지)

받은 지시를 따라 서고 페이지 한 장을 만든다. 지시가 무엇이고 어디까지 스스로 정해도 되는지는 작업을 맡길 때 따로 알려 준다. 지시가 모호하면 가장 단순하게 읽은 뒤 마지막 보고에 적는다.

## 파일
- 만들 파일: `/home/claude/cover_design/experiment2/<이름>.src.html` (이름 예: night_md)
- 빌드: `cd /home/claude/cover_design/experiment2 && python3 build.py <이름>` → `<이름>.html`
- 렌더링: `python3 shot.py <이름> /home/claude/cover_design/experiment2/tmp/<이름>/out.png` → 페이지 크기, 헤드라인이 넘친 표지 번호, 오류를 출력한다.
- 임시 파일(잘라 낸 이미지, 시험용 스크립트 등)은 `/home/claude/cover_design/experiment2/tmp/<이름>/` 안에만 둔다. `/tmp`나 다른 사람의 tmp 폴더는 쓰지도 열지도 않는다.
- 공용 파일(`../mz.js`, `../mz.css`, `../themes/common.js`, `../data.js`, `build.py`, `shot.py`)과 다른 사람의 파일은 고치지 않는다. 필요한 도우미는 자기 페이지 안에 정의한다.

## 페이지 골격 (그대로 시작)
```html
<!doctype html><html lang="ko"><head><meta charset="utf-8">
<title>…</title>
<!-- 쓰는 글꼴만 링크한다. 경로 예: ../node_modules/@fontsource/gothic-a1/800.css -->
<link rel="stylesheet" href="../mz.css">
<style> /* 지시의 토큰(또는 스스로 정한 값)을 :root CSS 변수로 옮기고, 그 변수로 스타일을 짠다 */ </style>
</head><body>
<div id="app"></div>
<script src="../data.js"></script>
<script>
(function(){
<<MZ>>
<<COMMON>>
/* 여기서 HTML 문자열을 만들어 document.getElementById('app').innerHTML에 넣는다 */
ready();   /* 반드시 마지막에 한 번. 글꼴이 오면 표지 제목을 맞추고 body[data-ready]를 붙인다 */
})();
</script></body></html>
```

## 글꼴 파일 (../node_modules/@fontsource/ 아래)
- gothic-a1/100~900.css, outfit/100~900.css, oswald/200~700.css, ibm-plex-mono/100~700.css (+ -italic), noto-serif-kr/200~900.css, bodoni-moda/400~900.css 와 400-italic~900-italic.css
- CSS에서 이름은 'Gothic A1', 'Outfit', 'Oswald', 'IBM Plex Mono', 'Noto Serif KR', 'Bodoni Moda'.

## 공용 도우미 (<<COMMON>>이 넣어 준다)
- `B`: 호 31개, 날짜·회차 오름차순. 각 호 필드: id, date("2026-09-30"), seq, title, url, phase, prevPhase, provisional, headline, btcd, stableD, stable1m, btc1m, run, window, note.
- `L`: 최신 호(제31호, 9/30). 오늘은 2026-09-30으로 본다(최신 호 = 오늘 호).
- `vol(b)`: 호 번호(31 등). `wd(date)`: 요일 한 글자. `mdot(date)`: "09.30". `parts(phase)`: ["C","D"]. `lastPh(b)`.
- `esc(s)`: HTML 이스케이프. `f(v,d)`: 소수 d자리 문자열(없으면 "–"). `sg(v,d)`: 부호 붙인 문자열(0이면 "±0.00" 꼴이므로 "전날과 같음" 같은 규칙은 직접 처리). 음수 부호는 U+2212.
- `cover(b)`: 그 호의 잡지 표지 HTML. 표지는 부모 폭을 꽉 채우므로, 원하는 폭을 가진 div로 감싼다: `'<div style="width:143px">'+cover(b)+'</div>'`. 높이는 폭 ÷ 0.68로 저절로 정해진다. 표지 안쪽(.mz와 그 자식)은 고치지 않는다. 감싼 div에 그림자, 받침, 링크는 괜찮다.
- `prevOf(b)`: 바로 앞 btcd 기록 호. `deltas(b)`: {dB: BTC.D 전날 대비, dS: ΣSTABLECOIN.D 전날 대비}.
- `pal(b)`: 그 호 표지의 배색. `pal(L).fr`가 최신 호 테두리색(9/30은 복숭아색). `BK.contrast(a,b)`: 두 hex의 명암비.
- `daily(key)`: 하루 한 값(그날 마지막 회차) [{d:"2026-09-03", v:60.11}, …], 값이 있는 날만. 날짜 빈틈(9/18·19)은 직접 확인해 선을 끊는다.
- `dayMap()`: {"2026-09-03":[호,호,호], …}. `stats()`: {n:31, days:26}.
- `runLabel(b)`: "06:10 본실행" / "안전판" / "지연 실행 10:57". `phaseText(p)`, `chipsOf(b)`.
- `PHN` 국면 이름, `PCOL` 국면 색, `PINK` 국면 면 위 글자색, `WD` 요일.
- `spark(points,w,h,stroke,opts)`: 아주 단순한 추세선 SVG. 축·기준선 있는 차트가 필요하면 직접 SVG를 그린다.

## 서고의 실제 문구 (부속 문서나 갱신 방식을 보여 줄 때, 또는 지시가 "지금 문구 그대로"라고 할 때 쓴다)
- 부속 문서(1건): 제목 "UNI·ARB 관통 해부", 날짜 2026-09-08, 설명 "브리핑에서 파생된 종목 심층 분석", 링크 https://claude.ai/code/artifact/f371939a-b726-438b-98e2-92abf515976c
- 부속 문서 설명: "브리핑에서 갈라져 나온 심층 문서다. 새 문서는 요청하면 Claude가 이 자리에 등록한다."
- 갱신 방식 설명: "이 서고는 손으로 고치지 않는다. 브리핑을 발행한 실행이 서고의 데이터베이스에 한 건을 등록하고, 이 페이지는 그 기록으로 목록과 타임라인과 표를 계산한다."
- 갱신 방식 항목:
  - 06:10: 본실행이 브리핑을 발행한 직후 서고에 그날 건을 등록한다. 등록이 실패하면 한 번 더 시도하고, 그래도 실패하면 실행 보고와 앱 알림에 사유를 남긴다.
  - 07:40: 안전판은 그날 브리핑이 이미 있어서 종료하는 날에도, 종료하기 전에 서고에 그날 건이 있는지 확인한다. 없으면 그날 브리핑을 읽어 등록한다.
  - 수동: 직접 요청해 만든 브리핑도 스킬에 적힌 같은 절차로 등록한다. 같은 날 주소가 다른 브리핑을 또 발행하면 2회차로 남는다.
  - 표지: 표지는 이 페이지가 등록된 기록으로 직접 그린다. 실행이 표지를 따로 만들거나 저장하지 않으므로, 등록 절차는 그대로다.
  - 정정: 발행한 브리핑의 수치를 고치면 서고의 기록도 함께 고친다.
  - 보관: 브리핑 원본은 각각의 아티팩트로 남고, 서고 기록은 이 페이지의 데이터베이스에 쌓인다. 지표 표는 CSV로 내려받을 수 있다.
- 알림 문구: "이 서고는 브리핑을 정리한 색인이며 투자 자문이 아닙니다. 수치는 각 브리핑이 조회한 시점의 값입니다."

## 렌더링 규칙
- 폭 1440 한 장, 가로로 넘치지 않게 한다. 처음 연 상태(hover 없음, 검색 닫힘, 접힌 것은 접힌 채)를 그린다. 동작(hover, 검색 결과, 펼치기)은 구현하지 않아도 되지만, 화면에 보이는 컨트롤은 지시대로 그린다.
- 끝나기 전에 렌더링 결과를 직접 본다(PNG를 1400px 높이 안팎으로 잘라 자기 tmp 폴더에 저장하고 Read로 연다). 겹침, 잘림, 넘침, 빈 자리, 오류가 없을 때까지 고친다. shot.py가 헤드라인 넘침이나 오류를 보고하면 고친다.
- 지시에 적힌 크기와 색이 있으면 CSS 변수로 옮겨 그대로 쓴다. 고정 이미지나 외부 자원은 쓰지 않는다.

## 마지막 보고 (한국어, 10줄 이내)
최종 파일 경로, 렌더링 크기, 지시에서 구현하지 않았거나 해석한 부분.
