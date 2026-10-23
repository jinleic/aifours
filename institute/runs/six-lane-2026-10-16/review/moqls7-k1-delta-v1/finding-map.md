# moqls7 K1 delta: finding map (desk, independent of the Codex delta note)

Delegated parent delta check, desk M7K1DeltaDesk. This map was written at 2026-10-17T22:58:58.668036-07:00 (host clock, PDT), while the
Codex delta review was still running and before its note was read. All references are LF-lines: 1-based indices into
text.split('\n') of the pinned copies under `snapshot/` (see `snapshot/manifest.json`).

Abbreviations:
- r1/r3: `K1-THEOREM.r1.md` (b702b021…8767) / `K1-THEOREM.r3.md` (2d77c637…a096).
- LEM: `LEMMAS.md` (4bddc9d4…50c9).
- README: lane `README.md` as pinned (548915ae…).
- RC: `REVIEW-CORRECTIONS.r2.json` (5105a686…0770).

Status values:
- RESOLVED: the finding is fully fixed.
- RESOLVED-IN-SUBSTANCE: the substance is fixed; a cosmetic residue remains.
- PARTIAL: part of the finding is fixed and part is unchanged.
- UNADDRESSED: nothing was changed.

## Codex note `moqls7-k1-review-codex-v1.note.md` (sha256 54a83ff3…df34)

| finding | r1 locus | status | where in the current text | desk remark |
|---|---|---|---|---|
| MAJOR 1: drat-trim control outcomes unreceipted; `ctl_unsat.drat` is `0` | r1:70–71 | RESOLVED | r3:90–97 | The producer outcome claim is withdrawn (r3:90–91) and the one-line `0` is described correctly. The parent receipt is hash-bound (r3:92–93 = 506b466d…9701, equal to `RESULT.json` receipts[1]). The six controls match `results.controls`, `drat_runs` `ctl_*` and `dt/ctl_*.out` exactly. r3:89 still reports the lane-binary `s VERIFIED` outcome from the producer summaries. This is a status report, not a control claim, and the parent recheck (route 2c) supersedes it. Observation only. |
| MAJOR 2: 315 / 97 / MILP minimality | r1:110–111 | RESOLVED | r3:136–137 (already in r2:112–113) | The sentences are deleted and an explicit non-claim is added. No "97", "315", "minimum-size" or MILP claim remains in r3, LEM or the corollary note; the only MILP mention is inside the disclaimer. |
| MINOR 1: hash suffixes | r1:64; README:7 | RESOLVED | r3:82 (full digest, equal to the file); README:7 (`a39911fd…a3ff2`, equal to `moqls7-parent-verdict.md` a39911fd…446a3ff2) | — |
| MINOR 2: sets vs lists | r1:57 | RESOLVED | r3:66–67 | The table header r3:55 still reads "reduced lists". It is numerically correct at k = 2 (Theorem 3.1). |
| MINOR 3: minimum computes the key, not \|par\| | r1:44 | RESOLVED | r3:51–53, r3:68–71 | Matches net_canon.c:68–74 (minimum key; distinct count; 846720/distinct). |
| MINOR 4: solver versions not tied to runs | r1:64–65 | RESOLVED | r3:83, r3:84, r3:85–86; parent versions at r3:96–97 | The receipt's `solvers` field records cadical 3.0.1 (sha 601c9fa8…) and kissat 4.0.4 (sha 05d6f3e9…). |
| MINOR 5: absent LEMMAS references; unreceipted history | README:23; k1_sat.py:8,15; k1_encB.py:4; pattern_check.py:2; r1:59; r1:128 | RESOLVED-IN-SUBSTANCE | LEM exists and declares itself late documentation (LEM:3–4), with F1–F4 at LEM:38–52. History is relabelled as non-evidence at r3:77–78 and r3:158–160. The unreceipted "run reported violations" wording is removed. | Residue: k1_sat.py:15 cites a "K1 weight lemma, review/LEMMAS.md" that has no exactly named counterpart (the closest is LEM:26–36 W). Option `--w3` is disabled in production (k1_certify.py:52), so this is not load-bearing. The code is frozen. |

## Claude note `moqls7-k1-review-claude-v2.note.md` (sha256 9ed37460…fb68)

| finding | r1 locus | status | where in the current text | desk remark |
|---|---|---|---|---|
| 1: driver digest; summary does not bind the driver | r1:64 | RESOLVED-IN-SUBSTANCE | r3:82; r3:92–97 | The digest is fixed. r3 does not say that the A summary lacks a driver hash. The binding is now supplied by the parent byte-exact replay: receipt verdict 2a, and RESULT X1 (the on-disk driver reproduced every CNF and proof). |
| 2: README baseline digest | README:7 | RESOLVED | README:7 | — |
| 3: solver versions unreceipted | r1:64–65 | RESOLVED | r3:83–86 | — |
| 4: drat-trim control misdescribed/unreceipted | r1:70–71 | RESOLVED | r3:90–97 | As for Codex MAJOR 1. |
| 5: 97 / MILP minimum unsupported | r1:110–111 | RESOLVED | r3:136–137 | 315 is no longer stated at all, which is acceptable. |
| 6: missing LEMMAS.md | README:23 and code docstrings | RESOLVED | LEM (whole file; LEM:3–4 dates it) | — |
| 7: sets vs lists | r1:46, r1:57, net_canon.c:4, net_canon.c:7 | PARTIAL (harmless) | r3:66–67 | The table header r3:55 and the frozen comment net_canon.c:7 ("Theorem 3.2" for lists) are unchanged. They are numerically equivalent at k = 2. |
| 8: \|par\| is not a minimum; add free action | r1:43–44 | RESOLVED | r3:51–53, r3:68–71 | The flag/free-action argument is checked by the desk; see delta-check.md. |
| 9: incomplete trust base | r1:58–60 | RESOLVED-IN-SUBSTANCE | r3:73–78 | Coverage is conditioned on correct keys and multiplicities, and r3 cites parent route 1: 1b explicit automorphisms, 1d non-isomorphism, 1i full classification. Residue: RESULT.json is cited by path only, without its sha256 (f46a7416…6570). |
| 10: straightening, ray criterion, C0 unproved | r1:15–18 | RESOLVED | r3:8–14; LEM:8–14 | — |
| 11: word-proof row citations | r1:103–104 | RESOLVED | r3:129–131 | The desk re-derived rows 1+3, 6+7 and 2+5, and the contradiction with row 4. |
| 12: §8 case split and sequential step | r1:142–143 | RESOLVED | r3:172–175 | — |
| 13: C1 overstates F1–F4; evaluator vs encoders | r1:122–123 | RESOLVED | r3:148–150; r3:155–157 | 294 = 42·7, 84 = 42·2, 210 = 42·5 check. |

Totals:
- Codex: 2/2 MAJOR resolved. MINOR: 4 resolved and 1 resolved in substance (k1_sat.py:15 docstring residue).
- Claude: 13 MINOR, of which 10 are resolved, 2 resolved in substance (1 and 9) and 1 partial and harmless (7).
- UNADDRESSED: none.
