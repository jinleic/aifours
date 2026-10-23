# RUH2 checkpoint 003 (closing): labelled partial + exact residual frozen; slice parked

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T17:28:46-0700. Previous checkpoint-002.md SHA256
999cf408f9d449bc4e14ad305a017fa24c60332259b54f54bb43036472790d08 (17:21:35). Scope frozen 17:07:02 before derivation.

Actual outcome (CANDIDATE_UNVERIFIED, LABELLED PARTIAL): Lemma L (strong windows for sets avoiding the super-heavy run, SH range
p>=13, 5<=e<=(p+2)/3); Theorem A: R-UH for 3<=c<=e-1 on the whole SH range; Theorem B: e=5 (kappa=p-5), every prime p>=13,
3<=c<=9; Corollary B (with accepted UH-A): the whole cell kappa=p-5 is empty for p>=13. Residual: (R1) 3e>p+2 (all of p=11,
p=13 with e=6,7, ...); (R2) SH range with e>=6 and e<=c<=2e-1. Inputs NF, GRX (if), RS(b), CD; UH-A only for Corollary B;
UH-SH/MW re-derived, not imported; KP3/KP4/R7 not cited. All case work by hand; no computation of any kind.

Frozen files (exclusive create x, then chmod a-w) in
/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/upperhalf-RUH-round2/:
- RUH2-scope-v1.md                  b1cdfaeee6db5985a2af1f8f98c4f66cd7a8e8e8fe77cbebab372f270d4c5dd0
- proof-RUH2-v1.md                  f391b08f2df02036b4a7cfc66c1f118e7f20c6dfb8d89af2a10e121ea58df4e2
- erratum-1-proof-RUH2-v1.md        a3c673137ed35b81220b51f9e19997f0c31b10a32bcb5dc7b222e641f50f3f61
- residual-RUH2-v1.md               267bd0354543568a1dbb7b3aa56327afedb415335b96f204c92b3aa3b435059b
- erratum-1-residual-RUH2-v1.md     52871fb8f9dc796a35fef55367764335506131856e1e24a96e3c204027ac94ac
- review-excerpts-RUH2-v1.json      c2238172ff26829aaeb5840336c77036337a7c2c0358695880de2ab21222bb2e (20 ranges, 19 files)
- review-package-RUH2-v1.md         086cb82461882609522180d63c30b564cc9d7cc6cdd5be8e4dfc1a10a003785f
Package + manifest + LF-numbered excerpts = 68,199 bytes (<100,000). Manifest file hashes re-read just before this file:
20 of 20 equal. Author line audit after freezing found two justification gaps in Theorem B (c=5 pair s=-4; free-length
range at c=9) and one wording slip in the residual note; all fixed by errata without editing frozen files.

Blocker: mathematical, residual R1/R2 (missing claims MC1, MC2 in the residual note). Next: parent-owned dual-family review
and verdict; slice parked.
