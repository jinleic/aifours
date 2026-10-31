# Exact single-threshold ε-allocation: diamond versus rounded optimal core (successor v2)

Owner InfoResearch96h-2, original info-1. Actual `/bin/date` observed before this file was first written: **Tue Oct 27 06:47:31 PDT 2026**. Status: **AUTHOR-WRITTEN, UNREVIEWED** registered-mathematics packet under v207 (`institute/runs/three-area-2026-10-23-96h/PH-privacy-complete-whole-read-and-qualified-original-directions-v207.json`, SHA256 12542cf8…e8f8). It is a NEW successor file. The pinned v1 `privacy-diamond-versus-rounded-core-epsilon-regimes-and-source-interface-v1.md` (SHA256 050e469fefae84205b273a71e79f587e106f7e0d6b6e427875d6a2b14695d450) is not edited. v1's Theorems A and B become corollaries of the exact criterion below, and its §6 source consequences carry over with the exact threshold.

Written reasoning only; no interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. Every polynomial identity is expanded by hand below and checked at stated parameter values by exact integer arithmetic. No decimal, chosen state, control or calibration enters any premise.

**Imports.** The imports and exclusions are those of v1 §0:
- LAW642 §1, §6, §8.1–§8.5 and NORM148, at their adopted scopes;
- the MDA per-cost interface, only for corollary (iii) of §7;
- ENTIRE116, cp102/AD33, cp108, all calibration/selection guides and the v156 bodies are NOT used or opened.

## 1. Notation

The notation is as in v1 §1:
- m = b/(1 − b), b = e^(−ε);
- T2 = m + 2m², T3 = m + 6m² + 6m³, T4 = m + 14m² + 36m³ + 24m⁴;
- M_r(q) = E(G + q)^r;
- J_D(q) = M4(q)/(3M2(q)), with J_D' = 2P_m/(3M2²), where P_m = 2M3M2 − M4M1 is LAW642 (D):

      P_m(q) = q⁵ + 5mq⁴ + (2m + 12m²)q³ + (12m³ − 2m)q² − (m + 8m² + 12m³)q + m² + 2m³.

New abbreviations:

    Q(q) = 2M3 − 3M1M2 = −q³ − 3mq² + 3mq + 2m + 9m² + 6m³        (v1 Lemma 1)
    v = m + m² = m(1 + m) = b/(1 − b)² = 1/(4·sinh²(ε/2)),    s = sinh²(ε/2) = 1/(4v).

The last identity holds because b/(1 − b)² = 1/(e^(ε/2) − e^(−ε/2))².

## 2. Lemma A — the D-family function has exactly two critical points

The coefficient signs of P_m are (+, +, +, sign(6m² − 1), −, +). There are exactly two sign changes whatever the middle sign (a zero coefficient is skipped). By Descartes' rule, P_m has at most two positive roots, counted with multiplicity.

J_D is smooth on [0, 1] with J_D(0) = J_D(1) = λP (v1 §1). Also J_D'(0) > 0 and J_D'(1) > 0, since P_m(0) = m²(1 + 2m) and P_m(1) = (1 + m)²(1 + 2m). So J_D decreases somewhere in (0, 1). Hence P_m has exactly two positive roots q_a < q*, both in (0, 1), with:
- P_m > 0 on (0, q_a) ∪ (q*, ∞) and P_m < 0 on (q_a, q*);
- J_D increasing on (0, q_a), decreasing on (q_a, q*), increasing on (q*, ∞).

So q* is the UNIQUE minimizer of J_D on [0, 1], and J_D(q*) < J_D(1) = λP.

Moreover P_m(2m) = m²(256m³ − 8m² − 22m − 1). The expansion: q⁵ → 32m⁵; 5mq⁴ → 80m⁵; the q³ term → 16m⁴ + 96m⁵; the q² term → 48m⁵ − 8m³; the q term → −2m² − 16m³ − 24m⁴; constant m² + 2m³. For 0 < m ≤ 1/4 we have 256m³ ≤ 16m < 22m, so P_m(2m) < 0 and therefore q_a < 2m < q*.

## 3. Lemma B — the diamond case is EXACTLY Q(q*) ≥ 0

This is v1 Lemma 2 with the uniqueness of Lemma A.
- **Necessity.** If the optimal core is a diamond q_o·D, then q_o minimizes J_D on (0, 1), so q_o = q*. LAW642 CLIP gives W ≥ M2(q*). By the screen identity, Q(q*) ≥ 0.
- **Sufficiency.** If Q(q*) ≥ 0, then W = J_D(q*), and the unique optimal core is q*·D. This uses LAW642 §8.1/§8.3/§8.4 exactly as in v1 Lemma 2(c).

(If Q(q*) = 0, the junction is c = 0 and the core is still the full diamond.)

## 4. Lemma C — exact division identity

    P_m(q) = −(q² + 2mq + 5m + 6m²)·Q(q) + R(q),
    R(q) = m(1 + m)·[(12m² + 12m − 1)·q + m(36m² + 48m + 11)].

**Derivation.** Expand (q² + 2mq + a)(q³ + 3mq² − 3mq − c0), with a = 5m + 6m² and c0 = 2m + 9m² + 6m³. The coefficients are:
- q⁵: 1;
- q⁴: 5m;
- q³: −3m + 6m² + a = 2m + 12m²;
- q²: −c0 − 6m² + 3ma = −2m + 12m³;
- q¹: −2mc0 − 3ma = −19m² − 36m³ − 12m⁴;
- q⁰: −a·c0 = −10m² − 57m³ − 84m⁴ − 36m⁵.

The q⁵ through q² coefficients agree with P_m exactly. The remainders are therefore:
- linear: −(m + 8m² + 12m³) + 19m² + 36m³ + 12m⁴ = −m + 11m² + 24m³ + 12m⁴ = m(1 + m)(12m² + 12m − 1);
- constant: m² + 2m³ + 10m² + 57m³ + 84m⁴ + 36m⁵ = m²(36m³ + 84m² + 59m + 11) = m²(1 + m)(36m² + 48m + 11).

**Checks.**
- At q = 0: −(5m + 6m²)·c0 + m²(1 + m)(36m² + 48m + 11) = m² + 2m³ = P_m(0).
- At q = 1: (1 + 7m + 6m²)(1 − 2m − 9m² − 6m³) = 1 + 5m − 17m² − 81m³ − 96m⁴ − 36m⁵, and R(1) = 36m⁵ + 96m⁴ + 83m³ + 22m² − m. Their sum is 1 + 4m + 5m² + 2m³ = P_m(1).

Since q² + 2mq + 5m + 6m² > 0 for q ≥ 0, at every positive root q of P_m:

    sign Q(q) = sign R(q).                                           (S)

## 5. Lemma D — the threshold polynomial

Let N = 36m² + 48m + 11 and Dn = 1 − 12m − 12m² = 1 − 12v. Clearing Dn³ in Q(mN/Dn) gives m·G(m), with

    G = −m²N³ − 3m²N²Dn + 3mN·Dn² + (2 + 9m + 6m²)Dn³.

Hand expansion:
- N² = 1296m⁴ + 3456m³ + 3096m² + 1056m + 121;
- N³ = 46656m⁶ + 186624m⁵ + 291600m⁴ + 224640m³ + 89100m² + 17424m + 1331;
- Dn² = 1 − 24m + 120m² + 288m³ + 144m⁴;
- Dn³ = 1 − 36m + 396m² − 864m³ − 4752m⁴ − 5184m⁵ − 1728m⁶.

Coefficient sums check these at m = 1: 9025 = 95², 857375 = 95³, 529 = 23², −12167 = (−23)³. Collecting the four products gives

    G = 2 − 30m − 1868m² − 14004m³ − 46728m⁴ − 84672m⁵ − 86400m⁶ − 46656m⁷ − 10368m⁸.

Direct substitution checks this at three points:
- m = 1: both forms give −290724;
- m = −1: both give 0;
- m = −1/2: both give 0.

Exact long division by 2m² + 3m + 1 = (2m + 1)(m + 1) leaves zero remainder:

    G = (2m² + 3m + 1)·K,   K = 2 − 36m − 1764m² − 8640m³ − 17280m⁴ − 15552m⁵ − 5184m⁶.

K collapses in v = m² + m, using (m² + m)³ = m⁶ + 3m⁵ + 3m⁴ + m³ and (m² + m)² = m⁴ + 2m³ + m²:

    −K = 5184v³ + 1728v² + 36v − 2.

Finally, with v = 1/(4s) and multiplying by s³ > 0:

    −K·s³ = 81 + 108s + 9s² − 2s³.

## 6. THEOREM — exact allocation

Let s = sinh²(ε/2). For every finite ε > 0:

    the unique optimal core is the FULL diamond q*·D   ⇔   2s³ − 9s² − 108s − 81 ≤ 0.

Otherwise the core has a genuine rounded arc ("an arc followed by a NONZERO upper facet", LAW642 §8.3). The cubic has coefficient signs (+, −, −, −), so it has exactly one positive root s_t; it is negative on (0, s_t) and positive on (s_t, ∞). Since s increases strictly with ε, there is EXACTLY ONE transition:

    D (diamond)  ⇔  ε ≤ ε_t := 2·arcsinh(√s_t),   R (rounded)  ⇔  ε > ε_t.

**Closed form.** s_t = 3/u_t, where u_t is the unique positive root of 3u³ + 12u² + 3u − 2 = 0 (substitute u = 3/s). Trigonometric Cardano on the depressed cubic y³ − (13/3)y + 74/27 = 0, with u = y − 4/3, gives

    u_t = (2√13/3)·cos( (1/3)·arccos(−37/(13√13)) ) − 4/3.

**Proof.**
- **Case v ≥ 1/12, i.e. s ≤ 3.** Then 12m² + 12m − 1 = 12v − 1 ≥ 0, so R(q) > 0 for every q > 0. By (S), Q(q*) > 0, and Lemma B gives D. Consistently, the cubic is negative here: 2s³ ≤ 54 < 81.
- **Case v < 1/12.** Then Dn > 0. Put q_c = mN/Dn ≥ 11m > 2m > q_a (Lemma A), so q_c is the unique positive zero of R, and R > 0 exactly on (0, q_c).
  - By (S) at q*: Q(q*) ≥ 0 ⇔ q* ≤ q_c.
  - By Lemma C at q_c: P_m(q_c) = −(positive)·Q(q_c).
  - Because q_c > q_a and the sign pattern of Lemma A holds: q_c ≥ q* ⇔ P_m(q_c) ≥ 0 ⇔ Q(q_c) ≤ 0.
  - By Lemma D, Q(q_c) has the sign of G, hence of K (since 2m² + 3m + 1 > 0), hence of 2s³ − 9s² − 108s − 81.
  
  Lemma B then gives D ⇔ cubic ≤ 0.
- **Rounded case and NORM148.** When the cubic is positive, Lemma B's necessity excludes the diamond. By LAW642 §8.3 the core is an arc plus a nonzero upper facet; the arc is genuine, so NORM148 gives the strict norm-radial gap. ∎

**Corollaries.**
- v1 Theorem A: D for ε ≤ ln((5 + √33)/2).
- v1 Theorem B: R for ε ≥ ln(2^18 + 1).
- New: D for all ε ≤ 2·ln(2 + √3) (the case s ≤ 3; 2·arcsinh(√3) = 2·ln(2 + √3)).

## 7. Exact consequences for SOURCE-MATCH-U1 (successor of v1 §6)

(i) **G13's dated question, now answered exactly.** The ledger records that G13 suggested squared-Euclidean optimality of its homothetic l1-staircase family. At LAW642 + this Theorem, the answer is:
- AFFIRMATIVE exactly for ε ≤ ε_t: the unique optimum is the homothetic staircase p ∝ b^ceil((|z|_1 − q*)_+), with V = M4(q*)/(3M2(q*)) and q* the larger positive root of P_m;
- NEGATIVE exactly for ε > ε_t.

This is a mathematical answer at the adopted cut. It is not a source-priority finding.

(ii) **Norm-radial separation holds iff ε > ε_t.** NORM148 says the norm-radial infimum equals V iff the actual core is homothetic to D. By the Theorem this happens exactly for ε ≤ ε_t. For ε > ε_t, every source conclusion whose optimal, attaining or equality law is norm-radial is strictly separated from T-MATCH (list as in v1 §6(i): G13/G15, K25, MDA, KHP, AS21/JY24 K-norm, Wei SGG, DA26 Gaussian). For ε ≤ ε_t NO such separation exists. SCDF, EG and the broad templates are never separated by this argument.

(iii) **Diamond regime overlap and the exact remaining gap.** For ε ≤ ε_t:
- E|Z|_2² = (2/3)E|Z|_1² on l1-radial laws, so V = (2/3)·(the l1-radial infimum of E|Z|_1²), attained only at μ_*.
- At the MDA per-cost interface (cost r ↦ r², attaining staircase l1-radial), V = (2/3)V1, and μ_* is the l1-radial optimizer of E|Z|_1² over ALL laws. This is a positive PRIOR same-norm object; the overlap is larger than previously recorded.
- The only SOURCE-MATCH-U1 implication still missing there is the mixed-cost all-law bound E_μ|Z|_2² ≥ (2/3)V1 for every feasible μ, with equality only at μ_*.

For ε > ε_t, T-MATCH additionally requires the rounded-core selector (LAW642 R-system). No norm-radial source can supply it.

(iv) **Scope.** This packet does NOT:
- locate a T-MATCH source;
- prove worldwide absence;
- make any claim of firstness, novelty or major-contribution;
- clear any partially read source range;
- constitute a parent adoption.

Defects in LAW642 §8 or NORM148 propagate here. The threshold is an exactly defined algebraic quantity. No decimal value is asserted or used, and no chosen-parameter evaluation enters any proof; the only point evaluations are the identity checks in §4 and §5. Positive PRIOR credit (SCDF, EG, G13/G15, K25/MDA, Amir–Rietzke, generic tools) is unchanged and, in the diamond regime, enlarged.

## 8. Process

Inputs and methods are as in v1 §7. All arithmetic is by hand: polynomial expansions, two exact remainder checks and four exact coefficient-sum checks. Same 18/OWN/HOLD/immutable. All earlier findings and ZERO quarantines are unchanged. Science cutoff 2026-10-27T11:05:38-07:00.
