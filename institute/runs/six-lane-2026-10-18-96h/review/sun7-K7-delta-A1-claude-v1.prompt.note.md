# Referee report, Slice A1: K7-A1-STRUCT §§0–5 → K7-TC (TC, R1/R3/R4/R5, TC-B, TC-P) → K7-TC-A22

I reviewed the embedded texts. I did not recompute the hashes, since tools were excluded. K7-A2-FIVE is outside this slice and nothing below concerns it. I verified all three files in dependency order and assumed none of their claims in advance.

## 1. Verdicts

| # | Claim | Verdict | Findings |
|---|---|---|---|
| 1 | A1 §0 triangle evaluation (W or {t,a,b}, entries in {1,2,4}) | **ACCEPT** | none |
| 2 | A1 §0 two/four allowed-set rule | **ACCEPT-WITH-FIXES** | G2 (Sun(5) accounting) |
| 3 | A1 §1 Corollary W3 (W3 = W3* = ∅) | **ACCEPT** | editorial: cite "Corollary R3 (iii)" |
| 4 | A1 §2 Lemma E3 | **ACCEPT-WITH-FIXES** | S1 |
| 5 | A1 §3 Lemma PFG-t (i)–(ii) | **ACCEPT-WITH-FIXES** | S2 |
| 6 | A1 §3 Corollary L | **ACCEPT-WITH-FIXES** | S3, G2 |
| 7 | A1 §4 Lemma B | **ACCEPT-WITH-FIXES** | S4 |
| 8 | A1 §5 Theorem K7-CASEB | **ACCEPT** | none |
| 9 | TC §1 Lemma TC and the rigidity source | **ACCEPT** | optional T3 (orientation dictionary) |
| 10 | TC §2 rows R1, R3, R4, R5 and the exclusion of ({1,4,4,4}\|c\|1) | **ACCEPT-WITH-FIXES** | **T1 (mandatory for #13)** |
| 11 | TC §3 Theorem K7-TC-B | **ACCEPT-WITH-FIXES** | **T2 (mandatory)** |
| 12 | TC §4 Proposition TC-P | **ACCEPT-WITH-FIXES** | T4 (scope sentence) |
| 13 | Theorem K7-TC-A22 | **ACCEPT-WITH-FIXES** | **X1 (mandatory)**, X2, X3 |

**Totals:** 0 FATAL, 0 MAJOR, 14 MINOR.

Three of the MINORs close load-bearing citation gaps and are mandatory:
- **T2:** the union bound ≤ 5/6 at a VFC apex.
- **T1 and X1:** row R1 is needed for E = 1 inside A22.
- **G2:** the direct Sun accounting.

The other MINORs are editorial. No statement changes.

Sections not reviewed as theorems: A1 §§6–7 (Q_B, Pc5'), TC §§5–6 (Q_B') and A22 §4. They carry no existence or "passes every rule" claim.

## 2. Global findings

- **G1 (MINOR, editorial).** All three headers say "conditional on candidate RICH". This is stale status, not a premise. The governing base is verdict 1167bc4f…: RICH-v1, erratum-1 R-1 and the consolidated erratum, with FG7 in chain form (a)/(b) and the RF2 equality clause of Corollary 5/6. PFG-t uses the RF1 chain form specifically.
- **G2 (MINOR, mandatory accounting).**
  - Direct exclusions in these files use Sun(2) and Sun(3). Sun(4) never acts as the excluding instance.
  - **Sun(5) is used directly only in Corollary L.** It enters through the clause "no allowed 5-set with pairwise gcds ≤ 4", in three places:
    - the feasibility of y = 1/4 in the case 44444 (the file's §0 omits this one);
    - the kill of 44441;
    - the kill of 44444.
  - This direct Sun(5) is the locally accepted, **computer-assisted** record 2cf02436….
  - The downstream conclusion "≥ 2 entries 4" needs only the b ≤ 1 kills, which use Sun(2) and Sun(3). So CASEB, TC and A22 do not depend directly on Sun(5).
  - TC §0 lists "Sun(2)–Sun(5)", which contradicts the manifest. Its direct use is Sun(2) and Sun(3).
  - All three files reach the computer-assisted Sun(5) and Sun(6) records (2cf02436…, efe1d849…) transitively through LFC/INV/E8, VFC, D23-MIX and RICH. They must say so, in the style of RF9.
- **G3 (MINOR).** Several labels drop 5^Bz and 5^Bt; for example, "t's label 3^A w_t" appears in Lemma B, R4, TC-B and A22 (c). This is harmless and should be stated once:
  - At a W-apex and at t, every W-entry is in {1,2,4}, c is in {1,2,3} and e is in {1,2,4}.
  - Bz·Bt = 0.
  - So no factor 5 ever enters a gcd.

## 3. Justification

### A1-STRUCT

**§0, triangle evaluation.**
- All pairwise gcds are 6, so γ = 6. Each ℓ is a w, or 3^A 5^Bt w_t for t, and is odd.
- With entries 2-powers sorted p ≤ q ≤ r: τ_min = r and τ_max = min(rp, qp, pq) = pq.
- Pass: (1,1,1), (1,2,2), (1,4,4), (2,2,2), (2,2,4), (2,4,4), (4,4,4). Die: (1,1,2), (1,1,4), (1,2,4).
- So (1,a,b) passes iff a = b; A22 uses this.
- Triangles through z (ℓ_z even) are correctly excluded.
- "Allowed" here means only that the triangle passes the L1 test.

**§0, two/four rule.**
- The pairwise gcds are 2, except 4 between two fours.
- A hereditary set passes the test exactly in these cases:
  - triples need a four–four pair;
  - 4-sets need at least 3 fours, since a 4-set with ≤ 2 fours has a 3-subset with ≤ 1 four, which dies by Sun(3);
  - no 5-set passes, which is a direct Sun(5) instance.
- Ones (label w) are singletons by Sun(2).
- "Allowed" means passing this necessary test, not realisability.

**§1, Corollary W3.**
- Take the W-triangle (3, a, b) with a, b ∈ {1,2,4} (NO5).
  - τ_min = 3·lcm(a,b).
  - At apex w, τ_max ≤ 3·min(a,b), which forces a = b.
  - Then τ_max = a·min(3,a) ≥ 3a, which forces a = 4.
- That contradicts Corollary R3 (iii): u ∈ W3 has no W-four.
- So every w lies in W3, hence W3 = W ⊇ T*, which the RICH theorem excludes.
- For α* the same runs in the inverted configuration (E6, L1 via Z2 G5), with NO5 and R3 for α* and RICH's second statement.

**§2, Lemma E3.**
- The t-label 3^{A+1} 5^Bt w_t shares no prime with any W-label. It shares only 3 with z, and only when c = 3.
- Every allowed set through t is contained in {t, z}.
- Put y_z = 0 and y_t = 1, and use the E8 standard weights on the four W-neighbours, which give value ≥ 4. With N = 4 the Sun(5) branch b ≥ 4 is vacuous.
- Then val ≥ 7 > 5.
- Repair S1 records why the standard weights are legitimate at an apex with marked neighbours.

**§3, PFG-t (i).**
- Use FG7 (a) (RF1) with V_u = U_u of C^x and β = x, ordering W along a spanning tree of Γ^x.
  - T_2 = lcm·x_{u1u2}.
  - Each later k satisfies k ≤ x_{ej} ≤ 2, where j is the earlier tree-neighbour and gcd(n_e, T_m) = 6.
- So T_W = 6·∏w_u·2^s, with v3 = 1 and no factor 5.
- Connectivity is exactly what prevents k = 3; an earlier entry 4 would allow k = 3.
- Since v2(n_t) = 1, gcd(n_t, T_W) = 6, and G0 gives μ(U_t W_W) ≥ 1/6.
- U_t W_W ⊆ X_u, which (V1) keeps disjoint from D_u.
- Double-counting over right U_t-cosets, with heredity of (V3), gives Σ y_u μ(D_u) ≤ 5/6.

**§3, PFG-t (ii).**
- Equality forces:
  - μ(U_t W_W) = 1/6;
  - ∪_W D_u = G ∖ U_t W_W;
  - y(S_R ∩ W) = 1 on every right coset R in that union.
- By (V4), D_z ∩ U_t = ∅, so μ(D_z ∩ U_t W_W) ≤ 1/6 − 1/n_t < 1/6 ≤ μ(D_z).
- D_z is left-U_t-invariant, so it contains a right coset R in the occupied union.
- That S_R contains z, lies in W ∪ {z} and is allowed.

**§3, Corollary L.** I enumerated (k1, a, b) with k1 + a + b = 5.
- Kills with value 6 or more:
  - b = 1: only pairs exist in the class, giving k1 + a + 2 = 6, or 8 when a = 0.
  - b = 0, a = 1: value 6.
  - b = 2 with k1 ≥ 2: value 4 + k1.
  - b = 3 with k1 = 2: value 6.
- Kills with value exactly 5, applying (ii):
  - 11111: {z, one} has gcd 1.
  - 1^{5−a}2^a for a ≥ 2: {z, s, s'} has all gcds 2 (Sun(3)).
  - 44441 and 44444: z plus four fours has maximum gcd 4 [Sun(5)].
  - 44222 and 44122: the weight-1 sets are {f1, f2, s}, {s, s'} and {one}. {z, f1, f2, s} is allowed iff gcd(z, four) = 4, i.e. iff E + v2(x*_tz) ≥ 2. {z, s, s'} and {z, one} never are.
- Survivors: 44412 ({z, f, f, f} is allowed), 44422, 44442, and 44222/44122 when z is four-type.
- The list is complete, and it is a necessary condition only.

**§4, Lemma B.** Every case gives val > 5:

| Case | Weights / reason | Value |
|---|---|---|
| W-part all in {1,2}, a ≥ 1 | z joins the pairwise-2 block (Sun(3)) | 4 + 3/2 |
| W-part all in {1,2}, a = 0 | y_z = 1 | 7 |
| (1,1,1,4) | ones and the four at 1 | 7 |
| (1,1,2,4) | two ones and the four at 1 | 6 |
| (1,2,2,4) or (2,2,2,4), E = 1 | gcd(z, four) = 2 makes {twos, four, z} a pairwise-2 block | 13/2 |
| E ≥ 2, e = 1 | t meets only z (gcd 3), so y_t = 1 adds 1 | 6 |
| E ≥ 2, e = 2 | see below | 6 |

- In the last case, gcd(t, z) = 6 and t has gcd 2 with every two and four.
  - The allowed sets through t are exactly {t, s}, {t, f}, {t, z, s} and {t, z, f}.
  - {t, s, s'} and {t, s, f} die by Sun(3).
  - {t, z, s, f} dies through its subset {t, s, f}.
  - {z, f, s} weighs 1.
- Hence e = 4 (E3 and NO5), E ≥ 2, and the W-part is (1,2,2,4) or (2,2,2,4).

**§5, CASEB.**
- TZ (ii) for α* gives α* = 4 on T* × (W∖T*), so α ≤ 2 there.
- Lemma B at each v ∉ T* (c = 3, at least 3 entries ≤ 2) gives:
  - exactly one four;
  - E ≥ 2;
  - α_vt = 4.
- That four cannot point into T*, so |W∖T*| ≥ 2. Hence |T*| = 3 and α_{v1v2} = 4.
- The triangle (4, α_{v1a}, α_{v2a}) has two entries ≤ 2, so it is (2,2,4) and α_av = 2.
- In the t-triangle (α_ta, 4, 2), the pattern (1,2,4) dies, so α_ta ∈ {2, 4}.
- Γ^α contains K_{3,2}, so it is connected and Corollary L applies: t has at least two α*-fours.
- α*_tv ≤ 2, so at least two a have α*_ta = 4. For those, α_ta = 2.
- By the contrapositive of Lemma B, each such a has α_aa' = α_aa'' = 4. Two such a make all three T*-edges 4.
- The α*-list follows from INV and from D23-MIX (v ∉ T*).
- The mirrored case follows by INV and E6.

### K7-TC

**Lemma TC.**
- Both sides are invariant under a common left translation.
- With g_a = 1, L_a^(u) = U_a U_u = X_u^(a), and both directions hold; (V1) then gives D_j ∩ D_u = ∅.

The orientation is correct in both families. In C^α* the objects are:
- U*_j = g_j U_j g_j⁻¹ and g*_j = g_j⁻¹;
- L*_j^(u) = g_j⁻¹ U*_j U*_u;
- the normalisation g*_a = 1 is the left translation by g_a;
- at apex a, μ(D*_j) = α_aj/6 and μ(X*_u) = α*_au/6.

I checked all four applications against this:

| Application | Row used | (u, a, j) | Disjointness obtained | Masses at apex |
|---|---|---|---|---|
| TC-B (i) | R4 (α*) at v | (v, a, z) | D*_z ∩ D*_v = ∅ at a | α_aj |
| TC-B (ii) | R5 (α*) at a_i | (a_i, v, z), (a_i, v, a3) | D*_z, D*_a3 disjoint from D*_ai at v | α_vj |
| TC-P | R1 (α) at u3, u5 | (u3, u4, u2), (u5, u4, u1) | D_u2 ∩ D_u3 = ∅, D_u1 ∩ D_u5 = ∅ at u4 | α*_{u4 j} |
| A22 | R1/e = 1 variant at w_i | (w_i, u, w_i') | D_wi' ∩ D_wi = ∅ at u | α*_uj (dual: α_uj) |

The rigidity source applies the RF2 equality clause to each y_i on the same fibre C. S_C is allowed by LFC (c).

**Rigid rows.**
- **R1** (gcds f–f 4, z–f 4, z–t 6, all others 2).
  - The maximal allowed sets are exactly as listed.
  - y_A and y_B are feasible with value 5, and y_A − y_B = ½([f1] − [f2]). So L_f1 = L_f2.
  - If E = 1, gcd(z, f) drops to 2 and only removes allowed sets. Since y_z = 0, y_A and y_B stay feasible, so **R1 holds for every E ≥ 1**.
- **R3** (z–f 4, t–f 4, z–t 12; maximal sets {f, z, t, s_i} and {s_i, s_j}).
  - [f] = [t].
  - A weight-1 set through z needs f under y_A, and then t.
  - This needs E ≥ 2.
- **R4.** The one o is coprime to everything. y_i has value 5, so every fibre without o contains f1, f2 and f3. z and t are coprime to o, so L_z, L_t ⊆ L_fi. This holds for any E.
- **R5.** The same argument with i = 1, 2 gives L_z, L_s ⊆ L_f1 ∩ L_f2. (L_t ⊆ L_f1 ∩ L_f2 also holds; the file does not claim it.)
- **Exclusion of ({1,4,4,4}|c|1).** With c ∈ {1,2} and Bz·Bt = 0, t's label is coprime to everything. y = (o: 1, fours: 1/3, t: 1) is feasible with value 6.

**TC-B.**
- Preliminaries.
  - (1,1,2) on T* dies by the triangle rule.
  - (1,1,1) makes the α*-row at a have W-part {1,1,4,4}, with value 2 + 4 = 6.
  - α*_ta = 1 makes (1, α*_tv, 4) die, so α*_ta ∈ {2, 4}.
- **(i)** Suppose α*_{v1v2} = 1.
  - The α*-row at each v is ({1,4,4,4}|c|e) with c ∈ {1,2}. The exclusion forces e = 2, so it is R4.
  - At a in C^α*, the masses are a', a'' 4/6; v's 2/6; z 3/6; t α_at/6, with α_at even.
  - A coset containing both v's has S = {v1, v2}: any third element of {a', a'', t} has gcd exactly 2 with both v's (Sun(3)), and z is excluded by disjointness.
  - Let R be the cosets outside Z := D*_z and V2. Then μ(R) ≥ 4/6 − 3/6 = 1/6.
  - Also 4/6 ≤ 2μ(V2) + μ(R).
  - So μ(∪) ≥ 5/6 + μ(R)/2 ≥ **11/12**.
- **(ii)** Suppose the T*-pattern is (1,2,2).
  - The α*-rows at a1 and a2 are ({1,2,4,4}|3|e) with e ∈ {2,4}, i.e. R5.
  - At v in C^α*, the masses are a's 2/6, v' 4/6, z 3/6, t 4/6.
  - Every a has gcd 2 with everything; v'–z and v'–t are 4, z–t is 12.
  - The only cosets with two a's are {a1, a2}.
  - Let K be the measure of the {a1, a2} cosets and N the cosets outside Z and K. Then μ(N) ≥ max(1/6, 4/6 − 2K).
  - So μ(∪) ≥ 3/6 + K + μ(N) ≥ **11/12**, with the minimum at K = 1/4.
- **Gap (T2).** Both contradictions need μ(∪_{j≠a} D_j) ≤ 5/6 at a W-apex of C^α*. (V4) alone gives < 1, which does not contradict 11/12.
  - Accepted RICH states FG7 only as an index statement. The union bound inside the proof of Corollary 5/6 is on the LFC side.
  - The needed lemma follows in three lines from G0, FG7 (b) and (V1); see the repair.

**TC-P.**
- R1 at u3 (fours u2, u4; e = 2) and at u5 (fours u4, u1; e = 2) give, at u4 in C^α, D_u2 ∩ D_u3 = ∅ and D_u1 ∩ D_u5 = ∅.
- The masses at u4 are u1, u2 4/6 and u3, u5 2/6.
- If K ≤ 2/6 the union is ≥ 8/6 − K ≥ 1. If K ≥ 2/6 it equals 1. Either way this contradicts (V4).
- The proof uses only these entries. It is subsumed by A22, since Pc5' has F = C5, F* = P5 and every degree (2,2).

### K7-TC-A22

- **(a)** F is 2-regular on 5 vertices, so it is C5. F* is edge-disjoint and 2-regular, so it is the complementary C5.
- **(b)** Twin rule: α_uv = 1 forces α_uw = α_vw for all w, so u and v have the same F-neighbourhood. Non-adjacent vertices of C5 share exactly one neighbour, so this is impossible. The same holds for α* with F*.
- **(c), e = 1 variant.**
  - t meets only z, with gcd 3.
  - y1 and y2 are feasible for every E. The maximal sets without t are {f1, f2, z, s} and {s1, s2}; for E = 1 they are also {f1, f2, s} and {f1, f2, z}.
  - y1(S) = y2(S) ⇔ #f = 2·#s ⇔ (#f, #s) ∈ {(0,0), (2,1)}.
  - For e = 2, (c) cites R1.
  - **E ≥ 2 is not available in A22.** Lemma B never fires when every degree is (2,2), and LZ gives E ≥ 2 only when α_zt = 2. So X1 is needed; T1 supplies it.
- **(d)** Γ^α is the complement of F, which is F*, so it is connected and |P*| ≥ 2. Symmetrically |P| ≥ 2, and P ∩ P* = ∅.
- **§2.** The count is the TC-P count with (w1', w2') in place of (u1, u2), and is ≥ 1, contradicting (V4). In the dual version in C^α*, the masses at u are 4/6 on the F-neighbours and 2/6 on the F*-neighbours.
- **§3.** Every 2-set in C5 has a vertex with no neighbour in it. Then |P| = 2 or |P*| = 2. u ∈ P is harmless, since u's t-mass is unused.

## 4. Exact repairs

**G1.** In every header and §0 of the three files, replace "conditional on the candidate(s) K7-D23-RICH-v1.md … (now in parent review)" and "at their candidate scope" with:

"on the accepted RICH base (verdict 1167bc4f…: RICH-v1 + erratum-1 R-1 + consolidated erratum; FG7 in chain form (a)/(b) per RF1, Corollary 5/6 with the RF2 equality clause)".

**G2.**
- In A1 §0, replace the Sun sentence with:

  "Direct: Sun(2), Sun(3) through LFC (c)/VFC (V3); Sun(5) directly exactly in the no-5-set clause of the two/four rule, used in Corollary L for the feasibility of y = 1/4 in 44444 and for the kills of 44441 and 44444 (this is the computer-assisted record 2cf02436…). The consequence 'at least two entries 4' uses only the b ≤ 1 kills (Sun(2), Sun(3)). Transitive: through LFC/INV/E8, VFC, D23-MIX and RICH, the closure reaches the computer-assisted Sun(5)/Sun(6) records 2cf02436…, efe1d849…. No Sun(7)."

- In TC §0 and A22 §0, replace "Sun(2)-Sun(5) only through …" with:

  "Direct: Sun(2), Sun(3) only; Corollary L enters only through 'at least two entries 4' (Sun(5)-free); transitive closure as in A1-STRUCT §0."

**G3.** Add to A1 §0:

"At a W-apex and at t, no W-entry, c or e is divisible by 5, and Bz·Bt = 0; hence 5^Bz and 5^Bt never enter a gcd and are suppressed in labels."

**S1 (E3).** After "give >= 4 (E8)", insert:

"(subset form as in RICH RF4: W-label gcds equal entry gcds; y_z = 0; t's label shares no prime with any W-label, so allowed sets through t lie in {t, z}; with four neighbours the Sun(5) branch b ≥ 4 is vacuous)".

**S2 (PFG-t).**
- Replace "as in FG7 each later factor satisfies" with:

  "by FG7 (a) (RF1; N = Q = W, V_u = U_u of C^x, β = x ≤ 5) each later factor satisfies".

- After "so S_R contains z and is allowed (VFC (V3))", add:

  "; S_R ⊆ W ∪ {z} (apex t) and S_R ∩ W is an allowed W-set of y-weight 1".

**S3 (Corollary L).**
- Replace the heading "(allowed t-rows)" with:

  "(t-rows not excluded by PFG-t: a necessary condition, no realisability claim)".

- After "44444 (y = 1/4)", insert:

  "(feasible since no 5-set of fours is allowed [Sun(5)])".

**S4 (Lemma B).** Replace "(1,1,1,4): W-alone 3 + 4; (1,1,2,4): 2 + V24(1,1) = 6." with:

"(1,1,1,4): y = 1 on the three ones and the four, 0 on z, t: val = 7. (1,1,2,4): y = 1 on the two ones and the four, 0 on the two, z, t ({two, four} weighs 1): val = 6."

**T1 (TC §2 heading).** Replace "(E >= 2 throughout; each value-5 weight …)" with:

"(R3 assumes E ≥ 2. R1, R4, R5 and the last item hold for every E ≥ 1: the only E-dependent gcd at u is gcd(z, four) = 2^min(E+v2 c, 2), and lowering it only removes allowed sets, so the displayed weights stay feasible. Each value-5 weight is feasible and Corollary 5/6 gives ≤ 5, so it is optimal.)"

**T2 (TC, before §3).** Insert:

"**Lemma FG-V.** Let a ∈ W, C ∈ {C^α, C^α*}, g_a = 1. Then μ(∪_{j≠a} D_j^(a)) ≤ 5/6. *Proof.* Y := ∩_{j≠a} U_j (subgroups of C). U_aY ⊆ U_aU_j = X_j^(a), which is disjoint from D_j^(a) by (V1). G0 gives μ(U_aY) ≥ 1/gcd(n_a, [G:Y]); FG7 (b) (N = Q = V∖{a}, V_j = U_j of C, β = the α-matrix of C ≤ 5 by E1, resp. INV (b) + E1) gives gcd(n_a, [G:Y]) | 6. QED"

Then, in §3 (i) and (ii), replace "FG7 for C^alpha* at a (resp. v)" with "Lemma FG-V for C^α* at a (resp. v)".

**T3 (optional, TC §0).** Add the orientation dictionary from §3 above.

**T4 (TC-P statement).** Replace "no configuration has its data" with:

"no (a1) configuration has α-rows ({2,2,4,4}|3|2) at u3, u5 with fours {u2,u4}, {u4,u1} and α*_{u4u1} = α*_{u4u2} = 4, α*_{u4u3} = α*_{u4u5} = 2; in particular Pc5' is not realised (subsumed by K7-TC-A22)".

**X1 (A22 1(c)).** Replace "for e = 2 this is R1 of K7-TC;" with:

"for e = 2 this is R1 of K7-TC, valid for every E ≥ 1 (TC §2 as repaired by T1; Case A does not force E ≥ 2);"

**X2 (A22 1(b)).** Replace "The same for alpha* on F." with:

"The same argument with α*, F* in place of α, F shows α* ≠ 1 on W."

**X3 (A22 1(d)).** Replace "Gamma^alpha = F* -complement... precisely {uv : alpha_uv <= 2} = the complement of F, a 5-cycle, is connected" with:

"Γ^α = {uv : α_uv ≤ 2} is the complement of F among the pairs of W, i.e. the 5-cycle F*, hence connected".

**Editorial, navigation only.**
- In the A1 title and §6, add: "pass the listed checks of §6 only; Pc5' is excluded by TC-P and K7-TC-A22".
- Mark TC §5's "counts are satisfiable / integral solutions" as unverified navigation, not premises.

## 5. Accepted scope, imports, and what is not concluded

**Scope.** Everything below holds in setting (a1) only (E, A ≥ 1, Bz·Bt = 0, any w's, arbitrary groups via R0), once the fixes are applied.
- **A1-STRUCT:**
  - W3 = W3* = ∅, and every W–W and W–t entry lies in {1,2,4}, in both orientations.
  - PFG-t and Corollary L hold in both orientations under connectivity of Γ^x. Their survivor list is a necessary condition.
  - Lemma B holds at every u ∈ W in either orientation.
  - CASEB holds for T = W ≠ T*, and in the mirror case by INV/E6.
- **K7-TC:**
  - Lemma TC holds for any configuration.
  - The rows are local necessary consequences at u ∈ W.
  - TC-B gives α*_{v1v2} = 2 and α* = 2 on T* in Case B, and in the mirror case by INV/E6.
  - TC-P holds for the data stated in T4.
- **K7-TC-A22:** Case A with every W-vertex of four-degree type (2,2) is excluded.

**Imports actually used.**
- R0, L0.1, L1 (inverted configuration via Z2 G5), LFC (a)–(d), INV, VFC (V1)–(V4), E8 (in E3 only), and the D23-MIX conclusions.
- From RICH: G0, FG7 (a)/(b), Corollary 5/6 with its equality clause, NO5, Corollary R3, TZ, and Theorem RICH.
- Direct and transitive Sun use is as in G2.

**Not concluded.**
- Case A with a vertex of four-degree type other than (2,2). (Remark only, not accepted as a claim here: the list (3,1)/(1,3)/(2,1)/(1,2) in A22 §4 is complete given Lemma B and INV, because degree 0 and (1,1) are impossible.)
- The Case B residue. Q_B and Q_B' are local-test navigation and carry no existence or completeness claim.
- (a2), K7-A2-FIVE, K6.2*, K7 and Sun(7) all remain OPEN.
- There is no novelty, Lean or human-review claim.
