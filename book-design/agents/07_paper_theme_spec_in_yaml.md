# 편집국 1면 · YAML 명세 작성

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-09-30 23:28 (한국 시간)
- 작업 설명(원문): `Paper theme spec in YAML`
- 도구 호출: 모두 24회 (Edit 8, Bash 7, Read 6, Write 1, Grep 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write a design spec for a web page, in YAML format. This spec will be the only instruction a front-end developer gets; they will implement it exactly without asking questions, so every visual decision must be explicit.

Read these files first:
- /home/claude/cover_design/experiment/brief_common.md (shared brief)
- /home/claude/cover_design/experiment/brief_paper.md (this theme's concept and the current draft)
- Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).

Output requirements:
- One YAML document only. Quote every colour hex value, like "#0C0E12", because # starts a comment in YAML.
- Keys in English. Descriptions and every piece of on-screen copy in Korean.
- Cover these topics: intent and mood; tokens (colours with hex values and their roles, typography with family, size in px, weight, line-height and letter-spacing per role, spacing scale, radii, shadows, motion if any); page frame and grid (1440px desktop); sections in order, each with layout and composition, exact sizes where they matter, and exact content mapping (which data fields appear where, and formats such as "59.18%" and "전날 +0.01%p"); components (cover display and its supports, cover collections, chips and badges, figures, phase timeline cells, list rows, buttons, search, navigation); states (hover, focus, empty, missing data); accessibility (contrast, focus order, labels); mobile 390px adaptation; do and don't.
- Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented).
- Keep it under about 300 lines.
- Do not invent facts or data that are not in the brief.
- Do not write any HTML, CSS or JS, and do not create any other files.

Save the spec to /home/claude/cover_design/experiment/specs/paper.yaml with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 콘셉트 유지: 페이지는 종이색(#F2EEE4)과 먹(#16140F), 괘선만 쓰고 색은 표지에만 둔다. 국면도 흑백 도장(글자, 걸친 판정은 반쪽 나눔)으로 그리고, 표지에는 그림자와 받침 괘선 말고 아무것도 더하지 않는다.
- 첫 화면: 제호를 112px로 낮추고 좌우 귀퉁이 상자(오늘의 국면 C / 다음 호 10월 1일 06:10)를 붙였다. '브리핑 전문 읽기'는 헤드라인 바로 밑 먹색 버튼으로 올려 1440×900 안에 들어오게 했다. 숫자를 되풀이하던 해설 문단은 없애고, 지표 상자에 기준선(+1.0%p, 0)과의 관계를 적었다.
- 구역 순서를 1면 → 국면과 지표 → 전체 표지 → 발행 목록 → 서고 안내로 바꿔 색 구역과 흑백 구역이 번갈아 온다. 국면 연표와 차트 3개는 한 날짜 축(40px 칸 30개)에 세로로 맞추고 눈금, 기준선, 망점 구역을 넣었다.
- 전체 표지는 8단 그리드(141px)에 맞춘 8열이고 줄마다 받침 괘선을 깐다. 9.18–19에는 '브리핑 없음' 칸을 넣어 32칸이 네 줄을 꽉 채운다. 시안에 없던 발행 목록과 지표 표는 한 표로 합쳐 되살리고(처음 10줄만), 부속 문서와 갱신 방식은 서고 안내로 모았다.
- 'No.' 표기를 '제31호'로 통일했고, 한국어 문구 규칙에 따라 영문 부제를 뺐다. 검색은 범위 선택, 결과 띠, 빈 상태를 정했고, 모바일은 표지 3열, 연표 10칸×3줄, 표 대신 줄 목록으로 바꾼다.
````
