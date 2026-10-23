## Verdict: ACCEPT-WITH-FIXES

**For the stated invocation `1/10000 3/20 12 4`, the central strict bound is mathematically justified, conditional on Lemma A and the other disclosed analytic inputs below.** I found no normalization, interval-enclosure, inverse-order, Hessian-sign, or parameter-coverage defect invalidating that invocation. There is one fail-open argument-handling defect in the checker’s general PASS verdict.

### Finding — [P2] Reject negative subdivision counts before returning PASS

**File:** `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/colour-complete-claim-snapshot-v1/code/cert_ldc3.py`  
**Lines:** 389–391  
**Priority:** 2  
**Confidence:** 1.00

Static control-flow counterexample, not executed: with arguments `1/10000 3/20 -1 -1`, both grid constructions and both Cartesian-product loops are empty. Consequently, neither `(Q)` nor `(C)` checks any box, both `failed` counters remain zero, and line 391 selects `PASS`. This permits a certificate verdict without parameter coverage. Reject negative subdivision counts at argument parsing—preferably require `NC > 0` and `M > 0`—and require the expected positive box totals before declaring PASS. This defect does **not** invalidate the specifically reported `NC=12, M=4` replay.

## Soundness audit

References below are to `code/cert_ldc3.py`.

### 1. Exact response and normalization

- **Lines 81–111:** Moments, covariance, `X0`, `Xmin`, `Rbar`, `G`, `Y`, `Kq`, `lq`, and `Qq` are computed using exact rationals. The identities connecting `R0` to `B3 * X0.inv() * B3.T`, and the projector to `B3 * BtB.inv() * B3.T`, are asserted exactly.
- The factor **`1/9` in `X0` is correct**: the Hessian at the normalized mean `(5/4)1` is `1/9` times the Hessian at `(5/36)1`.
- The exact response `Y = -(45/4) G⁻¹ bm` is consistent with the linearized dual stationarity equation. Its optimality is not a soundness premise: weak duality permits any `Y`.
- The unnormalized stationarity equation with **`mu4=1` is correct**. Normalizing `m(mu)` to total mass five changes `½ log m − log mu` only by a multiple of `1`, which `B3.T` annihilates.
- Strictly speaking, the **maximizer and Hessian**, not the value of `Ψ*` itself, depend only on `c=B3.T z`. The value additionally has the exact affine shift `Ψ*(z+t1)=Ψ*(z)+5t`. The code’s linear Taylor term accounts for that shift; this causes no gap.

### 2. `(Q)` coverage and parametric Krawczyk

- **Lines 356–365:** Each half-width is an exact maximum of absolute row sums times `r0`. Therefore the resulting `c`-box contains every `B3.T K_u eta` for every class and every real `eta∈B0`.
- With `NC=12`, the rational endpoints partition the **closed** box into all `12³=1728` subboxes. Shared boundaries are included; this is not merely a grid-point check.
- **Lines 209–247:** `G0` encloses the residual for the entire parameter subbox, while `dG` encloses the Jacobian throughout the positive candidate `mu`-box. The derivative is correctly taken with respect to the first three **unnormalized** coordinates.
- The monotone corner evaluations are valid: `m`, `Jm`, and `dS2` have nonnegative coefficients on positive inputs.
- The acceptance condition is strict interval containment, not a midpoint or floating-tolerance test. For each fixed parameter in the subbox, it supplies the Krawczyk existence condition.
- Although `Ya` has no separate determinant assertion, this is not a missing condition here: strict containment of the interval Krawczyk image in a nondegenerate box forces a weighted contraction bound for `I−Ya J`, hence nonsingularity of `Ya J` and `Ya`.
- Every resulting root lies in `Kv`; extracting its exact dyadic endpoints before calling `check_X` is valid. Global uniqueness and agreement between neighboring parameter boxes then follow from Lemma A, not from the approximate Newton solver.

### 3. Mean-value Hessian enclosure and inverse order

- **Lines 252–301:** The enclosed matrix is correctly
  \[
  X(\mu)=-\frac{\sum m(\mu)}5\,B_3^T
  \left(\tfrac12\operatorname{diag}(1/m)-S_2^{-1}\right)B_3.
  \]
  The normalization factor and both product-rule terms in `dX` are correct.
- The rational center is asserted to lie in the root-enclosure box. Thus the coordinate segments used by the mean-value enclosure remain inside the derivative-enclosure domain.
- The spectrum-weight ratios produce the claimed Loewner enclosure of `S2`. Its inverse perturbation is bounded entrywise by
  \[
  \frac{\epsilon_L}{1-\epsilon_L}\,\|S_{2,c}^{-1}\|_F.
  \]
  This follows from the inverse Loewner inequalities and the spectral-norm bound; the Frobenius norm is a valid upper bound.
- `sqrt_up` is not trusted merely because of its floating safety factor: **line 73 checks its squared rational value exactly**.
- **Lines 289–308:** The congruence matrices are exact rational encodings of chosen floating eigenvectors, with exact nonzero-determinant checks. Orthogonality or eigenvector accuracy is unnecessary. The symmetrized interval Gershgorin bounds correctly certify positivity of the actual symmetric matrix.
- Since `Xmin` is positive definite for the stated positive `eps`, the implication
  \[
  X\succeq X_{\min}
  \quad\Longrightarrow\quad
  B_3X^{-1}B_3^T\preceq \bar R
  \]
  uses the **correct inverse-order direction**.

### 4. `(C)`, zero identities, and strictness

- **Lines 313–347:** `HAFF0` and `DC` are the exact coefficients of the Hessian of the polynomial part of `Ubar`. The entropy contribution is correctly `+(3/2) A_u A_u.T / n^u`.
- With `M=4`, **lines 377–380** cover all `4⁴=256` closed eta subboxes. Positivity of every denominator is checked before use.
- The congruence/Gershgorin test is applied to **minus** the Hessian, so its positive result has the required negative-definiteness meaning.
- **Lines 112–116** establish the exact cancellations needed for `grad Ubar(0)=0`.
- The value identity is supplied analytically by Lemma F:
  \[
  \bar U(0)=\ln900+\tfrac52\ln(5/4)-3\ln3=L^*.
  \]
- Every segment from `0` to `eta∈B0` remains inside `B0`; its corresponding `c`-segment remains inside the certified `c`-box. Taylor’s upper-bound direction is correct, and multiplication by `n^u>0` preserves it.

Consequently, conditional on the disclosed global inner-maximization input, negative definiteness and the exact critical-point identities give
\[
\ln F(n)\le U(\eta)\le\bar U(\eta)<L^*
\]
**for every nonzero real eta in the closed box**, including arbitrarily small eta and points on its boundary.

### 5. Floating-point and Arb conversion audit

No floating result is used directly to establish a trusted positivity inequality:

- Newton iterations, midpoint residual estimates, initial radii, and floating box endpoints only choose candidate data subsequently checked by Arb.
- At 128-bit precision, finite binary64 centers and preconditioner entries are represented exactly as Arb points.
- Floating eigenvectors are converted to exact rational matrices; nonsingularity and the resulting inequalities are checked independently.
- `rat_lower` and `rat_upper` use exact dyadic midpoint/radius extraction, not nearest-rounded floating endpoints.
- Rational-to-Arb conversion and `union` enlarge enclosures; the radius constructor supplies an outward error bound.
- Arb `> 0` means positivity throughout the ball; NaN does not satisfy it.
- The floating `min_margin_lower_bound` fields at **372 and 386** use nearest-rounded conversion and are therefore **diagnostic, not directed-rounded certificates**. They do not participate in PASS or in the strictness argument.
- Runtime measurements are likewise diagnostic.

The source executes the certification loops sequentially and fixes Arb precision at 128 bits. NumPy/BLAS behavior affects candidate selection, not the validated inequalities. The argument assumes the assertion guards are enabled.

## Inputs not established by this checker

| Input | Disclosure in `CLAIM.md` | Status in this review |
|---|---|---|
| Translation of the original objective, spectra, overlaps, and pairing constraints into `S`, `W`, `A`, and `C_u` | §1 and §3 notation | Checked for consistency with the supplied statement; original PDF not independently audited. |
| Exponential-family parametrization, entropy Hessian formula, and scaling law | Lemma A | Written mathematical inputs; the formulas used here are consistent. |
| **Global slice concavity and boundary tangent bound, A1/A2** | Lemma A, including the positive-minor certificate filename | **Remaining external computational premise.** The polynomial-minor evidence was outside this assignment and was not inspected. |
| Weak pairing duality | Lemma B, with proof | Written input; normalization and cancellation are correct. |
| Exact equality `F(n*)=e^{L*}` | Lemma F, with proof | Written input; baseline arithmetic is consistent. |
| Parametric Krawczyk theorem, implicit-function/envelope formulas, inverse-order and norm inequalities, Sylvester/Gershgorin, Taylor and strict-concavity implications | Named or formulated in Lemma E | Standard analytic inputs; their required conditions were traced above. |
| Correct Python/Fraction, FLINT/fmpq, and Arb arithmetic and comparison semantics | Libraries are identified; not formally proved in CLAIM | Trusted implementation base, not independently verified library binaries. |

**Without A1/A2, PASS only validates local stationary branches and their local matrix bounds; it does not by itself certify the global `Ψ*` upper bound.** CLAIM discloses that dependency.

## Actual read scope

Read all **392 lines** of the assigned source and the relevant definitions and Lemmas A, B, F, and E in `CLAIM.md`. Consulted primary Arb/Python-FLINT API documentation and narrowly scoped library-source sections for conversion, comparison, and matrix-addition semantics. No `checkerB/` files or independent reviews were inspected. No tests, builds, edits, or certificate executions were performed; the successful parent replay is supplied evidence, not a new result of this review.

**Overall correctness:** incorrect as a general checker because of the vacuous-PASS defect; no defect found in the specified-parameter central proof.  
**Overall confidence:** 0.97.
