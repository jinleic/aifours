# reductions/ — STATUS v3

Written 2026-10-18 06:41 PDT (host clock) by `MathPhaseType3.ME3Reductions`. This file supersedes `STATUS-v2.md`
(kept, sha256 a644d430…d27e) only for the items below. Correctness only.

**Fix map.** `proof/reductions-v3.md` differs from `proof/reductions-v2.md` (bd497389…1e3f, untouched) in exactly two
places:
* a v3 status paragraph at the top;
* v2 LF373 (proof of Theorem L4(4)), which is now v3 LF384–385.

The fix answers finding 5 (MINOR) of `institute/runs/six-lane-2026-10-16/review/me3-charts-v2-delta-codex-v1.note.md`
(sha256 df03a74a1be4f5c50d931463507f7e2859010b96ca0e60895167dcd2fe2ce474). v2 called h/32 "the resultant"; the correct
statement is Res_x(q, 24y − x(9 − x)² + 24) = 432·h, whose monic normalization is h/32. The remainder proof of
h(Δ3) = 0 is unchanged. `diff -u` has exactly 2 hunks (`proof/reductions-v3.diff-from-v2.txt`). The earlier code checks
were already correct: they compared the *monic* resultant with h/32 (`exact-certs-v1` X_sympy_resultant_monic_eq_h/32;
`ctl-b-v1`). Only the v2 prose was wrong.

**Run `resultant-check-v1`** (exit 0; SymPy exact integers and rationals, no floats, AST self-scan):
* (a) Res = 13824y³ − 62208y² + 58320y − 11664 = 432·h. The 6×6 Sylvester determinant gives the same value.
* (b) The monic normalization of Res is h/32.
* (c) Wrong control: "Res == h/32" evaluates to False, with residual 13823y³ − 124407y²/2 + 1866105y/32 − 373221/32.
* (d) LC_y(Res) = 24³ = 13824.

| New file | sha256 |
|---|---|
| `proof/reductions-v3.md` | e5c75b24298f5b362b6c9f4e9c6fc572249cf459389ac5c80ff047694819b15c |
| `proof/reductions-v3.diff-from-v2.txt` | a8cd11c5b9a1d1def9cbccbc41dd98c810c0b97946fcb50366fd32baa3d58251 |
| `code/resultant_check_v1.py` | 23278390e4e4bc46f1328c3b2e8a9c27be6f8b76aaf401bfa9864ef961ff99cd |
| `runs/resultant-check-v1/resultant_check.json` | 5aa3c233691748dace65aef70167eca4c19f637c004d80bce35b2b671e68fe3a |
| `receipts/resultant-check-v1-pre.json` | 006a228290fdcafcee7944296987ef81fef0e5f8d59904d93f543c61dfd9da72 |
| `receipts/resultant-check-v1-post.json` | abf345a6a1afc5c302e47ede8715904407ddee6bfa20225801e8cdb5255e7031 |
