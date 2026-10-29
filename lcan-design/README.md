# lcan-design: 외부 UI 요소를 디자인 원칙에 맞게 보정한 사본

이 폴더는 [Lucian UX/UI Prompt](https://lucianlabs.dev/uxui-prompt/)(MIT 라이선스)의 UI 요소를 가져와, design-studio의 [디자인 원칙](../디자인_원칙.md)에 맞게 보정한 사본을 두는 곳입니다. 원작자와 관계가 없는 사본이며, 원작자가 만들거나 보증한 것이 아닙니다. 요소의 모양은 원본 그대로 두고, 글자 명암비처럼 디자인 원칙에 못 미치는 값만 고칩니다(2026-10-29 사용자 결정). 고치기 전의 원본은 `upstream/`에 고정한 커밋 그대로 둡니다.

이 작업을 이어받는다면 [HANDOFF.md](HANDOFF.md)(지금 상태, 사용자가 고른 것, 남은 일)와 [AGENTS.md](AGENTS.md)(규칙)부터 읽으면 됩니다.

## 쓰는 방법

1. 요소를 넣을 페이지에 [base.css](base.css)와 [lcan-theme.css](lcan-theme.css)를 이 순서로 넣습니다. 게시하는 페이지는 저장소 안의 다른 파일을 불러올 수 없으므로, 두 파일의 내용을 페이지 안에 복사해 넣습니다.
2. 요소는 `upstream/lucian-uxui-prompt/`의 원본을 그대로 붙여 넣습니다. 요소 코드를 고친 요소는 `elements/`에 있는 고친 판을 씁니다.
3. 요소 맨 위의 라이선스 주석 한 줄은 지우지 않습니다.
4. 어느 요소를 썼는지 그 작업 폴더의 HANDOFF.md에 적습니다.

아직 `upstream/`에 없는 요소를 쓰려면, 먼저 고정한 커밋의 원본을 `upstream/`에 들입니다. 방법은 [UPSTREAM.md](upstream/lucian-uxui-prompt/UPSTREAM.md)에 있습니다.

## 폴더 안내

```
lcan-design/
├── README.md                 이 파일
├── HANDOFF.md                인계 문서
├── AGENTS.md                 이 작업에만 해당하는 규칙
├── base.css                  토큰 이름과 원본 기본값(라이트), .ux 공통 규칙
├── lcan-theme.css            모든 작업이 쓰는 공통 테마: 원본 값에서 명암비가 모자란 토큰 여섯 개만 보정
├── upstream/
│   └── lucian-uxui-prompt/   고정한 커밋의 원본(고치지 않음)
│       ├── UPSTREAM.md       출처, 고정한 커밋, 가져온 날짜, 파일 목록
│       ├── LICENSE           MIT 라이선스 원문
│       ├── tokens.css        원본 토큰(한국어판 데이터에서 그대로 복사)
│       └── 023-…, 042-…, 072-…  들인 요소의 원본
├── drafts/                   비교한 시안(목록은 drafts/README.md)
│   ├── beige-token-options/  첫 비교: 베이지 스타일을 적용한 세 안(고르지 않음)
│   └── original-contrast-fix/  둘째 비교: 원본과 명암비 보정판(보정판을 고름)
├── elements/                 (아직 없음) 요소 코드를 고친 요소
├── prompts/                  (아직 없음) 이식 지시문(porting.md)
└── tools/                    (아직 없음) 점검 스크립트
```

'아직 없음'으로 적은 폴더는 [HANDOFF.md](HANDOFF.md)의 '남은 일'에 따라 만듭니다.

## 테마

- 공통 테마는 [lcan-theme.css](lcan-theme.css) 하나입니다. 원본의 라이트 값을 그대로 쓰고, 글자로 쓸 때 4.5:1에 못 미치는 토큰 여섯 개(`--ux-ink-3`, `--ux-accent`, `--ux-accent-2`, `--ux-mint`, `--ux-warn`, `--ux-danger`)만 색상과 채도는 두고 밝기를 낮췄습니다. 값과 근거는 [drafts/original-contrast-fix/notes.md](drafts/original-contrast-fix/notes.md)에 있습니다.
- 글꼴은 원본처럼 웹 글꼴을 불러오지 않고 원본의 글꼴 목록을 씁니다. 기기에 Pretendard가 없으면 기기의 기본 한글 글꼴로 보입니다.
- 다크 값은 아직 없습니다. 원본의 다크 값도 작은 설명 글자가 4.5:1에 못 미치기 때문에, 다크 화면에 요소를 쓰기 전에 같은 방법으로 보정해야 합니다.
- 작업별 테마 파일은 지금 없습니다. 어떤 작업에 다른 값이 꼭 필요하면, 사용자에게 물은 뒤 그 작업 폴더에 둡니다.
- [artifact-design/lcan-theme.css](../artifact-design/lcan-theme.css)는 쓰지 않는 파일입니다. 요소를 베이지 스타일로 다시 칠해 본 첫 비교의 기록으로 남겨 두었습니다.

## upstream에 들인 요소

| 번호 | 이름 | 들인 이유 | 날짜 |
| --- | --- | --- | --- |
| 023 | 펼쳐지는 알림 설정 | 첫 비교와 둘째 비교의 시험 요소 | 2026-10-29 |
| 042 | 단계 진행 마법사 | 첫 비교와 둘째 비교의 시험 요소 | 2026-10-29 |
| 072 | 접히는 인라인 알림 | 첫 비교와 둘째 비교의 시험 요소 | 2026-10-29 |

## 고친 요소

아직 없습니다. 요소 코드를 고쳐 `elements/`에 두면 아래 표에 한 줄씩 더합니다.

| 번호 | 이름 | 원본 커밋 | 쓰는 작업 | 바꾼 점 | 날짜 |
| --- | --- | --- | --- | --- | --- |

## 원본과 라이선스

- 원본은 [Seokwoooo/lucian-uxui-prompt](https://github.com/Seokwoooo/lucian-uxui-prompt)의 커밋 `7e339fa`(2026-10-16)입니다. 자세한 내용은 [upstream/lucian-uxui-prompt/UPSTREAM.md](upstream/lucian-uxui-prompt/UPSTREAM.md)에 있습니다.
- 원본은 MIT 라이선스입니다. 요소 파일 맨 위의 라이선스 주석 한 줄과 [LICENSE](upstream/lucian-uxui-prompt/LICENSE) 사본을 남깁니다.
- 원작자는 'Lucian'과 'lucianLabs'를 프로젝트와 소유자를 나타내는 이름으로 다룹니다([lucian-icons의 TRADEMARKS.md](https://github.com/Seokwoooo/lucian-icons/blob/main/TRADEMARKS.md)). 그래서 이 폴더는 그 이름을 출처를 밝힐 때만 씁니다. `upstream/lucian-uxui-prompt/`는 원본 저장소의 이름을 그대로 따른 경로입니다.
