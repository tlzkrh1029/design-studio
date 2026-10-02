# 편집국 1면 · XML 태그 명세 작성

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 10:32 (한국 시간)
- 작업 설명(원문): `Paper XML-tag spec`
- 도구 호출: 모두 35회 (Read 19, Bash 11, Edit 3, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer. Write the prompt that a front-end developer will receive to build a web page. Structure the whole prompt with XML tags, following Anthropic's published guidance for prompting Claude:
- Wrap each kind of content in its own tag, and use descriptive tag names consistently.
- Nest tags when the content has a hierarchy (for example <references> containing <reference index="1">).
- Put the long material near the top and the instructions at the end.
- In the instructions, refer to content by its tag name (for example "use only the values in <tokens>").
- Ask for outputs in tags: a short plan in <plan> before building, and a check against the acceptance criteria in <check> after building.
- Give the reason behind each important instruction, and say what to do rather than only what not to do.
Content inside a tag may be plain text, a Markdown list or CSS. This is a prompt, not a strict XML document, so do not escape characters.

The prompt will be the developer's only design instruction. The developer is a capable designer too: they will use the token values as they are and make every decision the prompt leaves open, guided by the brief inside it.

Read these files first:
- /home/claude/cover_design/experiment2/brief_common.md (shared brief)
- /home/claude/cover_design/experiment2/brief_paper.md (this theme's concept and the current draft)
- Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).

This is a controlled experiment. Do not open anything under /home/claude/cover_design/experiment/, and do not open any other file in /home/claude/cover_design/experiment2/ except the ones listed above and your own output.

Use these top-level tags, in this order:
1. <context>: what the page is, who opens it and why, and what this task changes.
2. <data>: the data facts the page shows, taken from the shared brief: counts, days without a briefing, days with several issues, the latest issue's values, the phases and the thresholds. Do not add facts.
3. <references>: what to keep from the current draft, one <reference> per part. The developer cannot see the screenshots, so describe each part in words.
4. <brief>: a short Markdown design brief with these sections in Korean: 목적; 분위기 (made concrete: colour, type, background and motion, not only adjectives); 고칠 점 (each weakness of the current draft and what to do about it); 우선순위 (the reading order, most important first); 상태별 규칙 (days without a briefing, the next issue, days with several issues, missing values, an empty search result); 피할 것 (each item with its reason and what to do instead); 맡기는 부분 (what the developer may decide freely); 완료 기준 (checks the finished page must pass).
5. <tokens>: a single :root { } rule with every design value: colours, font families, type sizes, weights and line heights, spacing, radii, shadows, layout widths and cover sizes. Name the variables by role (for example --text-2 or --line-ref), not by colour, and add a short comment where the role is not obvious.
6. <instructions>: numbered steps for the developer that refer to the other tags by name. Include these: build the page from <brief> and <tokens>; treat <brief> as the standard for judgement and the values in <tokens> as values to use as they are; add any new value they really need to the tokens and report it; write a plan of at most 10 lines in <plan> before building; after building, check every acceptance criterion in <brief> and write the results in <check>.

Rules:
- Keep <brief> short: about 50 lines and at most 60. Design values such as hex colours and pixel sizes belong in <tokens>, not in <brief>; the brief may name a token when it needs to. Data values and thresholds from the shared brief (for example +1.0%p) may appear anywhere.
- Write all descriptions and every piece of on-screen copy in Korean.
- Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented).
- Do not invent facts or data that are not in the brief.
- The page will be rendered at 1440px desktop width only, so mobile adaptation is not needed.
- Do not write any HTML or JS, write CSS only inside <tokens>, and do not create any other files.

Save the file to /home/claude/cover_design/experiment2/specs/paper.xml with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 1면 짜임: 헤드라인을 대표 표지(480px)와 가운데 단 위로 두 줄로 걸치고, 아래를 세 단(대표 표지 | 읽기 버튼·국면·지표 | 지난 두 호·다음 호 제32호)으로 나눴다. 그래서 첫 화면 밖에 있던 '브리핑 전문 읽기'가 헤드라인 바로 아래의 검은 칠 버튼으로 올라온다.
- 국면 표시: "색은 표지에만" 콘셉트를 지키려고 국면 색과 표지 배색을 페이지에 쓰지 않았다. 국면은 잉크 무늬 다섯 가지(검정 칠·망점·사선·가로줄·엇갈린 빗금)와 글자로 가르고, 'C→D'는 두 무늬를 반씩 나눠 보인다.
- 3면 통합: 국면 연표와 지표 차트 셋을 한 면에 쌓아 같은 날짜 칸(9/2~9/30, 29일 × 36px)을 쓰게 하고, +1.0%p와 0 기준선을 이름 붙여 긋게 했다. 지표 표기는 어디서나 BTC.D, ΣSTABLECOIN.D 1개월, BTCUSD 1개월 세 값과 같은 자릿수로 맞췄다.
- 상태와 일관성: 휴간(9/18·9/19)은 2·3·4면 모두에서 보이게 하고(2면 빈 지면 칸, 3면 짙은 종이 띠, 4면 휴간 한 줄), 시안이 9/1을 휴간처럼 그린 오류도 고쳤다. 표기는 '제n호'로, 같은 날 여러 번 낸 호에는 모두 'n회'를 달게 했다. 메뉴에만 있던 발행 목록(지표 표 겸 검색 결과, 범위 선택 포함)과 판권은 실제 면으로 넣었다.
- 표지 크기: 대표 480px과 작은 표지 141px 두 가지만 쓴다. 141px은 1면 오른쪽 단과 2면 8열 색인에 같이 쓰며, 8 × 141 + 7 × 24 = 1296으로 본문 폭에 딱 맞는다.
````
