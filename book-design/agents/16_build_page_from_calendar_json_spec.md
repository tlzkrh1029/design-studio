# 달력 벽 · JSON 명세로 페이지 구현

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-10-01 00:03 (한국 시간)
- 작업 설명(원문): `Build page from calendar JSON spec`
- 도구 호출: 모두 56회 (Bash 24, Read 22, Edit 7, Grep 1, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer. Implement one web page exactly as a design spec describes.

1. Read /home/claude/cover_design/experiment/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The spec to implement is /home/claude/cover_design/experiment/specs/calendar.json. It is your only design instruction. For data context you may also read /home/claude/cover_design/experiment/brief_common.md.
3. Do not open any other file in /home/claude/cover_design/experiment/specs/ and do not look at other experiment pages. This is a controlled experiment and each build must follow only its own spec.
4. Output name: calendar_json. Write /home/claude/cover_design/experiment/calendar_json.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment/out_calendar_json.png, look at the result, and fix problems until the page matches the spec and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for.
````

## 최종 보고 (원문 그대로)

````text
1. 페이지를 완성했습니다. 소스는 /home/claude/cover_design/experiment/calendar_json.src.html, 빌드 결과는 calendar_json.html, 렌더링은 /home/claude/cover_design/experiment/out_calendar_json.png이고 크기는 1440×1758입니다. shot.py 결과 헤드라인 넘침과 오류가 없고, 가로로 넘치지도 않습니다.
2. 명세 치수를 실제 렌더에서 재어 맞췄습니다: 본문 시작 y=80, 왼쪽·오른쪽 칸 모두 1,396이라 아래 끝이 맞음, 고른 날 카드 714(버튼 아래 끝 y=770), 지표 카드 666, 격자 1012×1170, 칸 136×226, 칸 표지 120.
3. 구현하지 않은 것: 검색 결과 창, 날짜 인식, 형광펜 표시, 차트 hover 안내선, 모바일 390 레이아웃. 고르기, 이전·다음 호, 회차 전환, 달력|목록 전환과 목록 표, 도움말, 격자·띠·표 키보드 이동은 구현했고 오류 없이 동작합니다.
4. 형제 서고 링크: 받은 자료에 기존 서고의 링크 값이 없어서 href="#" 자리표시로 두었습니다. 실제 주소를 넣어야 합니다.
5. 표지 모듈이 안에서 Oswald와 Outfit 800을 써서 표지용으로만 링크했습니다. 페이지 글자에는 쓰지 않습니다. 표지 자체 그림자(.mz)는 그대로 두고, 명세 그림자는 감싼 div에 주었습니다. 오늘 색은 명세 값 #F2B39F를 썼습니다(실제 9/30 표지 테두리는 #FCB8A5).
6. Σ 차트의 y 라벨 '+1.0%p'와 '−2.5%p'는 11px mono에서 폭이 약 42px라, 명세대로 x=36에 오른쪽 정렬하면 카드 여백 쪽으로 약 6px 나갑니다. 잘리지는 않습니다. 변화량 축 라벨에도 부호를 붙였습니다('+25%').
7. 그 밖에 해석한 부분: 머리 구분선은 간격 8에 자체 좌우 여백 8을 더했습니다. 범례 줄 caption은 16px 줄에 맞춰 12/16으로 했습니다. mono 글자 속 한글은 글자 단위로 Gothic A1로 대체했고, 전부 한글인 '기록 없음'만 통째로 Gothic A1입니다. 목록 보기에서 run 값이 없는 호에는 공용 runLabel의 '실행 기록 없음' 태그가 붙습니다.
````
