# agents: 하위 작업 지시문과 보고

작업 중에 Claude가 하위 에이전트 37개에게 나눠 맡긴 일의 기록입니다. 파일마다 Claude가 쓴 지시문과 하위 에이전트가 돌려준 최종 보고를 원문 그대로 담았습니다. 지시문은 영어로 썼고, 보고는 지시에 따라 한국어나 영어로 돌아왔습니다. 대화 전체 기록은 넣지 않았습니다.

하위 에이전트를 쓴 이유는 세 가지입니다.

- **독립성**: 코더 간 일치도, 보고서 검증, 블라인드 평가처럼 앞선 작업을 보지 않은 사람이 판단해야 하는 일
- **통제 실험**: 명세를 쓰는 사람과 만드는 사람을 나누고, 만드는 사람이 자기 명세만 보게 해야 하는 일
- **병렬 처리**: 같은 형식의 일을 테마 3개에 동시에 맡기는 일

| 번호 | 시작(한국 시간) | 단계 | 작업 | 파일 |
| --- | --- | --- | --- | --- |
| 01 | 09-30 19:05 | 주간지 분석 | 두 번째 코더, 표지 10장 (A조) | [01_second_coder_for_10_covers_set_a.md](01_second_coder_for_10_covers_set_a.md) |
| 02 | 09-30 19:05 | 주간지 분석 | 두 번째 코더, 표지 10장 (B조) | [02_second_coder_for_10_covers_set_b.md](02_second_coder_for_10_covers_set_b.md) |
| 03 | 09-30 20:17 | 주간지 분석 | 보고서 수치와 문장 검증 | [03_verify_doc_numbers_and_wording.md](03_verify_doc_numbers_and_wording.md) |
| 04 | 09-30 20:17 | 주간지 분석 | 표지 묘사와 코딩 표본 검증 | [04_spot_check_covers_against_images.md](04_spot_check_covers_against_images.md) |
| 05 | 09-30 23:28 | 1차 실험 | 밤의 가판대 · YAML 명세 작성 | [05_night_theme_spec_in_yaml.md](05_night_theme_spec_in_yaml.md) |
| 06 | 09-30 23:28 | 1차 실험 | 밤의 가판대 · JSON 명세 작성 | [06_night_theme_spec_in_json.md](06_night_theme_spec_in_json.md) |
| 07 | 09-30 23:28 | 1차 실험 | 편집국 1면 · YAML 명세 작성 | [07_paper_theme_spec_in_yaml.md](07_paper_theme_spec_in_yaml.md) |
| 08 | 09-30 23:28 | 1차 실험 | 편집국 1면 · JSON 명세 작성 | [08_paper_theme_spec_in_json.md](08_paper_theme_spec_in_json.md) |
| 09 | 09-30 23:29 | 1차 실험 | 달력 벽 · YAML 명세 작성 | [09_calendar_theme_spec_in_yaml.md](09_calendar_theme_spec_in_yaml.md) |
| 10 | 09-30 23:29 | 1차 실험 | 달력 벽 · JSON 명세 작성 | [10_calendar_theme_spec_in_json.md](10_calendar_theme_spec_in_json.md) |
| 11 | 10-01 00:02 | 1차 실험 | 밤의 가판대 · YAML 명세로 페이지 구현 | [11_build_page_from_night_yaml_spec.md](11_build_page_from_night_yaml_spec.md) |
| 12 | 10-01 00:02 | 1차 실험 | 밤의 가판대 · JSON 명세로 페이지 구현 | [12_build_page_from_night_json_spec.md](12_build_page_from_night_json_spec.md) |
| 13 | 10-01 00:02 | 1차 실험 | 편집국 1면 · YAML 명세로 페이지 구현 | [13_build_page_from_paper_yaml_spec.md](13_build_page_from_paper_yaml_spec.md) |
| 14 | 10-01 00:02 | 1차 실험 | 편집국 1면 · JSON 명세로 페이지 구현 | [14_build_page_from_paper_json_spec.md](14_build_page_from_paper_json_spec.md) |
| 15 | 10-01 00:03 | 1차 실험 | 달력 벽 · YAML 명세로 페이지 구현 | [15_build_page_from_calendar_yaml_spec.md](15_build_page_from_calendar_yaml_spec.md) |
| 16 | 10-01 00:03 | 1차 실험 | 달력 벽 · JSON 명세로 페이지 구현 | [16_build_page_from_calendar_json_spec.md](16_build_page_from_calendar_json_spec.md) |
| 17 | 10-01 10:32 | 2차 실험 | 밤의 가판대 · 브리프+토큰 명세 작성 | [17_night_brief_plus_tokens_spec.md](17_night_brief_plus_tokens_spec.md) |
| 18 | 10-01 10:32 | 2차 실험 | 밤의 가판대 · XML 태그 명세 작성 | [18_night_xml_tag_spec.md](18_night_xml_tag_spec.md) |
| 19 | 10-01 10:32 | 2차 실험 | 편집국 1면 · 브리프+토큰 명세 작성 | [19_paper_brief_plus_tokens_spec.md](19_paper_brief_plus_tokens_spec.md) |
| 20 | 10-01 10:32 | 2차 실험 | 편집국 1면 · XML 태그 명세 작성 | [20_paper_xml_tag_spec.md](20_paper_xml_tag_spec.md) |
| 21 | 10-01 10:32 | 2차 실험 | 달력 벽 · 브리프+토큰 명세 작성 | [21_calendar_brief_plus_tokens_spec.md](21_calendar_brief_plus_tokens_spec.md) |
| 22 | 10-01 10:33 | 2차 실험 | 달력 벽 · XML 태그 명세 작성 | [22_calendar_xml_tag_spec.md](22_calendar_xml_tag_spec.md) |
| 23 | 10-01 11:11 | 2차 실험 | 밤의 가판대 · 브리프+토큰으로 페이지 구현 | [23_build_night_page_from_brief_plus_tokens.md](23_build_night_page_from_brief_plus_tokens.md) |
| 24 | 10-01 11:11 | 2차 실험 | 밤의 가판대 · XML 태그 명세로 페이지 구현 | [24_build_night_page_from_xml_prompt.md](24_build_night_page_from_xml_prompt.md) |
| 25 | 10-01 11:12 | 2차 실험 | 밤의 가판대 · 명세 없이 바로 구현 | [25_build_night_page_directly_no_spec.md](25_build_night_page_directly_no_spec.md) |
| 26 | 10-01 11:12 | 2차 실험 | 편집국 1면 · 브리프+토큰으로 페이지 구현 | [26_build_paper_page_from_brief_plus_tokens.md](26_build_paper_page_from_brief_plus_tokens.md) |
| 27 | 10-01 11:12 | 2차 실험 | 편집국 1면 · XML 태그 명세로 페이지 구현 | [27_build_paper_page_from_xml_prompt.md](27_build_paper_page_from_xml_prompt.md) |
| 28 | 10-01 11:12 | 2차 실험 | 편집국 1면 · 명세 없이 바로 구현 | [28_build_paper_page_directly_no_spec.md](28_build_paper_page_directly_no_spec.md) |
| 29 | 10-01 11:12 | 2차 실험 | 달력 벽 · 브리프+토큰으로 페이지 구현 | [29_build_calendar_page_from_brief_plus_tokens.md](29_build_calendar_page_from_brief_plus_tokens.md) |
| 30 | 10-01 11:12 | 2차 실험 | 달력 벽 · XML 태그 명세로 페이지 구현 | [30_build_calendar_page_from_xml_prompt.md](30_build_calendar_page_from_xml_prompt.md) |
| 31 | 10-01 11:12 | 2차 실험 | 달력 벽 · 명세 없이 바로 구현 | [31_build_calendar_page_directly_no_spec.md](31_build_calendar_page_directly_no_spec.md) |
| 32 | 10-01 11:48 | 2차 실험 | 밤의 가판대 · 블라인드 평가 (평가자 A) | [32_blind_judge_night_pages_a.md](32_blind_judge_night_pages_a.md) |
| 33 | 10-01 11:48 | 2차 실험 | 밤의 가판대 · 블라인드 평가 (평가자 B) | [33_blind_judge_night_pages_b.md](33_blind_judge_night_pages_b.md) |
| 34 | 10-01 11:49 | 2차 실험 | 편집국 1면 · 블라인드 평가 (평가자 A) | [34_blind_judge_paper_pages_a.md](34_blind_judge_paper_pages_a.md) |
| 35 | 10-01 11:49 | 2차 실험 | 편집국 1면 · 블라인드 평가 (평가자 B) | [35_blind_judge_paper_pages_b.md](35_blind_judge_paper_pages_b.md) |
| 36 | 10-01 11:49 | 2차 실험 | 달력 벽 · 블라인드 평가 (평가자 A) | [36_blind_judge_calendar_pages_a.md](36_blind_judge_calendar_pages_a.md) |
| 37 | 10-01 11:49 | 2차 실험 | 달력 벽 · 블라인드 평가 (평가자 B) | [37_blind_judge_calendar_pages_b.md](37_blind_judge_calendar_pages_b.md) |

## 함께 보면 좋은 파일

| 하위 작업 | 입력 | 결과물 |
| --- | --- | --- |
| 01~02 두 번째 코더 | `magazine_analysis/analysis/codebook.json`, `coding_rules.md` | `analysis/coder2_A.jsonl`, `coder2_B.jsonl` |
| 03~04 보고서 검증 | `analysis/doc_main_tab.md`, `coding.jsonl` 등 | 보고(이 폴더), 반영 결과 `analysis/audit_changes.json` |
| 05~10 1차 명세 작성 | `cover_design/experiment/brief_*.md`, `originals/` | `experiment/specs/*.yaml`, `*.json` |
| 11~16 1차 구현 | `experiment/IMPLEMENT.md`, 자기 명세 | `experiment/<테마>_<형식>.src.html` |
| 17~22 2차 명세 작성 | `cover_design/experiment2/brief_*.md`, `originals/` | `experiment2/specs/*.md`, `*.xml` |
| 23~31 2차 구현 | `experiment2/IMPLEMENT.md`, 자기 명세(명세 없이 조건은 브리프와 원래 시안) | `experiment2/<테마>_<조건>.src.html`, `notes/*_xml.md` |
| 32~37 블라인드 평가 | `cover_design/judge/<테마>_<A,B>/brief.md`와 페이지 캡처 | `judge/<테마>_<A,B>/scores.json` |
