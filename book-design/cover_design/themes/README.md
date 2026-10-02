# themes: 서고 테마 시안 3종

밤의 가판대(`night`), 편집국 1면(`paper`), 달력 벽(`calendar`)입니다. 콘셉트와 구성은 [docs/04_서고_테마_시안.md](../../docs/04_서고_테마_시안.md)에 있습니다.

```sh
python3 build_themes.py night paper calendar   # *.src.html → *.html
```

`*.src.html`의 `<<MZ>>`, `<<COMMON>>` 자리에 표지 모듈(`../mz.js`)과 공용 도우미(`common.js`)가 들어갑니다. 페이지는 `../data.js`의 브리핑 기록 31건으로 그립니다.
