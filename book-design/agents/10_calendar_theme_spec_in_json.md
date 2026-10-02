# 달력 벽 · JSON 명세 작성

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-09-30 23:29 (한국 시간)
- 작업 설명(원문): `Calendar theme spec in JSON`
- 도구 호출: 모두 25회 (Read 8, Bash 8, Edit 7, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write a design spec for a web page, in JSON format. This spec will be the only instruction a front-end developer gets; they will implement it exactly without asking questions, so every visual decision must be explicit.

Read these files first:
- /home/claude/cover_design/experiment/brief_common.md (shared brief)
- /home/claude/cover_design/experiment/brief_calendar.md (this theme's concept and the current draft)
- Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).

Output requirements:
- One JSON object only. It must be valid JSON (no comments, no trailing commas).
- Keys in English. Descriptions and every piece of on-screen copy in Korean.
- Cover these topics: intent and mood; tokens (colours with hex values and their roles, typography with family, size in px, weight, line-height and letter-spacing per role, spacing scale, radii, shadows, motion if any); page frame and grid (1440px desktop); sections in order, each with layout and composition, exact sizes where they matter, and exact content mapping (which data fields appear where, and formats such as "59.18%" and "전날 +0.01%p"); components (cover display and its supports, cover collections, chips and badges, figures, phase timeline cells, list rows, buttons, search, navigation); states (hover, focus, empty, missing data); accessibility (contrast, focus order, labels); mobile 390px adaptation; do and don't.
- Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented).
- Keep it under about 300 lines when pretty-printed.
- Do not invent facts or data that are not in the brief.
- Do not write any HTML, CSS or JS, and do not create any other files.

Save the spec to /home/claude/cover_design/experiment/specs/calendar.json with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 달력 전체를 감싸던 큰 흰 카드를 없애고, 날짜 칸 하나하나를 흰 카드(136×226)로 만들어 청회색 벽에 붙은 달력으로 정리했습니다. 칸 표지는 약 100px에서 120px로 키웠습니다. '3회' 배지는 표지 밖 칸 윗줄로 옮겼고, 여러 번 발행한 날은 다른 표지를 겹치지 않고 표지 뒤 빈 종이로 쌓였음을 보여 줍니다.
- 칸마다 반복되던 채운 국면 칩은 작은 점+글자로 낮췄습니다. 한 달 국면 흐름은 달력 위 흰 '국면 흐름' 띠(9/1~9/30 하루 한 칸, 'C→D' 같은 걸친 판정은 반반 칠함)가 한 줄로 보여 주며, 이 띠를 눌러도 날짜를 고를 수 있습니다.
- 오른쪽 칸(320px)은 두 카드로 나눴습니다. 위는 고른 날 카드(272×400 표지와 받침대, 헤드라인, 칩 한 줄, '제31호 브리핑 펼치기' 버튼)이고, 아래는 지표 추이 카드(차트 3개, E 임시 기준 +1.0%p·0 기준선·고른 날 세로선)입니다. 버튼이 1440×800 첫 화면 안에 들어오고, 두 칸 높이가 약 1,396px로 맞습니다.
- 발행 목록과 지표 표는 '달력|목록' 전환 안의 표 하나로 합쳤습니다. 강조색은 오늘 표시용 복숭아색 #F2B39F 하나뿐입니다. 국면 색 위 글자는 A·B·E에 짙은 잉크, C·D에 흰색을 써서 명암비 4.5 이상을 맞췄습니다.
- 모바일(390px)에서는 고른 날 카드를 맨 위에 두고, 달력은 표지 없이 국면 막대만 넣은 작은 격자로 바꿉니다.
````
