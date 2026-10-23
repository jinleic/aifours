# rules-k6-v3: lemmas XE, N2-6 and RPLP, plus the certificate formats (addendum to rules-k6-v1 and v2)

The host-clock freeze record is in `evidence/freeze-v3.sha256`. rules-k6-v1 (3b135fea…b187) and rules-k6-v2 (b45049a0…fa6) stay frozen. Here [NEW] means only "written in this lane". All sizes below are in units of |G|.

**Why these lemmas.** The frozen run engine-v2-core56 left 263 orbits (11:20 PDT). All of them have E2 at vertex 0 and E3 at vertex 1, and almost every α in them is 2 or 4. The lemmas below target that family.

## L10. XE: equal products force an index-5 subgroup [NEW]

**Statement.** In Core5(6), let v, j, k be distinct and suppose U_vU_j = U_vU_k. Then α_jk = 1, W = U_jU_k is a subgroup of index 5, and [U_v : U_v∩W] = α_vj.

**Proof.**
1. X := U_vU_j = U_vU_k is right-invariant under U_j and under U_k, hence under W := ⟨U_j, U_k⟩.
2. Since U_v ⊆ X, we get U_vW ⊆ X. Also X = U_vU_j ⊆ U_vW. So X = U_vW.
3. |X| = α_vj/5 < 1 (L0.3), so W ≠ G.
4. Both U_j and U_k lie in W, so [G:W] divides gcd(5r_j, 5r_k) = 5. Hence [G:W] = 5.
5. U_jU_k ⊆ W, so α_jk/5 = |U_jU_k| ≤ |W| = 1/5. Hence α_jk = 1, and then U_jU_k = W.
6. Finally |U_vW| = [U_v : U_v∩W]·|W|, so α_vj/5 = [U_v : U_v∩W]/5. ∎

**Corollary.** If α_jk ≥ 2, then X_j ≠ X_k at every vertex v.

## L11. N2-6 [NEW]

**Statement.** In Core5(6), let v be a vertex such that:
1. r_v is odd, i.e. v ≠ E2;
2. α_vj = 2 for all five j ≠ v;
3. α_jk ∈ {2, 4} for every pair j, k ≠ v;
4. if v = E3, then 3 ∤ τ_jkl for every triple j, k, l ≠ v. A sufficient check: in every such triangle, τ_max(jkl) < 3·τ_min(jkl) whenever 3 ∤ τ_min(jkl).

Then no configuration exists.

**Proof.** Translate so that g_v = 1. For j ≠ v put X_j = U_vU_j, so |X_j| = 2/5.

1. **Each pairwise intersection is exactly a fifth.** Fix j ≠ k.
   - (T1) on the edge jk, whose opposite vertex is v: α_jk | r_vτ_vjk. Since r_v is odd and α_jk ∈ {2, 4}, α_jk | τ_vjk, so τ_vjk ≥ α_jk.
   - Put Z_jk := U_v(U_j∩U_k). By (T3), |Z_jk| = τ_vjk/(5α_jk) ≥ 1/5, and Z_jk ⊆ X_j∩X_k.
   - By (P2), |X_j∩X_k| is a multiple of 1/(5·gcd(r_v, α_jk)) = 1/5, because r_v is odd.
   - By XE, X_j ≠ X_k, so |X_j∩X_k| < 2/5.
   - Hence |X_j∩X_k| = 1/5. Then |Z_jk| = 1/5 and X_j∩X_k = Z_jk.
2. **The three fifths of a triple coincide.** Fix a triple j, k, l ≠ v and put W = U_j∩U_k∩U_l.
   - [G:W] = 5r_jr_kr_lτ_jkl.
   - Q := [G : U_v∩W] is a common multiple of [G:W] and of T_vjk = 5r_vr_jr_kτ_vjk. So Q is a multiple of 5r_jr_k·lcm(r_lτ_jkl, r_vτ_vjk).
   - gcd(r_v, r_lτ_jkl) = gcd(r_v, τ_jkl). This equals 1: τ involves only the primes 2 and 3, r_v is odd, and either v ≠ E3 or 3 ∤ τ_jkl by condition 4.
   - So r_v·r_lτ_jkl divides that lcm, and Q ≥ r_v[G:W].
   - Therefore |U_vW| = Q/(5r_v[G:W]) ≥ 1/5.
   - U_vW ⊆ Z_jk ∩ Z_jl ∩ Z_kl, and each Z has size 1/5. Hence Z_jk = Z_jl = Z_kl.
3. **Contradiction.** Any two pairs from the five neighbours are linked by a chain of triples, so all ten sets Z_jk are one set Z with |Z| = 1/5. The five sets X_j ∖ Z are pairwise disjoint, each of size 1/5. So |∪_j X_j| = 1/5 + 5/5 = 6/5 > 1. ∎

## L12. RPLP: Lemma R combined with the vertex counts [NEW]

**Setting.** A harmonic configuration in Core5(6). Fix a vertex v and normalise g_v = 1. Write N for the five other vertices. For j ∈ N put:
- X_j = U_vU_j and Y_j = G ∖ X_j;
- D_j = U_vg_jU_j, with |D_j| = q_j/5, where 1 ≤ q_j ≤ 5 − α_vj.

**Which sets are right U_v-cosets unions.**
- X_j is left U_v-invariant, so X_j and Y_j are unions of right U_v-cosets.
- D_j is also left U_v-invariant, so it too is a union of right U_v-cosets.
- By (R1), D_j ⊆ Y_j.

**Types of right cosets.** Give each right U_v-coset C the type (A_C, S_C), where A_C = {j : C ⊆ Y_j} and S_C = {j : C ⊆ D_j}. Then S_C ⊆ A_C, and S_C is hereditary-allowed (rules-k6-v2 L9 with rules-k6-v1 L7, evaluated with maxgcd).

**Forced containments.** Suppose τ_min(v,w,j) ≥ α_vwα_wj. By (T2) this forces τ = α_vwα_wj. Then (T3) gives |U_v(U_w∩U_j)| = |X_w|, so X_w ⊆ X_j, that is, Y_j ⊆ Y_w. Hence a type with j ∈ A and w ∉ A has measure 0.

**The LP.** For every allowed type (A, S) with A ≠ ∅ that is consistent with the forced containments, let x(A,S) be the total size of right cosets of that type. Then:
- **(E1_j)** Σ_{S∋j} x(A,S) = q_j/5.
- **(E2_j)** Σ_{A∋j} x(A,S) = |Y_j| = (5 − α_vj)/5.
- **(U_jk), (L_jk)** ylo_jk ≤ Σ_{A⊇{j,k}} x(A,S) ≤ yhi_jk, where yhi/ylo = 1 − (α_vj + α_vk)/5 + hi_jk/lo_jk, with hi and lo as in the P rule (rules-k6-v1 L4).
- **(TOT)** Σ x(A,S) = |∪_j Y_j| ≤ 1 − |U_v| < 1, since U_v lies in no Y_j.

**RPLP kill.** Fix v. If, for every admissible q, the minimum of Σ x subject to E1, E2, U and L is ≥ 1 (or the system is infeasible), then vertex v is impossible.

**Certificate (weak duality).** Give a dual vector (a_j, b_j free; u_jk ≥ 0; l_jk ≥ 0) such that:
- for every allowed column (A, S): Σ_{j∈S} a_j + Σ_{j∈A} b_j − Σ_{{j,k}⊆A} u_jk + Σ_{{j,k}⊆A} l_jk ≤ 1;
- the dual objective satisfies Σ_j a_j q_j/5 + Σ_j b_j(5 − α_vj)/5 − Σ u_jk yhi_jk + Σ l_jk ylo_jk ≥ 1.

Weak duality then gives min Σ x ≥ 1. If the primal is infeasible, such a vector exists by Farkas' lemma.

**Soundness.**
- maxgcd only enlarges the set of allowed columns, which lowers the minimum.
- The lo and hi bounds are valid for every admissible τ (rules-k6-v1 L8, M1).
- A forced containment holds whenever its hypothesis holds at τ_min, because that hypothesis pins τ.

## Certificate formats (engine v3; every one is checkable without trusting the engine)

1. **T.** For each special type, the enumeration tree is deterministic. A pruned node records its triangle, its three α's and the statuses. The checker regenerates the tree independently. The engine publishes, for each type: the number of labelled leaves, the number of pruned nodes, and the sha256 of the sorted list of labelled leaf codes.
2. **Orbits.** One line per canonical orbit: type, a representative α-matrix (as a code string), the rule, and its witness.
3. **K (v, S), P (v, pair or S), N2-6 (v).** The checker recomputes each.
4. **RLP (v).** For every admissible q at v, the global file `rlp_duals.json` holds an exact dual y ≥ 0 under the key "q|stats". The dual must satisfy Σ_{j∈S} y_j ≤ 1 for **every** allowed S (all of them, not only the maximal ones) and Σ (q_j/5) y_j ≥ 1.
5. **FH5 ((a,b), V).** The checker re-runs the exhaustive fibre search for all seven E5 placements. The engine records the number of assignments examined in each placement.
6. **RPLP (v).** For every admissible q, either an RLP dual (when the RLP LP for that q is already ≥ 1) or an RPLP dual vector (a, b, u, l) in a canonical constraint order: j in N ascending; then pairs (j,k) in lexicographic order. The checker rebuilds the columns, bounds and forced containments itself and verifies the vector exactly.
