# K7-block-lemma-v1: twin blocks of size ≥ 3 occupy exclusive cosets of an index-6 subgroup

- **Freeze record:** host-clock time and sha256 in `evidence/k7-block-lemma-v1.sha256`.
- **Labels:** [NEW] means written in this lane; it is not a novelty claim.
- **Status:** unreviewed. No computation was run. K7 stays OPEN.
- **Builds on:** `K7-structure-v1.md` (f4534c07…9fc1), with its notation: U is the set of unmarked vertices, M the marked set, ~ the twin relation, and a twin block is a ~-class.
- **Imports, all frozen and written:**
  - rules-k7-v1 L0.3;
  - L6 (XE);
  - L5 (F), used only with 2 ≤ |T| ≤ 4, per rules-k7-erratum-v1 W1. The relevant cases are Sun(2) (L0.6, the Chinese remainder theorem), Sun(3) and Sun(4) (Zhu), applied inside a subgroup;
  - K7-structure-v1 K7-TWIN(b), (c), (d).
- **No least-order frame:** no minimal-counterexample frame or Sun(7) is used.
- **Relation to FH:** this is a single written lemma with one explicit subgroup. It is not the FH certificate rule, which stays UNUSED.

## Lemma K7-BLOCK [NEW]

Let B ⊆ U be a twin block with s := |B| ≥ 3.

**Part (a): one subgroup for the whole block.**
- For distinct j, k ∈ B, the set U_jU_k is a subgroup W_B of index 6, and it does not depend on the pair.
- U_j ⊆ W_B for every j ∈ B.
- The cosets g_jW_B (j ∈ B) are pairwise distinct.

**Part (b): exclusive cosets.**
- For every v ∉ B, g_vU_v meets none of the s cosets g_jW_B (j ∈ B).
- g_vU_v meets exactly α_vB of the remaining 6 − s cosets of W_B.
- Hence α_vB ≤ 6 − s.

**Part (c): F-packing in the remaining cosets.** In each remaining coset C of W_B, let S_C be the set of vertices v ∉ B whose cosets meet C. Put

  λ_v := n_v·α_vB/6.

Then every T ⊆ S_C with 2 ≤ |T| ≤ 6 contains v ≠ v′ with gcd(λ_v, λ_v′) ≥ |T|. Also Σ_{v∉B} α_vB = Σ_C |S_C|.

**Part (d): consequences.**
1. s ≥ 4 is impossible. So every twin block has at most 3 vertices.
2. s = 3 is impossible when M = ∅.

### Proof of (a)

Fix distinct j, k ∈ B and a third v ∈ B, which exists because s ≥ 3.

1. **XE applies.** K7-TWIN(d) at apex v gives U_vU_j = U_vU_k. L6 applied to (v; j, k) gives:
   - W := ⟨U_j, U_k⟩ ≠ G;
   - m := [G:W] divides g_jk = 6;
   - U_vW = U_vU_j;
   - [U_v : U_v ∩ W] = m·α_vj/6 = m/6, since α_vj = 1.
2. **m = 6.** The last item is an integer, so m = 6.
3. **U_jU_k is the subgroup.** U_jU_k ⊆ W, and μ(U_jU_k) = α_jk/6 = 1/6 = μ(W). The sets are finite, so U_jU_k = W. It is a subgroup of index 6; call it W_jk.
4. **Independence of the pair.**
   - Apply step 3 to the pair (v, j), using k as the third vertex: W_vj = U_vU_j is a subgroup of index 6.
   - Step 1 gives U_vW_jk = U_vU_j = W_vj, so W_jk ⊆ W_vj.
   - Both have index 6, so W_jk = W_vj.
   - Two pairs that share a vertex therefore give the same subgroup. Two disjoint pairs {j,k} and {v,w} are linked through {j,v}.
   - So every pair in B gives the same subgroup W_B, and U_j ⊆ U_jU_k = W_B.
5. **Distinct cosets.** g_jU_j ∩ g_kU_k ≠ ∅ iff g_j⁻¹g_k ∈ U_jU_k = W_B, iff g_jW_B = g_kW_B. The cosets are disjoint, so the W_B-cosets are distinct.

### Proof of (b) and (c)

1. **Indices.** For v ∉ B and any j ≠ k in B:
   - K7-TWIN(d) gives U_vU_j = U_vU_k.
   - L6 gives [U_v : U_v ∩ W_B] = 6·α_vj/6 = α_vB, using W = ⟨U_j, U_k⟩ = W_B.
2. **Apply L5 (F) with H = W_B and m = 6.** Each g_lU_l meets exactly t_l := [U_l : U_l ∩ H] left H-cosets. Inside one H-coset, the pieces are pairwise disjoint and, after translation, they are left cosets in H of subgroups of index n_l t_l/6.
   - For j ∈ B: t_j = 1 and the index is n_j/6 = w_j, since j is unmarked.
   - For v ∉ B: t_v = α_vB and the index is λ_v.
3. **No outside vertex meets a block coset.** Suppose v ∉ B meets g_jW_B. Then T = {j, v} must satisfy gcd(w_j, λ_v) ≥ 2 by Sun(2) in H. But w_j is coprime to 30, to w_v and to α ≤ 5, so gcd(w_j, λ_v) = 1. This contradiction proves (b).
4. **Part (c).** (c) is L5 inside each remaining coset. The identity Σ α_vB = Σ_C |S_C| counts incidences.

### Proof of (d)

**Useful gcds.** For v ∈ U ∖ B, λ_v = α_vB·w_v. For z ∈ M, λ_z = α_zB·m_z·w_z, where m_z := 2^{ε_2(z)}3^{ε_3(z)}5^{ε_5(z)}.
- The m_z of distinct marked vertices are pairwise coprime.
- For v ∈ U ∖ B, α_vB ≠ 1, since v is not a twin of B.

**Case s ≥ 6.**
- s = 7: there would be seven distinct cosets of an index-6 subgroup. Impossible.
- s = 6: the seventh vertex v has α_vB ≥ 1, but no coset is left for it.

**Case s = 5.** By (b), α_vB ≤ 1 for both outside vertices.
- Unmarked outside vertices need α_vB ≥ 2, so both outside vertices z, z′ are marked, with α = 1.
- Both lie in the single remaining coset, with λ_z = m_z w_z and λ_z′ = m_z′ w_z′.
- These are coprime, which contradicts Sun(2) in H.

**Case s = 4.** Let R be the three outside vertices and C1, C2 the two remaining cosets.

*Possible values.* By (b), α_vB ∈ {1, 2}, and α_vB = 2 for v ∈ U.

*Pairwise gcds of the λ's are at most 2.*
- Unmarked pairs: gcd(2w, 2w′) = 2.
- Unmarked v with marked z: gcd(2, α_zB·m_z) ≤ 2.
- Two marked vertices: they share no marker prime, and α ≤ 2 carries no 3 or 5, so gcd(α_z m_z, α_z′ m_z′) ≤ 2.

*Each remaining coset holds at most 2 vertices.* A triple T would need a pair with gcd ≥ 3, which (c) rules out. So Σ_{v∈R} α_vB ≤ 4.

*Case by number of marked vertices in R:*

| marked in R | contradiction |
|---|---|
| 0 | Σ α = 6 > 4 |
| 1 | Σ α ≥ 2 + 2 + 1 > 4 |
| 2: z, z′, plus unmarked v | Σ α = 2 + α_z + α_z′ ≤ 4 forces α_z = α_z′ = 1. Then v lies in both cosets, and z, z′ lie in different ones. The pairs (v, z) and (v, z′) need gcd(2, m_z) = gcd(2, m_z′) = 2, so both carry marker 2, which is impossible. |
| 3 | The α's are (1,1,1) or (2,1,1) up to order. (1,1,1): some coset holds two of the vertices with α = 1, and gcd(m_z, m_z′) = 1 < 2. (2,1,1): the α = 2 vertex z_1 lies in both cosets, z_2 in one and z_3 in the other. gcd(2m_1, m_2) ≥ 2 and gcd(2m_1, m_3) ≥ 2 force m_2 and m_3 both even, which is impossible. |

**Case s = 3 with M = ∅.** All four outside vertices v are unmarked, with α_vB =: t_v ∈ {2, 3} by (b).
- gcd(λ_v, λ_v′) = gcd(t_v, t_v′): 2 for (2,2), 3 for (3,3), 1 for (2,3).
- So a coset never holds vertices with t = 2 and t = 3 together. It holds at most two vertices with t = 2, since a triple needs a pair with gcd ≥ 3. It holds at most three with t = 3, since a 4-set needs a pair with gcd ≥ 4.
- A vertex with t = 3 lies in all three remaining cosets. Then no vertex with t = 2 can be placed anywhere, so all four vertices have t = 3, and every coset holds four vertices. Contradiction.
- Otherwise all four have t = 2, needing 8 incidences against a capacity of 3·2 = 6. Contradiction. ∎

## Consequences for the K7 coverage (K7-structure-v1 Theorem K7-COV)

**Block sizes.** In every K7 configuration, every twin block has size 1, 2 or 3. Size 3 requires at least one marked vertex.

**Constraints for a block B of size 3 (only possible with M ≠ ∅):**
- α_vB ≤ 3 for every v ∉ B;
- the outside vertices live in three exclusive cosets of the index-6 subgroup W_B, subject to the F-packing of (c).

So the K7-COV data (ii) shrink to twin partitions with parts of size ≤ 2 when M = ∅, and of size ≤ 3 otherwise.

**When M = ∅** (all seven vertices unmarked): U has seven vertices in blocks of size 1 or 2, and K7-Q5 removes Q5. The families left are:
- Q23: a nested partition, with blocks of size ≤ 2;
- Q24: a 2/4 colouring of the block pairs, with blocks of size ≤ 2.

**Not done here:**
- the case s = 3 with M ≠ ∅;
- blocks of size 2 (L6 allows m ∈ {2, 3, 6});
- no count or enumeration.
