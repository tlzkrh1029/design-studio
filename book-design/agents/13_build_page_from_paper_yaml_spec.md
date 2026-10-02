# 편집국 1면 · YAML 명세로 페이지 구현

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-10-01 00:02 (한국 시간)
- 작업 설명(원문): `Build page from paper YAML spec`
- 도구 호출: 모두 61회 (Read 32, Bash 19, Edit 6, Grep 2, Write 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer. Implement one web page exactly as a design spec describes.

1. Read /home/claude/cover_design/experiment/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The spec to implement is /home/claude/cover_design/experiment/specs/paper.yaml. It is your only design instruction. For data context you may also read /home/claude/cover_design/experiment/brief_common.md.
3. Do not open any other file in /home/claude/cover_design/experiment/specs/ and do not look at other experiment pages. This is a controlled experiment and each build must follow only its own spec.
4. Output name: paper_yaml. Write /home/claude/cover_design/experiment/paper_yaml.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment/out_paper_yaml.png, look at the result, and fix problems until the page matches the spec and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for.
````

## 최종 보고 (원문 그대로)

````text
보고 (paper_yaml)
1. 파일: /home/claude/cover_design/experiment/paper_yaml.src.html → 빌드본 paper_yaml.html, 렌더 /home/claude/cover_design/experiment/out_paper_yaml.png. 크기는 1440×4769이고, shot.py 결과 헤드라인 넘침·오류·가로 넘침이 모두 없습니다. 측정한 세로 위치는 명세 계산과 같습니다(메뉴 괘선까지 298px, 1면 y 338, 구역 사이 96px, 표지 32칸 4줄).
2. 구현하지 않은 것: hover 툴팁과 날짜 띠, 검색 실행·범위 목록·결과 띠, 연표 화살표 키 이동, 스크롤에 따른 현재 메뉴 갱신, 1024–1439px 비례 축소, 모바일 390px·태블릿 적응. 발행 목록 펼치기·접기는 동작하고, hover·focus는 CSS 스타일만 넣었습니다.
3. ΣSTABLECOIN.D 차트: '위 끝 = max(최대, 1.0) + 한 눈금'과 '눈금 3~5개'를 같이 지키려고 아래 끝만 반 눈금 단위로 넓혔습니다(범위 −2.5~+2, 눈금 −2~+2). BTC.D는 59.0~60.5(0.5 간격), BTCUSD는 −10~+30(10 간격)입니다.
4. 범례 'A BTC!'는 A 도장 뒤에 'BTC!'만 적는 것으로 읽었습니다. 걸친 판정 견본은 데이터의 첫 걸친 판정(C→D), '오늘'은 최신 국면 도장에 윤곽, '여러 번 발행'은 점 3개입니다.
5. {첫 기록 날짜}는 '9월 3일'로 적었습니다. 처음 연 상태의 현재 메뉴는 '1면'으로 두었습니다. '매크로 리스크 서고' 주소는 자료에 없어 링크를 '#'로 두었습니다.
6. 표 '전날 %p'에서 9/20은 9/17과 비교한 숫자만 적었습니다. 72px 칸에는 '9.17 대비'가 들어가지 않고, 바로 위 공백 줄('09.18 금 – 09.19 토 브리핑 없음')이 그 사정을 보여 줍니다.
7. Outfit 500·700·800은 표지 부품이 쓰므로 표지용으로만 링크했고, 페이지 글자에는 쓰지 않았습니다. 표지(.mz) 자체 그림자는 고치지 않았으므로, 감싼 div에 준 명세 그림자와 함께 겹쳐 보입니다.
8. '직전 호' 머리 줄은 글자와 hair 괘선 사이를 8px 띄웠습니다. '기록 현황'의 '여러 번 발행한 날' 값은 한 줄에 들어가지 않아 다음 줄에 오른쪽 정렬로 내렸습니다.
````
