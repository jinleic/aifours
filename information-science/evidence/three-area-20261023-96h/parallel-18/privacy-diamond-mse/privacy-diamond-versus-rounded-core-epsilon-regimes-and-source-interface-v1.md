# Diamond versus rounded optimal core: explicit epsilon regimes and the exact SOURCE-MATCH-U1 consequence

Owner InfoResearch96h-2, original info-1. Actual `/bin/date` observed before this file was first written: **Tue Oct 27 06:38:43 PDT 2026**. Status: **AUTHOR-WRITTEN, UNREVIEWED** registered-mathematics and source-interface packet, written PROSPECTIVELY under `institute/runs/three-area-2026-10-23-96h/PH-privacy-complete-whole-read-and-qualified-original-directions-v207.json` (SHA256 12542cf8dafc02c4699a7f69d334d405eb2cf9a44b38f7c01b3a81ddb4b2e8f8, read complete before this work). This packet is written reasoning only. It is not a parent adoption, an independent review, or formal, kernel, executable, priority or novelty acceptance.

## 0. Imports, exclusions and what is new

**Named imports, used only at their recorded adopted scopes (not re-proved here):**
- LAW642: `privacy-all-law-optimum-self-contained-v1.md` (SHA256 957cab2b…7e53). Used: §1 (unique optimal law and the core form S_*), §6 (ZN formulas), §8.1–§8.5. From §8 this packet uses:
  - CLIP, and H(t, λ) = N − λZ with its unique zero W = V;
  - the diamond-regime boundary t_D(λ) = (sqrt(λ − v) − m)/2;
  - the cubic DC and its sign pattern (+, −, +), positive at t = 0 even at λP;
  - in the rounded regime, H_tt > 0 and derivative continuity at the junction;
  - a positive derivative in the lower-clip regime;
  - uniqueness;
  - 0 < d = t < 1/2 in the diamond case;
  - the screened D/R systems.
- NORM148: `privacy-all-norm-radial-attainment-rigidity-gap-v1.md` (SHA256 7100908e…d405), at its adopted scope. Over ALL norms, ALL nonnegative Borel radial profiles and arbitrary centres, the infimum equals V iff the actual core is homothetic to D. At each epsilon whose actual core has a genuine rounded arc it is STRICTLY larger than V.
- Only for the overlap remark in §6(ii): the MDA per-cost interface as recorded in the adopted MDA parent (`RUN/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA256 75614a6f…76ac3). There, every extended nondecreasing matching-norm cost has an attaining matching-norm staircase among ALL laws. **Reading used (named interface):** that attaining staircase is radial in the matching norm (here the l1 norm).

**Not used, opened or repaired:** the withdrawn ENTIRE116 calibration file and every calibration/selection/method guide; cp102/AD33; cp108; the v156 review bodies; old evaluated tables, decimals or controls. No chosen epsilon, state, control, boundary or decimal probe enters any proof. Every statement below is for whole parameter ranges. Machine checks: none. Every identity was expanded by hand, and the expansions are displayed.

**What is new relative to the record:** NORM148 explicitly records "no epsilon allocation, proof that a rounded regime occurs". LAW642 states the D/R dichotomy but allocates no epsilon. This packet proves three things:
1. an exact screen identity;
2. a diamond regime for all ε ≤ ln((5 + √33)/2);
3. a rounded regime for all ε ≥ ln(2^18 + 1).

It then derives the regime-separated SOURCE-MATCH-U1 consequences. The band between the two thresholds is NOT allocated here.

## 1. Notation

- 0 < b < 1 with ε = −ln b, and m = b/(1 − b).
- G is geometric with P(G = k) = (1 − b)b^k, so E binom(G, j) = m^j. Hence:
  - EG = m;
  - T2 = EG² = m + 2m²;
  - T3 = EG³ = m + 6m² + 6m³;
  - T4 = EG⁴ = m + 14m² + 36m³ + 24m⁴;
  - v = m + m²;
  - λP = T4/(3T2).
- For q ≥ 0 put M_r(q) = E(G + q)^r, so M_r' = r·M_{r−1}:
  - M1 = q + m;
  - M2 = q² + 2mq + T2;
  - M3 = q³ + 3mq² + 3T2·q + T3;
  - M4 = q⁴ + 4mq³ + 6T2·q² + 4T3·q + T4.
- For a diamond core qD (LAW642 §8.2): J_D(q) = M4(q)/(3M2(q)).
- Hence J_D'(q) = 2P_m(q)/(3M2(q)²), where P_m = 2M3·M2 − M4·M1 is the printed polynomial (D) of LAW642 §8.5.
- From (D): P_m(0) = m²(1 + 2m) > 0 and P_m(1) = 1 + 4m + 5m² + 2m³ = (1 + m)²(1 + 2m) > 0. The last expansion: 1 + 5m + (2m + 12m²) + (12m³ − 2m) − (m + 8m² + 12m³) + m² + 2m³ collects to 1 + 4m + 5m² + 2m³.
- J_D(0) = T4/(3T2) = λP. The core-D law equals the point-core law a.e. (LAW642 §8.2), so J_D(1) = λP as well.

## 2. Lemma 1 — exact screen identity

Put

    Q(q) = −q³ − 3mq² + 3mq + 2m + 9m² + 6m³.

**Claim.** 2M3 − 3M1·M2 = Q. Hence, at every q with P_m(q) = 0, the LAW642 D-branch screen λ = M4/(3M2) ≥ M2 = q² + 2mq + T2 holds iff Q(q) ≥ 0.

**Proof.** We have 2M3 = 2q³ + 6mq² + 6T2·q + 2T3 and 3M1·M2 = 3q³ + 9mq² + (3T2 + 6m²)q + 3mT2. Subtracting gives −q³ − 3mq² + (3T2 − 6m²)q + (2T3 − 3mT2). Here 3T2 − 6m² = 3m, and 2T3 − 3mT2 = 2m + 12m² + 12m³ − 3m² − 6m³ = 2m + 9m² + 6m³.

If P_m(q) = 0 then M4 = 2M3·M2/M1, so M4 ≥ 3M2² ⇔ 2M3 ≥ 3M1·M2 (M1, M2 > 0). ∎

Q is strictly concave on [0, ∞), since Q'' = −6q − 6m < 0, and Q(0) = 2m + 9m² + 6m³ > 0. Hence if Q(q1) < 0 for some q1 > 0, then Q < 0 on [q1, ∞). Indeed, for q > q1 concavity gives Q(q1) ≥ (1 − q1/q)Q(0) + (q1/q)Q(q), so Q(q) ≥ 0 would force Q(q1) > 0.

## 3. Lemma 2 — the diamond case is exactly a screened minimizer of J_D

(a) **Existence.** J_D is smooth on [0, 1], with J_D(0) = J_D(1) = λP, J_D'(0) > 0 and J_D'(1) > 0. It therefore exceeds λP just right of 0 and is below λP just left of 1. Every minimizer q* of J_D on [0, 1] lies in (0, 1), with P_m(q*) = 0 and J_D(q*) < λP.

(b) **Necessity.** Suppose the optimal core is a diamond q_o·D. LAW642 §8.4 gives 0 < q_o = 2t_o < 1. Then:
- W = V = J_D(q_o) ≤ J_D(q) for every q ∈ (0, 1), since every diamond core is a canonical competitor. So q_o minimizes J_D on (0, 1) and P_m(q_o) = 0.
- The CLIP profile is the full facet, so R_W(0) ≥ 2t_o, i.e. W ≥ (2t_o + m)² + v = M2(q_o).
- By Lemma 1, Q(q_o) ≥ 0.

(c) **Sufficiency.** Let q* ∈ (0, 1) satisfy P_m(q*) = 0, λ0 := J_D(q*) < λP and Q(q*) ≥ 0. Then W = λ0, and the unique optimal core is q*·D.

Proof of (c). Put t* = q*/2.
- By Lemma 1, λ0 ≥ M2(q*). This is exactly t* ≤ t_D(λ0), since (q* + m)² + v = M2(q*). So [0, t*] lies in the diamond regime, where H(t, λ0) = H_D(t) = (2/3)M4(2t) − 2λ0·M2(2t).
- dH_D/dt = (16/3)M3 − 8λ0·M1, which vanishes at q* because λ0 = M4/(3M2) = 2M3/(3M1) there. Also H_D(t*) = 0, while H_D(0) = (2/3)T4 − 2λ0·T2 > 0 because λ0 < λP.
- By LAW642 §8.4 the DC derivative is positive at t = 0 and has the pattern (+, −, +) with at most two positive zeros. If t* were the first zero, H_D would increase on [0, t*], contradicting H_D(t*) = 0 < H_D(0). So t* is the second zero, and H_D ≥ min(H_D(0), H_D(t*)) = 0 on [0, t*].
- For t ≥ t*, LAW642 §8.4 applies: after a diamond minimum the derivative stays positive to the junction; it then increases in the rounded regime (H_tt > 0); and the lower-clip regime has positive derivative (§8.3). So H(·, λ0) ≥ 0 everywhere, with value 0 at t*.
- Since min_t H(t, λ) is strictly decreasing in λ with unique zero W (§8.1), W = λ0.
- LAW642's uniqueness makes the CLIP core at (t*, λ0), the full diamond q*·D, the unique optimal core. Distinct q ∈ (0, 1) give distinct laws, so q* is the unique minimizer of J_D on (0, 1). ∎

## 4. Theorem A — diamond regime for ε ≤ ln((5 + √33)/2)

**Identity.** With m = b/(1 − b):

    6m³ + 9m² + 2m − 1 = (2b² + 5b − 1)/(1 − b)³.

Proof by multiplying out: 6b³ + 9b²(1 − b) + 2b(1 − b)² − (1 − b)³. The b³ coefficients 6 − 9 + 2 + 1 cancel; the b² coefficient is 9 − 4 − 3 = 2; the b coefficient is 2 + 3 = 5; the constant is −1.

**Theorem A.** Suppose 2b² + 5b − 1 ≥ 0, i.e. b ≥ (√33 − 5)/4, i.e. ε ≤ ln((5 + √33)/2). In particular this holds whenever ε ≤ ln 5 (b ≥ 1/5, m ≥ 1/4). Then the unique optimal law is the homothetic-diamond (l1-radial) staircase

    p_*(z) = Z^(−1) b^ceil((|z|_1 − q*)_+),

where q* ∈ (0, 1) is the unique minimizer of J_D on (0, 1). Its value is V = M4(q*)/(3M2(q*)). The screen holds strictly: V > M2(q*), so the rounded constraint is inactive on the whole core.

**Proof.** For q ∈ (0, 1):

    Q(q) = (6m³ + 9m² + 2m) + 3mq(1 − q) − q³ > 6m³ + 9m² + 2m − 1 ≥ 0,

since q³ < 1. Take a minimizer q* from Lemma 2(a). Then Lemma 1 gives the strict screen, and Lemma 2(c) applies. The index min{k ≥ 0 : z ∈ (q* + k)D} equals ceil((|z|_1 − q*)_+). ∎

## 5. Theorem B — rounded regime for ε ≥ ln(2^18 + 1)

**Theorem B.** If 0 < m ≤ 2^(−18), i.e. ε ≥ ln(2^18 + 1), the optimal core is NOT a diamond. By LAW642 §8.3 it is "an arc followed by a NONZERO upper facet", so the actual core has a genuine rounded arc. By NORM148 at its adopted scope, V is then STRICTLY smaller than the infimum over all norm-radial laws (every norm, every nonnegative Borel radial profile, every centre).

**Proof.** Suppose instead that the optimal core is a diamond q_o·D. By Lemma 2(b), q_o minimizes J_D on (0, 1) and Q(q_o) ≥ 0.

*Step 1 — Q(q_o) ≥ 0 forces q_o < (3/2)m^(1/3).* Drop −3mq² ≤ 0 and put q1 = (3/2)m^(1/3) ≤ 3/8:

    Q(q1) ≤ m[−27/8 + 2 + (9/2)m^(1/3) + 9m + 6m²].

For m ≤ 1/64 the bracket is at most −11/8 + 9/8 + 9/64 + 6/4096 < 0. Concavity (Lemma 1) then makes {q > 0 : Q(q) ≥ 0} lie in (0, q1).

*Step 2 — a lower bound on (0, q1).* Here M4(q) ≥ T4 ≥ m and M2(q) ≤ M2(q1) = m^(2/3)[9/4 + 3m^(2/3) + m^(1/3) + 2m^(4/3)]. For m ≤ 2^(−12) (m^(1/3) ≤ 1/16) the bracket is below 9/4 + 3/256 + 1/16 + 2/65536 < 75/32. Hence

    J_D(q) ≥ (32/225)·m^(1/3)   for every q ∈ (0, q1).

*Step 3 — an upper bound at s = m^(1/4) ∈ (0, 1).* M2(s) ≥ s², and

    M4(s) = 2m + 4m^(5/4) + 6m^(3/2) + 4m^(7/4) + 14m² + 24m^(9/4) + 12m^(5/2) + 24m^(13/4) + 36m³ + 24m⁴.

The terms come from q⁴ = m, 4mq³, 6T2·q², 4T3·q and T4. So

    3J_D(s) ≤ M4(s)/s² = 2m^(1/2)[1 + 2s + 3s² + 2s³ + 7s⁴ + 12s⁵ + 6s⁶ + 18s⁸ + 12s⁹ + 12s¹²].

For s ≤ 1/8 (m ≤ 2^(−12)) we have 2s ≤ 1/4, and the remaining terms after 1 + 2s sum to less than 1/16 (3/64 + 2/512 + 7/4096 + 12/32768 + … < 4/64). The bracket is therefore below 21/16, and J_D(s) ≤ (7/8)·m^(1/2).

*Step 4 — contradiction.* (32/225)m^(1/3) > (7/8)m^(1/2) ⇔ m^(1/6) < 256/1575. For m ≤ 2^(−18), m^(1/6) ≤ 1/8 < 256/1575, since 1575 < 2048. Then J_D(q_o) ≥ (32/225)m^(1/3) > J_D(s), contradicting the minimality of q_o.

Finally, m ≤ 2^(−18) ⇔ b ≤ 1/(2^18 + 1). ∎

## 6. Exact SOURCE-MATCH-U1 consequences, regime by regime

T-MATCH is as frozen in `privacy-current-source-equivalence-priority-ledger-v1.md` §1: the actual global value and selector, all-law minimization, and unique-law equality, at the same quantifiers.

**(i) Rounded regime, ε ≥ ln(2^18 + 1): statement-level separation.** By Theorem B and NORM148, at every such ε the infimum over the entire norm-radial class is strictly larger than V. Therefore no source CONCLUSION whose optimal, attaining or equality law lies in a norm-radial class can instantiate T-MATCH at those ε, whatever its proof. The first failed implication is that the claimed optimizer class excludes the unique optimal law. This covers, at the level of those statements:
- the homothetic l1 staircases of G13/G15;
- the matching-norm staircase optimizers of K25 and MDA;
- the product Laplace law of KHP (l1-radial);
- K-norm mechanisms (AS21, JY24; radial in the K-norm);
- spherical generalized-gamma laws (Wei; Euclidean-radial);
- Gaussian programs (DA26; radial in an ellipsoidal norm, and infeasible for pure DP anyway).

It does NOT separate:
- SCDF's arbitrary-core shell family, which contains the optimal law at the ledger's LAW642 + BRANCH-OLD conditional family-inclusion cut;
- EG's general framework/attainment;
- the broad R2DP/UDP-FL templates.

Their positive PRIOR credit is unchanged. Unread ranges of partially read sources are covered only for statements of this norm-radial form; any other content there remains uncovered.

**(ii) Diamond regime, ε ≤ ln((5 + √33)/2): positive overlap INCREASES; the gap is exactly one mixed-cost inequality.**

By Theorem A the unique optimal law μ_* is l1-radial and lies in G13's homothetic staircase family. So G13's dated suggestion, squared-Euclidean optimality of its homothetic family, has an AFFIRMATIVE answer at these ε (by LAW642 + Theorem A, not by any source). For the same family the answer is NEGATIVE in the rounded regime (i).

For every l1-radial feasible law ν the conditional law on {|z|_1 = r} is uniform along the facets, so E_ν|Z|_2² = (2/3)·E_ν|Z|_1². Hence V = (2/3)·inf over l1-radial feasible laws of E|Z|_1², attained exactly at μ_*.

At the named MDA per-cost interface (cost r ↦ r², attaining staircase radial in the l1 norm), the all-law infimum V1 of E|Z|_1² is attained by an l1-radial law, so V = (2/3)·V1. Every l1-radial V1-optimizer ν has E_ν|Z|_2² = V, so ν = μ_* by LAW642 uniqueness. Thus, in this regime, the squared-Euclidean optimizer COINCIDES with the all-law optimizer for the same-norm cost |z|_1², a positive PRIOR same-norm object at the MDA interface.

What no inventoried source supplies is the MIXED-cost all-law lower bound:

    E_μ|Z|_2² ≥ (2/3)·V1 for EVERY feasible μ, with equality only at μ_*.

This is the first failed implication for G13/G15, K25 and MDA: their conclusions concern costs that are functions of |z|_1 (or its mean), while |z|_2² is not. Pointwise, |z|_2²/|z|_1² ranges over [1/2, 1] (axes versus diagonals). So for a law that is not l1-radial, no inequality between E|Z|_2² and (2/3)·E|Z|_1² follows from same-norm stochastic domination alone, and that domination cannot yield this bound. In this regime SOURCE-MATCH-U1 is therefore EXACTLY that inequality with its equality case. LAW642 proves it; no source in the recorded inventory has been located that states or implies it.

**(iii) Unallocated band.** For ln((5 + √33)/2) < ε < ln(2^18 + 1), this packet does not determine whether the core is D or R. No claim is made there.

**(iv) Scope.** This packet does NOT:
- locate a T-MATCH source;
- prove worldwide absence;
- establish firstness or novelty;
- clear any partially read source range;
- supply a parent adoption.

The positive PRIOR credit recorded in the ledger (SCDF mechanisms, EG framework, G13/G15 question and family, K25/MDA same-norm optimality, Amir–Rietzke, generic tools) stands. Case (ii) ADDS overlap: the optimizer identity with the same-norm |z|_1² optimizer at the MDA interface. Any defect in LAW642 §8 or NORM148 propagates to Theorems A/B and to §6. The diamond-regime statement contradicts nothing adopted; NORM148 disclaimed allocation, and LAW642 already allowed the D case.

## 7. Process

Inputs: complete v207 read; own ledger (195 LF) read complete; LAW642 §1, §6 and §8 read; NORM148 and the MDA parent used only as recorded in the ledger and its pins. Every computation is a hand expansion of exact polynomials or a rational inequality displayed above. There was no interpreter, Eval, calculator, CAS, program, enumeration, solver, replay, CLI, nested agent, new GO, timer or poll. Same 18/OWN/HOLD/immutable. All earlier findings and ZERO quarantines are unchanged. Science cutoff 2026-10-27T11:05:38-07:00.
