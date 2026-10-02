# cover_design: 표지 모듈, 서고 페이지, 테마 시안, 실험

작업 환경의 `/home/claude/cover_design` 폴더를 옮긴 것입니다. 3단계부터 9단계까지의 코드와 결과물이 모두 여기에 있습니다. 스크립트는 이 절대 경로를 그대로 쓰므로, 다시 실행하는 방법은 저장소 [README](../README.md#다시-만들어-보기)를 보면 됩니다.

## 폴더와 파일

| 위치 | 단계 | 내용 | 문서 |
| --- | --- | --- | --- |
| `parts/`, `build_mz.sh`, `mz.js`, `mz.css` | 3 | 잡지형 표지 모듈(시안 2). `parts/*.js`를 이어 붙여 `mz.js`를 만듭니다. | [docs/03](../docs/03_잡지형_표지_모듈.md) |
| `mz_v1.js`, `mz_v1.css` | 3 | 표지 모듈 시안 1 | [docs/03](../docs/03_잡지형_표지_모듈.md) |
| `BRIEF.md` | 3 | 표지 설계 메모 | [docs/03](../docs/03_잡지형_표지_모듈.md) |
| `data.js`, `briefs.json` | 3 | 서고 데이터베이스에서 읽은 브리핑 기록 31건(9/2~9/30)의 사본 | |
| `harness.html`, `mkh.py`, `h.html` | 3 | 표지 미리보기 하네스(`h.html#shelf`, `#big`, `#row`, `#catalog`, `#schemes`) | |
| `plan.js` | 3 | 31호의 배치 계획(주제, 그림, 배색, 색상)을 출력하는 Node 스크립트 | |
| `shot.py`, `cshot.py`, `mshot.py`, `pshot.py`, `tshot.py`, `finalshots.py`, `cap.py`, `dbg*.py` | 3~5 | 하네스, 서고, 테마 시안을 캡처하고 점검한 스크립트 | |
| `final/` | 3~5 | 캔버스에 올린 최종 이미지 | |
| `out/` | 3~5 | 시안을 다듬는 동안 남긴 중간 캡처 | |
| `*.jpg`(이 폴더 바로 아래) | 3 | 표지 시안 1을 하네스와 서고 미리보기에 넣어 확인한 캡처(국면별 색 시연 포함) | [docs/03](../docs/03_잡지형_표지_모듈.md) |
| `page/`, `build_page.py` | 4 | 서고 5번째 판(`page/src.html`), 6번째 판(`page/final.html`), 6번째 판 미리보기(`page/preview.html`). 6번째 판은 `build_page.py`로 만들었습니다. | [docs/07](../docs/07_서고_적용_이력.md) |
| `themes/` | 5 | 서고 테마 시안 3종과 공용 도우미 | [docs/04](../docs/04_서고_테마_시안.md) |
| `experiment/` | 6 | 1차 실험: YAML, JSON 명세와 결과 | [docs/05](../docs/05_명세_형식_실험_1차.md) |
| `experiment2/` | 8 | 2차 실험: 브리프+토큰, XML 태그, 명세 없이, 블라인드 평가 점수 | [docs/06](../docs/06_명세_형식_실험_2차.md) |
| `judge/` | 8 | 블라인드 평가자 6명의 평가용 브리프, 점수, 대응표 | [docs/06](../docs/06_명세_형식_실험_2차.md) |
| `library_night/` | 9 | 서고 7번째 판(밤의 가판대) 원본, 빌드, 게시본, 미리보기, 데이터 사본, 확인 캡처 | [docs/07](../docs/07_서고_적용_이력.md) |
| `package.json`, `package-lock.json` | | 미리보기와 캡처에 쓰는 글꼴(@fontsource 7종). `npm install`로 받습니다. | |

## 빌드 흐름

```
parts/*.js ──build_mz.sh──▶ mz.js ─┬─ mkh.py ──────────▶ h.html (표지 하네스)
                                   ├─ build_page.py ───▶ page/final.html (6번째 판), page/preview.html
                                   ├─ themes/build_themes.py ─▶ themes/*.html (테마 시안)
                                   ├─ experiment/build.py ────▶ experiment/*.html (1차 실험)
                                   ├─ experiment2/build.py ───▶ experiment2/*.html (2차 실험)
                                   └─ library_night/build.py ─▶ library_night/final.html (7번째 판), preview.html
```

`themes/`, `experiment/`, `experiment2/`의 페이지 원본(`*.src.html`)에는 `<<MZ>>`(표지 모듈)와 `<<COMMON>>`(공용 도우미 `themes/common.js`) 자리가 있고, 빌드 스크립트가 그 자리를 채웁니다. 서고 7번째 판은 `/*<<MZCSS>>*/`, `/*<<MZJS>>*/` 자리를 씁니다.

## judge/

| 파일 | 내용 |
| --- | --- |
| `<테마>_<A,B>/brief.md` | 평가자에게 준 평가용 브리프(테마 콘셉트와 공통 브리프) |
| `<테마>_<A,B>/scores.json` | 평가자가 쓴 점수(P1~P6), 강점과 문제 한 줄씩, 요약 |
| `judge_map.json` | 평가자마다 P1~P6이 어떤 조건이었는지 적은 대응표와 이미지 목록 |
| `judge_unblinded.json` | 조건 이름을 붙인 점수 |
| `scratch/` | 평가 과정에서 작업 공간에 남은 보조 스크립트 |

평가자가 본 페이지 캡처(축소본과 조각)는 `experiment/boards/`, `experiment2/boards/`의 결과 화면과 같은 페이지를 잘라 만든 것이어서 넣지 않았습니다.

## 넣지 않은 것

- `node_modules/`(121MB): `npm install`로 다시 받을 수 있습니다.
- `experiment2/tmp/`(103MB): 2차 실험 작업자들의 임시 폴더(잘라 낸 확인 이미지와 시험 스크립트)입니다.
- 같은 화면의 중복 캡처: JPEG 사본이 함께 있던 PNG(`final/`, `experiment/boards/`, `experiment2/boards/`), 1차 실험의 재렌더링(`chk_*`)과 부분 캡처(`top_*`, `mid_*`, `bot_*`), 평가용 조각 이미지.
- `experiment/theme_specs.zip`: 1차 실험 명세를 대화에 보낼 때 묶은 압축 파일이며, 같은 명세가 `experiment/specs/`에 있습니다.
