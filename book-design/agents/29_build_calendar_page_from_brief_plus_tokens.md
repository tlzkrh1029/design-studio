# 달력 벽 · 브리프+토큰으로 페이지 구현

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 11:12 (한국 시간)
- 작업 설명(원문): `Build calendar page from brief+tokens`
- 도구 호출: 모두 68회 (Read 32, Bash 27, Edit 6, Grep 1, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer with a good eye for design. Build one web page from a design prompt.

1. Read /home/claude/cover_design/experiment2/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The design prompt is /home/claude/cover_design/experiment2/specs/calendar.md: a short design brief plus design tokens. It is your only design instruction. Use the token values as they are. Where the brief leaves a decision to you, make it yourself in line with the brief's purpose, mood and priorities. For data context you may also read /home/claude/cover_design/experiment2/brief_common.md.
3. This is a controlled experiment, and each build must follow only its own prompt. Do not open any other file in /home/claude/cover_design/experiment2/specs/, the screenshots in /home/claude/cover_design/experiment2/originals/, the theme briefs (brief_night.md, brief_paper.md, brief_calendar.md), anything under /home/claude/cover_design/experiment/, or other people's pages, images, notes or tmp folders. Keep your temporary files only in /home/claude/cover_design/experiment2/tmp/calendar_md/.
4. Output name: calendar_md. Write /home/claude/cover_design/experiment2/calendar_md.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment2/tmp/calendar_md/out.png, look at the result, and fix problems until the page follows the prompt and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for, including any tokens you added and why.
````

## 최종 보고 (원문 그대로)

````text
calendar_md 페이지를 만들었습니다. 1440×2003으로 렌더링했고 헤드라인 넘침·오류·가로 넘침이 없습니다. 첫 화면 900px 안에 최신 표지·헤드라인·국면·'브리핑 펼치기'(아래끝 873px)와 달력 머리·첫 두 주(아래끝 668px)가 들어갑니다.

1. 최종 파일은 /home/claude/cover_design/experiment2/calendar_md.src.html(빌드 결과 calendar_md.html)이고, 렌더링은 tmp/calendar_md/out.png에 1440×2003으로 저장했습니다. 표지는 108×158.8과 300×441.2이고, 점선은 10/1 한 곳뿐입니다.
2. 월 이동 화살표는 8월과 10월에 호가 없어서 둘 다 --text-disabled로 꺼 두었습니다. '매크로 리스크 서고'는 자료에 주소가 없어 href="#"으로 자리만 잡았습니다.
3. 고른 날 카드의 지표 세 줄은 흐름 카드의 세 차트와 같은 지표로 맞췄습니다. BTC.D는 전날 대비, ΣSTABLECOIN.D 1개월은 점유율 9.125%를 보조 글로, BTCUSD 1개월은 숫자만 둡니다. 실행 기록이 없는 회차의 탭은 '{n}회'만 씁니다.
4. 흐름 카드의 날짜 눈금(1~30)은 띠 바로 아래 한 줄로 두어 띠와 세 차트가 함께 씁니다. y 눈금은 차트마다 두 개씩 비어 있는 첫 열 안쪽에 두었습니다. 왼쪽 열의 '현재 값'은 최신 호 값입니다.
5. 고른 날은 흐름 카드에서 세로띠, 띠 칸의 --accent 링, 굵은 날짜, 차트 점으로 표시됩니다. 9/18·19의 띠 칸은 --line-strong 실선 윤곽만 두었고, 9/1은 띠 칸을 비워 두었습니다.
6. 표지 .mz에 내장된 그림자는 고칠 수 없어서 그대로 두고, 표지를 감싼 div에 토큰 그림자를 따로 얹었습니다. 그래서 그림자가 겹쳐 브리프의 '얕은 그림자'보다 다소 짙게 보입니다.
7. 흐름 카드 제목 옆에 상태 규칙을 옮긴 한 줄 '하루 한 칸 · 여러 번 발행한 날은 그날 마지막 회차 기준'을 더했습니다.
8. 동작으로는 날 고르기(달력·띠·차트·목록, --dur 페이드), 회차 탭, 검색 세 경우(날짜, 낱말, 결과 없음), 목록 보기와 CSV 내려받기, 갱신 방식 펼치기, 툴팁을 구현했고, 시험 스크립트에서 오류 없이 돌았습니다.
9. 더한 토큰은 두 개입니다. --next-dash: 4 3은 다음 호 점선의 무늬 값이 토큰에 없어서, --tip-max-w: 280px은 긴 헤드라인 툴팁을 줄바꿈하려고 더했습니다.
````
