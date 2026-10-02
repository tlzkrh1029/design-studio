# 표지 묘사와 코딩 표본 검증

- 단계: 주간지 분석 (문서 `docs/02_주간지_표지_분석.md`)
- 시작 시각: 2026-09-30 20:17 (한국 시간)
- 작업 설명(원문): `Spot-check covers against images`
- 도구 호출: 모두 149회 (Read 100, Bash 48, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are an independent visual checker for a Korean report on the cover designs of two Korean business weeklies (매경이코노미 = MK, keys mk_2341…mk_2378; 한경비즈니스 = HK, keys hk_1571…hk_1608, Jan–Sep 2026). You did not write it. Report only: do NOT edit any file and do NOT touch any online document.

Files:
- Report text: /home/claude/covers/analysis/doc_main_tab.md (issue numbers appear as 제NNNN호; MK issues are 2341–2378, HK issues are 1571–1608).
- Cover images: /home/claude/covers/주간지_표지_2026/매경이코노미/매경이코노미_2026_제{N}호.jpg and /home/claude/covers/주간지_표지_2026/한경비즈니스/한경비즈니스_2026_제{N}호.jpg. HK images are 2230×2816 with a ~120px white margin; MK images are 1000×1366 with an orange frame. One HK file (제1576호) is a spread: use the right-hand front cover. To look at an image, you may downscale it with PIL into your scratch directory (e.g. width 900) and open it with the Read tool, and crop/zoom into parts when text is small.
- Final coding: /home/claude/covers/analysis/coding.jsonl (one JSON object per cover; key like "mk_2354").
- Coding rules: /home/claude/covers/analysis/coding_rules.md (allowed values: codebook.json).

Tasks:
1. Every sentence or table cell in the report that describes what is on a specific cover (it names 제NNNN호) must match the image. Check each one: e.g. "제2354호에서는 지폐 더미 위의 빨간 퍼센트 기호를 망원경으로 올려다보고", the archetype example table, the masthead-overlap examples (제1584호, 제1601호, 제1606호), the design-system change table (e.g. HK 제1596호 bold issue number and price 5,000원; MK 제2368호 four secondary cover lines), quoted headline words (e.g. '적토마', '램마겟돈', 'KEEP CALM AND WATCH The GULF'). Also check "제1583호" (the report calls it a 4-panel comic about kangaroos; check the spelling used in the report). Mark each as correct / wrong (what the image actually shows) / uncertain.
2. Random coding audit: take these 12 covers: mk_2343, mk_2350, mk_2358, mk_2364, mk_2370, mk_2375, hk_1577, hk_1585, hk_1590, hk_1593, hk_1599, hk_1604 (if a key does not exist, pick the next issue). For each, view the image and compare against coding.jsonl for: medium, layout, image_area, ideal_real, headline_color, effect, subhead, emphasis, tone, archetype. Apply coding_rules.md. List only the disagreements, with a one-line reason, and give an overall agreement count (e.g. "113/120 agree").

Output (under ~700 words, no preamble):
(1) Wrong or doubtful descriptions: quote the report text → what the image shows → suggested correction.
(2) Count of descriptions checked and found correct.
(3) Coding audit disagreements + the overall agreement count.
````

## 최종 보고 (원문 그대로)

````text
**(1) Wrong or doubtful descriptions** (line numbers refer to `/home/claude/covers/analysis/doc_main_tab.md`)

- **Wrong, L214: '스퍼 트릴레마'.** 제2353호 prints 에너지 **'슈퍼 트릴레마'**, and coding.jsonl also has 슈퍼. Change it to '슈퍼 트릴레마'.
- **Wrong spelling, L233: '캐거루 4컷 만화(제1583호)'.** The content is right: it is a 4-panel comic of kangaroo characters (a kangaroo in a hoodie saying "직업이 뭐냐고요?"/"자녀입니다", then a kangaroo with a moustache in a suit), with the headline 800만 '캥 경제학'. Change it to **'캥거루 4컷 만화'**.
- **Doubtful, L112: "5장. 이 가운데 3장은 인물(제1584호), 로봇(제1601호), 쇠사슬(제1606호)이 제호 글자 앞을 지나감".**
  - All three named cases are correct: Musk's head covers 'SI', the robot's head covers 'NE', and the chain crosses the 'S'.
  - But on **제1600호** the crane hook block and its cables also pass in front of the 'E' and 'S' of BUSINESS. coding.jsonl has it as 겹치지 않음.
  - Suggest "6장 … 4장(… 크레인 갈고리 제1600호 …)". The street-lamp roof on 제1597호 only touches the last S from behind, so I did not count it.
- **Doubtful, L236: "탐정 실루엣이 서울 야경을 돋보기로 보는 표지(제1597호)".** The sky is an orange sunset with lights coming on, and the magnifier shows a ₩ graph going up. Say '노을 진 서울 풍경' instead of 야경.
- **Doubtful, L136: "실존 인물 10~30명".** I counted 10 on 제1595호, about 31 on 제1587호, and about 34 each on 제1572호 and 제1598호. Suggest '10~35명 안팎'.
- **Uncertain, L26/255/258/261: HK dates on Mondays (2026-01-05, 02-09, 06-29, 09-21).** The covers print date ranges starting on Wednesdays: 1571 2026.1.7-13, 1576·1577 2026.2.11-24, 1596 2026.7.1-7, 1608·1609 2026.9.23-10.6. If the Monday dates come from the website, say so. All MK dates match the covers.
- **Minor, L105: "주황색 '매경' … ECONOMY의 M만 주황색".** 제2341호 (신년호) prints '매경' and the 'M' in white on pink, so this holds for 37 of 38.
- **Typo (not visual), L258:** "없앰음" should be "없앰".

**(2) Count**

About 88 cover-specific statements checked:
- 13 scene descriptions in the body text
- 31 archetype-table cells
- 4 masthead-overlap examples
- 10 design-system and special-issue items, plus 8 dates
- 20 quoted headline items
- 2 others

**81 are correct**, 2 are wrong and 5 are doubtful or uncertain. The ones you named all check out:
- 제2354호 is exactly as written.
- 제1596호 shows 'No.1596' in bold, the divider is gone, and the price is 값 5000원 (제1595호 still shows 4500원).
- 제2368호 has the orange '창간 47주년 특대호' line and four secondary cover lines.
- 'KEEP CALM AND WATCH The GULF', '적토마', '램마겟돈', '프렌드플레이션' and 'All METAL RALLY' are printed as quoted.

**(3) Coding audit**

hk_1577 does not exist because it is the combined issue with 1576, so I used **hk_1578**. I coded each cover before looking at coding.jsonl, and measured image area by segmenting each cover's pixels.

Disagreements:
- **mk_2350**
  - image_area: 60~90% → **30~60%**. The spray band, RAM sticks and hand cover about 35%.
  - ideal_real: 문구 위·이미지 아래 → **문구와 이미지 겹침**. The headline is printed inside the black spray band in the middle of the picture (its own type_image is 이미지 위 오버레이).
- **mk_2358** image_area: 60~90% → **30~60%**. The graph and skyline fill only the bottom ~45%; the rest is a grid pattern.
- **mk_2375** image_area: 60~90% → **30~60%**. The safe and the crowd cover about 30–45%.
- **mk_2370** emphasis: 크기 대비 → **없음**. Both lines are the same height (70 vs 66 px); only the weight differs.
- **hk_1578** emphasis: 크기 대비 → **색 바꿈**. '3월' is white while '재테크의 변곡점' is red, at the same size.
- **hk_1593**
  - image_area: 60~90% → **30~60%**. The people cover about 43%.
  - subhead: 있음 → **없음**, on a strict reading of the rule. '투자 대가 9인이 말하는' completes one noun phrase, like the rule's own example '2026 재테크/7가지 질문'.
- **hk_1604**
  - layout: 중앙 오브젝트형 → **풀블리드 장면형**. The sky and skyline fill the whole cover, which also contradicts its own image_area of 풀블리드.
  - effect: 그림자 → **외곽선** (or 여러 효과). There is a dark outline on every side of the letters; the shadow is secondary.
  - archetype: 데이터·기호형 → **개념 은유형**. There are no numbers, charts, arrows or currency symbols; it is a symbolic scene of a map with seven technology bubbles.
  - subhead: 있음 → **없음**, on a strict reading. '대한민국 미래 책임질' completes the phrase.

Borderline, counted as agreement:
- mk_2343, mk_2364 and mk_2370 image_area 30~60%: the objects themselves cover only about 20%, so '30% 미만' is arguable.
- hk_1590 image_area.
- hk_1578 tone (기회·낙관 vs 중립).

There is a pattern in image_area: the coder never uses '30% 미만' and tends to code one band too high.

**Agreement: 108/120 (90%)**, or 110/120 if the two strict-reading subhead calls are excused.
````
