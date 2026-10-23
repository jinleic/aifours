# KII-W written review package v1 — full KII exclusion [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T17:32:08-0700, immediately before this exclusive create. Owner SunM13MixedFibres. Packaging used
  only sha256, byte counts and raw line ranges; no scientific computation. The parent owns reviews and verdicts.
- **Candidate:** K/KII-W-v1.md, sha256 b25d4274d09b24b7eaa346d5287af95cee65f99ae4939c4bd32f20eda2eb5c03 (192 lines, 18,750 B). **Scope:** K/KII-W-SCOPE-v1.md, sha256 6ed700c2b7660889c60759c55424ccd8a945c685b3bbc2c2385fa1451cb7e1e6
  (frozen before derivation; discloses that only StageB output COUNTS, never certificates/code/leaves, were ever seen).
- K = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/kii-written; ROOT = /Users/jinleic/repos/aifours. Exact absolute paths and whole-file hashes are in the JSON manifest.

## 1. Claim and boundary
Theorem KII-W: README class KII (CE with a = 2) is empty in every group with finite-index subgroups, for every exponent,
cofactor and marker placement. A written VERIFICATION REPLACEMENT for the KII branch of StageB, not a new class closure.
**Imports: only Sun(2) (proved inside) and Zhu's Sun(3); no Sun(4)-(7), no computer-assisted theorem, no StageB, no K52-W.**
Every new claim CANDIDATE_UNVERIFIED pending two-family review and the parent. No full Sun(7), novelty, Lean or human claim.

## 2. Verbatim theorem and proof (candidate lines 162-171)
```text
**Theorem KII-W [CANDIDATE_UNVERIFIED].** No group with finite-index subgroups contains seven pairwise disjoint left cosets
whose labelled index tuple lies in README class KII. This covers every exponent and cofactor, every position of i*, t
and of the high 5-part, and both values of every multiplier.
*Proof.* By R0 take G finite; Lemma SHAPE gives the normalisation and markers; choose c as in section 3. By (I1) one of the
two actual families Phi in {alpha, alpha*} (the configuration or its inverse, both KII with the same markers and the same
apex c) has Phi_yc = 1; work in it. If a plain entry equals 5: either some entry differs from 5 (Lemma B) or all four
equal 5 (Lemma Z, which passes to the other family). If no plain entry equals 5 and some plain entry is 3, or at least
three plain entries are 1, Lemma A applies. Otherwise every plain entry is in {1, 2, 4} with at most two 1s, and the Main
Lemma applies since phi = 1. Every case contradicts FC23. QED

```

## 3. Proof map (candidate line numbers)
SHAPE and markers 37-57; R0, MU, INV 59-76; FC23 78-91; apex choice, labels, GCD table and K1-K6
93-120; Lemmas B, A, Z 122-131; Main Lemma 133-160; theorem 161-171; DAG, Sun boundary, checks 172-192.
Mechanism: pick a C-apex c != i* (c = t when t is a C-vertex other than i*), so x has mass 1/2 and every C-neighbour other
than i* is plain (r coprime to 30). In the family (actual or inverse) where alpha_yc = 1, a plain 5 is isolated from all
non-5 C-entries (B), odd plain entries are isolated from x (A), an all-5 row inverts to an all-1 row (Z), and otherwise
y-centred or half-weightings give objective >= 1 (Main). Sun(3) enters only to bound sets of pairwise gcd <= 2 by two.

## 4. Review questions
1. SHAPE (both directions) from the README CE/KII definition; the re-derivation of R1(7)(II) uses Sun(2) and gcd <= 6.
2. Apex choice and plainness; x has multiplier 1 at c in BOTH families; the inverse is KII with the same markers.
3. FC23: only 2- and 3-subsets of actual fibre sets; Sun(2) proof; strict gap from the omitted own fibre.
4. GCD table and K1-K6, including min(v_2 r_x, v_2 r_(i*)) <= 1, t = y / t = i* / t = c, and gcd(X, I) >= 5 when gamma = 5.
5. Every weighting in B, A, Z, M1-M4d against ALL admissible sets (zero-weight items included) and every objective.
6. Exhaustiveness of the theorem's case split, and (I1)/(I2) applied to the actual inverse.
Return FATAL/MAJOR/MINOR per group with exact file:line and the smallest repair; an empty list is valid.

## 5. Excerpt sources (inclusive raw physical lines; whole-file sha256)
| source | sha256 | lines | role |
|---|---|---|---|
| K/KII-W-v1.md | b25d4274d09b24b7eaa346d5287af95cee65f99ae4939c4bd32f20eda2eb5c03 | 1-192 | NEW whole proof: SHAPE, R0/MU/INV, FC23 (Sun2+Sun3 only), apex c and GCD table, Lemmas B/A/Z, Main Lemma, Theorem KII-W, DAG |
| K/KII-W-SCOPE-v1.md | 6ed700c2b7660889c60759c55424ccd8a945c685b3bbc2c2385fa1451cb7e1e6 | 1-50 | frozen scope; exposure disclosed; no pre-freeze sketch |
| ROOT/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transitions-sun-physics-20261019-1700-v1.json | b29119aa12222bf31cdaf6afdb59e81bc58ad2525fa9e08c5384bf86bc7d6bf2 | 1-23 | parent authority (key math1) |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset7/README.md | 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1 | 9-29, 31-67, 85-97 | CE, P0/P1, R0, L0.x, R1(7) incl. (II), class table line 96; Sun(3)/(4) import line 15 |
| ROOT/institute/runs/six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md | 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35 | 16-24, 44-47, 58-60 | acceptance of the reduction/notation (A-1) and imports; no class exclusion used |
| ROOT/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-v1.md | 77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee | 7-17 | multiplier notation and range (L0.3) |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-v1.md | 45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c | 18-45, 52-71 | origin of the fibre count and inversion (re-proved in the new file; general LFC(c) not imported) |
| ROOT/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-erratum-v1.md | 7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5 | 10-32, 47-63 | mandatory elementary overlays E1-E3, E6-E7 (L0.3, Sun(2), own fibre, index-defined classes, double cosets) |
| ROOT/institute/runs/six-lane-2026-10-18-96h/review/sun7-lfc-inv-parent-verdict-v1.md | 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18 | 16-23, 33 | accepted scopes of LFC/INV and the R0 lift; its Sun(5)/Sun(6) provenance is NOT carried into FC23 |

## 6. Packaging metadata
Manifest K/review-excerpts-KIIW-v1.json, sha256 beff4ff703de889dc3f299175945f3d7675bde5b3191280f3e1d6114efd85aae (3,742 B): 16 ranges from 9 sources as
{path, sha256, start, end}. Selected raw bytes 46,179; package plus selected source 52,771 B (<= 100,000). The full
new proof is included; no new node is replaced by a context-only declaration.
