# 편집국 1면 · JSON 명세로 페이지 구현

- 단계: 1차 실험 (문서 `docs/05_명세_형식_실험_1차.md`)
- 시작 시각: 2026-10-01 00:02 (한국 시간)
- 작업 설명(원문): `Build page from paper JSON spec`
- 도구 호출: 모두 67회 (Read 25, Bash 25, Edit 10, Write 5, Grep 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer. Implement one web page exactly as a design spec describes.

1. Read /home/claude/cover_design/experiment/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The spec to implement is /home/claude/cover_design/experiment/specs/paper.json. It is your only design instruction. For data context you may also read /home/claude/cover_design/experiment/brief_common.md.
3. Do not open any other file in /home/claude/cover_design/experiment/specs/ and do not look at other experiment pages. This is a controlled experiment and each build must follow only its own spec.
4. Output name: paper_json. Write /home/claude/cover_design/experiment/paper_json.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment/out_paper_json.png, look at the result, and fix problems until the page matches the spec and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for.
````

## 최종 보고 (원문 그대로)

````text
paper_json 구현을 끝냈습니다.

1. 결과물: 원본 `/home/claude/cover_design/experiment/paper_json.src.html`, 빌드 `paper_json.html`, 렌더링 `/home/claude/cover_design/experiment/out_paper_json.png` (1440×4569). shot.py 기준 헤드라인 넘침과 오류가 없고, 가로 넘침도 없습니다. 모든 요소가 1296 폭 안에 있습니다.
2. 해석: 형제 서고 「매크로 리스크 서고」의 주소가 자료에 없습니다. 날짜 줄과 판권의 링크는 href="#" 자리로만 두었습니다.
3. 해석: 종이 결 `body::before`는 명세대로 position fixed입니다. inset 0 그대로면 전체 페이지 캡처에서 첫 1000px 아래에 결이 빠져서, 높이만 문서 높이에 맞췄습니다.
4. 해석: BTCUSD 패널의 「0 · D·E 전제선」 라벨을 선 바로 위에 두면 최신 점과 겹칩니다(값이 0선 위 16~20px에 붙어 있음). 겹칠 때만 선 바로 아래, D·E 전제 구간 안으로 내리는 규칙을 넣었습니다. ΣSTABLECOIN 라벨은 명세대로 선 위에 있습니다.
5. 해석: 검색 상자는 104+1+260+56이 폭 420을 넘어서, 전체 폭 420을 지키고 입력칸을 257로 줄였습니다. 오른쪽 여백을 4로 해서 자리 글자가 끝까지 보입니다.
6. 남은 점: 1면 지표 「9.125%」는 명세 크기(Oswald 46)에서 139px라 칸 안쪽 134px보다 5px 넓습니다. 오른쪽 여백을 조금 쓰지만 세로선까지 11px이 남아 겹치지 않고, 크기는 명세대로 두었습니다.
7. 해석: 1면의 「아래 48」을 2면까지의 간격으로 보았고, 나머지 면 사이는 64입니다. 부속 문서는 명세대로 제목과 설명만 두고 날짜는 넣지 않았습니다. Outfit은 표지 부품의 워드마크 때문에만 링크했습니다.
8. 구현: nav가 header 안에 있어야 해서 header 전체를 top −204로 sticky 처리해 메뉴 줄만 남게 했습니다. 연표·색인 툴팁, 접기, 검색과 결과 막대, 현재 면 표시, 연표 키보드 이동이 오류 없이 동작합니다. mobile_390은 구현하지 않았습니다.
9. 공개할 점: 스크래치패드를 다른 빌드와 같이 써서 파일 이름이 겹쳤습니다. 그 바람에 다른 페이지의 캡처 한 장을 실수로 열었고, 그쪽 measure.py를 한 번 덮어썼습니다(이후 그쪽에서 다시 씀). 본 캡처는 설계에 반영하지 않았고, 그 뒤 작업 파일은 pj_work/로 분리했습니다.
````
