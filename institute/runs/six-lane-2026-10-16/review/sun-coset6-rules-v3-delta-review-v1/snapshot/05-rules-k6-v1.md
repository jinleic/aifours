# rules-k6-v1: lemmas for the Core5(6) pattern engine

The host-clock freeze record is in `evidence/freeze-v1.sha256`. Corrections go only into new versions.

**Reading conventions.**
- "[NEW]" means only "written in this lane"; it is not a novelty claim.
- **[GEN]** marks lemmas proved for arbitrary indices n_i in sun-coset5 `rules-v1.md` (cb86c168…390f), together with its cumulative erratum `rules-v1-erratum-v3.md`. Their proofs do not depend on the index form. They are restated below with explicit hypotheses and specialised to Core5(6).

## 0. Setting

**Harmonic configuration.** G is finite. U_1, …, U_k ≤ G have indices n_i = [G:U_i]. The cosets g_1U_1, …, g_kU_k are **pairwise disjoint**.

**Pairwise data.** For i ≠ j:
- g_ij = gcd(n_i, n_j);
- I_ij = [G:U_i∩U_j];
- α_ij = I_ij / lcm(n_i, n_j).

**Core5(6).** k = 6 and n_i = 5r_i, where the r_i are pairwise coprime. Then:
- g_ij = 5, lcm(n_i, n_j) = 5r_ir_j and I_ij = 5r_ir_jα_ij.
- **Special vertices:**
  - E2 is the vertex with r even, if any. Its class is c2 = 1 if v₂(r_E2) = 1, and c2 = 2 if v₂(r_E2) ≥ 2.
  - E3 is the vertex with 3 | r, if any.
  - E5 is the vertex with 5 | r, if any.
  - Any two of these may coincide.

**Inputs from the minimal counterexample frame** (README §2):
- Sun(k) for k ≤ 4 holds in every group, by Zhu Theorem 1.1 and L0.6.
- Sun(5) holds in every group, by sun-coset5 proof-v4. This is a stated dependence.
- Sun(6) holds in every proper subgroup of the minimal G.

## L0. Basic facts [GEN; rules-v1 L0]

- **L0.1** Product formula: |XY| = |X||Y| / |X∩Y|.
- **L0.2** gU ∩ hV = ∅ if and only if g⁻¹h ∉ UV.
- **L0.3** |U_iU_j| = α_ij|G| / g_ij and 1 ≤ α_ij ≤ g_ij − 1. In Core5(6): α_ij ∈ {1, 2, 3, 4} and |U_iU_j| = α_ij|G|/5.
  - *Proof.* L0.1 gives |U_iU_j| = |G| I_ij / (n_i n_j) = α_ij|G| / g_ij. Disjointness and L0.2 give U_iU_j ≠ G.
- **L0.4** Every double coset AxB has size a multiple of |G| / gcd([G:A], [G:B]).
- **L0.5** AB ∩ AC is a union of (A, B∩C)-double cosets.
- **L0.6** If [G:A] and [G:B] are coprime, then AB = G, so every left coset of A meets every left coset of B. This is Sun's statement at k = 2.

## L1. Triangle lemma T [GEN; rules-v1 L1]

For distinct a, b, c put L = lcm(n_a, n_b, n_c) and T = [G : U_a∩U_b∩U_c]. Then L | T, and τ = T/L satisfies:

- **(T1)** I_xy | Lτ for every pair {x, y}.
- **(T3)** |U_y(U_x∩U_z)| = |G| L τ / (n_y I_xz).
- **(T2)** |U_y(U_x∩U_z)| ≤ min(|U_yU_x|, |U_yU_z|).

**Core5(6) form.**
- L = 5r_ar_br_c, because the r's are pairwise coprime.
- (T1) is equivalent to α_xy | r_zτ.
- (T3) reads |U_y(U_x∩U_z)| = τ|G| / (5α_xz).
- (T2) is equivalent to τ ≤ α_xyα_xz and τ ≤ α_yzα_xz.
- So τ_max is the smallest, over the three vertices, of the product of the two α's at that vertex.
- τ_min is the lcm over the three edges of α_e / gcd(α_e, r_opp), where r_opp is the r of the vertex opposite the edge. The table below lists gcd(α, r_z) by E2/E3 status alone; a prime p ≥ 5 never divides α ≤ 4.

| α | gcd(α, r_z) |
|---|---|
| 1 | 1 |
| 2 | 2 if z = E2, else 1 |
| 3 | 3 if z = E3, else 1 |
| 4 | 4 if z = E2 with c2 = 2; 2 if z = E2 with c2 = 1; else 1 |

The admissible τ are exactly the multiples of τ_min that are ≤ τ_max.

**T-kill.** If τ_min > τ_max, no configuration has these data. T-kills are **triangle-local**: whether a triangle is forbidden depends only on its three α's and on the E2-class and E3 status of its three vertices.

## L2. Links [GEN; rules-v1 L2]

If |U_y(U_x∩U_z)| = |U_yU_x|, then U_yU_x ⊆ U_yU_z and U_xU_y ⊆ U_zU_y.

In Core5(6) the hypothesis holds exactly when τ = α_xyα_xz.

## L3. Lemma K [GEN; rules-v1 L3]

**Statement.** Let v be a vertex and S a set of other vertices such that, for every pair {i, j} ⊆ S, U_vU_i ⊆ U_jU_i or U_vU_j ⊆ U_iU_j. Then Σ_{i∈S} |U_iU_v| ≤ |G| − |U_v|. In Core5(6) this reads Σ_{i∈S} α_iv ≤ 4.

**Proof.**
1. The sets g_iU_iU_v (i ∈ S) are pairwise disjoint, by L0.2.
2. Each of them is right U_v-invariant and misses g_vU_v.
3. Adding their sizes gives the bound.

**K1.** The pair condition at v holds for {i, j} when |U_i(U_v∩U_j)| = |U_iU_v| (L2 with apex i), or when |U_j(U_v∩U_i)| = |U_jU_v|. In Core5(6) this is τ_ivj = α_ivα_vj.

**K2.** If U_vU_j ⊆ U_vU_k, then α_vj + α_kj ≤ 4. This is L3 applied at j with S = {v, k}, using the inverse U_jU_v ⊆ U_kU_v.

## L4. Vertex count P [GEN; rules-v1 L4]

Fix a vertex v. For each other vertex j put X_j = U_vU_j and Y_j = G ∖ X_j.

- **(P1)** |X_j| = α_vj/5, and U_v ⊆ X_j.
- **(P2)** |X_j ∩ X_k| is a multiple of u = 1/gcd(n_v, I_jk). In Core5(6), u = 1/(5·gcd(r_v, α_jk)), with the gcd read from the table in L1.
- **(P3)** |X_j ∩ X_k| ≥ max(τ_vjk/(5α_jk), |X_j| + |X_k| − 1).
- **(P4)** If X_j ⊆ X_k, then K2 holds.
- **(P5)** For every set S of other vertices: Σ_{j∈S} |Y_j| − Σ_{j<k in S} |Y_j ∩ Y_k| < 1, with |Y_j ∩ Y_k| = 1 − |X_j| − |X_k| + |X_j ∩ X_k|.

**How the engine applies P.** All sizes are in units of |G|.
- hi_jk is the largest multiple of u that is ≤ min(|X_j|, |X_k|). It is lowered by one unit u if equality would force a containment that K2 forbids. If |X_j| = |X_k|, equality forces equality of the two sets, so both K2 conditions must hold.
- lo_jk is the bound in (P3), rounded up to a multiple of u.
- **P-pair kill:** lo_jk > hi_jk.
- **PB kill:** (P5) fails when every intersection is set to its hi value.

## L5. Fibre lemma F [GEN; rules-v1 L6], with k = 6 inputs

Let H ≤ G with [G:H] = m. For each l put t_l = [U_l : U_l∩H] and λ_l = [H : U_l∩H] = n_l t_l / m.

- **(F1)** g_lU_l meets exactly t_l left cosets of H, and 1 ≤ t_l ≤ m. Also t_l = 1 if and only if U_l ⊆ H.
- **(F2)** Fix a left coset C of H. The vertices whose cosets meet C give pairwise disjoint left cosets in H of the subgroups U_l∩H. So if s ≥ 2 of them meet C, some pair has gcd(λ_l, λ_l') ≥ s. The input used depends on s:
  - s ≤ 4: Zhu's theorem, or L0.6 when s = 2;
  - s = 5: Sun(5), a stated dependence;
  - s = 6: minimality, since H is proper.
- **(F3)** If U_i ⊆ H, then |U_iU_l| ≤ |HU_l| = t_l|G|/m. In Core5(6) with m = 5, this reads α_il ≤ t_l.

Proofs as in rules-v1 L6.

## L6. H5: index-5 subgroups from α = 1 edges [NEW]

**Statement.** In Core5(6), suppose α_ab = 1 and V := {v ∉ {a, b} : α_va = α_vb} ≠ ∅. Then:
- H := U_aU_b is a subgroup of index 5;
- U_a ⊆ H and U_b ⊆ H;
- for every v ∈ V, t_v = [U_v : U_v∩H] = α_va. In particular U_v ⊆ H when α_va = 1.

This covers M-S Lemma 3.7 with a = 5, which is the case α_va = 1.

**Proof.** Fix v ∈ V and put c = α_va = α_vb ∈ {1, 2, 3, 4}. Work in the triangle {v, a, b}.
1. **The bound τ ≤ c.** The vertex products are c at a, c at b and c² at v, so (T2) gives τ ≤ c.
2. **c divides τ.** Suppose c ≥ 2. By (T1), c | r_b τ and c | r_a τ, using the edges va and vb.
   - If c is prime (2 or 3): r_a and r_b are coprime, so c fails to divide at least one of them. Hence c | τ.
   - If c = 4: one of r_a, r_b is odd, and that one forces 4 | τ.
   - So τ = c. For c = 1 the bound already gives τ = 1.
3. **U_vU_a = U_vU_b.** By (T3) with apex v, |U_v(U_a∩U_b)| = τ/(5α_ab) = c/5 = |U_vU_a| = |U_vU_b|. Since U_v(U_a∩U_b) lies inside both, U_vU_a = U_v(U_a∩U_b) = U_vU_b. Call this set X.
4. **X = U_vW for W = ⟨U_a, U_b⟩.** X is right-invariant under U_a and under U_b, hence under W. So U_vW ⊆ X ⊆ U_vW.
5. **W has index 5.** |X| = c/5 < 1, so W ≠ G. Also [G:W] divides gcd(5r_a, 5r_b) = 5, since U_a ≤ W. Hence [G:W] = 5.
6. **W = U_aU_b.** U_aU_b ⊆ W and |U_aU_b| = 1/5 = |W|.
7. **t_v = c.** |U_vW| = t_v|W| = t_v/5, and |U_vW| = |X| = c/5.

W does not depend on v. ∎

## L7. Lemma R in LP form [NEW]

**Setting.** A harmonic configuration (pairwise disjoint cosets). Fix a vertex v and translate so that g_v = 1. For j ≠ v put D_j = U_vg_jU_j and d_j = |D_j|/|U_j|.

**The fibre facts (R1)–(R5′).** These are proved in sun-coset5 proof-v4 §5; the proofs use only disjointness and L0.
- **(R1)** D_j ∩ U_vU_j = ∅.
- **(R2)** |D_j| is a positive multiple of |G|/gcd(n_v, n_j).
- **(R3)** Every right coset U_vy ⊆ D_j meets g_jU_j, in a right coset of a subgroup of U_v of index d_j.
- **(R5′)** If D_j ∩ D_k ≠ ∅, then gcd(d_j, d_k) ≥ 2.

**A strengthening (R4′).** Let C be a right U_v-coset and S_C = {j : C ⊆ D_j}. If |S_C| = s ≥ 2, then:
- every pair in S_C has gcd ≥ 2;
- some pair in S_C has gcd ≥ s.

*Proof of (R4′).* The pieces in C, right-translated into U_v and then inverted, are pairwise disjoint left cosets in U_v. Apply Sun(s) in U_v (s ≤ 5, using the inputs of §0) to all of them. For the "every pair" part, apply L0.6 to each pair.

**Core5(6) form.**
- |D_j| = q_j|G|/5 with 1 ≤ q_j ≤ 5 − α_vj, so d_j = q_jr_j.
- The common primes of d_j and d_k lie in {2, 3}: q ≤ 4, and no two r's share a prime. In particular E5 is irrelevant here.

**LP statement.**
- **Measure.** For each non-empty S, let μ(S) be the total size of the right U_v-cosets C with S_C = S.
- **Coverage.** Σ_{S∋j} μ(S) = |D_j| = q_j/5.
- **Total.** Σ_S μ(S) ≤ 1 − |U_v| < 1. Here U_v·1 lies in no D_j, by (R1).
- **Support.** μ(S) > 0 only for **allowed** S: either |S| = 1, or every pair in S has maxgcd ≥ 2 and some pair has maxgcd ≥ |S|. "maxgcd" is the largest value of gcd(q_jr_j, q_kr_k) over all r with the given special statuses.
- **Lower bound.** Let LPmin(q) be the minimum of Σ_S μ(S) over μ ≥ 0 on allowed S with Σ_{S∋j} μ(S) ≥ q_j/5. This relaxes the true coverage equalities, so LPmin(q) is at most the true total.

**RLP kill.** If LPmin(q) ≥ 1 for every admissible vector q, i.e. every q with 1 ≤ q_j ≤ 5 − α_vj, then vertex v is impossible.

**Evaluation of LPmin.** By LP duality,
  LPmin = max Σ_j (q_j/5) y_j subject to Σ_{j∈S} y_j ≤ 1 for every maximal allowed S, and y ≥ 0.
- Maximal sets suffice: every non-maximal allowed set lies inside an allowed superset, and y ≥ 0 makes its constraint redundant.
- The engine solves this packing LP by exact rational simplex with Bland's rule.

**Soundness of maxgcd.** Using maxgcd only enlarges the allowed family, which lowers LPmin. Hence a kill computed with maxgcd is a kill for every instance.

## L8. Evaluation points, representatives and E5 [NEW]

**(M1) τ_min suffices.** Every admissible τ is a multiple of τ_min. The rules T, K, P and RLP are upward closed in τ:
- a K1 link at τ_min forces τ = τ_min;
- the (P3) lower bounds increase with τ;
- RLP and F do not read τ.

So a kill at τ_min is a kill for every admissible τ.

**(M2) Representatives suffice.** A pattern quantifies over all pairwise coprime r with given statuses: the E2 vertex and its class, the E3 vertex, and the E5 vertex.
- **How r enters each rule.** T, K, P and the support of RLP depend on r only through these statuses. For E2 the class matters for α = 4, and for maxgcd the 2-adic part of q_jr_j is v₂(q_j) + v₂(r_j). In the RLP maxgcd, E2 of class 2 contributes an unbounded v₂.
- **F rules.** gcd(λ_l, λ_l') involves only the primes 2, 3 and 5:
  - t ≤ 5 and m = 5, and the r's are coprime;
  - a class-1 E2 contributes v₂ = 1 exactly;
  - class-2 E2, E3 and E5 contribute exponents larger than any t-part. The representative exponents 2⁴, 3⁴ and 5⁴ dominate.
  - Because the kill condition is monotone in the gcds, a kill at the representative is a kill for every instance.

**E5.** E5 affects only the F rules: no α and no q is divisible by 5, and only one r is divisible by 5. **Every F certificate must refute every E5 placement, including "no E5".** The engine checks all seven placements.

## Certificates and the order of rules

**Enumeration.**
- There are 8 special-placement types up to S6.
- For each type, backtracking runs over the 15 edges, with α ∈ {1, 2, 3, 4}.
- A partial labelling is pruned as soon as a completed triangle is T-forbidden. Its certificate is the triangle-local record: the vertices, the three α's and the statuses.
- Every complete T-consistent labelling (a "leaf") is tested in this order: K, RLP, P (P-pair, then PB), FH5.

**FH5.**
- For each 1-edge (a, b) with V ≠ ∅, use H5 with m = 5.
- Vertices fixed inside H: a, b and every v ∈ V with α_va = 1.
- Forced values: t_v = α_va for the other v ∈ V.
- Free vertices: t_l ranges over 1..5. Every met-coset set M_l with |M_l| = t_l is enumerated, and a's coset is fixed to label 0.
- An assignment is rejected iff (F3) fails at a vertex with t = 1, or (F2) fails in some coset.
- The certificate requires every assignment to be rejected for **every** E5 placement.

**Output.**
- Each leaf yields one certificate or the label SURVIVE.
- Leaves are deduplicated into orbits by a canonical form under the stabiliser of the special placement.
- **Controls** record observations only and do not gate the run. They are:
  - **Core(5) and Core_3(4) reruns.** The same enumerator and the same code paths for T, K, P and RLP are run with the constants changed to (d = 4, k = 5) for Core(5) and (d = 3, k = 4) for Core_3(4). FH5 is omitted, because H5 is specific to the prime index 5.
    - Core(5): the canonical orbit count must be 21,150. Every orbit these rules leave must be one of the orbits that sun-coset5 engine-v1 killed with N2 or FH2, or the orbit S-D. Any other orbit would mean a rule is unsound.
    - Core_3(4) (= M-S Prop 4.3): the expectation is that every orbit is killed.
  - Realisable configurations survive.
  - Selected mutations break their certificates.
