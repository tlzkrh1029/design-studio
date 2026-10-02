# 밤의 가판대 · JSON 명세로 페이지 구현

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-10-01 00:02 (한국 시간)
- 작업 설명(원문): `Build page from night JSON spec`
- 도구 호출: 모두 69회 (Read 28, Bash 25, Edit 13, Write 1, Grep 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer. Implement one web page exactly as a design spec describes.

1. Read /home/claude/cover_design/experiment/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The spec to implement is /home/claude/cover_design/experiment/specs/night.json. It is your only design instruction. For data context you may also read /home/claude/cover_design/experiment/brief_common.md.
3. Do not open any other file in /home/claude/cover_design/experiment/specs/ and do not look at other experiment pages. This is a controlled experiment and each build must follow only its own spec.
4. Output name: night_json. Write /home/claude/cover_design/experiment/night_json.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment/out_night_json.png, look at the result, and fix problems until the page matches the spec and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for.
````

## 최종 보고 (원문 그대로)

````text
night.json 명세로 페이지를 만들었습니다. 최종 렌더링은 1440×4467이고 오류, 헤드라인 넘침, 가로 넘침은 없습니다. 겹침, 잘림, 빈 자리도 없음을 직접 확인했습니다.
- 파일: /home/claude/cover_design/experiment/night_json.src.html, 빌드 결과 night_json.html, 렌더링 /home/claude/cover_design/experiment/out_night_json.png
- 강조색: pal(L).fr의 실제 값 #FCB8A5(바탕 대비 11.6)를 그대로 썼습니다. 명세 예시 #F2B39F와 조금 다릅니다. 4.5 미만이면 OKLCH 명도를 0.02씩 올리는 규칙은 코드에 넣었지만 이번 값에는 쓰이지 않았습니다.
- 차트 세로 범위: 데이터와 기준선을 포함해 반올림한 경계로 잡았고, 위아래 눈금선 라벨은 그 경계값입니다. 기준선이 틀 선에 붙지 않고 라벨 자리가 남도록 범위를 넓혔습니다(ΣSTABLECOIN.D −2.500~+2.000%p, BTCUSD −5.00~+25.00%). 점 크기 '2px·5px'은 반지름으로 읽었습니다. 지름 2px 점은 2px 선에 묻히기 때문입니다.
- 흐름 구역: 24px 머리 줄과 내용 사이에 8px을 더 두었습니다. 30일 칸의 강조 고리와 축 라벨이 머리 줄 글자에 닿지 않게 하려는 것입니다. 범례는 날짜 숫자 줄 아래 20px에 두었습니다. 칸 바로 아래 20px로 두면 회차 점, 날짜 숫자와 겹칩니다.
- 히어로 그림자: 큰 그림자는 받침 뒤에, 접지 그림자는 받침 위에 오도록 나눴습니다. 이렇게 해야 명세의 '받침 위 접지 그림자'가 보입니다.
- 모노 글꼴 안의 한글: IBM Plex Mono에는 한글이 없어서 한글 낱말만 Gothic A1로 바꿨습니다. 모노 글꼴의 넓은 공백과 자간을 막으려는 것입니다.
- 형제 서고 '매크로 리스크 서고': 브리프에 주소가 없어 링크 대상 없이 모양만 그렸습니다. 그래서 초점 순서에서도 빠집니다.
- 안내 구역: 명세에 구역 머리가 없어서 화면에 보이지 않는 h2만 두었습니다.
- 동작: hover, 툴팁, 검색(범위 선택, 네 가지 날짜 형식, 맞은 낱말 강조, 빈 결과), 표 펼치기, 목록 펼치기, 타임라인 화살표 이동, 스포트라이트 페이드를 구현했고 오류 없이 도는 것을 확인했습니다. 첫 화면 렌더링에는 드러나지 않습니다. 모바일 390px은 명세대로 렌더링하지 않았습니다.
````
