# Repair review: `K7-A1-A2-delta-erratum-v1.md` (0e477743…)

I only read the texts embedded in the request. I did not hash any file. I spot-read the Old→New anchors against the embedded originals, and each one occurs where the overlay says it does. I re-derived only the new consumer dependencies. W3, CASEB and F1–F7 were not re-reviewed.

**Verdicts**

| Obligation | Verdict |
|---|---|
| O1: R1 at E = 1 | **ACCEPT_REPAIRS** |
| O2: Lemma FG-V | **ACCEPT_REPAIRS** |
| O3: auxiliary-scope repair | **ACCEPT_REPAIRS_WITH_FIXES** |
| O4: transfer and dependency map | **ACCEPT_REPAIRS_WITH_FIXES** |

Findings: **0 FATAL, 0 MAJOR, 7 MINOR, plus 4 optional.** No MINOR is load-bearing and none changes a quantifier.

## O1: R1 at E = 1 (TC.3, TC.4, A22.3): ACCEPT_REPAIRS

**Gcd matrix at u.** The labels of {f1, f2, s1, s2, z, t} are 4w, 4w, 2w, 2w, 3·2^E·5^Bz·w_z and 2·3^A·5^Bt·w_t. Here Bz·Bt = 0 and no W-label carries a 5. All 15 gcds:
- f1–f2 = 4.
- f–s, s1–s2, f–t, s–t and z–s are all 2.
- z–t = 6.
- z–f = 2^min(E,2).

Only z's label depends on E. So TC.4's claim is exact: the only change is z–four, which drops from 4 to 2.

**Monotonicity.** The allowed predicate (LFC(c), V3) requires every subfamily S′ with |S′| ≥ 2 to contain a pair with gcd ≥ |S′|. This is monotone in the gcds, so lowering a gcd can only remove allowed sets. At E = 1 the maximal allowed sets are {f1,f2,z,t}, {f1,f2,s_i}, {z,t,s_i} and {s1,s2}. The set {f1,f2,z,s_i} dies on its subset {f,z,s}.

**Weights and conclusion.**
- y_A and y_B each weigh ≤ 1 on every allowed set and have value 5.
- RICH Corollary 5/6 holds for every E ≥ 1, so value 5 is optimal.
- The occupied-fibre equality clause then gives y_A(S_C) = y_B(S_C) = 1 on every occupied fibre.
- Hence [f1 ∈ S_C] = [f2 ∈ S_C] on every occupied fibre.
- L_f1 and L_f2 are unions of occupied fibres, so L_f1 = L_f2. ✓

**No scope leak.** TC.3 keeps R3, R4, R5 and the ({1,4,4,4}|c|1) item at E ≥ 2. Their only load-bearing consumer is TC-B, which lives in Case B, where CASEB gives E ≥ 2. R3 is load-bearing nowhere; it is used only in section 5.

**A22 consumer in (a1).**
- For e = 2 the row is R1, now valid for every E.
- For e = 1, t's label 3^A·5^Bt·w_t meets only z, so every allowed set through t lies inside {t, z}.
- The sets {f1,f2,s1,s2} and {z,s1,s2} die by Sun(3) for every E.
- So y1 and y2 are feasible with value 5 for every E. Equal weight under both forces #fours = 2·#twos, so a set contains both fours or neither.
- The section 2 bound 8/6 − K + max(0, K − 2/6) ≥ 1, against V4, does not involve E.
- Therefore A22 holds for every E ≥ 1. ✓

**A22 consumer in (a2-no5).**
- The only factor 5 sits in p's labels (2^i·5^B·w_p or 5^B·w_p). The matrix is therefore unchanged whether p is a four, a two or the apex.
- At apex p, Corollary 5/6-a2 uses FG-a2 (b): x*_zt ≠ 5, and x*_zu ≤ 3 by D23P.
- At apexes in W′ it uses FG-a2 (a). ✓

*Optional:* mark R1's "Maximal allowed sets" list as "(E ≥ 2)". Each E = 1 maximal set lies inside a listed set.

## O2: Lemma FG-V (TC.7) and its consumers (TC.8–TC.10): ACCEPT_REPAIRS

**FG-V proof.**
- FG-V uses the actual family U^C_j of C (U_j, or g_jU_jg_j⁻¹ for the inverse). Normalising g_a = 1 is a left translation, so the subgroups are unchanged.
- U^C_aY lies in X_j = U^C_aU^C_j for every j ≠ a, and X_j ∩ D_j = ∅ by V1, so U^C_aY misses the union.
- G0 then gives the lower bound 1/gcd(n_a, [G:Y]).

**FG7 (b) premises, all met.**
- N = Q = V∖{a}.
- [G : U^C_j] = n_j, since INV preserves the index tuple.
- Pair parameters are the alpha-matrix of C: alpha ≤ 5 by E1; alpha* ≤ 5 by E1 applied to the inverse configuration (E6).
- a ∈ W∖Q.

No numeric LFC shortcut is used.

**TC-B (i): C^alpha*, apex a ∈ T*, opposite-family masses alpha_aj/6.**
- Masses: a′, a″ 4/6; v1, v2 2/6; z 3/6.
- Transfers: D*_z ∩ D*_v = ∅ for each v, via R4 at v and Lemma TC with (u, a, j) = (v, a, z).
- R4 needs alpha*_tv = 2, which comes from the last item of section 2 (E ≥ 2 in Case B).
- A coset holding both v's has S = {v1, v2} exactly.
- Union ≥ 3/6 + (4/6 − μ(R))/2 + μ(R) ≥ 11/12 > 5/6. ✓

**TC-B (ii): C^alpha*, apex v, masses alpha_vj/6.**
- Masses: each a 2/6; v′ 4/6; z 3/6; t 4/6.
- Transfers come from R5 at a1 and a2.
- With TC.9, the sets Z, K and N partition the union, and v′ ∉ K.
- So μ(N) ≥ 1/6 and μ(N) ≥ 4/6 − 2μ(K). The minimum is at μ(K) = 1/4, giving 11/12 > 5/6. ✓
- TC.9 also removes the original double count of K.

**No hidden premise.** The proof uses only Case B (CASEB, E ≥ 2), R4, R5 and the last item at E ≥ 2, Lemma TC, V1, G0, FG7 (b), E1, E6, INV, and R0.

*Optional:* add "G finite (R0 lifts)" to FG-V, because G0 is stated for finite G.

## O3: auxiliary-scope repair (A2.10, A2.12, A2.15, A2.16): ACCEPT_REPAIRS_WITH_FIXES

**A2.10 list.** It is the verdict's list minus FG7, plus the main theorem and Corollary R3. The S1–S4 survivors stay local-test-only, and RICH sections 6 and 9 are excluded. The counterexample is right: T_{z,t} = 6·2^E·3^A·w_z·w_t·5, so gcd(6·5^B·w_p, T_{z,t}) = 30.

**Adapted chain (A2.12), with p in any position.**
- T_2 = lcm·β holds exactly by definition, including when p is first or second.
- At a later step, an unmarked e gives gcd 6. For e = p, v5(T_m) = 0, so the gcd is again 6.
- Hence k ≤ β_ej ≤ 4 and T_{m+1} = w′_e·k·T_m.
- So T_Q = 6·5^{B[p∈Q]}·∏w_j·β·∏k. Its prime-to-30 part is the product of the original w_j; the 5^B appears only in the whole index. ✓

**gcd 6 at p and at n_t.**
- Before p enters, gcd(n_p, T_m) = 6 (shown above).
- A2.17 (v): gcd(6·3^A·w_t, 6·5^B·∏w_u·2^h) = 6. ✓

**Other checks.**
- (B6): g = 3·2^min(E+1, v2 T*_W) is correct.
- (S5): the order t, p, W′ with z ∉ Q is correct.
- No false "prime to 5" claim survives. The three false clauses are all withdrawn: LZ's "5 ∤ T*_W", PFG-t's "5 ∤ T_W" and RF8c. Every remaining "prime to 5" concerns n_z, n_t or non-p labels, and is true in (a2).
- CC is restricted to its separation hypothesis. The local indices alpha*_zj·r_j keep gcd 3 inside T*, gcd 1 across T* | W∖T*, and gcd 1 or 2 within the 1/2-classes. The masses match (a1) with Bz = Bt = 0.
- Navigation, survivors and LP-optimality are not promoted anywhere.

**MINOR**
- **AUX-1** (A2.11; also A2.17 (i)): "ell_j = r_j" and "ell_p = 5^B w_p" assert more than the old (B2), which said ell_j divides r_j. The proofs only use divisibility.
  - Fix: write "ell_j | r_j (so ell_p | 5^B w_p)".
  - No change is needed if L1 defines ell_j := r_j.
- **AUX-2** (A2.12): the reason given for e = p leaves out the earlier factors k, and the "any family" clause lacks an index hypothesis.
  - Fix: "…no n_j (j ≠ p), no β ≤ 4 and no earlier k (each ≤ 4) contains 5".
  - Fix: "any family with [G : V_j] = n_j and β_jk ≤ 4".
- **AUX-3** (optional; removes the only remaining reliance): (B3) asserts that RICH uses FG7 only in Cor 5/6 via (b) and in LZ via (a) over subsets of W. I took that from the prior reviews; the excerpts do not let me check it.
  - Fix: add "For the actual families of an (a2-no5) configuration and its inverse (all pair parameters ≤ 4), the order z, t, then W (p anywhere) gives FG7 (a)/(b) for every Q ⊆ V, reading 'unmarked' as 'in W', with prime-to-30 part ∏(original w_j) and v5(T_Q) = B[p∈Q]."
  - This is valid because neither n_z nor n_t carries a 5 in (a2).

## O4: A2.17 and the dependency map: ACCEPT_REPAIRS_WITH_FIXES

**What A2.17 gets right.**
- It transfers named claims only; navigation and survivor sections are excluded; and further errata force a redo.
- Each changed hypothesis is handled by the right fact, not by "unchanged proof" wording:
  - "w prime to 30" becomes "entry gcds" (ii).
  - Triangle ells are odd and prime to 3 (i).
  - The false "5 ∤ T_W" is deleted, and gcd(n_t, T_W) = 6 is re-proved with p anywhere in the tree (v).
  - E3's neighbour set B may contain p (vi).
  - o = p is allowed in R4/R5, and D23-MIX becomes D23-a2 (vii).
- The FG-V transfer (iv) uses G0 plus FG-a2 on actual families only, never auxiliary β ≤ 5.
- Sun accounting:
  - Direct Sun(5) appears only in A1 Corollary L (44444 feasibility; the 44441 and 44444 kills), and still holds when p is one of the fours because all gcds stay ≤ 4.
  - TC and A22 import only "at least two fours", which needs only the b ≤ 1 kills (Sun(2), Sun(3)) plus PFG-t.
  - The transitive closure to the computer-assisted Sun(5)/Sun(6) records is kept in A1.4, TC.2, A22.1, A2.2 and MAN.1. ✓

**MINOR**
- **TR-1** (A2.17 (iv)): FG-a2 (b) at a = p also needs β_zu ≤ 3 on W′, and "no entry is 5" does not supply it.
  - Fix: append "and, for (b), β_zu ≤ 3 on W′ (D23P for the alpha-matrix of C)". Alternatively, cite AUX-3.
- **TR-2** (A2.17 proof): the new R1 and A22 consumers appear only in the table and inside (vii).
  - Fix: add "(iv′) For every E ≥ 1, at an apex in W (p included, also as apex), a row ({2,2,4,4}|3|e) with e ∈ {1,2} has the (a1) gcd matrix with Bz = Bt = 0 for the same E (B1, B2). So y_A, y_B (TC.4) and y1, y2 (A22 1(c)) are feasible with value 5, and Corollary 5/6-a2 with its occupied-fibre clause gives L_f1 = L_f2."
- **TR-3** (A2.17 statement): "(E ≥ 2)" grammatically covers R3–R5 only, so the exclusion item reads as unscoped.
  - Fix: "row R1 (every E ≥ 1); rows R3, R4, R5 and the exclusion of ({1,4,4,4}|c|1) (each for E ≥ 2)".
- **TR-4** (TC.11 and the table): the restated TC-P is a generalisation, not a narrowing. Its hypotheses are two R1 rows plus four alpha* values at u4, and at E = 1 it rests on TC.4. The proof does cover it: it uses only the masses of u1, u2, u3, u5 at u4, two transfers and V4.
  - Fix: change the table row to "generalised; every E ≥ 1 via TC.4".
  - Fix: tag the z/t masses and "12 w_z", "4·3^A w_t" in the TC-P proof as "(Pc5′ values, unused)".
- **TR-5** (optional, A2.2): add that the transferred K7-TC and K7-TC-A22 claims use Corollary L only through "≥ 2 fours", which is Sun(5)-free.

**Editorial sweep.** No other item changes a quantifier or opens a gap:
- TC.5 and TC.6 restrict to occupied fibres, as the equality clause requires; the L-conclusions are unchanged.
- TC.12 arithmetic is correct.
- A1.11 and A1.12 give values 7, 6 and 5+1; "feasible" is enough.
- A1.8 adds a derived clause; the table calls this "wording", but it is harmless.
- A22.4, the A2.1 clique rule, and A2.3, A2.4, A2.8, A2.9, A2.13 and A2.14 are all fine.
- A1.4's "suppressed in labels" convention covers labels only. PFG-t (i) keeps 5^Bt in n_t and correctly uses 5 ∤ T_W in (a1).
- **ED-1 (MINOR, A1.6):** "the Sun(5)-dependent branch b ≥ 4 is vacuous" is inaccurate if b counts fours, because b = 4 does occur in E3 (W-part 4444).
  - Fix: "with four neighbours no 5-subset of the class exists, so no Sun(5)/Sun(6) instance enters".

## Conclusions now supported

These are model-reviewed written proofs, not Lean or human checks. They rest on the accepted RICH/D23P (1167bc4f…) and LFC/INV (8621e744…) bases, and transitively on the computer-assisted Sun(5)/Sun(6) records.

**(a1)**
- Corollary W3: W3 = W3* = ∅, and all W–W entries lie in {1,2,4}.
- Lemma E3.
- Lemma PFG-t (i)/(ii) under connectivity, and Corollary L as a necessary condition only (at least two entries 4).
- Lemma B and Theorem CASEB.
- Lemma TC and Lemma FG-V.
- R1 for every E ≥ 1; R3, R4, R5 and the ({1,4,4,4}|c|1) exclusion for E ≥ 2.
- Theorem K7-TC-B: alpha*_v1v2 = 2, and alpha* = 2 on T*.
- Proposition TC-P in its TC.11 form for every E ≥ 1, so Pc5′ is not realised.
- Theorem K7-TC-A22 for every E ≥ 1 and any group.

**(a2)**
- Lemma F: only the z–t entry can be 5, and in at most one orientation.
- FG-a2, Corollary 5/6-a2, D23-a2, and Proposition ZT5 (S1)–(S5).
- Theorem K7-A2-BRIDGE in its enumerated A2.10 form.
- Corollary K7-A2-TRANSFER for its named list in (a2-no5), with W = W′ ∪ {p}.

## Still conditional, relied on, or open

**Hypothesis-bound by their own statements:** PFG-t (connectivity), CC (separation), TC-B (Case B), A22 (Case A plus hypothesis A22), and S1–S4 (survivors only).

**Relied on from prior reviews, not re-derived here:** the (B1)–(B7) inventory of what RICH's proofs use. This includes the FG7-use inventory (removable via AUX-3), the CC weight/mass, and TZ (i) via Z2 G5.

**Not transferred:**
- FG7 for auxiliary families.
- RICH sections 6 and 9.
- A1-STRUCT sections 6–7.
- TC sections 5–6 (including Q_B′).
- A22 section 4.

**Open:**
- (a1) itself.
- Case A vertices with four-degree patterns (3,1), (1,3), (2,1) or (1,2).
- The Case B residue.
- (a2-zt5) beyond S1–S5.
- The (a2-no5) residue.
- K6.2*, full K7 and Sun(7).

No novelty claim is made.
