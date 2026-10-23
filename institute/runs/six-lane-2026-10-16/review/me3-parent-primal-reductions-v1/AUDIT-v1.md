# ME3 parent desk ME3ParentPrimal — audit of reductions L1–L6, the primal chart P and Lemma M (v1)

Desk `review/me3-parent-primal-reductions-v1/`, written 2026-10-18 PDT. **Correctness only.** No novelty, priority,
significance or gate statement. The dual charts (Lemma D, the six far charts) are **not** in this slice.

Inputs (all hashes re-verified, see `receipts/input-pins-v1.txt` and `receipts/input-pins-v2-final-binding.txt`):
`reductions/proof/reductions-v1.md` ad6c5091…5536, `reductions/proof/vcos-lower-bound-v1.md` 01821b4c…9e20,
`reductions/STATUS.md` 61776330…2c76, `proof/me3-theorem-v3.md` 30f6acff…9e87 (final pin; §3 Lemma M identical in
substance to v1 §3), `proof/charts-spec-v1.md` 5a43c252…1ff1, `code/spec_primal_P_v1.json` 6339c775…759c,
`runs/c03-primalP/leaves.txt.gz` b2773bab…f126 (read in place), `runs/c03-primalP/primal.json` aa719d37…2470e,
candidate pin `receipts/me3-candidate-pin-v1.json` 8bd1b39e…a859, manifest 91542ccd…2453.

Method. Every statement below was re-derived by hand from the definitions. Where a step is a finite identity or
a numerical inequality it was re-checked by a parent-authored script (exact sympy / exact rationals / Arb balls):
`code/red_checks_v1.py` (run x01), `code/p_formulas_v1.py` (run f01), `code/p_core_v1.py` + `code/p_replay_v2.py`
(run r01), `code/d1_lower_v1.py` (runs d1a/d1b/d1c), controls `code/p_controls_v1.py` (c01) and `v2` (c02). No
worker code was imported or executed; the worker driver `cert_primal_v3.py` was read only for the leaf format
(cell numbering, path bits, split rule) and `me3jet_v1.py`/`me3lib_v1.py` were read only to audit soundness.

---

## L1 — structure of ME(≤3)

* **Lemma 1.1 (decay ⇒ Re < 0).** Re-derived: with σ = max Re λ, d = max degree on Re λ = σ,
  t^{−d}e^{−σt}G = T + ε, T a finite trigonometric sum with distinct frequencies; mean of |T|² is Σ|c_λ|² > 0; if σ ≥ 0
  then |T + ε| ≤ |G| → 0 forces mean |T|² = 0. Sound.
* **Lemma 1.2 (dominant exponent is real).** If σ ∉ Λ, all λ with Re λ = σ are non-real and conjugation-closed, so
  T is real with zero mean and M(T²) > 0; f ≥ 0 gives T ≥ −ε, hence M(T⁻) = 0, M(|T|) = M(T) + 2M(T⁻) = 0 and
  M(T²) ≤ ‖T‖_∞M(|T|) = 0. Contradiction. Sound.
* **L1(a).** α𝟙 = 1 from F(0) = Pr(X < 0) = 0; G = α e^{At}𝟙 is an e.p. of order ≤ n (Jordan form), G → 0 so all
  contributing exponents have Re < 0 (1.1); f = −G′ ≥ 0 (F is C¹ and nondecreasing); E(f) = E(G) because λ ≠ 0 keeps
  deg(q′ + λq) = deg q. With a non-real exponent, 1.2 plus ord ≤ 3 forces E(f) = {λ0, λ, λ̄} simple, λ0 ≥ Re λ. Sound.
* **L1(b) converse.** Re-derived: x = (G,…,G^{(N−1)}) solves x′ = Cx (companion of χ), so G = e1ᵀe^{Ct}x(0); with
  S = [𝟙, e2, …, eN] (S e1 = 𝟙), A = SCᵀS⁻¹, α = x(0)ᵀS⁻¹: αe^{At}𝟙 = x(0)ᵀe^{Cᵀt}S⁻¹𝟙 = x(0)ᵀe^{Cᵀt}e1 = G(t),
  α𝟙 = G(0) = 1, real data. Sound.
* **Normal forms.** D-type E(f) = {−μ, −μ′ ± iν}, μ′ ≥ μ > 0; f(t/μ) has exponents −1, −(1+δ) ± iω with
  δ = μ′/μ − 1 ≥ 0, ω = ν/μ; SCV is invariant under f ↦ cf and f ↦ f(c·) (m_k ↦ c^{−k−1}m_k). Sound.

## L2 — cones, ratio form, mixtures, extreme rays, assembly

* **Lemma 2.1.** K_E is an intersection of closed half-spaces {f(t) ≥ 0}; pointed by (I1); ℓ = ∫f > 0 and m1 > 0 on
  K_E∖0; B_E = K_E ∩ {ℓ = 1} closed and bounded (ℓ ≥ c‖f‖ on the cone). Sound.
* **Lemma 2.2.** With x = 1/θ: R_θ = 1 − 2(m1/m0)x + (m2/m0)x², minimum at x = m1/m2 with value 1 − m1²/(m0m2) = S.
  Checked by hand. Sound.
* **Lemma 2.3 (mixtures).** ∫(t−θ)²g_μ ≥ c′θ²∫g_μ integrates over ν (Tonelli); minimize over θ. Sound.
* **Lemma 2.4.** SCV is continuous on the compact B_E (moments are linear functionals on the finite-dimensional
  V_E, m0, m1 > 0); extreme points of B_E lie on extreme rays; Minkowski/Carathéodory + 2.3. Sound.
* **Lemma 2.5.** Only the inclusion K_E ⊆ K_{E′} is used; the outline's "face" claim is false (the worker's
  counterexample e^{−t} ± e^{−3t} is correct: both lie in K_{E′}, sum 2e^{−t} ∈ K_E, neither in V_E). Confirmed.
* **Cor. 2.6 (assembly).** Every density lies in B_{E(f)} with E(f) of type R or D. Non-dominated complex E (Re λ >
  λ0) gives K_E = K_{λ0} by 1.2 (any element with a non-zero pair coefficient would have a non-real dominant
  exponent); E = {λ, λ̄} alone gives K_E = {0}. |E| ≤ 3 excludes a repeated pair. Sound.

## L3 — real exponents (cases A, B1, B2, C; lower order by padding)

* Size-3 real multisets are exactly: three distinct rates (A); a double rate smaller (B1) or larger (B2) than the
  simple one; a triple rate (C). Size ≤ 2 is padded into size 3 (2.5). Classification complete.
* **Lemma 3.1 (≤ N−1 zeros).** Induction via h = e^{−κ1t}g, h^{(m1)} kills p1 and keeps degrees of the others;
  Rolle with multiplicities. Sound.
* **Lemma 3.2.** (F2) checked for each type: ψ = e^{−λ1t} (A, B2), (1+t)e^{−λt} (B1), (1+t)²e^{−λt} (C);
  f/ψ → a1. a1 ≥ 0 on K_E; K′ = {a1 = 0} is an exposed face. Sound.
* **Lemma 3.3 (face rays).** a e^{−κ1t} + b e^{−κ2t} ≥ 0 ⟺ a ≥ 0, a+b ≥ 0 (affine in x = e^{−(κ2−κ1)t} ∈ (0, 1]);
  SCV values 1, 1/2 and (κ1² + κ2²)/(κ1 + κ2)² ≥ 1/2 ⟸ 2(κ1²+κ2²) − (κ1+κ2)² = (κ1−κ2)² — **exact re-check x01 R2**.
* **Lemma 3.4 (Hermite–Genocchi rays).** F_τ(t) = (t−τ)²∫_Σ e^{−(t−τ)⟨u,λ⟩}du = φ_{t−τ}[λ1,λ2,λ3] with
  φ_s(x) = e^{−sx} (φ_s″ = s²e^{−sx}); the confluent divided difference is a combination of
  φ_s^{(j)}(λ_i) = (τ−t)^j e^{λ_iτ}e^{−λ_it}, j < mult λ_i, hence F_τ ∈ V_E for coincident nodes too. F_τ > 0 off τ,
  F_τ(τ) = F_τ′(τ) = 0, F_τ″(τ) = 2·area(Σ) = 1. Uniqueness of the double-zero line from 3.1. Mixture:
  F_τ = ∫_Σ g_u, g_u = (t−τ)²e^{−μ_u(t−τ)}, μ_u ∈ [min λ, max λ] ⊂ (0, ∞); the time change t ↦ t/μ_u maps g_u to a
  multiple of (t − μ_uτ)²e^{−t}, so SCV(g_u) = s(μ_uτ) ≥ Δ3 and 2.3 applies. **Exact re-check x01 R2**: s²∫_Σ e^{−s⟨u,λ⟩}
  equals the (confluent) divided difference for nodes (1,2,3), (1,1,2), (1,2,2), (1,1,1) (residual 0).
* **Lemma 3.5 (extreme rays).** ≤ 2 zeros (3.1); interior zeros have even multiplicity, so on [0, ∞) only
  P0 (no zero), P1 (simple zero at 0), P2 (double at 0), P3 (double at τ > 0) occur; P0/P1 are interior points of a
  2-sided perturbation (|g| ≤ Mψ resp. Mψ0); P2/P3 give c F_τ. Converse extremality via forced double zeros.
  Exhaustive and sound.
* **Theorem L3.** SCV ≥ min(Δ3, 1/2) = Δ3 on real cones; attained by type C at τ = x1 (x1 > 0 certified, x01 R1b).

## L4 — Δ3 (parent exact certificate, run x01 R1a/R1b)

* m_k((t−τ)²e^{−t}) = (k+2)! − 2τ(k+1)! + τ²k! computed by sympy **from the integral definition**; P = m0m2 =
  (τ²−2τ+2)(2τ²−12τ+24), Q = m1 = (τ−2)² + 2 > 0; 4(P − 5Q²/4) = 3(τ²−4τ+2)² + 8τ² (residual 0) ⇒ Δ3 > 1/4.
* P′Q − 2PQ′ = 8(τ³ − 9τ² + 18τ − 6) = −48L3(τ); P/Q² → 2 at ±∞. The cubic has three simple real roots, isolated
  exactly and refined to width 1e−40: x1 ∈ 0.41577455678347908331153387312827447…, x2 ≈ 2.2942803602790417,
  x3 ≈ 6.2899450829374792. Arb: s(x1) = 0.276582530780945666463231609883 (± 4e−31), s(x2) ≈ 3.29859, s(x3) ≈ 0.92483,
  so Δ3 = s(x1) (s decreases on (−∞, x1], cubic < 0 at −1000).
* Remainder identity 24(P − Q²) − Q²(x(9−x)² − 24) ≡ 0 mod the cubic; resultant gives 432·(32y³ − 144y² + 135y − 27),
  irreducible over ℚ.
* Sturm (sympy count_roots, exact): P − (1+2765/10000)Q² and P − (1 + 0.2765825307809456)Q² have **no** real root and
  positive leading coefficient ⇒ Δ3 > 0.2765825307809456; exact evaluation at a rational τ0 in the x1 interval gives
  P − (1 + 0.2765825307809457)Q² < 0 ⇒ Δ3 < 0.2765825307809457. Arb (256 bits):
  Δ3 = 0.276582530780945666463231609882563467003 ± 3.7e−40 — agrees with the worker's value.

## L5 — common damping D1 (δ = 0)

* **Cone (5.1).** e^{−t}(a + R cos(ωt − χ)) ≥ 0 ⟺ a ≥ R (evaluate at ωt = χ + π + 2πk); extreme rays of
  {a ≥ |v|} are (|v|, v); R e^{−t}(1 + cos(ωt − χ)) = R f_{ω, χ+π}. So I_1 = inf SCV(f_{ω,φ}) = v_cos. Sound.
* **Moments (5.2).** ∫t^k e^{−t}cos(ωt − φ) = Re[e^{−iφ}k!(1 − iω)^{−(k+1)}]; m_k = k!(1 − Re[…]) > 0. Sound.
* **Algebraic form (5.3).** With β = arctan ω, ψ = φ − 2β: e^{−iφ} = e^{−iψ}(1 − iω)²/(1+ω²) (re-checked via
  cos 2β = (1−ω²)/(1+ω²), sin 2β = 2ω/(1+ω²)), hence Re-parts q(C − ωS), qC, q²(C + ωS); a0 = q(X+Y), a1 = qX,
  a2 = q²(X + a − Y) **without** using C² + S² = 1; 1 + SCV = 2(X+Y)(X+a−Y)/((1+ω²)X²). **Exact re-check x01 R3a**
  (all residuals 0).
* **Uniform bound (5.4).** Step 1 uses only Y ≥ −Y_m, Y² = Y_m² and a > 0. Step 2 (u = ω²v, X = ω²(1+v),
  Y_m = ω²s_m, s_m² = v(2−ω²v)): X² + aX − aY_m − Y_m² = ω⁴[(1+v)² + (1+ω²)(1+v−s_m) − s_m²] (exact residual 0).
  Step 3: s_m² ≤ 2v, √(2v) ≤ 1+v (since (1+v)² − 2v = 1 + v² ≥ 0), so 1+v−s_m ≥ 1+v−√(2v) ≥ 0 and the (1+ω²)
  factor can be dropped; N ≥ N0 = (1+v)² + 1 + v − √(2v) − 2v. Step 4: with σ = √(2v),
  2N0/(1+v)² = P(2−σ)/Q(2−σ)² = 1 + s(2−σ) ≥ 1 + Δ3 — Δ3 is the infimum over **all real** arguments, and
  2 − σ ranges over (−∞, 2] (exact residuals 0). Hence 1 + SCV ≥ (1+Δ3)/(1+ω²). Sound.
* **Tails.** ω ≤ 1/4: SCV ≥ (16Δ3 − 1)/17 > (16·2765/10000 − 1)/17 = 428/2125 = 0.20141… (exact). ω ≥ 4:
  m0 ≥ 1−ρ, m1 ≤ 1+ρ², m2 ≥ 2(1−ρ³), the bound 2(1−ρ)(1−ρ³)/(1+ρ²)² decreases in ρ, ρ ≤ 17^{−1/2} < ρ̄ = 2426/10000
  (ρ̄² > 1/17 exact), giving SCV ≥ 232498770764161/700733376734161 = 0.33179… (exact, equals the worker's value).
* **Attainment (5.6) and the ESSENTIAL bound.** Parent Arb (320 bits) from the moment formula at the rational point
  ω0 = 517966477543/500000000000, φ0 = 674076484769/2000000000000 ∈ [1/4, 4] × [0, 2π):
  SCV = 0.20090156350055695880138068245515932165686318020855 ± 2.5e−51 < U = 0.2009015635005569588013806824561593216569.
  Exact: U < 2014/10000 < 428/2125 (both tails), U < T = 11/50, U < 1/4, U < 2765/10000 < Δ3. So v_cos is a minimum
  attained on [1/4, 4] × [0, 2π] (continuity + compactness), v_cos < U < T, and Δ3 > v_cos. Cross-check through the
  primal evaluator at r = 0 agrees to 1e−80 (same Arb library). **These, and only these, numerical facts about
  v_cos are used by the global argument** (T > v_cos in Lemma M step 1 and in the dual charts; Δ3 > v_cos; tails >
  the value at (ω0, φ0) for attainment).
* **Optional decimal lower certificate (not needed for the theorem).** `d1_lower_v1.py`: branch-and-bound on
  [1/4, 4] × [0, 31416/5000] (a full φ-period) with the parent evaluator at r = 0, tails by 5.4/5.5 with the exact
  constants above. Certified v_cos ≥ 0.20090144 (contract band lower edge; 7,770 boxes, 4,365 leaves, depth ≤ 21) and
  v_cos ≥ 0.20090156350055 (14,110 boxes, 7,535 leaves, depth ≤ 46); exact certified-leaf area = domain area in both.
  Mutation L = 0.200901563500557 is refuted at the certified centre (17380071/2²⁴, 28272817419/83886080000), SCV =
  0.200901563500556973227… < L. Hence 0.20090156350055 ≤ v_cos < U (inside the contract band).

## L6 — strictly dominant real pole D2 (δ > 0)

* **6.1.** H → a as t → ∞ so a ≥ 0; a = 0 forces R = 0. Sound.
* **6.2.** h_τ ∈ span{1, e^{−δt}cos ωt, e^{−δt}sin ωt} (expanded explicitly, exact residual 0, x01 R4a);
  h_τ′ = ((ω²+δ²)/ω)e^{−δ(t−τ)}sin ω(t−τ) (δ = rω; residual 0); G′(τ) = 0 is one non-trivial condition on (b, c)
  because det[[−δ, ω], [−ω, −δ]] = δ² + ω² > 0, and G(τ) = 0 then fixes a: the double-zero set is a line. Sound.
* **6.3 extreme rays.** Cases (a) H > 0 (interior: inf H > 0, |G| ≤ M), (b) simple zero at 0 with H′(0) > 0
  (H ≥ ct/(1+t), perturb inside {G(0) = 0}), (c) double zero at 0, (d) zero at τ > 0 (interior minimum ⇒ double)
  are exhaustive; (c)/(d) are extreme by forced double zeros. Sound.
* **6.4 feasibility.** h_τ(0) = 1 − e^{rφ}(cos φ − r sin φ) = 1 − g_r(φ) (δτ = rφ; residual 0). g_r′ = −(1+r²)e^{ru}sin u
  (residual 0): g_r decreases on [0, π] from 1, increases on [π, 2π] from −e^{rπ} to e^{2πr} > 1, so θ1 ∈ (π, 2π) is
  unique, g_r < 1 on (0, θ1), > 1 on (θ1, 2π]. On s = t − τ ≥ 0 the local minima of h are 1 − e^{−2πkr} ≥ 0; τ ≥ 2π/ω is
  infeasible (h = 1 − e^{2πr} < 0 at s = −2π/ω); for τ < 2π/ω, h > 0 on (τ − π/ω, τ) and h is non-decreasing on
  (τ − 2π/ω, τ − π/ω], so the minimum on [0, τ) is h(0) when φ > π. Feasible ⟺ φ ∈ [0, θ1(r)]. Sound.
* **6.5 θ1 decreasing.** At the root, ∂_u g = −(1+r²)e^{ru}sin u > 0 and ∂_r g = u g − e^{ru}sin u = u − e^{ru}sin u > 0
  (residual 0 for ∂_r g), so θ1′ < 0 by the implicit function theorem; limits 2π and π. Parent Arb brackets:
  θ1(3/10) ∈ (4.65987805685937, 4.65987805685938), θ1(1) ∈ (3.94073313569291, 3.94073313569292),
  θ1(3) ∈ (3.46335292772992, 3.46335292772993) (certified sign changes of g_r − 1). Infeasible-ray control:
  h(0) at r = 3/10, φ = θ1 + 1/100 is −0.0441279542429399… < 0 (certified).
* **6.6 moments.** cos x + r sin x = Re[(1 − ir)e^{ix}] and (−δ+iω)(t−τ) = (−δ+iω)t + (r−i)φ (exact, f01 F3), so
  h_τ(t) = 1 − Re[c e^{(−δ+iω)t}] with c = (1−ir)e^{(r−i)φ}; ∫t^k e^{−zt} = k!/z^{k+1} (z = 1+δ−iω, Re z > 0) gives
  a_k = 1 − Re[cζ^{k+1}], ζ = 1/(1 + rω − iω). Diagnostic quadrature (mpmath, 40 digits, f01 F4) agrees to ≤ 3e−39
  at five points including r = 0 and ω = 12. At r = 0 it is exactly the D1 formula 5.2.

## Primal chart P (spec_primal_P_v1) — parent rebuild

* Quantities: a_k = 1 − Re P_k, P_k = cζ^{k+1}; 1 + S = 2a0a2/a1²; G = 2a0a2 − (61/50)a1² (a1 ≠ 0 ⇒ S > T ⟺ G > 0);
  a_k′ = ∂_r a_k = −Re(P_k L_k), L_k = φ + (r−i)/(1+r²) − (k+1)ωζ (from ∂_r log c = φ − i/(1−ir), ∂_r log ζ = −ωζ);
  D = a0′a1a2 + a0a1a2′ − 2a0a1′a2 = a0a1a2·∂_r log(1+S). All log-derivatives, ∂_xL_k and the dlog identity are exact
  sympy identities (f01 F1, F2, residuals 0); the parent code agrees with sympy derivatives of the definition-level
  expressions to < 1e−30 relative at 8 points (f01 F5); enclosure smoke test 0 violations on 40 random boxes × 12
  points (f01 F6, diagnostic).
* Box tests (parent, `p_core_v1.py`): SGE ⟺ certified a1 > 0 and G > 0 (naive ball, else mean-value form with the
  exact centre and box-ball gradients); DPOS ⟺ certified a0, a1, a2 > 0 and D > 0 (same); INFEAS ⟺ r_lo > 0,
  φ_lo > π (Arb π) and g_{r_lo}(φ_lo) > 1 (Arb at the exact corner). MVF validity: F(x) − F(m) = ∫₀¹∇F(m+s(x−m))·(x−m)ds
  with every ∇F value in the box-ball gradient enclosure.
* **INFEAS soundness (re-derived).** For a box point (r, φ): r ≥ r_lo > 0 and φ ≥ φ_lo > π. If φ_lo > 2π the point is
  infeasible outright. If φ_lo ∈ (π, 2π]: g_r ≤ 1 on [0, θ1(r)] (g_r(0) = g_r(θ1) = 1, g_r < 1 in between), so
  g_{r_lo}(φ_lo) > 1 forces φ_lo > θ1(r_lo); θ1 decreasing ⇒ θ1(r) ≤ θ1(r_lo) < φ_lo ≤ φ. No box touching r = 0 can be INFEAS. Sound; the
  spec's appeal to "g_r increasing on (π, 2π)" is only needed at the single corner.
* The positivity clauses (a1 > 0 for SGE; a0, a1, a2 > 0 for DPOS) are redundant at feasible points (moments of a
  non-negative non-zero density are positive) and harmless elsewhere.
* **Full replay (run r01, PASS_FULL_REPLAY).** 945,680/945,680 leaves read in place (sha b2773bab…f126 before and after);
  61,440/61,440 cells; complete prefix-free DFS tiling with 0 coverage errors; line hash 74d67a57…92a5 and depth
  histogram equal primal.json; counts SGE 891,318, DPOS 8,018, INFEAS 46,344, FAIL 0 (= claims). Every claimed outcome
  certified by the parent evaluator: SGE naive 47,437, MVF 796,648, recorded extra bisection 47,233 (depth 1: 47,077,
  depth 2: 156, all sub-boxes certified SGE); DPOS MVF 8,016, recorded bisection 2; INFEAS 46,344 by the corner rule.
  All 47,235 subdivided leaves are listed in `runs/r01-replay-full/subdivisions.txt.gz` (sha f490c498…121a; 94,680
  certified sub-boxes). The extra bisections are needed only because the parent mean-value form is slightly looser
  than the producer's at margin (direct parent MVF lower bounds ≈ −1e−5…−1e−2 on those leaves); coverage is
  preserved because a bisection replaces a leaf by two halves. Exact DPOS bounding box: r ∈ [0, 15/64],
  ω ∈ [1507/2560, 10633/6400], φ ∈ [0, 11781/16000] (= worker float box). 33.5 s, 38 MB RSS.
* Format dependency: cell order (r-major, then ω, then φ) and path semantics were read from the producer source. The
  replay is nevertheless self-contained: under the parent reconstruction every point of R_P lies in a leaf whose
  claimed outcome the parent certified, which is exactly what Lemma M consumes (and the line hash, depth histogram
  and DPOS box agree with the producer).
* Same numerical kernel as the worker (python-flint 0.9.0 / Arb): **not** an independent arithmetic library.

## Lemma M (continuation) — independent check

Claim: every feasible (r0, ω0, φ0) ∈ R_P with r0 > 0 has S > v_cos. Properties used and where they come from:
(i) the leaves tile R_P (r01 coverage); (ii) INFEAS boxes contain no feasible point (above); (iii) SGE ⇒ S > T at
feasible box points; (iv) DPOS ⇒ ∂_rS > 0 on the box; (v) θ1 decreasing (6.5), so {(r, ω0, φ0) : 0 ≤ r ≤ r0} is feasible
and lies in the product box R_P; (vi) a1 = m1 > 0 at feasible points, so σ(r) = S(r, ω0, φ0) is real-analytic on a
neighbourhood of [0, r0] (ζ never singular since ω > 0); (vii) σ(0) is the D1 SCV at (ω0, φ0), ≥ v_cos by definition;
(viii) T > v_cos (essential bound above).
Proof check: if σ(r0) ≥ T, done by (viii). Else J = {r : σ < T on [r, r0]} is an interval ending at r0 and is
upward closed, so every r ∈ (r* , r0] (r* = inf J) lies in J; such a point is feasible with S < T, so by (i)–(iii) any
leaf containing it is DPOS and σ′(r) > 0 by (iv); MVT gives σ strictly increasing on (r*, r0]. If r* > 0,
continuity gives σ(r*) ≥ T (else J extends below r*) while monotonicity + continuity give σ(r*) ≤ σ(r0) < T —
contradiction. So r* = 0 and σ(r0) > σ(r0/2) ≥ lim_{r→0+}σ = σ(0) ≥ v_cos. **Sound; no gap found.** Feasible points
on the boundary φ = θ1(r) are covered (INFEAS requires a strict g > 1). The assembly's remaining D2 set
(ω ∈ [1/5, 40], δ ≤ 3ω) is exactly r ∈ (0, 3] inside R_P; the dual charts for the rest are outside this slice.

## Controls (each must fail at the intended rule)

Run c01 (in-memory, cells 0–140, 95,907 leaves; positive control: all verified, 0 coverage errors):
altered derivative sign a_k′ → −a_k′ rejects 8,018/8,018 DPOS leaves at DPOS even after 3 bisections; false INFEAS
rejected at the intended clause (r_lo = 0: 2000/2000 DOMAIN_R_LO; φ_lo < π: 2000/2000 DOMAIN_PHI_LO; feasible corner:
2000/2000 G_NOT_GT_1; real INFEAS leaves widened below θ1: 2000/2000 G_NOT_GT_1); missing middle leaf, duplicated
middle leaf, last/middle path bit flipped → PATH_MISMATCH; missing last leaf → INCOMPLETE_CELL; duplicated last leaf →
EXTRA_LEAF; leaf moved to the next cell → INCOMPLETE_CELL (+CELL_ORDER); dropped cell → CELL_ORDER; weakened bound
T′ = S(mid)+1e−6 rejects 605/605 SGE leaves even after 3 bisections; T′ = 1/4 rejects 52,408/77,322 SGE leaves;
DPOS leaves relabelled SGE (S(mid) < T) rejected 1,656/1,656; a FAIL label is never accepted.
**Kept visible:** the extra control C1b (flip the sign of the a0a1a2′ term) was NOT rejected on any DPOS leaf — a
benign mutation, not a checker defect: run c02 certifies a2′ < 0 on all 8,018 DPOS leaves, so the flip increases D.
c02 also: flipping the sign of ∂_rζ inside L_k is rejected on 8,018/8,018 DPOS leaves; dropping the φ term of L_k is
benign (0/8,018 rejected; algebraically D_mut − D = φ·a1(a0 + a2 − (1+S)a1), positive at the D1 optimum
[INFERENCE: sign on the whole DPOS region not certified]).
Reductions mutations (x01 R5): Δ3 > 0.2766 (2 real roots), SOS coefficient 8 → 7 (residual τ²), an upper bound below
the certified SCV(ω0, φ0), the ω ≤ 1/2 tail (bound 53/2500 < U), ρ̄ = 0.2425 (ρ̄² < 1/17) and a feasible ray claimed
infeasible (h(0) = +0.04397 > 0) are all rejected.

## Findings summary

1. L1–L6, the real-pole classification (incl. coincident nodes and lower order), the Hermite–Genocchi mixture, the D1
   bound/tails/attainment, the D2 feasibility cutoff θ1 and the moment formula: **re-derived, no gap found**. The
   outline's face claim is false and unused (worker correction confirmed).
2. Primal chart P: **full parent replay certifies every leaf** (with 47,235 recorded 1–2-level bisections) and exact
   coverage of R_P. Lemma M: **sound**.
3. Essential v_cos facts: v_cos attained, SCV(ω0, φ0) < U < T, Δ3 > 0.2765825307809456 > U. Optional decimal
   certification: 0.20090156350055 ≤ v_cos (parent B&B).
4. Not covered here: dual charts / Lemma D; Lean/kernel check; independent arithmetic library (same Arb);
   the final ME3 theorem acceptance (needs the dual slice, hostile reviews and priority screen).
