# f121 — Independent same-harness scientific review v1

**Review id:** `f121-privacy-high-privacy-universal-laplace` · **kind:** INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW
**Observed `/bin/date` immediately before this write:** `2026-10-29T03:07:47Z` (`Wed Oct 28 20:07:47 PDT 2026`)
**Reviewer:** in-harness Claude reviewer (same harness as the author). This is NOT human review, NOT an independent model family, NOT formal/kernel verification, and grants NO novelty, priority or parent-adoption status.

## 0. Bindings, order of reading, disclosures

| item | path | pin (verified by `shasum -a 256` / `wc -c` / `wc -l` before reading; re-verified inside the control run) |
|---|---|---|
| manifest | `.../review-waves/f121-privacy-high-privacy-universal-laplace/manifest-v1.json` | SHA256 `ce84a1d3eb9fc071cf31fa05a7263806cb0735a5b9fcf8c6c1a1ef4b7a16194f`, 1781 bytes |
| input 1 (only input, read completely, first) | `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-sharp-high-privacy-universal-limit-v1.md` | SHA256 `8615b71531aee0c55760796aad35dc6cb39002606b64b919017ed7a6e8b647d2`, 8214 bytes, 108 LF — all three pins match the manifest |
| authority (scope only) | `.../three-area-2026-10-27-96h/contract-addendum-2-frontier-first-owner-direction-v1.json` | SHA256 `5e18c2d4b94656fc12b5cfce4122889fa6073e24a21f1e0062c79d846b6037ce`, 3210 bytes |

Read order: manifest → input 1 (whole file, `:raw`) → authority. Disclosures: no prior exposure to this candidate or to any held mathematical payload was used; the candidate contains no code, so nothing authored by the author was executed; no author contact, no web search, no external model/paid API, no Git, no deletion, no publication, no infrastructure change. Artifacts written by this review, all in the review directory and all `reviewer-` prefixed except this file: `reviewer-f121-controls-v1.py`, `reviewer-f121-controls-v1-receipt.json`, `reviewer-f121-controls-v1-receipt.txt`, `review-v1.md`.

## 1. Verdict (scoped over every variable)

**Classification: MINOR — no FATAL, no MAJOR, not INCONCLUSIVE.** Every load-bearing mathematical claim of the candidate was reconstructed independently by the reviewer and found correct within the candidate's declared scope. Three presentational/derivation gaps were found; each is repaired in §3 below without any new hypothesis, and none changes a conclusion.

Exact scope of this verdict (the candidate's own class, nothing wider):

| variable / object | range covered by the verdict |
|---|---|
| ε | every ε > 0 for the finite statements (1)–(4); ε → 0 along arbitrary sequences for (6) and the W2 statements |
| κ = κ(ε) | every nonnegative function of ε, including oscillating and unbounded; α := κε |
| class F_ε | Borel probability laws μ on R² with μ(A) ≤ e^ε μ(A+d) for **every** Borel A and **every** d with ‖d‖₁ ≤ 1 (closed full ℓ¹ diamond, both shift signs by symmetry of D) |
| functionals | J = E‖X‖₂², L = E‖X‖₁; scaled U = E‖Z‖₂², V = E‖Z‖₁ with Z = εX; infinite moments allowed (lower bounds then trivial) |
| limit law | Λ(dz) = ¼ e^{−‖z‖₁} dz on R² |
| metrics | TV = ½‖·‖_{L¹}; W1/W2 for the Euclidean cost (equivalent norms on R² give the same convergence statements) |
| hypothesis (5) | J + κL ≤ [4/ε² + 2κ/ε][1 + o(1)] as ε → 0 for a family μ_ε ∈ F_ε |

Claims and their status under this scope:

| claim | status | exact dependencies used in the reviewer's reconstruction |
|---|---|---|
| (1) J ≥ 2b(1+b)/(1−b)², L ≥ 2b/(1−b) for all μ ∈ F_ε, b = e^{−ε} | correct | only the four vertex shifts ±e₁, ±e₂ and half-line Borel events; layer-cake; exact series identities (control A1) |
| Laplace density (ε²/4)e^{−ε‖x‖₁} ∈ F_ε with J = 4/ε², L = 2/ε | correct | reverse triangle inequality for ‖·‖₁ (control F1); Laplace moments |
| (2)–(4) with a universal relative O(ε) | correct, and made explicit: e^{−ε}(4/ε² + 2κ/ε) ≤ inf_{F_ε}(J+κL) ≤ 4/ε² + 2κ/ε for **all** ε > 0, κ ≥ 0 | (1) + Laplace; the inequalities ε/(e^ε−1) ≥ e^{−ε} and ε coth(ε/2) ≥ 2 (control A2) |
| (7) ⇒ (8) ⇒ bounded density ≤ e/2 ⇒ all-point log-1-Lipschitz (ℓ¹) density ⇒ (9) | correct | FULL closed diamond (fractional, arbitrary-direction steps), tightness under (5) in both α-regimes, outer regularity, Lebesgue differentiation, Rademacher |
| (10) and equality rigidity ⇒ Λ | correct | (9) with constant exactly 1, finite first moment (second moment only for the second identity, trivial if infinite), Fubini on Lipschitz lines |
| weak ⇒ Λ for arbitrary α; W2 when α bounded; W1 for all α | correct | sub-subsequence principle; Fatou; weak + moment convergence ⇔ W_p |
| weak ⇒ TV (6) | correct | translation modulus (11) — true as stated; reviewer's sharp form ‖f − f(·−h)‖₁ ≤ 2 tanh((‖h‖₁+ε)/2) — plus mollification and tightness |
| §6 W2-divergent private example when α → ∞ | correct | closure of F_ε under translation and convex combination; exact moments U = 4 + α^{1/4}, V = 2 + t(R + e^{−R} − 1) (controls E1–E5) |

Not claimed by the candidate and not granted here: any finite-ε exact optimizer of J, L or J+κL over F_ε; any novelty/priority; any human, independent-model-family or formal clearance.

## 2. Independent reconstruction (reviewer's own derivations)

### 2.1 Finite-ε lower bounds (1) and the explicit universal constant
Fix μ ∈ F_ε, i ∈ {1,2}, and use only the shifts ±e_i ∈ D with half-line events A = [m−1,∞)×R (resp. (−∞,−m+1]×R). Privacy gives P(X_i ≥ m−1) ≤ e^ε P(X_i ≥ m), hence P(X_i ≥ n) ≥ bⁿ P(X_i ≥ 0) and symmetrically P(X_i ≤ −n) ≥ bⁿ P(X_i ≤ 0). For n ≥ 1 the outer events are disjoint and P(X_i ≥ 0) + P(X_i ≤ 0) = 1 + P(X_i = 0) ≥ 1, so P(|X_i| ≥ n) ≥ bⁿ. Layer-cake: E|X_i| = ∫₀^∞ P(|X_i| > t)dt ≥ Σ_{n≥1} P(|X_i| ≥ n) ≥ b/(1−b); E X_i² = ∫₀^∞ 2t P(|X_i| > t)dt ≥ Σ_{n≥1}(n² − (n−1)²)bⁿ = b(1+b)/(1−b)² (identity verified exactly in control A1). Summing i = 1,2 gives (1); no density, symmetry or independence is used, and infinite moments satisfy the bounds trivially.

Explicit constants (reviewer): ε·b/(1−b) = ε/(e^ε − 1) ≥ e^{−ε} because 1 − e^{−ε} ≤ ε; ε²·b(1+b)/(1−b)² = [ε coth(ε/2)]·[ε/(e^ε − 1)] ≥ 2e^{−ε} because coth x ≥ 1/x. Therefore, for every ε > 0 and every κ ≥ 0,

    e^{−ε} · (4/ε² + 2κ/ε)  ≤  inf_{F_ε}(J + κL)  ≤  4/ε² + 2κ/ε,

the upper bound being attained by the product-Laplace law. So the "universal O(ε)" in (2)–(4) is at most 1 − e^{−ε} ≤ ε in absolute value, uniformly in κ; the weighted ratio is a mediant of the two coordinate ratios and lies between them for every κ. Control A2 (60-digit Decimal) confirms this for ε ∈ [10⁻⁶, 5] and a κ battery including 0, 1/ε³, an oscillating (1+sin(1/ε))ε^{−3/2} and 10⁶, and shows the actual leading deviation is ε/2 for both J and L ((1−r)/ε → 0.5000).

### 2.2 Laplace feasibility
λ_ε(x) = (ε²/4)e^{−ε‖x‖₁} satisfies λ_ε(y) ≤ e^{ε‖d‖₁} λ_ε(y+d) for all y, d (reverse triangle inequality), so μ(A) = ∫_A λ_ε ≤ e^ε ∫_A λ_ε(y+d)dy = e^ε μ(A+d) for every Borel A and ‖d‖₁ ≤ 1. Coordinates are i.i.d. Laplace(1/ε): E|X_i| = 1/ε, E X_i² = 2/ε², so J = 4/ε², L = 2/ε. (Control F1: 40 000 boundary-of-diamond samples, max log-ratio exactly ε.)

### 2.3 Scaled measure order (7)–(8), density bound, all-point representative, (9)
For h ≠ 0 put n = ⌈‖h‖₁/ε⌉ ≥ 1 and d = h/(εn); then ‖d‖₁ ≤ 1 — this is where the FULL closed diamond is used (fractional length, arbitrary direction). Iterating privacy n times with the same d and rescaling, μ_ε(A) ≤ e^{εn} μ_ε(A+h) ≤ e^{‖h‖₁+ε} μ_ε(A+h) for all Borel A (control G1: 10 000 random (h, ε)).

Tightness under (5): multiplying (5) by ε² gives U + αV ≤ (4+2α)(1+o(1)); (1) gives U ≥ 4e^{−ε}, V ≥ 2e^{−ε}. If α is bounded along a subsequence, U is bounded there (this uses (5) and V ≥ 0 — see MINOR-2). If α → ∞ along a subsequence, V ≤ (2 + 4/α)(1+o(1)) → 2 and V ≥ 2e^{−ε}, so V → 2. Either way the subsequence is tight.

Passage to the limit: for every nonnegative measurable g, ∫g dμ_ε ≤ e^{‖h‖₁+ε} ∫ g(·−h) dμ_ε (indicators → simple functions → monotone convergence). For bounded continuous g both sides converge along the weakly convergent subsequence, giving ∫g dμ ≤ e^{‖h‖₁}∫g(·−h)dμ. Open sets follow from g_k ↑ 1_U with g_k(·−h) ≤ 1_{U+h}; Borel sets by outer regularity (U + h runs over the open supersets of A + h). This is (8) for every h and every Borel A.

Density bound: for h ∈ D, (8) gives μ(A) ≤ e μ(A+h); integrating over h ∈ D (|D| = 2) and using ∫_D 1_A(z−h)dh = |D ∩ (z−A)| ≤ |A| yields μ(A) ≤ (e/2)|A|. The representative p(z) := limsup_{r↓0} μ(B_r(z))/|B_r| is a version of the density, satisfies p ≤ e/2 everywhere, and because B_r(z) + h = B_r(z+h), inequality (8) at balls gives p(z) ≤ e^{‖h‖₁} p(z+h) for **every** z, h. Since ∫p = 1 there is z₀ with p(z₀) > 0, whence p(z) ≥ e^{−‖z−z₀‖₁}p(z₀) > 0 everywhere; using ±h, |log p(z) − log p(z+h)| ≤ ‖h‖₁, i.e. log p is 1-Lipschitz for ℓ¹ (so p itself is globally Lipschitz with constant e/2). Rademacher gives a.e. differentiability with |∂_i log p| ≤ 1, i.e. (9): |∂_i p| ≤ p a.e.

### 2.4 Integration by parts (10) and rigidity
With χ_R(z) = χ(z/R), χ smooth, compactly supported, ≡ 1 on the unit ball: ∫∂_i(z_i p χ_R) = 0 for the compactly supported Lipschitz integrand, so ∫pχ_R + ∫z_i∂_ip χ_R + ∫z_i p ∂_iχ_R = 0. The last term is ≤ (C/R)∫_{|z|≥R}|z_i|p ≤ C∫_{|z|≥R} p → 0; the middle term converges by dominated convergence since |z_i∂_ip| ≤ |z_i|p ∈ L¹ (finite first moment). Hence 1 = −∫z_i∂_ip ≤ ∫|z_i||∂_ip| ≤ ∫|z_i|p. Similarly ∂_i(z_i|z_i|p) = 2|z_i|p + z_i|z_i|∂_ip; the boundary term is ≤ (C/R)∫_{R≤|z|≤2R} z_i²p ≤ 2C∫_{|z|≥R}|z_i|p → 0 (first moment suffices), and the middle term needs ∫z_i²p < ∞ — if infinite the inequality is trivial. Hence 2∫|z_i|p ≤ ∫z_i²p. Summing: ∫‖z‖₁p ≥ 2, ∫|z|²p ≥ 4. Controls C1–C4 verify both identities numerically on every tested density (Laplace, e^{−√(1+z²)}, rate-a Laplace, (9)-cone perturbations) and that the inequalities hold exactly on the (9)-cone and fail as soon as |∂ log p| exceeds 1 somewhere (rate 1.5, "steeper" perturbations give E|Z₁| < 1).

Rigidity: if ∫‖z‖₁p = 2, each ∫|z_i|p ≥ 1 forces both = 1, so a.e. −z_i∂_ip = |z_i||∂_ip| and |∂_ip| = p; with p > 0 this is ∂_ip = −sign(z_i)p a.e. By Fubini, for a.e. z₂ the Lipschitz function z₁ ↦ log p(z₁,z₂) has a.e. derivative −sign(z₁), hence p(z₁,z₂) = p(0,z₂)e^{−|z₁|} for a.e. z₂ and, by continuity, for all; the same in z₂ gives p = p(0,0)e^{−‖z‖₁}, and normalization forces p(0,0) = 1/4. If instead ∫|z|²p = 4, then ∫z_i²p ≥ 2∫|z_i|p ≥ 2 forces ∫z_i²p = 2 and ∫|z_i|p = 1, reducing to the first case. Control C4 (perturbation cone φ_θ = |z| − θ·min(|z|,1), which keeps |φ'| ≤ 1) shows E|Z₁| = 1 only at θ = 0 and strictly larger for θ ∈ (0,1].

### 2.5 Case split, weak convergence of the whole family, W2/W1
α bounded: αV ≥ 2αe^{−ε} and (5) give U ≤ 4 + (4+2α)o(1) + 2α(1−e^{−ε}) → 4; with U ≥ 4e^{−ε}, U → 4. Fatou on a weak limit μ: ∫|z|²dμ ≤ 4; (10) gives ≥ 4; equality ⇒ μ = Λ. α → ∞: V → 2 (2.3), Fatou gives ∫‖z‖₁dμ ≤ 2, (10) gives ≥ 2, equality ⇒ μ = Λ (finite first moment suffices for the first identity, so the possibly infinite second moments of μ_ε are irrelevant — consistent with §6). Every sequence ε_k → 0 has, for each subsequence, a further subsequence along which α is bounded or α → ∞; it is tight and all its weak limits are Λ, so μ_ε ⇒ Λ for the whole family. If α is bounded along the whole family, U → 4 = E_Λ|Z|² and weak + second-moment convergence gives W2 → 0. W1: for α → ∞ subsequences, V → 2 = E_Λ‖Z‖₁ gives W1 → 0; for bounded-α subsequences W1 ≤ W2 → 0; the sub-subsequence principle gives W1 → 0 for arbitrary κ(ε) ≥ 0.

### 2.6 Weak ⇒ total variation
Each μ_ε has a density f_ε (original privacy integrated over D: 2μ_X(B) ≤ e^ε|B|). Sharp translation modulus (reviewer's derivation): let g = f_ε(·−h) (density of τ_hμ_ε), C = e^{‖h‖₁+ε}, A = {f_ε > g}, a = μ_ε(A), a' = ∫_A g = μ_ε(A−h), D = a − a' = ½‖f_ε − g‖₁. (7) with shift −h at A: a ≤ C a'. (7) with shift +h at A^c − h: 1 − a' = μ_ε(A^c − h) ≤ C μ_ε(A^c) = C(1−a). Hence D ≤ a(C−1)/C and D ≤ (C−1)(1−a), so D ≤ (C−1)/(C+1) and

    ‖f_ε − f_ε(·−h)‖₁ ≤ 2 tanh((‖h‖₁+ε)/2) ≤ ‖h‖₁ + ε ≤ e^{‖h‖₁+ε} − 1.

The candidate's (11) is therefore true. The constant 2(C−1)/(C+1) is attained by the staircase density c·C^{−|k|} on unit cells (control D1, exact rational arithmetic, with a = C/(C+1) and both set inequalities tight — re-checked exactly for C ∈ {11/10, 3, 7}) and by an LP over all cyclically-discretized private masses and many target sets A including an adaptive A* = {f > f(·−h)} (control D2: LP maximum equals (C−1)/(C+1) to 10⁻⁹ for s ∈ {0.2, 1, 3}, strictly below the candidate's (C−1)/2). (12) follows by Minkowski: ‖f_ε − f_ε∗ρ_δ‖₁ ≤ sup_{‖h‖₁≤δ}‖f_ε − f_ε(·−h)‖₁ ≤ δ + ε. For fixed δ, (f_ε∗ρ_δ)(z) = ∫ρ_δ(z−y)μ_ε(dy) converges pointwise to (Λ∗ρ_δ)(z) (bounded continuous integrand), the family is uniformly Lipschitz in z (constant ‖∇ρ_δ‖_∞), so convergence is uniform on compacts, and tightness controls the tails: L¹ convergence. Then limsup_ε ‖f_ε − λ‖₁ ≤ δ + ‖λ∗ρ_δ − λ‖₁ ≤ 2δ (the last by the same modulus applied to λ, which satisfies (8) with ε = 0), and δ ↓ 0 gives TV convergence for arbitrary κ(ε).

### 2.7 §6 counterexample
F_ε is closed under translation (the defining inequality is translation invariant) and convex combination (it is linear in μ), so (1−t)Λ + t τ_{Re₁}Λ in Z-coordinates is the law of εX for some X ∈ F_ε (control E5: 40 000 boundary samples, max log-ratio exactly ε). For Z₁ ~ Laplace(1) and R ≥ 0, E|Z₁+R| = R + e^{−R} (control E1), so exactly U = 4 + tR², V = 2 + t(R + e^{−R} − 1), |V−2| ≤ tR. With R = α^{1/2}, t = α^{−3/4}: U = 4 + α^{1/4}, |U + αV − (4+2α)| ≤ α^{1/4} + α^{3/4} = o(α), so (5) holds; W2(Law Z, Λ) ≥ √U − 2 = √(4+α^{1/4}) − 2 → ∞ (reverse triangle inequality in L²); TV = t(1 − e^{−R/2}) ≤ t → 0 (control E4); W1 ≤ tR = α^{−1/4} → 0 (coupling moving mass t by distance R). Controls E2 verify all of this for α ∈ {16, …, 10⁸}. Mutation E3 (t = 1/α) gives U = 5 and W2 ≥ √5 − 2: W2 can fail to converge even with bounded second moments, still consistent with the candidate (α → ∞, W2 not claimed). For bounded α the same mixture with fixed t, R > 0 violates (5) because U → 4 is forced (2.5) — consistent with the W2 claim in the bounded case.

## 3. Findings

**MINOR-1 — (11) is stated with a constant the sketched argument does not deliver; the statement is nevertheless true.** §5 says "the same all-point ball-average representative argument, applied to (7), gives ‖f_ε(·−h) − f_ε‖₁ ≤ e^{‖h‖₁+ε} − 1". The pointwise ratio f ≤ C f(·−h) alone only yields ∫(f − f_h)₊ ≤ (C−1)∫_A f_h ≤ C − 1, i.e. ‖f − f_h‖₁ ≤ 2(C−1), a factor 2 weaker than stated. The two-sided set argument of §2.6 proves the stated bound with room to spare (sharp constant 2 tanh((‖h‖₁+ε)/2), attained by the staircase, confirmed exactly and by LP). Impact on conclusions: none — (12) and the TV upgrade only need some modulus vanishing as ‖h‖₁ + ε → 0. Repair: replace the one-line justification by the set argument above (or by the sharp statement).

**MINOR-2 — §3 attributes the uniform bound on E|Z|² in the bounded-α case to (1).** (1) provides only lower bounds; the upper bound U ≤ (4+2α)(1+o(1)) comes from (5) together with αV ≥ 0. The subsequent tightness and U → 4 arguments are correct once "(1)" is read as "(5) with V ≥ 0". Repair: textual.

**MINOR-3 — rigidity step from ∂_ip = −sign(z_i)p a.e. to the product form is asserted, not argued.** It requires the Fubini/absolute-continuity-on-lines step for the Lipschitz function p (§2.4), which is available since §3 established global Lipschitz continuity of p. Repair: add the one-sentence Fubini argument; no new hypothesis.

Notes (not findings): (i) the relative error in (2)–(4) can be stated with the explicit bound |O(ε)| ≤ 1 − e^{−ε} ≤ ε (§2.1); the candidate's "O(ε)" is correct as written. (ii) The FULL closed diamond is load-bearing exactly in (7) (fractional, non-axis steps); nothing outside this class is claimed or granted. (iii) A 1-D discrete two-sided geometric law has smaller second moment than the continuous Laplace at finite ε (control B2: 180 vs 200 at b = 0.9) but it is not in F_ε (it fails for non-lattice shifts: μ({0}) > 0 = μ({d})); this does not contradict anything in the candidate and illustrates why no finite-ε exact optimizer is claimed or granted. (iv) The claim "No LAW642, MDA, PMLR, v241 or prior research theorem is imported" is consistent with the text, which is self-contained; the reviewer did not and did not need to identify those labels.

## 4. Counterexample search for failed quantifiers (none found)

For each quantifier the reviewer attempted to break it and recorded the outcome:
- "for all μ ∈ F_ε" in (1): laws outside F_ε break (1) immediately (B4: Laplace with rate 2ε; B5: a degenerate second coordinate; F2: Gaussian), so privacy on both coordinates is load-bearing; three explicit in-class laws (continuous Laplace, staircase, and the discrete geometric for the vertex-only tail inequality) satisfy (1) with the predicted tail equality P(|X_i| ≥ n) = bⁿ in two of them (B1–B3, exact).
- "for all κ(ε) ≥ 0, oscillating or unbounded" in (4): the finite-ε ratio is a mediant of the two coordinate ratios, so no κ can push it outside [e^{−ε}, 1] (A2 battery incl. oscillating and 10⁶).
- "every weak limit is Λ": the only input is (9) with constant 1 plus finite first moment; densities with |∂ log p| ≤ 1 never produce ∫‖z‖₁p < 2 (C2, C4 cone) and equality occurred only at Λ; violating the constant by any margin (rate 1.5, θ = 0.25 steepening) produces first moments below the threshold (C3, C4 NEG), so the inequality cannot be strengthened and is exactly what the limit supplies.
- "(11) for all h, all f_ε": LP maximization of the translation defect over all cyclically-discretized private masses and 16 target sets with adaptive refinement never exceeded (C−1)/(C+1) (D2), and the staircase shows this value is attained; the candidate's constant is never approached.
- "W2 need not converge when α → ∞": explicit private W2-divergent family verified (E2) and a bounded-second-moment non-convergent variant (E3); for bounded α the construction cannot satisfy (5) (§2.7), consistent with the W2 claim there.

## 5. Control run binding (one observed run)

- Script: `reviewer-f121-controls-v1.py`, SHA256 `0a43c288decaccc9cc9076192f955e997cb5058e25f30a85a8c919140e0ce0fb`, 24122 bytes; reviewer-authored; imports only numpy/scipy/stdlib; reads the candidate and manifest for pin verification only.
- Interpreter: `/usr/bin/python3` (CPython 3.9.6), numpy 2.0.2, scipy 1.13.1; HiGHS LP via `scipy.optimize.linprog`.
- Observed clocks (`/bin/date -u` from inside the script): start `2026-10-29T03:04:22Z`, end `2026-10-29T03:04:22Z`; exit status 0; wall ≈ 1.1 s.
- Result: 22 controls, 22 PASS (14 positive, 4 negative — each showing the expected violation —, 4 mutation).
- Receipts: `reviewer-f121-controls-v1-receipt.json` SHA256 `ab3bb59e40719375682dbad4b6101c4c86667398c7a56e8a94e32d92a06ee195` (9330 bytes); `reviewer-f121-controls-v1-receipt.txt` SHA256 `b9cfe6e1578135280a2f2514be489cb8870868de25cd375744dcb108b1af74ce` (7240 bytes, 30 LF). Both embed the candidate pins (`8615b715…`, 8214 bytes, 108 LF) and manifest pin (`ce84a1d3…`, 1781 bytes).
- Supplementary exact check (not in the script, run interactively in the same session, exact `fractions`): staircase with C ∈ {3, 11/10, 7} gives a = C/(C+1), a' = 1/(C+1), D = (C−1)/(C+1), and both set inequalities a ≤ Ca', 1−a' ≤ C(1−a) hold with equality.
- Control limitations: quadrature tolerances ≈ 10⁻¹³ (C, D1b, E1, E4); LP discretization N = 90 cells (the attained value is also proved analytically); privacy ratio checks are 40 000-sample spot checks (the proofs are the reverse-triangle / linearity arguments, not the samples); Decimal precision 60 digits. No control is a proof of a limit statement; the limit statements rest on §2.

## 6. Not established / outside this review

No finite-ε exact optimizer, no sharpness of the constant 1 − e^{−ε} at finite ε beyond the two-sided bracket, no novelty or priority assessment, no human review, no independent-model-family review, no formal/kernel verification. The candidate's §7 statement that no numerical/formal/independent/human/parent verification was performed is superseded only by this same-harness numerical-and-analytic review; parent adoption remains a parent decision.
