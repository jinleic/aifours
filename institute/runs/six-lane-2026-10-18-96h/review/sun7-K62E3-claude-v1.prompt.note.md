# Referee report: K62-E3-v1 read with erratum F1–F3

**Scope of review.** Written proofs only. I re-derived every step by hand and ran no computation.

**Overall verdict: ACCEPT-WITH-FIXES.** 0 FATAL, 0 MAJOR, 9 MINOR. All findings are editorial or concern import accounting, and none changes a statement. Theorem K62-E3 is correct as stated.

## Verdicts

| Item | Verdict |
|---|---|
| Lemma 1 | ACCEPT |
| Lemma 2, item 1 (x_vu ≠ 3) | ACCEPT |
| Lemma 2, item 2 (at most two 1s) | ACCEPT |
| Lemma 2, item 3(i) | ACCEPT |
| Lemma 2, item 3(ii) | ACCEPT (correct; redundant per F2) |
| Lemma 2, item 3(iii) with F2 | ACCEPT |
| Lemma 3 with F3 | ACCEPT-WITH-FIXES (m4) |
| Theorem step 0 (WLOG) | ACCEPT-WITH-FIXES (m5) |
| Theorem steps 1 and 2 | ACCEPT |
| Theorem step 3 | ACCEPT-WITH-FIXES (m6) |
| Theorem step 4 | ACCEPT |
| C1 | ACCEPT (m8) |
| C2 with F1 | ACCEPT-WITH-FIXES (m7) |

## 0. Setting and case coverage

**The K6.2\* data in the candidate are exact.** Each item follows from README §5 together with P0/P1:
- a ≤ 1, so at most one vertex has h ≥ 1.
- P1(iii)–(iv) together with f_d = 0 give at most one vertex with f ≥ 2.
- C ∩ E = {i\*} gives e_c = 1 for every c in O.
- P_(d i\*) = {2} with d and i\* both in E gives min(e_d, e\*) = 2, by P0(c).
- P0(b) makes the w's pairwise coprime.
- Recomputing the gcds gives 6 inside C, 4 for d–i\*, and 2 for d–O.
- E1 then gives alpha_dc = alpha\*_dc = 1, and alpha_(d i\*) and alpha\*_(d i\*) in {1, 2, 3}.

**No marker position or exponent case is missed:**

| Case | Where it enters | Handled |
|---|---|---|
| 3-marker on i\* | At d, every (c, i\*) gcd is 3 for every value of alpha_(d i\*) | ✓ |
| 3-marker on t ∈ O | gcd(λ_t, λ_i\*) = 9 only when alpha_(d i\*) = 3; Lemma 3 puts t first | ✓ |
| 3-marker absent | All label gcds are 3 | ✓ |
| 5-marker on d | Lemma 2 item 3 feeds the 5-part of Lemma 3 | ✓ |
| 5-marker on i\* | No effect: min h = 0, and T\*_O does not involve i\* | ✓ |
| 5-marker on p ∈ O (including p = t) | Lemma 3 puts p first; n_d then has no 5 | ✓ |
| 5-marker absent | Trivial | ✓ |
| e\* (≥ 2 when e_d = 2; = 2 when e_d = 3) | Enters only as 2^(e\*−2) or 2^(e\*−1), always paired against odd labels | ✓ |
| Sizes of f\*, f_t, h | Only minimum exponents enter | ✓ |

**Labels at v ∈ O do not depend on v's own markers.** Here g_vu = g_(v i\*) = 6, g_vd = 2 and x_vd = 1. So the cases v = t and v = p are covered.

## 1. Lemma 1: ACCEPT

Write a := x_(d i\*), which lies in {1, 2, 3}. At d:
- λ_c = 3^f_c 5^h_c w_c, which is odd.
- λ_i\* = a · 2^(e\*−2) 3^f\* 5^h\* w_\*.

The pairwise gcds are:
- (c, c') = 3.
- (c, i\*) = 3^min(f_c, f\* + v3(a)). The 5-part is trivial because min(h_c, h\*) = 0 and v5(a) = 0. The w-part is 1 because a ≤ 3.
- This equals 9 exactly when c = t and a = 3, which forces f\* = 1. Otherwise it is 3.

When all six labels have pairwise gcd 3:
- Sun(4), via LFC (c) at |T| = 4, caps every fibre at 3 pieces.
- So y ≡ 1/3 is feasible.
- LFC (d) gives 5/6 + a/12 ≤ 1 − 1/n_d, hence a = 1.

So a = 2 is impossible in every case, and a = 3 requires t. The alpha\* orientation is the same computation applied to the inverted configuration (INV (a) with E6). Under alpha + alpha\* ≤ 4, the only pair with no entry equal to 1 is (2, 2), and that is excluded. The only Sun instance used is Sun(4).

## 2. Lemma 2: ACCEPT, every item

**Item 1 (x_vu ≠ 3).**
- λ_u = 3^f_u 5^h_u w_u and λ_d = 2^(e_d−1) 5^h_d w_d are coprime, since at most one vertex has h ≥ 1.
- So Sun(2) keeps u and d out of a common fibre.
- Taking y_u = y_d = 1 gives val = 3 + 3 = 6, contradicting val < 6.

**Item 2 (at most two 1s).**
- The labels 3^(f_u−1) 5^h_u w_u of three such u, together with λ_d, are pairwise coprime.
- So val = 1 + 1 + 1 + 3 = 6, a contradiction.

**Item 3 (h_d ≥ 1, so h = 0 on all of C).** Each five f has label 5 · 3^(f_f−1) w_f, and any two fives have gcd 5.
- **(i)** Take u' outside F5. Then x_vu' is in {1, 2, 4}, and gcd(λ_u', λ_f) = 1: λ_f is odd, neither label has a usable 5, and at most one vertex has f ≥ 2. Put y = 1/|F5| on F5 and y_u' = 1; this is feasible and gives val ≥ 5 + 1. Feasibility holds because the total weight on F5 is 1; the stated reason "|F5| ≤ 4" is beside the point (m3).
- **(ii)** gcd(λ_i\*, λ_f) = 1, except that it is 3 when f = t and x_(v i\*) = 3. The allowed sets through i\* are then {i\*} and {i\*, t}. This gives val ≥ 6, or val = 5 + 9/4. Correct, and redundant by F2.
- **(iii)** By INV (b) with g = 6, x_vu = 5 forces x\*_vu = 1. Four such u give four 1s in the other orientation, contradicting item 2 there.

**Item 3(iii) is not circular.** Items 1–2 use LFC only and hold in both orientations. Item 3 in orientation x uses only item 2 in orientation x\*.

**F2 is correct, and holds in a stronger form.** |F5| ≤ #{u : x\*_vu = 1} ≤ 2 holds unconditionally. So whenever F5 is non-empty, case (i) always applies.

**Role in the main proof.** Lemma 2 is load-bearing only through Lemma 3, and only when h_d ≥ 1.

## 3. Lemma 3: ACCEPT-WITH-FIXES (m4)

**Identity.** By L0.1 and W\*_m ⊆ U\*_j:

mu(U\*_e W\*_m) = T_(m+1) / (n_e T_m) = k / gcd(n_e, T_m) ≤ mu(U\*_e U\*_j) = alpha\*_ej / 6. ✓

**Why gcd(n_e, T_m) divides 6 for unmarked e.**
- gcd(6 w_e, T_m) = gcd(6, T_m) · gcd(w_e, T_m).
- gcd(w_e, T_m) = 1, because w_e is prime to 30 and to the earlier w's. By the induction hypothesis, those earlier w's make up the whole prime-to-30 part of T_m.
- So k ≤ gcd · alpha\*_ej / 6 ≤ alpha\*_ej ≤ 5, using E1 in the inverted configuration.
- No prime above 5 enters, so the induction hypothesis propagates. ✓

**Why the marked vertices go first.**
- Suppose t came late. T_m could already carry 3^2, from some earlier k = 3. Then gcd(n_t, T_m) could be 18, and the bound only gives k ≤ 15, which allows 7, 11 or 13.
- A late p fails in the same way, with gcd up to 30.
- Putting the (at most two) marked O-vertices first avoids every such step. ✓

**Pair factor.**
- This arises only when t ≠ p and both lie in O.
- Then T_2 = lcm(n_t, n_p) · alpha\*_tp with alpha\*_tp ≤ 5, so the prime-to-30 part of T_2 is w_t w_p. ✓
- This case forces h_d = 0, so the 5-part of T_2 does not matter. ✓

**No factor 5 when h_d ≥ 1 (F3).**
- In this case p does not exist.
- T_1 and every n_e with e in O are prime to 5.
- k ≤ alpha\*_ej ≤ 4, by Lemma 2 applied to alpha\*.
- So 5 does not divide T\*_O. ✓
- The original sentence referred to a pair factor that cannot occur in this case; F3 is the correct reading.

**Consequence.** gcd(n_d, T\*_O) = 2^min(e_d, v2(T\*_O)), because:
- n_d has no factor 3;
- gcd(w_d, ∏ w_c) = 1;
- the 5-part is trivial. ✓

## 4. Theorem K62-E3

**Step 0 (WLOG alpha_(d i\*) = 1): sound.**
- Lemma 1 gives one of alpha_(d i\*), alpha\*_(d i\*) equal to 1.
- INV (a) shows the inverted family g_i^−1 U\*_i consists of pairwise disjoint left cosets with the same indices n_i.
- By E6, the class and marking depend only on the index tuple. So the inverted configuration is K6.2\* with the same d, i\*, O, t, p and the same exponents.
- Its alpha is the original alpha\* by definition.
- Inverting twice returns the original configuration, so its alpha\* is the original alpha. So alpha and alpha\* swap.
- The conclusion depends only on indices.

**Step 1 (incidence count): ✓.**
- By LFC (a)–(b) at d: t_c = n_d / 2 for c in O, and t_i\* = n_d / 4. None of these fibres is U_d.
- Summing: 5 n_d / 2 + n_d / 4 = 11 n_d / 4.

**Step 2 (at most three pieces per fibre): ✓.**
- With a = 1, the six labels have pairwise gcd exactly 3 in every marker case.
- So Sun(4) gives |S_F| ≤ 3 for every fibre F ≠ U_d.
- S_(U_d) is empty.

**Step 3 (light fibres): ✓.**
- Suppose wu lies in L_c. Since L_c U_d = L_c, w lies in L_c.
- Write w = g_c a g_c^−1 with a in U_c. Then a g_c^−1 lies in U_c U_d, so g_c^−1 lies in U_c U_d.
- Hence g_c lies in U_d U_c, so g_c U_c meets U_d, contradicting disjointness.
- A fibre F meets g_c U_c exactly when F ⊆ L_c.
- So fibres inside W\*_O U_d contain no O-piece.
- Counting: 11 n_d / 4 ≤ 3(n_d − M) + (M − 1), so 2M ≤ n_d/4 − 1, and M ≤ n_d/8 − 1/2 < n_d/8.
- Consistency check (not needed): mu(L_c) = alpha_dc / 2 = 1/2 = mu(U\*_c U_d), so L_c and U\*_c U_d partition G.

**Step 4 (granularity): ✓.**
- M = n_d · mu(U_d W\*_O) = [G : U_d ∩ W\*_O] / T\*_O ≥ lcm(n_d, T\*_O) / T\*_O = n_d / gcd(n_d, T\*_O).
- Hence gcd(n_d, T\*_O) > 8. By Lemma 3, this gives e_d ≥ 4 and v2(T\*_O) ≥ 4.
- From min(e_d, e\*) = 2, it follows that e\* = 2.
- The strict inequality in step 3 is exactly what kills e_d = 3: it would need M ≥ n_d/8, against M ≤ n_d/8 − 1/2.

## 5. Mutation sanity

- **e_d = 4 is not excluded.** e_d enters only through 2^min(e_d, v2(T\*_O)). At e_d = 4 the chain only yields v2(T\*_O) ≥ 4. Nothing in the file bounds v2(T\*_O) from above: v2(T\*_O) = 1 + Σ v2(k_m), with k_m up to 4. So gcd = 16 and M ≥ n_d/16 are compatible with M < n_d/8. ✓
- **alpha_(d i\*) = 3 breaks step 2.** This value needs t, by Lemma 1.
  - Then f\* = 1, and λ_i\* has v3 = 2.
  - So gcd(λ_t, λ_i\*) = 9 ≥ 4, and {t, i\*, c, c'} passes LFC (c).
  - The cap of 3 pieces per fibre therefore fails, and the incidence total becomes 13 n_d / 4. ✓
  - Step 0 is therefore load-bearing.
- **Candidate's control (3) checks out.** With h_d ≥ 1 and a 5 allowed in alpha\* on O, gcd could be 20 > 8 at e_d = 2. So Lemma 2 item 3 is load-bearing exactly when the 5-marker is on d.

## 6. Corollaries (not load-bearing; verdicts separate)

**Shared identities: all ✓.**
- Σ_F |B(F)| = 5 n_d / 2.
- |B(F)| ≥ 2 + [i\* ∈ S_F].
- B(F) ⊇ Q when F ⊆ W\*_Q U_d. Step 3 used only that w lies in U\*_c, so it applies to Q.
- β_3 + 2β_4 + 3β_5 = 1/2.
- β_4 + 2β_5 ≤ 1/4 − 1/n_d. This follows from N_3 + N_4 + N_5 ≥ n_d/4 + 1, since by LFC (b) U_d is not one of the fibres met by i\*.

**C1: ACCEPT.**
- The number of fibres in W\*_Q U_d is at most N_4 + N_5 ≤ n_d/4 − 1.
- Granularity then gives gcd(n_d, T\*_Q) > 4.
- Lemma 3 for Q has the same proof, with the marked vertices of Q first.
- Together with e_d ≥ 3, this gives v2(T\*_Q) ≥ 3.

**C2: ACCEPT-WITH-FIXES.**
- **Lower bound (with F1): correct.**
  - gcd(n_d, lcm(n_c, n_c') · alpha\*) = 2^(1 + v2(alpha\*)).
  - This needs e_d ≥ 3 and no common factor 5.
- **alpha\* ∈ {1, 2, 4} on all ten O-pairs: correct.**
  - There is no 3, by Lemma 2 item 1.
  - When h_d ≥ 1 there is no 5, by item 3.
  - When h_d = 0, the parenthetical isolation argument excludes 5; I verified it. λ_u = 3^(f_u−1) 5^(h_u+1) w_u is odd and coprime to λ_d = 2^(e_d−1) w_d. Taking y_u = y_d = 1 gives val = 8 ≥ 6.
- **Double count: correct.**
  - Σ_pairs n_d / 2^(1 + v2(alpha\*)) ≤ n_d (2 + β_4 + 3β_5).
  - β_4 + 3β_5 ≤ (3/2)(β_4 + 2β_5) < 3/8.
  - So 4n_1 + 2n_2 + n_4 ≤ 18, with n_1 + n_2 + n_4 = 10.
  - Hence n_4 ≥ 2n_1 + 2.
- **Orientation clause: correct.**

## 7. Findings

**FATAL:** none.

**MAJOR:** none.

**MINOR**, each with a minimal repair:

- **m1 (Premises).**
  - L0.1 is in README §0; §1 is R0. Repair: correct the citation.
  - Lemma 3 also uses the identity mu(U_i U_j) = alpha_ij / g_ij (the L0.3 bullet of E1). Repair: cite it, or derive it from L0.1.
- **m2 (Lemma 1).**
  - The letter x denotes both the orientation and the entry value.
  - The w-parts of the gcds are left out.
  - Repair: write a := x_(d i\*), and add "w-parts trivial by P0(b), and a ≤ 3".
- **m3 (Lemma 2).**
  - Repair: state that items 1–2 are proved in both orientations before item 3.
  - Repair: replace "since |F5| ≤ 4" with "the total weight on F5 is 1".
  - Optional: compress (ii)–(iii) to "|F5| ≤ #{u : x\*_vu = 1} ≤ 2".
- **m4 (Lemma 3).**
  - "t, then p" is undefined when only p exists. Repair: "marked O-vertices first (one vertex if t = p), then the unmarked ones".
  - Repair: define W\*_m := ∩_(i ≤ m) U\*_(c_i).
  - Repair: spell out gcd(6 w_e, T_m) = gcd(6, T_m).
  - Under F3, repair: also note that every n_e is prime to 5.
- **m5 (Step 0).** Repair:
  - state that g_d = 1 is imposed after the possible inversion;
  - state that d, i\*, O, t, p are fixed by the index tuple;
  - state that double inversion makes the swap alpha ↔ alpha\* exact.
- **m6 (Step 3).** Repair: add "L_c U_d = L_c" and "F meets g_c U_c if and only if F ⊆ L_c".
- **m7 (C2).** F1 is already supplied. Repair:
  - promote the h_d = 0 no-5 argument to a stated Lemma 2 item 4, which makes alpha ∈ {1, 2, 4} on O unconditional;
  - write out the derivation of β_4 + 2β_5 ≤ 1/4 − 1/n_d;
  - write out the step with factor 3/2;
  - note the dependence on e_d ≥ 3.
- **m8 (C1).** Repair:
  - state Lemma 3 for every non-empty Q ⊆ O;
  - note the dependence on e_d ≥ 3.
- **m9 (Scope).**
  - The forward reference to `K62-STATUS-v2.md` "(to be frozen)" is navigation only. Repair: label it so.
  - The "supersedes" remark is also navigation only, though correct as a set inclusion. Repair: label it so.
  - Repair: add the sentence "LFC (c) is invoked only at |T| = 2 and |T| = 4".

## 8. Arbitrary groups, import closure, open items

**Arbitrary groups.** The conclusion "every K6.2\* configuration has e_d ≥ 4, hence e\* = 2" holds in every group, via R0:
- N = ∩ core(U_i) is normal, of finite index, and contained in every U_i.
- Passing to G/N preserves all indices, all intersection indices, and pairwise disjointness.
- The class and e_d are read off the index tuple, so the finite-group theorem applies to G/N.

**Import closure, at the level of instances actually used.**
- R0.
- L0.1 together with Lagrange.
- E1: the range of alpha and alpha\*, plus the identity in m1.
- LFC (a), (b) and (d).
- LFC (c) only at |T| = 2 and |T| = 4:
  - |T| = 2 is Sun(2), which is L0.6 and elementary;
  - |T| = 4 is Sun(4), Zhu's classical Theorem 1.1.
- INV (a) with E6.
- INV (b), used only as the inequality alpha + alpha\* ≤ g. By E7 this needs no VFC.
- The K6.2\* data from P0/P1.

**Why only |T| = 2 and |T| = 4 are needed.** I checked that every feasibility verification and the cap in step 2 test only families defined by the |T| = 2 and |T| = 4 conditions.
- Sun(3) is never needed: every 3-set that occurs has pairwise gcd at least 3.
- No 5-set or 6-set ever needs to be excluded.

**Not used at any instance:** Sun(3), Sun(5), Sun(6), VFC, TG, the T rule, CLIQUE, RPLP, F7, Ppair, M-S Prop 4.5, Menon, K62-A, any computation.

**K63-RES and K62-FG are not imports.** The granularity mechanism (step 3, step 4 and the Lemma 3 chain) is proved in full here.

**Where the computer-assisted Sun(5) and Sun(6) appear.**
- They enter only formally, through the provenance of the accepted LFC package: its proof of (c) cites Sun(|T|) for |T| ≤ 6.
- Restricting LFC (c) to |T| in {2, 4}, with the same proof, removes them from the theorem's closure.
- Separately, placing K6.2\* on the Sun(7) frontier uses Sun(5), Sun(6) and VFC (through R1(7) and D2). That is frontier bookkeeping, not a premise of K62-E3.

**Open items (unchanged by this file):**
- **Full K6.2\* with e_d ≥ 4 and e\* = 2** remains OPEN. This covers every 3-marker position (on i\*, in O, or absent) and every 5-marker position. The file adds only necessary conditions: v2(T\*_O) ≥ 4 for survivors, plus C1 and C2.
- **K7 with the 2- and 3-markers on different vertices** is untouched by this file and remains OPEN.
- **Full Sun(7)** remains OPEN. The candidate makes no Sun(7) claim, and none follows from it.

This report assesses correctness only; it makes no novelty assessment.
