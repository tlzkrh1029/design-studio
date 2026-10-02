# 달력 벽 · XML 태그 명세로 페이지 구현

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 11:12 (한국 시간)
- 작업 설명(원문): `Build calendar page from XML prompt`
- 도구 호출: 모두 90회 (Read 32, Bash 30, Edit 21, Write 4, Grep 2, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer with a good eye for design. Build one web page from a design prompt.

1. Read /home/claude/cover_design/experiment2/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The design prompt is /home/claude/cover_design/experiment2/specs/calendar.xml: a prompt structured with XML tags. It is your only design instruction; follow its <instructions>. Write the <plan> it asks for to /home/claude/cover_design/experiment2/notes/calendar_xml.md before you build, and append the <check> to the same file after you build. For data context you may also read /home/claude/cover_design/experiment2/brief_common.md.
3. This is a controlled experiment, and each build must follow only its own prompt. Do not open any other file in /home/claude/cover_design/experiment2/specs/, the screenshots in /home/claude/cover_design/experiment2/originals/, the theme briefs (brief_night.md, brief_paper.md, brief_calendar.md), anything under /home/claude/cover_design/experiment/, or other people's pages, images, notes or tmp folders. Keep your temporary files only in /home/claude/cover_design/experiment2/tmp/calendar_xml/.
4. Output name: calendar_xml. Write /home/claude/cover_design/experiment2/calendar_xml.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment2/tmp/calendar_xml/out.png, look at the result, and fix problems until the page follows the prompt and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for, then the <check> results.
````

## 최종 보고 (원문 그대로)

````text
calendar_xml 페이지를 만들고 확인을 마쳤다. 프롬프트의 <instructions>를 따랐고, 완료 기준 9개가 렌더된 화면에서 모두 통과했다. 계획과 확인 기록은 노트 파일에 있다.

**보고 (한국어)**
- 최종 파일: /home/claude/cover_design/experiment2/calendar_xml.src.html. 빌드 결과는 /home/claude/cover_design/experiment2/calendar_xml.html, 렌더는 /home/claude/cover_design/experiment2/tmp/calendar_xml/out.png, 계획과 확인 기록은 /home/claude/cover_design/experiment2/notes/calendar_xml.md에 있다.
- 렌더링 크기는 1440 × 3862이다. 가로 넘침, 헤드라인 넘침, 오류는 없다.
- 구성: 머리(검색 + 페이지 안 이동 링크 + 형제 서고) → 달력 카드(936)와 sticky 오른쪽 칸(400) → 차트 3장 → "발행 목록" 표 → 바닥글(부속 문서, 갱신 방식).
- 형제 서고 "매크로 리스크 서고"는 주소가 주어지지 않아 링크 자리만 그렸다(href="#", 눌러도 이동하지 않음).
- 오른쪽 칸이 sticky라 전체 캡처에서는 그 아래(y 974–1362)가 벽으로 비어 보인다. 스크롤하면 칸이 따라오고 900px 화면 안에 통째로 든다.
- 요약 수치는 참고 시안의 형식("31 브리핑 · 27 발행한 날 …")을 그대로 썼다. 값은 완료 기준(31호, 27일, 2일, 3일, 26일)과 같다.
- "걸친 판정" 범례 견본은 데이터의 첫 사례인 C|D 두 색으로 그렸다.
- 칸, 선반, 차트는 그날 마지막 회차 기준이고, 오른쪽 칸의 지표는 보고 있는 회차 기준이다.
- 갱신 방식 문구("지표 표는 CSV로 내려받을 수 있다")가 참이 되도록 발행 목록에 CSV 내려받기를 넣었다.
- Oswald와 Outfit 800은 표지 안에서만 쓰이므로 링크만 했다. 새 토큰은 --line-w, --ring-w, --chart-select-w 세 개다.

<check>
측정 조건: 렌더 1440 × 3862, tmp/calendar_xml/check.py(Playwright, 1440×900 화면)로 쟀다.
1. 첫 화면에 오늘 호 일곱 요소 — 통과. y 좌표(위–아래): "오늘" 124–144, 제31호 159–182, "9월 30일 수요일" 152–182, 표지 198–563, 헤드라인 583–647, 국면 줄 659–678, "브리핑 열기" 694–746. 가장 아래 끝이 746이라 900 안에 든다.
2. 네 상태가 서로 다른 모양 — 통과.
   - 9/18·19: --line-empty 점선 빈 자리(속 --bg-sunken) + "브리핑 없음", 선반 대신 1px 바닥선.
   - 9/1: 날짜만 --text-3로 쓰고 "기록 전"을 붙임.
   - 10/1: --accent 점선 자리에 "제32호 / 06:10 / 발행 예정".
   - 달 밖(8.30·8.31·10.2·10.3): 점 표기 날짜만 --text-3.
   - 1.5px 점선은 1배율 Chrome에서 1px로 그려진다.
3. 회차 수·나란히·겹침 없음 — 통과. 날짜 줄에 3회·2회·2회가 보인다. 9/3을 고르면 100px 표지 셋이 x 1034–1134 / 1150–1250 / 1266–1366에 서고, 겹침 0, 보는 회차만 받침이 깔린다. 달력 표지 27장(104×153)도 겹침 0이고, transform·filter·opacity가 없다. 고른 칸의 고리는 표지에서 좌우 11px, 위 38px, 아래 16px 떨어져 있다.
4. 선반 띠와 범례 — 통과. 선반은 8px × 125px, 이웃과 2px 틈이다. 1주는 ?·C|D·?·A|C, 2~5주는 C 띠이고 9/18·19에서 끊긴다. 범례에 다섯 국면, 걸친 판정, "? 국면 없음"이 모두 있다.
5. 수치가 data와 같음 — 통과. 달력 머리 31/27/2/3/26. 오른쪽 칸 제31호, 국면 C · 선별적, 임시 기준 · 전날 국면 C, 06:10 본실행, 59.18%(전날 +0.01%p), −0.705%p(점유율 9.125%), +6.71%.
6. 기준선과 고른 날 — 통과. +1.0%p 점선("E 임시 기준 +1.0%p")과 0 점선("D·E 판정의 전제 기준 0")에 라벨이 있다. 세 차트에 고른 날 세로선·점·"9.30"이 있고, 표의 09.30 행이 칠해진다. 9/3을 고르면 세 차트와 표 세 행이 함께 바뀐다. 선은 9/18·19에서 끊긴다.
7. 검색 — 통과. "꼬리"는 2건(제29호 9/28, 제23호 9/23)이 나오고 두 칸이 --bg-match로 칠해진다. "얼룩말"은 "‘얼룩말’에 맞는 호가 없습니다", 찾는 법 한 줄, "검색 지우기"를 보이고 달력은 그대로다. "9/24"는 그날을 바로 고른다.
8. 명암비와 키보드 — 통과. 글자 377종을 실측해 최저가 5.58("브리핑 없음", --text-3/--bg-sunken)이다. Tab으로 검색, 날짜(한 칸만 Tab), "브리핑 열기", CSV에 모두 닿고, 닿은 곳마다 --focus-ring이 보인다. 달력은 화살표·Home·End로 옮기고, 고른 날이 포커스를 따라간다.
9. 디자인 값이 모두 토큰 — 통과. :root 밖의 값은 모두 var()다(예외는 화면에서 숨기는 .sr의 1px). JS에는 색 값이 없다. 새 토큰 세 개:
   - --line-w: 1px: 가는 선·테두리 두께. 토큰에 선 색만 있고 두께가 없어 더했다.
   - --ring-w: 2px: 고른 날 칸의 --accent 고리 두께.
   - --chart-select-w: 1.5px: 차트의 고른 날 세로선 두께.
</check>
````
