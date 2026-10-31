# Candidate global AME(4,6) support lower bound 46

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 19:10:09 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently accepted, formally verified, or novelty-cleared. This strengthening depends on `frontier-20261028-global-ame46-support-lower45-v1.md`, SHA-256 `26a4115ff62f56320af2647c550072255d0ab7c6c90de49ef83025d9219a1121`; the sharp `2n+2` unitary-support lemma `frontier-20261028-unitary-two-excess-classification-v1.md`, SHA-256 `4a6d012d39ae8ae3acd0bb2ba04d0f79c824a9002633a0d2a45d91038119bec0`; and the `2n+3` lemma `frontier-20261028-unitary-three-excess-classification-v1.md`, SHA-256 `a37a958ab0fca716ddeddd527a5e0cc4e8e35938c628f42e264f815488742bc2`. All are unreviewed dependencies. The only named classical mathematical import inherited through them is no-OLS(6).

## 1. Claim

Every normalized complex AME(4,6) state, in every product basis, has at least **46** nonzero coefficients. The published 60-term example then gives `46≤m≤60` for the global minimum. [Pandya arXiv:2610.16673v1 §VI](https://arxiv.org/html/2610.16673#S6) reports lower bound 38; comparison to that statement is not an independently completed priority or novelty audit. No 46-term witness, formal proof, or independent acceptance is claimed.

## 2. Four possible 45-support cases

Let t count coefficients with modulus 1/6, E be the remaining nonzero support, and `n=36−t`. As derived in the 42-review dependency, in **every** 2|2 flattening `6ψ` the maximal coefficients are singleton rows and columns, and removing them leaves an n×n unitary with no singleton row or column. Every two-coordinate projection of E has n pair values, every pair value has at least two E extensions, and `N≥72−t`. The lower-45 candidate excludes N≤44.

For N=45, `t≤30` and `N≥72−t` give `t∈{27,28,29,30}`:

- t=27 gives n=9 and `|E|=18=2n`. A residual unitary with no singleton and exactly `2n` nonzeros is a disjoint union of 2×2 blocks, so n must be even; impossible.
- t=28 gives n=8 and `|E|=17=2n+1`, excluded by the one-excess unitary-support lemma.
- t=30 gives n=6 and `|E|=15=2n+3`, excluded for even n by the sharp three-excess lemma.
- t=29 gives n=7 and `|E|=16=2n+2`. This last case is excluded below.

## 3. Residual alphabets for n=7

By the sharp two-excess classification, a 7×7 residual unitary with 16 nonzeros consists of one 3×3 eight-entry block and two full 2×2 blocks. In particular **every residual row and column has degree at most three**. Since every coordinate pair is a row or column projection in some cut, no pair value has more than three E extensions.

The incidence lemma in the 42-review packet says a residual coordinate with r values satisfies `2r≤3(n−r)`. For n=7, `r≤4`. Suppose a coordinate A takes four residual values. Each of its four fibers must vary in at least two other coordinates. Because every occurring pair has at least two E extensions, a fiber that varies in one coordinate contains at least four E entries. Since |E|=16, all four fibers contain exactly four entries.

Fix any other coordinate j. If j were constant in an A-fiber, that single pair `(A,j)` would have all four fiber entries as extensions, contradicting the degree-at-most-three conclusion. Thus j varies in **each** of the four fibers and the pair projection `(A,j)` has at least `4·2=8` values, contradicting n=7. Therefore every residual alphabet has at most three values.

Every pair projection has seven values. If any coordinate took at most two values, its projection with another coordinate of size at most three would have at most six values. Hence **each of the four residual alphabets has exactly three values**.

## 4. Active-coordinate counting contradiction

Call a coordinate of a maximal P word *active* if its symbol occurs in the corresponding residual alphabet. Since a maximal coefficient is isolated, the P and E projections partition all 36 pairs in each 2|2 row system.

For each party i, there are `6·3=18` possible pairs with its active symbol and a symbol at any fixed other party. Exactly n=7 of these pairs occur in E; all other 11 are uniquely represented by P. Thus exactly **11** P words have party i active.

For each pair i,j, the two active alphabets give `3·3=9` possible active/active pairs. Exactly seven occur in E, leaving exactly **two** uniquely represented by P.

For a P word x, let `k(x)∈{0,1,2,3,4}` be the number of its active coordinates. The two counts above imply

`Σ_{x∈P} k(x)=4·11=44`,

`Σ_{x∈P} C(k(x),2)=6·2=12`.

But `k−C(k,2)` takes the values `0,1,1,0,−2` for k=0,1,2,3,4; it is at most 1. Since |P|=29,

`32 = Σ_{x∈P} [k(x)−C(k(x),2)] ≤ 29`,

contradiction. Thus t=29,n=7,|E|=16 cannot occur. All four 45-support cases are excluded, yielding the candidate lower bound N≥46.

For reuse, the same reasoning gives a general necessary condition. If residual alphabets have sizes r_i and all pair projections have size n, then

`Σ_i (6r_i−n) − Σ_{i<j}(r_i r_j−n) ≤ t=36−n`.                  (1)

It counts only P positions and uses no chosen state, amplitudes, phases, or finite-field assumptions.

## 5. Exact controls and limits

`frontier-20261028-active-count-control-v1.py`, SHA-256 `dccb5f9afa3ccefbb096f1c4dfe5992cd72644410eeb0e293ec30009a69e84b4`, checks the five integer per-word weights, the `44−12=32>29` instance and a nearby formal n=6 count that the inequality does **not** reject. Receipt `frontier-20261028-active-count-control-v1.json`, SHA-256 `c49c56b773400248fb7ee2c11e3bb42bdd78c824d2bf68a6bf3d55a5bceee7b6`. This is a finite arithmetic control, not a substitute for the universal residual-geometry proof.

The n=7 maximum-degree conclusion is dependent on the written 2n+2 classification, and the even n=6 exclusion on the written 2n+3 classification; both require independent review. The bound is global only if all earlier 42, 44, and 45 candidate arguments and their named no-OLS(6) import are valid. No unreviewed claim is adopted merely by this packet.
