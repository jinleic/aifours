# Certified charts for the D2 bound — frozen specification v1

Worker `MathPhaseType3`. Written before the certified dual runs; the primal chart P was frozen in
`code/spec_primal_P_v1.json` before run c03. This document fixes the mathematics of every chart. Each chart's
machine-readable parameters (exact rational breakpoints, split weights, depth and evaluation caps) are in the spec
JSON named below. Library versions: `code/me3lib_v1.py` and `code/me3jet_v1.py` (primal);
`code/me3dual_v7.py` → `me3dual_v6.py` → `me3dual_v4.py` / `me3dual_v3.py`, with jets from `me3jet_v1.py` and
`me3jet_v2.py` (dual). Every leaf record has the format `cell path outcome`. The coverage audits
`code/check_cover_v1.py` (primal) and `code/check_cover_v2.py` (dual) replay the split rule from geometry alone.

## Common conventions

* T = 11/50. κ = 1/(1+T) = 50/61. Normal form: real pole 1, complex pair 1 + ξ, 1 + ξ̄ with ξ = δ − iω, δ ≥ 0,
  ω > 0. Ratios: r = δ/ω. Extreme-ray phase: φ = ωτ ∈ [0, θ₁(r)] (reductions L6).
* Arithmetic: python-flint 0.9.0 (Arb). All boxes have exact rational endpoints and enter as
  `arb(lo).union(arb(hi))`. Comparisons are certified ball comparisons. Working precision: 128 bits. A
  "mean-value form" (MVF) enclosure of a C¹ function F on a box B with midpoint m and half-widths h is
  F(m) + Σ_j ∂_jF(B)·[−h_j, h_j], where the ∂_jF(B) come from first-order jets evaluated on B. It is valid because
  F(x) − F(m) = ∫₀¹ ∇F(m + t(x − m))·(x − m) dt and every ∇F value lies in the convex balls ∂_jF(B).
* Split rule: bisect, at the exact rational midpoint, the coordinate maximizing width × weight (ties go to the
  lowest index). Child 0 is the lower half. Depth-first order. A box still undecided at max depth is a FAIL leaf.
  Any FAIL, or hitting the evaluation cap, means the chart is not certified.

## Chart P (primal; frozen in spec_primal_P_v1.json, run c03, coverage a01)

Domain: r ∈ [0, 3], ω ∈ [1/5, 40], φ ∈ [0, 31416/5000] ⊃ [0, θ₁(r)]. The quantities are the closed-form moments
a_k = 1 − Re(c ζ^{k+1}), c = (1 − ir)e^{(r−i)φ}, ζ = 1/(1 + rω − iω) (reductions Lemma 6.6),
G = 2a₀a₂ − (1+T)a₁², and D = a₀′a₁a₂ + a₀a₁a₂′ − 2a₀a₁′a₂ with a_k′ = ∂a_k/∂r at fixed (ω, φ)
(an exact sympy identity, run v01). Outcomes:
* INFEAS: φ_lo > π, r_lo > 0 and g_{r_lo}(φ_lo) > 1. Then φ > θ₁(r) for every box point, since θ₁ is decreasing
  and g_r is increasing on (π, 2π).
* SGE: a₁ > 0 and G > 0 (naive, else MVF), i.e. S > T at every box point.
* DPOS: a₀, a₁, a₂ > 0 and D > 0 (naive, else MVF), i.e. ∂S/∂r > 0 at fixed (ω, φ) at every box point.

## Dual charts (spec_dual_v1.json; driver cert_dual_v5.py)

For s ∈ [0, 1] (test centre μ = s/(1−s)), zz = 1/(1+ξ) and
W = zz(w₁ + zz(w₂ + zz·w₃)), with w₁ = κs²/N₁, w₂ = −2s(1−s)/N₁, w₃ = 2(1−s)²/N₁ and
N₁ = κs² − 2s(1−s) + 2(1−s)² > 0. This equals Q_T(μ(1+ξ))/Q_T(μ) for s ∈ [0, 1), where
Q_T(y) = (κy² − 2y + 2)/y³ is the Laplace transform of q(t) = (t−1)² − T/(1+T).
**Lemma D** (proof/me3-theorem-v1.md §2): if, for every s ∈ (0, 1), W lies in conv({0} ∪ {e^{−ξt} : t ≥ 0}), then
every nonnegative density with poles {1, 1+ξ, 1+ξ̄} has SCV ≥ T. Accepted certificates (finite convex combinations):
RADIAL (W = |W|e^{iα} with α ≥ 0 and |W| ≤ e^{−δα/ω}), SMALL (|W| ≤ e^{−2πδ/ω}), TRIANGLE
(W = a + b·e^{−ξθ′/ω}, a, b ≥ 0, a + b ≤ 1).

| Chart | Variables (exact ranges) | Assigned (δ, ω) set | Test(s) |
|---|---|---|---|
| SWC (corner) | s ∈ [0,1], δ ∈ [0, 3/10], ω ∈ [0, 1/5] | δ ≤ 3/10, 0 < ω ≤ 1/5 | series: Ψ_N + tail < 0 and Ig_N − tail ≥ 0 |
| SWB (B-edge) | s ∈ [0,1], δ ∈ [3/10, 64], ω ∈ [0, 1/5] | 3/10 ≤ δ ≤ 64, 0 < ω ≤ 1/5 | ω-expansion: B + ω_h²C₊ + E < 0, Im g/ω lower bound > 0 |
| G (general) | s ∈ [0,1], δ ∈ [0, 64], ω ∈ [1/5, 640] | same, minus P = {ω ∈ [1/5, 40], δ ≤ 3ω} (SKIP leaves) | SMALL / RADIAL / RADIAL-MVF / TRIANGLE |
| LW (large ω) | s ∈ [0,1], δ ∈ [0, 64], ν = 1/ω ∈ [0, 1/640] | δ ≤ 64, ω ≥ 640 | SMALL |
| LD1 (large δ) | s ∈ [1/16, 1], d = 1/(1+δ) ∈ [0, 1/65], β = arctan(ω/(1+δ)) ∈ [0, 15708/10000] | δ ≥ 64, all ω > 0 | RADIAL with α = β + arg P |
| LD2 (large δ, small s) | χ ∈ [0,1], ρ_t ∈ [0, 81/1040], β ∈ [0, 15708/10000]; s = χρ_t, d cos β = (1−χ)ρ_t | δ ≥ 64, all ω > 0, s ≤ 1/16 (SKIP leaves outside) | RADIAL with α = β + arg P̂ |

Chart details:
* **SWC.** g(ξ) = log W = Σ_{j≥1} c_jξ^j for |ξ| < min(1, 1/√B), with c_j = −2Re(p^j)/j + 3(−1)^j/j,
  p = (−A + i√(4B − A²))/2, A = (2κs² − 2s(1−s))/N₁, B = κs²/N₁ ≤ κ/(κ − 1/2). We have ξ^m = X_m − iωU_m, with
  X₀ = 1, U₀ = 0, X_{m+1} = δX_m − ω²U_m and U_{m+1} = X_m + δU_m, and |U_m| ≤ m|ξ|^{m−1}.
  * Φ/(ω|ξ|²) = −Σ_{j≥2} c_jU_{j−1} =: Ψ and Im g/ω = −Σ_{j≥1} c_jU_j =: Ig.
  * With N explicit terms (N = 20), the tails are bounded by 2ρ²(ρx)^{N−1}/(1 − ρx) + 3x^{N−1}/(1 − x) and
    2ρ(ρx)^N/(1 − ρx) + 3x^N/(1 − x), where x = √(δ_h² + ω_h²) and ρ = √(B_up).
  * Pass ⇒ Im g ≥ 0, so α = Im g ≥ 0 is an argument of W = e^g, and Φ = ω log|W| + δα < 0, giving RADIAL.
* **SWB.** For fixed real δ, put h(y) = g(δ − iy), y ∈ [0, ω]. Taylor's theorem with remainder gives
  * Re g(δ−iω) = g − ω²g″/2 + R_a with |R_a| ≤ ω⁴M₄/24;
  * Im g(δ−iω) = −ωg′ + ω³g‴/6 + R_b with |R_b| ≤ ω⁵M₅/120;
  * so Φ/ω = B + ω²C + E, where B = g − δg′, C = −g″/2 + δg‴/6 and |E| ≤ ω_h⁴(M₄/24 + δ_h M₅/120).
  The derivatives of g on the real axis are rational in (s, δ) and computed in real Arb. M_k bounds |g^{(k)}| on the
  rectangle [δ_l, δ_h] − i[0, ω_h] via |g^{(k)}| ≤ (k−1)!(|v₁|^k + |v₂|^k + 3|z|^{−k}), with
  v_{1,2} = κs/(κsz − (1−s)(1 ± i√(2κ−1))) = 1/(z − z_{1,2}), where z_{1,2} are the zeros of Nt(s, ·).
  Pass ⇒ Im g/ω ≥ −g′ − ω_h²|g‴|/6 − ω_h⁴M₅/120 > 0 and Φ/ω < 0, giving RADIAL.
* **G.** W is enclosed by the intersection of its naive ball with its complex MVF. The tests are:
  * SMALL;
  * RADIAL, with the argument branch fixed on the box by Im W > 0 (α = arg W), Im W < 0 (α = arg W + 2π) or
    Re W < 0 (α = arg(−W) + π); then ω log|W| + δα < 0, naive or MVF, where the MVF uses jets of log(±W) on the
    same branch and requires the midpoint to share it;
  * TRIANGLE with θ′ a rational approximation (from below, to 1e−4) of θ₁(r_mid). Its validity does not depend
    on θ′: e^{−ξθ′/ω} = e^{−rθ′}e^{iθ′} lies on the spiral for every θ′ ≥ 0.
  SKIP: a box with ω_h ≤ 40, ω_l ≥ 1/5 and δ_h ≤ 3ω_l lies in P.
* **LW.** zz = ν/(ν(1+δ) − i). SMALL: |W| < e^{−2πδν}.
* **LD1.** ζ = 1/(1+ξ) = d·cos β·e^{iβ}, W = ζP, P = w₁ + w₂ζ + w₃ζ², and δ/ω = (1−d)/tan β. Any α ≥ 0 that is an
  argument of W works; candidates are β + (principal arg P) when it is ≥ 0, β + Arg₊P, and finally
  Arg₊W ∈ [0, 2π) (ratio ≤ 2π/tan β_l).
  * For boxes with β_l = 0: Re P > 0 on the box, arg P(0) = 0 and the mean value theorem give
    α/tan β ≤ 1 + sup Im(P_β/P), with P_β = (w₂ + 2w₃ζ)·i·d·e^{2iβ}, and α ≥ 0 iff 1 + inf ≥ 0.
  * Boxes reaching β = 15708/10000 > π/2 use the fallback.
  * Test: |W| < exp(−(1−d)·ratio), with 1 − d taken as the box ball.
* **LD2.** P̂ = P/ρ_t² = [κχ² − 2χ(1−χ)(1−s)e^{iβ} + 2(1−s)²(1−χ)²e^{2iβ}]/N₁(s) and W = (1−χ)ρ_t³e^{iβ}P̂.
  The same argument choices as LD1 apply, with the factor 1 − d bounded by 1, which is conservative since the
  exponent is ≥ 0. SKIP: χ_lρ_{t,l} > 1/16 (s too large) or (1−χ_h)ρ_{t,l} > cos(β_l)/65 (d > 1/65), checked
  exactly or in balls.

## Coverage of all D-type pole configurations (ξ = δ − iω, δ ≥ 0, ω > 0)

* δ ≥ 64: LD1 ∪ LD2 (every s ∈ [0, 1], every β ∈ (0, π/2)).
* δ < 64 and ω ≥ 640: LW.
* δ < 64 and ω ∈ [1/5, 640]: P (if ω ≤ 40 and δ ≤ 3ω) or G.
* δ < 64 and ω < 1/5: SWC (δ ≤ 3/10) or SWB (δ ≥ 3/10).

Each dual chart covers all s ∈ [0, 1], hence all μ ∈ (0, ∞). The audits check that the leaves tile each chart and
that every SKIP leaf satisfies its geometric rule.
