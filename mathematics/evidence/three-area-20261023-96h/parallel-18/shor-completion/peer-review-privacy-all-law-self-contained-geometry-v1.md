# Peer review v84-A — all-Borel diamond MSE: self-contained geometry, calibration and uniqueness

**Reviewer.** Owner MathShor (runtime MathShor-2).

**Clock.** The last actual `/bin/date` before composing this review returned `Sun Oct 25 12:42:11 PDT 2026`. This is an earlier-observation bound.

**Pins.**

| Item | Identifier | SHA-256 |
|---|---|---|
| Assignment | `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v84.json`, entry v84-A, read raw LF1–142 | `56d5b0aa02c5e9920dc22e3cbd0170040ef0bd2b994e0322be7d6565b796af6a` |
| Receipt | `peer-review-wave-eighteen-v84-packet-receipt-v1.json`, read raw LF1–42 | `9769fc89ced5bf2d01f05803cb2bde93c92a3b9bd85710247dc2b5ab1c63ed32` |
| Exposure ACK | `peer-review-privacy-all-law-self-contained-geometry-ack-v1.json`, written 12:25:10 before any proof body | `7e7a22aa998cbe09e4035c6829e54e3c04b0af610b1347bd5fb9e8230a332926` |
| Own Shor primary checkpoint | `primary-continuation-20261025-102319-checkpoint-05-v1.json`, written 12:24:01 before the review | — |

**Mandatory order.** I read v9 first (b7c92143…, raw 1–35), then v10 (d61acbf7…, raw 1–31), then v11 (3ce29e3c…, raw 1–40). After that came the manifest entry, the receipt, the ACK, and finally the part.

**Character of this review.** Same-harness, same-family, cross-domain SERIAL written reconstruction.
- I previously reviewed three older privacy packets: the peak envelope, the entire one-core comparison and the OUTER1 tail calibration. Their pins are in the ACK.
- This author previously reviewed my Shor interface.
- S4 is new to me. I did not read the v84-B review or any other review of S4.

This review is NOT blind, cross-vendor, human, formal, kernel, executable or novelty acceptance.

## 0. Verdict

| Scope | Result |
|---|---|
| S4, the ENTIRE 642-LF self-contained proof (§§0–10), at its stated classical imports | **0 FATAL / 0 MAJOR / 0 MINOR.** Every model-specific step was reconstructed in writing (§§2–11 below), including all hostile-emphasis items of the scope. |
| Additional hidden premises | None beyond the classical facts listed in §12, which are elementary or covered by S4 §0 named imports. |
| S5 (parent disposition) | CONTEXT only. Its algebraic-nature claims are NOT part of S4's theorem and are NOT reconstructed here: minimal quintic, transition cubic 2592v³+864v²+18v−1, the S5/nonradical example, transcendence. |
| S6 (source refresh) | CONTEXT only. Not a correctness premise, and no priority or novelty conclusion. |

**Supported statement (WRITTEN, at the named classical imports).** Fix any finite ε > 0, and let b = e^{−ε}. Consider every Borel probability law μ on R² with μ(E) ≤ b^{−1}μ(E+h) for every Borel set E and every h in the CLOSED unit l1 diamond D. Among these there is exactly ONE law minimizing ∫|z|₂² dμ. Its density is Z_*^{−1}b^{n_*(z)}, where n_*(z) = min{k ≥ 0 : z ∈ S_* + kD}, and

S_* = {|z|₁ ≤ 2t_*, |z|² + 2m|z|_∞ + T2 ≤ λ_*},

with t_* > 0, λ_* = V, T2 < λ_* < λP, λ_* ≤ 4/ε², and terminal facet width d ∈ (0, 1/2). The parameters are fixed by the globally screened D/R scalar systems.

## 1. Coverage

The single part `peer-review-wave-v84-v84-A-part1-v1.md` (SHA-256 `8478beeb…ea83`, 71,385 bytes, 880 LF) was read raw at LF1–130, 131–260, 261–380, 381–500, 501–620, 621–740 and 741–880, ending included (S6|76 `}`). No displayed line was cut.

Source coverage: S1–S3 complete, S4 LF1–642 complete, S5 LF1–23, S6 LF1–76.

## 2. Model constants (S4 §1)

Let G be geometric with P(G=k) = (1−b)b^k and m = b/(1−b).
- The identity E C(G,j) = (1−b)b^j/(1−b)^{j+1} = m^j holds.
- Stirling expansion then gives T2 = EG², T3 = EG³ and T4 = EG⁴, exactly as printed.
- λP = T4/(3T2): polynomial division of 24m³+36m²+14m+1 by 2m+1 gives 12m²+12m+1, so λP = 4m²+4m+1/3. ✓
- v = T2 − m² = m + m² ✓.

## 3. All-law foundations (S4 §2)

**Absolute continuity.** Take N Lebesgue-null. By Tonelli, ∫_D μ(N+h)dh = ∫|(x−N)∩D| dμ(x) = 0. Privacy then gives 2μ(N) ≤ b^{−1}·0. So μ has a density p (RN). ✓

**Finite cap.** The set inequality gives p(x) ≤ b^{−1}p(x+h) a.e. for each fixed h. The set of failing (x,h) is Borel, with every h-section null, so by Fubini, for a.e. x the inequality p(x+h) ≥ bp(x) holds for a.e. h ∈ D. Integrating, 2b·p(x) ≤ ∫_{x+D}p ≤ 1. So M = ess sup p ≤ 1/(2b). No maximum is assumed. ✓

**Positivity.** Suppose A ⊆ {p=0} is bounded with |A| > 0.
- With −h ∈ D, μ(A+h) ≤ b^{−1}μ(A) = 0, and iterating covers every t ∈ jD, hence every t ∈ R².
- But ∫μ(A+t)dt = |A| > 0, a contradiction. ✓

**Attainment.** The product Laplace law is feasible: its density ratio is e^{ε(|x+h|₁−|x|₁)} ≤ 1/b. Its cost is 2·(2/ε²) = 4/ε² = U.
- Any sequence with cost ≤ U+1 is tight by Markov; Prokhorov gives a weak limit.
- For FIXED h and φ ∈ C_c⁺, ∫φdμ_j ≤ b^{−1}∫φ(·−h)dμ_j passes to the limit along the same subsequence. Radon order then gives all Borel E, for each h separately.
- Lower semicontinuity comes from truncating |x|².
- V > 0, since δ₀ is not absolutely continuous. ✓

**Phases.** Let a ∈ [bM, M), n_a = min{k : p > ab^k}, r_a = b^{n_a}.
- If n_a = k ≥ 1, then ab^k < p ≤ ab^{k−1}, so bp/a ≤ r_a < p/a.
- If n_a = 0, then r_a = 1 < p/a, and bp/a ≤ bM/a ≤ 1.
- Hence b/a ≤ Z_a ≤ 1/a, and J(q_a) ≤ J(p)/b.

Feasibility of each phase: the fixed-h null set does not depend on a or k, and p(x) > ab^k implies p(x+h) ≥ bp(x) > ab^{k+1}. So |n_a(x+h) − n_a(x)| ≤ 1 a.e. for each h, which gives measure privacy. ✓

**Layer identity and mixture (PH).** r_a = (1−b)Σ_k b^k 1_{p>ab^k} holds: the sum telescopes from k = n_a. Substituting u = ab^k maps [bM, M) onto [b^{k+1}M, b^kM), so (1−b)^{−1}∫r_a da = ∫₀^M 1_{p>u}du = p.

By Tonelli, the weights Z_a/(1−b)da form a probability measure and give the cost mixture (PH). Every J(q_a) ≥ V while the average is V. So the COST-defined set G = {a : J(q_a) = V} is measurable (Tonelli) and has full weight, hence full Lebesgue measure. Each phase has top plateau {p > a} of positive area. ✓

## 4. Same-law closed levels (S4 §3)

Let q = αb^n be ANY original optimal geometric density with a positive-area plateau. Put E_i = {n ≤ i}, and K_i = the support of 1_{E_i}dx.

**Compactness.** For a.e. x, J ≥ bq(x)∫_D|x+h|²dh. Here ∫_D h₁² = ∫_{−1}^{1}h²·2(1−|h|)dh = 1/3, so the integral equals 2|x|² + 2/3. On E_i this gives |x|² ≤ J/(2αb^{i+1}). So each K_i is compact, nonempty and nested, with E_i ⊆ K_i a.e. ✓

**FWD.** For each h, (E_i+h) ⊆ E_{i+1} a.e. Supports are monotone under a.e. inclusion, and the support of E_i+h is K_i+h. Hence K_i + D ⊆ K_{i+1}. This is a statement about closed sets, made separately for each h. ✓

**FILL.**
- If (1_{E_i}∗1_D)(y) > 0, then for a.e. such y a positive-measure set of h has y−h ∈ E_i, so q(y) ≥ bαb^i.
- For y ∈ K_i + int D, the set y−D contains a ball around a support point, so the convolution is positive.
- Level-nullity: the l1 distance d to K is 1-Lipschitz. Off K, with a nearest point z and u = (x−z)/d(x), we get d(x−tu) = d(x)−t from both inequalities. So ∇d·u = 1 and ‖∇d‖_∞ = 1.
- At a density point of {d=r}, differentiability forces ∇d = 0: a nonzero gradient confines the level set to o(δ)-slabs. By Rademacher and Lebesgue density, |{d=r}| = 0 for r > 0.
- Since K+D = {d≤1} and K+int D = {d<1}, this gives K_i + D ⊆ E_{i+1} a.e. ✓

**Lowering and SAND.** Lower q by the factor b on U = (E_{i+1}∖E_i)∖(K_i+D) ∩ {|x|² > J}.
- A changed point x (index i+1 → i+2) cannot have a neighbor y = x+h of index ≤ i. Otherwise y ∈ E_i, so y ∈ K_i off the translated null set E_i∖K_i, and then x ∈ K_i+D.
- So the neighbor indices lie in {i+1, i+2}, and reverse and both-changed pairs follow.
- The mass z′ ≥ b, and the normalized change is −(1−b)∫_U(|x|²−J)q/z′, which is strictly negative when |U| > 0.
- Hence K_{i+1} ⊆ (K_i+D) ∪ B̄_{√J}, and K_0 ⊆ B̄_{√J} by lowering the top set. ✓

**Same-law representative.**
- Define m(x) = min{i : x ∈ K_i} and q̂ = αb^m. Using ±h, q̂ is pointwise private for every x and every h ∈ D, and q̂ ≥ q a.e.
- The holes lie a.e. in B̄_{√J}. The normalized change is ∫(|x|²−J)ρ/(1+∫ρ), which is strictly negative unless ρ = 0, because the circle is null.
- So q̂ = q as laws. Each hole is null, since ρ ≥ αb^i(1−b) on a level-i hole. Hence K_i = supp(K_i). No averaging or symmetry was used. ✓

## 5. Four separate strict Steiner equalities and CAN (S4 §4)

**Steiner symmetrization S_e** in the axis and diagonal directions. D has centered interval fibers in each.
- By reverse Fatou, closedness gives limsup 1_{A_{s_k}} ≤ 1_{A_s}, so fiber length is upper semicontinuous and S_eA is compact.
- Area and inclusion are preserved.

**1D lemma.** |E+[−d,d]| = |E| + 2d + Σ_gaps min(L, 2d). To see this, write the span as |E| + ΣL and note that each gap loses max(L−2d, 0). Hence ℓ_{A+D}(s+σ)/2 ≥ ℓ_A(s)/2 + w(σ) ≥ |u| + |τ|, which gives S_eA + D ⊆ S_e(A+D). ✓

**Moment.** ∫(u² − (l/2)²)(1_E − 1_I) ≥ 0 pointwise. So the centered interval uniquely minimizes the along-fiber moment, while the perpendicular moment is preserved. ✓

**One direction, whole sequence.** Put K′_i = S_eK_i.
- Nesting holds, K′_i + D ⊆ S_e(K_i+D) ⊆ K′_{i+1}, and the levels cover the plane.
- So αb^{m′} is pointwise private.
- Mass is α(1−b)Σb^i|K′_i| = 1 by summation by parts.
- The moment satisfies α(1−b)Σb^iM(K′_i) ≤ V. Optimality forces equality.
- Every deficit has POSITIVE weight α(1−b)b^i, so K_i = S_eK_i a.e. for EVERY i.
- This is repeated separately for each of the four directions on the ORIGINAL levels, with no sequential replacement and no averaged optimum. ✓

**Exact upgrade.** Let x ∈ K_i and suppose its reflection or contraction image Lx is not in K_i. The closed complement gives an open ball B ∋ Lx; then L^{−1}B ∩ K_i has positive area (because K_i = supp K_i), while B ∩ K_i = ∅. That contradicts the a.e. identity, which transports under the invertible linear L. Contraction λ → 0 follows by closedness. ✓

**CAN.**
- The four reflections generate D4.
- Axis contractions give order ideals.
- Diagonal contraction plus swap gives the whole segment from (x,y) to (y,x).
- Positive area gives a point off both axes, hence a box and t_i > 0.

The CAN properties follow:
- Midpoints give |z|₁ ≤ 2t_i.
- Contraction of (t_i,t_i) gives F_i ≥ t_i.
- F_i(t_i) = t_i, and monotonicity holds.
- The segment point (F(y₁)+y₁−y₂, y₂) gives the 1-Lipschitz bound, using y₂ ≤ t_i ≤ F(y₁).
- No first-octant points exist with y > t_i, and each fiber is [y, F_i(y)].

Convexity is neither assumed nor obtained at this stage. ✓

**PAR, for any t ≥ 0, any CAN F and real r ≥ 0.**
- Reflect and sort the source. The sorting step uses that u ↦ |x−u| − |y−u| is nonincreasing for x ≥ y.
- Then x ≤ F(u) + r − |y−u|, which is at most F(y)+r for y ≤ t (Lipschitz) and at most 2t+r−y for y ≥ t (since F(u)+u ≤ 2t).
- Attainment and filling: horizontal shifts give the first cap. For the second cap, (t,t) + (x′−t, y−t) has l1 norm x′+y−2t ≤ r.
- For t = 0 this is rD. ✓

**MOM.** The octant area is A0/8 + rt + r²/4. For the moment:
- The strip contributes M0/8 + r∫(F²+y²) + r²∫F + r³t/3.
- The half-triangle contributes ∫₀^r(t+a)²(r−a)da = t²r²/2 + tr³/3 + r⁴/12.
- Multiplying by 8 gives MOM exactly. ✓

## 6. Erosion, original-optimality cap raising, IDX (S4 §5)

**(ER).** CAN bodies are order ideals in (max, sum): a sorted point with v > y lies below (x+y−v, v) on the swap segment. Every point of (x,y)+D has max ≤ x+1 and sum ≤ x+y+1, so it is dominated by (x+1, y). ✓

**Cap raising.** FWD/PAR give t_{i+1} ≥ t_i + 1/2 and F_{i+1} ≥ F_i + 1. Suppose there is a strict gap at some y.
1. Continuity gives an interior height and a point w ∈ K_{i+1}∖(K_i+D). SAND puts w in B̄_{√J}.
2. Let z = w − (1,0). Then z ∉ K_i (since z_x > F_i(y)), z ∈ K_{i+1}, and z+D ⊆ K_{i+1} by ER.
3. |z|² < |w|² ≤ J because w_x > 1.
4. Open margins give an open U of positive area, with index i+1, inside the open ball.
5. Raise q to αb^i on U.
   - For a raised u, every neighbor v satisfies v ∈ K_{i+1}, so n′(v) ≤ i+1. Also n(v) ≥ i, otherwise u ∈ K_{i−1}+D ⊆ K_i.
   - For an unchanged u′ next to a raised point, u′ ∈ K_{i+1}.
   - So pointwise privacy holds BEFORE normalization.
6. The normalized change ∫_U(|z|²−J)ρ/(1+∫ρ) is strictly negative, a contradiction.

This uses ORIGINAL optimality only, before W is introduced. Hence CAP holds. ✓

**IDX and g.**
- f = F_i − i is well defined by CAP, nonincreasing and 1-Lipschitz on [0,∞), since t_i ≥ t₀ + i/2.
- h(y) = y − f(y) is strictly increasing with h(t_i) = i.
- If x − f(y) ≤ i then h(y) ≤ i, so y ≤ t_i. Hence (x,y) ∈ K_i iff x − f(y) ≤ i, and n = max(0, ⌈x−f(y)⌉). The birth domain is retained. ✓
- g = y − f on [t,∞) satisfies g(t) = 0 and g′ = 1 − f′ ∈ [1,2].
- The one-core law has f = F₀ below t and 2t−y above, so g₀ = 2(y−t). ✓

## 7. The entire canonical class (S4 §6)

- Membership in S+kD+D = S+(k+1)D gives pointwise feasibility, so V ≤ W. ✓
- Layer cake: Z = A0 + 8tEG + 2EG² and N = M0 + 8m∫(F²+y²) + T2(8∫F + 4t²) + (16/3)tT3 + (2/3)T4. This is exactly ZN.
- The point core has cost T4/(3T2) = λP, so W ≤ λP.
- Only the definition and this ceiling are used in the lower bound. ✓

## 8. Signed inverse-birth lower bound (S4 §7)

**A_k formula.** On z ∈ (γ+ℓ−1, γ+ℓ] the integrand carries b^{j+ℓ}. Summation by parts gives A_k = b^jE(γ+G)^{k+1}/(k+1), with derivatives −b^jE(γ+G)^k inside a phase.

**Continuity at phase boundaries.** Continuity at integer s is equivalent to E(G+1)^r = T_r/b, which holds by the shift l′ = l+1 for r ≥ 1. So no jump measure appears. ✓

**(IB1).** In octant rows y ≥ t the index is ⌈z + g(y)⌉ with z = x − y, and the cost is 2y²+2yz+z². So the row integral is R(g(y), y). Substituting y = Y(s), with Jacobian Y′ (not g′), gives IB1.

**Inverse bounds.** The AC inverse theorem gives 1/2 ≤ Y′ ≤ 1. So 0 ≤ δ′ ≤ 1/2 and 0 ≤ δ ≤ s/2. ✓

**Integration by parts.**
- Q_y = R ✓ and Q_s = −b^jΦ phasewise ✓.
- Q(s, Y(s)) is AC across continuous phase boundaries and tends to 0, since A_k ≤ Cb^s and Y ≤ t+s.
- Hence I[Y] = −Q(0,t) + ∫b^{⌈s⌉}Φ. ✓

**Cubic increment.**

Φ(Y₀+δ) − Φ(Y₀) = δW₀ + δ²(2Y₀+γ+m) + (2/3)δ³,

where W₀ = 2Y₀² + 2(γ+m)Y₀ + c₁.

Signed Fubini applies to ∫b^{⌈s⌉}W₀∫₀^sδ′: its absolute bound is C∫s(1+s)²b^s < ∞. W₀ is not assumed pointwise nonnegative. (IB2) ✓

**(IB3).**
- Partial phase: with Y₀ = τ − η/2, W₀ = A(τ) + mη + η²/2, whose integral is A(τ)γ + mγ²/2 + γ³/6.
- Later phases: A(τ+ℓ/2) = A(τ) + (2τ+m)ℓ + ℓ²/2. The sums are Σb^ℓ = m, Σℓb^ℓ = m(1+m) and Σℓ²b^ℓ = b(1+b)/(1−b)³ = m(1+m)(1+2m).
- The bracket collapses to 2τ² + 2(1+2m)τ + 4m² + 4m + 2/3 − λ = Cdiag − λ.
- Hence T = b^jK. ✓

**K monotonicity.** ∂_τK = m(4τ+2+4m) + (4τ+2m)γ > 0 and ∂_λK = −(m+γ) < 0. With τ ≥ 1/2 and λ ≤ λP:
- Cdiag(1/2) − λP = 2m + 11/6.
- A(1/2) at λP equals 1/6 − 2m − 2m².
- So K(1/2,γ;λP) = 2m²(1−γ) + m(11/6 − 2γ + γ²/2) + (γ+γ³)/6.
- The middle quadratic decreases on [0,1] to 1/3. So K ≥ m/3 > 0 and T(u) ≥ b^{⌈u⌉}m/3 > 0.

**(IB4).** All IB2 terms are nonnegative. If δ ≢ 0, then δ′ > 0 on a set of positive measure, so the inequality is strict. ✓

**(LB).** Rows y ≤ t agree, by IDX with f = F₀ and the PAR profile F₀+k. The tail rows give I[Y] versus I[Y₀], over 8 D4-octants with null boundaries. Hence

N_o − WZ_o = Z_S(J_S − W) + 8(I[Y] − I[Y₀]).

Here J_S ≥ W holds by DEFINITION (K₀ is a CAN core), and λ = W ≤ λP is admissible. So V ≥ W, and therefore V = W. No one-core premise, Hfast, tail-A or root is used.

**(EQ).** At equality, δ ≡ 0, so g = g₀ and K_i = K₀ + iD, and K₀ attains W. ✓

## 9. Entire-class CAL (S4 §8)

**CLIP.**
- With ψ(F,y) = T2F + mF² + my² + F³/3 + y²F − 4y³/3 − λF + λy, we have H = const + 8∫₀^tψ(F(y),y)dy.
- ψ_F = (F+m)² − (λ−v−y²) and ψ_FF = 2(F+m) > 0, so H is minimized pointwise over t ≤ F ≤ 2t−y.
- CLIP lies in CAN:
  - R is nonincreasing, with slope y/(R+m) ≤ y/(t+m) ≤ 1 where R > t;
  - max(t, ·) and min(2t−y, ·) preserve monotonicity and 1-Lipschitz;
  - at y = t the value is t.
- So this is the strict fixed-t minimization over the WHOLE class, including nonconvex profiles. ✓

**Attainment.**
- Every core contains [−t,t]², so N ≥ 8t⁴/3. Also Z ≤ 8t² + 8tm + 2T2.
- For t ≥ max(m, √T2) the cost is ≥ 4t²/27. So any core of cost ≤ λP has t < A−1.
- H at CLIP is continuous on [0,A]; as t → 0, Z → 2T2 and N → (2/3)T4.
- Since Z ≥ 2T2, min_tH is strictly decreasing in λ, by at least 2T2·h for an increase h.
- min_tH(0) ≥ (2/3)T4 > 0, because N ≥ (2/3)T4: on [0,t], F³/3 + y²F − 4y³/3 ≥ 0 since F ≥ y.
- The point core gives 0 at λP.
- So the unique zero is W, attained by an actual core. ✓

**The value interval.**

| Claim | Reason |
|---|---|
| J_D(γ) = (1/3)E(G+γ)⁴/E(G+γ)² | γD has levels (γ+k)D, with Moment(cD) = (2/3)c⁴ and Area = 2c² |
| J_D′(1) > 0 | Its sign is that of 2E(G+1)²E(G+1)³ − E(G+1)⁴E(G+1) = (2T2T3 − mT4)/b² = m²(1+2m)/b² > 0 (verified by expansion) |
| W < λP and t_* > 0 | From the line above |
| W > T2 | For λ ≤ T2, R ≤ √(λ−v) − m ≤ 0, so CLIP is F = t. At λ = T2, H is the printed sextic with constant (2/3)(T4 − 3T2²) > 0 (T4 − 3T2² = m + 11m² + 24m³ + 12m⁴) and linear coefficient 16m/3 + 24m² + 16m³ > 0; all coefficients are positive. |
| W ≤ 4/ε² | The Laplace phases are cores γD with γ = log_b(a/M) ∈ (0,1], and their exact (PH) average cost is 4/ε² |

**(HT) envelope derivative.**
- The endpoint term ψ(t,t) = T2t + 2mt² contributes 8T2t + 16mt².
- ∂_tF equals 1 on the lower clip, 2 on the upper clip and 0 on the arc.
- Switching points are finitely many algebraic roots, and ψ_F vanishes at R. So H is C¹ with matching one-sided derivatives. ✓

**No lower clip.**
- R + y increases where R + m > y, so lower and upper clips exclude each other.
- If λ ≤ 2t² + 2mt + T2, the base of HT is ≥ (16/3)T3 − 8mT2 + 16tv > 0, and the lower integrand is ψ_F(t,y) > 0.
- So H_t > 0 in that regime. The interior minimizer t_* (with t_* < A−1) has H_t = 0. Hence W > 2t_*² + 2mt_* + T2.
- S_* = {|z|₁ ≤ 2t_*, |z|² + 2m|z|_∞ + T2 ≤ W}. It is convex as a conclusion, and lies strictly inside |z|² < W. ✓

**Global uniqueness.** Regimes: diamond [0, t_D], rounded (t_D, t_U), lower [t_U, ∞). Moreover t_D < t_U, because 2t_D² + 2mt_D + T2 = (λ+T2)/2 < λ.

*Diamond regime.*
- DC: E(G+q)³ = x³ + 3vx + c3 with x = 2t+m and c3 = m + 3m² + 2m³. This cubic is strictly convex.
- DC(0) = (2/3)T3 − λm > 0 even at λP, by the 2T2T3 − mT4 identity.

*Rounded regime.*
- The junction is λ = 2t² + 2d² + 2m(t+d) + T2.
- The upper integrand is 2(u²−d²) + 2m(u−d), with integral −4d³/3 − md².
- Then H_t/16 = C0 + tv − P(d), with C0 = m/3 + (3/2)m² + m³.
- d′ = −(2t+m)/(2d+m), so H_tt = 16[v + (2d+m)(2t+m)] > 0.

*Conclusion.* There is at most one positive local minimum below H(0,λ) = 2T2(λP − λ) > 0. At λ = W, every minimizer has value 0 and lies in the interior, so it is unique. Strict fixed-t convexity then makes the WHOLE optimal core unique. ✓

**Terminal width d < 1/2.** Suppose d ≥ 1/2, and set t′ = t − 1/2.
- t′ lies on the facet, so F′ = F − 1 satisfies the CAN conditions and PAR gives S = S′ + D exactly.
- Also u_{S′} = (1−b)1_{S′} + bu_S.
- The resulting cost is below W iff the average of |z|² over S′ is < W. This holds because S′ ⊆ S ⊆ {|z|² < W} and |S′| > 0.
- If t′ = 0, then S = D, the point-core law of cost λP > W.

Both cases are actual class competitors, so d ∈ (0, 1/2). ✓

**Screens and primitives.**
- P_m = 2M3M2 − M4M1 was expanded by hand: q⁵ + 5mq⁴ + (2m+12m²)q³ + (12m³−2m)q² − (m+8m²+12m³)q + m² + 2m³. ✓
- H_D′ = (4/(3M2))P_m at λ = M4/(3M2). The diamond screen λ ≥ M2(q) is equivalent to t ≤ t_D.
- R branch:
  - d > 0 forces R(t) > t, since λ − v − t² = (t+m)² + 2d² + 2md. So no lower clip.
  - t(d) > d gives c > 0.
  - Monotonicity of R+y makes [0,c] exactly the arc.
- Free integrand: −(2/3)(A−y²)^{3/2} + mA − m³/3 − (4/3)y³ + λy. ✓ Upper polynomial Uint ✓. J3 is the standard ∫(A−y²)^{3/2} ✓.
- A − c² = (t+d+m)² ✓. Z_* ✓, which reduces to 2M2(2t) at c = 0.
- A screened zero-value stationary point is a local minimum. In the diamond regime a local maximum has value > H(0,λ) > 0; the rounded regime is convex. By the uniqueness above it is the global zero, so λ = W. ✓

## 10. All original Borel laws (S4 §9)

- Any geometric optimum gives EQ, and its core attains W, so by class uniqueness it equals μ_*. The amplitude α = 1/Z_* is forced.
- For ANY original optimum, every phase in the cost-defined full-weight set G is such an optimum. So μ(E) = ∫q_a(E)Z_a/(1−b)da = μ_*(E).
- G is defined by one scalar cost equation. There is no intersection over uncountably many events. ✓

## 11. Hostile-scope checklist

| Item | Status |
|---|---|
| All-law density / a.e. positivity / finite cap / fixed-h null sets / weak-closed attainment | Reconstructed §3 |
| Jointly measurable all-phase mixture with strict thresholds | §3 |
| Any geometric optimum: same-law compact supports, FWD, FILL with distance-level nullity, actual normalized lowering, SAND, cost ball, filling without averaging | §4 |
| Each of the four Steiner directions on ORIGINAL levels separately, with strictly positive weighted deficits and exact regularity upgrades; nonconvex CAN | §5 |
| Full real-offset PAR/MOM; full-diamond erosion; cap raising at ORIGINAL optimality before W | §§5–6 |
| Exact global offset, ceiling, birth domain | §6 |
| Whole canonical class including t = 0 and nonconvex profiles; positive ZN; ceiling | §7 |
| Signed inverse-birth: Jacobian Y′, AC across phase boundaries, signed Fubini integrability, T > 0 for all λ ≤ λP, equality, V ≥ W from the ENTIRE definition | §8 |
| CAL: strict clip, feasibility, compact attainment, λ in (T2, λP), positive core, no lower clip, convexity as conclusion, global uniqueness with matching derivatives, actual d < 1/2 competitor | §9 |
| D/R global screens, normalizer and primitives, with no evaluated roots | §9 |
| Any geometric optimum, then all original laws, from ONE cost-defined good phase set | §10 |

## 12. Imports and hidden premises

The S4 §0 named classical imports actually used:
- RN, and order/regularity of Radon measures (including C_c-test order);
- Tonelli and absolutely integrable signed Fubini;
- Prokhorov and Portmanteau;
- Rademacher and the Lebesgue density theorem;
- the AC inverse function and chain rule;
- dominated differentiation and compactness.

Further facts used are elementary and proved or immediate in the text: Markov's inequality, nearest points on compact sets, reverse Fatou, and the standard antiderivative of (A−y²)^{3/2}. **No additional hidden model-specific premise was found.** The older S/C/X/A/B/CAL bodies, the 578-LF branch arithmetic and the numerical, Galois or transcendence material are not premises of S4. I did not need them, and they are not credited.

## 13. Findings, boundaries and assurance

**FATAL: none. MAJOR: none. MINOR: none.**

Non-defect remarks:
1. S4 §8.1 states the F-derivative and the second derivative 2(F+m) without the common factor 8. This is harmless.
2. The uniqueness count in §8.4 implicitly excludes the endpoint t = A. This is valid because H(A,W) ≥ Z(λP − W) ≥ H(0,W) and the minimizer is interior.

**Boundaries.**
- The result is for the additive query-output-independent channel class with the full closed diamond, squared Euclidean loss and every finite ε.
- It gives no nonadditive or data-dependent theorem and no whole-book solution.
- Numeric brackets, roots or tables are not accepted.
- S5's algebraic-nature claims stay at S5's own named scope and are not reconstructed here.
- S6 is bounded author context with no priority or novelty clearance.

**Assurance.** Same-harness, same-family, serial written reconstruction. It is not configured-family, human, formal, kernel, executable, publication or novelty acceptance. No scientific interpreter, program, enumeration, replay, solver, nested agent, external CLI or GO was used. HOLD v2 and v9/v10/v11 bind. The original cutoff and deadline are unchanged.
