# 달력 벽 · YAML 명세로 페이지 구현

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-10-01 00:03 (한국 시간)
- 작업 설명(원문): `Build page from calendar YAML spec`
- 도구 호출: 모두 73회 (Read 35, Bash 29, Edit 5, Write 3, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer. Implement one web page exactly as a design spec describes.

1. Read /home/claude/cover_design/experiment/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The spec to implement is /home/claude/cover_design/experiment/specs/calendar.yaml. It is your only design instruction. For data context you may also read /home/claude/cover_design/experiment/brief_common.md.
3. Do not open any other file in /home/claude/cover_design/experiment/specs/ and do not look at other experiment pages. This is a controlled experiment and each build must follow only its own spec.
4. Output name: calendar_yaml. Write /home/claude/cover_design/experiment/calendar_yaml.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment/out_calendar_yaml.png, look at the result, and fix problems until the page matches the spec and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for.
````

## 최종 보고 (원문 그대로)

````text
calendar_yaml 페이지를 완성했습니다. 렌더링은 1440 × 2687이고 가로 넘침은 없으며, shot.py가 헤드라인 넘침·오류를 보고하지 않았습니다. 명세 높이와도 맞습니다: 주 버튼 아래 끝 y 853.6(명세 854), 달력 카드 1222, 날 카드 950.6(약 951), 오른쪽 칸 합계 1226.6(약 1227).
- 구현하지 않음: mobile_390 규칙 전부(데스크톱 전용).
- 표지 그림자: 감싼 div에 cover_s / cover_l. .mz는 고칠 수 없어 표지 모듈 자체 그림자도 그대로 남아 있음. 고른 날 표지 높이는 모듈 비율대로 517.6px(명세 518).
- 차트 세로선: 고른 날 세로선이 기준선 라벨과 겹치는 곳(예: 9/30)에서는 라벨 위아래로 끊음. 날짜 태그는 그림 영역 안에 두고, 라벨과 겹치면 기준선 아래로 내림.
- 링크: '부속 문서'는 유일한 부속 문서(UNI·ARB 관통 해부) 주소. '갱신 방식'·'매크로 리스크 서고'는 명세에 주소가 없어 빈 링크(#).
- 작은 해석: 머리띠 툴팁은 화면 위로 잘리지 않게 아래로 띄움. 브랜드는 포커스 순서 두 번째 자리를 위해 맨 위로 가는 링크. '점선'은 dashed로 그림. '9월 기록' 줄 구분선은 줄 높이 36 안에 넣어 카드 252px.
- 정적 화면 밖으로도 구현: 고르기, 회차 전환, 달력·띠 키보드 이동, 검색, 목록 펼치기, 차트 호버, 300ms 스크롤. 각 상태를 눌러 확인했고 오류 없음.
파일 (/home/claude/cover_design/experiment/):
- calendar_yaml.src.html
- calendar_yaml.html
- out_calendar_yaml.png
````
