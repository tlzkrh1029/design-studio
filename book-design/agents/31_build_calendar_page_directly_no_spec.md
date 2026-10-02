# 달력 벽 · 명세 없이 바로 구현

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 11:12 (한국 시간)
- 작업 설명(원문): `Build calendar page directly, no spec`
- 도구 호출: 모두 56회 (Read 30, Bash 24, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a senior product and visual designer who also builds front-end pages. Redesign one web page and build it yourself. There is no design spec in this task: go straight from the brief and the current draft to the finished page. Do not write a spec, a plan document or any other design document first.

1. Read these files first:
   - /home/claude/cover_design/experiment2/brief_common.md (shared brief)
   - /home/claude/cover_design/experiment2/brief_calendar.md (this theme's concept and the current draft)
   - Look at the current draft screenshots listed in the theme brief (open the PNG files with your Read tool).
   - /home/claude/cover_design/experiment2/IMPLEMENT.md: the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules. Where it mentions instructions, the brief and the current draft are your instructions, and you make every design decision yourself.
2. Keep the concept of this theme, and improve on the current draft wherever you judge it weak (hierarchy, rhythm, density, consistency, legibility, how the covers are presented). Write all on-screen copy in Korean. Do not invent facts or data that are not in the brief.
3. This is a controlled experiment. Do not open anything in /home/claude/cover_design/experiment2/specs/ or /home/claude/cover_design/experiment2/notes/, the other theme briefs, anything under /home/claude/cover_design/experiment/, or other people's pages, images or tmp folders. Keep your temporary files only in /home/claude/cover_design/experiment2/tmp/calendar_direct/.
4. Output name: calendar_direct. Write /home/claude/cover_design/experiment2/calendar_direct.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment2/tmp/calendar_direct/out.png, look at the result, and fix problems until the page has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for, followed by 3-5 lines on your most important design decisions.
````

## 최종 보고 (원문 그대로)

````text
calendar_direct 페이지를 완성했습니다. 렌더 결과는 1440 × 2800이고 오류, 헤드라인 넘침, 가로 넘침이 모두 없습니다. 표지 폭은 최소 104px이며 달력 칸과 오른쪽 칸의 바닥이 같은 높이에서 끝납니다.

- 원본: /home/claude/cover_design/experiment2/calendar_direct.src.html
- 빌드 결과: /home/claude/cover_design/experiment2/calendar_direct.html
- 렌더: /home/claude/cover_design/experiment2/tmp/calendar_direct/out.png

**구현하지 않은 것**
- 날짜 고르기, 검색 결과, 목록 보기 전환, 표 펼치기, CSV 내려받기 같은 동작은 만들지 않고 처음 연 상태만 그렸습니다.
- 형제 서고 링크는 브리프에 주소가 없어 `#`로 두었습니다.
- 모바일(390px)은 CSS만 넣었습니다. 한 단 구성이고 오늘 호가 먼저 오며, 칸 폭이 96px보다 좁아 달력 칸에는 표지 없이 날짜와 국면 띠만 보입니다. 렌더는 한 번 띄워 오류가 없는 것만 확인했습니다.

**해석한 부분**
- **여러 번 낸 날**: 달력 칸에는 그날 마지막 회차를 걸었습니다. 지표 값도 마지막 회차 기준이라 맞췄고, 모든 회차는 달력 아래 줄에 따로 펼쳤습니다.
- **달 이동 화살표**: 8월 기록이 없고 10월은 아직 시작 전이라 둘 다 비활성으로 그렸습니다.
- **10월 1일 칸**: "제32호"는 다음 순번이고 "내일"은 오늘을 9월 30일로 보고 계산했습니다.
- **오늘 강조색**: 최신 호 표지 배색에서 실행할 때 뽑고 명암비를 확인합니다. 9월 30일 기준으로 청록 #022B3B와 복숭아 #FCB8A5이고, 기준을 못 넘으면 기본 잉크색으로 바뀝니다.
- **데이터에서 계산한 값**: "9월 5일부터 모두 임시 기준"과 9월 기록 숫자입니다.
- **부속 문서 날짜**: 실제 값은 2026-09-08이고, 페이지의 날짜 표기에 맞춰 "9월 8일"로 적었습니다.

**주요 디자인 결정**
1. **겹쳐 쌓기 제거**: 초안의 겹친 표지와 표지 위 배지를 없앴습니다. 회차 수는 날짜 줄의 "3회" 표시로 옮겼고, 여러 번 낸 날의 회차는 "하루에 여러 번 낸 날" 줄에 순서대로 펼쳤습니다. 그래서 31개 표지가 하나도 가려지지 않고, 실행 사유(저녁, 수동 실행, 지연 실행 10:57, 안전판)도 함께 읽힙니다.
2. **국면 표시**: 칸마다 붙던 "C" 배지 대신 날짜 밑에 이어지는 색 띠를 쓰고, 국면이 바뀐 날에만 이름을 달았습니다. 9월 초의 미기록·걸친 판정에서 9월 6일 이후 C가 이어지는 흐름이 한눈에 보입니다.
3. **지표 합치기**: 초안의 지표 카드 3개를 "9월의 흐름" 한 장으로 합쳤습니다. 하루 한 칸 국면 줄과 세 차트가 같은 날짜 축을 쓰고, 기준선(+1.0%p, 0), 9월 18·19일 공백, 오늘 열을 표시했습니다.
4. **빈칸 활용과 오른쪽 칸 구성**: 달력 앞뒤의 빈칸(8/30–31, 10/2–3)에 범례와 9월 기록을 넣어 머리 부분을 비웠습니다. 오른쪽 칸은 오늘 호 → 지난 호 → 부속 문서 순으로 이어지며, 오늘 호는 최신 표지 배색의 바탕과 "브리핑 열기" 버튼을 씁니다.
5. **오른쪽 패널 정리**: 표지와 같은 헤드라인을 글로 되풀이하던 부분을 빼고, 표지에 없는 기준선, 전날 대비, 실행 방식만 남겼습니다. 갱신 방식과 알림 문구는 실제 문구 그대로 바닥글에 넣었습니다.
````
