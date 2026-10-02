# experiment2: 2차 실험(브리프+토큰, XML 태그, 명세 없이)

실험 설계와 결과는 [docs/06_명세_형식_실험_2차.md](../../docs/06_명세_형식_실험_2차.md)에 있습니다.

| 파일 | 내용 |
| --- | --- |
| `brief_*.md`, `originals/` | 1차 실험과 같은 브리프와 원래 시안(경로만 바꿈) |
| `specs/<테마>.md` | 브리프+토큰 명세 3개 |
| `specs/<테마>.xml` | XML 태그 명세 3개 |
| `IMPLEMENT.md` | 구현자에게 준 안내(1차와 같은 내용에 '명세'를 '지시'로 바꾸고 임시 폴더 규칙을 더함) |
| `<테마>_md`, `<테마>_xml`, `<테마>_direct` (`.src.html`, `.html`) | 구현 페이지 9개 |
| `notes/<테마>_xml.md` | XML 태그 조건의 구현자가 쓴 `<plan>`과 `<check>` |
| `build.py`, `shot.py` | 빌드와 렌더링 |
| `renders/*.jpg` | 구현 페이지 전체 화면(1배율) |
| `sheets/<테마>.jpg` | 원래 시안, YAML, JSON, 브리프+토큰, XML 태그, 명세 없이를 나란히 놓은 비교 이미지 |
| `boards/res_*.jpg`, `boards/blobs.json`, `boards/sizes.json`, `boards/_m.html`, `boards2.py` | 캔버스에 올린 결과 화면(2배율), 캔버스 이미지 주소, 보드 높이, 보드 생성 도구 |
| `blind_scores.csv` | 블라인드 평가 원자료(평가자 6명 × 페이지 6개 = 36행) |

평가자에게 준 평가용 브리프와 평가자가 쓴 점수는 [`../judge/`](../README.md#judge)에 있습니다.
