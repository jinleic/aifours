# AME(4,6): support 45 is impossible when t≤28

**Disposition: same-harness written support for the f226 two-case exclusion.** Let a normalized complex AME(4,6) state have `N` nonzero coefficients in any one local product basis, and let `t` be the number of coefficients of modulus `1/6`. If `t≤28`, then `N≠45`. This conditional implication follows from a single actual 2|2 unitary flattening and elementary row orthogonality; it does not itself use no-OLS(6), a solver, or a separate support enumeration.

For `U=6ψ`, every modulus-one entry occupies a singleton row and column. Removing the `t` singleton blocks leaves an `n×n` unitary, `n=36−t`, whose rows and columns each have at least two nonzeros. Hence `N≥72−t`. At `N=45` and `t≤28`, only two integer cases remain:

| t | n | Remaining nonzeros | Exclusion |
|---:|---:|---:|---|
| 27 | 9 | 18 | Every residual row and column has degree two. Two rows cannot share exactly one nonzero column, so the support splits into full 2×2 blocks; the dimension must be even. |
| 28 | 8 | 17 | Excess one forces one row with three supported columns and all others with two. Covering those three columns requires two distinct two-subsets, whose rows then share exactly one nonzero column, contradicting orthogonality. |

Applying the separately adopted `t≤28` statement to all AME(4,6) states excludes `N=45`. Combining with the separately adopted lower bound `N≥45` gives the conditional **global bound `N≥46`**. Both applications inherit the f113 classical no-OLS(6) and prior-`t≤30` provenance; the f226 review did not reprove those imports. This record does **not** combine the result with the independently audited exclusions of 46 and 47 into a global `N≥48` claim. That final union requires a separate prospective audit. No minimum, new witness, novelty or priority is claimed here.

## Source and verification

- Source: `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261029-n45-two-case-using-adopted-t28-v1.md`, SHA-256 `429ad666e0f44b7d93219a6efb9ffdd4f3dfe4acb763f4c1fb39588e3ce10634`, 46 LF. The parent displayed raw lines 1–15, 16–30, 31–45 and 46.
- Frozen manifest: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f226-ame46-n45-two-case-t28/manifest-v1.json`, SHA-256 `8ed3da45796cea53d3808e4377d1d18386a5bab0aea7b4455efe022da5c8fb45`. Review: adjacent `review-v1.md`, SHA-256 `946a4b4977cfde885330a74f857c398904b46f937008583b7b0811df1003dc30`, 78 LF. Parent displayed all review lines in raw windows 1–15 through 76–78. The review reports **0F/0M/0m** for the stated implication and separate lower-46 deduction, conditional on their named imports.
- Parent checked `45≥72−t ⇒ t≥27`, both residual sizes and the row-support contradictions. The reviewer-owned exact control completed with exit 0 on smaller support graphs and reason-specific negatives; it did not enumerate the target dimensions and is not a substitute for the written proof. The review did not independently reprove the classical theorem or either adopted bound.

Parent observed `/bin/date` `2026-10-29T13:55:31-0700 PDT` before this disposition. Same-harness support is not human, independent-model-family, formal/kernel or novelty verification.
