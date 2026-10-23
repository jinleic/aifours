# CUT-erratum-v1 — mandatory wording overlay propagating the parent S56W erratum (no mathematical change)

- **Written:** `/bin/date` read at 2026-10-19T18:12:49-0700, immediately before this exclusive create. Owner SunM13MixedFibres.
- **Applies to:** `CUT-v1.md` (sha256 3d0a98fb647c2c5939c84501f5da1c5c76a8073a0d876e407ceac51af50fe8f8) and `review-package-CUT-v1.md` (sha256 8d83cb52767d58bd2fb51513ecb8dd5eef582552f6f5da77c8773b70b67e15a2), both byte-identical.
- **Source:** parent erratum RUN/review/sun56-S56W-parent-erratum-v1.md, sha256 b2299b6ffd37fcc1a68370fd0c75abf4a3590fc8d6fad41b0ef7e5da39f40aae
  (recorded 2026-10-19T18:08:37-0700; Codex 0F/1M/1m on S56W), and the transition
  RUN/control/written-k7-direct-marker-residual-scope-v1.json (bfaea95f…39bb), item "mandatory_first".
  RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h.

## Acknowledgement
The parent erratum (i) adds the standing hypothesis "PAIRWISE DISJOINT left cosets" to S56W's lemma setting (S56W line 35),
so S56W's L3 (Lemma K) and K2 hold only for pairwise disjoint cosets and their unrestricted standalone statements are
withdrawn (every application in S56W already had the hypothesis); and (ii) replaces S56W's "verbatim"/"word-for-word" claims
by "identical mathematical index-gcd statements and scope, with notation normalized"; trailing clarifications and sharpness
prose are not claimed literally identical, and substitution stays limited to the precise theorem statements. H5, H6 and
S56W remain PENDING; no historical record changes. I accept both items for S56W and carry them into CUT as follows.

## Replacements in CUT
| # | location | old | new |
|---|---|---|---|
| Q1 | CUT-v1.md line 23 (import map M2) | "whose statements are verbatim the accepted ones" | "whose statements are identical mathematical index-gcd statements with the accepted ones, with the same scope and notation normalized (S56W read with its parent erratum b2299b6f…0aae; trailing clarifications/sharpness prose not claimed literally identical)" |
| Q2 | CUT-v1.md ledger row HS (section 2) | "S56W (9dfa360e…b894) sections 1-7" | "S56W (9dfa360e…b894) sections 1-7 read with parent erratum b2299b6f…0aae (standing pairwise-disjoint hypothesis for L3/K2; statement identity in the normalized sense)" |
| Q3 | CUT-v1.md line 127 (requested check 2) | "the statement identity behind M1, M2, M3" | "the statement identity behind M1, M2, M3 (for M2: identical index-gcd statements and scope, notation normalized)" |
| Q4 | review-package-CUT-v1.md line 22 | "M2 (S5W/S6W verbatim accepted statements)" | "M2 (S5W/S6W: identical index-gcd statements and scope with the accepted ones, notation normalized, per the S56W parent erratum)" |
| Q5 | CUT-v1.md section 7 (citation substitution list) | (add) | Substituted citations must cite S5W/S6W WITH the S56W parent erratum; S56W's L3/K2 are cited only for pairwise disjoint cosets. |

Unchanged: the import map's content, the ledger's dependency findings, the conditional composite SUN7-COND, the gate table and
all residuals (A2X, H5, H6, S56W and the composition review remain pending). No acceptance, no full Sun(7) claim, no
history change, no F-1 cure. No scientific computation.
