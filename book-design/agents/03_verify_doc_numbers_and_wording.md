# 보고서 수치와 문장 검증

- 단계: 주간지 분석 (문서 `docs/02_주간지_표지_분석.md`)
- 시작 시각: 2026-09-30 20:17 (한국 시간)
- 작업 설명(원문): `Verify doc numbers and wording`
- 도구 호출: 모두 41회 (Bash 35, Read 4, Grep 1, SubagentHandback 1)

## 지시문 (원문 그대로)

````text
You are reviewing a finished Korean-language analysis report about the cover designs of two Korean business weeklies (매경이코노미 = MK, 38 covers, keys mk_2341…mk_2378; 한경비즈니스 = HK, 37 covers, keys hk_1571…hk_1608, Jan–Sep 2026). You did not write it. Be a demanding, independent checker. Report only: do NOT edit any file and do NOT touch any online document.

The report's main text is exported to: /home/claude/covers/analysis/doc_main_tab.md (lines like "&#91;embedded content: …]" are charts; ignore them).

Data behind it (all in /home/claude/covers/analysis/ unless noted):
- coding.jsonl: 75 JSON lines, one per cover, key + every coded variable (values are Korean category strings; people_n is a string; secondary_lines/headline_lines and four 1–5 scales are integers). This is the final coding; it overrides combined.csv, which may be slightly stale.
- codebook.json (variables and allowed values), coding_rules.md (decision rules).
- metrics.csv: per-cover image metrics (L_mean, C_mean, colorfulness, rms_contrast, edge_density, edge_top/mid/bot, jpeg_bpp, flat_share, symmetry, …). Doc reports medians.
- reliability.csv: inter-coder agreement per variable (agree, kappa, kappa_w, k_final, band). coder2_A.jsonl / coder2_B.jsonl are the second coder's raw codings of 20 covers.
- numeric_tests.csv (Mann-Whitney), assoc_corrected.csv (chi-square p, raw V, bias-corrected Vc, BH q per variable).
- palettes.json and out/palette.csv (5 dominant colours per cover, Lab k-means).
- /home/claude/covers/주간지_표지_2026/표지_목록.json: metadata (magazine, issue, publication_date, combined_issues, note, preview_crop_bbox…).
Quarters = publication_date Jan–Mar / Apr–Jun / Jul–Sep. Percentages in the report are shares of 38 (MK) or 37 (HK) covers unless the sentence says otherwise; rounding to whole percent.

Tasks:
1. Numeric verification. Write Python (pandas is available) to recompute EVERY number, percentage, count, median and ratio stated in the report that can be derived from these files: summary bullets, all tables, the paragraphs (e.g. "밝은 바탕 16장 중 15장은 검정", "매경의 개념 은유형 22장 중 21장은 중앙 오브젝트형", "증시·투자 표지에서 매경은 개념 은유형 4장…", quarter changes like "어두운 바탕이 33%에서 8%로", headline character counts, share of headlines containing digits, covers with Hanja, list-style headlines ending in numbers, headlines ending in '법', counts of covers per example type). Also check that every cover the report cites as an example of a category (e.g. the archetype table's examples, "제호와 이미지의 겹침" examples) is coded that way in coding.jsonl. Items that cannot be derived from data (e.g. descriptions of what is in a picture) are out of scope for this task: skip them.
2. Editorial review against the user's Korean writing rules: prose sentences must be complete (predicate + ending; tables, headings and list labels are exempt), no dropped particles/endings, avoid overusing '~의', avoid the em dash (—), avoid metaphorical words used in place of plain words (unless an established idiom), use established Korean translations for technical terms. Also flag typos, inconsistent terms between sections, and any claim that is contradicted elsewhere in the report or unsupported by the data (e.g. a difference called significant that is not).

Output (keep it under ~700 words, no preamble):
(A) Numeric mismatches: quote the exact report text, claimed value → computed value (with the numerator/denominator), and a suggested corrected wording.
(B) Claims you could verify and that are correct: just a one-line count (e.g. "112 checked, 107 correct").
(C) Typos and style issues: exact quote → suggested replacement.
(D) Logic or consistency issues: exact quote + why + suggestion.
If a category has nothing, write "none".
````

## 최종 보고 (원문 그대로)

````text
**(A) Numeric mismatches**
1. L16 and L84 say "카파 중앙값 0.76". The median of the 52 k_final values is (0.752+0.758)/2 = 0.755, which rounds to 0.75. The 0.76 comes from rounding twice. Change both to "0.75".
2. L155 and L280 give Maekyung's flat area share as "63%". The median flat_share is 0.6247, so it should read "62%".
3. L216 says "5장은 '투자법', '맞이하는 법', '살아가는 법'처럼 … 끝납니다". Only 3 of 37 headlines end in '법' (1585, 1596, 1602). Suggest "3장은 … '~법'으로 끝납니다".
4. L170 says "한경은 37장 중 23장에서 노란 표제가". Only 20 of 37 headlines are coded 노랑·금색. A yellow cluster shows up in about 22–24 palettes depending on the threshold, but covers 1578, 1580, 1583, 1594 (and 1603) get it from the background or other elements. Of the 20 yellow-headline covers, 19 show yellow in the palette (1589 does not). Suggest "노란색은 23장에서 지배색에 들어가며, 노란 표제 20장 중 19장이 여기에 속합니다".
5. L214 says "7장이 … 물음으로 끝납니다". Seven headlines are coded as questions, but only 5 end in one. The first example (2342, '새해도 달릴까 SK하이닉스') and 2343 do not. Suggest "7장이 … 물음을 담습니다".
6. L110 describes Hankyung's secondary cover lines as "2~3개 … 3장은 0개". The actual counts are 2 lines on 25 covers, 3 on 8, 1 on 1 (1593) and 0 on 3. Suggest "대개 2~3개(33장), 1개 1장, 0개 3장".
7. L104 says "두께는 표지 폭의 약 4%". The frame column in metrics.csv gives a median of 3.3% of width (range 2.8–4.2%). Suggest "약 3%".
8. L132 gives Hankyung "반도체·회로 6장". key_symbols supports only 5 (1571, 1576, 1588, 1592, 1599).
9. L134 says "이 인물은 멀리 있고(원경)", but the example it cites, 제2362호, is coded 풀샷. Suggest "대개 멀리 있고".

**(B)** 494 checked, 483 correct. This covers every table percentage, the quarter changes, the bright/dark-background headline colours, the archetype × layout counts, the topic × archetype counts, Hanja (4), list-style headlines (4), digits (16/37), character counts (12.3 and 15.8), all 32 archetype, masthead-overlap and 중계 examples, Fisher p=0.037 and q=0.054.

**(C) Typos and style**
- L214: '스퍼 트릴레마' → '슈퍼 트릴레마'
- L233: '캐거루' → '캥거루'
- L258: '구분선을 없앰음' → '구분선을 없앰'
- L160: "'~하는 법'같은" → "'~하는 법' 같은"
- L122: '콜라주·종이' → '콜라주·페이퍼' (the codebook term)
- L90 '(정박·중복)' and L77 '정박·중계 관계' → use "문구와 이미지의 관계(정박·중계·중복)" in both places.
- L92: "진지↔유쾌 척도는 … 차이였고" → "진지↔유쾌 척도의 불일치는 … 차이였고"
- L216: "매경이 문제를 던지고, 한경은 답을 건네는 방식입니다" → "매경은 문제를 던지고, 한경은 답을 건넵니다"
- Metaphors used in place of plain words:
  - L114: "정체성을 짊어지고" → "정체성을 맡고"
  - L187: "표제를 달구는 데" → "표제를 강조하는 데"
  - L187 heading: "색이 표제를 밀어 올림" → "색으로 표제를 강조함"
  - L7 and L276: "빛나는 (유색) 표제" → "효과를 넣은 (유색) 표제"
  - L290: "렌더로 빠르게 이동하고" → "렌더링 이미지 비중을 빠르게 늘리고"
- Established Korean terms:
  - '렌더' (L136, L249, L290) → '렌더링 이미지'
  - Optional: '샷/풀샷' → '숏/풀숏', the standard spelling
- Overuse of '의':
  - L240: "대부분의 표지에서 표제가 이미지의 뜻을" → "표지 대부분에서 표제가 이미지가 뜻하는 바를"
  - L289: "작은 화면에서의 전달력" → "작은 화면에서 읽히는 정도"
  - L289: "하나의 상징 사물" → "상징 사물 하나"
- No em dashes found.

**(D) Logic and consistency**
1. L96 "두 잡지 모두 표지의 틀은 매주 거의 바뀌지 않습니다" contradicts L100 ("한경은 … 대부분이 바뀝니다") and L114 ("틀이 약한"). Suggest "매경은 틀 전체가, 한경은 제호 블록만 매주 같습니다".
2. L114 presents "이미지가 제호를 가리는 연출" as typical of Hankyung, but it happens on only 3 of 37 covers. Say "3장에서".
3. L105 "주황색 '매경'과 'ECONOMY'" and "흰색 '한경'과 'BUSINESS'" read as fixed colours, but L107 shows the Latin part switching between black and white. Reword so the colour is attached only to '매경' and '한경'.
4. L148 labels Maekyung's value "제호 바로 아래 95%", but it is the same code (중단 1/3) as Hankyung's "중단 57%". Write "중단 95%(제호 바로 아래)".
5. L134 "나머지 표지는 … 융합이 중심" is not supported: Maekyung has 17 fusion (융합) covers and 16 juxtaposition (병치) covers. Suggest "사람이 없는 14장 중 9장이 융합".
6. L214 "효과를 전혀 주지 않아, 표제가 이미지를 설명하는 측면이 강합니다" does not follow. Drop the causal link.
7. L248 says a "밝은 바탕 + 2D 일러스트 은유 + 경고형 표제" combination became clear in Q3. Bright backgrounds went from only 5/12 to 6/13, and all three together appear on 1 of 13 Q3 covers (2372, a 데이터·기호형). Suggest "어두운 바탕이 줄고 2D 일러스트와 경고형 표제가 늘었습니다".
8. L270:
   - The Fisher test (p=0.037) compares one category chosen after the full comparison failed the correction (q=0.054). Say "사후 비교, 보정 전 p=0.037".
   - A corrected V of 0 does not "보여 줍니다" that the magazines share conventions. Say "차이가 드러나지 않았습니다".
9. L280, the design brief, labels whitespace "넓음" for Maekyung and "좁음" for Hankyung. The most common code is 보통 for both (74% and 57%), and 넓음 is only 26% for Maekyung. Say "여백 많음/적음" together with the flat-area share.
10. L240 reports 중계 counts (4 and 2) as findings, although the kappa for that item is −0.02. The only 중계 cover in the second-coder sample (2373, the cited '세금 이름표') was coded 중복 by the second coder. Present the counts as tentative.
11. L255 calls 1608 a 추석 합본호(1608~1609), but the metadata lists issue 1608 only. The L24–25 table mentions only the 설 합본호 and gives the range as 제1571~1608호. Either verify the cover or align both places.
12. L289 "작은 화면에서도 읽힙니다" is untested, and headline size has kappa 0.38. Suggest "읽히기 쉬울 것으로 보입니다".
13. L9 says "38장 모두 … 보조 커버라인 3개", but L110 says the anniversary issue has 4. Make it "37장".
````
