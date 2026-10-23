# Rules v1: lemmas used by the Core(5) pattern engine

Lane: `mathematics/evidence/six-lane-20261016/sun-coset5`. Created 2026-10-18 at about 09:35 PDT (host clock), then frozen read-only. Corrections go in a new version only.

Status of each item:
- **[PUB]**: published, cited exactly.
- **[PUB+]**: published, with a gap or misprint that is corrected here, and the correction is proved.
- **[NEW]**: new in this lane. The proof is written out and has **not been reviewed** by the parent or by a hostile reviewer.

Notation for the primary sources:
- **M-S** is Margolis–Schnabel, arXiv:1803.03569v1 (`sources/arxiv-1803.03569v1.pdf`). The journal version is Beitr. Algebra Geom. 60 (2019) 399–418.
- **Zhu** is arXiv:0807.2207v1 (`sources/arxiv-0807.2207v1.pdf`), Int. J. Mod. Math. 3 (2008) 197–206.
- **Sun** is arXiv:math/0501451v4 (`sources/arxiv-math0501451v4.pdf`), Internat. J. Math. 17 (2006) 1047–1064.
- **Menon** is arXiv:2608.15873v1 (`sources/arxiv-2608.15873v1.pdf`).

## 0. Setting and notation

**Harmonic configuration.** G is a finite group. U_1, ..., U_k ≤ G are subgroups with n_i = [G:U_i], and g_1, ..., g_k ∈ G are elements such that the cosets g_iU_i are pairwise disjoint. Finiteness of G is justified by R0 in the README.

**Pairwise data.** For each pair i ≠ j put
- g_ij = gcd(n_i, n_j);
- I_ij = [G : U_i ∩ U_j];
- α_ij = I_ij / lcm(n_i, n_j). This is an integer, because n_i and n_j both divide I_ij.

**The Core(5) setting.**
- k = 5 and n_i = 4 r_i, where the r_i are pairwise coprime positive integers.
- E2 is the unique vertex with r_i even, if there is one. E3 is the unique vertex with 3 | r_i, if there is one. E2 = E3 is allowed.
- Consequently g_ij = 4, lcm(n_i, n_j) = 4 r_i r_j and I_ij = 4 r_i r_j α_ij.

**Minimal counterexample (used in F2).** Suppose Core(5) fails. Fix a counterexample in a group G of minimal order among all finite groups that contain five pairwise disjoint cosets of subgroups whose pairwise index-gcds are all ≤ 4. Then every proper subgroup of G satisfies Sun's statement for k = 5.

## L0. Basic facts

**L0.1 [standard] Product formula.** For subgroups X, Y: |XY| = |X||Y| / |X ∩ Y|.

**L0.2 [PUB, M-S Lemma 3.2(3)].** gU ∩ hV = ∅ if and only if g⁻¹h ∉ UV.

*Proof.* gu = hv holds if and only if g⁻¹h = u v⁻¹ ∈ UV.

**L0.3.** In a harmonic configuration, |U_iU_j| = α_ij |G| / g_ij and 1 ≤ α_ij ≤ g_ij − 1. In Core(5) this reads α_ij ∈ {1, 2, 3} and |U_iU_j| = α_ij |G| / 4.

*Proof.*
- By L0.1, |U_iU_j| = |G| I_ij / (n_i n_j) = |G| lcm(n_i, n_j) α_ij / (n_i n_j) = α_ij |G| / g_ij.
- By L0.2 and disjointness, g_i⁻¹g_j ∉ U_iU_j. So U_iU_j ≠ G, which gives α_ij < g_ij.

**L0.4 [PUB, M-S Lemma 3.4(1)].** For subgroups A, B and any x ∈ G, |AxB| is a multiple of |G| / gcd([G:A], [G:B]).

*Proof.*
- |AxB| = |A||B| / |A ∩ xBx⁻¹| = |G| [G : A ∩ xBx⁻¹] / ([G:A][G:B]).
- [G : A ∩ xBx⁻¹] is a multiple of lcm([G:A], [G:B]).
- Substituting gives |AxB| = (integer) · |G| / gcd([G:A], [G:B]).

**L0.5 [PUB, mirror of M-S Lemma 3.4(2)].** For subgroups A, B, C, the set AB ∩ AC is a union of (A, B∩C)-double cosets.

*Proof.* Let x = ab = a'c, with y ∈ A and w ∈ B∩C. Then yxw = (ya)(bw) = (ya')(cw), which lies in AB ∩ AC.

**L0.6 [PUB, Sun 2006 Lemma 2.1 / M-S Lemma 2.2].** If [G:A] and [G:B] are coprime, then AB = G, so every left coset of A meets every left coset of B.

**L0.7 [PUB] Sun's statement for k ≤ 4, in every group.**
- k = 2: Sun 2006 Remark 2.2 (equivalently L0.6).
- k = 3, 4: Zhu Theorem 1.1 (Thms 2.2 and 3.1). It is also a consequence of M-S Theorem B.

**L0.8 [PUB, M-S Props 4.2, 4.3, 4.5]. Index tuples that are G-harmonic for no group G.** Throughout, the r_i are pairwise coprime.
- **Prop 4.2:** (2r_1, 2r_2, 2r_3).
- **Prop 4.3:** (3r_1, ..., 3r_4).
- **Prop 4.5:** (2r_1, 4r_2, 4r_3, 4r_4) with r_1 odd.

These are used only in R1 (README). The engine reproduces them as a control (§C below).

## L1. Triangle lemma T [NEW form; subsumes M-S Lemma 3.10(a),(c) and Zhu (3.1), (3.4)]

Fix distinct vertices a, b, c. Put L = lcm(n_a, n_b, n_c) and T = [G : U_a∩U_b∩U_c].

**Statement.** L divides T. The quotient τ = T/L is a positive integer satisfying:

- **(T1)** I_xy divides L·τ for each pair {x, y} ⊆ {a, b, c}.
- **(T3)** For every labelling {x, y, z} = {a, b, c}:
  |U_y(U_x∩U_z)| = |G| · L · τ / (n_y · I_xz).
- **(T2)** For every labelling, |U_y(U_x∩U_z)| ≤ min(|U_yU_x|, |U_yU_z|).

*Proof.*
- The triple intersection lies in each U_x and in each U_x∩U_y. Hence every n_x divides T, so L | T. Likewise every I_xy divides T = Lτ, which is (T1).
- (T3) is L0.1 applied with |U_y| = |G|/n_y, |U_x∩U_z| = |G|/I_xz and |U_x∩U_y∩U_z| = |G|/T.
- (T2) holds because U_y(U_x∩U_z) ⊆ U_yU_x ∩ U_yU_z.

**Definitions.**
- τ_min is the least positive τ satisfying (T1). The set of solutions of (T1) is exactly the set of multiples of τ_min, since I_xy | Lτ ⟺ (I_xy / gcd(I_xy, L)) | τ.
- τ_max is the largest τ satisfying (T2) at all three apexes.

**T-kill.** If τ_min > τ_max, no harmonic configuration has these data.

**Core(5) form.**
- L = 4 r_a r_b r_c.
- (T1) ⟺ α_xy | r_z τ.
- (T3) reads |U_y(U_x∩U_z)| = τ |G| / (4 α_xz).
- (T2) ⟺ τ ≤ α_xy α_xz and τ ≤ α_yz α_xz.

So τ_max is the smallest product of two of the three α's. Also τ_min = lcm over the edges xy of α_xy / gcd(α_xy, r_z). Here gcd(α, r_z) = α exactly when α = 2 and z = E2, or α = 3 and z = E3; otherwise it is 1.

## L2. Linking [NEW form of the step used in M-S 3.7, 3.8, 3.10(b)]

**Statement.** If |U_y(U_x∩U_z)| = |U_yU_x|, then U_yU_x ⊆ U_yU_z, and also U_xU_y ⊆ U_zU_y.

*Proof.*
- U_y(U_x∩U_z) is contained in U_yU_x and has the same size, so the two sets are equal. It is also contained in U_yU_z.
- Taking inverses of U_yU_x ⊆ U_yU_z gives U_xU_y ⊆ U_zU_y.

**Core(5) form.** The hypothesis holds exactly when τ = α_xy α_xz, the product of the two α's at x.

## L3. Lemma K [NEW generalisation of M-S Lemma 3.5; subsumes Cor 3.6, Prop 3.8, Cor 3.9, Lemma 3.10(b), Cor 3.11]

**Statement.** Let v be a vertex and S a set of other vertices. Suppose that for every pair {i, j} ⊆ S,

  U_vU_i ⊆ U_jU_i   or   U_vU_j ⊆ U_iU_j.

Then Σ_{i∈S} |U_iU_v| ≤ |G| − |U_v| < |G|, that is, Σ_{i∈S} α_iv / g_iv < 1. In Core(5) this reads Σ_{i∈S} α_iv ≤ 3.

*Proof.*
1. **The sets g_iU_iU_v (i ∈ S) are pairwise disjoint.** Suppose g_iu_iu = g_ju_ju' with u, u' ∈ U_v.
   - Then g_j⁻¹g_i = u_j u' u⁻¹ u_i⁻¹ ∈ U_jU_vU_i.
   - If U_vU_i ⊆ U_jU_i, then U_jU_vU_i ⊆ U_jU_i. This contradicts L0.2 for the disjoint pair g_jU_j, g_iU_i.
   - If instead U_vU_j ⊆ U_iU_j, then g_i⁻¹g_j ∈ U_iU_vU_j ⊆ U_iU_j, the same contradiction.
2. **None of these sets meets g_vU_v.** Each g_iU_iU_v is right U_v-invariant. If it met g_vU_v it would contain g_v, say g_v = g_iu_iu. Then g_vu⁻¹ = g_iu_i lies in g_vU_v ∩ g_iU_i, which is empty.
3. **Counting.** Summing the sizes |g_iU_iU_v| = |U_iU_v| = α_iv |G| / g_iv gives the claim.

**K1 (links).** The pair condition for {i, j} at v holds if |U_i(U_v∩U_j)| = |U_iU_v|, or if |U_j(U_v∩U_i)| = |U_jU_v|.
- By L2, the first equality gives U_vU_i ⊆ U_jU_i, and the second gives U_vU_j ⊆ U_iU_j.
- Core(5) form: τ_{ivj} = α_iv α_vj, where the product is of the two α's at v.

**K2.** If U_vU_j ⊆ U_vU_k (v, j, k distinct), then α_vj / g_vj + α_kj / g_kj < 1. In Core(5): α_vj + α_kj ≤ 3.

*Proof of K2.* Apply L3 at vertex j with S = {v, k}. Its pair condition requires U_jU_v ⊆ U_kU_v, which is the inverse of the hypothesis.

**Corrections to M-S.**
- *M-S Cor 3.11.* The printed proof asserts "by Lemma 3.10a) gcd(r_v, α(U,W)) = 1". With α(U,W) = α(V,W) that step does not follow, because 3.10(a) becomes trivial. The statement is still true whenever α(U,W) is 1 or a prime:
  - since r_u and r_v are coprime, gcd(r_v, α) = 1 or gcd(r_u, α) = 1;
  - in the second case apply 3.10(b) with U and V swapped; the quantity |VU| + |UW| equals |UV| + |VW|.

  In this lane the statement is an instance of K1 + L3: τ ≤ τ_max forces a link at the vertex shared by the two equal edges. This settles the screen caveat.
- *M-S Lemma 4.4.* The first bullet is misprinted. It should read "α(U_2, U_3) ≠ 2", and that is what its proof shows.

## L4. Vertex count P [NEW form; subsumes the Lemma 3.1 counts in M-S Props 4.3/4.5 and screen N1]

Fix a vertex v. For each other vertex j put X_j = U_vU_j and Y_j = G ∖ X_j.

**Statement.**
- **(P1)** |X_j| = α_vj |G| / g_vj, and U_v ⊆ X_j.
- **(P2)** |X_j ∩ X_k| is a multiple of u_vjk = |G| / gcd(n_v, I_jk). In Core(5), u_vjk = |G| / (4 gcd(r_v, α_jk)).
- **(P3)** |X_j ∩ X_k| ≥ max(|U_v(U_j∩U_k)|, |X_j| + |X_k| − |G|). The first term is given by (T3).
- **(P4)** If |X_j ∩ X_k| = |X_j|, then X_j ⊆ X_k, so K2 must hold for that containment.
- **(P5)** For every set S of other vertices:
  Σ_{j∈S} |Y_j| − Σ_{j<k in S} |Y_j ∩ Y_k| < |G|,
  where |Y_j ∩ Y_k| = |G| − |X_j| − |X_k| + |X_j ∩ X_k|.

*Proof.*
- (P2): by L0.5, X_j ∩ X_k is a union of (U_v, U_j∩U_k)-double cosets. By L0.4, each has size a multiple of |G| / gcd(n_v, I_jk). In Core(5), gcd(4r_v, 4r_jr_kα_jk) = 4 gcd(r_v, α_jk), because gcd(r_v, r_jr_k) = 1.
- (P3): U_v(U_j∩U_k) ⊆ X_j ∩ X_k, and inclusion–exclusion gives the second bound.
- (P4): immediate from K2.
- (P5): this is the Bonferroni inequality. Also ∪_j Y_j ⊆ G ∖ U_v, which is a proper subset of G.

**How the engine uses P (sound).** For each pair {j, k}:
- hi_jk is the largest multiple of u that is ≤ min(|X_j|, |X_k|). It is lowered by one unit u when equality would force a containment that K2 forbids. If |X_j| = |X_k|, equality would force X_j = X_k, and then both K2 conditions must hold.
- lo_jk is (P3) rounded up to a multiple of u.
- If lo_jk > hi_jk the pattern is killed: **P-pair**.
- Otherwise the left side of (P5) is non-increasing in each |X_j ∩ X_k|. If (P5) already fails with every |X_j ∩ X_k| set to hi_jk, it fails for the true values, and the pattern is killed: **P-Bonferroni**.

## L5. N2: all ten α = 2 is impossible in Core(5) [NEW, unreviewed]

*Proof.*
1. **Every triangle has τ = 2.** Each edge has α = 2, and at most one vertex is E2. So by (T1) τ is even, and by (T2) τ ≤ 4.
   - If τ = 4, then (T2) holds with equality at every apex. So every vertex is linked for the other two (K1), and L3 at any vertex of the triangle gives 2 + 2 ≤ 3, which is false.
   - Hence τ = 2. Therefore [G : U_a∩U_b∩U_c] = 8 r_a r_b r_c for every triangle.
2. **Fix a vertex v with r_v odd.** One exists, since at most one r is even. For the other vertices j put X_j = U_vU_j; then |X_j| = |G|/2.
3. **Pairwise intersections.** For other vertices j ≠ k put Z_jk = U_v(U_j∩U_k).
   - By (T3), |Z_jk| = 2|G| / (4·2) = |G|/4, and Z_jk ⊆ X_j ∩ X_k.
   - By (P2), |X_j ∩ X_k| is a multiple of |G| / (4 gcd(r_v, 2)) = |G|/4.
   - |X_j ∩ X_k| ≠ |G|/2: otherwise X_j = X_k, and K2 would give 2 + 2 ≤ 3.
   - Hence X_j ∩ X_k = Z_jk.
4. **The three Z's of a triple coincide.** Take distinct other vertices j, k, l and put W = U_j∩U_k∩U_l, so [G:W] = 8 r_j r_k r_l.
   - Q = [G : U_v ∩ W] is divisible by the three triangle indices 8 r_v r_j r_k, 8 r_v r_j r_l and 8 r_v r_k r_l. By coprimality, Q is divisible by 8 r_v r_j r_k r_l.
   - So |U_vW| = |G| Q / (4 r_v · 8 r_j r_k r_l) ≥ |G|/4.
   - But U_vW ⊆ Z_jk ∩ Z_jl ∩ Z_kl, and each Z has size |G|/4. Hence Z_jk = Z_jl = Z_kl = U_vW.
5. **Contradiction.** The six sets Z among the four other vertices are therefore all one set Z with |Z| = |G|/4.
   - The four sets X_j ∖ Z are pairwise disjoint, each of size |G|/4.
   - So |∪_j X_j| = 4·|G|/4 + |G|/4 = 5|G|/4 > |G|, a contradiction.

## L6. Fibre lemma F [NEW form; the case of H1 below subsumes screen N3]

Let H ≤ G with [G:H] = m. For each vertex l put t_l = [U_l : U_l∩H] and λ_l = [H : U_l∩H].

**Statement.**
- **(F1)** n_l t_l = m λ_l and 1 ≤ t_l ≤ m. The coset g_lU_l meets exactly t_l left cosets of H.
- **(F2)** Fix a left coset C of H and z ∈ C, and let S_C = {l : g_lU_l ∩ C ≠ ∅}.
  - For each l ∈ S_C, the set z⁻¹(g_lU_l ∩ C) is a left coset in H of U_l∩H. These cosets are pairwise disjoint.
  - Hence, if |S_C| = s ≥ 2, then gcd(λ_l, λ_l') ≥ s for some l ≠ l' in S_C. This uses L0.7 for s ≤ 4, and for s = 5 the minimality of G (§0; H is proper).
- **(F3)** If U_i ⊆ H, then |U_iU_l| ≤ |HU_l| = t_l |G| / m, that is, α_il / g_il ≤ t_l / m. In particular, if U_i, U_j ⊆ H then α_ij / g_ij ≤ 1/m.

*Proof.*
- (F1): [G : U_l∩H] = n_l t_l = m λ_l. The set g_lU_lH is a union of |U_lH| / |H| = t_l left H-cosets. Also t_l ≤ m, since distinct cosets of U_l∩H in U_l lie in distinct cosets of H.
- (F2): take y ∈ g_lU_l ∩ C. Then g_lU_l = yU_l and C = yH, so g_lU_l ∩ C = y(U_l∩H). Since z⁻¹y ∈ H, z⁻¹y(U_l∩H) is a left coset in H. Disjointness is preserved by translation.
- (F3): U_iU_l ⊆ HU_l, and |HU_l| = |H||U_l| / |H∩U_l| = t_l |H|.

## L7. Sources of a subgroup H

**H1 [PUB, M-S Lemma 3.7].** Suppose [G:U] = a r_u, [G:V] = a r_v, [G:W] = a r_w with r_u, r_v, r_w pairwise coprime, and α(U,V) = α(U,W) = α(V,W) = 1. Then UV = VU = UW = WU = VW = WV is a subgroup of index a. It contains U, V and W. In Core(5), a = 4.

**H2 [NEW, unreviewed].** In Core(5), suppose α_ab = 1, and let V2 be the non-empty set of vertices v with α_va = α_vb = 2. Put W = ⟨U_a, U_b⟩. Then one of the following holds:
- **(i)** [G:W] = 4, W = U_aU_b, and t_v = [U_v : U_v∩W] = 2 for every v ∈ V2;
- **(ii)** [G:W] = 2, and U_v ⊆ W for every v ∈ V2.

*Proof.* Fix v ∈ V2 and work in the triangle {v, a, b}.
1. **τ = 2.** By (T2), τ ≤ min(2·2, 2·1, 2·1) = 2. By (T1), 2 | r_b τ and 2 | r_a τ. Since r_a and r_b are not both even, τ is even. So τ = 2.
2. **U_vU_a = U_vU_b.** By (T3), |U_v(U_a∩U_b)| = 2|G| / (4·1) = |G|/2 = |U_vU_a| = |U_vU_b|. Hence U_vU_a = U_v(U_a∩U_b) = U_vU_b. Call this set X.
3. **X = U_vW.** X is right-invariant under U_a and under U_b, hence under W. Since U_v ⊆ X, this gives U_vW ⊆ X. Conversely X = U_vU_a ⊆ U_vW. So X = U_vW, and |X| = |G|/2 shows W ≠ G.
4. **[G:W] ∈ {2, 4}.** [G:W] divides gcd(4r_a, 4r_b) = 4.
5. **Index 4.** U_aU_b ⊆ W, and |U_aU_b| = |G|/4 = |W|, so W = U_aU_b. Also |U_vW| = t_v |W| = |G|/2, so t_v = 2.
6. **Index 2.** |U_vW| = |G|/2 = |W|, so U_v ⊆ W.

W does not depend on v, so the same alternative holds for all v ∈ V2.

## L8. Soundness of the engine's evaluation points [NEW]

**(M1) Evaluating at τ = τ_min is enough.** Every admissible τ is a multiple of τ_min, so τ ≥ τ_min. Every rule the engine uses is upward closed in each triangle's τ:
- T-kill means τ_min > τ_max.
- A link (K1) at τ_min means (T2) holds with equality there. Then τ = τ_min is forced, because a larger τ would violate (T2). So the links present at τ_min are present for every admissible τ.
- The lower bounds in (P3) increase with τ. The values hi_jk and the K2 conditions do not depend on τ.
- F, H1, H2 and N2 do not use the program's τ.

So a kill at τ_min is a kill for every admissible τ.

**(M2) Representative values of r are enough.** A Core(5) pattern (α, E2, E3) quantifies over all pairwise coprime r. The engine instead fixes

  r_i = p_i · 16^[i=E2] · 81^[i=E3],   with distinct primes p_i ∈ {5, 7, 11, 13, 17}.

Every quantity it uses depends on r only through the following:
- g_ij = 4;
- whether α_xy | r_z, and gcd(r_v, α_jk). Both depend only on the E2/E3 status.
- In F, gcd(λ_l, λ_l') = 2^min(v_2) · 3^min(v_3).
  - No prime p ≥ 5 is common to the two, since the r's are coprime, t ≤ 4 and m ∈ {2, 4}.
  - With v_2(r_E2) = 4 ≥ 3 and v_3(r_E3) = 4 ≥ 2, each min equals the largest value over all instances.
  - The F-kill condition "no pair reaches s" is monotone, so a kill at the representative is a kill for every instance.

## Engine rule order and certificates

**Order.** Rules are applied in the order T, K, P-pair, P-Bonferroni, N2, F-H1, F-H2. The certificate of a pattern is the first rule that fires, together with its witness:
- T: the triangle;
- K: the vertex and S;
- P: the vertex and the pair or S;
- N2: none;
- F: the source of H and the number of fibre assignments examined, all of which are refuted.

Patterns killed only through N2 or H2 are flagged, because those lemmas are [NEW] and unreviewed.

**F enumeration.**
- For each vertex l not known to lie inside H, the engine enumerates t_l ∈ {1, ..., m} and the set M_l of met cosets with |M_l| = t_l.
- Known inside vertices: the triangle for H1, and {a, b} for H2. For these t = 1, and they are placed in all possible cosets.
- Constraints:
  - (F3), with respect to every vertex that has t = 1;
  - t_v = 2 (case i) or t_v = 1 (case ii) for v ∈ V2 under H2;
  - (F2) in every coset, using the maximal possible gcds (M2).

**Controls (§C, required by the contract).**
- (C1) The same engine with rules T, K and P only, run on the shapes (2,2,2), (3,3,3,3) and (2,4,4,4) with r_1 odd, must kill every pattern. That reproduces M-S Props 4.2, 4.3 and 4.5.
- (C2) Realisable configurations must survive when the engine is run on their exact data: Menon's A5 example (6,6,6,10,15), the C2×S4 example (4,6,6,6,6), all their 4-subconfigurations, and k cosets of one subgroup. This is a sanity control with explicit permutation groups, not gate evidence.
- (C3) Exact computations give α = 1 in cyclic groups and α ≤ 2 in abelian groups for indices of the form 4r. These are sanity controls.
- (C4) Mutating one label (an α value or the E2/E3 status) in a certificate must break that certificate for the stated reason.
