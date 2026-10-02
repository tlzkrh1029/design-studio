# 밤의 가판대 · 명세 없이 바로 구현

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 11:12 (한국 시간)
- 작업 설명(원문): `Build night page directly, no spec`
- 도구 호출: 모두 74회 (Read 36, Bash 28, Edit 5, Grep 3, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer who also builds front-end pages. Redesign one web page and build it yourself. There is no design spec in this task: go straight from the brief and the current draft to the finished page. Do not write a spec, a plan document or any other design document first.

1. Read these files first:
   - /home/claude/cover_design/experiment2/brief_common.md (shared brief)
   - /home/claude/cover_design/experiment2/brief_night.md (this theme's concept and the current draft)
   - Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).
   - /home/claude/cover_design/experiment2/IMPLEMENT.md: the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules. Where it mentions instructions, the brief and the current draft are your instructions, and you make every design decision yourself.
2. Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented). Write all on-screen copy in Korean. Do not invent facts or data that are not in the brief.
3. This is a controlled experiment. Do not open anything in /home/claude/cover_design/experiment2/specs/ or /home/claude/cover_design/experiment2/notes/, the other theme briefs, anything under /home/claude/cover_design/experiment/, or other people's pages, images or tmp folders. Keep your temporary files only in /home/claude/cover_design/experiment2/tmp/night_direct/.
4. Output name: night_direct. Write /home/claude/cover_design/experiment2/night_direct.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment2/tmp/night_direct/out.png, look at the result, and fix problems until the page has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for, followed by 3-5 lines on your most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
**보고**
- 최종 파일: `/home/claude/cover_design/experiment2/night_direct.src.html`. 빌드 결과는 `/home/claude/cover_design/experiment2/night_direct.html`이고, 렌더링은 `/home/claude/cover_design/experiment2/tmp/night_direct/out.png`에 있다.
- 렌더링 크기는 1440×4937이다. shot.py 결과는 표지 헤드라인 넘침 없음, 오류 없음, 가로 넘침 없음이다. 텍스트 박스가 서로 겹치는지 프로그램으로 따로 검사했고, 1440px와 390px 모두 0건이었다.
- 형제 서고 "매크로 리스크 서고"는 브리프에 주소가 없어서 링크를 `href="#"`로 두었다.
- 검색은 닫힌 상태(범위 선택 + 입력칸)만 그렸고, 결과를 보여 주는 동작은 만들지 않았다. "나머지 23호 펼치기", "표로 보기", CSV 내려받기는 실제로 동작한다.
- "다음 호 자리"(10월 1일 목요일 06:10, 제32호)는 매일 06:10 발행 규칙에서 계산했다. 타임라인은 원래 시안의 9/1~9/30이 아니라 9/2~9/30, 29칸이다. 9/1은 서고가 시작되기 전이라 "브리핑 없음"으로 세면 브리프의 2일과 맞지 않는다.
- 강조색은 `pal(L).fr`를 그대로 쓴다. 바탕과의 명암비가 4.5보다 낮은 날만 자동으로 밝힌다. 오늘 복숭아색은 그대로 통과한다.
- 오늘 표지는 히어로와 '이번 주' 선반의 "오늘" 칸에 두 번 나온다. 한 주를 빠짐없이 보이게 하려고 일부러 그렇게 했다.
- 모바일(390px)은 CSS로만 대응했다. 렌더링 비교 대상은 아니지만 넘침이 없는 것까지 확인했다.

**핵심 디자인 결정**
1. 가판대는 한 줄에 한 주(월~일)씩 최신 호부터 꽂았다. 31호를 모두 148px 표지로 보이게 했고, 원래 시안의 "더 보기" 버튼은 없앴다. 표지는 8칸 격자에 맞췄다. 9/18·19는 빈칸으로 두고, 그날 하루 여러 회차는 "1회/2회" 표시로 구분한다. 날짜·요일·국면은 선반 앞면에 가격표처럼 찍었다.
2. 국면 타임라인과 지표 차트 3개를 날짜 축 하나로 합쳤다. ΣSTABLECOIN.D 1개월 차트에는 E 판정 기준선(+1.0%p)을, BTCUSD 1개월 차트에는 D·E 전제선(0)을 그렸다. 브리핑이 없는 날은 빗금으로, 오늘 열은 빛으로 표시해 국면과 지표의 흐름을 한눈에 읽게 했다.
3. 히어로는 헤드라인이 가장 먼저 읽히게 위계를 정리했다. 날짜(72→52px)와 수치(34px)를 낮췄고, 헤드라인 뒷절은 표지와 같은 강조색으로 썼다. 조명은 펜던트 등과 가장자리가 부드러운 빛줄기, 표지 바탕색의 후광, 가로로 긴 카운터 위 빛 웅덩이로 다시 만들었다. 표지 자체는 손대지 않았다.
4. 강조색은 '오늘' 신호에만 아껴 썼다. 메뉴 밑줄, 키커, 주 버튼, 오늘 태그, 오늘 열, 기준선이 그 자리다. 부속 문서, 갱신 방식, 형제 서고, 알림은 IMPLEMENT.md에 있는 실제 문구로 맨 아래 판권면에 모았다.
````
