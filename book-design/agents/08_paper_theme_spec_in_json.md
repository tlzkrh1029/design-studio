# 편집국 1면 · JSON 명세 작성

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-09-30 23:28 (한국 시간)
- 작업 설명(원문): `Paper theme spec in JSON`
- 도구 호출: 모두 24회 (Read 9, Bash 7, Grep 3, Edit 3, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write a design spec for a web page, in JSON format. This spec will be the only instruction a front-end developer gets; they will implement it exactly without asking questions, so every visual decision must be explicit.

Read these files first:
- /home/claude/cover_design/experiment/brief_common.md (shared brief)
- /home/claude/cover_design/experiment/brief_paper.md (this theme's concept and the current draft)
- Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).

Output requirements:
- One JSON object only. It must be valid JSON (no comments, no trailing commas).
- Keys in English. Descriptions and every piece of on-screen copy in Korean.
- Cover these topics: intent and mood; tokens (colours with hex values and their roles, typography with family, size in px, weight, line-height and letter-spacing per role, spacing scale, radii, shadows, motion if any); page frame and grid (1440px desktop); sections in order, each with layout and composition, exact sizes where they matter, and exact content mapping (which data fields appear where, and formats such as "59.18%" and "전날 +0.01%p"); components (cover display and its supports, cover collections, chips and badges, figures, phase timeline cells, list rows, buttons, search, navigation); states (hover, focus, empty, missing data); accessibility (contrast, focus order, labels); mobile 390px adaptation; do and don't.
- Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented).
- Keep it under about 300 lines when pretty-printed.
- Do not invent facts or data that are not in the brief.
- Do not write any HTML, CSS or JS, and do not create any other files.

Save the spec to /home/claude/cover_design/experiment/specs/paper.json with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
명세를 /home/claude/cover_design/experiment/specs/paper.json에 저장했습니다. 유효한 JSON이고 들여쓰기해 펼치면 261줄입니다.
- 페이지에는 종이와 잉크 계열 무채색 7개만 씁니다. 국면 색과 최신 표지 배색은 쓸 수 있어도 쓰지 않고, 색은 표지에서만 나오게 했습니다. 위계는 괘선(3px, 이중선, 1px, 점선), 명조와 고딕의 크기·굵기, 여백으로 세웁니다.
- 제호를 132px에서 84px로 줄이고 양옆 귀에 서고 현황을 넣었습니다. 1면은 표지 416 | 기사 | 사이드바의 3단입니다. 헤드라인 48px, 국면 판정 줄, 잉크 버튼 「브리핑 전문 읽기」가 첫 화면 900px 안에 들어오고, 사이드바에 지난 두 호와 다음 호 자리를 둡니다. 수치를 되풀이하던 해설 문단은 없애고, 기준선이 붙은 지표 3칸으로 바꿨습니다.
- 국면은 색 대신 A~E 레인의 위치로 보여 줍니다. 초안에 있던 서고 이전 날짜 9월 1일 칸은 빼고 9/2~9/30의 29칸만 둡니다. 지표 차트 3개는 같은 날짜 칸(36px)에 세로로 쌓고, 휴간은 빗금, 기준선 +1.0%p와 0은 점선과 구간 채움으로 표시해 하루를 위아래로 읽게 합니다.
- 초안에서 빠진 발행 목록과 지표 표는 하나의 표로 합치고, 부속 문서·갱신 방식·형제 서고는 「판권」에 모았습니다. 검색에는 범위 선택을 되살렸고, 메뉴는 실제로 있는 면(1면, 2면 표지 색인, 3면 국면·지표, 4면 발행 목록, 판권)으로만 이어집니다.
- 표기는 「제31호」, 음수는 U+2212로 통일하고, 한글이 섞인 문구에는 모노 글꼴을 쓰지 않습니다. 브리프에 없는 표지 그림·배색 이름은 넣지 않았습니다. 모바일에서는 표지 색인이 3열, 국면·지표는 한 상자 안의 가로 스크롤, 목록은 카드로 바뀝니다.
````
