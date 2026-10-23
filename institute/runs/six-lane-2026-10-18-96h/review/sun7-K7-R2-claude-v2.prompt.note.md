# R2 review: K7-CASEA-K23 and K7-CELL

**Reading order.** K23 is read with K23E (`15b1516d…`). CELL is read with CELLE (`56829e8d…`). The consolidated overlay `ecff4e76…` items R2.1–R2.4 are applied last. Imports follow the A1/A2 verdict `2a7c5b6c…` (overlay v1, then v2), RICH/D23P `1167bc4f…` and LFC/INV `8621e744…`.

**Result: 0 FATAL, 0 MAJOR, 14 MINOR. No claim is rejected.**

**Limits of this review:**
- It checks the written proofs only. I did not verify any hashes, and I did not verify that the Old spans are byte-unique.
- I visually matched the Old spans I used against the embedded copies: K23.1, R2.1–R2.4 and C.1–C.4. Each occurs once there.
- I received only lines 1–114 of `ecff4e76`: the header and items R2.1–R2.4. I did not see the DAG.*, META.*, R3a or R3b items. If those rewrite the K23 or CELL status lines or CELL §7, that rewrite is not covered here.

## 1. Per-claim verdicts

| Claim (with repairs applied) | Verdict | Findings |
|---|---|---|
| (R-a) row shapes, d and d* in {1,2,3}, at most one entry 1 | ACCEPT-WITH-FIXES | m4 |
| (R-b) twin rule | ACCEPT | m8 (citation only) |
| (R-c) R1 (import), R1⁻, R5, R4, R6, R3′ (K23.1), the two e = 1 exclusions | ACCEPT-WITH-FIXES | K23.1 is mandatory; m2, m3 |
| Lemma K3 (R2.2) | ACCEPT | — |
| Lemma K2 | ACCEPT | depends on K23.1 |
| Lemma CL | ACCEPT | — |
| Lemma S (i), (ii) | ACCEPT | — |
| (S-a), (S-b), (S-c), (S-d) | ACCEPT | — |
| (S-e) | ACCEPT | m5 (optional simplification) |
| (S-f) with R2.1 | ACCEPT-WITH-FIXES | m5 |
| Theorem K7-CASEA-K23 | ACCEPT-WITH-FIXES | m1, m6 |
| Proposition K7-CASEB-T | ACCEPT-WITH-FIXES | m7 |
| Lemma EQ (C.1 as amended by R2.4) | ACCEPT-WITH-FIXES | m9 |
| Lemma SUB | ACCEPT | — |
| Lemma IN (R2.3), including the lower bound | ACCEPT | m13 (cosmetic) |
| Lemma CELL (i)–(iii) | ACCEPT-WITH-FIXES | m10 |
| Theorem K7-CELL-A (C.2, C.3) | ACCEPT-WITH-FIXES | m10, m11, m13 |
| Theorem K7-CELL-B (C.4) | ACCEPT-WITH-FIXES | m12, m13 |
| CELL §7 chain | Valid as a conditional chain (see §4) | m14 |

## 2. Findings

**FATAL:** none. **MAJOR:** none.

**MINOR** (each with a minimal fix):

- **m1. K23 Corollary L accounting.** The header says Corollary L enters "only through 'at least two entries 4'". That is false: §4 also uses Corollary L to exclude 44411, via the b = 3, k1 = 2 kill. That kill needs only Sun(2), so the Sun(5)-free claim is unaffected.
  *Fix:* add "and, in §4, the Sun(2)-only exclusion of 44411". Alternatively, cite LFC(d) at t in C^α directly: y = 1/3 on the fours and 1 on the ones gives value 6.
- **m2. (R-c) R4 is new, not imported.** K23's R4 = (1,4,4,4|e) has c = 3 and e ∈ {2,4}. The accepted TC R4 has c ∈ {1,2}. So K23's R4, and its c = 3, e = 1 exclusion, are new claims proved here. Both proofs are valid for every E ≥ 1. K23's R5 is likewise proved E-free; it coincides with the accepted TC R5 when E ≥ 2.
  *Fix:* rename it (for example R4^(c=3)) or add "new at c = 3".
- **m3. (R-c) R6 states less than (S-f) uses.** The bold conclusion gives only L_s ⊆ L_f. (S-f) uses L_c ⊆ L_v1, where c and v1 are both fours. That containment does follow from R6's displayed fibre property.
  *Fix:* add "and L_f = L_f′ for any two fours". Also change "the two s" to "the vertex s with entry 2".
- **m4. (R-a) The bound d ≤ 3 is not justified in the text.**
  *Fix:* add one line: d* ≥ 1 and F ∩ F* = ∅ give d + d* ≤ 4.
- **m5. (S-f) and (S-e) assert entries without justification, and both cases are immediate.**
  - The (S-f) bullets after R2.1 use α*_v1v3 = α*_v1v4 = α*_v3c = 2 without justification. These values are true: the F*-neighbourhoods {c}, {v4}, {v3} and {v1,v2} pairwise differ, so (R-b) excludes 1.
  - More simply, both whole cases close in one line, as (S-a) already does. In (S-f) the vertices v1–v4 have d* = 1; in (S-e) so do v1, v2, b1, b2. By (R-a) these four vertices lie in P*. So |P| ≤ 1. F* has three edges, so CL gives |P| ≥ 2.
  - *Fix:* use this one-line kill, or add the twin justification.
  - Either way, R2.1 is correct but not load-bearing.
- **m6. §4, branch α_v1v2 = 1.** The mass list at apex x omits t, whose mass is α*_xt/6 ∈ {1/6, 2/6}. The omission is harmless.
  *Fix:* add "t: α*_xt/6, unused". Also change "some coset" to "some right U_x-coset R ⊆ D_y ∩ D_v1 (= D_y ∩ D_v2)".
- **m7. CASEB-T uses rigid rows outside the Case-A setting of K23 §0.**
  *Fix:* add a note that R1 and R1⁻ use only the labels at u: W-part {2,2,4,4}, c = α*_za = 3 for a ∈ T*, and e ∈ {1,2}. Both rows therefore hold in Case B, where E ≥ 2 by CASEB.
- **m8. Triangle-rule citation.** (R-b) and R2.1 cite the "accepted triangle rule". The conclusion list of `2a7c5b6c` does not name A1-STRUCT §0 separately.
  - The rule is an immediate specialisation of the accepted L1 (T1)–(T3): every ℓ is odd, so τ_min = r and τ_max = pq.
  - I re-derived it independently.
  - *Fix:* cite rules-k7 L1 alongside A1-STRUCT §0.
- **m9. EQ: definition of Q.**
  *Fix:* define Q := D_g1 ∪ D_g2. A right U_a-coset meets g_jU_j if and only if it lies in D_j. Also note that the z-mass hypothesis is never used.
- **m10. CELL (i) is invoked by C.2 outside its stated hypothesis.** The statement assumes the K-vertices lie in distinct K-cosets. C.2 uses it when t may share v_i's coset.
  - The facts C.2 actually needs are proved by the (i) argument without that hypothesis:
    - [G:K∩L] = 9 and the cell bijection follow from LK = G alone.
    - Any vertex v with U_v ⊆ K and m^L_v = 3 meets every cell of g_vK, in a coset of U_v∩L of index n_v/3. The symmetric statement holds for L.
  - *Fix:* state (i) in this vertex-wise form.
  - Also say explicitly that index 9 comes from U_xK = G, not from K ≠ L. Two distinct index-3 subgroups can meet in index 6; the order-2 subgroups of S₃ are an example.
- **m11. CELL-A, m-step.** The text says g_uU_u "meets a K-coset containing the coset of v1, v2 or t".
  *Fix:* justify it by g_v1K ≠ g_v2K (from SUB): any two of the three K-cosets include one of these two. The position of t is not yet known at that point, and the argument does not need it.
- **m12. CELL-B, index of z's piece.**
  *Fix:* write N_z = [K′∩H : U*_z∩H] = [G : U*_z∩H]/9, using U*_z ⊆ K′. This makes visible that it is the index of a cell piece.
- **m13. Import lists.**
  - CELL omits L0.2 (used in SUB) and LFC erratum E6 (used for "nor its inverse" and for the mirror case).
  - The package cites LFC (a)–(c) for IN, but IN uses only (a)–(b).
  - IN's sentence "y_i = 1 is feasible" is unnecessary.
- **m14. Stale status and metadata (historical, per instructions).**
  - Stale relative to `2a7c5b6c`: the K23/CELL headers, §7's "each link is pending review", and the package import table.
  - Package §2 still quotes the invalid R3′ vector and the pre-R2.4 gloss of C.1.
  - Consumers must read K23E, CELLE and `ecff4e76`. The status items of `ecff4e76` were not seen (see Limits).

## 3. Focus points checked

**Labels at u ∈ W (c = 3) and their gcds:**
- A one against anything: 1.
- Two–two and two–four: 2.
- Four–four: 4.
- z–two: 2; z–four: 2^min(E,2).
- W–t: gcd(entry, e).
- z–t: 3·gcd(2^E, e).

**R3′ under K23.1:**
- Values: y1 = (o 1, f ½, s ½, s′ ½) and y2 = (o 1, t ½, s ½, s′ ½) both have value 1+2+1+1 = 5.
- Feasibility: {f,s,s′} and {t,s,s′} have pairwise gcds 2,2,2, so neither is allowed (Sun(3)). The one o is singleton-only (Sun(2)).
- Fibres containing o: there S_C = {o}, so f and t are both absent.
- Every other occupied fibre: subtracting the two weight-1 equations gives [f] = [t].
- Fibres containing z: o is absent, so two of {f,s,s′} are present. They cannot be s and s′, because {z,s,s′} has gcds 2,2,2. So f is present, and therefore t is present.
- The old printed y2 (t weight 1) has value 7. It is also infeasible: {t,s} is allowed and would carry weight 3/2.

**R1⁻:** y1 alone suffices.
- t has e = 1, so its label is coprime to every W-label. Hence t ∈ S_C forces S_C ⊆ {t,z}.
- Otherwise [f] + [f′] = 2.
- So L_f = L_f′, for every E.

**The other rows:**
- R5, R4 and R6 have value 5; the two e = 1 exclusions have value 6.
- All are feasible as displayed, and all are E-free.
- The row list is exhaustive: d = 1 gives only R3 and R3′ (Lemma B, e = 4).

**K3 and K2 orientation.**
- In C^x at apex a ∈ W, the D-masses are x*/6. Lemma TC needs u, a, j distinct (R2.2), and FG-V needs a ∈ W.
- K2: work in C^{x*} at apex a. The masses are x_at = 4 and x_as = 2, so 6 > 5.
- Why x_as = 2: INV gives x_as ≤ 2. If x_as = 1, s and a are twins, so s has type (1,1), which (R-a) excludes.

**Lemma S and the (S-*) cases.**
- The parities and part (i) check, and (ii) yields exactly six vectors.
- (S-b): F* is the complementary 5-cycle and there are no ones.
  - Kill at apex u1 in C^{α*}: α_{u1c} + α_{u1a} = 4 + 2.
  - Kill at apex b in C^α: α*_{bu0} + α*_{ba} = 4 + 2.
- (S-c): all three graph shapes reduce to K2.
- (S-d), path case: K3 at w, then K3 at y.
- R2.1: I concur that the original step was unsupported. N_F*(v1) = N_F*(v2) = {c}, so α*_v1v2 = 1 is possible, and then 4 + 1 = 5 gives no contradiction. The replacement is correct: the triangle (1, α_tv2, 4) forces α_tv2 = 4 > 2.

**Theorem K23.**
- Note that N_F(x) = N_F(y) = N_F(w) = {v1,v2}, so (R-b) does not exclude an entry 1 inside {x,y,w}.
- The proof still holds. A row (1,2,4,4|e) is either R5 (e ∈ {2,4}) or excluded (e = 1), so it is rigid. Hence "not R2" implies L_v1 = L_v2.
- K3 at v1 then gives α*_v1v2 + α*_v1x = 4 + 2. So the row is R2, which forces both twos.
- Branch α_v1v2 = 1:
  - D_z is disjoint from D_v1 and D_v2 (R4 plus Lemma TC).
  - FG-V gives D_v1 = D_v2 = U∖D_z.
  - Since μ(D_y) = 4/6 > 3/6, some R lies in D_y ∩ D_v1 ∩ D_v2. The local indices are 4w, 2w, 2w, which Sun(3) forbids.
- Last step: Γ^{α*} = F = K₂,₃ is connected, and Corollary L excludes 44411.

**CASEB-T.**
- The α*-row at a is (2,2,4,4|3|α*_ta).
- For α*_ta ∈ {1,2} it is R1 or R1⁻. K3 at v1 in C^{α*} then gives 4 + 2 = 6.

**EQ.**
- Local-index gcds: 4 between the g's; 2 for g–s and s–s.
- The odd parts of the five non-z indices are pairwise coprime: they are the w's and 3^A 5^Bt w_t.
- Counting the s-mass: 1 ≤ μ(Q) + 2(μ(U) − μ(Q)), so μ(U) ≥ 5/6. This saturates FG-V.
- Old C.1's coprimality of "all" indices was false: z and t both carry a factor 3. It was never used, and R2.4 states the correct version.

**SUB.**
- U_jU_k ⊆ ⟨U_j,U_k⟩ ⊆ X_j, and all three have measure 2/6, so they are equal.
- The cosets are distinct by L0.2 for the pairs (a,j) and (j,k). The pair (a,k) is distinct if and only if x_ak = 2.

**IN.**
- The group g_iU_ig_i⁻¹ acts transitively on the m^K_i K-cosets that g_iU_i meets.
- Each such coset therefore contains t_i/m^K_i fibres of L_i, and t_i/m^K_i ≤ n_j/3 − 1. This gives x_ji < 2m^K_i.
- The argument uses g = 6, so it is a K7 statement.

**CELL.**
- Index of a vertex piece: n_v·m^L_v/9 = n_v/3.
- (ii): N_z = n_z·b₁b₂/9 with b₁, b₂ ≤ 3, so its prime factors lie in {2,3} or divide r_z.
- (iii): the three translated pieces are disjoint cosets of subgroups of K∩L, so Sun(3) applies inside K∩L.

**CELL-A.**
- SUB at v_i yields K ⊇ U_v1, U_v2, U_t.
- LFC(d) at t in C^{α*} allows α*_t = 1 on at most one of x, y, w. SUB at x then yields L.
- m^K = 3 on {x,y,w} and m^L = 3 on {v1,v2,t}.
- t gets its own K-coset by Sun(3) in K∩L.
- z avoids the cells of the K-cosets of v1 and v2, so U_z ⊆ K. Then 1/2 = μ(U_zU_v1) ≤ 1/3, a contradiction.

**CELL-B.**
- C.4 is right: in C^α the a-labels at t would be 2w, not 4w.
- N_z = 2^(E+1) 5^Bz w_z m^H_z/3. Integrality forces m^H_z = 3.
- The pieces of t, a and z then have indices 2·3^A 5^Bt w_t, 2w_a and 2^(E+1) 5^Bz w_z. Since Bz·Bt = 0, their pairwise gcds are all 2, which Sun(3) forbids.

**Saturation.**
- Every value-5 or 5/6 saturation step is at u, a ∈ W, in an actual orientation.
- At t, the proofs use only plain LFC(d) (bound < 1) and PFG-t/Corollary L. The connectivity hypotheses were checked in (S-a), (S-e), (S-f) and §4.
- Nothing saturates at z.

**R1 at E = 1** is never load-bearing in this slice. Every branch here has E ≥ 2, either from a single-four row via Lemma B or from CASEB.

## 4. Does §7 close (a1)?

**Yes, conditionally.** It rests only on now-accepted imports plus the claims accepted above:

- **Partition.** TZ(iii) splits (a1) into exactly three cases: Case A (T = T* = W), Case B (T = W ≠ T*) and the mirror (T* = W ≠ T).
- **Case A, all-(2,2) type:** excluded by TC-A22, accepted for every E ≥ 1.
- **Case A, any other type:** K23 reduces it to the K₂,₃ family or its inverse, which CELL-A excludes.
- **Case B:** CASEB and TC-B (accepted) plus CASEB-T reduce it to data that CELL-B excludes.
- **Mirror:** handled by INV/E6.
- **Arbitrary groups:** R0.
- **No hidden imports.** The slice uses no item from the non-transferred sections listed in `2a7c5b6c`.
- **Sun instances.** Direct uses are Sun(2) and Sun(3) only, including Sun(3) inside K∩L. The transitive closure reaches the computer-assisted Sun(5) and Sun(6) records. Sun(7) is not used.

This is a single-family review. Parent acceptance, and the scoped Codex repair review, are still pending. So this review alone does not establish that (a1) is closed.

## 5. Active repaired dependencies

**Slice repairs:**
- K23.1: mandatory. K2, S(i) and (S-c) depend on it.
- R2.2: mandatory.
- R2.3: mandatory.
- R2.4 amending C.1: mandatory reading of EQ.
- C.2: mandatory. The original citation of CELL (iii) was circular.
- C.4: mandatory.
- C.3: typo only.
- R2.1: correct but non-load-bearing (m5).

**From the accepted overlays (v1, then v2):**
- TC.7 with V2.3 (FG-V, finite G).
- TC.2 (orientation dictionary).
- A1.9 (Corollary L as a necessary condition only).
- A1.4, V2.1 and TC.2 (Sun accounting).
- A22.1–A22.4 (through TC-A22).
- TC.4 (R1 for E ≥ 1): imported, but not load-bearing here.

**From RICH/D23P:** FG7(b) in chain form (Item 1a), and the Corollary 5/6 occupied-fibre equality clause (Item 2a).

**From LFC/INV:** E1, E2, E6, E8.

R3a and R3b remain conditional on this R2, and R3b also on R3a. Neither is reviewed here.

## 6. Exact conclusions and open cases

**Proved, if the parent accepts this slice** (all in (a1), for every group):
1. In Case A, every type other than all-(2,2) is, up to inversion, the K₂,₃ family carrying the data stated in Theorem K23.
2. In Case B, α_ta = 2 and α*_ta = 4 for every a ∈ T*.
3. EQ, SUB, IN and CELL hold at their corrected scopes. EQ needs an apex in W of an actual configuration; IN is a K7 statement.
4. The K₂,₃ family and its inverse are empty. Case B and its mirror are empty.
5. Therefore (a1) contains no configuration. The closure includes the computer-assisted Sun(5) and Sun(6) imports.

**Still open:**
- the (a2-no5) residue;
- (a2-zt5) beyond S1–S5 (no A2-ZT5 theorem is accepted here);
- any transfer of K23 or CELL to (a2). The transfer audit `84cf9555…`, R3a and R3b are all unreviewed here;
- K6.2*, full K7 and Sun(7).

No novelty claim is made.
