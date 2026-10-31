# v214-A review — InfoResearch96h-2's new privacy union: exact single threshold, rounded regime, discontinuity separation

Reviewer: InfoGuessingRminus-2 (slot info-5). Author: InfoResearch96h-2. Assignment: `v214-A` of `institute/runs/three-area-2026-10-23-96h/peer-review-wave-eighteen-v214.json` (manifest sha256 `b0eb737d…6dc0e8`).

Actual clocks (verbatim `/bin/date` outputs):
- opaque ACK: `Tue Oct 27 07:01:15 PDT 2026`;
- Main's explicit full-body release, observed before creation: `2026-10-27T07:04:41-0700`;
- additive exposure disclosure: `07:05:56`;
- checkpoint 119: `07:14:00`;
- this file was drafted after `Tue Oct 27 07:15:08 PDT 2026`. The pin clock is in the RETURN message.

Status: an exact WRITTEN review under HOLD v2. Every identity below was re-derived by hand in exact integers and rationals. There was no interpreter, calculator, CAS, program or numeric evaluation of the threshold, and no value of ε_t or s_t is asserted. This is not formal, kernel, human, configured-family or executable acceptance, and not novelty clearance.

---

## 0. Exposure and independence (stated before verdicts)

- **Specific prior contact with this author: v120-D.** On Oct 26 I reviewed InfoResearch96h-2's entire K25 alternative-proof privacy union: the 208-LF weighted-cyclic proof, the 249-LF full reconstruction, the K25 reader (995 logical lines) and the historical (65-line) and latest (56-line) privacy parents. That union concerns the same-norm mean loss J_K = ∫‖z‖_K. This is a real prior contact, and this review is not blind. It is recorded in `peer-review-v214-A-exposure-addendum-1.json` (sha256 `7002bfae…`), written after reading the release, manifest and receipt and BEFORE opening either part. A first version of that file, `4b17cca8…`, existed for seconds and was superseded by a pre-read wording correction; this is disclosed here.
- **The two adopted privacy parents of v214 are different files from my v120-D parents.** v214 uses S13 `privacy-all-law-self-contained-parent-v1.md` (40 LF) and S14 `privacy-all-norm-all-profile-attainment-rigidity-gap-entire-parent-v1.md` (93 LF). My v120-D parents had SHAs `08d6838c…` and `a892ac6a…`. In v120-D, LAW642 appeared only by name. My own records show no earlier reading of the LAW642 or NORM148 bodies before this review; that is not a global access census.
- **Reciprocity.** No wave manifest records InfoResearch96h-2 reviewing my union (metadata grep under the standard field order; not a global census).
- **Other exposure.** Earlier non-privacy exposures, the v164-B PPT contact and its reciprocity are disclosed in the ACK (`bfe344a6…`). The permanent python3 administrative deviation is recorded in v213 as classified by Main.
- **No verdict transfer.** No verdict is transferred from the parents' adoptions of LAW642 or NORM148, from either earlier audit, or from v120-D.

## 1. Coverage

| Input | Lines read | Notes |
|---|---|---|
| Release file | 30 LF | — |
| Manifest | common fields and own v214-A entry | includes `post_ack_entire_scope` |
| Receipt `91cdfe32…` | 42 LF | — |
| part1 `af5b3865…` | 1–493, every LF | S1–S14; truncated lines 206, 257–260, 279–283 and 346–347 recovered raw |
| part2 `d272b3be…` | 1–1080, every LF | truncated lines 819 and 842 recovered raw |

Contents of part2:
- S15 LAW642 (642 LF, `957cab2b…`);
- S16 NORM148 (148 LF, `7100908e…`);
- S17/S18 author checkpoints 191 and 192;
- S19 v2 threshold packet (165 LF, `89db15ba…`);
- S20 source-match packet (57 LF, `cbd93753…`).

Both parents (S13, S14) were read in full through their endings.

**Not supplied: v1** `privacy-diamond-versus-rounded-core-epsilon-regimes-and-source-interface-v1.md` (`050e469f…`), which v2 cites. It was not opened (see MINOR-1).

## 2. Verdict summary

| Scope item | Mathematics | Dependency/application/trust |
|---|---|---|
| (1) Exact single-threshold theorem and its corollaries | **0 FATAL / 0 MAJOR / 0 MINOR**; RECONSTRUCTED in full | **0 FATAL / 0 MAJOR / 1 MINOR** (MINOR-1: load-bearing Lemma B and two auxiliary facts cite the unsupplied, unreviewed v1; reviewer re-derived all three from LAW642) |
| (2) Rounded-arc regime above ε_t | 0/0/0, RECONSTRUCTED | 0/0/0 (LAW642 §8.3–8.4; NORM148 Gate III) |
| (3) Discontinuity separation at every ε | 0/0/0, RECONSTRUCTED | 0/0/0 (LAW642 §1, §8.1, §8.3) |
| (4) Every LAW642/NORM148 application | 0/0/0 — every use is inside the adopted statements or the adopted 642-LF proof | MDA per-cost interface: author-named positive-PRIOR import, NR by the reviewer, callers listed in §7 |
| Source-status claims | not mathematics | MINOR-2: one table phrase can be read as a worldwide-absence claim; explicit disclaimers elsewhere |

**Overall: FATAL 0, MAJOR 0, MINOR 2.** No result is promoted beyond the adopted LAW642/NORM148 cut. No source-equivalence (T-MATCH) source has been located, and none is claimed.

## 3. Scope item (1): the exact single-threshold theorem

### 3.1 Notation and base identities (re-derived)

- G is geometric with P(G=k) = (1−b)b^k and m = b/(1−b). Since E binom(G,j) = m^j, the Stirling expansion gives E G² = T2 = m+2m², E G³ = T3 = m+6m²+6m³ and E G⁴ = T4 = m+14m²+36m³+24m⁴.
- M_r(q) = E(G+q)^r, so M_r′ = rM_{r−1}. Also E(G+1)^r = T_r/b.
- **J_D = M4/(3M2) is the MSE of the diamond-core law qD.** The density b^{max(0, ⌈|z|_1−q⌉)} has |z|_1-marginal ∝ r·b^{n(r)}. The layer decomposition gives ∫r^{j+1}b^{n} dr ∝ M_{j+2}(q)/(j+2). On each level set of the ℓ1 norm the conditional law is uniform (constant gradient norm), so E[|z|_2² | r] = (2/3)r². Hence E|z|_2² = (2/3)·(1/2)M4/M2 = M4/(3M2).
- J_D(0) = T4/(3T2) = λP. J_D(1) = (T4/b)/(3T2/b) = λP. These are the facts v2 attributes to "v1 §1".
- J_D′ = (4M3M2 − 2M4M1)/(3M2²) = 2P_m/(3M2²).
- P_m = 2M3M2 − M4M1 was re-expanded and matches LAW642 (D) coefficient by coefficient:
  - q³: 8T2 + 12m² − 6T2 − 4m² = 2m + 12m²;
  - q²: 12mT2 − 2T3 = 12m³ − 2m;
  - q¹: 6T2² − T4 = −(m + 8m² + 12m³);
  - q⁰: 2T2T3 − mT4 = m² + 2m³.
- Q(q) = 2M3 − 3M1M2 = −q³ − 3mq² + 3mq + 2m + 9m² + 6m³, re-derived. v2 attributes this to "v1 Lemma 1". The step uses 3T2 − 6m² = 3m and 2T3 − 3mT2 = 2m + 9m² + 6m³.
- v = m+m² = b/(1−b)² = 1/(e^{ε/2} − e^{−ε/2})² = 1/(4 sinh²(ε/2)), so s = 1/(4v).

### 3.2 Lemma A (Descartes count for J_D′): RECONSTRUCTED

- **Sign pattern.** The coefficient signs of P_m are (+, +, +, sign(6m²−1), −, +). There are two sign changes whatever the middle sign (a zero is skipped), so P_m has at most two positive roots.
- **Endpoint values.** P_m(0) = m²(1+2m) > 0. P_m(1) = 1 + 4m + 5m² + 2m³ = (1+m)²(1+2m) > 0.
- **Two simple roots.** J_D(0) = J_D(1) with J_D′ > 0 at both ends forces J_D′ < 0 somewhere in (0,1). So P_m has at least two odd-multiplicity zeros in (0,1), hence exactly two simple roots q_a < q*, and no other positive root. The sign pattern is +, −, +, and q* is the unique minimizer of J_D on [0,∞), with J_D(q*) < λP.
- **Position of 2m.** P_m(2m) = 32m⁵ + 80m⁵ + (16m⁴ + 96m⁵) + (48m⁵ − 8m³) − (2m² + 16m³ + 24m⁴) + m² + 2m³ = m²(256m³ − 8m² − 22m − 1). For 0 < m <= 1/4, 256m³ <= 16m < 22m, so P_m(2m) < 0 and q_a < 2m < q*.

### 3.3 Lemma B (diamond ⟺ Q(q*) >= 0): RECONSTRUCTED by the reviewer from LAW642

v2 writes only "This is v1 Lemma 2 with the uniqueness of Lemma A", and its sufficiency bullet cites "v1 Lemma 2(c)". v1 is not supplied. I re-derived the lemma from LAW642 §8.

1. **Full-diamond CLIP condition.** The core is the full diamond 2tD iff R_λ(0) >= 2t, that is, √(λ−v) − m >= 2t, that is, λ >= (2t+m)² + v = M2(q) with q = 2t. This is the D-branch screen of LAW642 §8.5. Sufficiency also needs R(y) >= 2t − y on [0,t]. That follows from LAW642 §8.3: R(y)+y is increasing while R >= t, and R cannot reach t before y = t.
2. **Screen identity.** At a root of P_m, M4 = 2M3M2/M1. Hence J_D(q) − M2(q) = (M4 − 3M2²)/(3M2) = Q(q)/(3M1). So the screen holds iff Q(q) >= 0.
3. **Necessity.** Suppose the optimal core is q_oD.
   - LAW642 gives terminal width d = t < 1/2 and t > 0, so q_o ∈ (0,1).
   - Every γD with γ ∈ (0,1) is a feasible CAN-class law with cost J_D(γ) >= W = J_D(q_o). So q_o minimizes J_D, and q_o = q* by Lemma A.
   - Item 1 at λ = W gives W >= M2(q*). Item 2 then gives Q(q*) >= 0.
4. **Sufficiency.** Suppose Q(q*) >= 0 and put λ* = J_D(q*).
   - λ* >= M2(q*) > T2, and λ* < λP by Lemma A, so λ* lies in the LAW642 §8.4 range (T2, λP).
   - At t* = q*/2 the CLIP core is q*D (items 1–2), so H(t*,λ*) = Z(J_D − λ*) = 0.
   - dH_D/dq = (8/3)M3 − 4λM1 = (4/(3M2))P_m = 0 at λ*, so t* is stationary.
   - t* is not the first (+ to −) zero of the convex DC cubic: otherwise H would increase from H(0,λ*) = (2/3)T4 − 2λ*T2 > 0, contradicting H(t*) = 0. So t* is a local minimum with value 0 < H(0,λ*).
   - LAW642 §8.4 shows that at most one positive local minimum can lie below H(0,λ). So min_t H(t,λ*) = 0.
   - LAW642 §8.1 shows the minimum is strictly decreasing in λ with unique zero W. So W = λ*, and the unique optimal core is q*D.
   - If Q(q*) = 0, the junction is c = 0 and the law is still the diamond law, as in LAW642 §8.5.

### 3.4 Lemma C (division identity): RECONSTRUCTED

With a = 5m + 6m² and c0 = 2m + 9m² + 6m³, expand (q² + 2mq + a)(q³ + 3mq² − 3mq − c0). The coefficients are:
- q⁵: 1;
- q⁴: 5m;
- q³: −3m + 6m² + a = 2m + 12m²;
- q²: −c0 − 6m² + 3ma = −2m + 12m³;
- q¹: −2mc0 − 3ma = −19m² − 36m³ − 12m⁴;
- q⁰: −ac0 = −10m² − 57m³ − 84m⁴ − 36m⁵.

The q⁵ through q² coefficients agree with P_m. The remainders are:
- linear: −m + 11m² + 24m³ + 12m⁴ = m(1+m)(12m² + 12m − 1), since (1+m)(12m² + 12m − 1) = 12m³ + 24m² + 11m − 1;
- constant: 11m² + 59m³ + 84m⁴ + 36m⁵ = m²(1+m)(36m² + 48m + 11), since (1+m)(36m² + 48m + 11) = 36m³ + 84m² + 59m + 11.

Because q² + 2mq + a > 0 for q >= 0, (S) holds: sign Q = sign R at every positive root of P_m.

### 3.5 Lemma D (threshold polynomial and collapse to v): RECONSTRUCTED term by term

- **The cleared form.** With q_c = mN/Dn, Q(q_c)·Dn³ = m·[−m²N³ − 3m²N²Dn + 3mNDn² + (2 + 9m + 6m²)Dn³] = m·G.
- **The building blocks.** I re-expanded N², N³, Dn² and Dn³. All four printed forms agree, and their m = 1 values are 95², 95³, 23² and (−23)³.
- **The four products.** I expanded each fully; m=1 values are in brackets.
  - N²Dn = 121 − 396m − 11028m² − 46368m³ − 77328m⁴ − 57024m⁵ − 15552m⁶ [−207575 = 9025·(−23)]
  - NDn² = 11 − 216m + 204m² + 8064m³ + 19728m⁴ + 17280m⁵ + 5184m⁶ [50255 = 95·529]
  - (2+9m+6m²)Dn³ = 2 − 63m + 474m² + 1620m³ − 14904m⁴ − 58320m⁵ − 78624m⁶ − 46656m⁷ − 10368m⁸ [17·(−12167)]
- **Collected coefficients of G, from m⁸ down:**
  - m⁸: −46656 + 46656 − 10368 = −10368;
  - m⁷: −186624 + 171072 + 15552 − 46656 = −46656;
  - m⁶: −291600 + 231984 + 51840 − 78624 = −86400;
  - m⁵: −84672;
  - m⁴: −46728;
  - m³: −14004;
  - m²: −1868;
  - m¹: −30;
  - m⁰: 2.

  These match v2, including G(1) = −290724.
- **Factorization.** (1 + 3m + 2m²)·K reproduces every coefficient of G, so G = (2m²+3m+1)K.
- **Collapse to v.** 5184v³ + 1728v² + 36v − 2 = 5184m⁶ + 15552m⁵ + 17280m⁴ + 8640m³ + 1764m² + 36m − 2 = −K.
- **Return to s.** With v = 1/(4s), −K·s³ = 81 + 108s + 9s² − 2s³.

### 3.6 Theorem and corollaries: RECONSTRUCTED

- **Case v >= 1/12 (s <= 3).** R(q) = v[(12v−1)q + mN] > 0 for q > 0, so Q(q*) > 0 and the core is a diamond. Consistently, 2s³ <= 54 < 81.
- **Case v < 1/12.** Then m < 1/12 and Dn > 0.
  - q_c = mN/Dn >= 11m > 2m > q_a is the unique positive zero of R, with R > 0 exactly on (0, q_c).
  - (S) gives Q(q*) >= 0 ⟺ q* <= q_c.
  - Lemma C at q_c gives P_m(q_c) = −(positive)·Q(q_c).
  - The sign pattern of Lemma A gives q_c >= q* ⟺ P_m(q_c) >= 0 ⟺ Q(q_c) <= 0.
  - Lemma D: sign Q(q_c) = sign G = sign K = sign(2s³ − 9s² − 108s − 81).
  - So diamond ⟺ cubic <= 0.
- **One transition.** The s-cubic has sign pattern (+, −, −, −), hence exactly one positive root s_t; it is negative before s_t and positive after. s = sinh²(ε/2) is strictly increasing in ε, so there is exactly one transition, ε_t.
- **Closed form for u_t:**
  - with u = 3/s, the cubic equals −27(3u³ + 12u² + 3u − 2)/u³;
  - with u = y − 4/3, this becomes y³ − (13/3)y + 74/27;
  - 4p³ + 27q² = −3312/27 < 0, so there are three real roots;
  - the trigonometric form has amplitude 2√13/3 and argument (3q/(2p))√(−3/p) = −37/(13√13);
  - the unique positive u-root is the largest root (k = 0).
- **Corollary ε <= 2ln(2+√3).** s <= 3 ⟺ sinh(ε/2) <= √3 ⟺ ε <= 2·arcsinh(√3) = 2ln(2+√3). This is exactly the v >= 1/12 case.
- **v1 Theorem A.** It follows, since (5+√33)/2 < (2+√3)²: 14 + 8√3 > 5 + √33.
- **v1 Theorem B.** I checked it without locating s_t. At ε = ln(2^18+1), s = 2^34/(2^18+1) >= 2^15. For s >= 198, 9s² + 108s + 81 <= 198s² <= s³, so the cubic is >= s³ > 0.

## 4. Scope item (2): rounded-arc regime above ε_t — RECONSTRUCTED

- **Not a diamond.** If the cubic is positive, the Theorem gives Q(q*) < 0. The contrapositive of Lemma B's necessity then excludes a diamond core.
- **Arc plus a nonzero facet.** LAW642 §8.3 excludes lower clipping at the optimum, leaving "arc followed by a nonzero upper facet" or the full facet. So the core is in the rounded branch with d ∈ (0,t), and the arc length c = t − d > 0 is genuine.
- **Strict gap.** NORM148 Gate III (adopted) then gives the strict norm-radial gap V_N > V for each such fixed ε. The curvature F″ = −A/(A−y²)^{3/2} < 0 is re-derived. This is a strict pointwise-in-ε gap, not an evaluated or uniform one.
- No rounded-core parameter values or numerical ranges are asserted, by the author or by me.

## 5. Scope item (3): no continuous-density optimizer at any ε — RECONSTRUCTED

- **Two plateaus meet at every boundary point.** S_* is compact and convex (LAW642 §8.3) and contains [−t*, t*]² (§8.1), so it has nonempty interior. Every boundary point x0 is a limit of interior points, where p_* = Z^{−1} (n = 0). It is also a limit of points x0 + δu in the open set int(S_* + D) ∖ S_*, where p_* = Z^{−1}b (n = 1). Take u an outward normal and δ small; D contains a neighbourhood of 0.
- **No continuous version.** A continuous a.e.-version would be constant on each open set, hence on each closure, giving Z^{−1} = Z^{−1}b. This is impossible since b < 1.
- **Consequence.** The optimal law is unique as a law (LAW642 §1). So any feasible law with a continuous density version differs from μ_* and has cost strictly above V, at every finite ε.
- **Applications.** This applies at statement level to product-Laplace (e^{−ε|x|_1}), K-norm, Gaussian and spherical generalized-gamma optimizers, all of which have continuous densities. It says nothing about the unread ranges of those sources. The author states this correctly (S20 §1, final paragraph).

## 6. Scope item (4): every application of LAW642 and NORM148

| Use (location) | Within the adopted statement or proof? | Reviewer check |
|---|---|---|
| Unique optimal law, density Z^{-1}b^{n_*}, core S_* (v2 §1/§6; S20 §1) | Yes: S13 adopted theorem | Used as stated |
| ZN/moment formulas, M_r, T_r, E(G+1)^r = T_r/b (v2 §1–2) | Yes: LAW642 §6, §8.2 | Re-derived |
| J_D formula and J_D(0) = J_D(1) (v2 §2) | Yes (§8.2), but cited as "v1 §1" | Re-derived (§3.1) |
| D-branch system P_m = 0, λ = M4/(3M2), screen λ >= M2(q) (v2 §1, §3) | Yes: §8.5 | Re-expanded P_m; screen re-derived from CLIP |
| CLIP, H monotone in λ with unique zero W (Lemma B) | Yes: §8.1 | Used as stated |
| No lower clipping; arc plus nonzero facet or full facet; convex core (v2 §6; S20 §1) | Yes: §8.3 | Used as stated |
| At most one positive local minimum below H(0,λ); regime boundaries (Lemma B sufficiency) | Yes: §8.4 | Used as stated; the local-minimum identification of t* is the reviewer's step (§3.3 item 4) |
| Strict norm-radial gap iff a genuine arc (v2 §6, §7(ii); S20 §2) | Yes: NORM148 Gate III (S14) | Used as stated; arc genuineness re-derived |
| NORM148 Lemma H / class attainment | Not used beyond Gate III | — |

No use goes beyond LAW642's adopted 642-LF proof or NORM148's three adopted gates. **v2 states that defects in LAW642 §8 or NORM148 propagate (§7(iv)); I concur.**

## 7. Findings, NR items and source-status check

### MINOR-1 (dependency/trust): v2's load-bearing Lemma B depends on an unsupplied, unreviewed v1

v2 relies on v1 `050e469f…` for three things:
- Lemma B ("This is v1 Lemma 2 …"; sufficiency "as in v1 Lemma 2(c)");
- the Q formula ("v1 Lemma 1");
- the endpoint facts J_D(0) = J_D(1) = λP ("v1 §1").

v1 is outside this union and unreviewed. The reviewer re-derived all three from LAW642 §8 (§3.1, §3.3), so the Theorem is supported at review scope with no mathematical gap. But the supplied v2 text is not self-contained at its key step. Suggested repair: an additive self-contained addendum containing the §3.3 argument. Do not edit v2.

### MINOR-2 (source-status wording)

The S20 §2 table row for G13/G15 says G13's question "is answered AFFIRMATIVELY here, by LAW642 + v2, not by any source". Read alone, "not by any source" can sound like a worldwide-absence claim. It should read "not by any inventoried source".

This is mitigated by explicit disclaimers elsewhere:
- S20 §3.1: "No source in the recorded inventory has been located that states or implies this";
- S20 §3.3: "No worldwide absence, firstness, novelty or priority clearance is claimed";
- v2 §7(iv);
- checkpoint 192.

No packet claims novelty, priority, firstness or worldwide absence.

### Named import, NR by the reviewer: the MDA per-cost interface

This positive-PRIOR import is named by the author. Callers:
- v2 §7(iii) bullet 2 ("V = (2/3)V1", "μ_* is the ℓ1-radial optimizer of E|Z|_1² over ALL laws");
- S20 §2 K25/MDA row;
- S20 §3.1, through V1.

The step E|Z|_2² = (2/3)E|Z|_1² on ℓ1-radial laws, and hence V = (2/3)·(ℓ1-radial infimum), attained only at μ_* for ε <= ε_t, is elementary and RECONSTRUCTED. The passage from the ℓ1-radial infimum to the ALL-law infimum V1 uses MDA's all-law radial optimality for cost r². That passage is NOT_RECONSTRUCTED here.

### Source-status statements

These are author reports, not mathematics:
- the mixed-cost all-law bound is absent from the inventoried sources;
- AS21, JY24, Wei, AG26, R2DP, UDP-FL, GVapprox, scalar GV and LCR scalar were read only in part, with the exact unread ranges listed in checkpoint 192.

They are correctly scoped to the recorded inventory, except for the MINOR-2 phrase.

## 8. Nonclaims and process

- **Nothing promoted.** No T-MATCH source is located. No worldwide absence, novelty, priority or firstness is claimed, and no partially read range is cleared. Nothing here is parent adoption, formal/kernel/human/configured-family/executable acceptance, or completion of the broad book article.
- **Process history.** The author's process histories and quarantines stay as recorded: ENTIRE116, cp102/AD33 and cp108 guidance ZERO, the v156 bodies unopened, aux214 STOP, N4 UNKNOWN. I opened none of the quarantined material.
- **Identity checks are not threshold evaluation.** The author's exact identity checks at m = 1, −1 and −1/2 are disclosed hand arithmetic checking polynomial identities, not threshold evaluation. I re-did the m = 1 checks as cross-checks of my own expansions only.
- **Tools.** I used only reads, `/bin/date`, `shasum` and `wc`. No interpreter was used in this review.

Next: pin this file, RETURN to Main, then write and send ONE new whole-primary ACK and wait. The original R-minus primary stays PAUSED, under STOP158, until then. The same eighteen owners, science cutoff 2026-10-27T11:05:38-07:00 and delivery 12:35:38 remain.

**END OF v214-A REVIEW.**
