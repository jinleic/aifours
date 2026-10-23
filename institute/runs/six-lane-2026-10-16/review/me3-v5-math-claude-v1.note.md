**DISPOSITION: ACCEPT-WITH-FIXES**

**FATAL:** none. **MAJOR:** none.

Taking the imports listed at the end as given, SOURCE00 together with SOURCE01 proves the stated theorem for the full class. Every fix below is textual: a definition, an inlined one-line proof, or an explicit range check. No chart, certificate, region or constant changes.

---

## MINOR findings

**m1. "Real span" wording (check 8).** SOURCE00:LF126, LF129–130.
- **Problem.**
  - The display at LF124 is correct, and it is the definition the Lemma D proof uses (c is complex).
  - LF126, read literally, puts real coefficients on e^{−(1+ξ)t} and e^{−(1+ξ̄)t}. A real-valued result then needs equal coefficients, which leaves only a·e^{−t} + b·e^{−(1+δ)t}cos ωt. The sine term is lost, and the identification with K_E at LF127 becomes false.
  - LF129's "conic hull of the three generators" applies nonnegative coefficients to complex-valued generators while K is a cone of real functions, so the comparison is ill-posed.
- **Repair LF126:** "the cone of all nonnegative functions in the real span of e^{−t}, e^{−(1+δ)t}cos ωt and e^{−(1+δ)t}sin ωt (equivalently, the real-valued elements of the complex span of e^{−t}, e^{−(1+ξ)t}, e^{−(1+ξ̄)t})".
- **Repair LF129–130:** "K is not the set of nonnegative combinations of these three real functions: e^{−t}(1 − e^{−δt}cos ωt) ∈ K has coefficient −1 on e^{−(1+δ)t}cos ωt (a = 1, c = −1)."
- No mathematical consequence. I concur with SOURCE06:LF16–26.

**m2. Lemma D is not actually proved in v5's text.** SOURCE00:LF61–64, LF138, LF145, LF147, LF149.
- **Problem.**
  - q_θ is never defined.
  - "As in v3" (LF138) and "unchanged from v3 §3" (LF149) cite a document that v5 labels INVALID (LF8).
  - Validity of the certificates is asserted by a review verdict (LF145), not proved.
  - w₁, w₂, w₃ are undefined.
  - The Imports list omits reductions v4 and the replayed leaf predicates.
- I re-derived every missing step. **Insert:**
  - (a) Define q_θ(t) := (t−θ)² − ρθ². For Re z > 0, ∫₀^∞ q_θ e^{−zt} dt = 2/z³ − 2θ/z² + κθ²/z = θ³Q_T(θz), because 1 − ρ = κ. Hence ∫q_θ f = θ³Q_T(θ)[a + Re(cW)].
  - (b) Q_T > 0 on (0, ∞), because 2κ = 100/61 > 1 makes the discriminant 4 − 8κ negative.
  - (c) ∫q_θ f ≥ 0 for all θ > 0 ⟺ min_θ R_θ ≥ ρ ⟺ SCV ≥ T. This uses LF82 and the fact that x/(1+x) is increasing.
  - (d) The certificates give the hypothesis directly:
    - RADIAL gives one term: t₁ = α/ω ≥ 0 and λ₁ = |W|e^{δα/ω} ∈ [0, 1].
    - SMALL implies RADIAL with α = Arg₊W ∈ [0, 2π) (any α if W = 0), using δ ≥ 0.
    - TRIANGLE gives (λ, t) = (a′, 0) and (b′, t′).
    - The representation may depend on θ; the proof uses only "for every θ there exists". No closure is taken.
  - (e) w₁ = κs²/N₁, w₂ = −2s(1−s)/N₁, w₃ = 2(1−s)²/N₁, with N₁ = κs² − 2s(1−s) + 2(1−s)² > 0 and Σw = 1.
- **Also state:**
  - v3's invalidity concerns only its SWC evidence.
  - Imports include reductions v4 and the replayed predicates.

**m3. The α ≥ 0 conventions at the predicate-to-RADIAL interface are not written down.** SOURCE00:LF141, LF226; SOURCE03:LF203, LF249, LF331.
- **G.**
  - RADIAL requires α ≥ 0.
  - G's replayed predicate fixes α only as "a certified branch (Im W>0 | Im W<0 | Re W<0)".
  - That implies RADIAL only if α is taken in (0, π), (π, 2π) and (π/2, 3π/2) respectively.
  - If α ∈ (−π, 0) were used on the Im W < 0 branch, ω log|W| + δα < 0 would allow |W| > 1, which is not RADIAL.
  - Neither v5 nor spec v2 states these ranges, and spec v1 is not in the packet.
- **SWB and SWC.**
  - α := Im g, where g is the analytic branch of log W that is real at ω = 0 (SWB) or has g(0) = 0 (SWC).
  - SWB's second inequality, or Ig_N − tailIg > 0 for SWC, gives α > 0.
  - The first inequality gives log|W| + (δ/ω)α < 0.
- **Checked here.**
  - The SWB remainder orders are right. Re g(δ − iω) has no ω³ term and Im g has no ω⁴ term, so ω⁴M4/24 and, after dividing by ω, ω⁴·δM5/120 are correct.
  - The SWC control value Ig₂₀ = 2 − 2^{−19} equals the truncation of −g′ at (s, ξ) = (0, 1/2).
- **Repair:** add a per-method table to spec v2 giving "α used, and why α ≥ 0", and cite it at LF226.

**m4. skip-d relies on outer-range facts that are not stated.** SOURCE01:LF77–78, LF102–103.
- **Problem.** The implication "d > 1/65 or cos β ≤ 0" needs:
  - 0 ≤ 1 − χ_h ≤ 1 − χ;
  - 0 ≤ ρ_{t,l} ≤ ρ_t;
  - cos decreasing on [β_l, β_h] ⊆ [0, π].
- Checker v3 certifies β_top > π/2 but not β_top ≤ π.
- **Repair.**
  - State the LD2 outer box: χ ∈ [0, 1], ρ_t ∈ [0, 81/1040], β ∈ [0, β_top] with π/2 < β_top < π.
  - Add the exact check β_top < π to the checker description.
- This is not a demonstrated defect.

**m5. LD2 SKIP sentence.** SOURCE00:LF231–233.
- **Problem.** "such s are physical points of LD1" is false for skip-s points with d > 1/65 or β ≥ π/2, and the argument does not need it.
- **Replace with:** "Each LD2-physical point lies in some LD2 leaf by the tiling. No SKIP leaf contains a physical point, so it lies in a CERT:ld2 leaf. Each s ∈ [1/16, 1) is LD1-physical, and every LD1 leaf is CERT."

**m6. "Physical point" is undefined for G, SWB, SWC and LW.** SOURCE00:LF226, LF235; SOURCE01:LF50–56, LF89, LF92–93.
- **Problem.**
  - Spec v2 defines physical points only for LD.
  - It states the ω = 0 exclusion only for SW.
  - LW's ν = 0 face is not addressed.
- **Repair:** for G/SW/LW, define physical as 0 < ω < ∞ (ν > 0 for LW), δ ≥ 0 and 0 < s < 1. The faces ω = 0, ν = 0 and s ∈ {0, 1} are extensions, and only points with δ > 0 are consumed.
- **Consistency probe (unused).**
  - The δ = 0 faces of G (ω > 40), LW, and SWC (ω ≤ 1/5) contain no SKIP leaves, so they would assert SCV ≥ T on those D1 cones.
  - This agrees with L5: minimizers lie in (1/4, 4), and the ω ≥ 4 tail is 0.3318 (SOURCE04:LF71).
  - It also agrees with my uncertified hand estimate min_φ SCV ≈ 0.269 at ω = 1/5, near φ ≈ 0.08.

**m7. Notation and assignment in Lemma M and §5.** SOURCE00:LF114, LF154–162, LF173, LF223, LF228, LF246; SOURCE01:LF84.
- **Problems.**
  - Cor 7.2 is phrased in terms of S₂, while Lemma M uses S.
  - "feasible", a_k and "R_P" are undefined.
  - "minus P" subtracts an (r, ω, φ) box from a (δ, ω) set.
  - LF223 assigns P only when δ < 64; LF246 has no δ bound.
  - SOURCE01:LF84 writes μ where v5 writes θ.
- **Repair.**
  - feasible := 0 ≤ φ ≤ θ₁(r).
  - a_k := m_k/k! = 1 − Re(cζ^{k+1}), and S := 2a₀a₂/a₁² − 1 = S₂.
  - ∂_r is taken at fixed (ω, φ) with δ = rω, so both c and ζ vary. Then ∂_rS = 2[a₁(a₀′a₂ + a₀a₂′) − 2a₀a₂a₁′]/a₁³. DPOS's a₁ > 0 therefore makes the certified sign the sign of ∂_rS, consistent with SOURCE05:LF8–10.
  - Define P̄ := {1/5 ≤ ω ≤ 40, 0 ≤ δ ≤ 3ω} and use it at LF173, LF223, LF228 and LF246.
  - P̄ reaches δ = 120. Its overlap with LD is harmless, because Lemma M holds on all of P̄.

**m8. Exhaustiveness is used silently.** SOURCE00:LF242.
- **Problem.** "Otherwise … lies in a D cone" uses, without saying so:
  - a nonnegative density with a complex pair has a real exponent λ < 0 with coefficient a > 0;
  - the pair is at least as damped, i.e. δ ≥ 0;
  - if δ < 0 or a = 0, then e^{−(1+δ)t}Re(ce^{iωt}) dominates and changes sign, so c = 0.
- **Repair:** this is contained in L1–L2 "Assembly" (LF84); cite it at LF242.

---

## Per-check results

1. **Quantifiers: PASS.**
   - LF55 is the task's class: continuous laws, any order ≤ 3, any pole configuration. ∫(1+t²)f < ∞ is automatic.
   - The cases (real exponents including confluent and lower orders via LF85, D1, D2) are exhaustive by the imported L1–L2 (m8).
   - No sign structure on α or A is assumed anywhere.
2. **Interfaces: PASS.**
   - L6 re-derived: h_τ(t) = 1 − Re((1−ir)e^{−ξ(t−τ)}) has a double zero at τ exactly when r = δ/ω.
   - Its moments are m_k = k!(1 − Re(cζ^{k+1})) with c = (1−ir)e^{(r−i)φ}.
   - At r = 0 this gives c = e^{−iφ}, the cos family, so σ(0) in Lemma M is a cos-family SCV.
   - The normal form is identical at SOURCE00:LF110 and LF122 and at SOURCE01:LF18–19.
   - Cor 7.2 is consumed with exactly its hypothesis (all φ ∈ [0, θ₁]).
3. **Lemma D: PASS (m1, m2).**
   - All parts hold: a ≥ 0 by the limit (δ > 0) or the period mean (δ = 0); finite convex combinations with mass ≤ 1; Q_T > 0; the "for every θ there exists" quantifier; and the zero cases W = 0, Σλ < 1 and a = 0.
   - No hull closure is used.
   - TRIANGLE is valid but has 0 accepted leaves (SOURCE03:LF301–306), so the float angle heuristic (SOURCE00:LF301–302) lies on no accepted path.
4. **Lemma M: PASS.**
   - θ₁:
     - Let G_r(v) = e^{rv}(cos v − r sin v). Feasibility holds exactly when max over [0, φ] of G_r is ≤ 1.
     - ∂_vG = −(1+r²)e^{rv} sin v > 0 on (π, 2π).
     - On {G = 1}, ∂_rG = v − e^{rv} sin v > 0.
     - Hence θ₁′ < 0, θ₁(0) = 2π, and θ₁ decreases to π. The fixed-(ω₀, φ₀) path is feasible and stays inside P.
   - The INFEAS corner rule (SOURCE04:LF59) is sound because θ₁ is decreasing, not because G is monotone in r; that monotonicity fails near v = π.
   - Path points with σ < T can lie only in DPOS leaves.
   - The infimum argument, the contradiction when r* > 0, and strictness for r₀ > 0 are all correct. Nothing is claimed at r₀ = 0, and only the exact definition of v_cos is used there.
5. **Coverage: PASS (m4–m6).**
   - The (δ, ω) quadrant:
     - δ ≥ 64 goes to LD; d and β compactify δ → ∞, ω → ∞ and ω → 0.
     - δ < 64 splits into LW (ω ≥ 640), P̄ ∪ G (1/5 ≤ ω ≤ 640) and SWC ∪ SWB (ω < 1/5).
   - The s-range:
     - G, SW and LW are closed in s.
     - LD1 ∪ LD2 covers (0, 1) because ρ_t ≤ 81/1040 and χ ∈ (0, 1).
   - SKIP rules:
     - A G SKIP box is exactly a subset of P̄.
     - Every P̄ cone has all its phases inside P, since θ₁ ≤ 2π < 31416/5000.
     - LD2 SKIP boxes contain no physical point.
   - Padding faces are never consumed.
   - SWC convergence: B = κθ²/N(θ) ≤ 100/39, so 1/√B > 0.62 > √0.13 ≥ |ξ|.
6. **D2 cone: PASS.**
   - LF124 equals K_E: Re(ce^{−ξt}) realizes every real (cos, sin) coefficient pair.
   - The v4 "cone{…}" defect is gone. The only residue is m1.
7. **Strictness and attainment: PASS.**
   - Dual-assigned cones: SCV ≥ T > 773/3844 ≥ v_cos.
   - P̄ cones: Lemma M on every phase, then Cor 7.2 (the minimum is attained on an extreme ray of that fixed cone).
   - Strictness is per cone. The proof correctly makes no uniform-gap claim, since by Cor 7.1(2) the infimum over D2 is v_cos.
   - D1: SCV ≥ v_cos by Lemma 2.4 and Lemma 5.1, and attainment follows from L5's exact chain.
   - No decimal value of v_cos is used anywhere.
8. **Real span: MINOR (m1).**

---

## Audited here versus imported

**Audited by hand in this review:**
- **L5:** moments (27, 62, 171)/74, giving SCV = 773/3844 < 1007/5000 < 11/50.
- **L3–L4:** h′ = 96(y − 3/2)² − 81 ≥ 149/3 on [1/4, 1/3], and h(553/2000) < 0 < h(1/3).
- **Lemma D and the certificates:** all of Lemma D; RADIAL, SMALL and TRIANGLE.
- **Feasibility and P-chart facts:** θ₁ and feasibility; the INFEAS rule; the L6 moments; the DPOS sign factor and SOURCE05's E-identity; Lemma M.
- **SWC and SWB:** the SWC coefficients c_j from W = q(1+ξ)/(N(θ)(1+ξ)³), with its radius bound and control value; the SWB remainder orders.
- **LD charts:**
  - ζ = d cos β e^{iβ} and δ/ω = (1−d)/tan β;
  - the three candidates;
  - mvt0, which needs 1 + sup ≥ 0 and β/tan β ≤ 1;
  - LD2's replacement of 1 − d by 1.
- **SKIP rules and coverage:** the SKIP implications; the s-union; the quadrant coverage.
- **Leaf counts:** the sums for P, G, SWB, SWC and LD2.

**Imported, not re-derived:**
- **Reductions v4:**
  - L1–L2 classification and Assembly, including confluent real cases and the exclusion of δ < 0;
  - Lemma 2.4 (outline checked: compact base and quasi-concavity of min_θ R_θ);
  - that Δ₃ is the real-exponent minimum (only its bracket was checked);
  - Lemmas 4.2, 5.1 and 5.4, Thm 5.6, Cor 5.7, and Lemmas 6.3/6.4;
  - Cor 7.2 (structure checked only).
- **Certified computations:**
  - the truth of every leaf predicate, the tilings, and the SKIP re-checks (SOURCE03–05);
  - the spec-v1 definitions of X_m, U_m, Ψ, Ig, M4, M5 and the tails, and G's α branches (m3);
  - the LD and LW outer domains (m4).
- **Not examined:** Arb/python-flint semantics, the float audits, and all provenance and binding (b04, the pin closure, and SOURCE06 finding 1).
