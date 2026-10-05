# design-studio: 디자인 작업실

여러 화면의 디자인 작업을 한곳에 모아 두는 저장소입니다. 작업마다 결과를 평가하고 기록하면서 디자인을 단계적으로 개선하는 것이 목적입니다. 작업은 Claude와 함께 진행하며, 다른 AI(ChatGPT, Codex 등)나 사람도 이어받을 수 있도록 작업 폴더마다 인계 문서(HANDOFF.md)와 작업 지침(AGENTS.md)을 둡니다.

## 작업 목록

| 폴더 | 작업 | 지금 상태 | 먼저 읽을 문서 |
| --- | --- | --- | --- |
| [book-design/](book-design/) | 서고의 표지와 페이지('크립토 브리핑 서고', '국채 및 경제 매크로 서고') | 크립토 브리핑 서고의 7번째 판(밤의 가판대 테마)이 게시되어 있습니다. | [HANDOFF.md](book-design/HANDOFF.md) |
| [artifact-design/](artifact-design/) | 아티팩트의 디자인과 스타일. 대시보드에 한정하지 않으며, 대시보드 대안 시안 5종(판정형 브리핑, 예외 기반 알림, 지표 트리, 대화형 분석, 에이전트형 분석)에서 출발합니다. | 시안 두 개의 원본이 `drafts/`에 있고, 위치 지도와 거리 막대 패턴이 `patterns/location-map/`에 있습니다. 대시보드 대안 시안 속 크립토 내용은 예시이며, 이 작업은 디자인과 스타일만 다룹니다. 기준선은 아직 정하지 않았습니다. | [HANDOFF.md](artifact-design/HANDOFF.md) |
| [crypto-dashboard-design/](crypto-dashboard-design/) | 미국 증시·크립토 모니터링 화면. 지금은 미국 섹터 모니터링 화면(섹터 전환 매트릭스, 거래소 상장 표시, 돌파 지도)을 다루며, 하위 개념인 블룸버그 스타일 크립토 대시보드를 `bloomberg-style/`에 둡니다. | 블룸버그 스타일 시안 네 개의 원본과 사례 캡처 두 장이 `bloomberg-style/`에 있습니다. 기준선은 아직 정하지 않았습니다. | [HANDOFF.md](crypto-dashboard-design/HANDOFF.md) |

## 폴더 안내

```
design-studio/
├── README.md                 이 파일
├── AGENTS.md                 모든 작업에 공통인 작업 지침
├── 디자인_원칙.md               여러 작업에 두루 통하는 디자인 결정
├── book-design/              작업 1: 서고의 표지와 페이지
│   ├── HANDOFF.md            인계 문서
│   ├── AGENTS.md             서고 작업에만 해당하는 규칙
│   └── …                     표지 모듈, 서고 페이지 판본, 실험과 분석 기록
├── artifact-design/          작업 2: 아티팩트의 디자인과 스타일(내용은 예시)
│   ├── HANDOFF.md            인계 문서
│   ├── AGENTS.md             이 작업에만 해당하는 규칙
│   ├── patterns/             다시 쓰는 디자인: 위치 지도와 거리 막대(location-map)
│   └── drafts/               시안 원본: 대시보드 대안 시안 5종, 상권 지도 시안
└── crypto-dashboard-design/  작업 3: 미국 증시·크립토 모니터링 화면
    ├── HANDOFF.md            인계 문서(섹터 모니터링 인계 브리프 포함)
    ├── AGENTS.md             이 작업에만 해당하는 규칙
    └── bloomberg-style/      하위 개념: 블룸버그 스타일 크립토 대시보드
        ├── README.md         스타일 설명과 사례 캡처 2장
        └── drafts/           시안 원본: 섹터 전환 터미널, 거래소 상장 표시, 돌파 장부, 돌파 벽
```

## 이어받는 방법

1. [AGENTS.md](AGENTS.md)와 [디자인_원칙.md](디자인_원칙.md)를 읽습니다. Claude와 GPT가 번갈아 일하는 방법은 AGENTS.md의 '인계 규칙'에 있습니다.
2. 맡은 작업 폴더의 HANDOFF.md와 AGENTS.md를 읽습니다. 작업 폴더의 AGENTS.md와 맨 위의 AGENTS.md가 서로 다르면 작업 폴더의 규칙을 따릅니다.
3. 지금 상태와 사용자가 고른 것, 지켜야 할 규칙을 짧게 정리한 뒤 사용자의 지시를 기다립니다.

다른 AI에게 처음 보낼 메시지는 다음처럼 쓰면 됩니다. `<폴더>` 자리에는 `book-design`, `artifact-design`, `crypto-dashboard-design` 가운데 하나를 넣습니다.

```
https://github.com/tlzkrh1029/design-studio 저장소의 <폴더> 작업을 이어서 하려고 합니다.
먼저 맨 위의 AGENTS.md와 디자인_원칙.md, 그리고 <폴더>/HANDOFF.md와 <폴더>/AGENTS.md를 읽고,
지금 상태와 사용자가 고른 것, 지켜야 할 규칙을 짧게 정리해 주세요. 그다음 제가 맡길 작업을 기다려 주세요.
```

## 새 작업을 더할 때

- 맨 위에 새 폴더를 만들고, 폴더 이름은 영어 소문자와 하이픈으로 짓습니다(예: `book-design`).
- 폴더 안에 HANDOFF.md와 AGENTS.md를 두고, 위의 작업 목록에 한 줄을 더합니다.

## 이력

- 2026-10-02: 독립 저장소였던 [book_design](https://github.com/tlzkrh1029/book_design)을 이 저장소의 `book-design/` 폴더로 옮겼습니다. 커밋 13개는 식별 번호까지 그대로 이어집니다. 원래 저장소는 보관(archive) 처리해 읽기 전용으로 남겨 둡니다.
- 2026-10-02: `dashboard-design/` 폴더를 만들고, 섹터 모니터링 인계 브리프의 내용을 HANDOFF.md로 옮겼습니다.
- 2026-10-03: 사용자가 고른 시안 다섯 개의 원본을 저장소로 내보냈습니다. 섹터 모니터링 화면의 시안 네 개는 `dashboard-design/drafts/`에 두었습니다. 크립토 시장 화면의 시안 하나는 새 작업 `crypto-dashboard-design/`(작업 3)으로 나누고, 그 폴더의 `drafts/`에 두었습니다.
- 2026-10-05: 사용자의 결정에 따라 두 작업 폴더의 내용을 맞바꿨습니다. 대시보드 대안 시안 5종은 `dashboard-design/`으로 옮긴 뒤 폴더 이름을 `artifact-design/`으로 바꿨고, 이 작업은 아티팩트의 디자인과 스타일을 다룹니다(시안 속 크립토 내용은 예시입니다). 섹터 모니터링 작업은 `crypto-dashboard-design/`으로 옮겨 '미국 증시·크립토 모니터링 화면'으로 정의했고, 하위 개념인 블룸버그 스타일 크립토 대시보드는 그 시안 네 개와 함께 `bloomberg-style/`에 모았습니다.
- 2026-10-05: '건대스타시티점 브리핑'의 상권 지도를 다시 디자인하면서 `artifact-design/patterns/location-map/`(위치 지도와 거리 막대)을 만들고, 비교한 시안을 `artifact-design/drafts/location-map-drafts/`로 내보냈습니다. 같은 날 디자인 원칙 8(지도)을 더했습니다.

## 공개 범위

- 공개 저장소입니다. 서점 표지, 잡지 표지, 다른 회사 제품의 화면 캡처처럼 권리가 다른 곳에 있는 이미지는 넣지 않고, 목록과 출처 주소, 분석 결과 같은 사실 정보만 넣습니다. 서고 작업에서 뺀 것은 [book-design/docs/09](book-design/docs/09_공개_범위와_제외_항목.md)에 정리되어 있습니다.
- 사용자의 이름, 이메일 같은 개인 정보는 넣지 않습니다. 커밋 작성자는 `Claude <noreply@anthropic.com>`입니다.
- 저장소에 나오는 claude.ai 링크는 모두 소유자만 열 수 있는 비공개 아티팩트를 가리킵니다.
