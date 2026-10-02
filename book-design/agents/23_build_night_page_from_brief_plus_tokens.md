# 밤의 가판대 · 브리프+토큰으로 페이지 구현

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 11:11 (한국 시간)
- 작업 설명(원문): `Build night page from brief+tokens`
- 도구 호출: 모두 49회 (Read 22, Bash 20, Edit 5, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer with a good eye for design. Build one web page from a design prompt.

1. Read /home/claude/cover_design/experiment2/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The design prompt is /home/claude/cover_design/experiment2/specs/night.md: a short design brief plus design tokens. It is your only design instruction. Use the token values as they are. Where the brief leaves a decision to you, make it yourself in line with the brief's purpose, mood and priorities. For data context you may also read /home/claude/cover_design/experiment2/brief_common.md.
3. This is a controlled experiment, and each build must follow only its own prompt. Do not open any other file in /home/claude/cover_design/experiment2/specs/, the screenshots in /home/claude/cover_design/experiment2/originals/, the theme briefs (brief_night.md, brief_paper.md, brief_calendar.md), anything under /home/claude/cover_design/experiment/, or other people's pages, images, notes or tmp folders. Keep your temporary files only in /home/claude/cover_design/experiment2/tmp/night_md/.
4. Output name: night_md. Write /home/claude/cover_design/experiment2/night_md.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment2/tmp/night_md/out.png, look at the result, and fix problems until the page follows the prompt and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for, including any tokens you added and why.
````

## 최종 보고 (원문 그대로)

````text
- 최종 파일: /home/claude/cover_design/experiment2/night_md.src.html → night_md.html, 렌더 tmp/night_md/out.png. 1440×4691, 가로 넘침·헤드라인 넘침·오류 없음.
- 확인: 첫 화면 900px 안에 표지·헤드라인·날짜·버튼·국면·지표 세 값이 다 들어옴(받침대 끝 788px). 선반 5개에 31호, 9/18·19 빈칸, 9/3·9/5·9/24 묶음, 다음 호 점선 칸. 국면 띠 29칸과 차트 셋의 날짜 열·주 구분선이 같은 x(오늘 칸과 점 1356px). 스포트라이트 켜짐(900ms)은 캡처 전에 끝남.
- 해석: BTC.D 작은 추세선의 기준선은 아랫줄 비교 기준인 전날 값(59.17)으로 그었다.
- 해석: --accent는 토큰 #F2B39F 그대로 썼다(pal(L).fr은 #FCB8A5). 다른 날만 그날 테두리색을 쓰고, 4.5:1 미만이면 --text-1 쪽으로 섞는다.
- 해석: 맨 위 선반 이름은 주 전체('이번 주 · 09.28–10.04 · 3호'), 맨 아래는 9/1을 빼고 '첫 주 · 09.02–09.06 · 8호'. 목록은 최신순이고, 같은 날은 늦은 회차가 위에 오며 날짜는 그 행에만.
- 해석: 부속 문서·갱신 방식은 바닥글의 접힌 링크(실제 문구 그대로). '매크로 리스크 서고'는 주소가 주어지지 않아 href="#". 검색 범위는 주 단위이고, 검색·결과 없음·31호 모두 보기는 동작까지 구현.
- 더한 토큰: --spot-rise 240px(원뿔 꼭짓점을 화면 위 밖에 둬 빛이 위에서 떨어지게), --spot-edge 0.4(빛의 바깥 40%를 어둠으로 녹이는 구간. 이게 없으면 가장 밝은 곳이 표지 뒤에 숨어 빛이 안 보였다).
- 더한 토큰: --icon 18px(선 아이콘), --col-date 104 / --col-phase 64 / --col-num 120 / --col-run 152px(목록 열 너비). 표지 높이와 원뿔 각도는 기존 토큰으로 계산했다.
````
