# 밤의 가판대 · YAML 명세로 페이지 구현

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-10-01 00:02 (한국 시간)
- 작업 설명(원문): `Build page from night YAML spec`
- 도구 호출: 모두 60회 (Read 30, Bash 23, Edit 5, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer. Implement one web page exactly as a design spec describes.

1. Read /home/claude/cover_design/experiment/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The spec to implement is /home/claude/cover_design/experiment/specs/night.yaml. It is your only design instruction. For data context you may also read /home/claude/cover_design/experiment/brief_common.md.
3. Do not open any other file in /home/claude/cover_design/experiment/specs/ and do not look at other experiment pages. This is a controlled experiment and each build must follow only its own spec.
4. Output name: night_yaml. Write /home/claude/cover_design/experiment/night_yaml.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment/out_night_yaml.png, look at the result, and fix problems until the page matches the spec and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for.
````

## 최종 보고 (원문 그대로)

````text
1. 최종 파일: /home/claude/cover_design/experiment/night_yaml.src.html. 빌드 결과 night_yaml.html, 렌더링 /home/claude/cover_design/experiment/out_night_yaml.png. 크기 1440×4752이고 가로 넘침, 표지 헤드라인 넘침, 오류 모두 없다. 표지·받침·29칸·선반·카드·목록 열의 좌표는 DOM으로 재어 명세 수치와 맞췄다.
2. 강조색은 규칙대로 최신 호 표지 테두리색 pal(L).fr를 받아 #FCB8A5를 썼다. surface_2 대비 9.9라 보정은 없었다. 토큰의 #F2B39F는 값을 못 받을 때 쓰는 대체값으로만 두었다.
3. 해석: 빛기둥의 "흐림 32"는 그림자 표기와 같은 흐림 반경으로 보고 CSS blur(16px)로 옮겼다. 로고 불빛은 0 0 8px glow로 했다.
4. 해석(차트): y 눈금 글자와 선이 겹치지 않도록 368 폭 안 왼쪽 40을 눈금 자리로 두었다. x 눈금은 176 플롯 아래에 두었다. 격자 3줄은 기준선과 겹치지 않는 값으로 골랐다(BTCUSD 카드는 5·15·25).
5. 해석(겹침 수정): 가판대 첫 줄 뒤벽 빛은 표지 위 40에서 시작하는데 묶음 머리는 표지 위 24에 있어 제목을 가로질렀다. 그래서 첫 줄만 제목과 겹치는 16px을 잘랐다. 국면 띠 빈 칸의 점선은 명세에 무늬가 없어 4/4로, 범례 견본은 3/2로 했다.
6. 해석: "서고 안내" 구역은 명세에 메타·안내가 없어 제목만 있는 구역 머리로 두었다. 부속 문서 행은 명세대로 제목만 넣었다. 갱신 방식 항목은 원문을 그대로 키(06:10 등)와 문장의 두 칸 목록으로 옮겼다.
7. 없는 값: "매크로 리스크 서고"는 주소가 없어 href="#"(이동 없음)로 두었다. Outfit은 표지 모듈이 쓰는 굵기만 링크했고 페이지 글자에는 쓰지 않았다. 오늘은 안내대로 2026-09-30으로 고정했다.
8. 동작 구현: 검색(범위, 날짜 형식, 결과 판, 목록 검색 모드), 표 펼치기, 목록 펼치기, 국면 칸 툴팁과 화살표 이동, 메뉴 현재 구역 표시. 오류 없이 도는 것을 확인했다. 차트 hover 툴팁과 모바일 390 적응은 구현하지 않았다.
9. 참고: 공유 scratchpad에서 파일 이름(x2.png 등)이 다른 병렬 작업과 겹쳐 다른 페이지의 크롭이 한 번 열렸다. 구현에는 전혀 쓰지 않았고, 그 뒤로는 전용 폴더(scratchpad/night_yaml_private)에서만 작업했다.
````
