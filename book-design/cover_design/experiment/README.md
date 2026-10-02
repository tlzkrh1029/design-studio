# experiment: 1차 실험(YAML 명세와 JSON 명세)

실험 설계와 결과는 [docs/05_명세_형식_실험_1차.md](../../docs/05_명세_형식_실험_1차.md)에 있습니다.

| 파일 | 내용 |
| --- | --- |
| `brief_common.md`, `brief_night.md`, `brief_paper.md`, `brief_calendar.md` | 명세 작성자에게 준 공통 브리프와 테마 브리프 |
| `originals/` | 원래 시안 캡처(전체와, 위아래로 나눈 조각) |
| `specs/<테마>.yaml`, `specs/<테마>.json` | 명세 작성자가 쓴 명세 6개 |
| `IMPLEMENT.md` | 구현자에게 준 안내(페이지 골격, 공용 도우미, 실제 서고 문구, 렌더링 규칙) |
| `<테마>_<형식>.src.html` | 구현자가 쓴 페이지 원본 |
| `<테마>_<형식>.html` | `python3 build.py <이름>`으로 표지 모듈과 도우미를 넣은 페이지 |
| `build.py`, `shot.py` | 빌드와 렌더링(`python3 shot.py <이름> <출력.png> [배율] [폭]`) |
| `out_<테마>_<형식>.jpg` | 구현자가 렌더링한 전체 화면(1배율) |
| `cmp_<테마>.jpg` | 원래 시안, YAML, JSON을 나란히 놓은 비교 이미지 |
| `boards/res_<테마>_<형식>.jpg` | 캔버스에 올린 결과 화면(2배율) |
| `boards/_m.html`, `boards/spec_sizes.json`, `specboard.py` | 명세를 캔버스 보드로 옮길 때 쓴 도구와 보드 높이 |
| `scratch/` | 구현자들이 공용 임시 폴더에 남긴 점검 스크립트(측정, 확대, 상호작용 확인) |
