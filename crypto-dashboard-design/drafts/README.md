# drafts: 크립토 시장 화면의 시안 원본

이 폴더에는 Claude 아티팩트로 만든 시안의 원본과, 일반 브라우저에서 열리는 미리보기를 둡니다. 원래 아티팩트는 소유자만 열 수 있는 비공개 링크이므로, 다른 AI와 사람은 이 폴더의 파일로 시안을 봅니다. 내보내기 규칙은 저장소 맨 위 [AGENTS.md](../../AGENTS.md)의 '시안 내보내기' 절에 있습니다.

| 시안 | 여는 파일 | 원래 아티팩트 | 아티팩트 마지막 수정 | 내보낸 날짜 |
| --- | --- | --- | --- | --- |
| 대시보드 대안 시안 5종(보드 7개) | [dashboard-alternatives/preview/index.html](dashboard-alternatives/preview/index.html) | [WmKCNfQZsKopTe8FsaoBY4](https://claude.ai/artifact/WmKCNfQZsKopTe8FsaoBY4) | 2026-09-27 | 2026-10-03 |

## 여는 방법

- GitHub 웹 화면에서는 HTML 파일이 코드로만 보입니다. 저장소를 내려받은 뒤(Code → Download ZIP) '여는 파일'을 브라우저로 엽니다.
- 글꼴(IBM Plex Sans KR, IBM Plex Mono, Noto Serif KR)은 Google Fonts에서 받으므로, 인터넷에 연결되어 있어야 원래 글꼴로 보입니다.
- 이 시안은 Claude 디자인 캔버스로 만들었습니다. `source/`의 원본(`canvas.json`과 보드마다 하나씩 있는 `*.dc.html`)은 캔버스의 런타임(`support.js`)이 있어야 열리며, 런타임은 저장소에 넣지 않았습니다. 그래서 `preview/`에 런타임 없이 열리는 미리보기를 두었습니다.
- 미리보기는 원본에서 `x-dc` 감싸개와 런타임 스크립트만 뺀 것이며, 보드의 내용과 스타일은 바꾸지 않았습니다. 이 시안의 보드에는 동작하는 스크립트가 없으므로, 미리보기도 원본과 같은 화면을 보여 줍니다.

## 렌더링 점검(2026-10-03)

- 보드 일곱 개를 각자의 보드 크기로 열어, 스크립트 오류와 가로 넘침, 잘림이 없음을 확인했습니다. 미리보기 목록(`preview/index.html`)도 데스크톱(1440px)과 모바일(390px) 폭에서 가로로 넘치지 않았습니다.
- 점검 환경에서는 Google Fonts에 접속할 수 없어서, 같은 글꼴을 npm의 @fontsource 패키지에서 받아 적용한 뒤 확인했습니다.
