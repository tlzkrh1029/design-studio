# canvas: 디자인 캔버스 「크립토 브리핑 표지 시안」

작업 결과를 한곳에서 비교하려고 만든 디자인 캔버스(https://claude.ai/artifact/JJpmYZbrGDqb3oqdkD4iwp, 비공개)의 프로젝트 파일입니다. 저장소에 넣은 것은 15번째 판 기준입니다. 캔버스는 9월 30일 21시 38분에 처음 게시했고, 단계마다 페이지와 보드를 더했습니다.

## 구성

- `project/canvas.json`: 캔버스 설정입니다. 페이지 5개, 보드 39개의 위치와 크기, 보드 사이에 둔 설명 메모, 보드 순서, 처음 열리는 페이지(`exp-night`)가 들어 있습니다.
- `project/*.dc.html`: 보드 하나에 파일 하나입니다. 화면 캡처 보드는 이미지 한 장(`/_blob/<id>`)을 담고, 명세 보드는 명세 본문을 글로 담습니다.

| 페이지 | 내용 |
| --- | --- |
| 표지 시안 | 서고에 적용한 모습, 모바일, 전체 표지 31장, 최근 5호, 그림 44종, 배색 12종과 설명 메모 4개 |
| 서고 테마 시안 | 밤의 가판대, 편집국 1면, 달력 벽 |
| 실험 · 밤의 가판대 / 편집국 1면 / 달력 벽 | 원래 시안, 1차 실험(YAML, JSON 명세와 결과), 2차 실험(명세 없이, 브리프+토큰, XML 태그 명세와 결과), 블라인드 평가 메모 |

캔버스의 메모 내용은 [docs/03](../docs/03_잡지형_표지_모듈.md), [docs/04](../docs/04_서고_테마_시안.md), [docs/05](../docs/05_명세_형식_실험_1차.md), [docs/06](../docs/06_명세_형식_실험_2차.md)에 옮겨 두었습니다.

## 보드와 이미지

`/_blob/<id>` 이미지는 캔버스 아티팩트 안에 저장되어 있어서 이 저장소에서는 열리지 않습니다. 같은 화면을 저장소의 아래 파일에서 볼 수 있습니다. 저장소의 파일은 보드보다 큰 배율(대부분 2배)로 캡처한 JPEG입니다.

| 페이지 | 보드 파일 | 제목 | 보드 크기 | 이미지 id | 저장소의 같은 화면 |
| --- | --- | --- | --- | --- | --- |
| 표지 시안 | `Main.dc.html` | 서고에 적용한 모습 | 1440×1120 | `e693c5af…` | `cover_design/final/page_top.jpg` |
| 표지 시안 | `Mobile.dc.html` | 모바일 | 390×844 | `9e3f2cfb…` | `cover_design/final/mobile.jpg` |
| 표지 시안 | `Shelf.dc.html` | 전체 표지 31장 | 1068×1659 | `0dd6958e…` | `cover_design/final/shelf2.jpg` (또는 같은 크기의 shelf.jpg) |
| 표지 시안 | `Covers.dc.html` | 표지 크게 보기 (최근 5호) | 2192×637 | `e54399c3…` | `cover_design/final/covers.jpg` |
| 표지 시안 | `Scenes.dc.html` | 그림 44종 (각 그림을 어울리는 호에 입혀 본 모습) | 2042×2512 | `318a1f4a…` | `cover_design/final/scenes2.jpg` (또는 같은 크기의 scenes.jpg) |
| 표지 시안 | `Schemes.dc.html` | 배색 12종 × 기준 색상 (9월 30일 표지로 시연) | 1142×2673 | `0b84ec64…` | `cover_design/final/schemes.jpg` |
| 서고 테마 시안 | `Night.dc.html` | 시안 1 · 밤의 가판대 | 1440×2928 | `73e18b7b…` | `cover_design/final/theme_night.jpg` |
| 서고 테마 시안 | `Paper.dc.html` | 시안 2 · 편집국 1면 | 1440×3155 | `d9193b79…` | `cover_design/final/theme_paper.jpg` |
| 서고 테마 시안 | `Calendar.dc.html` | 시안 3 · 달력 벽 | 1440×1718 | `1be897a1…` | `cover_design/final/theme_calendar.jpg` |
| 실험 · 밤의 가판대 | `ExpNightOrig.dc.html` | 원래 시안 | 1440×2928 | `73e18b7b…` | `cover_design/final/theme_night.jpg` |
| 실험 · 밤의 가판대 | `ExpNightYamlSpec.dc.html` | YAML 명세 (프롬프트) | 1440×4943 | 없음 | `cover_design/experiment/specs/`의 해당 명세 |
| 실험 · 밤의 가판대 | `ExpNightYamlResult.dc.html` | YAML 명세로 만든 결과 | 1440×4752 | `3732ce66…` | `cover_design/experiment/boards/res_night_yaml.jpg` |
| 실험 · 밤의 가판대 | `ExpNightJsonSpec.dc.html` | JSON 명세 (프롬프트) | 1440×4242 | 없음 | `cover_design/experiment/specs/`의 해당 명세 |
| 실험 · 밤의 가판대 | `ExpNightJsonResult.dc.html` | JSON 명세로 만든 결과 | 1440×4467 | `7c5af9a7…` | `cover_design/experiment/boards/res_night_json.jpg` |
| 실험 · 밤의 가판대 | `ExpNightDirectResult.dc.html` | 명세 없이 바로 만든 결과 | 1440×4937 | `32b4666c…` | `cover_design/experiment2/boards/res_night_direct.jpg` |
| 실험 · 밤의 가판대 | `ExpNightMdSpec.dc.html` | 브리프 + 토큰 (프롬프트) | 1440×3183 | 없음 | `cover_design/experiment2/specs/`의 해당 명세 |
| 실험 · 밤의 가판대 | `ExpNightMdResult.dc.html` | 브리프 + 토큰으로 만든 결과 | 1440×4691 | `826271d7…` | `cover_design/experiment2/boards/res_night_md.jpg` |
| 실험 · 밤의 가판대 | `ExpNightXmlSpec.dc.html` | XML 태그 (프롬프트) | 1440×5272 | 없음 | `cover_design/experiment2/specs/`의 해당 명세 |
| 실험 · 밤의 가판대 | `ExpNightXmlResult.dc.html` | XML 태그로 만든 결과 | 1440×6905 | `b9a45bb1…` | `cover_design/experiment2/boards/res_night_xml.jpg` |
| 실험 · 편집국 1면 | `ExpPaperOrig.dc.html` | 원래 시안 | 1440×3155 | `d9193b79…` | `cover_design/final/theme_paper.jpg` |
| 실험 · 편집국 1면 | `ExpPaperYamlSpec.dc.html` | YAML 명세 (프롬프트) | 1440×4983 | 없음 | `cover_design/experiment/specs/`의 해당 명세 |
| 실험 · 편집국 1면 | `ExpPaperYamlResult.dc.html` | YAML 명세로 만든 결과 | 1440×4769 | `e0785579…` | `cover_design/experiment/boards/res_paper_yaml.jpg` |
| 실험 · 편집국 1면 | `ExpPaperJsonSpec.dc.html` | JSON 명세 (프롬프트) | 1440×5317 | 없음 | `cover_design/experiment/specs/`의 해당 명세 |
| 실험 · 편집국 1면 | `ExpPaperJsonResult.dc.html` | JSON 명세로 만든 결과 | 1440×4569 | `6d780828…` | `cover_design/experiment/boards/res_paper_json.jpg` |
| 실험 · 편집국 1면 | `ExpPaperDirectResult.dc.html` | 명세 없이 바로 만든 결과 | 1440×5860 | `90c5c676…` | `cover_design/experiment2/boards/res_paper_direct.jpg` |
| 실험 · 편집국 1면 | `ExpPaperMdSpec.dc.html` | 브리프 + 토큰 (프롬프트) | 1440×3250 | 없음 | `cover_design/experiment2/specs/`의 해당 명세 |
| 실험 · 편집국 1면 | `ExpPaperMdResult.dc.html` | 브리프 + 토큰으로 만든 결과 | 1440×5102 | `8b16bf7b…` | `cover_design/experiment2/boards/res_paper_md.jpg` |
| 실험 · 편집국 1면 | `ExpPaperXmlSpec.dc.html` | XML 태그 (프롬프트) | 1440×5161 | 없음 | `cover_design/experiment2/specs/`의 해당 명세 |
| 실험 · 편집국 1면 | `ExpPaperXmlResult.dc.html` | XML 태그로 만든 결과 | 1440×6165 | `13894b4a…` | `cover_design/experiment2/boards/res_paper_xml.jpg` |
| 실험 · 달력 벽 | `ExpCalendarOrig.dc.html` | 원래 시안 | 1440×1718 | `1be897a1…` | `cover_design/final/theme_calendar.jpg` |
| 실험 · 달력 벽 | `ExpCalendarYamlSpec.dc.html` | YAML 명세 (프롬프트) | 1440×5013 | 없음 | `cover_design/experiment/specs/`의 해당 명세 |
| 실험 · 달력 벽 | `ExpCalendarYamlResult.dc.html` | YAML 명세로 만든 결과 | 1440×2687 | `f3e6072e…` | `cover_design/experiment/boards/res_calendar_yaml.jpg` |
| 실험 · 달력 벽 | `ExpCalendarJsonSpec.dc.html` | JSON 명세 (프롬프트) | 1440×5305 | 없음 | `cover_design/experiment/specs/`의 해당 명세 |
| 실험 · 달력 벽 | `ExpCalendarJsonResult.dc.html` | JSON 명세로 만든 결과 | 1440×1758 | `ad663c5d…` | `cover_design/experiment/boards/res_calendar_json.jpg` |
| 실험 · 달력 벽 | `ExpCalendarDirectResult.dc.html` | 명세 없이 바로 만든 결과 | 1440×2800 | `188fb9e7…` | `cover_design/experiment2/boards/res_calendar_direct.jpg` |
| 실험 · 달력 벽 | `ExpCalendarMdSpec.dc.html` | 브리프 + 토큰 (프롬프트) | 1440×3237 | 없음 | `cover_design/experiment2/specs/`의 해당 명세 |
| 실험 · 달력 벽 | `ExpCalendarMdResult.dc.html` | 브리프 + 토큰으로 만든 결과 | 1440×2003 | `15f8ab08…` | `cover_design/experiment2/boards/res_calendar_md.jpg` |
| 실험 · 달력 벽 | `ExpCalendarXmlSpec.dc.html` | XML 태그 (프롬프트) | 1440×5335 | 없음 | `cover_design/experiment2/specs/`의 해당 명세 |
| 실험 · 달력 벽 | `ExpCalendarXmlResult.dc.html` | XML 태그로 만든 결과 | 1440×3862 | `7d79d0bf…` | `cover_design/experiment2/boards/res_calendar_xml.jpg` |
