# Referee report: K62-SH-v1 and K62-DG-v1 (with K62-DG-erratum-v1)

**Basis.** I read the texts as they appear in your message. I did not recompute hashes and used no tools, computation or delegation. I used imports only at the scopes you listed. I took P_ob from K62-STATUS-v2 §3 as a definition only; its claimed local-test survival plays no role here.

## Summary

| File | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| K62-SH-v1 | ACCEPT-WITH-FIXES | 0 | 0 | 3 |
| K62-DG-v1 + erratum-v1 | ACCEPT-WITH-FIXES | 0 | 0 | 5 |

- Every numbered claim checks as stated.
- All fixes concern citations, provenance or wording. No statement needs to change.
- The DG erratum is mandatory. It is a real gap repair, not only a wording change (see DG-m5).

## K62-SH-v1

**SH-1: ACCEPT.**
- (a) mu(L_c) = t_c/n_d = 1/2.
- mu(U*_cU_d) = alpha*_dc/2 = 1/2, because g_dc = 2 forces alpha*_dc = 1.
- The two sets are disjoint by the K62-E3 step-3 argument, which only uses w ∈ U*_c.
- (b) The same argument works with i* in place of c. mu(U*_{i*}U_d) = alpha*_{d i*}/4 by L0.1, using g_d = 1 so that U*_d = U_d.

**SH-2(a): ACCEPT.**
- mu(Z) = [G : U_d ∩ U*_{i*} ∩ U*_c]/(n_d J) ≥ 1/gcd(n_d, J).
- The gcd formula is correct:
  - v2 J = 2 + v2 a, which uses e* = 2.
  - The 3-part is trivial because f_d = 0.
  - The w-part is trivial because a ≤ 5 and the w's are pairwise coprime and prime to 30.
- For odd a the gcd is 4. Either h_d = 0, or h_d ≥ 1 forces h* = h_c = 0 and excludes a = 5.
- So mu(Z) ≥ 1/4 = mu(U_dU*_{i*}). This is the only place alpha*_{d i*} = 1 is used.
- Hence Z = U_dU*_{i*} ⊂ U_dU*_c. Taking set inverses gives the claim.

**SH-2(b): ACCEPT.** Compute lcm(n_d, J, I)/(n_d J) prime by prime:

| Prime | Ratio | Reason |
|---|---|---|
| 2 | 2^{e_d}/2^{e_d+2} | — |
| 3 | 3^2/3 | I carries 3^{f*}·3 = 9 since f* = 1; J carries exactly 3 since f_c = f* = 1 and 3 ∤ a |
| 5 | 1 | at most one h is positive; if a = 5 then h_d = 0 and J's 5-part dominates I's |
| w | 1 | — |

- The total is 3/4 > 1/2 = mu(U_dU*_c), so the claim holds.
- The excluded inputs are exactly where the method fails:
  - c = t gives a ratio of 1/4.
  - a = 3 gives 1/4.
  - a = 5 with h_d ≥ 1 gives 3/20.

**Theorem SH(i): ACCEPT.**
- Σ_F(|B(F)| − 2) = n_d/2, and every term is ≥ 0 because |S_F| ≤ 3 (Sun(4) via K62-E3 step 2).
- The n_d/4 fibres met by g_{i*}U_{i*} each contribute ≥ 1.
- U*_{i*}U_d is right-U_d-invariant with measure 1/4, so it is a union of n_d/4 fibres.
  - By SH-1(b) these fibres are disjoint from L_{i*}, so they are different fibres.
  - They include U_d, which contributes 3.
  - If |Odd*| ≥ 3, each of them has |B| ≥ 3 by SH-2(a) and SH-1(a).
- So the sum is ≥ n_d/4 + 3 + (n_d/4 − 1) = n_d/2 + 2, a contradiction.

**SH(ii): ACCEPT.**
- This is SH-2(b) alone; no counting is involved.
- If alpha*_{d i*} = 3, then INV(b) forces alpha_{d i*} = 1.
- K62-E3 Lemma 1 then forces t to exist, so f* = 1.

**SH(iii): ACCEPT.**
- The inverted configuration (INV(a) with E6) has the same index tuple, hence the same h_d.
- Its entries satisfy (alpha~, alpha~*)_{d i*} = (1, 1) and alpha~*_{i* c} = alpha_{i* c}.
- Applying (i) to it gives the claim.

**Orientation.**
- (i) needs alpha_{d i*} = 1, for t_{i*} = n_d/4 and the three-piece cap.
- (i) also needs alpha*_{d i*} = 1, for mu(U*_{i*}U_d) = 1/4.
- (ii) covers the case (1, 3); (iii) covers (1, 1) read in the other family.
- Since K62-E3 Lemma 1 excludes the entry 2, these cases are exhaustive.

**Role of h_d = 0.**
- It is needed only to admit a = 5 into Odd*. With 5 ∤ n_d, the 5 in J is invisible to the gcd in (a) and to the ratio in (b).
- If h_d ≥ 1, the bounds drop to 1/20 and 3/20 and nothing follows.
- For a ∈ {1, 3}, no condition on h_d is needed.
- h_d plays no role in the count of (i).

**§4 scope: ACCEPT.**
- The file excludes nothing on its own.
- P_ob is consistent with it: Odd* = ∅, Odd = {c_5}, and (ii) is vacuous.

## K62-DG-v1 with erratum-v1

**DG-1: ACCEPT.**
- **Characterisation of B(F).** c ∈ B(F) ⇔ F ∩ g_cU_c = ∅ ⇔ F ⊄ L_c ⇔ F ⊂ G∖L_c = U*_cU_d.
  - L_c is a union of fibres.
  - L_c and U*_cU_d are disjoint, each of measure 1/2.
- **Left and right cosets are used consistently.** Fibres are left U_d-cosets. L_c, U*_cU_d and Z_Q are all unions of fibres.
  - So N(Q) = n_d·mu(Z_Q).
  - Z_Q is left-W*_Q-invariant, so it is a disjoint union of (W*_Q, U_d)-double cosets.
- **No normality is needed.**
  - |W*_Q x U_d| = |W*_Q · xU_dx^{-1}| = |W*_Q||U_d|/|W*_Q ∩ xU_dx^{-1}|.
  - The numerator of the measure [G : W*_Q ∩ xU_dx^{-1}]/(T*_Q n_d) is divisible by T*_Q and by [G : xU_dx^{-1}] = n_d.
  - So each double coset has measure equal to a positive multiple of 1/gcd(T*_Q, n_d).
- **Positivity is proven.** 1 ∈ U*_c for each c, so U_d ⊂ Z_Q and N(Q) ≥ 1.
- **The gcd equals 2^{min(e_d, v2 T*_Q)}.** This is the K62-E3 Lemma 3 chain applied to Q (erratum v2 Z10). I re-checked it for |Q| = 1 to 4:
  - marked vertices come first;
  - each unmarked step has k ≤ alpha*_{ej} ∈ {1, 2, 4};
  - the prime-to-30 part is ∏_{c ∈ Q} w_c;
  - there is no factor 5 when h_d ≥ 1.
- DG-1 does not use alpha_{d i*} = 1.

**DG-2: ACCEPT.** There is no inclusion–exclusion here. All three bounds come from Σ_F C(|B(F)|, k), which has non-negative weights.
- **(i):** n_d/2 = #{|B| ≥ 3} + A_4 + N(O), with #{|B| ≥ 3} ≥ n_d/4 + 1.
- **Fibre counts by |B|:**
  - b_3 = n_d/2 − 2A_4 − N(O)
  - b_4 = A_4 − N(O)
  - b_5 = N(O)
- **Triple and quadruple sums:**
  - Σ_R N(R) = n_d/2 + 2A_4 + 5N(O)
  - Σ_Q N(Q) = A_4 + 4N(O)
- Substituting (i) gives (ii) and (iii), with the signs as stated.
- The bound N(O) ≤ n_d/8 − 1/2 follows from A_4 ≥ N(O).

**DG-3: ACCEPT-WITH-FIXES (DG-m2).**
- Set ell_z = n_z/6. These are odd and pairwise coprime, including marked vertices.
  - So v2 T*_R = 1 + v2 tau*.
- (T1): x_ab divides ell_c·tau*, hence x_ab divides tau*.
- The tau_max bound: tau*/(6 x_ab) ≤ min(x_ca, x_cb)/6, which gives tau* ≤ x1·x2.
- A deep triple therefore has alpha*-values:
  - (2,4,4) with tau* = 8, or
  - (4,4,4) with tau* ∈ {8, 16}.
- tau* = 12 is possible for (4,4,4), but it has depth 3, so the claim is unaffected.

**DG-4: ACCEPT.** The step "k ≤ m_e implies v2 k ≤ v2 m_e" is valid because m_e is a power of 2.

**Theorem DG: ACCEPT.**
- n_d/16 is an integer since e_d ≥ 4.
- (a) Suppose N(O) > n_d/16.
  - Then N(Q) ≥ n_d/8 for every 4-subset Q.
  - DG-2(iii) then gives N(O) ≥ n_d/8 + 1/3, contradicting N(O) ≤ n_d/8 − 1/2.
  - With N(O) ≤ n_d/16, the sum of N(R) is at most 19n_d/16 − 2.
- (b) Both 20/16 and 19/16 exceed 19/16 − 2/n_d.
  - If exactly one triple is deep, its depth is exactly 5, its values are (4,4,4), tau* = 16, and e_d ≥ 5.

**Corollary on P_ob: ACCEPT-WITH-FIXES (erratum mandatory; DG-m4, DG-m5).** I checked this against STATUS-v2 §3.

| Edges | alpha | alpha* |
|---|---|---|
| Cycle edges in O | 4 | 2 |
| Chords in O | 2 | 4 |
| d-edges | 1 | 1 |

Since alpha_{d i*} = 1, Theorem DG applies in the stated orientation without inversion.

- **Triple types.** Every 3-subset of the 5-cycle has one or two cycle edges.
  - Five triples have alpha* = (2,2,4), forcing tau* = 4.
  - Five have (2,4,4), allowing tau* ∈ {4, 8}.
- **Step 2.** Take the apex c_4 opposite the cycle edge c_1c_2.
  - 8/12 = 2/3 equals alpha*_41/6 and alpha*_42/6, so X*_1 = X*_2.
  - 4/12 = 1/3 equals alpha*_43/6, so X*_3 ⊂ X*_2.
  - Every edge from c_4 is tight, and D~_1 has measure alpha_41/6 = 1/3, so it is non-empty.
  - The labels are 2ell_1, 2ell_2, 4ell_3. Their pairwise gcd is 2, so Sun(3) fails.
  - Using rotation is legitimate: step 2 uses only the O–O data and the n_c = 6·ell_c form, never the i*-row or the markers.
- **Step 3 (as repaired by the erratum).** All ten triples have depth 3.
  - Every 4-subset is a path, so any of its at least two unmarked vertices has m_e = 2.
  - Hence v2 T*_Q ≤ 4.
- **Step 4.** 10/8 > 19/16 − 2/n_d, the required contradiction.
- The erratum's Old block matches the frozen step 3 as reproduced here; I checked by reading, not hashing.

**§6 scope: ACCEPT.**

## Exact scope, if accepted

**Excluded.** Only configurations with the (alpha, alpha*) pattern P_ob, with the 3- and 5-markers anywhere and any e_d ≥ 4.
- STATUS-v2 defines P_ob only for the unmarked case; the proof covers the extension to arbitrary markers.
- As navigation only, and not as an accepted claim: the written proof never uses the i*-rows or alpha*_{d i*}.

**Constrained, not excluded.**
- SH gives conditions (i)–(iii) on the i*-row.
- Theorem DG applies in each family where x_{d i*} = 1. In each such family, one of the following holds:
  - a 4-subset has depth at least 5;
  - at least two deep triples exist;
  - exactly one deep triple exists, with values (4,4,4), tau* = 16 and e_d ≥ 5.
- If e_d = 4, the theorem forces at least two deep triples in each such family.

## Import closure

| | Direct Sun instances (classical) | Route |
|---|---|---|
| SH | Sun(4) | LFC(c) at \|T\| = 4, via K62-E3 Lemma 1 and step 2 |
| DG | Sun(2) | K62-E3 Lemma 2 / Z11(a), feeding DG-3, DG-4 and the Lemma 3 chain |
| DG | Sun(3) | Corollary step 2 |
| DG | Sun(4) | K62-E3 step 2 and Lemma 1 |

- Neither file uses LFC(c) with |T| ≥ 5.
- The computer-assisted Sun(5)/Sun(6) enter only through the provenance of the accepted LFC package, as in the K62-E3 verdict.
- Neither file says so explicitly, and neither claims to be free of Sun(5)/Sun(6).
- DG also cites rules-k7-v1 L1 and VFC (V1)/(V3). These are outside the context you supplied, but everything DG actually uses from them can be re-derived from the supplied imports.

## No closure claimed

Confirmed:
- SH §4 and DG §6 both leave K6.2* (e_d ≥ 4, e* = 2) and Sun(7) OPEN.
- Neither file says anything about K7.
- Theorem DG is stated as necessary conditions only.

## Minimal repairs (all MINOR)

**SH-m1, provenance.** Add a sentence like K62-E3 erratum v2 Z1:
- LFC(c) is used only at |T| = 4.
- The LFC package's provenance includes the computer-assisted Sun(5)/Sun(6).
- There is no claim that this file's import closure avoids them.

**SH-m2, proof details.**
- Write out the disjointness argument for i* in SH-1(b).
- In SH-2, state that the 3-part and w-part are trivial and that v2 J = 2 + v2 a uses e* = 2.

**SH-m3, wording.**
- In SH-2(a), replace "Invert." with "taking set inverses (not the configuration inversion INV)".
- In SH(i), add: "U*_{i*}U_d is right-U_d-invariant, so it is the union of n_d·alpha*_{d i*}/4 = n_d/4 fibres."

**DG-m1, provenance.** Add the same sentence as SH-m1, noting that LFC(c) is used at |T| ∈ {2, 3, 4}.

**DG-m2, citations.**
- In DG-3, replace the citation of L1 with the two-line derivation above.
- Cite the gcd chain as erratum v2 Z10 (every non-empty Q). The verdict's wording mentions only 4-subsets, so add one line saying the chain works verbatim for |Q| ≤ 3.
- Cite the {1, 2, 4} restriction as erratum v2 Z11(a).
- In DG-1, add: "[G : xU_dx^{-1}] = n_d; no normality is used" and "DG-1 does not use alpha_{d i*} = 1."

**DG-m3, wording in DG-4 and Theorem DG.**
- DG-4: add "since m_e is a power of 2".
- Theorem DG(a): write "N(O) ≥ n_d/8 + 1/3" and note that n_d/16 is an integer.
- Theorem DG(b): "at least 5" should read "exactly 5".

**DG-m4, Corollary step 2: replace (V1)/(V3) with LFC on the original configuration.**
- Normalise g_{c_4} = 1. This conjugates all U*_j simultaneously, so the containments from tau* survive.
- L_j = g_jU_jU_{c_4} and U*_jU_{c_4} are disjoint, with measures alpha_{4j}/6 and alpha*_{4j}/6.
- Tightness then gives L_j = G∖(X*_j)^{-1}, so L_1 = L_2 ⊂ L_3, each of measure 1/3.
- A fibre inside L_1 meets the cosets of c_1, c_2 and c_3, with labels of pairwise gcd 2. This contradicts LFC(c) at |T| = 3.
- State explicitly why rotation is allowed.

**DG-m5, erratum and scope wording.**
- The erratum fixes a real gap, not just wording: the frozen step 3 fails when both ends of the 4-path are marked (for example t = c_1, p = c_4).
- The Corollary's header should say "the (alpha, alpha*) pattern of P_ob, markers anywhere".

No novelty or priority assessment is made.
