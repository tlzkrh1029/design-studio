# 편집국 1면 · 브리프+토큰 명세 작성

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 10:32 (한국 시간)
- 작업 설명(원문): `Paper brief+tokens spec`
- 도구 호출: 모두 13회 (Bash 6, Read 5, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write the prompt that a front-end developer will receive to build a web page. Use this method: a short Markdown design brief that fixes the intent, plus design tokens written as CSS custom properties that fix the values. The brief and the tokens will be the developer's only design instruction. The developer is a capable designer too: they will use the token values as they are and make every decision the brief leaves open, guided by the brief.

Read these files first:
- /home/claude/cover_design/experiment2/brief_common.md (shared brief)
- /home/claude/cover_design/experiment2/brief_paper.md (this theme's concept and the current draft)
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

Save the file to /home/claude/cover_design/experiment2/specs/paper.md with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 흑백 신문 콘셉트는 그대로 지켰습니다. 색은 표지에만 둡니다. 국면 A~E도 색을 쓰지 않고 글자와 먹 무늬(먹·빗금·망점·가로줄·겹빗금)로 구분하며, 무늬는 토큰으로 정했습니다.
- 헤더를 줄였습니다. 제호는 96px로 줄이고, 날짜 줄은 제호 양옆의 작은 박스로 옮겨 헤더를 240px 안에 넣었습니다. 1440×900 첫 화면에 표지(400px) 전체, 헤드라인(52px, 두 줄 안팎), 먹 바탕의 ‘브리핑 전문 읽기’ 버튼이 모두 들어옵니다. 1면 지표 칸은 국면 판정을 맨 앞에 두고, ΣSTABLECOIN.D를 1개월 변화로 맞췄습니다. 시안에서 같은 숫자가 세 번 나오던 것도 없앴습니다.
- 국면 연표와 지표 그래프 3개를 같은 날짜 열에 위아래로 쌓아 ‘국면과 지표’ 한 구역으로 합치고 1면 바로 아래에 두었습니다. 그래프에는 +1.0%p와 0 기준선을 점선과 라벨로 그리고, 값이 없는 날은 선을 끊습니다. 연표는 시안과 달리 9.1을 빼고 9.2부터 시작합니다.
- 구역 순서는 1면 → 국면과 지표 → 표지 전체 → 발행 목록(지표 표를 겸함) → 부속 문서·갱신 방식 → 판권입니다. 시안 메뉴에 있었지만 구역이 없던 ‘발행 목록·부속 문서·갱신 방식’을 채우고, 검색에 범위 선택을 더했습니다.
- 상태별 표시를 정했습니다. 다음 호는 점선 틀(점선은 다음 호에만 씀), 브리핑이 없는 날은 ‘발행 없음’, 하루 여러 호는 모든 호에 회차를 답니다. 표기는 ‘제31호’, ‘9.30 수’로 통일하고 한글 기울임은 쓰지 않습니다.
````
