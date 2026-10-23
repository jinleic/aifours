# phys-2 slice-concavity lemma: parent verification (2026-10-17 00:06 PDT)

**Status: parent-verified component, not a certificate of the Maximum Hypothesis.** The lemma replaces the
"numerically confirmed" concavity of ln G̃ used by Díaz–Kaporis–Kemkes–Kirousis–Pérez–Wormald (2009, §7)
inside the inner fibre maximisation. Claude hostile review is pending, bundled with the colouring certificate.

## Statement (lane README §2, checkpoint 1)

For μ ∈ (0,∞)⁴ indexing the cells (−1,−1),(−1,1),(1,−1),(1,1), let S be the 36 nonnegative integer
2×2 matrices with entry sum 5 and no zero row or column, w_s = 5!/∏ s!, Φ(μ) = Σ_s w_s μ^s,
m_k = Σ_s w_s s_k μ^s and S2_kl = Σ_s w_s s_k s_l μ^s. With μ(m) the inverse of μ ↦ m on the open moment
cone, ψ(m) = Σ_k m_k(½ ln m_k − ln μ_k(m)) is strictly concave on every slice {Σ_k m_k = c} of the open cone.

## Analytic bridge, re-derived by the parent

1. With θ = ln μ, m = ∇_θ Φ(e^θ) and ∂m/∂θ = S2. S2 ≻ 0 because the spectra span ℝ⁴ (e.g.
   (4,0,0,1), (0,4,1,0), (1,0,0,4), (0,1,4,0) have determinant −15² ≠ 0) and μ > 0. Hence θ(m) is smooth
   with ∂θ/∂m = S2⁻¹.
2. Homogeneity of degree 5 gives S2·1 = 5m and Σ_k m_k = 5Φ, so S2⁻¹m = ⅕·1. Therefore
   ∂ψ/∂m_j = ½(ln m_j + 1) − θ_j − ⅕ and **Hess ψ = ½D⁻¹ − S2⁻¹**, D = diag(m).
3. Pencil argument: A = ½D⁻¹ and B = S2⁻¹ are positive definite, and A m = ½·1, B m = ⅕·1, so m is a
   generalised eigenvector with eigenvalue 5/2; the remaining three eigenvectors are B-orthogonal to m,
   i.e. lie in 1⊥. Hence A − B ≺ 0 on 1⊥ iff the other three eigenvalues are < 1, iff (dual pencil,
   y = Ax) S2 − 2D ≺ 0 on m⊥.
4. Since ℝ⁴ = span(1) ⊕ m⊥ (as m·1 = 5Φ ≠ 0), and M := 5Φ(2D − S2) + 3mmᵀ satisfies M1 = 0 and
   uᵀMu = 5Φ·u'ᵀ(2D − S2)u' for u = α1 + u', u' ∈ m⊥: S2 ≺ 2D on m⊥ iff M ⪰ 0 with kernel span(1),
   iff any 3×3 principal block of M is positive definite.
5. A homogeneous polynomial with only strictly positive coefficients is positive on (0,∞)⁴, so positive
   coefficients of the three leading principal minors give the conclusion for every μ > 0.

Closure: concavity (not strictness) passes to the closed slice by continuity, as the lane states.

## Polynomial step, recomputed independently

[`check_slice_concavity_independent.py`](check_slice_concavity_independent.py) uses plain integer dictionaries
(no python-flint or sympy, no lane code). Receipt: [`slice-concavity-parent-check-v1.json`](slice-concavity-parent-check-v1.json),
status `POLYNOMIAL_POSITIVITY_PASS`: |S| = 36; Φ equals its inclusion–exclusion closed form; M is symmetric and
M1 = 0 exactly; for each of the four choices of dropped index, P1, P2, P3 are homogeneous of degree 10, 20, 30
with 154, 949 (943 when dropping index 0) and 2766 terms, all coefficients strictly positive (minima 200,
100000, 5·10⁷). The lane's two implementations reported the same term counts for its chosen index.

## What this does not establish

It does not certify the Maximum Hypothesis, the outer bound over the overlap polytope, the central concavity
box, boundary layers or the bridge from F to the conditional colouring proof. It removes one numerical
assumption from the inner maximisation step.
