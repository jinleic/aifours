# Independent degree-three tensor certificate

Date: 2026-10-14 (America/Los_Angeles).

This supplement was derived by the enclosing worker while HMZ ran, without reading the actor's live files. HMZ independently obtained the same coefficient-three result by the representation-theoretic exact-sequence proof in `STRUCTURAL.md`. The new tensor certificate cross-checks its crucial finite Levi claim; it is not a Lean formalization or a proof of universal Serre equality.

## Exact family theorem and hypotheses

For every pair of positive integers r,s, set

    A(r,s) = [[2,-1,-1],[-1,2,-1],[-r,-s,2]].

In every full characteristic-zero realization, the positive Serre and maximal Cartan-disjoint ideals agree in every degree with alpha_3<=3. This is a written consequence of the established coefficient-one and coefficient-two theorems, the exact radical recurrence, the accepted uniform rank-three height-seven theorem, and the finite-Levi argument below. No literature-novelty claim is made. It does not improve the already accepted A_one band alpha_3<=4.

The finite Levi on nodes 1,2 is sl3(C). Its level-one module V is the adjoint representation, with e3 identified with E31. Bracket generation and the actual Levi action give a surjective Levi-equivariant map L_k(V)->S_k, where L_k is the genuine bracket-length component of the free Lie algebra. Its kernel is Levi stable. Both modules are finite-dimensional, so Weyl complete reducibility makes S_k a direct-summand quotient. Consequently absence of a trivial constituent in L_k(V) passes to S_k. This use of finite-dimensional characteristic-zero semisimplicity is essential; arbitrary quotients in a nonsemisimple category would not justify the implication. No irreducibility of the nonsymmetrizable whole algebra is assumed.

The full Cartan realization, including the extra direction for singular A(1,1), is retained. This argument restricts the action to the finite Levi; it does not replace the full Cartan by the row span of A.

## Actual Lie-space certificate

The ordered sl3(Q) basis is

    E12, E23, E13, E21, E32, E31, H1=E11-E22, H2=E22-E33.

The checker derives its Cartan weights and F1=ad(E21), F2=ad(E32) actions from 3-by-3 matrix commutators. It does not relabel arbitrary vector spaces as a Lie algebra. The free-Lie components are bracket spans in the tensor algebra, using the characteristic-zero free-Lie embedding.

The separately implemented `produce_levi.py` and `check_levi.py` use different reconstruction routes:

- Producer: standard Lyndon bracketing, triangular coordinates and integer Bareiss determinants.
- Checker: direct tensor expansions, the span of every left-normed length-three bracket, separately reconstructed matrix actions, sparse rational rank, exact tensor-identity checks of all matrix entries, and rational Gaussian determinants. It imports no producer module.

The final independent check obtained:

| Quantity | Exact value |
|---|---:|
| Dimension of L3(ad sl3) | 168 |
| Weight-zero dimension | 18 |
| Two lowering target dimensions | 13 and 13 |
| Joint lowering rank | 18 |
| Selected 18-by-18 determinant | 288 |

The selected zero-based rows of the 26-by-18 matrix are `0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,20`. Thus no nonzero weight-zero vector is killed by both Levi lowerings. In a finite-dimensional sl3 module such a vector would be invariant: each sl2 restriction makes a lowest vector of weight zero trivial. Therefore L3(V), and hence S3, has no trivial constituent.

## Exhaustive first-defect argument

If an extra relation exists in the downward-closed band alpha_3<=3, choose one of least total height inside the band. The established coefficient-two theorem forces alpha_3=3; the coefficient-zero/one theorem forces a=alpha_1>=2 and b=alpha_2>=2. Every simple lowering kills the vector, because it decreases height while remaining inside the band. The first two rows of A alpha<=0 give

    2a-b<=3,  2b-a<=3.

If a>b, then a>=b+1>=3 and 2a-b>=a+1>=4, a contradiction; similarly b>a is impossible. Hence a=b is 2 or 3. These are all possibilities, including every high-coordinate case.

- (2,2,3) is excluded by the inherited height-seven theorem.
- (3,3,3) has Levi weight zero and would give a nonzero invariant in S3, excluded above.

This proves the stated family band, not all levels and not all GCMs. The existing uniform-height-seven receipt is hash-bound by the checker at SHA-256 `7275abb3ecfc9b8c0efc4c437274229cec6be4245ae5674d69ef79df7b48c44d`; its large polynomial certificates were not rerun here.

## Rejection controls and the next structural obstruction

The checker rejected a changed lowering coefficient and an omitted source vector. Each single lowering separately has rank 13, so dropping either lowering genuinely destroys injectivity on the 18-dimensional source.

It also independently checked a nonzero degree-four weight-zero Lie vector, expressed by 35 bracket trees and 208 nonzero tensor terms, killed by both F1 and F2. This refutes the proposed all-level extension of the *no Levi invariant* mechanism. This supplementary checker does not test its omitted lowering D3 or survival in a Serre quotient, so its receipt correctly says it is not a counterexample. The separate HMZ level-four scripts do analyze the unique invariant line and all other primitive spaces for r,s>=4; those are separate, stronger evidence with their own receipts.

The remaining universal obstruction is injectivity of the actual omitted lowering on all surviving Levi-lowest multiplicity spaces at every level, plus arbitrary GCMs without a symmetrizable single-node complement. No finite-field rank defect is promoted to a characteristic-zero relation.

## Exercised command

From this directory, the following command completed successfully:

    python3 produce_levi.py --output level3-certificate.json
    python3 check_levi.py level3-certificate.json --output levi-independent-check.json

The receipt is `levi-independent-check.json`. Both programs use one Python process and standard-library exact arithmetic. For replay, choose a new output receipt path; neither program overwrites existing evidence.
