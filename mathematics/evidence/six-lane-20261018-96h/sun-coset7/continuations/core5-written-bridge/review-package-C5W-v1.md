# C5W written review package v1 — a written Core(5) theorem [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T17:42:26-0700, immediately before this exclusive create. Owner SunM13MixedFibres. Packaging used
  only sha256, byte counts and raw line ranges; no scientific computation. The parent owns reviews and verdicts.
- **Candidate:** K/C5W-v1.md, sha256 2e4b42b2ce88cad9f13b56b027fb10ea1082fb3d20df8acbbdff5667d4db5c69 (150 lines, 14,878 B). **Scope:** K/C5W-SCOPE-v1.md, sha256 3daa4a45e36530c3d66e7e4b02cf3f6b4fd69365716b68c5b7ff2f4cde57a24f,
  frozen before proof-v4 and erratum v3 were read; it lists all prior exposure (including the old bridge's rule names and
  counts, which are never used).
- K = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/core5-written-bridge; ROOT = /Users/jinleic/repos/aifours. Exact absolute paths and whole-file hashes are in the JSON manifest.

## 1. Claim and boundary
Theorem C5W proves the proof-v4 statement Core(5) for every finite group: every Core(5) pattern (alpha, E2, E3) is
impossible, so the S-D class is empty as well. It replaces the finite bridge of proof-v4 section 4 (and makes section 6 a
redundant cross-check) by a written argument using only Sun(2) (proved inside) and Zhu's Sun(3): no Sun(4)-(6), no
minimal-order frame, no engine/checker/certificate/count, no Sun(5) instance. Verification replacement of a previously
claimed case (Gong): no novelty. CANDIDATE_UNVERIFIED pending two-family review and the parent; the composite written
Sun(5) proof stated in the corollary is conditional on that review.

## 2. Verbatim theorem and proof (candidate lines 110-122)
```text
**Theorem C5W [CANDIDATE_UNVERIFIED].** Core(5) holds: no finite group has five pairwise disjoint left cosets with indices
4 r_i and r_i pairwise coprime. The proof covers every placement of E2/E3 (absent, equal, distinct), r_i = 1, and all
exponents and cofactors.
*Proof.* Let Gamma be such a configuration and Gamma* its inverse (Lemma INV: same r_i, E2, E3; alpha*_ij = 1 whenever
alpha_ij = 3).
- **Case 1: E2 and E3 are not two distinct vertices.** Choose v = E2 if E2 exists, otherwise v = E3 if E3 exists, otherwise
  any vertex. Every neighbour of v is plain (the markers are unique, and if both exist they equal v). If some
  alpha_vj != 3, Lemma PR for Gamma is a contradiction. Otherwise all alpha_vj = 3, so all alpha*_vj = 1 != 3, and Lemma PR
  for Gamma* is a contradiction.
- **Case 2: E2 = a and E3 = b exist with a != b.** If some alpha_ap != 3 (p in P), Lemma AR for Gamma is a contradiction.
  Otherwise all alpha_ap = 3, so all alpha*_ap = 1 != 3, and Lemma AR for Gamma* is a contradiction. QED

**Corollary (bridge replacement).** In the accepted proof-v4 section 7, the dichotomy "certificate orbit / S-D orbit" can be
```

## 3. Proof map (candidate line numbers)
Target and import table 16-33; setting, MU, markers 34-43; INV and FC 44-66 (FC from line 52); local gcds G1, G2, V2
67-76; Lemma PR 77-87; Lemma AR 88-108; theorem 109-121; corollary and S-D consistency check 122-131; DAG and checks 132-150.
Mechanism: at an apex v the neighbours carry labels r_j alpha_vj and masses alpha_vj/4; a plain neighbour with multiplier 1
is isolated, plain 2s pair only with 2s, plain 3s only with 3s. A row with only plain neighbours fails the count unless all
four multipliers are 3; at E2 (when E2 != E3) the count fails unless all three plain multipliers are 3. Inversion turns a
multiplier 3 into 1, so the inverse configuration (same markers) then fails the same lemma.

## 4. Review questions
1. Exact quotation of Core(5) and E2/E3 (proof-v4 lines 49, 113); no hypothesis dropped or added.
2. FC: fibre construction, Sun(2) proof, and that only 2- and 3-subsets of fibre sets are constrained.
3. INV: the inverse is a Core(5) configuration with the same r_i and markers; alpha + alpha* <= 4.
4. Local gcds G1, G2, V2 and the valuations for plain neighbours and for b at the E2 apex.
5. Lemma PR for every (n_1, n_2, n_3) with n_3 <= 3, and Lemma AR for every beta and every (n_1, n_2, n_3) with n_3 <= 2:
   check feasibility on ALL admissible sets (zero-weight items included) and every objective value.
6. The theorem's two-case split (markers absent/equal versus distinct) and the choice of v in Case 1.
7. The corollary's conditional wording; that no bridge, certificate, count or S-D step is a premise.
Return FATAL/MAJOR/MINOR per group with exact file:line and the smallest repair; an empty list is valid.

## 5. Excerpt sources (inclusive raw physical lines; whole-file sha256)
| source | sha256 | lines | role |
|---|---|---|---|
| K/C5W-v1.md | 2e4b42b2ce88cad9f13b56b027fb10ea1082fb3d20df8acbbdff5667d4db5c69 | 1-150 | NEW whole proof: MU, INV, FC (Sun2 proved + Zhu Sun3), local gcds, Lemmas PR and AR, Theorem C5W, corollary, DAG |
| K/C5W-SCOPE-v1.md | 3daa4a45e36530c3d66e7e4b02cf3f6b4fd69365716b68c5b7ff2f4cde57a24f | 1-55 | frozen scope (before proof-v4 was read); full exposure list incl. old bridge counts (not used) |
| ROOT/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transitions-sun5-moq-corner-20261019-1735-v1.json | 59e3fb4319f20f578e8d504682343421d82bbc094e33eace85c996b3c261a7ca | 1-27 | parent authority (key math1) |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset5/proof-v4.md | 3d17efcc034cca643515e581fa4667515086d0844a58b951e2641080d6c94516 | 37-61, 103-113, 201-207, 243-278 | Core(5) statement and R0/R1 (37-61); minimal frame and E2/E3 pattern definition (103-113); S-D definition (201-207, not used); closure and dependencies (243-278) |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset5/rules-v1-erratum-v3.md | 1b3e126e1c398a71401b4c7e13cbc19c276befe095bb1c0043450c3cd425e8ed | 1-18 | cumulative rules erratum (read; none of its items is load-bearing here) |
| ROOT/institute/runs/six-lane-2026-10-16/review/sun-coset5-parent-verdict-v1.md | 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301 | 1-18, 30-35 | accepted Sun(5) scope and limits (the counts in lines 18-23 are exposure only, never premises) |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-v1.md | 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c | 18-71 | origin of the fibre count and inversion; re-proved in the new file at k = 5 with Sun2/Sun3 only |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-erratum-v1.md | 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5 | 10-32, 47-63 | mandatory elementary overlays E1-E3, E6-E7 |
| ROOT/institute/runs/six-lane-2026-10-18-96h/review/sun7-lfc-inv-parent-verdict-v1.md | 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18 | 16-19 | accepted LFC/INV statements; its Sun(5)/Sun(6) provenance is NOT imported |

## 6. Packaging metadata
Manifest K/review-excerpts-C5W-v1.json, sha256 00dbb6ba489b61afd7b4aeda9322f0f0d5066c6cfa08bae358e452d33286208d (3,281 B): 14 ranges from 9 sources as
{path, sha256, start, end}. Selected raw bytes 42,949; package plus selected source 50,152 B (<= 100,000). The full
new proof is included; no new node is replaced by a context-only declaration.
