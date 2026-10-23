# Sun5 second checker v1 — input scalar schema (strict)

- Written: 2026-10-19T17:33:27-0700 (host /bin/date). Applies to `code/sun5_second_checker_v1.py` (a6ecf3122320b321e899504778fe5024bba96dc4babe8fd04d025d0d260b78f0).
- Pinned input: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-core5-certificates-run1-parent-extract.tsv`, sha256 e9bd7c54d9d9c85228f071973763c186d9a064f1269faffd70d43d53e18b5bb2, 635388 bytes (= gunzip of producer `engine-v1-run1/certificates.tsv.gz`, sha256 1c7e8008a35ac1bd5dbc6be2b3ec886a36b62765a62ef2a15a5ff8f0f541be85; run.json records the same uncompressed sha256). Untrusted data.
- Citation basis for the layout: survivors.json (key decoding), controls.json C4 demos (rule + witness arrays, `--` markers), proof-v4 §4 (certificate semantics, FH2 counts "[864, 16]"), rules-v1 "Engine rule order and certificates". The grammar below is exactly what the checker accepts; anything else fails closed with the stated reason.

## File
| item | rule | reason on violation |
|---|---|---|
| bytes | only 0x09, 0x0A, 0x20–0x7E | file `FILE_FORBIDDEN_BYTE:count=,first_offset=` |
| size | non-empty | file `FILE_EMPTY` |
| end | final byte 0x0A | file `FILE_NO_FINAL_NEWLINE`; last line `PARSE_TRUNCATED_FINAL_LINE` |
| lines | one record per line, no header, any order | empty line `PARSE_EMPTY_LINE` |
| fields | exactly 3, separated by single 0x09 | `PARSE_FIELD_COUNT` (key not parsed ⇒ its orbit is missing) |

## KEY (field 1)
`[123]{10} "/" [-0-4] [-0-4]` — digit k is α on edge k of (01,02,03,04,12,13,14,23,24,34); then E2, E3; a digit is a vertex, `-` is none. Violation `PARSE_KEY`. Repeated key string `PARSE_DUPLICATE_KEY:first_line=`.

## RULE (field 2)
Exactly one of `T`, `K`, `PB`, `N2`, `FH2`, `SURVIVE`; else `PARSE_UNKNOWN_RULE` (includes uncited P-pair/F-H1 tags).

## WITNESS (field 3), byte grammar; d = `[0-4]`; N = `0|[1-9][0-9]{0,5}`
| rule | grammar | static constraints | semantics checked against recomputation |
|---|---|---|---|
| T | `[[d,d,d],N,N]` | a<b<c | N1 = τ_min(a,b,c), N2 = τ_max(a,b,c); require τ_min > τ_max |
| K | `[d,[d(,d){1,3}],"N(/D)?"]`, D = `[1-9][0-9]{0,5}` | S strictly increasing, 2≤|S|≤4, v∉S; rational canonical (D>1, gcd(N,D)=1) | q = Σ_{i∈S}α_iv/4 (= Σ|U_iU_v|/|G|); every pair linked; Σα_iv ≥ 4 |
| PB | same as K | same | q = Σ_S(1−x_j) − Σ_pairs(1−x_j−x_k+hi_jk); require q ≥ 1 |
| N2 | `[]` | — | all ten α = 2 |
| FH2 | `[[d,d],[d(,d){0,2}],N,N]` | a<b, V2 strictly increasing, V2∩{a,b}=∅ | α_ab = 1; V2 = recomputed {v: α_va=α_vb=2} ≠ ∅; N1 = #assignments case (i), N2 = #assignments case (ii); all assignments of both cases rejected |
| SURVIVE | `-` | — | record orbit = orbit(S-D of proof-v4 §6) |

Static violations: `PARSE_WITNESS_SYNTAX`, `PARSE_INDEX_ORDER`, `PARSE_VERTEX_IN_SET`, `PARSE_NONCANONICAL_RATIONAL`.
Semantic reasons: `T_SERIALIZED_TAU_MIN_MISMATCH`, `T_SERIALIZED_TAU_MAX_MISMATCH`, `T_NOT_KILLING`, `K_LINK_ABSENT:ij`, `K_SUM_BELOW_4`, `K_SERIALIZED_SUM_MISMATCH`, `PB_NOT_KILLING`, `PB_SERIALIZED_VALUE_MISMATCH`, `N2_NOT_ALL_TWO`, `FH2_ALPHA_AB_NOT_1`, `FH2_V2_EMPTY`, `FH2_V2_MISMATCH`, `FH2_CASE_I_NOT_REFUTED`, `FH2_CASE_II_NOT_REFUTED`, `FH2_COUNT_I_MISMATCH`, `FH2_COUNT_II_MISMATCH`, `SURVIVOR_NOT_SD`.
Coverage reasons: record `ORBIT_OVERLAP:line=`, `ORBIT_OVERLAPPED:line=`; file `ORBIT_OVERLAP_EVENTS:count=`, `UNIVERSE_MISSING:count=` (+ ≤20 decoded examples).
Self-check failures (never PASS): INCOMPLETE_ERROR with traceback text (group closure ≠ S5, colouring enumeration not bijective, orbit-stabiliser mismatch, image outside 𝓛, S-D stabiliser ≠ {id,(3 4)}, Burnside sum not divisible or ≠ record count under an exact partition).

## Derivation notes for the two serialized rationals
- K q: proof-v4 §4 states the K test Σ_{i∈S}α_iv ≥ 4; rules-v1 L3 states it as Σ|U_iU_v| < |G|. The serialized string is the latter sum in units of |G|. Corroborated by hand on two pinned records (`1111111111/00` → "1", `2333333333/20` [0,[1,3]] → 5/4) and the controls.json demo (`1233133333/1-` → K [0,[1,3],"1"]). [INFERENCE from cited semantics + data; no code read.] The checker requires exact equality, so a wrong reading can only produce FAIL, never a false PASS.
- PB q: rules-v1 L4 (P5) left side at hi; hand-corroborated on `3333333333/00` [1,[0,2,3,4]] → 1, `1122322332/20` → 1, `1222333333/00` → 1, `2223223233/44` → 1. Same fail-closed property.

## Observed syntactic census of the pinned input (regex/JSON shape only; no predicate evaluated)
21150 lines, all keys match KEY; rules T 20465, K 637, PB 20, N2 5, FH2 22, SURVIVE 1 (= run.json counts); 8 byte templates; K strings {"1": 527, "5/4": 110}, PB {"1": 20}, FH2 counts all (864,16); all index lists strictly increasing; no CR, no space, ASCII only. These observations are not used by the checker.
