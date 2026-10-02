# 밤의 가판대 · JSON 명세 작성

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-09-30 23:28 (한국 시간)
- 작업 설명(원문): `Night theme spec in JSON`
- 도구 호출: 모두 16회 (Read 9, Bash 4, Grep 1, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write a design spec for a web page, in JSON format. This spec will be the only instruction a front-end developer gets; they will implement it exactly without asking questions, so every visual decision must be explicit.

Read these files first:
- /home/claude/cover_design/experiment/brief_common.md (shared brief)
- /home/claude/cover_design/experiment/brief_night.md (this theme's concept and the current draft)
- Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).

Output requirements:
- One JSON object only. It must be valid JSON (no comments, no trailing commas).
- Keys in English. Descriptions and every piece of on-screen copy in Korean.
- Cover these topics: intent and mood; tokens (colours with hex values and their roles, typography with family, size in px, weight, line-height and letter-spacing per role, spacing scale, radii, shadows, motion if any); page frame and grid (1440px desktop); sections in order, each with layout and composition, exact sizes where they matter, and exact content mapping (which data fields appear where, and formats such as "59.18%" and "전날 +0.01%p"); components (cover display and its supports, cover collections, chips and badges, figures, phase timeline cells, list rows, buttons, search, navigation); states (hover, focus, empty, missing data); accessibility (contrast, focus order, labels); mobile 390px adaptation; do and don't.
- Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented).
- Keep it under about 300 lines when pretty-printed.
- Do not invent facts or data that are not in the brief.
- Do not write any HTML, CSS or JS, and do not create any other files.

Save the spec to /home/claude/cover_design/experiment/specs/night.json with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
명세를 /home/claude/cover_design/experiment/specs/night.json에 저장했습니다. 올바른 JSON이고, 들여쓰기해 펼치면 227줄입니다.
- 히어로 위계를 정리했습니다. 420px 표지는 스포트라이트와 받침 위에 세우고, 헤드라인(46px)을 주인공으로 둡니다. 날짜는 40px로 내렸고, 오늘 호 칩 줄에는 국면·임시 기준·전날 국면만 둡니다. 헤드라인은 마지막 쉼표에서 나눠 뒷부분(본표제)을 강조색으로 씁니다.
- 가판대는 136px 표지를 8칸씩 선반 4개에 꽂아 9월 31장과 '다음 호 자리'를 한눈에 보여 줍니다. '더 보기'는 없애고, 선반마다 은은한 조명을 깔았습니다.
- 초안에서 빠진 지표 시계열을 '9월의 흐름' 구역으로 되살렸습니다. 국면 타임라인과 같은 30열에 BTC.D, ΣSTABLECOIN.D 1개월 변화, BTCUSD 1개월 차트를 쌓고 기준선(+1.0%p, 0)을 그립니다. 표는 버튼을 누르면 펼쳐집니다. 검색에는 범위 선택을 더해 결과가 발행 목록을 거르게 했고, 부속 문서·갱신 방식·형제 서고는 '안내' 구역에 담았습니다.
- 강조색은 최신 표지 테두리색을 따르되 바탕 대비 4.5 미만이면 밝혀 씁니다. 가장 어두운 회색 글자는 #8E95A1(명암비 6.5)로 올렸습니다. 한글 넓은 자간, 영문 장식 라벨, 등락 초록·빨강은 금지했고, 실행 알약은 안전판·지연 실행 같은 예외만 도드라지게 했습니다.
````
