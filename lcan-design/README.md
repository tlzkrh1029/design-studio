# lcan-design: 외부 UI 요소를 작업별 스타일에 맞게 고친 사본

이 폴더는 [Lucian UX/UI Prompt](https://lucianlabs.dev/uxui-prompt/)(MIT 라이선스)의 UI 요소를 가져와, design-studio의 작업별 스타일과 [디자인 원칙](../디자인_원칙.md)에 맞게 고친 사본을 두는 곳입니다. 원작자와 관계가 없는 사본이며, 원작자가 만들거나 보증한 것이 아닙니다. 고치기 전의 원본은 `upstream/`에 고정한 커밋 그대로 둡니다.

이 작업을 이어받는다면 [HANDOFF.md](HANDOFF.md)(지금 상태, 사용자가 고른 것, 남은 일)와 [AGENTS.md](AGENTS.md)(규칙)부터 읽으면 됩니다.

## 폴더 안내

```
lcan-design/
├── README.md                 이 파일
├── HANDOFF.md                인계 문서
├── AGENTS.md                 이 작업에만 해당하는 규칙
├── upstream/
│   └── lucian-uxui-prompt/   고정한 커밋의 원본(고치지 않음)
│       ├── UPSTREAM.md       출처, 고정한 커밋, 가져온 날짜, 파일 목록
│       ├── LICENSE           MIT 라이선스 원문
│       └── tokens.css        원본 토큰(한국어판 데이터에서 그대로 복사)
├── base.css                  (아직 없음) 토큰 이름과 기본값, 새로 더한 --lcan-* 토큰
├── drafts/                   (아직 없음) 고치는 중인 요소
├── elements/                 (아직 없음) 사용자가 채택한 요소
├── prompts/                  (아직 없음) 이식 지시문(porting.md)
└── tools/                    (아직 없음) 점검 스크립트
```

'아직 없음'으로 적은 파일과 폴더는 [HANDOFF.md](HANDOFF.md)의 '남은 일'에 따라 만듭니다.

## 채택한 요소

아직 없습니다. 요소를 채택하면 아래 표에 한 줄씩 더합니다.

| 번호 | 이름 | 원본 커밋 | 쓰는 작업 | 바꾼 점 | 채택한 날 |
| --- | --- | --- | --- | --- | --- |

## 작업별 테마 파일

요소의 색, 모서리, 굵기 값은 각 작업 폴더의 `lcan-theme.css`가 정합니다. 테마 파일은 그 스타일을 정의한 문서나 페이지 바로 옆에 둡니다.

| 작업 | 스타일 | 테마 파일 | 상태 |
| --- | --- | --- | --- |
| artifact-design | 베이지 스타일(HANDOFF.md 2절) | [artifact-design/lcan-theme.css](../artifact-design/lcan-theme.css) | 초안입니다. HANDOFF.md 2절에 적힌 값만 넣었습니다. |
| artifact-design | 사이트 대문의 다크 스타일 | `artifact-design/patterns/site-launcher/lcan-theme.css` | 아직 없습니다. |
| book-design | 밤의 가판대 | `book-design/cover_design/library_night/lcan-theme.css` | 아직 없습니다. |
| crypto-dashboard-design | 블룸버그 스타일 | `crypto-dashboard-design/bloomberg-style/lcan-theme.css` | 아직 없습니다. |

'아직 없습니다'로 적은 테마 파일은 그 작업이 요소를 처음 들일 때 만듭니다.

## 원본과 라이선스

- 원본은 [Seokwoooo/lucian-uxui-prompt](https://github.com/Seokwoooo/lucian-uxui-prompt)의 커밋 `7e339fa`(2026-10-16)입니다. 자세한 내용은 [upstream/lucian-uxui-prompt/UPSTREAM.md](upstream/lucian-uxui-prompt/UPSTREAM.md)에 있습니다.
- 원본은 MIT 라이선스입니다. 요소 파일 맨 위의 라이선스 주석 한 줄과 [LICENSE](upstream/lucian-uxui-prompt/LICENSE) 사본을 남깁니다.
- 원작자는 'Lucian'과 'lucianLabs'를 프로젝트와 소유자를 나타내는 이름으로 다룹니다([lucian-icons의 TRADEMARKS.md](https://github.com/Seokwoooo/lucian-icons/blob/main/TRADEMARKS.md)). 그래서 이 폴더는 그 이름을 출처를 밝힐 때만 씁니다. `upstream/lucian-uxui-prompt/`는 원본 저장소의 이름을 그대로 따른 경로입니다.
