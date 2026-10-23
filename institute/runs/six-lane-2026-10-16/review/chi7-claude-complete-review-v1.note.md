# Referee report: `PROOF_CHI7.r1.md` (sha256 8a79ba3c…906c)

**Bottom line.** I find no fatal and no major defects.

- **Upper bound.** The proof correctly reruns KPW's balanced-colouring second moment and small subgraph conditioning (SSC) at (k, d) = (4, 7).
- **New mathematics.** The only new content is Lemma 2.1 → Theorem 2.2 → Corollary 2.3, and it is correct. It is the k = 4 case of the constant AN already obtain in their display (12).
- **Audit.** My own audit of the supplied KPW §§1–4 agrees with the proof's audit. The hypothesis d < 2(k−1)log(k−1) acts only through (H1), (H2) and the trivial consequence k ≥ 3.
- **Lower bound.** χ ≥ 4 is already published (Molloy–Reed, as quoted in KPW).
- **What remains** is citation and statement fixes.

Line conventions: "P l.x" is the proof file. "KPW/AN/W99 l.x" are the layouts supplied to me; these do not match the proof's own references (finding m1).

---

## 1. Adversarial audit: every place d or the hypothesis enters KPW §§1–4

| KPW step (supplied lines) | How d enters | Uses the hypothesis or a consequence? |
|---|---|---|
| Prop 2(a), EY count, l.187–228. Lemma 3, l.235–244, proof l.398–575 | Saddle point r² = dn/(k(k−1)). Off-saddle bounds exp(dn/2 − dn/(k(k−1))) and exp(dn/2 − d log²n/(8k(k−1))) at l.479–512 | No. Needs only d > 0 and k ≥ 3 |
| E(YX_m) and joint moments, l.258–376. Lemma 4, l.379–397 | Factor (d(d−1)n/k)^m and ratio C(−2m)/C(0) | No |
| (1.2), l.155–160 | Series Σ((d−1)/(k−1)²)^m/m | (H1) only: it converges iff d−1 < (k−1)². At (4,7) the ratio is 2/3 |
| (1.3), l.161–167. Proof of Thm 1, l.171–176 | Algebraic identity from Prop 2 | Only through Prop 2(b) and (1.2). The lower-bound sentence at l.177–181 uses minimality of k, but the proof does not use it |
| (3.1)–(3.9), l.579–789. Lemma 5 and proof, l.725–735 and l.1051–1156 | Scale dn/k. Maximiser ℓ ∝ m_pq·m_rs on L̂, then extension by continuity | No. I re-derived (3.9): the powers of n, e and d cancel, and k^{−(d−1)n}·k^{dn} = k^n |
| Lemmas 6, 7, 9: l.800–842, l.1157–1231, l.1233–1272 | None | Only k ≥ 3, for the eigenvalue (k−1)(k−2) > 0 |
| Lemma 8 and proof, l.907–923 and l.1273–1549 

| ρ = √(dn)/(k(k−1)) (l.1313); c = d/(2k²(k−1)²) (l.1415); ε′ < d/(16k²(k−1)²) (l.1376–1377); "ε small" (l.1475) | No. By (3.20) with \|a_pq\| < ε log n/√n, ε′ = d(k−1)²k²ε²/(2(k²−2k+2)) + o(1). So d cancels, and the condition is ε² < (k²−2k+2)/(8k⁴(k−1)⁴). The choice at l.1475 is likewise d-free |
| (3.10)–(3.11), l.859–930 | Exponent −n(k²−2k−d+2)Q/(2(k²−2k+2)). Re-derived: d(k−1)² − (d−1)(k²−2k+2) = k²−2k+2−d | The formula holds for all d. Its decay needs (H1) |
| (3.12)–(3.14), l.953–1012 | Positive definiteness of H, Euler–Maclaurin, Lemma 4 (explicit remark at l.998–999) | (H1) |
| (3.15) and the S_2 bound, l.1013–1049 | AN Theorem 7 | (H2). There is no coupling with ε: for fixed ε, C > 0, exp(−Cε²log²n/(k−1)⁴) = n^{−Θ(log n)} |
| §4, k′ at l.1553 | Parity of dk | No |
| Theorem 10 proof, l.1566–1647 | (4.1) and the (1.1) analogue via b_ij concentration (l.1600–1618). (4.2) via restricting M to near J (l.1634–1641) and b_pqrs concentration (l.1642–1647). Closes via l.1583–1584 | (4.1) and (1.1): no. The restriction is the S_2 estimate, so (H2). Concentration: no. The close uses Prop 2(b) and (1.2)/(1.3), so (H1) and (H2) |
| Theorem 1 for k ∤ n, l.1648–1660 (supplied text ends mid-sentence) | d ≥ 3, Theorem 10, local-structure facts | Visible part: no. The quote "(Note that k ≥ 3 …)" at P l.200 is not in my copy. It would only use the consequence k ≥ 3, which holds at k = 4 |

**Answer to the central question: confirmed.** No step other than (H1) and (H2) uses the hypothesis.

- **Consequences actually used.** Only two: k ≥ 3 (Lemmas 3, 6, 9 and the spare colour in §4) and (H1) itself.
- **Why (H1) is a consequence.** Since 2 log x ≤ x, we get 2(k−1)log(k−1) ≤ (k−1)² < k²−2k+2. This is why KPW write "guaranteed from our assumptions" at l.998.
- **Sanity check near J.** The decay rates per unit of Σa² are:
  - true exponent (3.11): 3/20;
  - φ: ((k−1)²−d)/(2(k−1)²) = 1/9;
  - global constant: C_7 ≈ 0.0231.
  
  The ordering is the expected one, because φ is the Lemma 5 relaxation and is an upper bound on the true exponent.

## 2. Findings

**Fatal:** none. **Major:** none.

**Minor**

- **m1. Line references do not match the supplied layouts.** This affects P l.39–40, 49, 55, 68, 80, 176, 183, 186–200, 207, 251 and 261. The offset grows monotonically. Examples:
  - KPW: "l.570" is l.579; "l.982–983" is l.998–999; "l.1004–1020" is l.1020–1036; "l.1356" is l.1377; "l.1536/1558/1610" are l.1560/1583/1634.
  - AN: g_c "l.275–286" is l.280–291; display (12) "l.756–763" is l.797–806.
  - W99: Theorem 4.1 "l.1561–1596" begins at l.1592; Theorem 2.6 "l.361–366" is l.368–373; equation (3) "l.248" is l.253.
  
  Fix: regenerate the references against the pinned layout hashes.
- **m2. Theorem 10 is misstated (P l.248–250).** The proof says "pairwise non-adjacent edges". KPW l.1561–1563 require the endpoints to induce a perfect matching. The reduction does produce induced matchings (see 3.6), so the conclusion stands, but the statement should be corrected.
- **m3. Wrong source for loop exclusion (P l.237).** (3.2)–(3.3) are second-moment constraints. The relevant source is the first-moment count at KPW l.191–198, or simply the definition of a proper colouring.
- **m4. "Uniformly distributed" needs its conditioning stated (P l.251–254).** It holds only conditionally on 𝒢 = {dist(v₁,v₂) ≥ 4, no triangle at v₁ or v₂}, where P(𝒢) → 1.
  - I checked that, conditional on 𝒢, the pair (G′, L) is exactly uniform: every (G′, L) has exactly C(14,7) good preimages.
  - The proof should state this and the a.a.s. transfer.
  - KPW's own text for this step runs past the supplied l.1660, so P l.183 ("l.1–1645") and P l.200 cannot be checked against the pinned text.
- **m5. SSC conclusion is not visible in the cited source (P l.68–75).** The W99 excerpt stops inside condition (d) at l.1610. Hypothesis (d) and the conclusion P(Y>0) = exp(−Σ_{δ_i=−1} λ_i) + o(1) are not visible. They match Janson's theorem and KPW's own use at l.171–175. Cite the actual statement.
- **m6. The Theorem depends on an unreviewed computation (P l.310–316, 323).** As written, the Theorem's proof relies on Prop 5.4, which is computer-assisted. The published route already suffices: KPW l.69 and l.177–181 at q = 3, d = 7. Make that route primary and §5 a cross-check.
- **m7. Notation clash (P l.204 vs l.44).** (H2) uses KPW's J_k (all ones), while §2 uses J with all entries ¼. Unify.

**Checked and correct, no action needed:** the remark at P l.207–209. With δ from KPW l.941, nδ² = ε²log²n/(k−1)⁴, so the exponent does need the extra (k−1)⁻⁴. The conclusion n^{−Θ(log n)} is unchanged.

## 3. Verification of the requested items

### 3.1 Lemma 2.1: correct, including the equality cases

- **(a)** The mean value theorem on t ↦ t log 4t over [pᵢ/2, pᵢ] gives the stated bound. The quadratic term is O(ε). Since ε log 4ε → −∞ dominates, boundary points are never minimisers.
- **(b)** ∂ⱼ[(3/2) log 3 Σp²] = 3 log 3·pⱼ, so ψ is as stated. ψ″ = −1/u² < 0, so p takes at most two distinct values.
- **(c)** Each of the following checks:
  - y = (1−v)/4 and Σp² − ¼ = 3v²/4;
  - G′ = 3L, L′ = q − 3 log 3, and q″ = 54/(1+3v)³ + 2/(1−v)³ > 0;
  - q(0) = q(2/3) = 4 and q(1/3) = 3;
  - since 1 < log 3 < 4/3, q − 3 log 3 has exactly two zeros;
  - L(0) = L(2/3) = 0, and the sign pattern of L is as claimed;
  - G(0) = G(2/3) = 0, and G is strictly monotone on each piece.
  
  The endpoint values G(−1/3) = G(1) = 8 log 2 − (9/2) log 3 ≈ 0.601 are consistent.
- **(d)** r′ = atanh u − u ≥ 0, and (3/8) log 3 < ½.
- **(e)** Sound.
- **Cross-check against AN.** By AN Prop 10 (l.427–438), D(p‖U) ≥ log 4 − f(Σp²) = y·η(y). So Lemma 2.1 is equivalent to min η = (3/2) log 3 at k = 4, with equality at (¾, 1/12, 1/12, 1/12), where D = ½ log 3 and Σp² = 7/12.

### 3.2 Theorem 2.2 and Corollary 2.3: correct

- H(A) = log 4 − ¼ Σᵢ D(aᵢ‖U).
- E(A) − E(J) = log(1 + (ρ−1)/9) ≤ (ρ−1)/9. With c ≥ 0 this bounds the energy gain from above, while Lemma 2.1 bounds the entropy deficit from below.
- Σᵢ(Σⱼ aᵢⱼ² − ¼) = ρ − 1 = Σ(aᵢⱼ − ¼)². This needs only row-stochasticity.
- C_7 = 0.023091. φ_7(J) agrees with KPW l.1015–1019. (3.15′) has exactly the form of KPW (3.15) at l.1032–1036, uniformly near J.

### 3.3 φ = g_{d/2}, and AN display (12)

- On doubly stochastic matrices, Σ_{p≠r, q≠s} m_pq·m_rs = k² − 2k + Σm². So the two lines of KPW (3.8) (l.749–757) agree, and both equal AN's g_{d/2} (l.280–291).
- At k = 4: η(0) = 2, η(1/3) = (3/2) log 3, η(3/4) = (4/3) log 4. The minimum is (3/2) log 3, since 3⁹ < 2¹⁶. This gives c* = (27/8) log 3 ≈ 3.7078 > 7/2.
- The (10) → (11) step uses log(1+x) ≤ x and y ∈ [0, 1 − 1/k]. A bracket is lost in the layout of (10) at l.745–746; this is harmless.
- The main line of the proof does not need any of this.

### 3.4 SSC at (4,7), against W99 Theorem 4.1 (l.1592–1610)

- λᵢ = 6ⁱ/(2i) and δᵢ = (−1)ⁱ 3^{1−i}. Only δ₁ = −1.
- **(a)** From W99 Theorem 2.6.
- **(b)** From KPW (1.1), which is d-free.
- **(c)** Σ λᵢδᵢ² = (9/2) Σ (2/3)ⁱ/i = (9/2) log 3, which equals KPW (1.2) at (4,7).
- **(d)** E(Y²)/(EY)² → 3¹²/(3^{9/2}·3³) = 3^{9/2}. I also recombined (3.14) with γ(k) (l.921–923): the powers of n, k and 2π reproduce the Prop 2(b) constant.
- EY grows exponentially, since 4(¾)^{7/2} ≈ 1.461.

### 3.5 Loop and double-edge conditioning: correct

- {Y > 0} ⊆ {X₁ = 0}, so P(Y>0 | X₁=0) → 1.
- The denominator P(X₂=0 | X₁=0) → e⁻⁹.
- Each simple graph corresponds to (d!)ⁿ pairings, and P(Simple) → e⁻¹².

### 3.6 n ≡ 2 (mod 4): correct, subject to m2 and m4

- Arithmetic: k′ = 4, r = 2, ℓ = 7, and n−2 ≡ 0 (mod 4).
- On 𝒢 there are 14 distinct neighbours, with no edges inside N(vᵢ) and none between N(v₁) and N(v₂). So the new edges form an induced perfect matching and G′ is simple.
- Giving both vᵢ colour 3 is valid.
- Theorem 10 depends on d only through Prop 2(b) and (1.2)/(1.3).

### 3.7 Lower bound

- **Published route.** 3(2/3)^{7/2} ≈ 0.726 < 1 (KPW l.69), and 7 > 5 log 3 (KPW l.177–181).
- **Lemmas 5.1–5.3.** Correct. I re-derived the exponent nΦ_d and the factor e⁴(N+1)².
- **Prop 5.4.** Unverified (see §4).

### 3.8 The argument does not give d = 8: confirmed

- At (4,8), (H1) = 2 and the series (1.2) has ratio 7/9, so both still hold. The failure is in (H2).
- Witnesses that J is not the global maximiser of φ_8:
  - φ_8((J+I)/2) − φ_8(J) ≈ +0.00742, which is equivalent to 13³² > 2⁵⁶·3³²·5⁵;
  - AN's own matrix (l.343–345) gives +0.00329;
  - C_8 < 0.
- Because φ is only an upper bound, this says nothing about χ(G_{n,8}), as P l.336–337 correctly states.

## 4. Numerical checks (separate from correctness; recomputed by hand)

| Quantity | Value | Quantity | Value |
|---|---|---|---|
| C_7 | 0.023091 | C_8 | −0.032465 |
| c* | 3.707817 | 2c* | 7.415634 |
| 6 log 3 / 8 log 4 / 7 log 4 / 5 log 3 | 6.5917 / 11.0904 / 9.7041 / 5.4931 | Σλδ², 3^{9/2} | 4.943755, 140.296 |
| 16(¾)⁷ | 2.1357 | Φ_5, Φ_6, Φ_7 at the balanced point | +0.08495, −0.11778, −0.32052 |
| max Φ_7 on C₂ | −2 log 2 | (J+I)/2 gap at d = 7 / d = 8 | −0.032602 / +0.007419 |

For Prop 5.4 I evaluated Φ_7 on C₁ at a = 0.28, 0.30, 0.32, ⅓, 0.34, 0.36, 0.40, 0.45. The values are −0.599, −0.415, −0.334, −0.3205, −0.324, −0.367, −0.578, −1.031. These are consistent with the maximum being at the balanced point, but they are not a proof.

The float sanity checks in P l.350–353 are not evidence. Along (1−t)J + tI I get a minimum ratio of ≈ 0.0435, which matches the proof.

## 5. Independent proof map and trust boundary

Tags:
- [V] verified here;
- [A] imported, with its d-dependence audited here;
- [I] imported as is;
- [C] computer-assisted, not reviewed.

**Upper bound**

1. [V] φ = g_{d/2}.
2. [V] Lemma 2.1 ⇒ Theorem 2.2 ⇒ Corollary 2.3, which is (H2).
3. [V] (H1), (1.2) and (1.3) at (4,7).
4. [A] KPW §3 gives E(Y²) (Prop 4.1).
5. [I] KPW Prop 2(a).
6. [I] W99 Theorem 4.1 (Janson) and Theorem 2.6 (Bollobás), with [V] the hypothesis checks and conditioning. This gives n ≡ 0 (mod 4).
7. [A] KPW Theorem 10. KPW's own proof of it is a sketch.
8. [V] The reduction combinatorics and conditional uniformity, with [I] KPW's text beyond l.1660. This gives n ≡ 2 (mod 4).

**Lower bound**

9. [I] Molloy–Reed (KPW l.69, l.177–181), with [V] the arithmetic.
10. Alternative: [V] Lemmas 5.1–5.3 and [C] Prop 5.4.

**Trust boundary.** The Theorem is as reliable as KPW §§2–4 at general d, Janson/Wormald SSC, Bollobás and Molloy–Reed, plus the [V] items. My visibility limits were the KPW text ending at l.1660 and the W99 text ending at l.1610.

## 6. Significance (novelty not assessed)

If the imports hold, the proof closes KPW's {4,5} window at d = 7. The new mathematics is small: an elementary per-row inequality equivalent to AN's minimum of η, plus a d-dependence audit. The route provably stops at d = 8.

On the remark at P l.391–392: for q = 5 and q = 6 the window [2(q−1)log(q−1), 2(q−1)³log(q−1)/(q(q−2))) contains no integer. The first candidate is q = 7, d = 22, which I have not checked.

VERDICT: ACCEPT-WITH-FIXES
