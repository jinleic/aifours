**Summary.** I judged each claim on its own, reading v1 through its mandatory errata. I re-derived every case from the label formulas. No probe output or LP optimum is used as a premise.

| claim | verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| K63-D (v1 + H1) | **CORRECT** | 0 | 0 | 3 |
| K63-E (v1 + J1 + J2) | **CORRECT** | 0 | 0 | 3 |
| K7-35 (v1 + K1) | **CORRECT** | 0 | 0 | 3 |

The v1 defects repaired by H1, J1, J2 and K1 were real. Each would have been MAJOR in v1. The governing errata close all four, and I re-checked each repair.

**Common recomputation.**
- **Local indices.**
  - In K7, λ_j = r_j α_vj.
  - In K6.3 at an apex v in C, λ_c = r_c α_vc and λ_d = r_d α_vd, with d weighted 2α_vd in units of 1/6.
  - At d, λ_c = 2 r_c α_dc, in units of 1/3.
- **Why the gcds reduce.** The w's are pairwise coprime and prime to 30, so they are prime to every α ≤ 5 and to every marker. Hence gcd(λ_j, λ_k) = gcd(m_j α_j, m_k α_k).
- **Marker exponents.** The markers are powers of distinct primes on distinct vertices. A, B, F and the 5-exponents enter a gcd only through [3|·] and [5|·].
  - The 2-exponent E enters only g(i*, four) ∈ {2, 4} and g(i*, t) when α_t = 4.
  - In K63-D every certificate with y_i* > 0 has no four in the u-row, and its only positive set through {i*, t} is a pair. So E never changes a certificate.
- **Allowed sets.** Every allowed set is a clique of the "gcd ≥ 2" graph. I checked every positive-weight clique, which is a superset of the allowed sets.
- **Lift to arbitrary groups.** R0 (the finite-core quotient) preserves indices, disjointness and the conjugates used by INV. The arbitrary-group statements follow.

---

## 1. K63-D — CORRECT

**Apex choice (D0).** The choice depends only on the labelled index tuple (E6), so the same v serves the inverted configuration.
- If |M_C| ≤ 1, any v has at most one marked neighbour and at least four unmarked ones.
- If |M_C| = 2, take v in M_C. This works whether the markers split 1+1 or one vertex carries two of them.
- If |M_C| = 3, each marked vertex carries exactly one marker, so the remaining case is v = p.

**D0, α_vd = 1.** λ_d = w_d is isolated, contributing 2. The C-part must reach 4.

**(a), N ∈ {4, 5} unmarked, marked neighbour at weight 0.**
- k5 ≥ 1 gives 5.
- 1 ≤ k3 ≤ 3 with k5 = 0 gives 3 + ≥1.
- k3 ≥ 4 gives k3.
- Otherwise R1∪R24 gives min(N, 4) = 4.

**(b), apex p.** The gcds are:
- g(u,i) = 2^{min(v2 a_u, E + v2 a_i)} · gcd(odd parts);
- g(u,t) = 3 if a_u = 3, else gcd(a_u, a_t);
- g(i,t) = 2^{min(E + v2 a_i, v2 a_t)} · 3^{[a_i = 3]} · 5^{[a_i = a_t = 5]}.

C-part values for every case:

| case | weights | critical sets | value |
|---|---|---|---|
| b1: k5 ≥ 1 | 1/k5 on fives | — | 5 |
| b2: k3 ∈ {1,2} | 1/k3 on threes + standard | — | 3 + (3−k3) ≥ 4 |
| b3: a_t ≥ 3 | 1/3 on threes and t | {t,u,u'} = 1; {t,u,u',u''} has all gcds 3, not allowed; so no 5-set | 3 + a_t/3 ≥ 4 |
| b3: a_t = 1, 3∤a_i | y_i = 1 | i isolated | 3 + a_i |
| b3: a_t = 2, 3∤a_i | y_t = 1/3, y_i = 2/3 | {t,u,u'} = 1; {t,i} = 1; {t,i,u} not allowed | ≥ 13/3 |
| b3: a_i = 3, a_t = 1 | 1/3 on i and t | all five pairwise gcds 3, so sets have size ≤ 3 | 13/3 |
| b3: a_i = 3, a_t = 2 | y_i = 1/3, y_t = 0 | {i,t,u,u'} allowed (g = 6), sum 1; {i,u,u',u''} not allowed, so no 5-set | 4 |
| b4: (0,0,3) | 1/3 on fours | — | 4 |
| b4: (2,1,0) | y_two = 1 | two's partners i, t at 0 | 4 |
| b4: (2,0,1) | y_four = 1 | — | 6 |
| b4: (1,1,1) | 1/2 on the two and the four | — | 4 |
| b4: (1,0,2) | 1/2 on fours | — | 5 |
| b4: (0,2,1) | 1/2 on all | {2,2,4} not allowed | 4 |
| b4: (0,1,2) | 1/2 on fours | — | 4 |
| b4: (3,0,0) | i∼t: 1/2, 1/2; otherwise 1, 1 | — | ≥ 4 / ≥ 5 |
| b4: (1,2,0), (0,3,0) | 1/2 on twos, plus t-rule | — | ≥ 4 |

**t-rule.**
- a_t even: y_t = 1/2. {t, 2} = 1 and {t, 2, 2'} is not allowed. Adds a_t/2.
- a_t odd and i∼t: per H1, this holds exactly when a_i = 3 or a_i = a_t = 5. Set y_i = y_t = 1/2. {2, i} = 1, {i, t} = 1, and {2, i, t} and {2, 2', i} are not allowed. Adds ≥ 2.
- Otherwise t is isolated and adds a_t.

The minimum C-part is 4 in every case.

**D5, α_vd = 1.** λ_d = 5^{h_d} w_d is compatible exactly with C-fives.

| case | weights | value |
|---|---|---|
| k5 = 0 | y_d = 1, standard on ≥ 4 unmarked | 2 + 4 |
| 1 ≤ k5 ≤ 4, an unmarked five exists | 1/k5u on unmarked fives (their partners are fives, d, or a five-x, all at ≤ 1/k5u or 0), standard on the rest | 5 + ≥1 |
| as above, all unmarked are fives | y_x = 1 (x is 5-free with α_vx ≠ 5, hence isolated) | 5 + α_vx |
| k5 = 1, x the only five | standard on 4 unmarked, y_d = 1, y_x = 0 (only sets through d are {d} and {d,x}) | 4 + 2 |
| k5 = 5, inverse row α* = 1 | unmarked isolated, 1 each; x∼d iff 2∣m_x and α*_vd = 2 (then 1/2, 1/2), else 1, 1 | ≥ 13/2 or ≥ 7 |

Applying the same v to the inverted configuration gives α*_vd = 2. Then α + α* = 4 > 3, a contradiction.

**Findings**
- **H1 (v1 gap, closed).** v1 tested t∼i* by "3 | α_pi*".
  - Concrete case: u-row (2,2,2), α_pt = α_pi* = 5, any E, F, B. Here g(t, i*) = 5, so all three of v1's clauses fail.
  - H1's weights give 3 + 5 = 8. H1 governs.
- **MINOR D-1 (D5 Step 2).** "Only when m_c is a power of 2" is wrong when |M_C| = 1 and x carries both markers (m_x = 2^E 3^F).
  - Literal counterexample: α*_vd = 2. Then g(x, d) = 2, but the text assigns y_x = y_d = 1, so {x, d} sums to 2 and the certificate is infeasible.
  - Repair: replace the condition with "2 | m_c". This gives 4 + 1/2 + 2 = 13/2.
  - In Step 1, "a power of 2 or of 3" should read "{2,3}-smooth". The conclusion there is unaffected.
- **MINOR D-2 (D0 (a)).** "≥ 5 if some α = 5" must read "some *unmarked* α = 5". Example: a marked x with α_vx = 5 and unmarked row (1,1,1,1) gives 4, not 5. The bound ≥ 4 still holds.
- **MINOR D-3 (imports).** M1-F3's ROW-U-deg is stated for a six-neighbour row. K63-D actually uses the subset form: the class analysis on 4–5 C-neighbours with g = 6, as in accepted K63-U0 Step 1 and E8. Cite that instead.
- **Remark.** D0 with M_C = ∅ subsumes K63-U0.

---

## 2. K63-E — CORRECT

K63-E uses only K63-D's §1 notation, not its theorem.

**D-ROW at d.**
- Labels: λ_c = 2·5^{h_c} α_dc, so every gcd lies in {2, 4}, and equals 4 iff both vertices are in P.
- Allowed sets: all pairs; 3- and 4-sets with at most one element outside P; no 5-sets. A 4-set with exactly two P-elements contains a 3-subset with only one P-element, so it is not allowed.
- LFC requires the objective to be < 3 (units of 1/3). Each excluded size reaches 3:
  - |P| = 0: weight 1/2 everywhere gives 3.
  - |P| = 1: weight 1/2 everywhere gives 7/2.
  - |P| = 2: weight 1/2 off P and 1/4 on P; the largest set {P, P, x} sums to 1; value 3.
  - |P| = 6: weight 1/4 everywhere gives 3.
- Hence 3 ≤ |P| ≤ 5, and the same holds for |P*|. P and P* are disjoint (2 + 2 > 3), so |P| = |P*| = 3 and A = P*.

**C-ROW.** Compatibility with d (λ_d = 3^F 5^{h_d} α_vd):
- threes: always;
- fives: iff h_d ≥ 1;
- evens: iff α_vd = 2;
- nothing else.

Situations: S0 (no 5-marker), Sd (h_d ≥ 1), Sp (p ∈ C, h_d = 0).

In S0 and Sp, every C-five f has λ_f coprime to λ_d. Then y_d = y_f = 1 gives 2α_vd + 5 ≥ 7. This is J2 item 1; its proof does not depend on k3, and it also covers v = p.

**(a) α_vd = 1.**

| sub-case | weights | value |
|---|---|---|
| k3 ∈ {1,2}, S0 or Sd | 1/k3 on threes; 1/k5 on fives (Sd); y_d = 0; else standard on the rest | ≥ 3 + 3 |
| k3 = 1, the three is p (Sp) | y_p = 1 (partner d only, at 0), standard on 4 | 7 |
| k3 = 2, threes {p, u3} (Sp) | y_u3 = 1 (partners within {p, d}, both 0), standard on 3 | 6 |
| k3 ∈ {1,2}, p not a three (Sp) | 1/k3 on threes, standard on 5−k3 including p | ≥ 6 |
| k3 = 0, h_d = 0 | y_d = 1 (isolated), standard | ≥ 6 |
| k3 = 0, Sd, 1 ≤ k5 ≤ 4 | 1/k5 on fives, rest standard | 5 + ≥1 |
| k3 = 0, Sd, k5 = 0 | y_d = 1 | 6 |
| k3 = 0, Sd, k5 = 5 | survives as the second alternative | — |

**(b) α_vd = 2.**
- k3 ∈ {1,2}: as in (a), with y_d = 0.
- k3 ≥ 3: fives are already gone (by J2 item 1 in S0/Sp; in Sd by 1/3 on threes, 1/k5 on fives, y_d = 0, value ≥ 8).
  - Weights: 1/3 on the threes and on d.
  - Cliques through d are either d with threes (size ≤ 3, sum 1) or d with evens. Among the latter, {d, x} ≤ 5/6 and {d, 4, 4} = 5/6 (after J1); {d, 2, 2} and {d, 2, 4} are not allowed.
  - Each remaining vertex contributes exactly 1: a one at weight 1, a two at 1/2, a four at 1/4. For p: α_vp = 1 gives 1; α_vp = 2 gives 1/2 · 2 = 1; α_vp = 4 gives 1/2 · 4, or 1 when J1 sets y_p = 1/4.
  - Objective: k3 + 4/3 + (5 − k3) = 19/3.

**Closure.**
1. Take v in A. Suppose the second alternative holds: then α*_vc = 1 for every C-neighbour, the inverse labels are pairwise coprime, and the inverse objective is 5 + 2α*_vd ≥ 7, a contradiction.
2. So k3(v) ≥ 3. Each three-neighbour u of v has a three in its own row, so C-ROW (b) gives α_ud ≠ 2, i.e. u ∈ A.
3. But |A ∖ {v}| = 2 < 3, a contradiction.

**Findings**
- **J1 (v1 gap, closed).** Concrete case: k3 = 3, remaining {p, u} with α_vp = α_vu = 4, α_vd = 2.
  - {p, u, d} is allowed (g(p, u) = 4) and its v1 sum is 1/2 + 1/4 + 1/3 = 13/12.
  - J1 sets y_p = 1/4, giving 5/6 and objective 19/3.
- **J2 (v1 gap, closed).** Concrete case: k3 = 1 with p the only three, plus an unmarked five f.
  - {p, f} is allowed (gcd 5) and sums to 1 + 1/k5 > 1.
  - J2 item 1 excludes the fives.
- **MINOR E-1.** The C-ROW (b), k3 ≥ 3 parenthetical "a five would have been killed by y = 1/k5 + others" is left "unchanged" by J2, but it is not a certificate as written.
  - If y_d = 1/3 is kept: in Sd with k3 = 4 and one five f, {d, f} sums to 4/3.
  - In Sp with p a three: {p, f} sums to 1/3 + 1.
  - Repair, by situation:
    - S0 and Sp: use the J2 item 1 certificate, value 9.
    - Sd: 1/3 on threes, 1/k5 on fives, y_d = 0, value ≥ 8.
  - Amend J2's "unchanged" sentence accordingly.
- **MINOR E-2.** J2 items 2–4 presuppose v ≠ p. The apex v = p is covered (no marked C-neighbour; fives are coprime to d), but this should be stated.
- **MINOR E-3.** Same import issue as D-3.
- **Remarks.** The closure needs only |A| ≤ 3, and the second-alternative kill does not need α*_vd = 2.

---

## 3. K7-35 — CORRECT

**ROW-2 at w ∈ W.** The gcds are:
- g(t,u) = 3 if a_u = 3, else gcd(a_t, a_u);
- g(p,u) = 5 if a_u = 5, else gcd(a_p, a_u);
- g(t,p) = 2^{min(v2 a_t, v2 a_p)} · 3^{[a_p = 3]} · 5^{[a_t = 5]}.

Every row falls under (a'), (b') or (c').

**(a').**
- k5 ≤ 3: 5 + ≥1.
- k5 = 4 with a_t ≠ 5: 1/4 on fives, y_t = 1 (t's only possible partner is p, at weight 0). Value 5 + a_t.

**(b'), k3 = 1.** 3 + 3.

**(b'), k3 = 2**, with remaining unmarked {x, y}:
- {1,2}: 3 + 3.
- {1,4}: 3 + 5.
- {2,4}: 3 + 3.
- {4,4}: 3 + 4.
- {1,1} and {2,2}: 3 + 2 = 5 so far, then:
  - a_p ∈ {1,5}: y_p = 1, adds ≥ 1.
  - a_p ∈ {2,4} with twos: y_p = 1/2, adds ≥ 1. {p, 2, 2'} is not allowed.
  - a_p ∈ {2,4} with ones: y_p = 1, adds ≥ 2.
  - a_p = 3 and a_t = 4: {3, 3, t, p} has all pairwise gcds 3, so put 1/3 on each. Twos at 1/2: {t, 2} = 5/6, and {p, 2} and {t, 2, 2'} are not allowed. Value 19/3.

The survivors are exactly the stated ones: a_p = 3, a_t ≠ 4, {x, y} ∈ {{1,1}, {2,2}}.

**(b'), k3 = 3.** If x = 4: 3 + 4. If a_t = 4 and x ∈ {1,2}, put 1/3 on threes and t (base 13/3):

| a_p | x = 1 (y_x = 1) | x = 2 |
|---|---|---|
| 1 | y_p = 1: 19/3 | y_x = 2/3, y_p = 1: 20/3 |
| 2 | y_p = 2/3 (partner t): 20/3 | y_x = 2/3, y_p = 1/3 ({p,t,x} all gcd 2, not allowed): 19/3 |
| 3 | y_p = 1/3 (all gcds 3): 19/3 | y_x = 2/3, y_p = 1/3: 20/3 |
| 4 | y_p = 2/3: 8 | y_x = 0, y_p = 2/3 ({p,t,x} allowed, sum 1): 7 |
| 5 | y_p = 1: 31/3 | y_x = 2/3, y_p = 1: 32/3 |

**(b'), k3 = 4 with a_t = 4.** 4 + 4/3 + p's contribution ≥ 1, giving ≥ 19/3.

**(c').**
- a_p = 3: y_p = 1 (partner t only), value 7.
- a_t = 5: y_t = 1, value 9.
- a_t = 3 with a_p ≠ 3: t is isolated, value 7.
- a_p = 5 with a_t ≠ 5: p is isolated, value 9.
- Otherwise ROW-U-deg holds, and ROW-U (i)–(iii) follow.

**Global steps.**
- **(0)** ROW-1 applies at t via the accepted ROW-1-deg transfer (G2). The sixth label 5^B α is odd and {3,5}-smooth.
  - k5 = 5 gives α* = 1 on W, and the inverse objective is 5 + α*_tp ≥ 6.
  - Threes: weights 1/3, 1, 1/2 on threes, ones, twos, and y_p ∈ {1, 1/2}, give 5 + 1 = 6. Here p shares no prime with the threes.
  - So F_t ⊔ F*_t = W ∪ {p}, each of size 3.
- **(1)** No five inside W.
- **(2)** No three inside W.
  - W3 = F*_t, so p ∈ F_t, and k3 = 2 at every w ∈ W3 (k3 ≥ 3 would force |W3| ≥ 4).
  - K1, for any mixture of per-w values: u1's W3-entries are ≤ 2, so its three fours must be towards u2, p and t.
  - Then α_u1p = 4 while α_pw = 3 for w ∈ W3, contradicting ROW-1 (b) at the marked apex p (its only marked neighbour t carries just the 3-marker).
- **(3)** Every vertex has ≥ 3 fours in both α and α*. These sets are disjoint, so each vertex has exactly three. A 3-regular graph on 7 vertices has degree sum 21, which is odd: impossible.

**Findings**
- **K1 (v1 gap, closed).** v1 assumed one common value across W3.
  - Concrete pattern: α_{w1,u} = 1 but α_{w2,u} = α_{w3,u} = 2. Then u1's W3-row is (1, 2, 2), which neither of v1's branches covers.
  - K1's replacement handles every mixture.
- **MINOR K-1.** The k3 = 3 (x = 1) and k3 = 4 totals add p's *weight* 2/3 where its *contribution* belongs. The true minimum contribution is 1, so the exact objectives are ≥ 19/3. The stated bound of 6 is still valid because LFC is strict.
- **MINOR K-2.** Step (3)'s "verbatim" inversion should say explicitly, as M1-F6 does, that:
  - the inverted step (0) uses the original LFC (α** = α);
  - ROW-1 is applied to α* at t and p via ROW-1-deg.
- **MINOR K-3 (imports).** K7-35 uses 1 ≤ α ≤ 5, but LFC-erratum E1 (L0.2/L0.3) is not listed. Add it.

---

## 4. Scope (if all three are accepted)

What remains open:
- **K7:** only configurations with both an e ≥ 2 vertex and an f ≥ 2 vertex (same or different vertices, 5-marker anywhere).
- **K6.3:** only f_d ≥ 2 together with a 2-marker i* in C.
- **K6.2\*:** all of it.

K5.3 keeps its qualified StageA disposition. The exploratory remarks in K63-D §4 and K63-E §5 are bounded observations, not premises. There is no Sun(7) claim and no novelty or priority claim.
