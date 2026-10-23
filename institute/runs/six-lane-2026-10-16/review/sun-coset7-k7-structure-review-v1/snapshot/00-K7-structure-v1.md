# K7-structure-v1: twin blocks, the quotient trichotomy, a written Q5 lemma, and the K7 coverage statement

- **Freeze record:** host-clock time and sha256 in `evidence/k7-structure-v1.sha256`.
- **Labels:** [NEW] means written in this lane; it is not a novelty claim.
- **Status:** nothing here is reviewed. There is no computation: no script was run, and no count or enumeration is claimed. It removes **no** class. K7 stays OPEN. The file only turns the leads of FINITE-COVERAGE-k7-v1 §5 into proved statements with explicit hypotheses, plus one sub-family elimination (Lemma K7-Q5).
- **Imports:** only frozen written rules, read with rules-k7-addendum-v1 and rules-k7-erratum-v1:
  - rules-k7-v1 L0.3, L1 (T), L4 (P, including its K2 barring);
  - L6 (XE), in §6 only;
  - Corollary VFC-count, in Lemma K7-Q5.
- **Correction to my FINITE-COVERAGE §5 lead:** it attributed the 11-type table to "the T and K rules". The cut from 16 to 11 types is made by **Ppair** (L4 with K2), not by K. §2 below states it exactly.

## 0. Setting and notation

**Class K7.** Seven vertices V; every pairwise gcd g_ij = 6. Write n_i = 2^{e_i} 3^{f_i} 5^{g_i} w_i with gcd(w_i, 30) = 1.

**Profiles (README P0–P1).**
- e_i, f_i ≥ 1;
- for i ≠ j: min(e_i,e_j) = 1, min(f_i,f_j) = 1 and min(g_i,g_j) = 0;
- the w_i are pairwise coprime.

**Markers.** Hence at most one vertex has e ≥ 2 (marker 2), at most one has f ≥ 2 (marker 3), and at most one has g ≥ 1 (marker 5). Several markers may sit on one vertex.
- **Marked set M:** the vertices carrying at least one marker; |M| ≤ 3.
- **Unmarked set U = V ∖ M:** every vertex of U has n = 6w, with w coprime to 30. So |U| ≥ 4.

**Excess vector.** ε(v) = (e_v − 1, f_v − 1, g_v). Then ℓ_v = n_v/6 = 2^{ε_2(v)} 3^{ε_3(v)} 5^{ε_5(v)} w_v in every triangle, because γ = 6 throughout.

**The function d.** For 1 ≤ r ≤ 5 put

  d_v(r) := 2^{min(ε_2(v), v_2(r))} · 3^{min(ε_3(v), v_3(r))} · 5^{min(ε_5(v), v_5(r))}.

So d_v ≡ 1 if v ∈ U. If v ∈ M, then d_v(r) > 1 only when r shares one of v's marked primes: r ∈ {2, 4} for marker 2, r = 3 for marker 3, r = 5 for marker 5.

**Edge notation.** In a triangle {x, y, z}, r_x denotes the α of the edge opposite x.

## 1. Lemma K7-TRI (the triangle conditions in K7) [NEW, specialisation of L1 and L4]

For a triangle {x, y, z} in K7, let a ≤ b ≤ c be its three α's in sorted order.

**(T)**
- τ_min = lcm(r_x/d_x(r_x), r_y/d_y(r_y), r_z/d_z(r_z)).
- τ_max = a·b.
- T requires τ_min ≤ a·b.

**(P at apex v)**, with the other two vertices j, k, so that α_vj = r_k, α_vk = r_j and α_jk = r_v:
- u_v = 1/(6·d_v(r_v));
- μX_j = r_k/6 and μX_k = r_j/6;
- Lb = max(τ_min/(6 r_v), (r_j + r_k)/6 − 1, 0);
- lo = u_v⌈Lb/u_v⌉;
- hi = min(r_j, r_k)/6, minus u_v when the containment that equality needs is barred by K2. That containment is X_j ⊆ X_k when r_k < r_j, X_k ⊆ X_j when r_j < r_k, and both when the two are equal. K2 bars X_j ⊆ X_k unless r_k + r_v < 6.
- Ppair kills the pattern if lo > hi at some apex.

*Proof.*
1. **Triangle quantities.** In K7, γ_y = lcm(6,6) = 6 and g = 6 on every edge.
2. **τ_max.** L1 gives τ_max = min over apexes y of ⌊6·α_xz·min(α_xy, α_yz)/6⌋. Each apex contributes (opposite α)·(the smaller adjacent α). These are c·a, b·a and a·b, so the minimum is ab.
3. **τ_min.** The τ_min term of the edge opposite v is r_v/gcd(r_v, ℓ_v). Since r_v ≤ 5 is coprime to w_v, gcd(r_v, ℓ_v) = d_v(r_v).
4. **u.** L4 gives u_vjk = 1/gcd(n_v, I_jk) with I_jk = lcm(n_j, n_k)·α_jk. For p = 2, v_p(gcd) = min(1 + ε_2(v), max(v_2 n_j, v_2 n_k) + v_2(r_v)).
   - If v carries marker 2, then j and k have e = 1, and this equals 1 + min(ε_2(v), v_2 r_v).
   - Otherwise both expressions equal 1.
   - The same holds for p = 3. For p = 5 it equals min(ε_5(v), v_5 r_v).
   - The w-parts contribute nothing.
   - Hence gcd(n_v, I_jk) = 6·d_v(r_v).
5. **Lb, lo, hi and K2.** These follow verbatim from L4 and rules-k7-addendum-v1 (F6), with g = 6 and γ = 6. Since d_v(r_v) is an integer, min(r_j, r_k)/6 is a multiple of u_v, so the floor in hi is exact. ∎

## 2. Lemma K7-U (the table for all-unmarked triangles) [NEW]

If x, y, z ∈ U, then d ≡ 1 and u = 1/6. After T and Ppair, the sorted type (a, b, c) of {x, y, z} is one of these **11 types**:

  (1,1,1), (1,2,2), (1,3,3), (1,4,4), (2,2,2), (2,2,4), (2,3,3), (2,4,4), (3,3,3), (4,4,4), (5,5,5).

*Proof.*

**T leaves 16 types.** T requires lcm(a,b,c) ≤ ab. Going case by case on a:

| a | admissible (b, c) | types |
|---|---|---|
| 1 | lcm(b, c) ≤ b forces c = b | (1, b, b), b = 1..5 |
| 2 | b = 2 needs lcm(2,c) ≤ 4, so c ∈ {2,4}; b = 3 needs lcm(6,c) ≤ 6, so c = 3; b = 4 needs c = 4; b = 5 needs c = 5 | (2,2,2), (2,2,4), (2,3,3), (2,4,4), (2,5,5) |
| 3 | — | (3,3,3), (3,4,4), (3,5,5) |
| 4 | — | (4,4,4), (4,5,5) |
| 5 | — | (5,5,5) |

The other 19 of the 35 multisets fail T.

**Ppair kills 5 more.** In each of the following, take the apex v whose adjacent α's are p < q and whose opposite α is r = q, with τ_min = lcm(p, q, q). The containment that equality needs is X_j ⊆ X_k, and K2 bars it because p + q ≥ 6. So hi = (p − 1)/6, while lo ≥ τ_min/(6q):

| type | τ_min | lo | hi | killed |
|---|---|---|---|---|
| (1,5,5) | 5 | 1/6 | 0 | yes |
| (2,5,5) | 10 | 2/6 | 1/6 | yes |
| (3,4,4) | 12 | 3/6 | 2/6 | yes |
| (3,5,5) | 15 | 3/6 | 2/6 | yes |
| (4,5,5) | 20 | 4/6 | 3/6 | yes |

**The remaining 11 pass both rules.** I checked T and Ppair by hand at all three apexes of each; the computation is short. Passing T and Ppair is not a claim that these types are realisable or that they survive the other rules. ∎

## 3. Lemma K7-TWIN (twin blocks) [NEW]

**Definition.** x ~ y for x, y ∈ U means x = y or α_xy = 1.

**(a)** ~ is an equivalence relation on U. Its classes are the **twin blocks**.

**(b)** If x ~ y with x ≠ y, then α_xz = α_yz for **every** z ∈ V ∖ {x, y}, marked or unmarked.

**(c)** If x ~ y with x ≠ y, then α_xz ≠ 5 for every z.

**(d)** If x ~ y with x ≠ y, then U_zU_x = U_zU_y for every z ∈ V ∖ {x, y}.

*Proof.*

**(b) and (a).** Take a triangle {x, y, z} with α_xy = 1.
- The edge xy contributes 1/d_z(1) = 1 to τ_min.
- The edges xz and yz are opposite the unmarked vertices y and x, so they contribute α_xz and α_yz.
- So τ_min = lcm(α_xz, α_yz). The sorted type is (1, b, c) with b = min(α_xz, α_yz), so τ_max = b.
- T gives lcm(α_xz, α_yz) ≤ min(α_xz, α_yz), hence α_xz = α_yz. This is (b).
- For (a): with α_xy = α_yz = 1 and z ∈ U, (b) gives α_xz = α_yz = 1. So ~ is transitive. Reflexivity and symmetry are clear.

**(c).** Suppose α_xz = α_yz = 5. Take the apex x (u_x = 1/6), with j = y and k = z:
- μX_y = 1/6 < μX_z = 5/6, and τ_min = lcm(1, 5, 5) = 5;
- Lb ≥ 5/(6·5) = 1/6, so lo = 1/6;
- equality needs X_y ⊆ X_z, which K2 bars because α_xy + α_zy = 6. So hi = 0 < lo.
- Ppair kills this for every marking of z.

**(d).** Take the apex z, with j = x and k = y. By (b), μX_x = μX_y = b/6 with b = α_zx.
- τ_min = lcm(b, b, 1/d_z(1)) = b, so Lb ≥ τ_min/(6·1) = b/6.
- L4 gives μ(X_x ∩ X_y) ≥ b/6 = μX_x = μX_y. These are finite sets, so X_x = X_y. ∎

**Consequences.**
- α between two distinct blocks B and B′ is well defined (β(B, B′) := α_xy for x ∈ B, y ∈ B′), and β ∈ {2,3,4,5}.
- For z ∈ M, a_{zB} := α_zx (x ∈ B) is well defined, and a_{zB} ∈ {1,2,3,4} whenever |B| ≥ 2.

## 4. Lemma K7-Q (the quotient trichotomy) [NEW]

Let B_1, …, B_b be the twin blocks of U. Exactly one of the following holds.

- **(Q5)** Every block is a singleton (b = |U|), and every β equals 5.
- **(Q23)** Every β lies in {2,3}, and "β = 2" is an equivalence relation on the blocks. So U carries a two-level nested partition: twin blocks inside **2-classes**, with α = 1 within a block, 2 between blocks of the same 2-class, and 3 between 2-classes.
- **(Q24)** Every β lies in {2,4}. The triangle tables put no further condition on the 2/4 colouring of the block pairs.

The degenerate cases b = 1 (all of U one block) and "all β = 2" fall under both Q23 and Q24. A coverage enumeration may assign them to either family, provided it treats them exactly once.

*Proof.* Triangles on three distinct blocks have every α ≥ 2. By K7-U their types lie in

  {(2,2,2), (2,2,4), (2,3,3), (2,4,4), (3,3,3), (4,4,4), (5,5,5)}.

**A 5 forces Q5.** Suppose β(s, t) = 5.
- By K7-TWIN(c), B_s and B_t are singletons.
- For every other block u, the triangle (s, t, u) must be (5,5,5).
- For blocks u, u′ ∉ {s}, the triangle (s, u, u′) then has two 5's, so β(u, u′) = 5.
- So every β = 5, and by TWIN(c) every block is a singleton.

**3 and 4 never coexist.** Suppose β(s, t) = 3 and β(x, y) = 4.
- A triangle containing a 3 is (2,3,3) or (3,3,3), so s and t have no 4-edges. In particular x, y ∉ {s, t}.
- The triangle (s, x, y) contains a 4 and its other two values lie in {2,3}. A type containing a 4 is (2,2,4), (2,4,4) or (4,4,4), so β(s,x) = β(s,y) = 2. Likewise β(t,x) = 2.
- Then (s, t, x) has type (2,2,3), which T excludes. Contradiction.

**Q23.** With only 2's and 3's, the type (2,2,3) is excluded, so β = 2 is transitive.

**Q24.** With only 2's and 4's, all four types (2,2,2), (2,2,4), (2,4,4) and (4,4,4) are allowed. ∎

## 5. Lemma K7-Q5 (a written elimination of a sub-family) [NEW]

**Claim.** A K7 configuration of type Q5 has |U| = 4, that is, exactly three marked vertices. Every Q5 configuration with |U| ≥ 5 is impossible.

*Proof.* Let v ∈ U and apply Corollary VFC-count at v.

1. **Unmarked neighbours.** For each of the |U| − 1 unmarked neighbours j, α_vj = 5, so q_j ≤ 6 − 5 = 1. Hence q_j = 1 and d_j = q_j·n_j/6 = w_j.
2. **Marked neighbours.** For z ∈ M, d_z = q_z·n_z/6 = q_z·m_z·w_z with m_z := 2^{ε_2}3^{ε_3}5^{ε_5} of z. The m_z of distinct marked vertices are pairwise coprime, because each marker sits on one vertex.
3. **Unmarked neighbours stand alone.** w_j is coprime to 30, to every q ≤ 5 and to every other w. So gcd(d_j, d_x) = 1 for every other neighbour x, and no allowed set contains j together with another vertex.
4. **The weights.** Put y_j = 1 on each unmarked neighbour. This contributes (|U| − 1)/6 to Σ y q/6.

The cases:

| \|U\| | \|M\| | argument | total |
|---|---|---|---|
| 7 | 0 | unmarked neighbours alone | 6/6 = 1 |
| 6 | 1 | add y_z = 1 for the marked z | 5/6 + q_z/6 ≥ 1 |
| 5 | 2 | see below | ≥ 4/6 + 2/6 = 1 |

For |U| = 5, with marked vertices z and z′:
- If {z, z′} is not allowed, put y_z = y_z′ = 1.
- If it is allowed, then gcd(d_z, d_z′) ≥ 2 forces max(q_z, q_z′) ≥ 2, since q_z = q_z′ = 1 gives gcd(m_z w_z, m_z′ w_z′) = 1. Put weight 1 on the larger q.

In every case some feasible y has Σ y_j q_j/6 ≥ 1, contradicting VFC-count. This holds for every admissible q-vector at v. ∎

**Not covered.** For |U| = 4 the same bound can fall below 1, for example when the marked q-vector is (2,2,1) with the q = 1 vertex carrying marker 2. Q5 with |U| = 4 therefore stays in the coverage family below.

## 6. Theorem K7-COV (the coverage statement for a reduced representation) [NEW]

**(i) Reduced data.** Every K7 pattern (profiles and α) that passes T and Ppair on all triangles of U, and on all triangles with two vertices in one twin block, is determined by:
1. **Marking data:** M (|M| ≤ 3), with the capped profiles of its vertices. Each marker 2/3/5 sits on at most one vertex, the capped excesses are ε_2 ∈ {0..3}, ε_3 ∈ {0,1} and ε_5 ∈ {0,1,2}, and every pairwise gcd is 6.
2. **The twin partition** of U (|U| = 7 − |M| ≥ 4).
3. **Quotient data**, one of:
   - Q5 (all blocks singletons, every β = 5). K7-Q5, which uses VFC at an unmarked vertex, allows this only when |U| = 4;
   - Q23 (a partition of the blocks into 2-classes);
   - Q24 (a 2/4 colouring of the block pairs).
4. **Marked rows:** a_{zB} ∈ {1,…,5} for z ∈ M and each block B, with a_{zB} ≤ 4 when |B| ≥ 2.
5. **α among the marked vertices.**

**(ii) Lifting.** The data of (i) determine the full α-matrix by α_xy = 1 within blocks, β between blocks, and a_{zB} towards marked z. Each data set lifts to exactly one pattern up to Sym(U).

**(iii) Symmetry.**
- The profile stabiliser is Sym(U) × {id_M}. All unmarked vertices have the profile (1,1,0), and distinct marked vertices have distinct marker sets, hence distinct profiles.
- A permutation of U maps twin blocks to twin blocks of the same size, and transforms the quotient data and the marked rows accordingly. Two data sets give the same pattern orbit iff some size-preserving bijection of the blocks carries one data set onto the other: quotient data, marked rows, and the same marked–marked α's.

**(iv) Soundness obligation.** The reduction removes nothing that T and Ppair keep. Every rule (T, K, VFC, P, RPLP) must still be applied to the **lifted 7-vertex pattern**, including every triangle and star that contains marked vertices, using the d-relaxed conditions of K7-TRI. No rule may be evaluated on the quotient alone.

**(v) Completeness up to symmetry.** Enumerate the data of (i), one representative per orbit of (iii), and evaluate every rule on the lift. This covers every K7 configuration in every group: the pattern of any configuration passes T, Ppair and VFC, so it is one of these lifts.

*Proof.*
- (i) and (ii) follow from K7-TWIN (a)–(c), K7-Q and K7-Q5.
- (iii): the stabiliser is the stabiliser of the profile tuple; the CAP hypotheses hold by README P0–P1.
- (iv) and (v): the pattern of any configuration passes T and Ppair, so (i) and (ii) apply to it. It also passes VFC, so K7-Q5 applies to it, and it is one of the lifts. Rules are evaluated on actual patterns. ∎

**Marked-vertex relaxation (exact form).** In a triangle containing z ∈ M:
- only the edge opposite z can have its τ_min term reduced, namely to r_z/d_z(r_z);
- at the apex z the P-grid refines to 1/(6·d_z(r_z));
- triangles with two marked vertices z, z′ reduce at most the two edges opposite them.

**Example of the relaxation.** Let z carry marker 2 with ε_2(z) = 1, and let x, y be unmarked vertices in different blocks with α_xy = 4, α_zx = 1 and α_zy = 2.
- T: τ_min = lcm(4/d_z(4), 1, 2) = lcm(2, 1, 2) = 2 ≤ τ_max = 1·2.
- Ppair passes at all three apexes. I checked this by hand: at the apex z the grid is 1/12, with lo = 1/12 and hi = 1/6.

For an all-unmarked triangle the type (1,2,4) fails T. So α = 1 between a marked and an unmarked vertex does not force equal rows; TWIN(b) holds only for unmarked twins.

## 7. Structural leads (proved facts, not used for any kill; FH remains UNUSED)

**Twins generate a subgroup.** By K7-TWIN(d) and L6, twins j ~ k satisfy:
- W := ⟨U_j, U_k⟩ ≠ G, with m = [G:W] dividing 6;
- [U_v : U_v ∩ W] = m·α_vj/6 ∈ ℤ for all v ∉ {j, k}.

So:
- m = 2 forces α_vj = 3 for every v outside the pair;
- m = 3 forces α_vj ∈ {2, 4};
- m = 6 gives U_jU_k = W, a subgroup of index 6, since μ(U_jU_k) = 1/6.

In a block of size ≥ 3, a third twin v has α_vj = 1, which forces m = 6. Then all pairs of the block give the same W_B ⊇ U_j for j ∈ B, and the block's cosets lie in pairwise distinct cosets of W_B.

These facts are inputs for a future fibre (FH) argument with H = W_B of index 6. Under rules-k7-addendum-v1 §A4 such an argument needs frozen L6 data, the admissible m, the fibre domains and the least-order scope before any use.

## 8. What remains, exactly

- **K7 is OPEN.** Q5 with |U| ≥ 5 is eliminated in writing (K7-Q5, unreviewed). The rest of K7 lies in the families of K7-COV (Q23, Q24, Q5 with |U| = 4, with marked rows), and the lift must be checked against every rule.
- **No representation, enumeration, count or computation is claimed or authorised here.** The size of the reduced family is not computed.
- **Q24 does not reduce K7 to a binary graph alone.** The binary quotient graph (Q24) and the nested partition (Q23) replace the 5^21 raw α-labels only on U. The marked rows and the α's among marked vertices are still free inside the relaxed tables.
