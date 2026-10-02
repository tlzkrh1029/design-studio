# 밤의 가판대 · YAML 명세 작성

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-09-30 23:28 (한국 시간)
- 작업 설명(원문): `Night theme spec in YAML`
- 도구 호출: 모두 25회 (Read 9, Bash 9, Edit 4, Skill 1, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write a design spec for a web page, in YAML format. This spec will be the only instruction a front-end developer gets; they will implement it exactly without asking questions, so every visual decision must be explicit.

Read these files first:
- /home/claude/cover_design/experiment/brief_common.md (shared brief)
- /home/claude/cover_design/experiment/brief_night.md (this theme's concept and the current draft)
- Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).

Output requirements:
- One YAML document only. Quote every colour hex value, like "#0C0E12", because # starts a comment in YAML.
- Keys in English. Descriptions and every piece of on-screen copy in Korean.
- Cover these topics: intent and mood; tokens (colours with hex values and their roles, typography with family, size in px, weight, line-height and letter-spacing per role, spacing scale, radii, shadows, motion if any); page frame and grid (1440px desktop); sections in order, each with layout and composition, exact sizes where they matter, and exact content mapping (which data fields appear where, and formats such as "59.18%" and "전날 +0.01%p"); components (cover display and its supports, cover collections, chips and badges, figures, phase timeline cells, list rows, buttons, search, navigation); states (hover, focus, empty, missing data); accessibility (contrast, focus order, labels); mobile 390px adaptation; do and don't.
- Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented).
- Keep it under about 300 lines.
- Do not invent facts or data that are not in the brief.
- Do not write any HTML, CSS or JS, and do not create any other files.

Save the spec to /home/claude/cover_design/experiment/specs/night.yaml with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
명세를 /home/claude/cover_design/experiment/specs/night.yaml 에 저장했습니다(285줄, YAML 파싱 확인, 색상값 22개 모두 따옴표 처리).

- 히어로: 72px 날짜가 헤드라인을 누르던 위계를 뒤집어 날짜는 48px, 헤드라인은 44px/800으로 주인공이 되게 했습니다. 칩 4개는 "국면 줄" 하나(배지·임시 기준·전날 국면)로 줄였고, 표지 400px은 전등·빛기둥·후광 아래 받침에 세우고 캡션 "다음 호 · 10월 1일 목요일 06:10 예정"을 붙였습니다.
- 강조색: 최신 호 표지 테두리색을 받아 surface_2 대비 4.5 미만이면 흰색을 섞어 밝히는 규칙을 넣었습니다. 등락에는 색을 쓰지 않고 부호만 씁니다(국면 C 초록과 겹치기 때문).
- 가판대: 히어로와 겹치던 최신 호를 빼고 지난 호 30장을 한 줄 8칸(143×210)으로 모두 꽂았습니다. 브리핑 없는 날(9/18·19)은 점선 빈 자리로 두어 32칸 4줄이 되며, "더 보기"는 없앴습니다.
- 구역 순서: 국면 띠를 히어로 바로 아래로 올렸고, 발행 전인 9/1 칸을 지워 29칸으로 맞췄습니다. 작은 추세선은 빼고 기준선(+1.0%p, 0)을 그은 "지표 추이" 차트 3개와 표를 새로 넣었습니다. 검색에는 범위 선택과 결과 판을 더했고, 부속 문서·갱신 방식은 "서고 안내" 구역으로 되살렸습니다.
- 명암비는 계산해서 확인했고, 영어 장식 라벨을 없앴으며 가장 작은 글자는 12px입니다. 부속 문서·갱신 방식은 지금 서고의 문구를 그대로 옮기라고만 적었습니다. 제가 그 문구를 갖고 있지 않아 새로 쓰지 않았습니다.
````
