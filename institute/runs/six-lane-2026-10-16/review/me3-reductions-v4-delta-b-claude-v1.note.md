**DISPOSITION: ACCEPT-WITH-FIXES** for reductions-v4, correctness only. 0 FATAL, 0 MAJOR, 4 MINOR, all editorial.

- Every statement and proof on the essential path is accepted as written.
- The fixes touch one missing definition, two unused remarks and notation. They need no re-review.

**Limits of this audit**
- I used no tools and executed nothing. Hashes were compared only as printed.
- The diff was not supplied, so I audited the full final text. SOURCE02 only steered emphasis, so the completeness of its hunk list is not relied on.
- The owner's theorem file and STATUS-v4 are not in the packet.
- S00:n means SOURCE00, line n.

### 1. Earlier findings (SOURCE01)

- **MINOR-1: fixed.**
  - S00:591–593 now reads "equality for some minimizer (Thm 5.6)".
  - Minimizers are written (ω_m, φ_m) at S00:526, 538 and 756–757.
  - (ω*, φ*) appears only as the EXPLORATORY Newton point, with its non-certification stated (S00:566–576).
- **MINOR-2: fixed, more strongly than I asked.**
  - The chain is now exact and needs no U: Lemma 4.2 (S00:429–434), tail 428/2125 (S00:494–496), witness 773/3844 (S00:522–538).
  - Sturm and Arb material is relabelled supplementary (S00:397–401, 453, 549–551).
  - The hand route is recorded at S00:553–564; its wording is MINOR-B.
- **MINOR-3: fixed in this file** (S00:467–469, 596–599, 755). The original locus is the owner's S00:160, which is not supplied, so the owner-side fix is unverified. See also MINOR-A.
- **MINOR-4: fixed** (Cor 7.2 and Remark 7.2a, S00:760–785; audited in §2).
- **MINOR-5: fixed in this file** (S00:587, 609–613, 802–803). The owner's S00:50 and STATUS S04:24 are not supplied, so those are unverified.
- **MINOR-6: fixed.**
  - Renames: S00:167, 278, 286–293.
  - "≢ 0" note: S00:95–101.
  - ME(N) ⊆ ME(≤3) with padding: S00:162, 172–174.
  - Cosmetic residue is MINOR-D.

### 2. Mathematical changes: independently audited, all correct

**Positive mass (S00:95–101, 216–233)**
- m1 > 0 holds because t·f > 0 on {f > 0}∖{0}, which has positive measure.
- Lemma 2.3: ∫f = ∫_M(∫g_μ)dν > 0, since every inner integral is > 0 and ν(M) > 0.
- The θ-wise inequality integrates by Tonelli, and f is shown to satisfy 0.2 before Lemma 2.2 is applied to it.
- Remark 2.3a(2): (1+t²)(t−τ)²e^{μ_max|τ|}e^{−μ_min t} dominates for either sign of τ.
- Every later use of "≢ 0" (1.1, 1.2, 1.3, 2.1, 2.3a) concerns a continuous function.

**Root isolation, closed form and resultant (S00:385–427)**
- I re-expanded each of these:
  - 4P−5Q² = 3(τ²−4τ+2)² + 8τ²;
  - P′Q − 2PQ′ = 8q;
  - the six values of q;
  - 2P − 3Q² = τ⁴ − 8τ³ + 20τ² − 12;
  - s(0) = 48/36 − 1.
- The sign pattern of q and Δ3 = s(x1) ∈ (1/4, 1/3) follow.
- Independent check that h(s(x_i)) = 0, working mod q with x³ ≡ 9x² − 18x + 6:
  - P ≡ 34x² − 96x + 60 and Q² ≡ 19x² − 60x + 42.
  - So P − Q² ≡ 15x² − 36x + 18 ≡ Q²·C, where C := (x(9−x)² − 24)/24 ≡ (−3x² + 21x − 6)/8.
  - Put D := 8C. Then D² ≡ −90x² + 612x − 234 and D³ ≡ −2430x² + 16362x − 6372.
  - Hence 16h(C) = D³ − 36D² + 270D − 432 ≡ 0.
- The resultant correction holds, given the distinctness in MINOR-C. Since q is monic, Res_x(q, 24y − x(9−x)² + 24) = ∏_i 24(y − s(x_i)) = 13824·h/32 = 432h.
- Irreducibility: h ≡ 2y³ + y² + 3 (mod 5) takes the values 3, 1, 3, 1, 2. Rational-root denominators divide 32, so they are prime to 5.

**Lemma 4.2 (S00:429–434)**
- h′ = 96(y − 3/2)² − 81, so h′ ≥ h′(1/3) = 149/3 on [1/4, 1/3].
- h(1/4) = −7/4 and h(1/3) = 86/27.
- h(553/2000) = 0.676449508 − 11.009124 + 37.3275 − 27 = −1293623/250000000.
- With Δ3 ∈ (1/4, 1/3) and h(Δ3) = 0, strict monotonicity gives 553/2000 < Δ3.

**D1 chain**
- I_1 = v_cos via Lemma 2.4 on each cone plus Lemma 5.1 (S00:469, 596–599) is the correct citation.
- Tail: (Δ3 − ω²)/(1 + ω²) decreases in ω, and (16·553/2000 − 1)/17 = 428/2125 > 1007/5000.
- Witness:
  - I recomputed (m0, m1, m2) = (27, 62, 171)/74 via Lemma 5.2.
  - I recomputed them again via Lemma 5.3, with ψ = φ_e − π/2, X = 62/37, Y = −35/37 and a = 2.
  - SCV = 4617/3844 − 1 = 773/3844.
  - 773·5000 < 1007·3844, and 773·2125 = 1642625 < 1645232 = 428·3844.
- Lemma 5.5, exactly:
  - 2·3787·123215229403 − 26471369² = 232498770764161;
  - 26471369² = 700733376734161;
  - the quotient exceeds 33/100.
- Thm 5.6 attainment uses only the compact strip [1/4, 4] × [0, 2π], which contains (1, φ_e), plus strict tails.
- Cor 5.7 uses no Newton point. f_{ω_m,φ_m} is a genuine D1 law, since all three exponents contribute.
- Remark 5.6a: 21/104, the derivative −(5/2)ω/(1+ω²)², 21·3844 = 80724 > 80392 and the control 3/17 are all correct.

**D2 strictness**
- Cor 7.1(2):
  - φ_m ∈ [0, 2π) and θ1(0+) = 2π give feasibility for small r.
  - As r → 0, c → e^{−iφ} and ζ → (1 − iω)^{−1}. With m1 > 0, S_2 → v_cos.
- Cor 7.2:
  - Re(c e^{−ξt}) = e^{−δt}(Re c cos ωt − Im c sin ωt), so K = K_E. It is not the conic hull.
  - e^{−t}h_0 ∈ K, so K ≠ {0}.
  - The minimum over the fixed cone is attained on one of its own extreme rays (Lemma 2.4(1),(3); the base is compact by 2.1).
  - Those rays are exactly the feasible phases φ ∈ [0, θ1(r)], endpoints included (6.3, 6.4).
  - Strictness at the minimizing phase therefore suffices. No continuity or compactness in φ is used.
- No uniform gap is claimed, which is right: if I_2 = v_cos, then inf over cones of (min_K SCV − v_cos) = 0.
- Dual cones use the exact T = 11/50 > 773/3844 ≥ v_cos.

**Degenerations, padding and classification**
- Padding: (α,0)·diag(e^{At}, e^{−t})·(𝟙;1) = αe^{At}𝟙, so mass and density are unchanged.
- Real exponents with N ≤ 2 are handled by inclusion (Lemma 2.5).
- The confluent cases B1, B2 and C use confluent Hermite–Genocchi. D1 (δ = 0) has its own cone family.
- δ < 0 is excluded by the proved Lemma 1.2, not assumed:
  - a dominant pair gives K_E = K_{{λ0}} (S00:264);
  - a pair alone gives K_E = {0}.
- L1(a) takes arbitrary real (α, A): no sign conditions, non-minimal representations allowed, and non-contributing eigenvalues of any real part. It uses only that G = Pr(X ≥ t) is real, so even a complex-parameter convention gives the same class.

### 3. Flags
- **New error on the proof path:** none.
- **Unproved step:** none on the proof path. There is one unstated but derivable step in an unused remark (MINOR-C).
- **Silent restriction of the class:** none. "Continuous" is in the theorem statement, and orders 1–3, confluent cases and equal damping are all covered.
- **Reliance on a decimal v_cos:** none.
  - 0.2014 = 1007/5000, 0.2765 = 553/2000 and 0.33 enter only as rationals.
  - U, Theorem 5.8, the Newton value and the contract band are all off the proof path, as S00:805–806 says.

### Findings
**FATAL:** none. **MAJOR:** none.

**MINOR-A — S00:20–21, 469, 547: v_cos is never defined in this file.**
- S00:547 defers to "the contract".
- So the fix-map phrase "never 'by definition'" is inexact. Lemmas 2.4 and 5.1 give I_1 = inf_{ω,φ} SCV(f_{ω,φ}), and "= v_cos" is then exactly the definition.
- What is *not* definitional is SCV ≥ v_cos for a general D1 law, and that is now correctly proved.
- Repair: add to the §5 Setting (S00:464–465): "v_cos := inf_{ω>0, φ∈ℝ} SCV(f_{ω,φ}). By Lemma 1.4 and 1 − cos x = 2cos²(x/2 − π/2), it does not depend on the rate or on the cos² convention. It is attained by Thm 5.6." Reword S00:20–21 to match.

**MINOR-B — S00:553–554: the remark overstates what holds without Lemma 4.2.**
- "Theorem 5.6 also holds without Lemma 4.2" is literally false for two of Thm 5.6's clauses:
  - "773/3844 < 553/2000 < Δ3" (S00:525);
  - "ω ≤ 1/4 ⇒ SCV > 0.2014" (S00:526).
- On (1/5, 1/4] the hand bound is only 3/17, as S00:563 itself says.
- Repair: "Attainment, v_cos ≤ 773/3844 and the tails hold without Lemma 4.2, with 1/5 in place of 1/4 in both the window and the tail (there SCV > 21/104 > 0.2014), and with 773/3844 < 1/4 < Δ3."

**MINOR-C — S00:424–425: "Equivalently … = 432·h(y)" skips a step.**
- The remainder fact only shows that each s(x_i) is a root of h.
- To conclude ∏(y − s(x_i)) = h/32, the three values must also be pairwise distinct.
- That follows from part (3): strict monotonicity on [x1, x2] and [x2, x3] gives s(x1) < 1/3 < 1/2 < s(x3) < s(x2). Numerically these are about 0.2766, 0.9248 and 3.2986.
- The step is not stated, but no proof uses the remark.
- Repair: replace "Equivalently" with "Consequently, since (3) gives s(x1) < 1/3 < 1/2 < s(x3) < s(x2), …".

**MINOR-D — S00:27, 293 vs S00:534, 770: notation clash.**
- The fix map says the renames leave m_k only as a moment.
- But v4 uses m* (S00:534) and the new m_K (Cor 7.2, S00:770) for minimum values.
- Repair: rename them v* and v_K.

**Notes (no action required)**
- S00:777–778: "If the theorem holds, I_2 = v_cos is an unattained infimum" presupposes the strict D2 clause. Better: "even I_2 = v_cos would not decide whether a D2 law attains it, and it rules out a uniform gap."
- S00:339–340 (unchanged since v1): continuity in u alone does not bound ∫(1+t²)g_u uniformly. Cite Remark 2.3a(2), which supplies the majorant.
- SOURCE02:51–53 lists Lemma 5.1 as unchanged since v1, but SOURCE02:38 changes its statement (S00:467–469). This has no effect here, because I audited the final text.

### Audited vs imported

**Audited by hand in this pass:**
- every class-b hunk at its v4 lines;
- L4(1)–(4) and Lemma 4.2, including the mod-q identity and the resultant constant;
- irreducibility;
- all D1 rationals: 428/2125, 773/3844 by two routes, 21/104, 3/17, and Lemma 5.5's exact fraction;
- the algebra of Lemmas 5.3 and 5.4;
- the logic of Cor 5.7, 7.1, 7.2 and Remark 7.2a;
- positive mass and padding;
- re-checks of Lemma 1.2, L1(b) and the h′ formula in Lemma 6.2.

The remaining unchanged parts of L1–L3, Lemmas 5.1–5.2 and L6 rest on my v1 audit plus spot checks.

**Imported, or not verified here:**
- The 18-digit bracket (S00:445–447). Its endpoints differ by exactly 2⁻⁶⁰/12, one cell of 60 bisections of [1/4, 1/3], but I did not recompute the digits. No proof uses it.
- The receipts of exact-certs-v1, resultant-check-v1 and alt-route-check-v1. They are redundant with my hand checks on the proof path.
- All Arb, SymPy and float material (U, the θ1 table, the Newton point, the band, the ctl-* runs) and Theorem 5.8. All of it is off the proof path.
- The owner's Lemmas D and M, and the coverage of (0, ∞)² by the (δ, ω) chart assignment.
- The requirement that Lemma M compares against the exact v_cos, or an exact constant ≥ 773/3844, and never against U or Theorem 5.8. My v1 note recorded that the owner's S00:112 used the exact v_cos; I did not re-check it.
- The owner-side loci of old MINOR-3 and MINOR-5, and STATUS-v4.
- Imports I1–I8, and all hashes.
