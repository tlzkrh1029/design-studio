# 달력 벽 · XML 태그 명세 작성

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 10:33 (한국 시간)
- 작업 설명(원문): `Calendar XML-tag spec`
- 도구 호출: 모두 14회 (Bash 8, Read 4, Write 1, SubagentHandback 1)

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
- /home/claude/cover_design/experiment2/brief_calendar.md (this theme's concept and the current draft)
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

Save the file to /home/claude/cover_design/experiment2/specs/calendar.xml with your file-writing tool. Then reply with only a 3-5 line summary, in Korean, of the most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
- 겹쳐 쌓던 표지와 칸 귀퉁이의 국면 배지를 없앴다. 대신 칸 폭 전체에 국면 색 "선반"을 깔아 표지가 그 위에 서게 했다. 선반은 받침이라 표지 규칙에 맞고, 한 주가 한 줄 띠로 이어져 국면 흐름이 읽힌다. 국면 글자는 색 위가 아니라 날짜 줄에 본문색으로 써서 A·B·E 색의 명암비 미달을 피했다. 여러 회차 날은 칸에 대표 표지 1장과 "n회"만 두고, 오른쪽 칸에서 모든 회차를 나란히 보인다.
- 오른쪽 칸 순서를 표지(248px) → 세리프 헤드라인 → 국면 줄 → "브리핑 열기"로 바꿨다. 계산상 버튼이 1440×900 첫 화면 안(y≈790)에 들고, 오른쪽 칸은 스크롤해도 따라온다.
- 바탕은 지금의 청회색 벽과 흰 카드를 그대로 둔 무채색이다. 강조색은 최신 호 표지에서 뽑은 짙은 청록(누르는 것·고른 것)과 복숭아(오늘) 두 가지뿐이다. 글꼴은 역할별로 나눠 Gothic A1(UI), Outfit(날짜·숫자), IBM Plex Mono(표 숫자), Noto Serif KR(헤드라인 전용)을 쓰고, Oswald는 뺐다.
- 같은 점선이던 세 상태를 서로 다르게 나눴다. 빈 날은 점선 빈 자리에 띠가 끊기고, 기록 전은 날짜만 두고, 다음 호는 청록 점선 자리로 둔다. 흐리던 안내 글자는 명암비 4.5 이상으로 올렸다.
- 월 이동과 요약 수치(범례 겸용)를 달력 머리로 모았다. 오른쪽 칸의 중복 추세선은 빼고, 아래 차트에 +1.0%p·0 기준선과 고른 날 표시를 그렸다. 발행 목록과 지표 표는 한 표로 합쳤다.
````
