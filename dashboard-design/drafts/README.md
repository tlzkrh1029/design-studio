# drafts: 섹터 모니터링 화면의 시안 원본

이 폴더에는 Claude 아티팩트로 만든 시안 가운데 사용자가 고른 네 개의 원본을 둡니다. 원래 아티팩트는 소유자만 열 수 있는 비공개 링크이므로, 다른 AI와 사람은 이 폴더의 파일로 시안을 봅니다. 내보내기 규칙은 저장소 맨 위 [AGENTS.md](../../AGENTS.md)의 '시안 내보내기' 절에 있습니다.

| 시안 | 여는 파일 | 원래 아티팩트 | 아티팩트 마지막 수정 | 내보낸 날짜 |
| --- | --- | --- | --- | --- |
| 섹터 전환 터미널 | [sector-rotation-terminal/index.html](sector-rotation-terminal/index.html) | [6591K5Cr3HAFUAKMXav4in](https://claude.ai/artifact/6591K5Cr3HAFUAKMXav4in) | 2026-09-27 | 2026-10-03 |
| 거래소 상장 표시 시안(시안 A·B·C) | [exchange-listing-display/preview/index.html](exchange-listing-display/preview/index.html) | [DQdQzpqxnuHJE5wYtTkEgH](https://claude.ai/artifact/DQdQzpqxnuHJE5wYtTkEgH) | 2026-09-27 | 2026-10-03 |
| 돌파 장부 | [breakout-ledger/index.html](breakout-ledger/index.html) | [GAHGNoGtA86SW1eiWBahft](https://claude.ai/artifact/GAHGNoGtA86SW1eiWBahft) | 2026-09-27 | 2026-10-03 |
| 돌파 벽 | [breakout-wall/index.html](breakout-wall/index.html) | [6xTRHAErUfaFX579aDCtCS](https://claude.ai/artifact/6xTRHAErUfaFX579aDCtCS) | 2026-09-27 | 2026-10-03 |

네 시안 모두 블룸버그 터미널 같은 스타일로 만든 화면입니다. 이 스타일은 이 작업의 여러 디자인 스타일 가운데 하나의 사례이며, 기준선이 아닙니다([bloomberg-style/](../bloomberg-style/README.md) 참고).

## 여는 방법

- GitHub 웹 화면에서는 HTML 파일이 코드로만 보입니다. 저장소를 내려받은 뒤(Code → Download ZIP) '여는 파일'을 브라우저로 엽니다.
- 글꼴(IBM Plex Mono, Nanum Gothic Coding, IBM Plex Sans KR)은 Google Fonts에서 받으므로, 인터넷에 연결되어 있어야 원래 글꼴로 보입니다.
- 섹터 전환 터미널, 돌파 장부, 돌파 벽은 HTML 파일 하나로 이루어져 있고 Claude 전용 기능을 쓰지 않으므로, 원본을 그대로 엽니다. 색 규약 같은 화면 설정은 그 화면을 연 브라우저에만 저장됩니다.
- 거래소 상장 표시 시안은 Claude 디자인 캔버스로 만들었습니다. `source/`의 원본(`canvas.json`과 보드마다 하나씩 있는 `*.dc.html`)은 캔버스의 런타임(`support.js`)이 있어야 열리며, 런타임은 저장소에 넣지 않았습니다. 그래서 `preview/`에 런타임 없이 열리는 미리보기를 두었습니다. 미리보기는 원본에서 `x-dc` 감싸개와 런타임 스크립트만 뺀 것이며, 보드 세 개(시안 A, B, C)를 원래 크기(1520×740)로 보여 줍니다. 이 시안의 보드에는 동작하는 스크립트가 없으므로, 미리보기도 원본과 같은 화면을 보여 줍니다.

## 내보내며 바꾼 것

- 섹터 전환 터미널의 데이터 설명과 코드 주석에 들어 있던 비공개 저장소의 이름과 주소를 '비공개 저장소'로 바꿨습니다. 그 밖의 내용은 아티팩트와 같습니다.
- 돌파 장부, 돌파 벽, 거래소 상장 표시 시안의 원본은 바꾸지 않았습니다.

## 데이터

각 시안의 아래쪽에 있는 데이터 설명을 정리하면 다음과 같습니다.

| 시안 | 실제 데이터 | 예시 데이터 |
| --- | --- | --- |
| 섹터 전환 터미널 | 구성종목 상위 10개(stockanalysis.com, 2026-09-25~26 기준), 거래소 상장 점(2026-09-27 12:34 UTC에 수집한 거래소 목록과 대조한 값) | 히트맵 수치, 비율선, RRG 국면, 신호 |
| 거래소 상장 표시 시안 | 구성종목과 비중(stockanalysis.com, 2026-09-26 기준) | 상장 여부와 커버리지. 화면의 설명은 상장 플래그만 예시라고 밝히고, 히트맵 수치와 비율선, RRG 국면, 신호에 대해서는 따로 설명하지 않습니다. |
| 돌파 장부, 돌파 벽 | 칸에 놓인 종목과 비중(stockanalysis.com, ETF마다 2026-08-13~09-26 기준) | 가격, 그리고 가격에서 계산한 돌파·이탈·경과일·실패 |

## 렌더링 점검(2026-10-03)

- 섹터 전환 터미널, 돌파 장부, 돌파 벽은 데스크톱(1440×900)과 모바일(390×844) 폭에서, 거래소 상장 표시 시안의 보드는 보드 크기(1520×740)에서 열었습니다. 스크립트 오류는 없었습니다.
- 점검 환경에서는 Google Fonts에 접속할 수 없어서, 같은 글꼴을 npm의 @fontsource 패키지에서 받아 적용한 뒤 확인했습니다.
- 원본에 있는 다음 문제는 내보내면서 고치지 않았습니다. 고칠지는 사용자가 정합니다([HANDOFF.md](../HANDOFF.md) 4절).
  - 섹터 전환 터미널: 모바일 폭(390px)에서 매트릭스 제목 줄('SECTOR ROTATION MATRIX'와 기간 표시)이 줄바꿈되지 않아, 화면이 가로로 15px 넘칩니다.
  - 거래소 상장 표시 시안: 세 보드 모두 높이가 740px로 고정되어 있어, 넘친 내용이 아래쪽에서 잘립니다(시안 A 47px, B 111px, C 21px). 시안 B에서는 오른쪽 구성종목 표의 9번째 줄이 아래쪽 상태 표시줄과 겹칩니다.

## 내보내지 않은 시안

- 섹터 전환 매트릭스 v2와 v3, 돌파 지도(시안 v6)는 사용자가 내보내지 않기로 정했습니다(2026-10-02). 돌파 지도(시안 v6)의 화면 캡처는 [bloomberg-style/](../bloomberg-style/README.md)에 있습니다.
- 대시보드 대안 시안 5종은 내용이 크립토 시장 화면이어서 작업 3으로 옮겼고, [crypto-dashboard-design/drafts/](../../crypto-dashboard-design/drafts/README.md)로 내보냈습니다.
