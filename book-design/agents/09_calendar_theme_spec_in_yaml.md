# 달력 벽 · YAML 명세 작성

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-09-30 23:29 (한국 시간)
- 작업 설명(원문): `Calendar theme spec in YAML`
- 도구 호출: 모두 17회 (Read 8, Bash 6, Write 1, Edit 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write a design spec for a web page, in YAML format. This spec will be the only instruction a front-end developer gets; they will implement it exactly without asking questions, so every visual decision must be explicit.

Read these files first:
- /home/claude/cover_design/experiment/brief_common.md (shared brief)
- /home/claude/cover_design/experiment/brief_calendar.md (this theme's concept and the current draft)
- Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).

Output requirements:
- One YAML document only. Quote every colour hex value, like "#0C0E12", because # starts a comment in YAML.
- Keys in English. Descriptions and every piece of on-screen copy in Korean.
- Cover these topics: intent and mood; tokens (colours with hex values and their roles, typography with family, size in px, weight, line-height and letter-spacing per role, spacing scale, radii, shadows, motion if any); page frame and grid (1440px desktop); sections in order, each with layout and composition, exact sizes where they matter, and exact content mapping (which data fields appear where, and formats such as "59.18%" and "전날 +0.01%p"); components (cover display and its supports, cover collections, chips and badges, figures, phase timeline cells, list rows, buttons, search, navigation); states (hover, focus, empty, missing data); accessibility (contrast, focus order, labels); mobile 390px adaptation; do and don't.
- Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented).
- Keep it under about 300 lines.
- Do not invent facts or data that are not in the brief.
- Do not write any HTML, CSS or JS, and do not create any other files.

Save the spec to /home/claude/cover_design/experiment/specs/calendar.yaml with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 여러 번 발행한 날의 표지를 겹쳐 쌓고 어둡게 하던 방식은 표지 규칙 위반이라 없앴습니다. 칸마다 표지는 1장(104×153)이고, 날짜 줄에 ‘3회’ 배지를 붙이며, 회차는 오른쪽 카드의 회차 전환으로 넘깁니다. 어떤 표식도 표지 위에 얹지 않습니다.
- 달력 위에 하루 한 칸짜리 ‘국면 흐름’ 띠를 넣었습니다(30칸, 글자가 든 색 블록, 걸친 판정은 좌우 반반). 주마다 끊겨 보이던 A~E 흐름을 한 줄로 읽을 수 있습니다.
- 오른쪽 카드는 표지 352×518 바로 아래에 헤드라인과 ‘브리핑 펼치기’를 두어, 첫 화면(높이 900) 안에서 오늘 호를 열 수 있게 했습니다. 칩 4개는 국면 칩, 임시 기준, 메타 한 줄로 줄였고, 그 아래 ‘9월 기록’ 카드를 두어 달력과 높이를 맞췄습니다.
- 스파크라인 카드는 축, 기준선(+1.0%p와 0), 고른 날 세로선이 있는 차트 3개로 바꿨고, 지표 표는 발행 목록의 열로 합쳤습니다. 검색 범위 선택과 결과 상태, 형제 서고 링크도 다시 넣었습니다.
- 명암비가 모자라던 회색 글자는 없애 모든 글자를 4.5:1 이상으로 맞췄습니다. 오늘 표시에는 최신 호 표지의 복숭아색 #F2B39F만 씁니다. 모바일(390px)에서는 달력 칸에서 표지를 빼고 가로 표지 선반으로 옮깁니다.
````
