**Verdict: ACCEPT.** I found no mathematical or code error in `checkerB/code/central_iv.py` or `cb_common.py` that would undercut Lemma E. Lemma E says ln F(n) < L* for every n with 0 < max_k |n_k − 1/9| ≤ 1/10000. There are two low-severity (P3) items below. Neither one affects the recorded PASS.

**Finding 1 (P3, confidence 0.9): some required checks are only Python `assert`s, and the output JSON prints fixed `True` values.**
- **Where:** `central_iv.py:158` runs `check_spectra()` and `check_arows()` only inside an assert. Other asserts are at 161–167, 180–186, 204 (Rbar = B·Xmin⁻¹·Bᵀ, which links the Hessian bound to the concavity step), 208, 222 (nlo > 0), 250 and 455. In `cb_common.py` they are at 45–47, 63, 97–98 and 168.
- **The JSON:** lines 472–475 write `True` literals for the identity flags. They are not computed results.
- **Effect:** under `python -O` or `PYTHONOPTIMIZE`, every one of these checks is skipped, but PASS (line 489) is still printed. The nlo > 0 assert is the only thing that ensures every n^u stays positive on the box and that the 1/nlo term really is an upper bound. For a larger `--r0` run under `-O`, a non-positive nlo would make the vertex matrices more negative, not less.
- **Recorded run:** not affected. I checked every asserted identity by hand. The evidence JSON also shows computed values: X0_diag is positive with X0_offdiag_zero true, nlo_min = 2491/22500, num_spectra = 36, and the coefficients of Ubar(0) are (−3, −1, 9/2), which match L*.
- **Fix:** replace these asserts with a `require(cond, msg)` helper that raises `SystemExit`. Store the computed booleans in "identities" and AND them into PASS. Abort if `sys.flags.optimize` is set.

**Finding 2 (P3, documentation only, confidence 0.8): the docstring cites a stronger lemma than CLAIM proves.**
- **Where:** docstring section D4, lines 27–28 and 46–47. It says "psi is concave on conv(S)" and refers to a "lemma L" that is defined nowhere.
- **Gap:** CLAIM Lemma A proves only (A1), strict concavity on open slices, and (A2), the tangent bound from interior points. Concavity along segments that lie inside faces of conv(S) is not established.
- **No logical gap:** the code needs only three things. (A2) makes an interior stationary point a global maximiser. The segment argument in CLAIM Lemma E step 2 gives uniqueness. Non-degeneracy the code certifies directly: X ⪰ Xlb ≻ Xmin ≻ 0 at every point of the Krawczyk box.
- **Fix:** reword D4 to cite (A1) and (A2) and spell out the segment argument. No code change is needed.

**Trace of derivations D1–D6 against the code (all correct):**

| Item | Code (central_iv.py unless noted) | What I checked |
|---|---|---|
| Spectra, weights, Φ | cb_common 22–48 | The degree in each variable is at most 5, so equality on the grid {0..5}⁴ proves the polynomial identity. |
| Pairing, C_u, A rows | cb_common 51–98 | Each pair (u,k)/(v,k′) maps back to itself; no entry pairs with itself; the A rows match (7.2). |
| D1–D3, weak duality | Y at 196, K_u at 197 | Exact. Any Y is valid, and this Y matches CLAIM's {0, ±75582/17915}. |
| D4, the stationarity system h | 301–339 | h(φ) = ½Bᵀ ln m̂ − 4φ equals Bᵀ∇ψ, because Bᵀ ln μ = 4φ and Bᵀ1 = 0. J_h equals Bᵀ·Hess ψ·Cov·B (I checked BᵀN⁻¹Cov·B = 4I), and also equals −X·(¼BᵀCov·B). Hess Ψ* = B·X⁻¹·Bᵀ. |
| Values at z = 0 | 178–187 | X0 = Bᵀ(900·W2⁻¹ − (2/5)I)B is positive definite. The first row of R0 matches CLAIM. |
| D5, region and grid | 199, 413–415, 362 | γ_i = r0·max_u Σ_j \|(BᵀK_u)_ij\| bounds c(t·K_u·η) for t ∈ [0,1]. The 8³ grid covers the c-box exactly, and each sub-box interval is rounded outward. |
| D5, Krawczyk | 357–383 | Requires the operator strictly inside the box, with det(Yk) ≠ 0 checked in interval arithmetic. c enters only additively, so one test covers every c in the sub-box. The centre is inside the box because the radius is at least 2⁻¹⁰⁰. |
| D5, Loewner bound | 385–399 | Directions are right: N ⪯ Nhi gives N⁻¹ ⪰ Nhi⁻¹, and mlo ≤ m̂ gives −½diag(1/m̂) ⪰ −½diag(1/mlo). mlo > 0 is checked at 391. The interval Gauss–Jordan step encloses the inverse of the point matrix Σ qhi·s·sᵀ. |
| Gershgorin and Sylvester | 400–403, 428 | Applied to one fixed symmetric matrix, Xlb − Xmin. Both tests must pass, and the run must have 0 failed sub-boxes. |
| Smooth branch | — | X ≻ 0 lets the implicit function theorem apply. (A2) plus uniqueness makes the branch the maximiser, so Ψ* is C^∞ near the c-box and the Taylor remainder is valid. |
| D6, concavity | 209–220, 257–275, 289 | I re-derived Haff and D_c. The nlo term bounds the log term from above. The bound matrix is affine in η and is checked at all 16 vertices by exact Sylvester tests of −Tm and −(Tm + δI), with δ = 1176209/10⁶. |
| Value and gradient at 0 | 228–251, 186, 208 | Ubar(0) = L* is checked exactly over (ln 2, ln 3, ln 5). The gradient is 0 because Σa_u = 0 and Σℓ_u = 0, which holds for any Y. |
| Final bound | — | ln F ≤ L* − (δ/2)\|η\|² < L* for every η ≠ 0. |

**Floating point, precision and box:**
- **Floats:** they are used only to choose δ (eigenvalues at 268–272), for the Newton centre and the preconditioner Yk (341–357), for the box radii and endpoints, and in reporting (`float()`, `floor_str`, contraction, `tau`, which is never used). None of them feeds a trusted inequality.
- **Precision:** interval and float precision are both 128 bits (456–457). The reset `mp.prec = 128` at line 268 affects only the eigenvalue estimate. The code is single-threaded.
- **mpmath 1.3.0 source:** integers convert with floor/ceiling rounding and mpf values convert exactly. `mpi_exp` and `mpi_log` round outward, and `iv.log` goes through `ctx.ln` to `mpi_log`. Division by an interval containing 0 returns (−∞, ∞), which makes the test fail rather than pass.
- **Box:** the n-box is [−1/10000, 1/10000]⁴ in η = (n00, n01, n10, n11) − 1/9, the same B0 as in CLAIM. On it every n^u ≥ 2491/22500. The script does not enforce r0 or ε itself, so you need to check `params` in the JSON (1/10000, 3/20, NC 8, 128 bits).
- **CLAIM §6 wording:** it describes the vertex argument through convexity of λ_max of Hess Ubar. The code instead checks the affine upper-bound matrix. Both arguments are valid.

**What I read:**
- All of `CLAIM.md`, `central_iv.py` and `cb_common.py`. Their SHA256 hashes match the pins.
- Checker B's own `central_iv_r0_1e-4_eps3_20_NC8.json`.
- The mpmath 1.3.0 files `ctx_iv.py` and `libmpi.py` in `random5reg-colour/.venv`.

I ran nothing. I did not read `code/cert_ldc3.py`, any of checker A, any reviews, or other checker B files.

**What remains assumed:**
- Lemma A, both (A1) and (A2), including its positivity of the minor polynomials.
- That mpmath 1.3.0 rounds `mpf_exp`, `mpf_log` and basic arithmetic correctly in the requested direction, and that Python `Fraction` arithmetic is exact.
- Lemma F (L* = ln F(n*)), and Lemmas D and G for the rest of the domain.
- That the recorded run did not use `-O`. The JSON cannot show this; it matters only for the asserted identities, which I checked by hand.

Overall confidence: 0.85.
