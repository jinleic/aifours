# Erratum 2 to `proof/me3-theorem-v5.md` (exposition, definitions and inlined proofs only)

Worker `MathPhaseType3`, 2026-10-18 PDT. This is a static erratum, created as a new file. It changes no file and
involves no new computation.

**Frozen and unchanged (sha256):**
* `proof/me3-theorem-v5.md`: 1504ec692f2b0e26e2292e789c79ebde65f4f9ce171343a52ca9ce39d83cec60
* `proof/me3-theorem-v5-erratum-1.md`: 9f1e72e8220c61afe5bb2247cfd53c927dfb45c6ebd6e0506f77634bdac8e7b4
* `proof/charts-spec-v2.md`: d401774ec8c531560dd2e2cf3de52249547b6737dab5f14245a5da3e1acd5437
* `reductions/proof/reductions-v4.md`: be1f7190ba71f06b3e951886581d285cc74435a49e3c2983776cebb6101f6eb1
* every spec, run, leaf file, certificate, audit and receipt.
* Pin v3, `receipts/me3-candidate-pin-v3.json`: fa9327f2b35c31544128e612c55024caf97540d9fe05bdaf184861d8604d8b4b.
  On the parent's instruction there is no re-pin, so this erratum is not in the pin-v3 manifest.

**Sources.** Paths under `review/` are relative to `institute/runs/six-lane-2026-10-16/review/`.
* `review/me3-v5-math-claude-v1.note.md`, sha256 65c5ef6e84ada40e98ffe56ce67a30316f27f702105de492233409de5077ae24.
  Verdict ACCEPT-WITH-FIXES: 0 FATAL, 0 MAJOR, 8 textual MINOR findings m1–m8. Its SOURCE00 is v5 and its SOURCE01 is
  charts-spec-v2. "LF n" below means line n of the named file.
* `review/me3-v5-math-swc-followup-codex-v1.note.md`, sha256
  acb04f463f1ca7402e2f0c1621ad655c5e1594e40686839ed927e1fc461667dd. Verdict ACCEPT-WITH-FIXES. It resolves MAJOR 1 of
  `review/me3-v5-math-codex-v1.note.md` (sha256 2f977ed0…97b6). Its sole remaining MINOR, the "real span" wording, is
  handled by erratum 1 E1 together with m1 below.
* The reviewed parent derivation `review/me3-parent-dual-replay-v1/derivation-v1.md`, sha256
  a6b69bbaf175df779c4990f66ca6a979f3117594b1c5af202e0acda7c9870273, is quoted as "PD:n". It goes with the dual desk's
  `RESULT-v1.json`, sha256 995f6419c7917e3830f3b7491742dcf4116a8ed796e676bcc7ff9752756ccb2e: aggregate PASS, all six
  dual charts accepted with 0 failures, SWC replayed against d03.

**Reading rule.**
* The governing text is v5 as amended first by erratum 1 and then by this erratum. Where both errata amend the same
  passage, this one governs; see the precedence list at the end.
* "Old" quotes are verbatim.
* No item changes a chart, region, constant or certificate, or the Theorem's statement. Each item is one of:
  * a definition;
  * an inlined proof of a step that v5 only cited;
  * an explicit range check of a hard-coded exact value.

## Fix map

| Finding | Target (file:LF) | Repair | Section |
|---|---|---|---|
| Claude m1; Codex follow-up MINOR | v5:126 (erratum 1 E1); v5:129–130 | real-coefficient basis; the comparison with complex generators is withdrawn | m1 |
| Claude m2 | v5:8–10, 61–64, 133–147, 149 | Lemma D proved in full; v3's invalidity scoped; imports extended | m2 |
| Claude m3 | v5:141, 226 | per-method table: which α, and why α ≥ 0 | m3 |
| Claude m4 | charts-spec-v2:77–78, 102–103 | LD outer boxes; β_top = 15708/10000 < 3 < π | m4 |
| Claude m5 | v5:231–233 | LD2 SKIP sentence restricted to the LD2 target domain | m5 |
| Claude m6 | v5:226, 235; charts-spec-v2:50–56, 89, 92–93 | physical points of G, SWB, SWC, LW; padding faces | m6 |
| Claude m7 | v5:114, 151–162, 172–173, 223, 228, 245–247; charts-spec-v2:84 | feasible, a_k, S = S₂, ∂_r, R_P; pole projection P̄ | m7 |
| Claude m8 | v5:242 | D-cone split cited to reductions-v4 L1–L2 | m8 |

## m1. Real-coefficient basis — v5 LF126 and LF129–130

* **LF126.** Erratum 1 E1 governs: K is the cone of all nonnegative functions
  a·e^{−t} + b·e^{−(1+δ)t}cos ωt + b′·e^{−(1+δ)t}sin ωt with a, b, b′ ∈ ℝ, where b = Re c and b′ = −Im c.
  * Equivalent description (Claude m1): the real-valued elements of the complex span of e^{−t}, e^{−(1+ξ)t} and
    e^{−(1+ξ̄)t}.
  * Reason: for ω > 0 the three exponents are distinct, and the exponentials are linearly independent. So
    A·e^{−t} + B·e^{−(1+ξ)t} + C·e^{−(1+ξ̄)t} is real-valued iff A ∈ ℝ and C = B̄. It then equals
    e^{−t}[A + Re(2B·e^{−ξt})], i.e. a = A and c = 2B.
* **LF129–130.**
  * Old: "* K is not the conic hull of the three generators. For example, e^{−t}(1 − e^{−δt}cos ωt) ∈ K has a = 1 and
    c = −1, that is, coefficient −1/2 on each complex exponential."
  * New: "* K is not the set of nonnegative combinations of the three real basis functions e^{−t},
    e^{−(1+δ)t}cos ωt and e^{−(1+δ)t}sin ωt. Two members with a negative coefficient (both are nonnegative because
    e^{−δt} ≤ 1):
    * e^{−t}(1 − e^{−δt}cos ωt) ∈ K, with a = 1 and c = −1, has coefficient −1 on e^{−(1+δ)t}cos ωt;
    * e^{−t}(1 − e^{−δt}sin ωt) ∈ K, with a = 1 and c = i, has coefficient −1 on e^{−(1+δ)t}sin ωt."
  * The v5 comparison with "the conic hull of the three generators" put nonnegative coefficients on complex-valued
    generators. That is ill-posed for a cone of real functions, and it is withdrawn.
  * Erratum 1's "Addition after v5 LF130" is superseded by the second example above.
* **No mathematical consequence.** Every step uses the displayed definition at LF124.

## m2. Lemma D proved in full; scope of v3's invalidity; imports

**(1) What "INVALID" means for v3 (v5 LF8–10).**
* "INVALID" applies to two things:
  * the certificate evidence of v3 and pin v1 for the corner chart SWC (run d02, whose corner coefficients were
    float-rounded);
  * v3 and pin v1 as candidate packages.
* It does not assert that v3's written lemmas are false. The hostile reviews found v3 §2 (Lemma D) and v3 §3 (Lemma M)
  valid.
* v5 nevertheless no longer depends on citations to v3:
  * Lemma D is proved in full below. This replaces "As in v3" at LF138 and the review verdict at LF145, which becomes
    supplementary.
  * Lemma M is proved in full in erratum 1 E6, using the definitions in m7. This replaces "unchanged from v3 §3" in the
    heading at LF149, which now reads "Lemma M (full proof: erratum 1 E6; definitions: erratum 2 m7)".

**(2) Imports (append to v5 LF61–64).**
* **Reductions v4:** `reductions/proof/reductions-v4.md`, sha be1f7190…6eb1, with its exact certificates. The written
  proofs imported are:
  * Lemmas 1.2 and 1.4, Theorem L1(a)–(b) and the normal forms;
  * Lemmas 2.1–2.5 and Cor 2.6;
  * Theorems L3/L4 and Lemma 4.2;
  * Lemmas 5.1–5.5, Thm 5.6 and Cor 5.7;
  * Lemmas 6.1–6.6;
  * Cor 7.1 and Cor 7.2.
* **The seven chart certificates:** the leaf predicates and tilings of c03-primalP, d01-G, d01-SWB, d01-LW, d01-LD1,
  d01-LD2 and d03-SWC. They rest on the frozen specs, checker v3 and binding audit b04.
  * These are computational facts, conditional on the Arb and python-flint semantics of §6.
  * The parent primal desk replayed all 945,680 P leaves (`review/me3-parent-primal-reductions-v1/RESULT-v1.json`).
  * The parent dual desk replayed every leaf of the six dual charts, SWC against d03 (`RESULT-v1.json` 995f6419…cb2e).

**(3) Replacement for v5 LF133–147, from "Let Q_T(y) = …" through "Parametrization: …".**
This is the reviewed parent derivation PD:9–41 with the gaps filled.

Constants: T = 11/50, κ := 1/(1+T) = 50/61 and ρ := T/(1+T) = 1 − κ = 11/61.

**Lemma D.** Fix δ ≥ 0 and ω > 0, and put ξ = δ − iω. Let K be as at LF124 (with m1). For y > 0 put
Q_T(y) := (κy² − 2y + 2)/y³, and for θ > 0 put W(θ) := Q_T(θ(1+ξ))/Q_T(θ). Suppose that for every θ > 0, W(θ) has a
representation
  W(θ) = Σ_{k=1}^{m} λ_k e^{−ξt_k},  with m finite, λ_k ≥ 0, Σλ_k ≤ 1 and t_k ≥ 0.
The representation may depend on θ, and m = 0 (the empty sum, representing W = 0) is allowed. Then SCV(f) ≥ T for
every f ∈ K∖{0}.

*Proof.*
* **(a) Laplace identity.** For θ > 0 put q_θ(t) := (t − θ)² − ρθ². For Re z > 0, ∫₀^∞ t^k e^{−zt} dt = k!/z^{k+1}.
  Hence
    ∫₀^∞ q_θ(t)e^{−zt} dt = 2/z³ − 2θ/z² + (1 − ρ)θ²/z = 2/z³ − 2θ/z² + κθ²/z = θ³Q_T(θz).
* **(b) Positivity.** N(y) := κy² − 2y + 2 has κ > 0 and discriminant 4 − 8κ = −156/61 < 0. So N > 0 on ℝ, and
  Q_T(y) = N(y)/y³ > 0 for y > 0. In particular θ³Q_T(θ) > 0.
* **(c) The integral.** Let f = e^{−t}H ∈ K∖{0} with H = a + Re(ce^{−ξt}). The function q_θ is real and
  Re(1 + ξ) = 1 + δ > 0, so by (a)
    ∫₀^∞ q_θ f = a·θ³Q_T(θ) + Re(c·θ³Q_T(θ(1+ξ))) = θ³Q_T(θ)·[a + Re(cW(θ))].
* **(d) Nonnegativity.** Re(ce^{−ξt_k}) = H(t_k) − a, so
    a + Re(cW(θ)) = (1 − Σλ_k)a + Σλ_k H(t_k) ≥ 0.
  This uses a ≥ 0 (LF131), 1 − Σλ_k ≥ 0, λ_k ≥ 0, and H(t_k) ≥ 0 because t_k ≥ 0.
  With (b) this gives ∫q_θ f ≥ 0, i.e. ∫(t − θ)²f ≥ ρθ²∫f. Since ∫f > 0 (reductions-v4 Lemma 2.1; K = K_E), this says
  R_θ(f) ≥ ρ.
* **(e) Conclusion.** (d) holds for every θ > 0, so min_{θ>0} R_θ(f) ≥ ρ.
  * By reductions-v4 Lemma 2.2, min_θ R_θ(f) = SCV(f)/(1 + SCV(f)); f satisfies its §0.2 by Remark 2.3a.
  * x ↦ x/(1+x) is strictly increasing on [0, ∞), and ρ = T/(1+T).
  * Hence SCV(f) ≥ T. ∎

Remarks:
* Conversely, ∫q_θ f ≥ 0 for every θ > 0 ⟺ min_θ R_θ(f) ≥ ρ ⟺ SCV(f) ≥ T. Only "⇒" is used.
* No closure and no limit of representations is taken. For each θ a finite representation is required, and nothing is
  uniform in θ.

**Certificates.** Each gives the representation of Lemma D at the θ in question.
* **RADIAL.** W = |W|e^{iα} for some α ≥ 0, with |W| ≤ e^{−δα/ω}.
  * Take m = 1, t₁ = α/ω ≥ 0 and λ₁ = |W|e^{δα/ω} ∈ [0, 1]. Then
    λ₁e^{−ξt₁} = |W|e^{δα/ω}·e^{−δα/ω}e^{iα} = W.
  * If W = 0, take m = 0.
  * Any argument α ≥ 0 of W may be used. In particular, if g satisfies e^g = W and Im g ≥ 0, then α = Im g, and RADIAL
    reads Φ := ω Re g + δ Im g ≤ 0.
* **SMALL.** |W| ≤ e^{−2πδ/ω}.
  * If W ≠ 0, then α := Arg₊W ∈ [0, 2π) satisfies e^{−δα/ω} ≥ e^{−2πδ/ω} ≥ |W|, using δ ≥ 0. This is RADIAL.
  * If W = 0, take m = 0.
* **TRIANGLE.** W = a′ + b′e^{−ξt′} with a′, b′ ≥ 0, a′ + b′ ≤ 1 and t′ ≥ 0. Take m = 2, (λ₁, t₁) = (a′, 0) and
  (λ₂, t₂) = (b′, t′).

**Parametrization (replaces LF147).**
* For θ ∈ (0, ∞) put s := θ/(1+θ) ∈ (0, 1). This is a bijection, with θ = s/(1−s).
* Put N₁ := κs² − 2s(1−s) + 2(1−s)² = (κ+4)s² − 6s + 2. It is positive on ℝ, since its discriminant is
  36 − 8(κ+4) = 4 − 8κ = −156/61 < 0.
* Put w₁ := κs²/N₁, w₂ := −2s(1−s)/N₁, w₃ := 2(1−s)²/N₁ (so w₁ + w₂ + w₃ = 1) and zz := 1/(1+ξ). Then
    W = zz(w₁ + zz(w₂ + zz·w₃)).
* Derivation: W = N(θz)/(N(θ)z³) with z = 1 + ξ. Multiplying numerator and denominator by (1−s)² gives
  (κs²z² − 2s(1−s)z + 2(1−s)²)/(N₁z³).
* Chart boxes may contain s ∈ {0, 1}. The rational expression extends there, and the ball enclosures contain its value
  at every s ∈ (0, 1) of the box. Lemma D needs the representation only for s ∈ (0, 1) (PD:35–41).

## m3. Method table: the argument α behind each accepted test — v5 LF141 and LF226

**LF226, new first sentence:** "Every CERT leaf certifies, at each physical point of its box (m6), the RADIAL, SMALL or
TRIANGLE certificate of §2, with the argument α given in the table of erratum 2 m3."

Every accepting test is a certified ball inequality over the whole closed box. It therefore holds at each physical
point of the box (PD:45–47).

| Chart and accepting test | α used | Why α is an argument of W | Why α ≥ 0 | Inequality giving \|W\| ≤ e^{−δα/ω} |
|---|---|---|---|---|
| G and LW: SMALL | Arg₊W (any α if W = 0) | definition | α ∈ [0, 2π) | G: \|W\| < e^{−2πδ_h/ω_l} ≤ e^{−2πδ/ω}. LW: \|W\| < e^{−2πδ_hν_h} ≤ e^{−2πδ/ω}. Then SMALL ⇒ RADIAL |
| G: RADIAL or RADIAL-MVF; branch Im W > 0 on the box | Arg W (principal) | principal argument | Arg W ∈ (0, π) | F := ω log\|W\| + δα < 0, naive ball or MVF |
| G: branch Im W < 0 on the box | Arg W + 2π | differs from Arg W by 2π | Arg W ∈ (−π, 0), so α ∈ (π, 2π) | same F < 0 |
| G: branch Re W < 0 on the box | π + Arg(−W) = π + atan(Im W/Re W) | e^{iα} = −(−W)/\|W\| = W/\|W\| | Arg(−W) ∈ (−π/2, π/2), so α ∈ (π/2, 3π/2) | same F < 0, with Log(−W) in the MVF |
| G: TRIANGLE (no accepted leaf in d01-G) | none; t′ = θ′/ω | — | θ′ ≥ 31415/10⁴ > 0 | the explicit two-term representation |
| SWB: bedge or bedge-mvf | Im g(δ − iω), where g is the analytic logarithm of W on R = [δ_l, δ_h] − i[0, ω_h] that is real on the real axis | e^g = W | second predicate: Im g/ω ≥ −g′ − ω_h²\|g‴\|/6 − ω_h⁴M₅/120 > 0, so α > 0 | first predicate: log\|W\| + (δ/ω)α = Φ/ω ≤ B + ω_h²·max(C, 0) + ω_h⁴(M₄/24 + δ_hM₅/120) < 0 |
| SWC: corner or corner-mvf | Im g(ξ), with g := Log(1 − pξ) + Log(1 − p̄ξ) − 3Log(1 + ξ) = Σ_{j≥1} c_jξ^j | e^g = W | second predicate: Ig_N − tail_Ig ≥ 0, so Im g/ω = Ig ≥ 0 and α ≥ 0 | first predicate: log\|W\| + (δ/ω)α = \|ξ\|²Ψ ≤ \|ξ\|²(Ψ_N + tail_Ψ) < 0 |
| LD1, β_l > 0: candidate test | β + a, where a is: Arg P (if Re P > 0 or Im P > 0 on the box); Arg P + 2π (if Im P < 0); π + Arg(−P) (if Re P < 0) | W = ζP and ζ = d cos β·e^{iβ}, with d cos β > 0 at physical points | the ball test α ≥ 0 is certified | \|W\| < exp(−(1−d)·α/tan β) = e^{−δα/ω}, since δ/ω = (1−d)/tan β |
| LD1, β_l > 0: fallback | Arg₊W | definition | α ∈ [0, 2π) | \|W\| < exp(−(1−d)·2π/tan β_l) ≤ e^{−δα/ω}, since 0 ≤ α/tan β ≤ 2π/tan β_l for physical β ∈ [β_l, π/2) |
| LD1, β_l = 0: mvt0 | β + Arg P(β) (principal), with Re P > 0 on the box | as for the candidate test | Arg P(0) = 0 since P(0) > 0, and α(β) = ∫₀^β (1 + Im(P_β/P)) du ≥ 0 because 1 + inf Im(P_β/P) ≥ 0 is certified | α/tan β ≤ (1 + sup Im(P_β/P))·β/tan β ≤ 1 + sup, and \|W\| < exp(−(1−d)(1 + sup)) |
| LD2: ld2 (the same three tests) | as for LD1, with P̂ in place of P (P = ρ_t²P̂, W = (1−χ)ρ_t³e^{iβ}P̂) | (1−χ)ρ_t³ > 0 at physical points | as for LD1 | as for LD1, with 1 in place of 1 − d; this is conservative since 0 < 1 − d ≤ 1 and the exponent is ≥ 0 |

Notes:
* **G branches.** Quoting PD:54–56: "RADIAL on a fixed branch. The branch region is certified on the box: Im W > 0
  (α = Arg W), Im W < 0 (α = Arg W + 2π) or Re W < 0 (α = π + atan(Im W/Re W)). On that region α is continuous and
  smooth, with values in [0, 2π)."
  * The branch condition is certified for the enclosure of W over the whole box, so it holds at every box point. That
    makes α a smooth function on the box and validates the mean-value form of F.
  * The code also requires the box midpoint to lie on the same branch.
  * If α ∈ (−π, 0) were used on the Im W < 0 branch, F < 0 would not imply RADIAL. That choice is never made.
* **G TRIANGLE.** θ′ := ⌊10⁴θ̃⌋/10⁴, where θ̃ ≥ π is a float bisection value; hence θ′ ≥ 31415/10⁴. Its accuracy is
  irrelevant (PD:27–29). d01-G has no CERT:triangle leaf, so the float heuristic lies on no accepted path.
* **SWB logarithm.**
  * On the convex closed rectangle R (with z = 1 + ξ), W = q(s, z)/(N₁z³) has no zero and no pole:
    * z ≠ 0;
    * for s > 0, q(s, z) = κs²(z − z₁)(z − z₂) with z_{1,2} = (1−s)(1 ± i√(2κ−1))/(κs), and an accepted box has
      finite enclosures of v_{1,2} = 1/(z − z_{1,2}) and of 1/|z| on R, since otherwise M₄ and M₅ are not finite and
      the box is rejected;
    * for s = 0, W = 1/z³.
  * So W has an analytic logarithm on R, unique up to 2πik. Fix the branch that is real on the real segment.
  * W > 0 there. For s ∈ (0, 1), q(s, ·) has discriminant 4s²(1−s)²(1 − 2κ) < 0; for s = 0 and s = 1, q = 2 and
    q = κz² respectively.
  * The derivatives g^{(k)} do not depend on the branch. Taylor's theorem in y for y ↦ g(δ − iy) then gives both
    predicates (PD:82–93).
* **SWC logarithm.**
  * |ξ| ≤ √(0.3² + 0.2²) = √13/10 < 1, and |p|² = B = κs²/N₁ ≤ 100/39, because 100N₁ − 39κs² = 50(3s − 2)². Hence
    |pξ| ≤ 1/√3 < 1.
  * So 1 − pξ, 1 − p̄ξ and 1 + ξ all lie in the open disc of radius 1 about 1, where principal logarithms are analytic.
    Thus g is analytic, g(0) = 0, e^g = W, and c_j = (−2Re(p^j) + 3(−1)^j)/j (PD:95–98; Codex SWC follow-up).
  * With ξ^m = X_m − iωU_m, Φ = ω|ξ|²Ψ and Im g = ωIg (PD:99–100).
  * The worker's accepting predicate is Ig_N − tail_Ig ≥ 0 (charts-spec-v1; `me3dual_v9.py` LF68/73), which already
    gives α ≥ 0. The parent dual desk replayed the strict form, Ig_N − tail_Ig > 0, on all 34,304 SWC leaves with 0
    failures (PD:104; RESULT-v1).
* **LD charts.** "ζ := 1/(1+ξ) = d cos β e^{iβ} and δ/ω = (1−d)/tan β" (PD:62), and "the factor 1 − d is replaced by
  1 … conservative because every exponent is ≥ 0" (PD:76).
  * For mvt0, the mean value theorem is applied in β at fixed (s, d) for LD1 and at fixed (χ, ρ_t) for LD2. The
    segment from β = 0 to the point stays in the box because β_l = 0 (PD:69–72).

## m4. LD outer boxes and β_top — charts-spec-v2 LF77–78 and LF102–103

The outer boxes are the exact breakpoint ranges of `code/spec_dual_v1.json`. They are hard-coded in `check_cover_v3.py`
and verified as exact rational equalities by b03-cover-LD1 and b03-cover-LD2, both audit_ok.
* LD1: s ∈ [1/16, 1], d ∈ [0, 1/65], β ∈ [0, β_top].
* LD2: χ ∈ [0, 1], ρ_t ∈ [0, 81/1040], β ∈ [0, β_top].
* Here β_top := 15708/10000.

**Exact range facts.**
* π/2 < β_top, since π < 3.1416. This is certified by a ball comparison in check_cover_v3 and by the dual desk (PD:64).
* β_top = 15708/10000 < 3 < π, since 15708 < 30000 and π > 3.
* So every leaf box has β-range [β_l, β_h] ⊆ [0, β_top] ⊂ [0, π], where cos is strictly decreasing.

**skip-d (replaces the justification at LF77–78).** Let (χ, ρ_t, β) be any point of a skip-d leaf box.
* 0 ≤ χ ≤ χ_h ≤ 1 gives 0 ≤ 1 − χ_h ≤ 1 − χ, and 0 ≤ ρ_{t,l} ≤ ρ_t.
* Hence (1 − χ)ρ_t ≥ (1 − χ_h)ρ_{t,l} > cos(β_l)/65 ≥ cos(β)/65.
* If β ∈ (0, π/2), then cos β > 0 and d = (1 − χ)ρ_t/cos β > 1/65. Otherwise β ∉ (0, π/2). Either way the point is
  not LD2-physical (PD:78–79).

**Checker description (amends LF102–103).** "For LD charts it also certifies β_top > π/2 by a ball comparison. The
hard-coded outer-domain equality, which the checker verifies exactly, gives β ≤ β_top = 15708/10000 < 3 < π."

No code or chart rerun is needed. The bound is an exact rational consequence of an outer domain that has already been
verified exactly, together with π > 3.

## m5. LD2 SKIP sentence — v5 LF231–233

* **Old:** "* LD2's `SKIP:skip-s` and `SKIP:skip-d` leaves contain no point of LD2's physical domain (0 < s ≤ 1/16,
  0 < d ≤ 1/65, 0 < β < π/2). A skip-s box has s > 1/16 throughout; such s are physical points of LD1, whose leaves
  are all CERT. A skip-d box has d > 1/65 or cos β ≤ 0 throughout (charts-spec-v2)."
* **New:**
  * "The LD2 target domain is δ ≥ 64 (i.e. 0 < d ≤ 1/65), 0 < s ≤ 1/16 and β = arctan(ω/(1+δ)) ∈ (0, π/2).
  * Each target is an LD2-physical point (χ, ρ_t, β), with ρ_t = s + d cos β ∈ (0, 81/1040] and χ = s/ρ_t ∈ (0, 1)
    (charts-spec-v2 LF82–83). By the tiling it lies in some LD2 leaf.
  * No SKIP leaf contains an LD2-physical point:
    * skip-s: s = χρ_t ≥ χ_lρ_{t,l} > 1/16;
    * skip-d: erratum 2 m4.
  * Hence every LD2 leaf containing the target is a CERT:ld2 leaf. A SKIP leaf excludes the LD2 target domain and claims
    nothing about other points. In particular, a skip-s box may contain points with d > 1/65 or β ≥ π/2, which are
    physical for neither LD chart.
  * Targets with δ ≥ 64 and s ∈ [1/16, 1) are LD1-physical points, and every LD1 leaf is CERT:ld1."

## m6. Physical points of G, SWB, SWC and LW; padding faces — v5 LF226, LF235; charts-spec-v2 LF50–56, 89, 92–93

The outer boxes are the exact breakpoint ranges of the frozen specs (spec_dual_v1, and spec_dual_v3 for SWC), verified
by checker v3.

| Chart | Outer box | Physical points | Padding faces (nothing claimed) |
|---|---|---|---|
| G | s ∈ [0, 1], δ ∈ [0, 64], ω ∈ [1/5, 640] | 0 < s < 1 | s ∈ {0, 1} |
| SWB | s ∈ [0, 1], δ ∈ [3/10, 64], ω ∈ [0, 1/5] | 0 < s < 1, ω > 0 | s ∈ {0, 1}; ω = 0 |
| SWC | s ∈ [0, 1], δ ∈ [0, 3/10], ω ∈ [0, 1/5] | 0 < s < 1, ω > 0 | s ∈ {0, 1}; ω = 0 |
| LW | s ∈ [0, 1], δ ∈ [0, 64], ν = 1/ω ∈ [0, 1/640] | 0 < s < 1, ν > 0 | s ∈ {0, 1}; ν = 0 |
| LD1, LD2 | m4 | charts-spec-v2 LF51–52 | charts-spec-v2 LF54 |

* **Chart point.** A pole (δ, ω), with δ ≥ 0 and ω > 0, and a test centre θ = s/(1−s) correspond to:
  * (s, δ, ω) in G, SWB and SWC;
  * (s, δ, 1/ω) in LW;
  * (s, 1/(1+δ), arctan(ω/(1+δ))) in LD1;
  * (s/ρ_t, ρ_t, β) in LD2, with d = 1/(1+δ), β = arctan(ω/(1+δ)) and ρ_t = s + d cos β.
* **Padding faces** are extensions:
  * s ∈ {0, 1} are not test centres;
  * at ω = 0 the normalized SWB and SWC quantities extend continuously, but RADIAL is concluded only for ω > 0;
  * at ν = 0, W = 0.
* **What the assembly consumes.** Dual certificates are used only at points with δ > 0 and (δ, ω) ∉ P̄ (m7).
  * Points with δ = 0 are D1 and are handled by Cor 5.7.
  * The dual certificates are also valid there, since Lemma D allows δ = 0. That consequence (SCV ≥ T on those D1
    cones) is consistent with L5 but is not used (Claude m6, consistency probe).

**LF235.**
* Old: "Hence, for every dual-assigned (δ, ω) and every s ∈ (0, 1), the corresponding chart point is a physical point
  of a CERT leaf."
* New:
  * "Hence, for every dual-assigned (δ, ω) (m7: δ > 0 and (δ, ω) ∉ P̄) and every s ∈ (0, 1), the chart point above is a
    physical point of the assigned chart (LD1 for s ≥ 1/16 and LD2 for s ≤ 1/16 when δ ≥ 64).
  * Every leaf containing that point is a CERT leaf:
    * in G, because G's SKIP boxes lie in P̄ (m7);
    * in LD2, by m5;
    * SWB, SWC, LW and LD1 have no SKIP leaves.
  * Its certificate (m3) gives the representation required by Lemma D at that θ."

## m7. Notation for Lemma M and the P/dual assignment

Targets: v5 LF114, LF151–162, LF172–173, LF223, LF228 and LF245–247, and charts-spec-v2 LF84. The definitions below are
the ones used by erratum 1 E6.

**Definitions.**
* **R_P** := [0, 3] × [1/5, 40] × [0, 31416/5000] in (r, ω, φ). This is the box that run c03 tiles, called "chart P"
  at LF151.
* For (r, ω, φ) ∈ R_P put c := (1 − ir)e^{(r−i)φ}, ζ := 1/(1 + rω − iω) and a_k := 1 − Re(cζ^{k+1}) for k = 0, 1, 2.
* **Feasible** means: r = 0 (any φ), or r > 0 and 0 ≤ φ ≤ θ₁(r).
  * For feasible r > 0, a_k = m_k/k!, where m_k are the moments of the extreme ray e^{−t}h_{φ/ω} of the D2 cone with
    δ = rω (reductions-v4 Lemmas 6.3, 6.4 and 6.6).
  * For r = 0 they are the moments of the D1 ray e^{−t}(1 − cos(ωt − φ)) (Lemma 5.2).
  * These rays are nonzero and nonnegative, so a₁ = m₁ > 0 (Lemma 2.1).
* **S** := 2a₀a₂/a₁² − 1, wherever a₁ > 0. At feasible points S is the SCV of the ray, and for r > 0 it equals
  S₂(r, ω, φ) of reductions-v4 Cor 7.2 (LF114).
* **∂_r** is the derivative in r at fixed (ω, φ), with δ = rω, so c and ζ both vary.
  * a_k′ := ∂_r a_k = −Re(cζ^{k+1}[φ + (r − i)/(1 + r²) − (k + 1)ωζ]). This is an exact sympy identity, checked in run
    v01 and by the parent desk in f01.
  * Put D := a₀′a₁a₂ + a₀a₁a₂′ − 2a₀a₁′a₂ = a₁(a₀′a₂ + a₀a₂′) − 2a₀a₂a₁′. Then ∂_r S = 2D/a₁³.
  * DPOS requires a₁ > 0, so the certified sign D > 0 is the sign of ∂_r S.
* **Leaf outcomes of c03.**
  * **INFEAS:** φ_lo > π, r_lo > 0 and g_{r_lo}(φ_lo) > 1. This gives φ_lo > θ₁(r_lo), because g_{r_lo} ≤ 1 on
    [π, θ₁(r_lo)] and θ₁ < 2π. Every box point then has φ ≥ φ_lo > θ₁(r_lo) ≥ θ₁(r), since θ₁ is decreasing. So no box
    point is feasible.
  * **SGE:** a₁ > 0 and 2a₀a₂ − (1+T)a₁² > 0 on the box, i.e. S > T.
  * **DPOS:** a₀, a₁, a₂ > 0 and D > 0 on the box, i.e. ∂_r S > 0.
* **Pole projection:** P̄ := {(δ, ω) : 1/5 ≤ ω ≤ 40, 0 ≤ δ ≤ 3ω} = {(rω, ω) : (r, ω) ∈ [0, 3] × [1/5, 40]}.
  * P̄ reaches δ = 120.
  * For (δ, ω) ∈ P̄ with δ > 0: r = δ/ω ∈ (0, 3], and every phase φ ∈ [0, θ₁(r)] satisfies φ ≤ θ₁(r) < 2π <
    31416/5000. So every extreme ray of the cone is a feasible point of R_P with r > 0.

**Assignment.** This replaces the "Assigned set" entries of the P and G rows at LF172–173, the coverage list at
LF220–224, and LF245–247. Each D2 pole (δ > 0, ω > 0), and hence each whole D2 cone, is assigned as follows.
* **P̄-assigned**, if (δ, ω) ∈ P̄. Lemma M applies at every phase, and Cor 7.2 then gives SCV > v_cos on the cone.
* **Dual-assigned** otherwise, to one of:
  * LD1 ∪ LD2, if δ ≥ 64;
  * LW, if δ < 64 and ω ≥ 640;
  * G, if δ < 64 and 1/5 ≤ ω ≤ 640;
  * SWC, if δ ≤ 3/10 and ω < 1/5;
  * SWB, if 3/10 ≤ δ < 64 and ω < 1/5.

  In each case Lemma D, with m6, gives SCV ≥ T > 773/3844 ≥ v_cos on the cone.

The two classes are exhaustive. The overlap of P̄ with LD (64 ≤ δ ≤ 120) is harmless: Lemma M holds on all of P̄, and
each dual certificate holds wherever it is certified. The assignment merely picks one.

**Line edits.**
* **LF172, P row:** the assigned set is P̄, with δ allowed above 64.
* **LF173, G row:** "δ ∈ [0, 64], ω ∈ [1/5, 640], (δ, ω) ∉ P̄", replacing "minus P", which subtracted an (r, ω, φ) box
  from a (δ, ω) set.
* **LF223:**
  * "(δ, ω) ∈ P̄: P; otherwise, δ < 64 and ω ∈ [1/5, 640]: G".
  * LF221–222 and LF224 apply to (δ, ω) ∉ P̄.
* **LF228:**
  * "lie in P" becomes "lie in P̄". A G SKIP box is a subset of P̄: every point has
    1/5 ≤ ω_l ≤ ω ≤ ω_h ≤ 40 and δ ≤ δ_h ≤ 3ω_l ≤ 3ω.
  * Erratum 1 E3's split is kept, with P read as P̄: δ > 0 goes to Lemma M with Cor 7.2, and δ = 0 to Cor 5.7.
* **LF245:** "D2 with dual-assigned poles" means δ > 0 and (δ, ω) ∉ P̄.
* **LF246:** "The remaining D2 cones (ω ∈ [1/5, 40], r ≤ 3)" becomes "The P̄-assigned D2 cones ((δ, ω) ∈ P̄, δ > 0)".
* **Lemma M (LF156, LF159):** "∈ P" and "inside P" mean "∈ R_P" and "inside R_P".
* **charts-spec-v2 LF84:** it writes μ for the test centre that v5 calls θ; μ = θ = s/(1−s).

## m8. Exhaustiveness at the D-cone split — v5 LF242

* **Old:** "* Otherwise, after time scaling, X lies in a D cone."
* **New:** "* Otherwise the density f of X has a contributing non-real exponent.
  * By reductions-v4 Theorem L1(a)(2),(4), via Lemma 1.2: E(f) = {λ₀, λ, λ̄} with λ₀ < 0 real, Re λ ≤ λ₀, and all three
    simple. So the pair is at least as damped as the real exponent. If it were strictly less damped, or if no real
    exponent contributed, Lemma 1.2 would leave the nonnegative f with no contributing pair (Cor 2.6:
    K_E = K_{{λ₀}}).
  * Write λ₀ = −μ and λ = −μ′ + iν, with μ > 0, μ′ ≥ μ and ν > 0 (choosing the conjugate if needed).
  * By the normal forms and Lemma 1.4, g(t) := f(t/μ) has E(g) = {−1, −(1+δ) ± iω} with δ = μ′/μ − 1 ≥ 0 and
    ω = ν/μ > 0, and SCV(g) = SCV(f).
  * So g/∫g lies in the D1 cone (δ = 0; Lemma 5.1) or in the D2 cone K of §2 (δ > 0; reductions-v4 §6, K = K_E).
  * Its coefficient on e^{−t} is a > 0: by Lemma 6.1 for D2, and for D1 by Lemma 5.1 (a ≥ √(b² + c²) > 0, as the pair
    contributes).
  * The real-exponent case, including lower orders and padding, is the first bullet (Theorem L3, Lemma 2.5,
    Cor 2.6)."

No pole configuration is assumed silently. The case split (R) / (D1) / (D2) is that of reductions-v4 L1(a)(4), its
normal forms and Cor 2.6.

## Precedence with erratum 1

| v5 passage | Governing text |
|---|---|
| LF21–22, LF126 | erratum 1 E1 (m1 adds an equivalent description) |
| LF129–130 | m1; supersedes erratum 1 E1's "Addition after v5 LF130" |
| LF23–24, LF228–230 | erratum 1 E3, with P read as P̄ (m7) |
| LF55 | erratum 1 E5 |
| LF74–75, LF335 | erratum 1 E2 |
| LF133–147 (Lemma D) | m2 |
| LF151–162 (Lemma M) | erratum 1 E6, with the definitions of m7 |
| LF172–173, LF220–224, LF245–247 | m7 |
| LF226, LF235 | m3 and m6 |
| LF231–233 | m5 |
| LF242 | m8 |

## Scope of the Claude review (imported versus audited), and the effect of this erratum

* **Audited by hand in that review:**
  * L5's exact values;
  * L3–L4's h-certificate;
  * Lemma D and the three certificates;
  * θ₁, feasibility, the INFEAS rule, the L6 moments, the DPOS sign factor and Lemma M;
  * the SWC coefficients, radius and control value Ig₂₀ = 2 − 2^{−19};
  * the SWB remainder orders;
  * the LD coordinates, candidates, mvt0 and the 1 − d replacement;
  * the SKIP implications, the s-union and the quadrant coverage;
  * the leaf-count sums.
* **Imported there:**
  * reductions v4: L1–L2 and the assembly, Lemma 2.4, the real-exponent minimum, Lemmas 4.2, 5.1 and 5.4, Thm 5.6,
    Cor 5.7, Lemmas 6.3/6.4, and Cor 7.2 (structure only);
  * the certified computations: the truth of every leaf predicate, the tilings and the SKIP re-checks;
  * the spec-v1 definitions, G's α branches, and the LD and LW outer domains.
* **What this erratum changes about the imported items:**
  * G's α branches and the LD/LW outer domains are now written down exactly (m3, m4, m6), together with what each
    accepted test asserts.
  * Their truth on every leaf is still a certified computation, replayed by the parent dual desk.
* **Not examined by that review, and covered elsewhere:**
  * Arb and python-flint semantics (v5 §6; float-audit erratum 1; smokes s02 and s04);
  * the float audits;
  * provenance and binding (b04; the parent pin closures).
