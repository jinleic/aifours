# Erratum: LF split-count metadata in the parent-owned Gram review manifest (desk M7GramDeltaDesk)

Recorded 2026-10-17T23:56:06.104936-07:00 (host clock). The old manifests are immutable and are NOT rewritten; this table is the parent-side erratum.

- Correct convention: line N = element N of `text.split('\n')`. For LF-terminated text `len(text.split('\n')) = lf_count + 1`; the last element is empty.
- `moqls7-gram-review-inputs-v2/manifest.json` (`cabdbbb61f042167ff784b84546db6807d80e257ffb9c4566e350ee177471d6d`) states: "line N = element N (1-based) of text.split('\n'); a file that ends with LF has lines_split_LF = lf_count lines; form feeds stay inside lines." This is one low for LF-terminated files.
- Every pinned copy still hashes to its recorded SHA-256.

## inputs-v2 (used by both old reviews): 14 of 18 entries one below

| path | lf_count | ends LF | recorded lines_split_LF | len(text.split('\n')) | erratum: corrected value |
|---|---:|---|---:|---:|---|
| `review/AMENDMENT-1.r1.md` | 49 | yes | 49 | 50 | **50** |
| `review/GRAM-ENCODING.r1.md` | 90 | yes | 90 | 91 | **91** |
| `code/gram_enc.py` | 168 | yes | 168 | 169 | **169** |
| `code/gram_encB.py` | 221 | yes | 221 | 222 | **222** |
| `code/gram_certify.py` | 94 | yes | 94 | 95 | **95** |
| `code/gram_controls.py` | 77 | yes | 77 | 78 | **78** |
| `code/gram_controlsB.py` | 73 | yes | 73 | 74 | **74** |
| `code/k2_classes.py` | 65 | yes | 65 | 66 | **66** |
| `code/k2_classesB.py` | 67 | yes | 67 | 68 | **68** |
| `code/ls_classes.c` | 134 | yes | 134 | 135 | **135** |
| `evidence/ls7_main_classes.txt` | 147 | yes | 147 | 148 | **148** |
| `explore/gram/gram_controls_v1.json` | 24 | no | 25 | 25 | correct as recorded |
| `explore/gram/gram_controlsB_v1.json` | 19 | no | 20 | 20 | correct as recorded |
| `review/K1-THEOREM.r1.md` | 145 | yes | 145 | 146 | **146** |
| `sources/2607.12933v2.layout.txt` | 462 | no | 463 | 463 | correct as recorded |
| `sources/2607.12933v2.raw.txt` | 702 | no | 703 | 703 | correct as recorded |
| `README.md` | 136 | yes | 136 | 137 | **137** |
| `explore/ls_classes.stderr` | 149 | yes | 149 | 150 | **150** |

The superseded, never-used `moqls7-gram-review-inputs-v1/manifest.json` carries the same error in 14 of 18 entries (same files). `moqls7-k1-review-inputs-v1/manifest.json` has none.

## Citation lines are unchanged

- All 223 `path:line` citations in `moqls7-gram-review-codex-v1.note.md` and `moqls7-gram-review-claude-v2.note.md` were resolved against the immutable inputs-v2 copies.
- 218 were resolved automatically (183 explicit, 35 bare `:N`). Five bare references were mis-attributed by the regex heuristic. By hand they resolve to `code/gram_certify.py`: claude-v2 note LF112 `:71`, LF114 `:76-78`, LF119 `:72` and `:71`, and LF189 `:52-53`. All of these lines are nonempty.
- Every cited line is nonempty and lies in 1..lf_count. None is element lf_count+1, the empty trailing element.
- Line N is element N under both readings, so **no cited line text changes**. Only the 14 count fields are one low.
- This settles the finding labelled Codex MINOR-6 (`manifest.json:10`). REVIEW-CORRECTIONS.r2.json:27 passed it to the parent. No other action is needed.
