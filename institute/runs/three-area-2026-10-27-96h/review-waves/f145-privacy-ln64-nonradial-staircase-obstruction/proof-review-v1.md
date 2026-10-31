# proof-review-v1 — f145-privacy-ln64-nonradial-staircase-obstruction

**Kind:** INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (proof-reviewer slot; outputs restricted to `proof-review-v1.md` and `proof-*` files).
**Authority:** `contract-addendum-2-frontier-first-owner-direction-v1.json` (as named in the manifest).
**Observed native clock before this write:** `2026-10-28T21:24:32-0700 PDT` (= `2026-10-29T04:24:32Z`).
**Manifest:** `manifest-v1.json`, SHA256 `8b11415d77d1cc66f4a79cf59f4ed441de8ff46436ea06ba6755944214fe6c01`, 3312 bytes — verified at `2026-10-29T04:09:14Z`.

## 0. Read order, verification, and boundaries actually honoured

Inputs were hashed before reading (all three at `2026-10-29T04:09:23Z`) and read completely, raw, in the declared order:

| # | path | SHA256 | bytes | LF | status |
|---|---|---|---|---|---|
| 1 | `parent-required-numeric-correction-v1.json` | `3b29787c…1197bb` (full: `3b29787c171857d35099fded30bc7d1c2bd9b957537d64b54891209a8a1197bb`) | 1446 | 16 | match; read FIRST |
| 2 | `…/privacy-diamond-mse/frontier-20261028-ln64-rational-nonradial-obstruction-v1.md` | `028397b5e5c5cae583f9fc69ed1efadbaeda169c729d3cb878b74b1e2cc14e01` | 7063 | 87 | match; read after 1 |
| 3 | `written-releases/info-1-mda-primary-definitions-v1.md` | `25740af38e4ed3d36e925be499e7a0fa4920182989c8ba55c99811538fb03718` | 1542 | 9 | match |

Not read, by manifest/assignment: the optional MDA26 parent file named in the candidate's §1 (`privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`), the arXiv HTML pin named in input 3 (no public-source expansion), and the sibling `arithmetic-*` files that were present in the directory at listing time (not manifest inputs; not opened, to keep this review independent). No author code exists in the candidate (prose only); nothing authored by others was imported or executed. No Git, deletion, external model, network, or author contact.

Files written by this reviewer (all `proof-` prefixed, in the review directory):

| file | SHA256 | note |
|---|---|---|
| `proof-controls-v1.py` | `d24c80e22c4fc7de27ef4ec93d84428c84ed7fc0bb971a3b012fba2f76388d5d` | first control run; **kept on record** |
| `proof-controls-v1-receipt.json` | `b4421dfd27e152d89fee89e11fda152d24ac319ebfb0666e9cb382692abb8051` | 115 checks, **1 FAIL** (reviewer checker defect, see §8) |
| `proof-controls-v2.py` | `319f357071054d4496d0cfabb79a0fd097ad05562b6996e7c06b5f27cd30d7a6` | same script; hull table extended k≤13 → k≤17 |
| `proof-controls-v2-receipt.json` | `28c3572500519e3c57f2a6ce1b1d3615491c73ccf5613a1c40b15512a341c690` | 115 checks, 0 FAIL; clock `04:23:09Z`–`04:23:10Z` |
| `proof-review-v1.md` | this file | |

## 1. Model and notation (from input 3 and the candidate's §1)

Registered model: additive-noise laws on R², pure ε-DP for **every Borel event** and **every shift in the full closed ℓ₁ diamond** D = {|x₁|+|x₂| ≤ 1}, cost J = E‖X‖₂². Here ε = ln 64, b = e^{−ε} = 1/64, m = b/(1−b) = 1/63 (verified exactly).

Candidate objects (Eq.(1)): a = 3761763123·10⁻¹⁰, z = a + 10⁻¹⁰, η = 1/100, S = aD ∩ {‖x‖∞ ≤ a−η}, n_S(x) = min{k ∈ Z≥0 : x ∈ S + kD}, P_S the law with density ∝ b^{n_S}. Throughout, T_R := {‖x‖₁ ≤ R, ‖x‖∞ ≤ R−η}, so S = T_a. Verified: η < a/2 (a/2 ≈ 0.188).

## 2. All-k shell geometry — independent proof of candidate Eq.(3)

**Lemma 1 (exact ℓ₁ distance to S).** Let 0 < η ≤ a, c := a−η, and for x ∈ R² put p = |x₁|, q = |x₂|. Then
dist₁(x,S) := min_{s∈S} ‖x−s‖₁ = p + q − min( a , min(p,c) + min(q,c) ) = max( p+q−a , (p−c)⁺ + (q−c)⁺ ).

*Proof.* S is invariant under coordinate sign changes, and ‖(σ₁p,σ₂q) − s‖₁ = ‖(p,q) − (σ₁s₁,σ₂s₂)‖₁, so dist₁(x,S) = dist₁((p,q),S); assume x = (p,q), p,q ≥ 0. For s ∈ S let s' := (clip(s₁;0,p), clip(s₂;0,q)). Clipping never increases |sᵢ|, and both constraints defining S are monotone in |s₁|,|s₂|, so s' ∈ S; clipping toward the target never increases |p−s₁| or |q−s₂|. Hence the minimum is attained with 0 ≤ s₁ ≤ p, 0 ≤ s₂ ≤ q, where ‖x−s‖₁ = p+q−(s₁+s₂). Maximising s₁+s₂ under s₁ ≤ min(p,c), s₂ ≤ min(q,c), s₁+s₂ ≤ a gives min(a, min(p,c)+min(q,c)); it is attained (if min(p,c)+min(q,c) ≤ a take sᵢ = min(·,c); otherwise s₁ = min(p,c) ≤ c < a and s₂ = a−s₁, which lies in [0, min(q,c)] exactly because a ≤ min(p,c)+min(q,c)). The second form follows from p+q−min(A,B) = max(p+q−A, p+q−B) and p+q−min(p,c)−min(q,c) = (p−c)⁺+(q−c)⁺. ∎

**Theorem A (candidate (3), all k, all signs, all boundaries).** If 2η ≤ a then for every real k ≥ 0 (in particular every integer k ≥ 0): S + kD = T_{a+k}. Consequently n_S(x) = ⌈dist₁(x,S)⌉ and the shells are {n_S = k} = T_{a+k} \ T_{a+k−1} (T_{a−1} := ∅).

*Proof.* S is compact and kD is compact, convex, with 0 ∈ kD, so x ∈ S+kD ⟺ dist₁(x,S) ≤ k (the minimum over S is attained; k = 0 gives S+{0} = S = T_a). By Lemma 1, dist₁(x,S) ≤ k ⟺ [p+q ≤ a+k] ∧ [(p−c)⁺+(q−c)⁺ ≤ k]. Claim: given p+q ≤ a+k, the second condition ⟺ [p ≤ a+k−η] ∧ [q ≤ a+k−η].
(⇒) If p > c then p−c ≤ k, i.e. p ≤ a+k−η; if p ≤ c then p ≤ a−η ≤ a+k−η. Same for q.
(⇐) Neither coordinate exceeds c: 0 ≤ k. Exactly one, say p > c ≥ q: p−c ≤ (a+k−η)−(a−η) = k. Both exceed c: (p−c)+(q−c) = p+q−2a+2η ≤ (a+k)−2a+2η = k−(a−2η) ≤ k, **using 2η ≤ a**.
Hence x ∈ S+kD ⟺ ‖x‖₁ ≤ a+k and ‖x‖∞ ≤ a+k−η ⟺ x ∈ T_{a+k}. All sign patterns are covered by Lemma 1; boundary points are included on both sides because every inequality is non-strict and both sets are closed. ∎

The hypothesis is sharp: with 2η > a the identity fails (negative control §8: a′ = 3/10, η′ = 1/5, k = 1, witness (11/10, 1/5) ∈ T_{13/10} \ (S′+D)). The candidate's hypothesis "η < a/2" is a strict instance of 2η ≤ a and holds here.

*Comparison with the author's proof of (3).* The author's reduction argument (reduce each coordinate to ≤ a−η, then lower until the ℓ₁ sum is a; total reduction x+y−a ≤ k) is correct and its case split (both / only one coordinate needs reduction) matches the cases above, with the author's "k−a+2η < k" being the double-overshoot case. Two presentational gaps, neither an error: the construction does not state that the lowered point keeps both coordinates in [0, a−η] (true because step 2 only lowers coordinates and step 1 already enforced ≤ a−η), and the intermediate bound k−a+2η is not the bound finally used. **Verdict for all-k geometry: no defect; MINOR (presentation only).**

The index is genuinely non-radial: at r = (2a−η)/2 ∈ (a−η, a), n_S(r,0) = 1 while n_S(r/2, r/2) = 0 (control 4).

## 3. Full-event, full-closed-D privacy — independent proof

**Theorem B.** (i) For all x ∈ R² and all h ∈ D: |n_S(x+h) − n_S(x)| ≤ 1. (ii) Z_S := ∫ b^{n_S} dx < ∞, so f := b^{n_S}/Z_S is a Borel probability density. (iii) For every Borel A ⊂ R² and every h in the closed diamond D: e^{−ε} P(X∈A) ≤ P(X ∈ A+h) ≤ e^{ε} P(X∈A).

*Proof.* (i) dist₁(·,S) is 1-Lipschitz for ‖·‖₁ (triangle inequality), so |dist₁(x+h,S) − dist₁(x,S)| ≤ ‖h‖₁ ≤ 1, and ⌈u⌉ ≤ ⌈v+1⌉ = ⌈v⌉+1 whenever u ≤ v+1. (The author's route — (S+kD)+D = S+(k+1)D by convexity of D, applied to ±h — is equally valid.) (ii) n_S is Borel (each T_R is closed) and by Theorem A, Z_S = Σ_k b^k Leb(T_{a+k}\T_{a+k−1}) ≤ Σ_k b^k·2(a+k)² < ∞. (iii) Pointwise and everywhere, f(x+h)/f(x) = b^{n_S(x+h)−n_S(x)} ∈ [b, 1/b] = [e^{−ε}, e^{ε}]. Hence P(X∈A+h) = ∫_A f(x+h)dx ≤ e^{ε}∫_A f = e^{ε}P(X∈A) and likewise ≥ e^{−ε}P(X∈A). For the additive mechanism M(d) = q(d)+X with q(d)−q(d′) ∈ D this is exactly the registered condition (A ranges over all Borel sets, including null sets, where both sides are 0; h ranges over the full closed D, including ‖h‖₁ = 1). ∎

**Verdict for true all-event privacy of P_S: no defect (PASS).** The property is exact, not approximate, and needs neither η < a/2 nor the specific rationals; those enter only the cost computation.

## 4. Cap moments, shell areas, and the infinite geometric sum — recomputed

**Cap.** The +x₁ cap of T_R's complement in RD is {x₁ ≥ R−η, |x₂| ≤ R−x₁}; with x₁ = R−u, 0 ≤ u ≤ η:
area = ∫₀^η 2u du = η²; ∫(x₁²+x₂²) = ∫₀^η [2u(R−u)² + (2/3)u³] du = R²η² − (4/3)Rη³ + η⁴/2 + η⁴/6 = **R²η² − (4/3)Rη³ + (2/3)η⁴**, matching candidate (4). The four caps are pairwise disjoint and non-degenerate whenever R > 2η (two adjacent caps would need x₁+x₂ > 2R−2η > R), which holds for every R = a+k ≥ a > 2η.

**Octagon T_R.** Leb(RD) = 2R², ∫_{RD}‖x‖₂² = (2/3)R⁴ (∫_D x₁² = 4∫₀¹x²(1−x)dx = 1/3). Hence
L(R) := Leb(T_R) = 2R² − 4η², Q(R) := ∫_{T_R}‖x‖₂² = (2/3)R⁴ − 4R²η² + (16/3)Rη³ − (8/3)η⁴.
Both confirmed exactly by independent polygon integration (shoelace and Green's-theorem second moment on the 8 rational vertices (±(R−η),±η),(±η,±(R−η))) for R ∈ {a, a+1, a+2, a+5, 7/3, 1, 3/100}, and the identity diamond − 4·cap = octagon holds exactly for area and moment (controls §2).

**Geometric sum.** With Theorem A, Z_S = Σ_{k≥0} b^k[L(a+k) − L(a+k−1)] (L(a−1) := 0). All series converge absolutely (polynomial × geometric), so Abel summation is exact: Z_S = (1−b)Σ_k b^k L(a+k) = E[L(a+N)] with P(N=k) = (1−b)b^k, i.e. **Z_S = 2M₂(a) − 4η²**, and identically **N_S = (2/3)M₄(a) − 4M₂(a)η² + (16/3)M₁(a)η³ − (8/3)η⁴**, M_j(g) := E(g+N)^j — candidate (5). Raw moments of N: from memorylessness P(N=k) = bP(N=k−1) one gets E N^j = m Σ_{i<j} C(j,i) E N^i, whence E N = m, E N² = m+2m², E N³ = m+6m²+6m³, E N⁴ = m+14m²+36m³+24m⁴ (polynomial identities verified at 7 values of m, plus exact partial sums with a rigorous tail bound at m = 1/63). These give exactly the M₂, M₄ of candidate (6).

**Exact cost.** With the rationals of (1):
Z_S = 67325211993630408409001/198450000000000000000000, N_S = 4355768046089487574226880288026708390699272667/78764805000000000000000000000000000000000000000,
**J(P_S) = N_S/Z_S = 4355768046089487574226880288026708390699272667 / 26721376640271909097532496900000000000000000000 ≈ 0.163006873**, identical to candidate (9). An independent direct layer sum (81 explicit octagon layers by polygon integration, no Abel step, plus a rigorous tail bound < 2·32⁻⁸¹) agrees with the closed form (controls 6).

**Verdict for moment/cost: no defect (PASS).** Every layer is included exactly; no truncation.

## 5. The centered diamond staircase family — reconstruction of (6)–(8)

For core γD (γ ≥ 0) the shells are {γ+k−1 < ‖x‖₁ ≤ γ+k}; the same Abel summation gives Z_γ = 2M₂(γ), N_γ = (2/3)M₄(γ), so **J(P_γ) = M₄(γ)/(3M₂(γ))** — candidate (6) — for every γ ≥ 0, not only [0,1].

**Derivative.** J′ = (M₄′M₂ − M₄M₂′)/(3M₂²). Expanding with the coefficients c₂ = m+2m², c₃ = m+6m²+6m³, c₄ = m+14m²+36m³+24m⁴:
M₄′M₂ − M₄M₂′ = 2g⁵ + 10m g⁴ + (4c₂+16m²)g³ + (24mc₂−4c₃)g² + (12c₂²−2c₄)g + (4c₂c₃−2mc₄),
and substituting: 2c₂+8m² = 2m+12m², 12mc₂−2c₃ = 12m³−2m, 6c₂²−c₄ = −m(1+8m+12m²) = −m(1+2m)(1+6m), 2c₂c₃−mc₄ = m²(1+2m). So sign J′ = sign P_m with
**P_m(g) = g⁵ + 5m g⁴ + (2m+12m²)g³ + (12m³−2m)g² − m(1+2m)(1+6m)g + m²(1+2m)** — candidate (7), reproduced by exact polynomial arithmetic at m = 1/63 and 7 further m values.

**Sign/root classification at m = 1/63.** Coefficients (descending) are +, +, +, −, −, + (12m³−2m = 2m(6m²−1) < 0): exactly two sign changes, no zero coefficient, so Descartes allows 0 or 2 positive roots with multiplicity. Exact evaluation: P_m(0) = 65/250047 > 0; P_m(a) < 0 (≈ −2.38·10⁻¹²); P_m(z) > 0 (≈ +6.62·10⁻¹²); P_m(1) = 266240/250047 > 0. Hence roots r₁ ∈ (0,a) and g_* ∈ (a,z) exist, are the only positive roots, and are simple. Therefore P_m > 0 on [0,r₁), < 0 on (r₁,g_*), > 0 on (g_*,∞): J is strictly increasing on [0,r₁], strictly decreasing on [r₁,g_*], strictly increasing on [g_*,∞). (Bisection locates r₁ ≈ 0.0141449; P_m > 0 at 1000 sample points of (z,5].)

**Global minimum.** The candidates for the minimum on [0,1] are the endpoint 0 and g_*. P_0 = P_1 as laws (index shift by one, uniform factor 1/b), and exactly M₄(0)M₂(1) = M₄(1)M₂(0), so J(0) = J(1) ≈ 0.39783; since 1 > g_* and J is strictly increasing on [g_*,1], J(1) > J(g_*). Hence **min_{[0,1]} J(P_γ) = J(g_*)**, and in fact min over all γ ≥ 0 is J(g_*) (reviewer observation: the obstruction also covers staircases with cores larger than D; the candidate does not need or claim this).

**Rational enclosure (8).** M₂, M₄ have positive coefficients, hence are strictly increasing on g ≥ 0; a < g_* < z gives M₄(g_*) > M₄(a) and M₂(g_*) < M₂(z), so J(g_*) > M₄(a)/(3M₂(z)) (strictly). Verified M₄(a) < M₄(z), M₂(a) < M₂(z). J(a) ≈ J(z) ≈ 0.163008828.

**Verdict for the staircase derivative/root/minimum argument: no defect (PASS).** The author's Descartes/endpoint argument is complete once P_0 = P_1 is used to dismiss the endpoint local minimum, which the candidate does.

## 6. The gap (10) — mandatory correction checked, every-staircase strict gap

Exact recomputation (control 8):
LB := M₄(a)/(3M₂(z)) − J(P_S) = **55892104628095766169604064637687395172793197064705238995982813 / 28589579218686463271455054512504719394059809867200000000000000000000** (in lowest terms, gcd = 1) ≈ 1.95498·10⁻⁶ > 10⁻⁶.

This equals the parent correction's `correct_gap_numerator/correct_gap_denominator` exactly. The candidate's printed denominator in Eq.(10) (62 digits) is exactly 10⁶ times too small (68-digit corrected value ÷ printed = 10⁶ verified), so the printed value ≈ 1.955 would exceed J(P_S) itself ≈ 0.163 — an impossible "gap" and a pure transcription defect in the display; the numerator and the inequality ">1/1000000" are unaffected. Classification: **MAJOR transcription defect in the printed Eq.(10), fully repaired by the mandatory parent overlay; the overlay's fraction is independently confirmed.** The candidate's own text already states (10) is a lower bound, not the exact gap; the true family gap J(g_*) − J(P_S) lies in [LB, UB] with UB := M₄(z)/(3M₂(a)) − J(P_S) ≈ 1.95513·10⁻⁶.

Sensitivity controls: the author-reported failed coarse bracket [37617/100000, 37618/100000] indeed yields a NEGATIVE outward gap (≈ −5.57·10⁻⁶), and the adjacent 10⁻¹⁰ cell (a−10⁻¹⁰, a) has no sign change — so the enclosure is not an artefact of a loose bracket. Sampled J(P_{i/97}) > J(P_S)+10⁻⁶ for i = 0..97.

**Chain for claim (2):** for every γ ∈ [0,1] (indeed every γ ≥ 0), J(P_γ) ≥ J(g_*) > M₄(a)/(3M₂(z)) = J(P_S) + LB > J(P_S) + 10⁻⁶. **Verdict for the every-staircase strict gap: PASS with the mandatory correction preserved.** Consequently no member of the centered diamond staircase family P_γ can be an all-law J-minimiser at ε = ln 64 in the registered model.

## 7. The optional all-radial strengthening — NOT ADMITTED (conditional, unverified)

The MDA26 parent file named in the candidate's §1 was not supplied by the manifest and was not read. What this review does verify is only the elementary identity used in the extension: for any density depending on ‖x‖₁ alone, J = (2/3)W with W = E‖X‖₁² (in ℓ₁-polar coordinates x = r(t,1−t) the Jacobian is r and ∫₀¹(t²+(1−t)²)dt = 2/3; consistent with ∫_{RD}‖x‖₂² = (2/3)R⁴ vs ∫_{RD}‖x‖₁² = R⁴; control 9). What it does NOT verify: that the W-minimiser over the full-D class is a centered diamond staircase (the MDA26 premise). Hence "P_S beats every ℓ₁-radial full-D-private law" remains a **conditional nonclaim: INCONCLUSIVE / NOT ADMITTED here**, exactly as the candidate labels it. If that premise were valid, the logic W(Q) ≥ min_γ W(P_γ) = (3/2)J(g_*) ⇒ J(Q) ≥ J(g_*) > J(P_S)+10⁻⁶ would be sound, but no such status is granted by this review.

No all-law optimum, no identification of the true nonradial optimiser, no novelty or priority is claimed by the candidate for (2), and none is granted here.

## 8. Controls actually run (receipts)

Script `proof-controls-v2.py` (SHA above), pure `fractions.Fraction`, authored by this reviewer; receipt `proof-controls-v2-receipt.json`, clock `2026-10-29T04:23:09Z`–`04:23:10Z`, **115 checks, 0 failures**. Positive controls: raw-moment identities (7 values of m + partial sums with tail bound), polygon formulas on unit square/triangle, octagon/diamond/cap areas and second moments at 7 radii, exact Minkowski hulls S+kD = T_{a+k} for k ∈ {0,1,2,3,7,10}, distance-index = hull-index on 80 boundary points (vertices and edge midpoints of T_{a+k}, k ≤ 4) and 4000 random rationals in [−8,8]², vertex index k and just-outside index k+1, non-radiality witness, privacy index |Δn| ≤ 1 on 30 000 random (x,h) with 30 % of h on ∂D (deltas seen exactly {−1,0,1}) and on 800 structured boundary pairs, J(P_S) = (9), direct 81-layer sum = closed form, quintic identity at 8 values of m, exact signs of P_m at 0,a,z,1, Descartes count 2, J(0) = J(1), P_m > 0 on 1000 points of (z,5], LB = corrected fraction, lowest terms, LB > 10⁻⁶, LB < UB, monotonicity inequalities, 98 sampled γ. Negative controls (each detected): (3) fails for 2η > a with witness (11/10,1/5); a shift with ‖h‖₁ = 2 moves the index by 2; a deliberately wrong half-width-shell law violates |Δn| ≤ 1 inside D; the printed Eq.(10) value exceeds J(P_S); the author's coarse bracket gives a negative outward gap; the adjacent 10⁻¹⁰ cell has no sign change.

Honest record of the first run: `proof-controls-v1.py` reported **1 FAIL** in "4.dist_index_equals_hull_index_on_boundary_and_random". Diagnosis (separate stdin snippet, no file written): all 204 mismatches were random points with shell index ≥ 14, for which my hull table (built only for k ≤ 13 while the sample box allows ‖x‖₁ ≤ 16) returned `None`; every mismatch had `n_hull = None` and index > 13. This was a range defect in the reviewer's checker, not a discrepancy in the candidate; v2 differs from v1 only by the header comment, the hull range 14 → 18, and the receipt filename. The v1 files are preserved unedited.

## 9. Verdicts at exact scopes

| scope | verdict | severity |
|---|---|---|
| P_S is a Borel law with ε = ln 64 privacy for every Borel event and every shift in the full closed D (Theorem B) | **PASS** | none |
| Clipped-core geometry S+kD = T_{a+k} for every integer k ≥ 0, all signs/boundaries (Theorem A; candidate (3)) | **PASS** | MINOR (presentation only; proof correct; hypothesis 2η ≤ a sharp and satisfied) |
| Cap/octagon areas and ℓ₂² moments (4), exact infinite geometric shell sums (5), exact cost (9) | **PASS** | none |
| Staircase cost (6), derivative quintic (7), Descartes/endpoint global minimum at g_* ∈ (a,z), enclosure (8) | **PASS** | none |
| Printed fraction in Eq.(10) | **DEFECT as printed — repaired by mandatory overlay**; corrected fraction independently reproduced in lowest terms | MAJOR transcription (display only) |
| Strict gap > 10⁻⁶ below EVERY centered diamond staircase P_γ, γ ∈ [0,1] (claim (2)) | **PASS** (with correction preserved); also holds for all γ ≥ 0 | none |
| All-ℓ₁-radial strengthening via MDA26 | **NOT ADMITTED / INCONCLUSIVE** — premise unsupplied and unread; only the J = (2/3)W identity verified | conditional nonclaim preserved |
| Any all-law optimum, true optimiser identification, novelty, priority | **not claimed; not granted** | — |

**Exact dependencies of the unconditional result (2):** the registered model definitions (input 3), the elementary geometry/analysis reproduced in §§2–5 of this review, and exact rational arithmetic with the parameters of (1) — plus the mandatory numeric correction for the display of (10). No dependence on LAW642, v241, v253, MDA26, or any earlier unreviewed theorem.

## 10. Limits

Same-harness review by a sibling agent: this is **not** human review, not an independent-model-family review, not a formal/kernel verification, and not a novelty or priority check. Exactness claims rest on `fractions.Fraction` arithmetic in CPython 3.14.3 as recorded in the receipts; the proofs in §§2–5 are written mathematics checked by this reviewer only.
