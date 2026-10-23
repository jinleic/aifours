# Hostile review: K63-RES-v1 read through K63-RES-erratum-v1

The review covers K63-RES-v1 (sha256 `1542a551…`) together with K63-RES-erratum-v1 (`e70a5518…`). I used no tools and no computation. The hashes are as supplied; I did not re-hash anything. Imports are taken only at the scopes of these verdicts:
- 8621e744: LFC, INV and ROW-U with errata E1–E8.
- 1a1c6390: the stated conclusions of K63-D and K63-E.
- c792dc68: the TG and CLIQUE statements exactly as written there.
- README §§0–2 and §5.

This is not a novelty assessment.

**Result: 0 FATAL, 0 MAJOR, 9 MINOR.** No statement needs to change. Every MINOR is an attribution or wording repair, and none hides a mathematical gap.

| Item | Verdict |
|---|---|
| (1) Lemma FG | **CORRECT** |
| (2) Corollary 5/6: (a) the α* side, (b) the α side | **CORRECT** in both orientations |
| (3) Row Lemma, all cases, with F3 read through R1 | **CORRECT** |
| (4) Theorem K63-RES and the K6.3 closure | **CORRECT**; the closure follows |
| (5) Restricted star remark (§6 with R2) | **CORRECT as restricted**. It is not load-bearing, and inside the residue it is an instance of K63-RES. |

---

## (1) Lemma FG — CORRECT

**What the induction actually carries.**
- Invariant: L_m divides T_m, and T_m/L_m has no prime factor above 5.
- Equivalently, the prime-to-30 part of T_m is exactly ∏_{i≤m} w_{j_i}.
- So the w's are tracked throughout. FG does not claim that T_Q has only the primes 2, 3, 5.
- The final identity gcd(n_v, T_Q) = gcd(6, T_Q) comes from w_v being coprime to that product.

**Base, for every possible shape of Q ∩ {i\*, d}.**
- **Q contains both i\* and d:** T_2 = lcm(n_\*, n_d)·β_{\*d}, with β_{\*d} ≤ g_{\*d} − 1 = 2.
- **Q contains exactly one of them:** T_1 = n_j.
- **Q contains neither:** j_1 = p if p ∈ Q; otherwise any vertex of O∖{v}.
- **5-freeness:** if p exists, then h_\* = h_d = 0. Since β ∈ {1, 2} contributes no 5, the first three bases are 5-free.

**Step.**
- i\* and d occur only in the base, so every added e lies in O and n_e = 2·3·5^{h_e}·w_e.
- By Lagrange, T_{m+1} = lcm(n_e, T_m)·k for a positive integer k.
- By the product formula, μ(V_eW_m) = T_{m+1}/(n_eT_m) = k/gcd(n_e, T_m).
- Since W_m ⊆ V_{j_1}, μ(V_eW_m) ≤ β_{ej_1}/g_{ej_1}. This is at most 5/6, or at most 2/3 when j_1 = d.
- gcd(n_e, T_m) divides 2·3·5^{min(h_e, v_5(T_m))}·gcd(w_e, T_m), and this equals 6:
  - the invariant gives gcd(w_e, T_m) = 1;
  - the 5-part is trivial, because either h_e = 0 or e = p sits directly on a 5-free base.
- 3 always divides this gcd, so it is 3 or 6, and k ≤ 2 or k ≤ 5 respectively. Either way k has no prime factor above 5.
- For any prime q ≥ 7, v_q(T_{m+1}) = max(v_q(n_e), v_q(T_m)), so the invariant passes to m + 1.

**Edge cases checked.**
- **Singleton Q:** T = n_j, and gcd(n_v, n_j) = g_vj ∈ {3, 6}.
- **Q inside O∖{v}:** p goes first if present; the case without p is immediate.
- **Q avoids p while the 5-marker is on i\* or d:** a 5 in the base is harmless, because every later h_e = 0.
- **Exponents:** arbitrary E, F and h only enter the 2-, 3- and 5-parts. n_e can match at most 2·3 of these.
- **w's:** w's equal to 1 are allowed.

**The conjugate family U\*.**
- [G : g_jU_jg_j⁻¹] = n_j.
- β(U\*) = α\* by the definition in INV (a).
- α\* ≤ g − α ≤ g − 1 by INV (b).
- FG uses only the indices and (B), and both are invariant under the conjugation introduced by the g_v-normalisation in §2.

**A mutation of my own, showing why the base pair is {i\*, d}.**
- Suppose the two special vertices other than p both lay in C, with g = 6.
- Then the base could carry β = 5, so gcd(n_p, T) = 30 becomes possible, and k ≤ 25 need not avoid primes above 5.
- So FG depends essentially on g_{\*d} = 3, and R2's restriction to the §0 shape is necessary for FG as written.

## (2) Corollary 5/6 — CORRECT in both orientations

**(b), the α side, after normalising g_v = 1.** I checked the order of every product and inverse:
1. w ∈ W\*, so w = g_j a g_j⁻¹ for some a ∈ U_j.
2. If wu ∈ g_jU_jU_v with u ∈ U_v, then w ∈ g_jU_jU_v·u⁻¹ = g_jU_jU_v.
3. Multiplying on the left by g_j⁻¹ gives a g_j⁻¹ ∈ U_jU_v, hence g_j⁻¹ ∈ a⁻¹U_jU_v = U_jU_v.
4. Inverting gives g_j ∈ (U_jU_v)⁻¹ = U_vU_j. Writing g_j = ub, we get u = g_j b⁻¹ ∈ g_jU_j ∩ U_v.
5. U_v equals g_vU_v only because g_v = 1, so this contradicts disjointness. The normalisation is therefore essential, not cosmetic.

**Coset count for (b).**
- W\*U_v is right-U_v-invariant, so it is a union of μ(W\*U_v)·n_v ≥ n_v/6 left U_v-cosets.
- g_vU_v is one of these cosets, and none of them meets ∪_{j≠v} g_jU_j.
- LFC (b) and (c) give Σ_j y_j t_j = Σ_{C ≠ g_vU_v} Σ_{j∈S_C} y_j ≤ #(fibres met) ≤ (5/6)n_v.
- Here t_j/n_v = α_vj/g_vj, and μ(W\*U_v) = μ(U_vW\*).
- The bound is the non-strict ≤ 5/6, and the Row Lemma correctly requires val > 5.

**(a), the α\* side.**
- W ⊆ U_j gives U_vW ⊆ U_vU_j, which is disjoint from D_j by (V1).
- U_vW and every D_j are left-U_v-invariant, so summing over right cosets gives Σ y_j μ(D_j) ≤ μ(∪D_j) ≤ 1 − μ(U_vW) ≤ 5/6.
- By INV (b), μ(D_j) = α\*_vj/g_vj and d_j = λ\*_j.
- (B) for U is the range part of E1.

**Unified form.** Multiplying the bound by 6 gives val ≤ 5, as stated.

## (3) Row Lemma — CORRECT

**Types and standing facts.**
- λ_j = type(j)·w_j exactly, so label gcds equal type gcds.
- I re-derived (F1)–(F4), with (F3) as replaced by R1.
- For (F4): if 3 ∤ x\*, the types of T3 and d are odd and carry no 3 shared with i\*. So any common factor is a power of 5. It requires h_q ≥ 1, which forces h_\* = 0 and x\* = 5. Since the 5-marker is unique, there is at most one such q.

**Case table.** Every weight not listed is 0. Every total is in units of 1/6.

| Case | Positive weights | Feasibility key | val |
|---|---|---|---|
| (1a) h_d = 0 | T5 at 1/k5; d at 1 | type(d) = 3^F shares nothing with any five | 7 |
| (1b) h_d ≥ 1, some z ∉ T5 | T5 at 1/k5; z at 1 | every C-type is unmarked, gcd(x_z, 5) = 1 | ≥ 6 |
| (1c) x\* ≠ 5 | T5 ∪ {d} at 1/5; i\* at 4/5 | i\* shares nothing with any five; sets through i\* lie in {i\*, d} | ≥ 26/5 |
| (1c) x\* = 5 | all six at 1/5 | pairwise gcds all 5; the 6-set is excluded by Sun(6) | 27/5 |
| (2) x\* = 3 | all six at 1/3 | pairwise gcds all 3 (Sun(4)) | 17/3 |
| (2) x\* ≠ 3 | T3 ∪ {d} at 1/3; i\* at 2/3 if q exists, else 1 | (F4) | 8, or ≥ 17/3 |
| (3a) | K at 1/3; z at 1 if x_z = 1, else 2/3 | sets through z lie in {z, i\*} | ≥ 17/3 |
| (3b) with q | T3 ∪ {d} at 1/3; i\* at 2/3 | q and z are incompatible | 7 |
| (3b) no q | T3 ∪ {d} at 1/3; i\* and z at 1/2 each if compatible, else 1 each | compatible iff x_z is even, or z = p and x\* = 5 | ≥ 31/6, or ≥ 17/3 |
| (4) basic | T3 at 1/2; z's by the stated rule | T3 and the z's are incompatible | 3 + V_Z |
| (4a) x\* = 3 | K at 1/3; ones at 1 | the ones are isolated | 17/3 |
| (4a) x\* ∈ {1, 2, 4} | T3 at 1/2; ones at 1; i\* at 1 | i\* is isolated | ≥ 6 |
| (4a) x\* = 5 | q ∈ T3: i\* at 1/2. q a one: y_q = 0, i\* at 1. q = d or no q: i\* at 1 | | 15/2 · 9 · 10 |
| (4b) x\* = 3 | K at 1/3; twos at 1/2 | {z1, z2, i\*} has all gcds 2 (Sun(3)) | 17/3 |
| (4b) x\* ≠ 3, triple not allowed | T3 ∪ {d} at 1/3; twos at 1/2; i\* at 1/2 | {i\*, z} sums to 1; {i\*, q} sums to 5/6 | ≥ 31/6 |
| (4b) triple allowed | T3 ∪ {d} at 1/3; i\* at 1 | see the branch check below | 23/3 |
| (5) | t at 1; standard weights on Z | t shares nothing with Z | ≥ 6 |
| (6) | d at 1; standard weights on O' | d shares nothing with O' | ≥ 6 |

**Basic certificate in (4).**
- {2,4} and {4,4} give 7; {1,2} gives 6; {1,4} gives 8.
- Only {1,1} and {2,2} give exactly 5, and those are exactly cases (4a) and (4b).

**The flagged branch: {2, 2, i\*} allowed, with a 5-marked two and x\* = 5.**
- gcd(z, i\*) = 2·5^[h_z ≥ 1 and 5 | type(i\*)].
- So the triple is allowed exactly when z = p and x\* = 5, which forces h_\* = 0.
- Then the unique 5-marker lies outside T3 ∪ {d}, and 3 does not divide x\*.
- Therefore i\* has no positive-weight partner, and the total is 8/3 + 5 = 23/3.

**Completeness.**
- k5 ≥ 1 splits into: h_d = 0; h_d ≥ 1 with k5 ≤ 3; h_d ≥ 1 with k5 = 4.
- Then k5 = 0 and k3 ∈ {4, 3, 2, 1, 0}.
- Case (4) splits further by the pair {x_z1, x_z2}.
- The smallest margin is 31/6 − 5 = 1/6. Every case gives a strict val > 5.

**E, F and h.** Only E ≥ 1 and F ≥ 1 matter, together with which vertex carries the 5-marker.

**Final step.**
- x_vd ∈ {1, 2}: α_vd ≤ 2 by E1, and α\*_vd ≤ 3 − α_vd by INV (b).
- The Row Lemma gives α_vd = α\*_vd = 2.
- That gives 4 ≤ g_vd = 3 against INV (b) (via E7), a contradiction.

## (4) Theorem K63-RES and the K6.3 closure — CORRECT

**Why the §0 shape is exactly the remaining class.**
- d ∈ A_3∖A_2 gives f_d ≥ 1 and e_d = 0.
- With f_d ≥ 2, P1(iv) forces f_c = 1 on all of C.
- P1(iii) places the unique vertex with e ≥ 2 in C.
- a ≤ 1 allows at most one 5-marker.

**Exhaustive split of K6.3.**
- f_d = 1: excluded by K63-D.
- f_d ≥ 2 with no vertex of e ≥ 2: excluded by K63-E.
- f_d ≥ 2 with e_{i\*} ≥ 2: excluded by this file.
- K63-U0 is redundant here.

**R0 lift.**
- N = ∩ core(U_i) is normal and lies inside every U_j and every g_jU_jg_j⁻¹.
- So W_Q, W\*, D_j and L_j are all unions of N-cosets.
- Indices, β, α, α\*, measures and disjointness all pass to G/N; see 8621e744, item 6.

**Conclusion.** If this file is accepted, class K6.3 is excluded entirely. Full Sun(7) remains open, as the file itself says.

## (5) Restricted star remark — CORRECT as restricted

**Inside the residue, the remark is redundant.**
- Under R2 the remark lives inside the residue, so it is an immediate instance of Theorem K63-RES.
- More specifically, it is Row Lemma case (2) with x\* = 3, applied in both orientations.

**The route offered in the file goes through CLIQUE.**
- The file justifies the remark via FG plus CLIQUE steps (ii)–(v).
- c792dc68 accepts CLIQUE only in its full-clique form, and states explicitly that it is "NOT the withdrawn single-star theorem". So this route reuses proof steps outside the accepted scope.

**My reconstruction of those steps, from c792dc68's summary.** They do use only v's row plus index data:
- α_vc = α\*_vc = 3 forces D_c = Y_c.
- All C-labels at v are 3 times pairwise-coprime cofactors, so Sun(4) allows at most three pieces per fibre.
- The counting gives 6m1 + 9m2 + 10m3 ≤ 25/3, together with m1 + 2m2 + 3m3 = 5/2, hence m1 = m2 = 0.
- d can overlap the C-union only through gcd(d, i\*) = 6, and only inside D_{i\*}.

**Necessity of R2.** The (1) mutation shows that FG's proof does not transfer to other K6.3 shapes, so R2's restriction is needed.

---

## Import-scope ledger

| Fact | Where used | Accepted scope | Status |
|---|---|---|---|
| R0; P0/P1; K6.3 definition | §0, §4 | README §§1, 2, 5; 8621e744 item 6 | OK |
| Product formula for arbitrary subgroups | §1 step and final line; §2(b) | README L0.1 | OK, but cited as "L0.3" (m1) |
| α ≤ g − 1 | (B) for U | E1 | OK |
| INV (a) with E6; INV (b); E7 | (B) for U\*; q = α\*; §4 | 8621e744 | OK |
| LFC (a)–(c) and the summation in (d) | §2(b) | 8621e744 | OK |
| ROW-U standard weights; E8 | §3 | 8621e744 item 3 | OK |
| VFC (V1) | §2(a) | 73a25ba6, as listed in LFC-INV's imports; read by the parent at 8621e744 item 2 | OK |
| VFC (V2)–(V4) and the count | §2(a) | cited inside the accepted CLIQUE (c792dc68 overlay); no verdict named in K63-RES | **gap in citation, removable (m3)** |
| TG | listed in §0 only | the triple form only | not needed (m2) |
| Sun(2), Sun(3), Sun(4), Sun(6) | through LFC (c) and (V3) | imports for t ≤ 6 | OK; Sun(5) unused (m9) |
| K63-D, K63-E | closure only | 1a1c6390 conclusions | OK |
| CLIQUE proof steps (ii)–(v) | §6 only | outside c792dc68 | **scope gap, not load-bearing (m7)** |

## MINOR findings

**m1. The product formula is cited as "L0.3".**
- Where: §0 premise "L0.3 identity", used in the §1 step for μ(V_eW_m), in the §1 final line, and in §2(b) for μ(W\*U_v).
- Problem: E1 states the identity for coset-disjoint pairs U_i, U_j. Here one factor is a multi-intersection or an arbitrary H.
- The fact itself is true.
- Repair: cite README L0.1 plus Lagrange for these uses, and keep E1 only for the range α ≤ g − 1.

**m2. TG is cited in a form that is not its accepted statement.**
- Where: §0 premise "TG … general computational form".
- Problem: the accepted TG statement is the triple form μ(X_a ∩ X_b ∩ X_c) ≥ 1/gcd(n_v, T), while FG needs |Q| up to 6.
- FG's own last display already derives the bound from L0.1 and lcm | [G : H ∩ W_Q].
- Repair: drop TG from the premises. This also confirms that no TG or CLIQUE premise is load-bearing.

**m3. No verdict is named for VFC (V2)–(V4) and the VFC count.**
- Where: §0 premise "VFC (V1)–(V4) and the VFC-count argument … accepted", used in §2(a).
- Problem: no controlling verdict is named for (V2)–(V4) or for the count.
- Preferred repair, which avoids VFC entirely: prove (a) as (b) applied to the inverted configuration.
  - INV (a) with E6 preserves the labelled index tuple, so the same v is chosen.
  - The inverted configuration's own conjugate family is g_i⁻¹(g_iU_ig_i⁻¹)g_i = U_i. After normalising its v-representative, this becomes a conjugate of U, with β = α ≤ g − 1 by E1.
  - LFC for that configuration has labels [U_v\* : U_v\* ∩ U_j\*] = n_jα\*_vj/g_vj.
  - It therefore yields Σ y_j α\*_vj/g_vj ≤ 5/6, which is exactly (a).
- Alternative repair: cite the verdict that accepts (V2)–(V4) and the count.

**m4. One letter for two objects.**
- Where: §0, §1 and (B).
- Problem: "V" denotes both the vertex set and the subgroup family in (B) and FG ("FG for V = U").
- Repair: rename the family.

**m5. The normalisation sentence is incomplete.**
- Where: §2, opening sentence ("indices, intersections and disjointness are unchanged").
- Problem: left-translating by g_v⁻¹ conjugates U\*, and hence W\*.
- α\* and (B) are invariant under this conjugation, so FG still applies. The contradiction step in (b) needs g_v = 1.
- Repair: say so in one sentence.

**m6. (1b) appeals to (F3) outside its domain.**
- Where: §3 (1b), "z is incompatible with every five", and R1's "Effect" paragraph.
- Problem: z may be a three, which lies outside (F3)'s domain {1, 2, 4}.
- The claim is true directly: h_d ≥ 1 forces every C-vertex to be unmarked, so type(z) = x_z ≤ 4 and type(five) = 5.
- Repair: replace the appeal to (F3) with this line.

**m7. "Not used: K63-CLIQUE" conflicts with §6.**
- Where: §0 "Not used: K63-CLIQUE", versus §6 "steps (ii)–(v) use only v's row".
- Problem: §6 does reuse CLIQUE proof steps, outside the accepted scope.
- Repair: justify §6 by K63-RES, or by Row Lemma (2) with x\* = 3, and narrow the "Not used" line to "for Theorem K63-RES".

**m8. CLIQUE is described as a special case of the residue.**
- Where: §5, "K63-CLIQUE is the special case of the residue…".
- Problem: CLIQUE is stated for all of K6.3. Its overlap with the residue is the instance k3 = 4, x\* = 3 of Row Lemma (2).
- Repair: reword.

**m9. The load-bearing Sun instances are not listed.**
- Where: §0, Sun clause. The load-bearing instances are:
  - Sun(2): incompatible pairs, in every case.
  - Sun(3): {two, two, ·}, and {z1, z2, i\*} in (4b).
  - Sun(4): the gcd-3 cliques in cases (2)–(4).
  - Sun(6): (1c) with x\* = 5.
- Sun(6) is genuinely necessary there. Without it, the all-six constraint Σy ≤ 1 caps val at 5.
- Sun(5) is unused.
- Sun(6) is an accepted import, but it is computer-assisted (8621e744, Limits). So "no computation is a premise" holds for this file, not for its whole import closure.
- Repair: list the instances, in the style of the K62-A overlay.

## Not re-verified: outside the packet

- **K63-D and K63-E errata:** I used only the conclusions stated in 1a1c6390.
- **K63-TG-v1 and its errata v1–v3:** the CLIQUE steps were reconstructed from c792dc68's summary only.
- **Verdict 73a25ba6:** not read.
- **§§6–7 self-reports:** navigation only; not needed.
