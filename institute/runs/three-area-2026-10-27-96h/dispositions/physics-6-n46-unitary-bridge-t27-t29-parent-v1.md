# AME(4,6) with support 46: maximal-coefficient counts 27, 28, 29 are impossible

**Disposition: same-harness written support, unconditional at its own scope.** For a normalized complex AME(4,6) state in any product basis with exactly `N=46` nonzero coefficients, the number `t` of coefficients of modulus 1/6 is not 27, 28 or 29. The proof uses only complex unitarity of the 2|2 flattenings. Since `N≥72−t` gives `t≥26`, and `|E|≤n²` gives `t≤32`, this bridge alone leaves `t∈{26,30,31,32}`. **Only together with the separately recorded, no-OLS(6)-conditional [t≤29 result](physics-6-maximal-coefficients29-parent-v1.md) does a 46-term state need exactly t=26.** No N=46 exclusion, 46-term witness, global bound ≥47, or novelty claim follows.

Native clock observed before composing: **2026-10-28T21:37:24-0700 PDT**, not an asserted file-creation time.

## Reconstruction

For a 2|2 cut, `U=6ψ` is a 36×36 unitary. A modulus-1/6 coefficient is the unique nonzero of its row and column, so removing the t maximal coefficients leaves an `n×n` unitary `V`, `n=36−t`, with every row and column degree at least two and `|E|=46−t` nonzeros. The three cases are `(t,n,|E|)=(27,9,19)`, `(28,8,18)`, `(29,7,17)`, with excess `|E|−2n` equal to 1, 2, 3.

Support lemmas for a unitary: two rows (or columns) cannot share exactly one nonzero column; connected support components are square; an excess-zero component is a full 2×2 block; in a connected component of size `m≥3`, degree-two rows have pairwise disjoint column pairs, each such pair is met by at least two higher-degree rows, and `m≤2r` for row excess r.

- **Excess one** forces `m≤2`, impossible for a positive-excess component: t=27 is excluded.
- **Excess two**: a size-4 component would have two degree-three rows meeting two covering column pairs in even numbers; so the component is a 3×3 block with eight entries and `n` is odd. `n=8` is even: t=28 is excluded.
- **Excess three**: sizes 4, 5, 6 are excluded by parity and pair-incidence counting, leaving a full 3×3 block plus 2×2 blocks; all degrees are at most 3.
- **t=29**: in every pair projection the residual E has seven cells with two or three extensions. Each symbol fiber varies in at least two other coordinates, so `2r≤3(7−r)` and `r≤4`; `r=4` would force at least eight projected cells. Hence every residual alphabet has exactly three symbols. Counting P words active at a coordinate (`4·11=44`) and at a coordinate pair (`6·2=12`), and `k−C(k,2)≤1`, gives `32≤|P|=29`, a contradiction.

Parent spot-checked the written identities: `2r≤21−3r` gives `r≤4`; `k−C(k,2)=0,1,1,0,−2`; `44−12=32>29`; the m=4 excess-two parity obstruction; and the `2n+3` size bound `m≤6`.

## Evidence and limits

Parent read the complete 85-LF [candidate](../../../../physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-n46-t27-t29-unitary-bridge-v1.md), SHA-256 `635e3ed2fe790efb70b297fa9dab119cbda31e0d256114e9591d89ce60014dde`, the complete 82-LF [proof review](../review-waves/f141-ame-n46-maximal-coefficient-bridge/proof-review-v1.md), `6bbdb240d7b97cc5986e10731f42408601e25c19842c8aa6eb425ca1ae7d0b1c`, and the complete [finite review](../review-waves/f141-ame-n46-maximal-coefficient-bridge/finite-review-v1.md). The proof review reports 0 FATAL / 0 MAJOR / 3 MINOR (compressed fiber-variation wording; the support source imports excess-one from a non-declared file, which the bridge re-proves; a sharpenable nonclaim). It reconstructed every lemma for all n, enumerated 0/1 supports exhaustively up to n=9 (e=1), n=8 (e=2) and n=9 (e=3) with reason-specific filters, checked the sharpness matrices in exact ℚ(√2) and ℤ[ω], and showed by exact arithmetic that the active-count inequality alone kills only the (3,3,3,3) profile, so the alphabet-size reduction is load-bearing. Its z3 UNSAT reports and one 600-second `unknown` are supplementary, not certificates. The finite review independently enumerated n≤4 supports, realized both survivor shapes by exact unitaries, built a rectangular-component false-positive control, and verified the 44−12 contradiction over all 40,920 incidence histograms, at exactly its conditional set-theoretic scope.

The three exclusions depend on no classical theorem. The t=26 conclusion inherits the no-OLS(6) and t≤30 boundaries of the imported t≤29 result. The t=26 branches other than the (4,4,4,4) alphabet case remain open; the author's ≥46/≥47 successor claims remain unadopted. All evidence is same-harness, not human, independent-model-family, formal/kernel or novelty acceptance.
