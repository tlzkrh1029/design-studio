# lcan-design 시안 목록

이 폴더에는 lcan-design에서 비교한 시안을 하나씩 폴더로 둡니다. 시안마다 비교 화면(`index.html`), 그 화면을 만드는 `build.py`, 렌더링 점검 스크립트 `shot.py`, 점검 캡처(`screenshots/`), 기록(`notes.md`)이 있습니다.

| 폴더 | 내용 | 아티팩트 | 만든 AI와 날짜 | 결과 |
| --- | --- | --- | --- | --- |
| [beige-token-options/](beige-token-options/notes.md) | 첫 비교. 요소 023, 042, 072에 artifact-design의 베이지 스타일을 적용한 세 안(A 먹 강조·평면, B 먹 강조·그림자, C 보라 강조·평면)과 경고색 두 안(금색, 주황)을 원본과 나란히 놓았습니다. | https://claude.ai/artifact/9aF7DUrSwCad8Tf8x8XQi5 | Claude, 2026-10-29 | 사용자가 모두 고르지 않았습니다. 원본이 낫다고 했습니다. |
| [original-contrast-fix/](original-contrast-fix/notes.md) | 둘째 비교. 같은 요소 세 개를 원본과, 글자 명암비가 4.5:1에 못 미치는 토큰 여섯 개만 보정한 판으로 나란히 놓았습니다. | https://claude.ai/artifact/MGcT6Gxfi7gFNR3912sdx3 | Claude, 2026-10-29 | 사용자가 보정판을 기본으로 골랐습니다. 값은 [../lcan-theme.css](../lcan-theme.css)로 옮겼습니다. |

두 아티팩트 링크는 소유자만 열 수 있는 비공개 링크이며, 저장소에 내보낸 날짜는 둘 다 2026-10-29입니다.

## 여는 방법

- `index.html`은 일반 브라우저에서 바로 열립니다. 화면 둘레의 글꼴은 Google Fonts에서 불러오므로, 인터넷에 연결되어 있지 않으면 기기의 글꼴로 보입니다. 요소 칸의 글꼴은 원본처럼 웹 글꼴을 불러오지 않습니다.
- `python3 build.py`를 실행하면 `upstream/`의 원본과 테마 파일로 `index.html`을 다시 만듭니다. `index.html`은 직접 고치지 않습니다.
- `python3 shot.py --fonts <node_modules/@fontsource 폴더>`를 실행하면 1440px와 390px에서 렌더링해 점검하고, 캡처를 `screenshots/`에 둡니다. Playwright가 필요하고, 글꼴은 `npm install @fontsource/ibm-plex-sans-kr @fontsource/noto-serif-kr @fontsource/ibm-plex-mono`로 받은 파일을 씁니다.

내보낸 시안은 고치지 않습니다. 시안을 고친 새 판은 새 폴더에 둡니다(맨 위 AGENTS.md의 '시안 내보내기').
