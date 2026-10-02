# 밤의 가판대 · XML 태그 명세 작성

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 10:32 (한국 시간)
- 작업 설명(원문): `Night XML-tag spec`
- 도구 호출: 모두 14회 (Read 5, Edit 5, Bash 2, Write 1, SubagentHandback 1)

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
- /home/claude/cover_design/experiment2/brief_night.md (this theme's concept and the current draft)
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

Save the file to /home/claude/cover_design/experiment2/specs/night.xml with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 가판대를 주 단위 선반으로 바꿨습니다. 최신 주가 맨 위에 오고, 주 안에서는 날짜순으로 하루 한 칸씩 31호를 모두 세웁니다. 9/18·19는 회색 점선 빈 자리로 두고, 9/3·9/5·9/24는 회차 수만큼 표지를 붙여 꼬리표 하나로 묶습니다. 맨 위 선반 끝에는 강조색 점선으로 '다음 호(10.01 목 06:10)' 자리를 둡니다. '더 보기' 버튼과 표지 아래 초록 C 배지 21개는 없앴습니다.
- 히어로에서는 헤드라인을 가장 큰 글자로 올리고, 날짜는 그 위 한 줄로 줄였습니다. 같은 무게로 늘어서던 칩 네 개는 '국면 큰 칸 + 이름'과 보조 줄로 나눴습니다. 지표는 추세선을 빼고 오늘 값과 기준선 대비 문장만 둡니다(ΣSTABLECOIN.D는 수준 대신 1개월 변화 −0.705%p를 크게).
- 국면 타임라인과 지표 차트 3개를 같은 날짜 축에 쌓아 '국면·지표' 구역 하나로 합쳤습니다. 날짜는 9/2부터 그리고 +1.0%p·0 기준선에 이름을 붙입니다. 발행 목록은 31호 전체에 지표 열을 더해 검색 대상 겸 지표 표로 바꿨고, 메뉴는 실제 구역과 1:1로 맞췄습니다.
- 강조색(--accent)은 그날 표지의 테두리색입니다. 빛 번짐과 검색어 강조는 color-mix로 이 색에서 만들어, 값 하나만 바꾸면 페이지 전체가 함께 바뀝니다. 쓰임새는 '오늘' 표식, 주 버튼, 다음 호 자리, 초점 테두리로 한정했습니다.
- 증감은 국면 색과 겹치지 않게 색 대신 부호와 ▲▼로만 씁니다. 국면 칸 글자는 명암비에 맞춰 A·B·E는 검정, C·D는 흰색으로 정했고, 영문 보조 제목은 모두 한국어로 바꿨습니다.
````
