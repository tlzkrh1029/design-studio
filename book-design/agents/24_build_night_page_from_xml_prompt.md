# 밤의 가판대 · XML 태그 명세로 페이지 구현

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 11:11 (한국 시간)
- 작업 설명(원문): `Build night page from XML prompt`
- 도구 호출: 모두 64회 (Read 34, Bash 27, Write 2, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer with a good eye for design. Build one web page from a design prompt.

1. Read /home/claude/cover_design/experiment2/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The design prompt is /home/claude/cover_design/experiment2/specs/night.xml: a prompt structured with XML tags. It is your only design instruction; follow its <instructions>. Write the <plan> it asks for to /home/claude/cover_design/experiment2/notes/night_xml.md before you build, and append the <check> to the same file after you build. For data context you may also read /home/claude/cover_design/experiment2/brief_common.md.
3. This is a controlled experiment, and each build must follow only its own prompt. Do not open any other file in /home/claude/cover_design/experiment2/specs/, the screenshots in /home/claude/cover_design/experiment2/originals/, the theme briefs (brief_night.md, brief_paper.md, brief_calendar.md), anything under /home/claude/cover_design/experiment/, or other people's pages, images, notes or tmp folders. Keep your temporary files only in /home/claude/cover_design/experiment2/tmp/night_xml/.
4. Output name: night_xml. Write /home/claude/cover_design/experiment2/night_xml.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment2/tmp/night_xml/out.png, look at the result, and fix problems until the page follows the prompt and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for, then the <check> results.
````

## 최종 보고 (원문 그대로)

````text
I've built the night_xml page and it follows the spec. The completion check passes 9 of 9 items. The render is 1440 × 6905 with no overflow, no headline overflow and no errors. The search states and the flow hover were also tested in a browser.

**보고**
- 최종 파일: /home/claude/cover_design/experiment2/night_xml.src.html → night_xml.html. 렌더링은 /home/claude/cover_design/experiment2/tmp/night_xml/out.png(1440×6905), 계획과 점검은 /home/claude/cover_design/experiment2/notes/night_xml.md에 있다.
- --accent는 토큰 값 #F2B39F 그대로 두었다. 9/30 표지 테두리의 실제 값(pal(L).fr)은 #FCB8A5라 조금 다르다. 날마다 그날 표지색으로 바꾸는 연결은 넣지 않았다.
- 페이지 스타일은 세 글꼴만 쓴다. 다만 표지를 원래대로 그리려고 표지 부품이 쓰는 Outfit 700·800, Gothic A1 600, Oswald 600도 함께 불러왔다.
- 갱신 방식은 IMPLEMENT의 실제 문구를 존댓말로 썼다. 지시가 <data>의 시각·실행 값으로만 쓰라고 해서, <data>에 없는 '07:40' 대신 실행 값 '안전판'을 항목 이름으로 썼다.
- '매크로 리스크 서고' 링크는 주소가 주어지지 않아 href="#"로 두었다(안내 구역과 바닥글 두 곳).
- 흐름의 국면 칸은 정사각형 32px(열 36 − 간격 4)로 그렸다. --flow-cell-height 40은 칸과 회차 점이 들어가는 줄 높이로 읽었다.
- 발행 목록은 지표 표를 겸하므로 31호를 모두 펼쳤다. 안내 문구의 "CSV로 내려받을 수 있다"가 사실이 되도록 'CSV 내려받기' 단추를 더했다. 칸에 올리면 뜨는 읽기 창, 검색, 메뉴의 현재 구역 표시는 실제로 동작한다.
- 헤드라인은 48px·640px 폭에서 첫 절이 한 줄에 들어가지 않아 세 줄이 되었고, 구절 단위로 끊었다. 히어로의 ΣSTABLECOIN.D 칸은 브리프대로 수준과 기준선 대비를 작은 두 줄로 두었다.

**<check>**
1. 첫 화면의 표지·헤드라인·국면·'브리핑 펼치기' — 통과: 표지 y121–768, 헤드라인 217–395, 국면 칸 443–499, 버튼 731–783로 모두 900 안이다.
2. 가판대 31호, 빈 자리, 회차 묶음 — 통과: 표지 31개가 섰고 09.18·09.19는 점선 빈 자리와 '브리핑 없음'이다. '09.03 목 · 3회', '09.05 토 · 2회', '09.24 목 · 2회' 꼬리표 하나씩에 표지별 회차 번호를 달았다.
3. 다음 호 자리 — 통과: 맨 위 선반 끝 강조색 점선 자리에 '다음 호 / 10.01 목 / 06:10 예정'만 있고, 흐름 축 끝에는 강조색 점선 빈 칸이 있다.
4. 흐름의 날짜 위치와 기준선 이름 — 통과: 9/30 칸 중심과 세 지표 줄의 오늘 점이 모두 x=1306이고, 9/3·9/5의 첫 점도 칸 중심과 같다. +1.0%p와 0 기준선에 이름이 붙어 있다.
5. 메뉴와 검색 결과 없음 — 통과: 메뉴 5개가 구역 5개와 1:1이다. 결과 없음 화면은 안내 문장, '범위를 전체로'·'검색 지우기', 예 09.24를 보여 주고 두 버튼이 동작한다.
6. 화면 문구 한국어 — 통과: 남은 영문은 지표·국면 이름, 실제 문구의 CSV·Claude, 문서 제목 UNI·ARB, 표지 안 글자뿐이다.
7. 명암비 — 통과: 페이지 글자와 바탕 35쌍을 자동 측정해 최저 5.08(B 칸)이다. 강조색 면 위 글자 10.4, 검색 자리 글 4.94, 행 hover 위 --text-3 4.57이다.
8. 강조색과 토큰 — 통과: 강조색은 허용된 쓰임새에만 썼고 메뉴 밑줄·눈썹 줄·헤드라인·차트 선은 무채색이다. CSS 본문에 직접 쓴 색·px 값은 없다(그라디언트 멈춤 %와 원뿔 방향 180deg만 남음). 토큰 값은 바꾸지 않았다.
9. 표지 무가공, 가로 스크롤 — 통과: 표지는 그림자·받침·주변 빛만 받고 hover는 --lift-hover만큼 세로로 뜬다. scrollWidth는 1440이다.

새 토큰 11개(이유는 notes 파일에 있다):

| 토큰 | 값 | 쓰임 |
|---|---|---|
| --hairline | 1px | 머리카락선·테두리 두께 |
| --mark-width | 2px | 현재 메뉴 밑줄, 오늘 칸 테두리 |
| --topbar-blur | 12px | 상단 막대 뒤 흐림 |
| --beam-spread | 20deg | 빛 기둥 퍼짐 각 |
| --beam-soft | 5deg | 빛 기둥 가장자리 번짐 |
| --beam-apex | −1150px | 빛 기둥 꼭짓점 높이 |
| --dot-issue | 4px | 흐름 칸 아래 회차 점 |
| --icon | 16px | 선 아이콘 크기 |
| --icon-stroke | 1.5px | 선 아이콘 획 두께 |
| --section-desc-width | 560px | 구역 머리 설명 폭 |
| --popover-width | 288px | 흐름 읽기 창 폭 |
````
