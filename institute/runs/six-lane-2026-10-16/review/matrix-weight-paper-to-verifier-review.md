# Matrix-weight candidate: paper-to-verifier audit

Read-only reviewer `MatrixWeightReferee` returned **corepoint-sufficient** after 3m32s. It inspected the
pinned table and verifier against AMH arXiv:2603.19901v1, but ran no code. This is a source/transcription
audit, not a runtime or novelty certification. Parent runtime evidence is separate in
`matrix-weight-parent-verification-v1.json` and `matrix-weight-parent-psd-control.json`.

## Verdict and findings

A nonnegative integral table satisfying exactly Eqs. (31)–(35), with ordinary weights (38), suffices
for the paper's **putative** integer matrix-weight question. No actual stabilizer group or projector
is required by that question. No load-bearing omission or normalization mismatch was found.

- Gamma counts ordered Pauli-label pairs with five coordinate categories. There is no extra factor
  2, 6 or 2^24. The paper's displayed Eq. (41) has unspecified `a_i` and an apparently duplicated
  multinomial/factorial expression. The intended combinatorial count used here matches the authors'
  `gamma_field` / `multinomial_field` implementation in their public `fun.jl`.
- Alpha/beta substitutions and the factor `3^((i+j)/2−t)` match Eq. (42). Nonzero table entries have
  even i and j, so all relevant blocks are rational; no surviving square-root terms are discarded.
- The old pinned worker `alp` is not literally Fraction-only: zero binomial summands with negative
  powers can introduce Python floats. The parent compared 96,409 nonzero contributions to a distinct
  integer constructor with no mismatch; its all-integer polynomial constructor is load-bearing.
- The full legitimate index set and normalization, anticommutation, triple symmetry of **x**,
  projector row sums, KL, purity, self-dual, additive, Type-II and specified weight equations are
  covered. Eq. (28)'s ordinary/diagonal identification follows from triple symmetry and equal gammas.
- All 169 blocks are represented, including zero blocks. The worker's maximum-diagonal Schur
  complement routine handles zero pivots correctly. Parent verification additionally reconstructs
  explicit rational positive Gram decompositions.
- The additional LP inequalities in Remark 5 follow here from self-duality and even support.
  Further SDP constraints and the complete hierarchy mentioned there are **not** certified.
- Eight-dimensional-family and genus-two CRT/height claims are separate obligations and are not
  necessary for the single-point result.

## Exact supported statement

The pinned table is a putative integral matrix-weight enumerator satisfying AMH Eqs. (31)–(35) and
weights (38). Parent independent exact replay passed all 20,475 admissible orbits and all 169 PSD
blocks; it also rejected a linear-feasible PSD-only negative control. This proves the stated finite
moment-feasibility claim, not existence of `[[24,0,10]]_2`, a complete quantum-code hierarchy result,
novelty, or human peer review.

Primary sources: [paper §3.3](https://arxiv.org/html/2603.19901v1#S3.SS3),
[Open Problem 1](https://arxiv.org/html/2603.19901v1#Thmproblem1),
[Appendix A](https://arxiv.org/html/2603.19901v1#A1),
[authors' normalization code](https://github.com/ganglesmunne/SDP_bounds_on_quantum_codes_rational_certificates/blob/main/fun.jl).
