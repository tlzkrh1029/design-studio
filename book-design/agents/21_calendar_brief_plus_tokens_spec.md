# 달력 벽 · 브리프+토큰 명세 작성

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 10:32 (한국 시간)
- 작업 설명(원문): `Calendar brief+tokens spec`
- 도구 호출: 모두 8회 (Read 4, Bash 2, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write the prompt that a front-end developer will receive to build a web page. Use this method: a short Markdown design brief that fixes the intent, plus design tokens written as CSS custom properties that fix the values. The brief and the tokens will be the developer's only design instruction. The developer is a capable designer too: they will use the token values as they are and make every decision the brief leaves open, guided by the brief.

Read these files first:
- /home/claude/cover_design/experiment2/brief_common.md (shared brief)
- /home/claude/cover_design/experiment2/brief_calendar.md (this theme's concept and the current draft)
- Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).

This is a controlled experiment. Do not open anything under /home/claude/cover_design/experiment/, and do not open any other file in /home/claude/cover_design/experiment2/ except the ones listed above and your own output.

Write one Markdown file with these three parts, in this order:

1. A design brief titled "# 디자인 브리프: …", with these sections in Korean:
   - 목적: what the page is for, who opens it, and the five things they do on it.
   - 분위기: the mood, made concrete. Say what to do with colour, type, background and motion, not only adjectives.
   - 참고한 것: what to keep from the current draft. The developer cannot see the screenshots, so describe it in words.
   - 고칠 점: each weakness of the current draft and what to do about it.
   - 우선순위: the order in which the eye should read the page, most important first.
   - 상태별 규칙: how to show days without a briefing, the next issue, days with several issues, missing values and an empty search result.
   - 피할 것: each item with its reason and what to do instead.
   - 맡기는 부분: what the developer may decide freely.
   - 완료 기준: checks the finished page must pass.
2. "# 토큰": one ```css block containing a single :root { } rule with every design value: colours, font families, type sizes, weights and line heights, spacing, radii, shadows, layout widths and cover sizes. Name the variables by role (for example --text-2 or --line-ref), not by colour, and add a short comment where the role is not obvious.
3. "# 요청": a short closing request asking the developer to build the page from the brief and the tokens. Say that the brief is the standard for judgement and the tokens are values to use as they are, and that any new value they really need must be added to the tokens and reported at the end.

Rules:
- Keep the brief short: about 50 lines and at most 60, not counting the tokens. Design values such as hex colours and pixel sizes belong in the tokens, not in the brief; the brief may name a token when it needs to. Data values and thresholds from the shared brief (for example +1.0%p) may appear in the brief.
- Write all descriptions and every piece of on-screen copy in Korean.
- Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented).
- Do not invent facts or data that are not in the brief.
- The page will be rendered at 1440px desktop width only, so mobile adaptation is not needed.
- Do not write any HTML or JS, write CSS only inside the tokens block, and do not create any other files.

Save the file to /home/claude/cover_design/experiment2/specs/calendar.md with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 달력의 둥근 상자를 얇은 괘선 격자로 바꾸고 모든 날짜 칸의 높이와 표지 크기(108px)를 맞췄습니다. 초안처럼 표지를 겹쳐 쌓지 않고, 여러 번 발행한 날은 마지막 회차 표지 한 장과 'n회'만 칸에 둡니다. 나머지 회차는 고른 날 카드의 회차 탭에서 봅니다.
- 상태마다 모양을 따로 정했습니다. 브리핑 없는 날은 실선으로 그린 빈 표지 자리, 기록 전 날과 다른 달 날짜는 숫자만, 다음 호는 페이지에 하나뿐인 점선 자리입니다. 검색에 맞은 날은 칸 바탕만 형광펜색으로 칠하고 표지는 건드리지 않습니다.
- 지표 카드 셋과 오른쪽 추세선을 전체 폭 '9월의 흐름' 카드 하나로 합쳤습니다. 하루 한 칸짜리 국면 띠 아래에서 세 차트가 같은 날짜 열을 쓰고, +1.0%p와 0 기준선에는 이름표를 붙였습니다. 값이 없는 날은 선을 끊습니다.
- 고른 날 카드는 표지(300px) → 세리프 헤드라인(Noto Serif KR) → 국면 → '브리핑 펼치기' 순서로 바꿔 버튼이 첫 화면 안에 들어오게 했습니다. 강조색은 최신 표지에서 따온 짙은 청록과 복숭아 두 가지뿐이고, 국면 색은 국면 정보에만 씁니다.
- 국면 표식의 글자색을 색마다 정했습니다. 초안의 흰 글자는 A·B·E 위에서 명암비가 3.0~3.9로 기준에 못 미쳐, 세 색 위에는 어두운 글자를 씁니다. 모든 글자 조합은 4.5 이상이 되도록 토큰 값을 계산해 맞췄습니다.
````
