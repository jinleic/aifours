**Boundary.** I read RICH together with its mandatory erratum first. R-1 withdraws the NO5(a) Sun(6) six-set branch and the c = 3 propagation. Nothing else in the file cites them: R3, TZ and LZ use only the statement of NO5. I reviewed against the embedded texts only. I did not recompute any SHA256 (no tools) and ran no computation. Neither candidate's conclusion is used as a premise for the other.

---

## A. K7-D23-RICH-v1 + erratum-v1 (setting a1)

| Item | Verdict | FATAL/MAJOR/MINOR |
|---|---|---|
| G0 | ACCEPT | 0/0/0 |
| FG7 | ACCEPT-WITH-FIXES | 0/0/1 (RF1) |
| Cor 5/6, including the equality clause | ACCEPT-WITH-FIXES | 0/0/1 (RF2) |
| NO5 (with R-1) | ACCEPT-WITH-FIXES | 0/0/1 (RF3) |
| R3: all branches, S1–S4 weights, equality conclusion, Cor R3 | ACCEPT-WITH-FIXES | 0/0/2 (RF4, RF5) |
| TR | ACCEPT | 0/0/0 |
| CC | ACCEPT | 0/0/0 |
| Theorem K7-D23-RICH | ACCEPT-WITH-FIXES | 0/0/1 (RF6) |
| TZ (i)–(iii) | ACCEPT-WITH-FIXES | 0/0/1 (RF7) |
| LZ | ACCEPT-WITH-FIXES | 0/0/1 (RF8) |
| §0 / R-2 import accounting | ACCEPT-WITH-FIXES | 0/0/1 (RF9) |

**Overall RICH: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 9 MINOR.** No statement changes.

### Verification record

**G0.** μ(HY) = [G:H∩Y]/(ab) = k·lcm(a,b)/(ab) = k/gcd(a,b) with k ≥ 1.

**FG7.**
- z and t come first in the chain. Then T₂ = lcm(n_z,n_t)·β_zt with β ≤ 5, so the prime-to-30 part is w_z w_t.
- At each unmarked step e:
  - 6 | T_m, and the prime-to-30 part of T_m is a product of other w's, so gcd(6w_e, T_m) = 6.
  - μ(V_eW_m) = k/6 ≤ μ(V_eV_j) = β_ej/6 for every earlier j, so k ≤ 5.
- The marked-first ordering is load-bearing. If a marked vertex came later, gcd(n, T_m) could exceed 6 (for example 12), and then k ≤ 10 could be 7.
- Final step: gcd(6w_u, T_Q) = gcd(6, T_Q) = 6.

**Cor 5/6.**
- Suppose g_j a g_j⁻¹ ∈ g_jU_jU_u. Then g_j⁻¹ ∈ U_jU_u, so g_j ∈ U_uU_j, so g_jU_j meets U_u, which is impossible. This uses left cosets only; no normality is assumed.
- M = n_u·μ(U_uW*) ≥ n_u/gcd(n_u,[G:W*]) = n_u/6, by G0 and FG7 with Q = N. This is the omitted-set bound μ ≥ 1/6.
- (n_u/6)·val = Σ_C Σ_{S_C} y ≤ #{occupied fibres} ≤ n_u − M ≤ 5n_u/6. So val ≤ 5, non-strict, as the file states.
- If val = 5, every occupied fibre has S_C-weight exactly 1. In addition M = n_u/6, and every fibre outside W*U_u is occupied.
- For α*: the inverted W* is a conjugate of ∩U_j, so FG7 applies with V_j = U_j and β = α.

**NO5.**
- (a), Bz = 0 (this also covers a 5-marker on t): gcd(5w_v, 2^E c w_z) = 1, so val = 5+c ≥ 6.
- (a), Bz ≥ 1:
  - 5∤e gives val 5+e.
  - e = 5 with some W-entry a ≠ 5 gives val 5+a.
  - R-1 branch: INV gives α* = 1 on the four W-neighbours and on t. The inverse labels are w_v, 3^A w_t and 2^E5^{Bz}c*w_z.
  - If c* = 3, only {z,t} is compatible. y = 1 on W∪{z} gives val 7.
  - If c* ∈ {1,2}, all labels are pairwise coprime and val = 5+c* ≥ 6.
  - This branch uses Sun(2) only and works for every c.
- (b): an entry in {1,2,4} is coprime to λ_t = 3^A5^{Bt+1}w_t (val 5+a), so all four W-entries are 3. Then:
  - Coprime (z,t): val 5+c.
  - c ∈ {1,2}, Bz ≥ 1: weights (1/3 on the threes and t, 2/3 on z) give 4+5/3+2c/3 ≥ 19/3.
  - c = 3, Bz = 0: all gcds are 3, val 20/3.
  - c = 3, Bz ≥ 1: gcd(z,t) = 15. The allowed sets are the sets of size ≤ 3 and the 4-sets containing {z,t}. With y_z = 0, val = 17/3. This lies in (5,6), so this branch genuinely needs Cor 5/6.

**R3, label gcd matrix.**
- (a,a′) = gcd(a,a′).
- (z,a) = 1, 2, 3^{[c=3]}, 2^{min(E+v₂c, 2)} for a = 1, 2, 3, 4.
- (t,a) = 1, 2^{[e even]}, 3, gcd(e,4) for a = 1, 2, 3, 4.
- (z,t) = 2^{min(E+v₂c, v₂e)}·3^{[c=3]}.
- No 5 is ever shared, because Bz·Bt = 0, W-entries ≤ 4, c ≤ 3 and e ≤ 4.

**R3, what I checked.** I checked every weight vector against all hereditary allowed sets:
- Exact-gcd-2 triples are excluded: {2,2,z}; {b,z,t} when c ∈ {1,2} and e = 2; {b₁,b₂,t}; {2,4,z} when E = 1.
- z/t-sharing sets are allowed: R3′ when z–t ∈ {6,12}; {z,t,a,a′}; {b,z,t} when c = 3 and e is even.
- 5-sets are excluded hereditarily, since each contains a 4-subset missing z or t with all gcds 3.
- E matters only through z–4 and through z–t at e = 4. The only branch where allowedness changes, (c=3, k₃=2, e odd, (2,4)), is split into E = 1 and E ≥ 2 in the file.

**R3, branch values.** Every kill is strictly above 5.
- c ∈ {1,2}:
  - k₃ = 1: ≥ 6.
  - k₃ = 2: (1,1) 5+c; (1,b) 4+b; (2,2) 5+c/2; (2,4) 6; (4,4) 7.
  - k₃ = 3: b = 1 gives ≥ 16/3; b ∈ {2,4} with e odd gives ≥ 16/3; e = 2, b = 2 gives 5+c/3; e = 2, b = 4 gives 19/3; e = 4 gives ≥ 17/3.
  - k₃ = 4: ≥ 16/3.
- c = 3:
  - k₃ = 1: ≥ 6.
  - k₃ = 2, e odd: (1,1) and (2,2) give 5+e/3; (1,b) gives ≥ 17/3; (2,4) gives 6+e/3 for E = 1 and 17/3+e/3 for E ≥ 2; (4,4) gives 17/3+e/3.
  - k₃ = 2, e even: (1,b), (2,4) and (4,4) give ≥ 6. (1,1) gives 6 at e = 4 and survivor S3 at e = 2. (2,2) gives 11/2 at e = 4 and survivor S4 at e = 2.
  - k₃ = 3: e odd gives 5+e/3 or ≥ 17/3. With e even: b = 1 gives 16/3 at e = 4 and survivor S2 at e = 2; b ∈ {2,4} gives ≥ 16/3.
  - k₃ = 4: e odd gives 5+e/3; e = 4 gives 16/3; e = 2 is survivor S1.

**R3, survivors** (all with c = 3, e = 2, z–t = 6).

| Survivor | val | Allowed sets containing t with weight 1 |
|---|---|---|
| S1 | 4+1 = 5 | only {z,t,a,a′} |
| S2 | 3+1+1 = 5 | only {z,t,a,a′} |
| S3 | 3+2 = 5 | subsets of R3′ that contain z |
| S4 | 3/2+3/2+2 = 5 | R3′ and {b,z,t} |

Every such set contains z. By the equality clause, every fibre meeting g_tU_t also meets g_zU_z. Cor R3 (i)–(iii) follow.

**TR.** Both directions are pure set identities: g_tU_tU_u ⊆ U_zU_u ⇔ U_zg_tU_t ⊆ U_zU_u. They use left U_u-cosets only and no normality. D_u ∩ X_u = ∅ is (V1).

**CC.**
- The local gcds are 3 on T*∪{t}, 1 between T* and O*, and in {1,2} on O*∪{t}.
- Every S_R is either a subset of T* of size ≤ 3, a singleton of value 1, or at most two elements of value 2.
- The weighted mass is (|T*|+|O*|+1)/6 = 1, but (V4) gives < 1.
- The argument uses right U_z-cosets and VFC, and does not need |T*| ≥ 3.

**Theorem K7-D23-RICH.**
- Every object lives in the original configuration at z with g_z = 1, and VFC q = α* there (INV b).
- Chain: R3 at u ∈ T* gives the fibre condition; TR turns it into D_t ∩ D_u = ∅; CC then gives the contradiction.
- The second statement follows by inversion (E6).

**TZ.**
- (i): τ_min is a multiple of lcm(3, s) = 3s, while τ_max ≤ x·min(3,s) = xs at apex z. So x ≤ 2 dies, and x = 5 is excluded by NO5.
- (ii): an entry 3 would put v in W3 ⊆ T, so the entries are 4. Each u ∈ T then has a 4, so u ∉ W3, and W3 = ∅.
- (iii): the connected spanning graph K(T, W\T) has every edge with α = 4, hence α* ≠ 4, hence no edge crosses the cut (T*, W\T*). So T* ∈ {∅, W}, and |T*| ≥ 3 forces T* = W.

**LZ.**
- From 5n_z/2 ≤ 3(n_z−M) − (n_z s/6 − (M−1)) we get M ≤ n_z(3−s)/12 − 1/2.
- G0 gives M ≥ n_z/g, hence g > 12/(3−s).
- Since 5∤T*_W (all k ≤ α* ≤ 4 by NO5), g = 3·2^{min(1+E, v₂T*_W)}.
- s = 1 gives v₂ ≥ 2. s = 2 gives E ≥ 2 and v₂ ≥ 3.
- If Γ*₁ were connected, ordering W along a spanning tree would make every k_m = 1, so v₂ = 1, a contradiction.

### Findings and minimal repairs (all MINOR)

**RF1 (FG7 ↔ LZ).**
- Problem: FG7 is stated only for Q ⊆ V\{u} with u ∈ W, and its proof bounds k only through j₁. LZ uses Q = W at the marked apex z, and k_m ≤ α*_ej for every earlier j. Both are valid by the same inclusion V_eW_m ⊆ V_eV_j.
- Repair: split FG7 into two parts.
  - (a) For any non-empty Q ⊆ V ordered marked-first: T_Q = n_{j₁}·β_{j₁j₂}·∏k_m, with k_m ≤ min over earlier j of β_ej (≤ 5), and the prime-to-30 part of T_Q is ∏w_j.
  - (b) For u ∈ W\Q: gcd(n_u, T_Q) | 6.

**RF2 (Cor 5/6).**
- Define the weight of a fibre C ≠ g_uU_u as Σ_{j∈S_C} y_j.
- State the equality conclusion as: "Σ_{S_C} y_j = 1 whenever S_C ≠ ∅."
- Add: "normalising by g_u⁻¹ conjugates W* without changing its index; for α*, W* is a conjugate of ∩U_j."

**RF3 (NO5 for α*).** Spell out the role swap:
- In R-1 for α*, use c = α_uz ∈ {1,2,3} (D23-MIX for α) and LFC(d) of the original configuration.
- (b) for α* uses Cor 5/6 for α*.

**RF4 (R3 standard weights).**
- Problem: R3 applies E8 to a subset of the unmarked neighbours at an apex that also has the marked neighbours z and t. This needs justification.
- Repair: add the justification:
  - Among unmarked neighbours, label gcds equal α-gcds.
  - z and t carry weight 0, and allowedness is hereditary.
  - This is the accepted subset-form bound (LFC verdict item 3; K63 verdict H5).
  - With ≤ 3 such neighbours, the Sun(5)-dependent b ≥ 4 branch is vacuous.

**RF5 (R3 text).**
- Delete "R3′ contributes at most max(3, e)". It is an unproved optimality remark and is not needed.
- State that S1–S4 are survivors of this local test only, not claimed realisable or LP-optimal.

**RF6 (§6/§9).**
- §6 says the abstract pattern "has T* = W = W3 and is therefore not realisable". The note is unembedded and unreviewed, so that premise is unchecked here.
- Reword as: "Navigation only: if the pattern has T* ⊆ W3 or T ⊆ W3*, it is not realised by any configuration. No other local pattern is excluded."
- §9's remark that several rows without a W-three pass Cor 5/6 with zero z-weight is unproved and backed by no finite program. Mark it unverified and non-load-bearing.

**RF7 (TZ).**
- In (i), cite D23-MIX for s ∈ {1,2}, NO5 for x ≠ 5, and Z2-erratum G5 for the α* version.
- Replace the garbled sentence in (iii) with the cut argument given in the verification record.

**RF8 (LZ).**
- Cite LFC(b): U_z holds no piece.
- Cite D23-MIX for s ∈ {1,2}.
- Say explicitly that the L_j argument is rerun only for j ∈ W, so fibres of W*U_z may carry the t-piece.
- Cite FG7(a) as repaired in RF1.

**RF9 (imports).**
- §0's "Not used: ROW-1" and R-2's "Sun(5)/Sun(6) only inside E8" are true for direct use only.
- The imported D23-MIX conclusion rests on ROW-1, the ROW-1-deg transfer (Z2 G2), D23-CENTER, T/F7/VFC and LFC. Their closure contains the accepted computer-assisted Sun(5) and Sun(6).
- Add one sentence stating this; see section C.

---

## B. K7-D23P-v1 (setting a2)

| Item | Verdict | FATAL/MAJOR/MINOR |
|---|---|---|
| ROW-2 transfer to z (§1) | ACCEPT-WITH-FIXES | 0/0/1 (PF1) |
| Row trichotomy exhaustive (including α_zt = 5 and α_zp = 5) | ACCEPT | 0/0/0 |
| (a′) exclusion via inverse LFC | ACCEPT | 0/0/0 |
| Fours-position count / choice of Q | ACCEPT | 0/0/0 |
| M1: both tables, INV step, F7 orientation | ACCEPT-WITH-FIXES | 0/0/1 (PF2) |
| M2 | ACCEPT | 0/0/0 |
| Theorem K7-D23P | ACCEPT-WITH-FIXES | 0/0/1 (PF3) |

**Overall D23P: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 3 MINOR.**

### Verification record

**ROW-2 transfer, label gcds at z.**
- (u,u′) = gcd(α,α′).
- (u,t) = 2^{min v₂}·3^{[3|α_zu]}.
- (u,p) = 2^{min v₂}·3^{[3 | both]}·5^{[5|α_zu]}.
- (t,p) = 2^{min(v₂α_zt, v₂α_zp)}·3^{[3|α_zp]}·5^{[5|α_zt]}.

This is identical to ROW-2's matrix at w. ROW-2's proof, including erratum K2, reads only these gcds, the ROW-U-deg/E8 weights and LFC(d). The apex index enters only through 1 − 1/n. H35 ("no e ≥ 2") is never read: z's 2-part never enters a neighbour label, and r_t, r_p are odd in both settings. The α* version is ROW-2 at z in the inverted configuration (E6).

**Trichotomy.**
- k₅ ≥ 1 gives (a′). k₅ = 0 and k₃ ≥ 1 gives (b′). Otherwise every W′-entry is in {1,2,4}, giving (c′).
- The (c′) proof also kills α_zt ∈ {3,5} and α_zp ∈ {3,5}: the offending marked label adds +3 or +5 to min(4,4), giving ≥ 7.
- (a′) and (b′) are disjoint.
- In (b′), α_zt = 5 is not excluded, and it is not needed.

**(a′) exclusion.**
- INV gives α* = 1 on W′∪{t}. With c′ = α*_zp, gcd(λ*_t, λ*_p) = 3^{[c′=3]}.
- If c′ = 3, val = 7. Otherwise val = 5+c′ ≥ 6, for every c′ ∈ {1,2,4,5}.
- This uses Sun(2) only. For α*, use LFC of the original configuration.

**Positions.**
- α*_zj = 4 forces α_zj ≤ 2.
- For a ∈ T, q_a ≤ 3 and q_a ∈ {1,2,4}, so q_a ∈ {1,2}.
- |T| = 4: at most two positions remain, which is impossible.
- |T| = 3: the fours are exactly at {o,t,p}, so Q = {o,p}.
- |T| = 2: α_zp = 3 removes p, so the fours are exactly at {o₁,o₂,t}, and Q = {o₁,o₂}.
- t is correctly never put in Q. With t, the α-triangle term 3/gcd(3, ℓ_t) = 1 and the inverse local index of t shares 3 with that of a.

**M1, α-triangle (3, s_b, x).** Here τ_min = lcm(3, s_b, x/gcd(x, 2^E w_z)) and τ_max = min(x·s_b, s_b·min(3,x), 3·min(s_b,x)).

| x | Result |
|---|---|
| 1 | dies: 3s_b vs s_b |
| 2 | dies: 3s_b vs 2s_b |
| 3 | survives |
| 4 | survives, except s_b = 1 with E = 1, which dies (6 > 3) |
| 5 | dies: 15s_b vs 3s_b (z has no 5 in a2) |

So x ∈ {3,4}.

**M1, α*-triangle (q_a, 4, x*).** Here τ*_min = lcm(4, x*/gcd(x*, r_z)) and τ*_max = min(x*·q_a, 4·min(q_a,x*), q_a·min(4,x*)).

| x* | Result |
|---|---|
| 1 | dies: 4 vs q_a |
| 2 | survives iff q_a = 2 (4 vs 2q_a) |
| 3 | dies: 12 vs ≤ 6 |
| 4 | survives |
| 5 | dies: 20 vs ≤ 10 |

INV with x ≥ 3 forces x* = 2, hence q_a = 2.

**F7 orientation.** In the inverted configuration at z with g*_z = 1, the pair (a,b) is forced: 4·6 ≥ 6·2·2. So X*_a ⊆ X*_b, consistent with the measures 2/6 ⊆ 4/6. The reverse pair would need 48 ≤ 24 and is not forced.

**M2.**
- μ(Y*_a) = 4/6 and μ(D*_a) = α_za/6 = 3/6.
- The inverse local index d*_j equals α_zj·r_j.
- 3w_a is coprime to s_b r_b, so D*_a ∩ D*_b = ∅. Hence each D*_b ⊆ Y*_a\D*_a, which has measure 1/6.
- A single s_b = 2 already gives mass 2/6. Two s_b = 1 sets have coprime r_b, so they are disjoint with mass 2/6.

**Theorem.**
- (a′) is excluded.
- (c′)/(c′) is excluded by D23-CENTER; its literal scope includes a 5-marker on a third vertex.
- (b′)/(c′) is excluded by M1–M2, and (c′)/(b′) by inversion.
- So both rows are (b′), which gives the stated "more precisely" clauses. R0 lifts the result to arbitrary groups.

### Findings and minimal repairs (all MINOR)

- **PF1.** In §1:
  - display the six-label gcd matrix above;
  - state that H35 is not read by ROW-2's local proof;
  - list K7-35 erratum K2 as part of ROW-2;
  - mirror the wording of Z2 G2 / NO4 X-6.
- **PF2.** In M1:
  - insert the two exact tables above, including the E- and s_b-dependence at x = 4;
  - note that x = 5 dies only because z has no 5-part in (a2) (contrast NO4 X-11);
  - move M2's "g*_z = g_z⁻¹ = 1, U*_z = U_z" sentence before the F7 step.
- **PF3.** §0 should:
  - list L0.3 (LFC erratum E1), which M2 uses;
  - state the transitive closure: ROW-2 → ROW-U-deg/E8 → Sun(5)/(6).

---

## C. Import closure

- **RICH, direct imports:**
  - R0, L0.1 and the K7 definition;
  - LFC (a)–(d), INV (a)(b);
  - LFC erratum E1, E2, E6, E7, E8;
  - LFC verdict item 6;
  - L1 and VFC (accepted by 73a25ba6…, applied to the inverted configuration via Z2 G5);
  - the D23-MIX conclusion (verdict d3453de1…).
- **RICH, direct Sun instances after R-1:** Sun(2), Sun(3) and Sun(4) only. R-2 is correct on this point.
- **D23P, direct imports:**
  - LFC, INV, E1, E2, E6, E7;
  - ROW-2, by proof transfer (verdict 1a1c6390…);
  - D23-CENTER at its literal scope;
  - L1, F7 (addendum A1), VFC, L0.3, R0.
- **D23P, direct Sun instances:** Sun(2) only.
- **Transitive closure of both:** through the accepted packages (ROW-U/E8, ROW-1 with K7-M1 erratum and verdict 7121cee…, ROW-2, D23-CENTER, LFC), it reaches Zhu's Sun(3)/(4) and the locally accepted, computer-assisted, model-reviewed Sun(5) (2cf02436…) and Sun(6) (efe1d849…).
- **Not used:** no Sun(7) inside any subgroup (at most 6 pieces per LFC or VFC fibre), no minimal frame, no FH, no RPLP LP, no probe or census.

## D. Scope if accepted

- **RICH:** no (a1) configuration has T* ⊆ W3 or T ⊆ W3*. The structural constraints of §9 hold for the residue. The abstract obstruction P is excluded only as a non-realizability consequence, conditional on P having that property, and no other local pattern is excluded.
- **D23P:** no (a2) configuration has a 4-type z-row in either orientation, so both z-rows are (b′).
- **Still OPEN:**
  - the (a1) residue, which needs D_t ∩ D_u = ∅ for u ∈ T* with no W-three in its α-row, or a count that tolerates such u;
  - (a2) with both rows (b′);
  - shared 2/3 markers with a 5-marker elsewhere;
  - the full K7 residue;
  - K6.2* (including e_d ≥ 4);
  - Sun(7).
- This is a model referee report on the written text, not Lean or human review. It makes no novelty, significance or Sun(7) claim.
