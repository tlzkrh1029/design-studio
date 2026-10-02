# Coding rules for magazine cover analysis (second coder)

You code Korean business-weekly covers (매경이코노미 = mk_, 한경비즈니스 = hk_) with a fixed codebook.
The allowed values for every variable are in `/home/claude/covers/analysis/codebook.json`
(`categories[].vars[]`, each with `var` and `values`). Use the value strings EXACTLY as written there.
Variables whose `values` is a string ("자유 기록", "정수", "1~5" ...) take free text, an integer, or 1–5.

Output: one JSON object per cover, one line each, keys = `key` + every `var` in the codebook, same order not required.
Integers for `secondary_lines`, `headline_lines`, and the four 1–5 scales (`calm_dynamic`, `serious_playful`,
`minimal_maximal`, `negative_positive`). Everything else is a string.

## Decision rules (apply exactly)

- Unit = one cover. If several values fit, pick the single most prominent one.
- Main headline block = the largest text group other than the masthead (the cover story title) plus lines set with it.
- `headline` = the main headline text as printed (one line, spaces between lines).
- `secondary_lines` = number of secondary cover lines (other stories), counted per story, not per printed line. Small tags like "단독"/"스페셜 리포트" do not count separately.
- `headline_lines` = printed lines in the main headline block (including a kicker/deck line set in that block).
- `subhead` = "있음" only when the headline block contains a separate phrase in a clearly different size/weight/colour that explains the headline (a kicker above or a deck below), not when the lines simply complete one phrase (e.g. "2026 재테크 / 7가지 질문" → 없음; "기생이 아니라 생존이다 / 800만 '캥 경제학'" → 있음).
- `badge` = a promotional graphic device (a seal, sticker, ribbon, special-issue logo, supplement thumbnail, "BEST analyst" mark, "OO 선정" pill). Tiny text flags on secondary lines do not count.
- `boxout` = a solid colour shape placed behind headline text to hold it (not a badge).
- `masthead_color` = colour of the Latin part of the masthead (ECONOMY / BUSINESS).
- `masthead_overlap`: "이미지가 제호 일부를 가림" when part of the image passes IN FRONT of the masthead letters; "제호가 이미지 위에 얹힘" when detailed main-image content (not plain sky/background) sits directly behind the masthead; otherwise "겹치지 않음".
- `medium`: 실사 사진 = an unaltered-looking photograph; 사진 합성 = photos combined/cut out/composited (incl. people cut-outs on a background); 사실적 3D·CG = photoreal or painterly digital render (incl. AI-looking imagery); 2D 일러스트 = flat/vector/line drawing; 콜라주·페이퍼 = paper cut-outs, torn paper, collage look; 타이포그래피 중심 = type is the image.
- `people_n` counts human figures (not animals/robots/characters). `people_kind`: photos of identifiable real people → 실존 인물 사진; photos of anonymous models → 익명 인물 사진; drawn/rendered/silhouette/miniature figures (even of real people) → 그림·실루엣·미니어처.
- `shot`, `gaze`, `angle` refer to the main human figure if any; `shot`/`gaze` = 해당 없음 when no people. Angle refers to the camera view of the main subject.
- `image_area` = share of the cover occupied by the main image content (not a flat background). A picture that fills the whole cover as one scene = 풀블리드.
- `vr_structure` (Phillips & McQuarrie): 직설 = shows the subject literally; 병치 = two or more elements placed side by side to be compared/related; 융합 = two things merged into one object (e.g. a chip that is a rocket); 대체 = one element stands in for the absent other (e.g. Pac-Man = AI eating software).
- `vr_meaning`: 연결 = association/metonymy (flag → country, logo → company); 유사 비교 = metaphor (X is like Y); 대립 비교 = contrast/opposition shown; 해당 없음 = no rhetorical figure.
- `layout`: 중앙 오브젝트형 = one central object/cluster on a mostly plain ground; 풀블리드 장면형 = a full-cover scene; 인물 초상형 = one person dominates; 인물 그리드형 = many people arranged in rows; 타이포그래피 주도형 = type is the dominant visual; 분할형 = the cover is split into clear zones (left/right, top/bottom, stripes, panels).
- `headline_v` = vertical third containing the centre of the main headline block, measured on the cover area.
- `ideal_real` (Kress & van Leeuwen): 문구 위·이미지 아래 / 이미지 위·문구 아래 (text placed at the bottom over or under the picture) / 문구와 이미지 겹침 (text sits inside the middle of the picture) / 좌우 배치 (text on one side, main image on the other).
- `salience` = what the eye hits first after the masthead in about one second.
- `whitespace`: 넓음 = large calm empty areas; 좁음 = busy edge to edge; 보통 = between.
- `bg_hue`, `bg_value` = the dominant background colour family and its lightness. `harmony`: 단색조 = one hue in several values; 유사색 = neighbouring hues; 보색 대비 = opposite hues dominate; 무채색+포인트 = greys/white/black with one or two accent hues; 다색 = many hues.
- `itten` = the single strongest of Itten's contrasts on the cover (명암 light-dark, 한난 warm-cool, 보색 complementary, 채도 saturation, 면적 extension/proportion, 색상 pure hue).
- `headline_color` = colour of the largest headline words. `accent` = what the strongest accent colour is used for.
- `font_class`: 고딕 = sans; 명조 = serif; 그래픽·디스플레이 = decorative/condensed/brush-display; 손글씨·레터링 = hand lettering; 혼용 = two classes in the block.
- `headline_size` = cap height of the largest headline words ÷ cover height: <4%, 4~7%, ≥7%.
- `effect` = visible treatment of headline type (drop shadow, stroke/outline, 3D/metal/texture).
- `emphasis` = device that makes part of the headline stand out (colour change, size contrast, quotation marks).
- `type_image`: 분리 = headline sits on clear background; 이미지 위 오버레이 = headline printed over busy picture; 글자가 이미지의 일부 = the words are physically part of the picture (on an object, a screen, etc.).
- `sentence` = grammatical form of the headline block's main phrase. `verbal_device` = the most prominent verbal device. `tone` = the headline's stance. `script_mix` = scripts other than Hangul in the headline block (numbers, Latin, Hanja); two or more kinds → 여러 문자.
- `anchorage` (Barthes): 정박 = the text fixes the meaning of an otherwise ambiguous image; 중계 = text and image each add something (joke/dialogue/extra layer); 중복 = the image just repeats what the text says.
- `dependency` = could a reader identify the cover story's topic from the picture alone (ignore headline and cover lines, but labels inside the picture count)?
- Scales 1–5 (3 = neutral): calm→dynamic; serious→playful; minimal→maximal (amount of visual elements); crisis/negative→opportunity/positive.
- `archetype` = the main communication strategy: 개념 은유형 (a constructed symbolic object or scene: metaphor or metonymy), 스펙터클 재현형 (the real subject itself shown literally and dramatically), 인물 명단형 (many real people), 인물 초상형 (one real person's portrait photo), 데이터·기호형 (numbers, charts, arrows, currency symbols carry the message), 캐릭터·풍자형 (cartoon characters, humour, satire), 타이포그래피형 (type carries the message).
