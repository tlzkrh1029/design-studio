# 편집국 1면 · 브리프+토큰으로 페이지 구현

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 11:12 (한국 시간)
- 작업 설명(원문): `Build paper page from brief+tokens`
- 도구 호출: 모두 85회 (Bash 34, Read 33, Edit 12, Write 5, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer with a good eye for design. Build one web page from a design prompt.

1. Read /home/claude/cover_design/experiment2/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The design prompt is /home/claude/cover_design/experiment2/specs/paper.md: a short design brief plus design tokens. It is your only design instruction. Use the token values as they are. Where the brief leaves a decision to you, make it yourself in line with the brief's purpose, mood and priorities. For data context you may also read /home/claude/cover_design/experiment2/brief_common.md.
3. This is a controlled experiment, and each build must follow only its own prompt. Do not open any other file in /home/claude/cover_design/experiment2/specs/, the screenshots in /home/claude/cover_design/experiment2/originals/, the theme briefs (brief_night.md, brief_paper.md, brief_calendar.md), anything under /home/claude/cover_design/experiment/, or other people's pages, images, notes or tmp folders. Keep your temporary files only in /home/claude/cover_design/experiment2/tmp/paper_md/.
4. Output name: paper_md. Write /home/claude/cover_design/experiment2/paper_md.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment2/tmp/paper_md/out.png, look at the result, and fix problems until the page follows the prompt and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for, including any tokens you added and why.
````

## 최종 보고 (원문 그대로)

````text
paper.md 브리프대로 페이지를 만들었고, 제가 돌린 검사를 모두 통과했습니다.

1. **파일:** 원본 `/home/claude/cover_design/experiment2/paper_md.src.html`, 빌드 결과 `/home/claude/cover_design/experiment2/paper_md.html`, 렌더 `/home/claude/cover_design/experiment2/tmp/paper_md/out.png`(**1440×5102**). shot.py는 오류도, 헤드라인 넘침도 보고하지 않았습니다.
2. **검사 결과:** 머리 높이는 233px(상한 240)입니다. 1440×900 첫 화면에 최신 호 표지 전체(y 261–849), 헤드라인, ‘브리핑 전문 읽기’ 띠가 모두 들어갑니다. 색 검사에서 표지 밖 색 픽셀은 0이고, 검색(결과·일치 강조·결과 없음 안내·지우기)도 동작합니다.
3. **추가한 토큰:**
   - `--tl-head-h: 18px`: 연표 칸 위에 구간 이름과 ‘3회’를 적는 줄.
   - `--fs-stat-side: 18px`: 1면 큰 숫자 옆 단위(%, %p)와 국면 이름.
   - `--grain-size: 160px`: 종이 결이 반복되는 단위.
4. **해석, 1면:** 서가는 최신부터 제30호·제29호를 두고, 오른쪽 끝에 점선 다음 호 틀을 둡니다. 틀 안에 ‘제32호’를 덧붙였습니다. 지표 칸 보조 줄은 BTC.D 전날 대비, ΣSTABLECOIN.D 수준값, BTCUSD 전날 값입니다.
5. **해석, 연표·차트:** 구간 이름은 하루 전체가 이틀 이상 이어진 구간에만 적습니다. 걸친 날은 ‘C→D’로 적고 띠를 반씩 나눕니다. 차트 날짜 눈금은 모두 짧은 꼴로, ‘9.3’ 아래 ‘목’을 쌓았습니다. 차트 라벨 단 셋째 줄은 ‘기준선 +1.0%p’, ‘기준선 0’입니다.
6. **해석, 표지 전체·목록:** 둘 다 같은 날 안에서도 늦은 회차부터(2회 다음 1회) 놓습니다. 같은 날 표지를 묶는 괄호선은 캡션 아래에 두고 날짜를 한 번만 적었습니다. 부속 문서와 갱신 방식은 위아래 두 구역으로 두고, 각각 두 단의 작은 글로 짰습니다.
7. **검색:** 결과 헤드라인을 보통 굵기로 두어, 일치한 낱말(`--fw-emph`, 바탕 `--bg-2`)이 굵게 보입니다. 지표 표 CSV 내려받기 링크는 페이지가 직접 만듭니다.
8. **남은 일:** ‘매크로 리스크 서고’ 주소가 주어지지 않아 링크는 자리표시(`href="#"`)입니다.
9. **글꼴·그림자:** 표지 워드마크가 쓰는 Outfit 700을 추가로 링크했고, 페이지 글자는 네 가족만 씁니다. 표지 자체 그림자는 건드리지 않았고, 토큰 그림자는 감싼 div에 줬습니다.
10. **색 번짐:** 크롬의 LCD 글자 렌더링이 표지 밖 글자에 색 번짐을 만들어, `#app`에 `will-change: transform`을 줘 글자를 회색조로 그립니다.
````
