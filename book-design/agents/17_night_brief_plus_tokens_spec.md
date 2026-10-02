# 밤의 가판대 · 브리프+토큰 명세 작성

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 10:32 (한국 시간)
- 작업 설명(원문): `Night brief+tokens spec`
- 도구 호출: 모두 7회 (Read 4, Write 1, Bash 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write the prompt that a front-end developer will receive to build a web page. Use this method: a short Markdown design brief that fixes the intent, plus design tokens written as CSS custom properties that fix the values. The brief and the tokens will be the developer's only design instruction. The developer is a capable designer too: they will use the token values as they are and make every decision the brief leaves open, guided by the brief.

Read these files first:
- /home/claude/cover_design/experiment2/brief_common.md (shared brief)
- /home/claude/cover_design/experiment2/brief_night.md (this theme's concept and the current draft)
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

Save the file to /home/claude/cover_design/experiment2/specs/night.md with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 콘셉트(거의 검은 무대, 스포트라이트 아래 최신 호, 선반 위 지난 호, 강조색 = 최신 호 테두리색)는 그대로 둡니다. 히어로에서는 헤드라인을 가장 큰 글자로 올려 날짜와 다투지 않게 했습니다. 강조색은 버튼·오늘 표식·다음 호 자리·조명 기미 네 곳에만 씁니다.
- 가판대는 한 주에 선반 하나입니다(맨 위가 이번 주, 선반 안은 월→일). 31장을 숨기지 않고 모두 세웁니다. 브리핑이 없는 날은 좁은 빈칸으로 두고, 같은 날 나온 여러 호는 붙여 세우며, 이번 주 선반 끝에 '다음 호' 점선 칸을 둡니다.
- 시안에 없던 지표 시계열은 '국면과 지표' 구역으로 만들었습니다. 국면 띠(9/2~9/30, 29칸)와 차트 셋이 같은 날짜 열을 함께 씁니다. +1.0%p와 0 기준선, 그 너머 판정 구역을 표시합니다. 히어로의 ΣSTABLECOIN.D는 판정에 쓰는 1개월 변화(−0.705%p)를 크게 보입니다.
- 발행 목록은 지표 표와 합쳐 검색 결과 자리로 씁니다. 실행 칸은 안전판·지연 실행 같은 예외만 드러냅니다. 영어 부제와 로고는 한국어로 바꿉니다.
- 국면 칸 글자색은 명암비로 정했습니다(A·B·E는 어두운 글자, C·D는 흰 글자). 그래서 모든 글자가 4.5:1을 넘습니다. 오르내림은 색 대신 부호와 기준선으로 나타냅니다.
````
