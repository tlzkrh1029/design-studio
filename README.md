# design-studio: 디자인 작업실

여러 화면의 디자인 작업을 한곳에 모아 두는 저장소입니다. 작업마다 결과를 평가하고 기록하면서 디자인을 단계적으로 개선하는 것이 목적입니다. 작업은 Claude와 함께 진행하며, 다른 AI(ChatGPT, Codex 등)나 사람도 이어받을 수 있도록 작업 폴더마다 인계 문서(HANDOFF.md)와 작업 지침(AGENTS.md)을 둡니다.

## 작업 목록

| 폴더 | 작업 | 지금 상태 | 먼저 읽을 문서 |
| --- | --- | --- | --- |
| [book-design/](book-design/) | 서고의 표지와 페이지('크립토 브리핑 서고', '국채 및 경제 매크로 서고') | 크립토 브리핑 서고의 7번째 판(밤의 가판대 테마)이 게시되어 있습니다. | [HANDOFF.md](book-design/HANDOFF.md) |
| [dashboard-design/](dashboard-design/) | 미국 섹터 모니터링 화면(섹터 전환 매트릭스, 거래소 상장 표시, 돌파 지도) | 블룸버그 터미널 스타일을 스타일 사례 하나로 정리했습니다. 기준선은 아직 정하지 않았습니다. | [HANDOFF.md](dashboard-design/HANDOFF.md) |

## 폴더 안내

```
design-studio/
├── README.md             이 파일
├── AGENTS.md             모든 작업에 공통인 작업 지침
├── 디자인_원칙.md          여러 작업에 두루 통하는 디자인 결정
├── book-design/          작업 1: 서고의 표지와 페이지
│   ├── HANDOFF.md        인계 문서
│   ├── AGENTS.md         서고 작업에만 해당하는 규칙
│   └── …                 표지 모듈, 서고 페이지 판본, 실험과 분석 기록
└── dashboard-design/     작업 2: 미국 섹터 모니터링 화면
    ├── HANDOFF.md        인계 문서
    ├── AGENTS.md         이 작업에만 해당하는 규칙
    └── bloomberg-style/  스타일 사례: 블룸버그 터미널 스타일
```

## 이어받는 방법

1. [AGENTS.md](AGENTS.md)와 [디자인_원칙.md](디자인_원칙.md)를 읽습니다. Claude와 GPT가 번갈아 일하는 방법은 AGENTS.md의 '인계 규칙'에 있습니다.
2. 맡은 작업 폴더의 HANDOFF.md와 AGENTS.md를 읽습니다. 작업 폴더의 AGENTS.md와 맨 위의 AGENTS.md가 서로 다르면 작업 폴더의 규칙을 따릅니다.
3. 지금 상태와 사용자가 고른 것, 지켜야 할 규칙을 짧게 정리한 뒤 사용자의 지시를 기다립니다.

다른 AI에게 처음 보낼 메시지는 다음처럼 쓰면 됩니다. `<폴더>` 자리에는 `book-design`이나 `dashboard-design`을 넣습니다.

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

## 공개 범위

- 공개 저장소입니다. 서점 표지, 잡지 표지, 다른 회사 제품의 화면 캡처처럼 권리가 다른 곳에 있는 이미지는 넣지 않고, 목록과 출처 주소, 분석 결과 같은 사실 정보만 넣습니다. 서고 작업에서 뺀 것은 [book-design/docs/09](book-design/docs/09_공개_범위와_제외_항목.md)에 정리되어 있습니다.
- 사용자의 이름, 이메일 같은 개인 정보는 넣지 않습니다. 커밋 작성자는 `Claude <noreply@anthropic.com>`입니다.
- 저장소에 나오는 claude.ai 링크는 모두 소유자만 열 수 있는 비공개 아티팩트를 가리킵니다.
