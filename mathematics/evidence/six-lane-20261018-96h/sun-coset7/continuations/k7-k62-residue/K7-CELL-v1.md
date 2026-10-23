# K7-CELL: index-3 subgroups from equality structures; the K_{2,3} family of Case A and the Case-B family of (a1) are empty (conditional)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:39:34-0700.
- **Owner:** Sun7K62Successor. Single author, unreviewed. No computation was run; no probe is a premise.
- **Status:** CANDIDATE, **conditional** on the unreviewed candidates `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf),
  `K7-TC-v1.md` (cc48340d...e117) and `K7-TC-A22-v1.md` (9ebec279...1b46b41), read through the overlay
  `K7-A1-A2-delta-erratum-v1.md` (0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e), and on
  `K7-CASEA-K23-v1.md` (f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3: Theorem K7-CASEA-K23,
  Proposition K7-CASEB-T). Used from them: Lemma TC, Lemma FG-V, Theorem CASEB, Theorem K7-TC-B, Theorem K7-CASEA-K23,
  Proposition K7-CASEB-T. No closure claim: Sun(7) remains OPEN.
- **Accepted imports:** RICH (verdict sha256 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0); LFC
  (a)-(d), INV, VFC (V1)-(V4), L0.1, L0.3, R0. **Direct Sun instances:** Sun(2) and Sun(3) (Zhu) only, the latter also
  applied inside the subgroup K cap L (section 4). Transitive closure as in A1-STRUCT section 0 (as amended).

## 0. Conventions

Setting (a1) (RICH section 0). C is the configuration (subgroups U_j, representatives g_j) or its inverse (subgroups
g_jU_jg_j^-1, representatives g_j^-1); x denotes the alpha-matrix of C and x* that of its inverse, so in C:
mu(U_jU_k) = x_jk/6 (L0.3) and, at an apex a normalised g_a = 1, X_j := U_aU_j (measure x_aj/6), Y_j := G \ X_j,
D_j := U_a g_j U_j subset Y_j (V1) of measure x*_aj/6 with local index x*_aj r_j (INV (b)). For a subgroup K of G and a
vertex i, m^K_i := [U_i : U_i cap K] is the number of left K-cosets met by g_iU_i, and mu(U_iK) = mu(KU_i) = m^K_i/[G : K].

## 1. Lemma EQ (equality structure) [NEW]

Let a in W and suppose that at apex a of C the masses x*_aj/6 on (W cup {t}) \ {a} are 4/6 at two vertices g1, g2
(local indices 4 times an odd number) and 2/6 at the three others s1, s2, s3 (local indices 2 times an odd number), and
z has mass 3/6. Then **D_g1 = D_g2**, both equal to the union Q of the right U_a-cosets meeting g1 or g2, and
mu(Q) = 4/6.
*Proof.* Every pair among g's and s's has gcd 4 (two g's) or 2; a set holding a g and two s's, or three s's, has all
pairwise gcds 2 and is not allowed (Sun(3), VFC (V3), heredity), with or without z. So a coset in Q holds at most one s,
and a coset outside Q at most two. The s-mass is 6/6, hence 1 <= mu(Q) + 2 (mu(U) - mu(Q)) with U the union of all D_j,
so mu(U) >= (1 + mu(Q))/2 >= 5/6 since mu(Q) >= mu(D_g1) = 4/6. Lemma FG-V gives mu(U) <= 5/6, so mu(Q) = 4/6, and
D_g1, D_g2 (subsets of Q of measure 4/6) equal Q. QED

## 2. Lemma SUB (index-3 subgroup) [NEW]

At an apex a of C (g_a = 1) let D_j = D_k with mu(D_j) + mu(X_j) = 1 (so D_j = Y_j), and suppose x_jk = x_aj = 2. Then
**K := U_aU_j = U_jU_k is a subgroup of index 3 containing U_a, U_j, U_k**, and g_aK, g_jK, g_kK are pairwise distinct
except that g_aK = g_kK is possible when x_ak != 2.
*Proof.* X_j = G \ D_k is right-invariant under U_k (D_k is) and under U_j, hence under <U_j, U_k>, and contains 1; so
<U_j, U_k> subset X_j and mu(<U_j, U_k>) <= 2/6. Also U_jU_k subset <U_j, U_k> and mu(U_jU_k) = x_jk/6 = 2/6. Hence
<U_j, U_k> = X_j = U_jU_k =: K, of measure 1/3, and U_a subset U_aU_j = K. Disjointness of g_iU_i and g_lU_l means
g_i^-1 g_l is not in U_iU_l (L0.2); U_aU_j = U_jU_k = K, and U_aU_k = K when x_ak = 2. QED

## 3. Lemma IN (counting inside a subgroup of index 3) [NEW]

Let K have index 3 and contain U_j for a vertex j (apex j of C). For every vertex i whose coset meets g_jK,
**x_ji < 2 m^K_i**; in particular, if x_ji = 4 then m^K_i = 3.
*Proof.* The fibres at j (left U_j-cosets) inside g_jK number n_j/3, one of them g_jU_j (no piece, LFC (b)). The left
multiplications by g_iug_i^-1 (u in U_i) preserve g_iU_i, the fibres and the set L_i of fibres meeting g_iU_i, and
permute transitively the m^K_i left K-cosets met by g_iU_i; so each of them contains t_i/m^K_i fibres of L_i, with
t_i = n_j x_ji/6 (LFC (a)-(b)). The weight y_i = 1 (all others 0) is feasible, so summing over the fibres inside g_jK:
n_j x_ji/(6 m^K_i) <= n_j/3 - 1 < n_j/3. QED
**Lower bound.** If U_l subset K and mu(U_iU_l) = x_il/6 > 1/3, then m^K_i >= 2 (U_iU_l subset U_iK).

## 4. Lemma CELL [NEW]

Let K != L be subgroups of index 3, and let K contain U_v for three vertices v (the "K-vertices") whose cosets lie in the
three distinct left K-cosets, L contain U_x for three vertices x (the "L-vertices") whose cosets lie in the three
distinct left L-cosets, with m^L_v = 3 for every K-vertex and m^K_x = 3 for every L-vertex. Then:
- (i) [G : K cap L] = 9, and the nine left (K cap L)-cosets ("cells") correspond bijectively to the pairs
  (left K-coset, left L-coset); every cell contains a piece of the K-vertex of its K-coset (a left coset of U_v cap L, of
  index n_v/3 in K cap L) and a piece of the L-vertex of its L-coset (index n_x/3).
- (ii) For any other vertex z, a nonempty piece g_zU_z cap c of a cell c is a left coset of U_z cap K cap L, whose index
  N_z in K cap L has all prime factors in {2, 3} or dividing r_z.
- (iii) If in a cell c the three pieces of v, x and z have pairwise gcds of indices <= 2, then g_zU_z does not meet c
  (Sun(3) inside K cap L).
*Proof.* (i) U_xK = G for an L-vertex x, so LK = G and |L||K|/|L cap K| = |G|. A K-coset meets each L-coset in at most
one (K cap L)-coset and is the union of three of them, which gives the bijection. g_vU_v meets all three L-cosets
(m^L_v = 3), each in a left coset of U_v cap L subset K cap L, of index n_v m^L_v / 9 = n_v/3; likewise for x.
(ii) [G : U_z cap K cap L] = n_z [U_z : U_z cap K] [U_z cap K : U_z cap K cap L], and both brackets are integers <= 3.
(iii) Translating c to K cap L, the three pieces are pairwise disjoint left cosets of subgroups of K cap L. QED

In setting (a1), n_v/3 = 2 r_v with r_v = w_v for v in W and r_t = 3^A 5^Bt w_t; the w's are coprime to 30 and Bz Bt = 0.
Hence for v, x in W and any third vertex z: gcd(2 w_v, 2 w_x) = 2 and gcd(2 w_v, N_z), gcd(2 w_x, N_z) divide 2.

## 5. Theorem K7-CELL-A (conditional) [NEW]

**No (a1) configuration lies in the K_{2,3} family of Theorem K7-CASEA-K23 (nor in its inverse).**

*Proof.* Work in C = C^alpha (the inverse family is the same statement for the inverted configuration, E6). Data
(K7-CASEA-K23): W = {v1, v2} cup {x, y, w}; alpha = 4 on v-(x,y,w) and t-(x,y,w), alpha = 2 inside {x, y, w} and on
v1 v2, alpha_zu = 3 on W, alpha_tv in {1, 2} not both 1; alpha* = 2 on v-(x,y,w), alpha* = 4 inside {x, y, w} and on
v1 v2, alpha*_tv = 4, alpha*_t in {1, 2} on {x, y, w}.
- **K.** Choose i in {1, 2} with alpha_tv_i' = 2 for the other index i' (possible as not both alpha_tv are 1). At apex
  v_i the masses alpha*_(v_i j)/6 are v_i' and t: 4/6, x, y, w: 2/6, z: 3/6 (local indices 4w, 4 3^A 5^Bt w_t, 2w,
  3 2^E 5^Bz w_z). Lemma EQ gives D_(v_i') = D_t; alpha_(v_i v_i') = 2 gives D_(v_i') = Y_(v_i'); Lemma SUB
  (j = v_i', k = t, x_jk = alpha_(v_i' t) = 2) gives K = U_v1U_v2 = U_(v_i')U_t of index 3 containing U_v1, U_v2, U_t,
  with v1, v2 and v_i', t in distinct K-cosets.
- **t has its own K-coset.** See the cell step below.
- **L.** By LFC (d) at t in C^alpha* (labels: v1, v2: 4w; a 3-side vertex with alpha*_t = 1: w, coprime to all), at most
  one of x, y, w has alpha*_t = 1 (y = 1/2 on v1, v2 and 1 on two such ones gives value 6). Take x with alpha*_tx = 2.
  At apex x the masses are y, w: 4/6; v1, v2, t: 2/6; z: 3/6. Lemma EQ gives D_y = D_w; alpha_xy = 2 gives D_y = Y_y;
  Lemma SUB (j = y, k = w, alpha_yw = 2) gives L = U_xU_y = U_yU_w of index 3 containing U_x, U_y, U_w, with x, y, w in
  distinct L-cosets (all alpha = 2 inside {x, y, w}).
- **m's.** For u in {x, y, w}: mu(U_uU_v1) = 4/6, so m^K_u >= 2; if m^K_u = 2, g_uU_u meets a K-coset containing the coset
  of v1, v2 or t, and Lemma IN at that apex (alpha_vu = alpha_tu = 4) gives m^K_u = 3. So m^K_u = 3. Likewise, for
  j in {v1, v2, t}: mu(U_jU_x) = 4/6, every L-coset contains one of x, y, w, and alpha_(u j) = 4 for u in {x, y, w}, so
  m^L_j = 3. K != L since U_x is not inside K.
- **Cells.** If t shared its K-coset with v1 (or v2), the cells of that K-coset would contain pieces of v1, t and an
  L-vertex u with indices 2w_v1, 2 3^A 5^Bt w_t, 2w_u, pairwise gcd 2: Lemma CELL (iii) applied to the vertex t (with
  N_t = 2 3^A 5^Bt w_t) excludes it. So v1, v2, t occupy the three K-coset and Lemma CELL applies. In a cell of the
  K-coset of v1 or v2 the pieces of v, u (an L-vertex) and z have pairwise gcds <= 2 (section 4), so g_zU_z meets none
  of these cells; hence g_zU_z lies in the K-coset of t, i.e. U_z subset K. Then U_zU_v1 subset K has measure <= 1/3,
  while mu(U_zU_v1) = alpha_zv1/6 = 1/2. Contradiction. QED

## 6. Theorem K7-CELL-B (conditional) [NEW]

**No (a1) configuration lies in Case B (T = W != T*), nor in its mirror (T* = W != T).**

*Proof.* Work in C = C^alpha* (the mirror is the inverted configuration). Data (CASEB, K7-TC-B, K7-CASEB-T):
T* = {a1, a2, a3}, W \ T* = {v1, v2}; alpha: a-a 4, a-v 2, v1 v2 4, t-v 4, t-a 2; alpha*: a-v 4, a-a 2, v1 v2 2,
t-a 4, z-a 3, alpha*_tv in {1, 2}. In C the masses at an apex u are alpha_uj/6 and mu(U*_jU*_k) = alpha*_jk/6.
- **H.** At apex a1 the masses are a2, a3: 4/6; v1, v2, t: 2/6 (alpha_ta1 = 2); z: 3/6 (local indices 4w, 2w,
  2 3^A 5^Bt w_t, 3 2^E 5^Bz w_z). Lemma EQ gives D*_a2 = D*_a3; alpha*_(a1 a2) = 2 gives D*_a2 = Y*_a2; Lemma SUB
  (alpha*_(a2 a3) = 2) gives H = U*_a1U*_a2 = U*_a2U*_a3 of index 3 containing U*_a1, U*_a2, U*_a3; as alpha* = 2 on all
  a-a pairs, the three a's occupy the three H-cosets.
- **K'.** LFC (d) at t in C^alpha (labels a: 4w; v with alpha*_tv = 1: w) forbids alpha*_tv1 = alpha*_tv2 = 1 (y = 1/3 on
  the a's, 1 on the two ones: value 6). Choose i with alpha*_(t v_i') = 2. At apex v_i the masses are v_i': 4/6
  (alpha_v1v2 = 4), t: 4/6 (alpha_tv = 4), a1, a2, a3: 2/6, z: 3/6; Lemma EQ gives D*_(v_i') = D*_t;
  alpha*_v1v2 = 2 gives D*_(v_i') = Y*_(v_i'); Lemma SUB (alpha*_(v_i' t) = 2) gives K' = U*_v1U*_v2 = U*_(v_i')U*_t of
  index 3 containing U*_v1, U*_v2, U*_t.
- **m's.** m^H_v, m^H_t >= 2 (mu(U*_aU*_v) = mu(U*_aU*_t) = 4/6) and Lemma IN at the a's (alpha*_av = alpha*_at = 4) give
  m^H_v1 = m^H_v2 = m^H_t = 3; m^K'_a >= 2 (mu(U*_aU*_v1) = 4/6) and Lemma IN at v1, v2, t (alpha*_va = alpha*_ta = 4)
  give m^K'_a = 3 (any two K'-cosets contain the coset of v1 or v2). K' != H.
- **Cells.** As in section 5, t cannot share a K'-coset with v1 or v2 (pieces v, t, a with indices 2w_v,
  2 3^A 5^Bt w_t, 2w_a, pairwise gcd 2), so Lemma CELL applies with K-vertices v1, v2, t and L-vertices a1, a2, a3.
  z meets no cell of the K'-cosets of v1, v2 (pieces v, a, z, pairwise gcds <= 2), so U*_z subset K' and z lies in the
  K'-coset of t. Then N_z = [G : U*_z cap H]/9 = n_z m^H_z/9 is an integer only if m^H_z = 3, so
  N_z = 2^(E+1) 5^Bz w_z, and in every cell of that K'-coset the pieces of t, of the a and of z have indices
  2 3^A 5^Bt w_t, 2 w_a and 2^(E+1) 5^Bz w_z, pairwise gcd 2 (Bz Bt = 0): z meets no cell. Contradiction. QED

## 7. Conditional chain and scope

- **Chain (stated only as a conditional chain, not as a closure claim).** If RICH (accepted), A1-STRUCT, K7-TC, K7-TC-A22
  (through the overlay), K7-CASEA-K23 and this file are all correct, then in (a1): TZ (iii) gives T = W or T* = W;
  T = T* = W is Case A, which K7-TC-A22, K7-CASEA-K23 and Theorem K7-CELL-A leave empty; T = W != T* is Case B and its
  mirror, empty by Theorem K7-CELL-B. Each link is pending review; no exclusion of (a1) is asserted here.
- **Not covered:** (a2) (no transfer to (a2-no5) or (a2-zt5) is claimed); K6.2*; full Sun(7). No novelty, Lean or
  human-review claim.
- **Requested checks:** Lemma EQ (set sizes; in Case B and at x the vertex t is a two and {z, t, s} is allowed - the
  count only uses "at most two twos outside Q"); Lemma SUB (right-invariance and measures); Lemma IN (homogeneity of
  fibres across K-cosets); Lemma CELL (bijection of cells; prime factors of N_z); the two cell contradictions, in
  particular the integrality step m^H_z = 3 in Theorem K7-CELL-B and the final measure contradiction in K7-CELL-A.
