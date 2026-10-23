# Minimal SCV of ME(≤3) — integration proof, version 1 (DRAFT: dual certificate status filled in v2)

Worker `MathPhaseType3`, lane `mathematics/evidence/six-lane-20261016/me3-minimum-scv/`, 2026-10-18 PDT.
**Status: worker candidate, unreviewed. Correctness only — no novelty, priority or "first" claim.** Scope: the frozen
contract's statement (HSTZ 2016 Definitions 1, 2, 5; constant v_cos as the cos-family minimum).

## 0. Statement

**Theorem.** Every continuous X ∈ ME(≤3) satisfies SCV(X) = m₀m₂/m₁² − 1 ≥ v_cos, where
v_cos := min_{ω>0, φ∈ℝ} SCV(e^{−t}(1 − cos(ωt − φ))). The minimum is attained by the cos family, and every law whose
density has a complex pair with real part strictly beyond the real pole (case D2) has SCV > v_cos.

Ingredients:
* Written reductions from the reductions subtree (§1, by the subagent `ME3Reductions`, independently re-read here).
* Two elementary written lemmas: Lemma D in §2, and the Lemma M continuation in §3.
* Certified ball-arithmetic computations over compact charts, with exact-rational box records and independent
  coverage audits (§4).

The only imports are ordinary background (finite-dimensional convexity, the mean value theorem, Taylor's theorem
with remainder, power series of log) and the correctness of the Arb ball arithmetic library (python-flint 0.9.0).

## 1. Reductions imported (reductions/proof/reductions-v1.md, sha ad6c5091…5536; STATUS.md sha 61776330…2c76)

* **L1–L2.** Continuous ME(≤3) densities are exactly the normalized nonzero elements of the cones K_E of nonnegative
  exponential polynomials with an admissible exponent multiset E (|E| ≤ 3). SCV is scale- and time-scale invariant.
  SCV/(1+SCV) = min_θ R_θ, R_θ(f) = ∫(t−θ)²f/(θ²∫f) (Lemma 2.2). On each K_E∖0, the infimum of SCV is attained
  on an extreme ray (Lemma 2.4). Assembly (Cor. 2.6): inf over ME(≤3) = min(I_R, I_1, I_2), the infima over real,
  D1 and D2 cones. Lower-order laws are covered by the inclusion K_E ⊆ K_E′ (Lemma 2.5; the "face" claim is false,
  as the subagent showed).
* **L3–L4.** Real exponents give SCV ≥ Δ₃ ∈ (0.2765825307809456, 0.2765825307809457), with an exact certificate
  that Δ₃ > 1/4.
* **L5.** In D1 the extreme rays are the cos family, so I_1 = v_cos by definition. The minimum is attained
  (Thm 5.6), and certified 0.20090156350055 ≤ v_cos < U = 0.200901563500556958801… (runs ctl-c-v2, ctl-f-main-v1).
* **L6.** In D2 (real pole 1, pair 1 + ξ, 1 + ξ̄, ξ = δ − iω, δ, ω > 0, r = δ/ω), the extreme rays are e^{−t}h_τ
  with φ = ωτ ∈ [0, θ₁(r)]. Here θ₁ is C¹ and strictly decreasing from 2π (r → 0) to π (r → ∞), and
  m_k = k!(1 − Re(cζ^{k+1})) with c = (1 − ir)e^{(r−i)φ} and ζ = 1/(1 + δ − iω).

Consequently (Cor. 7.1 there) the Theorem is equivalent to I_2 ≥ v_cos. Sections 2–4 prove the stronger statement
that every D2 extreme ray has S > v_cos.

Throughout: T := 11/50, κ := 1/(1+T) = 50/61, ρ := T/(1+T) = 1 − κ. Note v_cos < U < T.

## 2. Lemma D (an elementary dual sufficient condition)

Fix δ ≥ 0 and ω > 0, put ξ = δ − iω, and let K be the cone of nonnegative densities with exponents
{−1, −(1+ξ), −(1+ξ̄)}. Every f ∈ K has the form f(t) = e^{−t}H(t), H(t) = a + Re(c e^{−ξt}) ≥ 0 on [0, ∞), with
a ∈ ℝ, c ∈ ℂ, and a ≥ 0. (If δ > 0, let t → ∞. If δ = 0, average the nonnegative H over one period.)

For y > 0 let Q_T(y) := (κy² − 2y + 2)/y³. Since κ > 1/2 the numerator N(y) = κy² − 2y + 2 is positive for all real
y, so Q_T(y) > 0 for y > 0.

**Lemma D.** Suppose that for every θ > 0 the number W(θ) := Q_T(θ(1+ξ))/Q_T(θ) admits a representation
W(θ) = Σ_{k=1}^{m} λ_k e^{−ξt_k} with m finite, λ_k ≥ 0, Σλ_k ≤ 1 and t_k ≥ 0. Then SCV(f) ≥ T for every f ∈ K∖0.

*Proof.*
1. For θ > 0 put q_θ(t) := (t − θ)² − ρθ². For Re z > 0, ∫₀^∞ q_θ(t)e^{−zt} dt = 2/z³ − 2θ/z² + (1−ρ)θ²/z
   = θ³Q_T(θz). Hence ∫q_θ f = Q_θ(1)[a + Re(c·W(θ))] with Q_θ(1) = θ³Q_T(θ) > 0. (Linearity; the real part
   commutes with the integral.)
2. Write W = Σλ_k e^{−ξt_k}. Then a + Re(cW) = (1 − Σλ_k)a + Σλ_k[a + Re(c e^{−ξt_k})] = (1 − Σλ_k)a + Σλ_k H(t_k) ≥ 0.
3. So ∫(t−θ)²f ≥ ρθ²∫f for every θ > 0, i.e. R_θ(f) ≥ ρ, and Lemma 2.2 gives SCV/(1+SCV) ≥ ρ = T/(1+T), i.e.
   SCV ≥ T. ∎

**Certificate forms used** (each yields the representation in Lemma D):
* RADIAL: W ≠ 0 and some α ≥ 0 with W = |W|e^{iα} and |W| ≤ e^{−δα/ω}. Take m = 1, t₁ = α/ω and
  λ₁ = |W|e^{δα/ω} ∈ [0, 1]. Then λ₁e^{−ξt₁} = |W|e^{δα/ω}·e^{−δα/ω}e^{iα} = W. If W = 0, take λ₁ = 0.
  **Any** argument α ≥ 0 of W may be used; no branch convention is needed. In particular, if g is a continuous
  logarithm of W along some path and Im g ≥ 0, then α = Im g works, and the condition reads
  Φ := ω·Re g + δ·Im g ≤ 0.
* SMALL: |W| ≤ e^{−2πδ/ω}. Then RADIAL holds with α = Arg₊(W) ∈ [0, 2π), and also trivially when W = 0.
* TRIANGLE: W = a′·1 + b′·e^{−ξt′} with a′, b′ ≥ 0, a′ + b′ ≤ 1 and t′ ≥ 0. (Use 1 = e^{−ξ·0}.)

No closure or limit point is used: every certificate is an explicit finite convex combination, and the weight left
on "0" is justified by a ≥ 0.

**Parametrization used in the computations.** For θ ∈ (0, ∞) put s = θ/(1+θ) ∈ (0, 1), so θ = s/(1−s). With
N₁(s) := κs² − 2s(1−s) + 2(1−s)² = (1−s)²N(θ) > 0 and zz := 1/(1+ξ):
  W = zz·(w₁ + zz·(w₂ + zz·w₃)),  w₁ = κs²/N₁, w₂ = −2s(1−s)/N₁, w₃ = 2(1−s)²/N₁.
(Multiply numerator and denominator of N(θz)/(N(θ)z³) by (1−s)².) The formula is a rational function of
(s, ξ) on [0, 1] × {Re ξ > −1}. Boxes may include s ∈ {0, 1}; their enclosures contain the true values for all
s ∈ (0, 1) in the box.

## 3. Lemma M and the continuation argument (primal chart P)

Let R_P := [0, 3] × [1/5, 40] × [0, 31416/5000] in (r, ω, φ). For points with φ ≤ θ₁(r) (r > 0), or r = 0 and any φ,
let S(r, ω, φ) be the SCV of the extreme ray: e^{−t}h_{φ/ω} when r > 0, and the D1 ray e^{−t}(1 − cos(ωt − φ))
when r = 0. By L6 the closed-form moments are continuous on R_P and C¹ in r. With a_k := m_k/k!, 1 + S = 2a₀a₂/a₁²,
and ∂_r log(1+S) = D/(a₀a₁a₂), where D := a₀′a₁a₂ + a₀a₁a₂′ − 2a₀a₁′a₂ and a_k′ := ∂a_k/∂r at fixed (ω, φ).
(The derivative formula is an exact sympy identity, run v01.)

**Certificate (run c03, spec frozen in code/spec_primal_P_v1.json; audit a01).** R_P is tiled by finitely many
closed boxes, each with one outcome:
* INFEAS: no point of the box has φ ≤ θ₁(r);
* SGE: S > T at every box point;
* DPOS: a₀, a₁, a₂ > 0 and ∂_r S > 0 at every box point.
Counts: 891,318 SGE, 8,018 DPOS, 46,344 INFEAS. Audit a01 replays the exact split rule from geometry alone and
confirms that the 945,680 leaves tile all 61,440 initial cells.

**Lemma M (continuation).** For every feasible (r₀, ω₀, φ₀) ∈ R_P with r₀ > 0, S(r₀, ω₀, φ₀) > v_cos.

*Proof.*
1. If S(r₀, ω₀, φ₀) ≥ T, done, since T > U > v_cos. Otherwise put σ(r) := S(r, ω₀, φ₀) for r ∈ [0, r₀].
2. Every point (r, ω₀, φ₀) with r ∈ [0, r₀] is feasible, because θ₁ is decreasing (L6.5): φ₀ ≤ θ₁(r₀) ≤ θ₁(r)
   for 0 < r ≤ r₀, and r = 0 is the D1 slice, defined for every φ. All these points lie in R_P.
3. σ is continuous on [0, r₀] and differentiable on (0, r₀].
4. Let J := {r ∈ [0, r₀] : σ < T on [r, r₀]} and r* := inf J.
5. For r ∈ (r*, r₀], the point (r, ω₀, φ₀) is feasible with S < T. Choose any leaf box containing it. That box is
   not INFEAS, since it contains a feasible point, and not SGE, since S < T there. So it is DPOS, and σ′(r) > 0.
   Hence σ is strictly increasing on (r*, r₀].
6. If r* > 0, then by continuity and the definition of r*, σ(r*) ≥ T. (If σ(r*) < T, continuity would give σ < T on
   [r* − ε, r₀], contradicting the infimum.) But monotonicity and continuity give σ(r*) ≤ σ(r₀) < T, a
   contradiction. So r* = 0.
7. Then σ(r₀) > σ(0) = SCV(e^{−t}(1 − cos(ω₀t − φ₀))) ≥ v_cos, by the definition of v_cos. ∎

## 4. The far region (dual charts)

The pole configurations with δ < 64 and (ω < 1/5, or ω > 40, or δ > 3ω), together with all configurations with
δ ≥ 64, are certified by Lemma D on six compact charts. Each chart is specified in `proof/charts-spec-v1.md`
(sha 5a43c252…1ff1, frozen with `code/spec_dual_v1.json`, receipt `receipts/spec-dual-freeze-v1.json`). Each chart
yields: for every (δ, ω) in its assigned set and every s ∈ [0, 1], one of RADIAL, SMALL or TRIANGLE holds. By
Lemma D, every density with those poles has SCV ≥ T > v_cos. **The certified run results and audits are recorded in
version 2 of this document.**

## 5. Assembly

Let X be a continuous ME(≤3) law with density f.
* If f has only real contributing exponents: SCV ≥ Δ₃ > U ≥ v_cos (L3–L4).
* Otherwise, after the time scaling that puts the real pole at 1 (L1), f lies in a D cone with parameters
  (δ, ω) ∈ [0, ∞) × (0, ∞).
  * If δ = 0 (D1): SCV ≥ v_cos by L5 and the definition of v_cos.
  * If δ > 0 and (δ, ω) lies in a dual chart's assigned set: SCV ≥ T > v_cos (§4).
  * Otherwise ω ∈ [1/5, 40] and r = δ/ω ≤ 3. By L2 the minimum of SCV over the cone is attained on an extreme ray,
    and by Lemma M every extreme ray has S > v_cos. So SCV(X) > v_cos.
Attainment: L5 Theorem 5.6. ∎ (pending the §4 certificates)

## 6. Correctness dependencies and limits

* The certified computations rely on Arb's ball arithmetic being an outward-correct enclosure, on the code
  implementing the stated formulas, and on the deterministic split rule. Defences:
  * the leaf records plus independent geometric coverage audits;
  * exact sympy identities for the derivative formula (v01);
  * 40-digit quadrature checks of the closed-form moments (v01).
  The parent will rebuild the evaluators from the definitions.
* No Lean or kernel check. No human referee.
* The book's general minimal-representation question is not addressed. This is the separately published HSTZ 2016
  ME(3) conjecture only.
