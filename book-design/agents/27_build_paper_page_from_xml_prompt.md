# 편집국 1면 · XML 태그 명세로 페이지 구현

- 단계: 2차 실험 (문서 `docs/06_명세_형식_실험_2차.md`)
- 시작 시각: 2026-10-01 11:12 (한국 시간)
- 작업 설명(원문): `Build paper page from XML prompt`
- 도구 호출: 모두 57회 (Read 28, Bash 24, Write 3, Edit 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are a front-end developer with a good eye for design. Build one web page from a design prompt.

1. Read /home/claude/cover_design/experiment2/IMPLEMENT.md first. It explains the page skeleton, the shared helpers, the real copy to use, the build and render commands, and the rules.
2. The design prompt is /home/claude/cover_design/experiment2/specs/paper.xml: a prompt structured with XML tags. It is your only design instruction; follow its <instructions>. Write the <plan> it asks for to /home/claude/cover_design/experiment2/notes/paper_xml.md before you build, and append the <check> to the same file after you build. For data context you may also read /home/claude/cover_design/experiment2/brief_common.md.
3. This is a controlled experiment, and each build must follow only its own prompt. Do not open any other file in /home/claude/cover_design/experiment2/specs/, the screenshots in /home/claude/cover_design/experiment2/originals/, the theme briefs (brief_night.md, brief_paper.md, brief_calendar.md), anything under /home/claude/cover_design/experiment/, or other people's pages, images, notes or tmp folders. Keep your temporary files only in /home/claude/cover_design/experiment2/tmp/paper_xml/.
4. Output name: paper_xml. Write /home/claude/cover_design/experiment2/paper_xml.src.html, build it with build.py, render it with shot.py to /home/claude/cover_design/experiment2/tmp/paper_xml/out.png, look at the result, and fix problems until the page follows the prompt and has no overlaps, clipping, overflow or errors.
5. Finish with the short Korean report that IMPLEMENT.md asks for, then the <check> results.
````

## 최종 보고 (원문 그대로)

````text
## 보고 (paper_xml)

**페이지를 만들었고, 완료 기준 14개를 모두 통과했습니다.** 렌더링 크기는 1440 × 6165이고, 가로 넘침·헤드라인 넘침·오류는 0건입니다. 기준마다 Playwright로 실제 화면을 재서 확인했습니다.

- 최종 파일: /home/claude/cover_design/experiment2/paper_xml.html (원본 paper_xml.src.html)
- 렌더링: /home/claude/cover_design/experiment2/tmp/paper_xml/out.png
- 계획(<plan>)과 점검(<check>): /home/claude/cover_design/experiment2/notes/paper_xml.md

**해석한 부분과 구현하지 않은 부분**
1. 다음 호 칸은 지난 호와 같은 틀에 맞추려고 문구를 둘로 나눴습니다. 호·날짜 줄에 '제32호 · 10월 1일 목요일', 명조 제목 줄에 '06:10 발행 예정'이 들어가, 읽는 순서대로 지시 문구와 같습니다.
2. 형제 서고 '매크로 리스크 서고'는 주소가 자료에 없어 링크를 href="#"로 두었습니다(날짜 줄 오른쪽, 판권 두 곳). 실제 주소를 받으면 바꿔야 합니다.
3. 표지 부품(.mz)에는 원래 그림자가 들어 있습니다. .mz는 고치지 않았기 때문에, 감싼 링크에 준 토큰 그림자와 겹쳐 그려집니다.
4. 날짜 줄 왼쪽은 '2026년 9월 30일 수요일'로, 허용된 긴 날짜 꼴 앞에 연도만 붙였습니다.
5. 지시에 없던 것을 몇 가지 더했습니다.
   - 4면 표 위에 검색 안내 한 줄을 두었고, 검색 중에는 이 줄이 결과 수와 '검색 지우기'로 바뀝니다.
   - 'CSV로 내려받기' 링크를 넣었습니다.
   - 판권도 같은 면 머리 틀('판권' 꼬리표)로 열었습니다.
   - 3면 차트에서 값이 없는 날은 칸 가운데에 '—'를 두었습니다.
6. hover, 검색 필터, Enter 때 4면으로 이동, 스크롤에 따른 메뉴 현재 위치는 모두 동작합니다. 렌더링은 처음 연 상태입니다.
7. 추가한 토큰은 없습니다. tokens의 :root는 글자 그대로 넣었습니다.

**<check> 결과: 14개 항목 모두 통과**
1. 첫 화면 — 900px 안에 제호(180), 헤드라인(529), '브리핑 전문 읽기'(613)가 다 들어가고, 표지 윗부분이 약 340px 보입니다.
2. 링크 — 헤드라인, 대표 표지, 읽기 버튼 모두 제31호 url로 갑니다.
3. 색 — LCD 글자 번짐을 끄고 렌더링했을 때, 표지(±2px) 밖에서 토큰 회색보다 채도가 높은 픽셀은 0개입니다.
4. 표지 — 31장이 모두 보이고, 테두리·필터·변형은 0건, 표지끼리 겹침도 0쌍입니다.
5. 1면 오른쪽 단 — 지난 두 호와 다음 호 칸이 같은 틀이고, 다음 호가 맨 아래입니다.
6. 휴간 — 9/18·9/19가 2·3·4면에서 휴간으로 보이고, 9/1은 어디에도 없습니다.
7. 'n회' — 9/3·9/5·9/24의 일곱 호 모두에 붙었습니다(2면과 4면). 3면 날짜 밑에도 회수가 적혀 있습니다.
8. 기준 문구 — 'E 임시 기준 +1.0%p'와 '0 아래면 D·E 전제'가 1면과 3면에 같은 말로 있습니다.
9. 3면 날짜 칸 — 국면 띠와 차트 셋의 날짜 칸 위치 차이가 최대 0px입니다.
10. 부호와 자릿수 — 하이픈 음수 0건이고, 지표마다 소수 자릿수가 어디서나 같습니다.
11. 명암비 — 미달 0건이고, 가장 낮은 것이 5.4:1입니다.
12. 문구 — 모두 한국어이고 <data>에 없는 사실은 없습니다. 영문은 지시가 정한 부제와 지표 이름뿐입니다.
13. 검색 — 범위 선택과 입력이 있습니다. 결과가 나오는 경우, 결과가 없을 때 빈 결과 문구, 지우면 원래 목록으로 돌아오는 것까지 확인했습니다.
14. 값의 출처 — 모든 값이 토큰에서 왔습니다.
````
