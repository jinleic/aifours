# K7-unmarked-lemmas-v1: with no marked vertex, the family Q23 with at least two 2-classes is impossible

- **Freeze record:** host-clock time and sha256 in `evidence/k7-unmarked-lemmas-v1.sha256`.
- **Labels:** [NEW] means written in this lane; it is not a novelty claim.
- **Status:** unreviewed. No computation was run. K7 stays OPEN: the marked cases, and Q24 with M = ∅, remain.
- **Builds on:**
  - `K7-structure-v1.md` (f4534c07…9fc1): K7-U, K7-TWIN, K7-Q, K7-COV;
  - `K7-block-lemma-v1.md` (93c3cd1f…29db3);
  - `K7-pair-lemma-v1.md` (77ce8b1b…c3d), Corollary P2.
- **Imports (frozen written rules only):**
  - L4 (P, the lower bound via T3 at the apex);
  - L6 (XE);
  - L5 (F), with 2 ≤ |T| ≤ 4, using Sun(2)–Sun(4) inside a subgroup (imports);
  - Corollary VFC-count.
- **Not used:** least-order frames, Sun(7) and FH.

## Lemma K7-HIGH (VFC) [NEW]

Let v ∈ U, and suppose all six neighbours of v are unmarked with α_vj ≥ 3. Then no configuration exists.

*Proof.* Apply VFC at v.
1. **Values of q.** Each neighbour has q_j ≤ 6 − α_vj ≤ 3, and d_j = q_j·n_j/6 = q_j w_j. So gcd(d_j, d_j′) = gcd(q_j, q_j′).
2. **Allowed sets.** Split the neighbours by q ∈ {1, 2, 3} into groups of sizes k_1, k_2, k_3. A pair from different groups, or a pair containing an element with q = 1, has gcd 1. So every allowed set of size ≥ 2 lies inside the q = 2 group or the q = 3 group.
   - q = 2 group: gcd 2, so allowed sets have size ≤ 2.
   - q = 3 group: gcd 3, so allowed sets have size ≤ 3.
3. **A feasible y.**
   - q = 1: y = 1.
   - q = 2: y = 1/2 if k_2 ≥ 2, otherwise 1.
   - q = 3: y = 1/3 if k_3 ≥ 3, otherwise 1/k_3.
4. **The total.** Each group contributes at least (its size)/6 to Σ y_j q_j/6:

| group | contribution |
|---|---|
| q = 1 | k_1/6 |
| q = 2 | k_2/6 if k_2 ≥ 2, and 2/6 if k_2 = 1 |
| q = 3 | k_3/6 if k_3 ≥ 3, and 3/6 if k_3 ∈ {1, 2} |

So the total is at least (k_1 + k_2 + k_3)/6 = 1. This contradicts VFC-count, for every admissible q. ∎

## Lemma K7-CLASS (index-2 subgroup inside a 2-class) [NEW]

Assume M = ∅ and family Q23 **with at least two 2-classes**. By P2 every block is a singleton, so U = V is partitioned into r ≥ 2 classes, with α = 2 inside a class and α = 3 between classes. Then no class has size 2, 3 or 4.

*Proof.*

**Step 1: an index-2 subgroup.** Let C be a class with c := |C| ≥ 2, and fix j, k ∈ C. For any v ∉ C, the triangle (v, j, k) has α_jk = 2 and α_vj = α_vk = 3.
- L4 at apex v: τ_min = lcm(3, 3, 2) = 6, so μ(X_j ∩ X_k) ≥ 6/(6·2) = 3/6 = μX_j = μX_k. Hence U_vU_j = U_vU_k.
- L6 then gives W := ⟨U_j, U_k⟩ with m := [G:W] dividing 6.
- α_jk/6 = 2/6 ≤ 1/m, so m ≤ 3.
- [U_v : U_v ∩ W] = m·3/6 ∈ ℤ, so m is even.
- Hence m = 2, and U_v ⊆ W for every v ∉ C.

**Step 2: the packing data.** Apply L5 with H = W.
- t = 1 for j, for k and for all 7 − c vertices outside C. Each of these lies in a single W-coset, with λ = n/2 = 3w.
- Every other i ∈ C has t_i ∈ {1, 2} and λ_i = 3 t_i w_i.
- The gcds of the λ's are 3, except 6 for two vertices that both have t = 2.
- Sun(4) in W requires every 4 pieces in one coset to contain a pair with gcd ≥ 4. So a W-coset holds at most 3 vertices with t = 1, and at most 6 such vertices fit in total.

**Step 3: case by case.**

**c = 2.** The vertices with t = 1 number 2 + 5 = 7 > 6.

**c = 3, C = {j, k, i}.**
- The vertices with t = 1 number at least 6, so t_i = 2, and the six vertices with t = 1 split 3 + 3 between the two cosets.
- i meets both cosets. Each coset then holds 3 vertices with t = 1 plus i, and these four have all pairwise gcds equal to 3. This contradicts Sun(4).

**c = 4, C = {j, k, i_1, i_2}.**

| subcase | contradiction |
|---|---|
| both t_i = 1 | 7 vertices with t = 1 |
| exactly one t_i = 2 | 6 vertices with t = 1 split 3 + 3, and the vertex with t = 2 joins both cosets; four vertices with gcds 3 |
| both t_i = 2 | Both vertices with t = 2 lie in both cosets. Any 4-subset must contain both of them, otherwise all its gcds are 3. So each coset holds at most 2 vertices with t = 1, leaving room for 4 < 5. ∎ |

## Theorem K7-Q23U [NEW]

If M = ∅, no K7 configuration of family Q23 with at least two 2-classes exists.

*Proof.*
- By P2, every block is a singleton. By K7-CLASS, every class has size 1 or at least 5.
- With r ≥ 2 classes summing to 7, some class is a singleton {o}: a class of size 5 or 6 leaves 2 or 1 vertices, which must form singletons, and if no class has size ≥ 5 then all classes are singletons.
- The vertex o has α = 3 to all six other vertices, all unmarked.
- K7-HIGH at o gives the contradiction. ∎

## Corollaries for M = ∅

**K7-HIGH reproves K7-Q5 for M = ∅**, since every α equals 5.

**In family Q24 with M = ∅**, every vertex has a neighbour with α ≤ 2: a twin, or a block at β = 2.

**Cumulative M = ∅ status.** All of the following are written and unreviewed:

| family | status |
|---|---|
| Q5 | impossible |
| Q23 with at least two 2-classes | impossible |
| Q23 with a single 2-class (all β = 2, including b = 1); assigned to Q23 by K7-structure-erratum-v1 X1 | remains. Twin pairs are excluded by P3's argument (k_4 = 0), so only the seven-singleton all-2 pattern is left. That pattern is not excluded here; VFC at a vertex does not refute every q, e.g. q = (4,4,4,4,4,2). |
| Q24 (at least one β = 4) | remains, with these constraints: blocks of size ≤ 2 (K7-BLOCK); every twin pair has at least three outsiders at β = 4 (P3); every vertex has a neighbour at α ≤ 2 (K7-HIGH) |

**Not covered:** the all-2 pattern on seven singletons and Q24, both with M = ∅; and every case with M ≠ ∅.
