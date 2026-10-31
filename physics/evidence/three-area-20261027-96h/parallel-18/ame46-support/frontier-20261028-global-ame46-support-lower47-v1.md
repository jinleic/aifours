# Conditional candidate global AME(4,6) support lower bound 47

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 20:08:27 PDT 2026`; not an exact completion time. **WRITTEN synthesis plus exact finite-support enumeration**, not independently accepted, formally verified, or novelty-cleared. Every premise below is an explicitly pinned, unreviewed author candidate; review of the entire dependency chain is required. The inherited classical mathematical import is Tarry's no-OLS(6) theorem.

## 1. Claim and evidence boundary

The combined candidate says every normalized complex AME(4,6) state has at least **47** nonzero coefficients in every product basis. The published 60-term example would then yield `47≤m≤60`; no 47-term state or exact minimum is claimed. [Pandya arXiv:2610.16673v1 §VI](https://arxiv.org/html/2610.16673#S6) reports lower bound 38; that is only a cited-source comparison, not a completed priority/novelty audit.

The proof closes the conditional N=46 case. Its all-`(4,4,4,4)` branch uses exact finite enumerations; the rest is written linear algebra, combinatorics and F₂ rank. Same-harness finite checks are not independent scientific review or formal proof.

## 2. Pinned dependency map

1. `frontier-20261028-global-ame46-support-lower46-v1.md`, SHA-256 `36586d04dd9e6cdc2bdf11e1bfcb2f85c07890cbf902386fef264260876b73eb`: candidate `N≥46`, maximal-entry/residual framework and its pinned 42/44/45/one- and two-excess dependencies. It also cites the three-excess lemma. None is adopted here.
2. `frontier-20261028-global-ame46-maximal-coefficients29-v1.md`, SHA-256 `2520967103592e125423a5a22c0ed5e86236582f149fb9375cb0c6f2070b476c`: candidate global `t≤29`, independent of total support.
3. `frontier-20261028-unitary-three-excess-classification-v1.md`, SHA-256 `a37a958ab0fca716ddeddd527a5e0cc4e8e35938c628f42e264f815488742bc2`: candidate classification of a residual unitary with `2n+3` nonzeros; for n=7 it has row/column degree at most 3.
4. `frontier-20261028-n46-residual-no-hamming1-v1.md`, SHA-256 `98bb82499cda7135db96de89b6a7fb9901274c892af3fd125ac7a9d446992b0d`: candidate that, in the N=46,t=26 residual, no two nonmaximal words differ in exactly one coordinate. Its free-fiber component proof inherits no-OLS(6) and the n=2/n=4 residual contradictions.
5. `frontier-20261028-n46-five-symbol-noh1-exclusion-v1.md`, SHA-256 `846de5872ef83ba18dfbbb8b2225cdb24dff146db4af776ffe3bbb76d46a0333`: written F₂-rank candidate excluding every residual-alphabet profile containing 5, assuming item 4.
6. `frontier-20261028-n46-residual-alphabet-exclusions-v1.md`, SHA-256 `966f125ed180bb48b2848b0900ca37a5f4ee53fab44d5c937050a529cba6e2fc`: the source-free active-incidence exclusion of profile `(3,4,4,4)` and supporting residual reductions.
7. `frontier-20261028-n46-4444-noh1-exclusion-v1.md`, SHA-256 `6f697745893f123feda438af137088b8175e42b17b0632f00beb4bf3819e2da8`: written normal form plus two exact finite enumerations excluding `(4,4,4,4)`, assuming item 4.

## 3. Why an N=46 candidate has t=26

Let t be the number of coefficients of modulus 1/6, let P be those positions, E the other nonzero positions, and `n=36−t`. The residual framework gives `N≥72−t`, `t≤29`, and in every cut an n×n unitary residual with no singleton row/column. For N=46, `26≤t≤29`.

- t=27 gives n=9, `|E|=19=2n+1`, excluded by the one-excess unitary lemma.
- t=28 gives n=8, `|E|=18=2n+2`, excluded for even n by the two-excess classification.
- t=29 gives n=7, `|E|=17=2n+3`. Item 3 gives maximum residual pair degree 3. If a coordinate had four residual symbols, its four fibers each contain at least four E points; since every pair degree is at most 3, every other coordinate must vary in each such fiber, giving at least eight pair values, not n=7. Thus all residual alphabets are at most 3, and every pair must have seven values, forcing all four alphabet sizes to be 3. Pair partitioning between E and P gives 11 P words active at each party and two P words active at each pair. Therefore `Σ_{x∈P}(k(x)−C(k(x),2))=4·11−6·2=32`, but every summand is at most 1 and |P|=29, contradiction.

Thus t=26,n=10 and |E|=20. Every pair projection of E has ten values and every value has exactly two E extensions.

## 4. Exhaustion of N=46 residual alphabets

Every residual symbol fiber varies in at least two coordinates and contains at least four E words. Thus each local residual alphabet has size at most five. It has size at least two, and the product of every two local alphabet sizes is at least ten, since their pair projection has ten values.

If any alphabet has size five, item 5 excludes the profile: no-distance-one makes each of its five balanced four-word fibers a parity fiber, and hence the partner incidence matrices are pairwise orthogonal over F₂. The pinned proof excludes the possible partner sizes by rank, kernel-partition and, where needed, the three-qubit shadow-rank bound.

If no alphabet has size five, all sizes are 3 or 4: size two cannot pair with an alphabet of size at most four. Two size-three alphabets cannot pair because `3·3<10`, so, up to order, the only possibilities are `(3,4,4,4)` and `(4,4,4,4)`.

Item 6 excludes `(3,4,4,4)` by maximal-P activity counting: every P word would have one or two active coordinates, there would be no singleton-active P word at a size-four party, and for any active symbol of such a party its required singleton count would be `2d−5=0`, impossible for integer residual degree d.

Item 7 excludes `(4,4,4,4)` conditional on its exact enumeration. Maximal-P counting permits either all four local residual degree types `Y=(2,2,3,3)` or one `X=(2,2,2,4)` and three Y. No-distance-one makes low four-word fibers parity sets and makes high fibers pair-injective. The normalized all-Y case has 2,975 pair-incidence patterns, 10 high-fiber signatures, and 40 support candidates in a conservative superset; all 40 have a unique row/column overlap in each cut. The normalized one-X case has 240 incidence patterns and 10 admissible high-projection graph triples, none with the required eight-word pair-injective cover. Such unique overlaps contradict unitary orthogonality.

Thus every N=46 profile is excluded conditional on the pinned arguments. Combined with item 1, the candidate lower bound is N≥47.

## 5. Finite evidence and requested attack surface

The all-`(4,4,4,4)` result is supported by two separately structured exact programs, not a SAT-status claim:

- balanced-subset implementation `frontier-20261028-n46-4444-noh1-enum-v1.py`, SHA-256 `96c519e0169380d333fd7a1414925e0decca2335c6cdf0ac4846c377e7d4ee4c`, receipt SHA-256 `45e5a0fbdb0b13dcd3f26905dde807b7067dc6ada115a965ed2e81cd66dbd21e`;
- independent partial-Latin/edge-cover replay `frontier-20261028-n46-4444-noh1-latin-replay-v1.py`, SHA-256 `eb413c112a0398500f9642b9f39fb5ef20079f95aa09da29c95c27d298025425`, receipt SHA-256 `50a20186279163febfd47f586c37172d90ecd751a9cad19ddac4b7e7497ddd13`.

The size-five F₂-rank claims have exact graph controls in `frontier-20261028-n46-fivefiber-orthogonality-v1.py`, SHA-256 `ef8d368fbca44bf133756946649c638e793d6e4a31abb74a817f8f93c2a6efff`, receipt SHA-256 `ddc0347c41fcd968d7d5af5f28bce408c8c9b5bf450d6832ea2bde73b9270de9`.

Review must independently attack, at minimum: all earlier global-bound premises; the free-fiber propagation, block separation, and bipartite phase argument in item 4; the F₂ rank/kernel partition in item 5; the at-most-one-X degree deduction; the incidence-orbit and 144 high-fiber normalization; and independent exhaustive replay of both all-Y and one-X branches. The 40-support enumeration intentionally includes 30 cross-fiber-distance-one supports, all still rejected, rather than assuming them away. No priority or novelty inference follows from these same-harness computations.
