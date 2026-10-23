# K7-D23-RICH: different-vertex 2/3 markers (5-marker absent, on z or on t): no configuration whose alpha*-three centre neighbours all carry an alpha W-three; structural lemmas for the residue

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T05:13:41-0700.
- **Owner:** Sun7K62Successor (continuation `k7-k62-residue`). Single author, unreviewed.
- **Status:** CANDIDATE written mathematics. No computation was run for it; no exploratory output is a premise. "[NEW]" =
  written here, not a novelty claim. Full Sun(7) and the K7 different-vertex family remain OPEN (see section 9).

## 0. Exact scope (frozen before the claims) and imports

**Setting (a1).** Class K7: n_i = 6 r_i, r_i pairwise coprime, r_i = m_i w_i with m_i the {2,3,5}-part and the w_i
pairwise coprime and coprime to 30. The 2-marker is on z and the 3-marker on t != z:

  r_z = 2^E 5^Bz w_z,  r_t = 3^A 5^Bt w_t,  E, A >= 1,  Bz, Bt >= 0,  Bz * Bt = 0,

and the five vertices of W := V \ {z, t} are unmarked (n_u = 6 w_u). All exponents are actual and unbounded. alpha and
alpha* are the (symmetric) alpha-matrices of the configuration and of its inverse (INV); 1 <= alpha, alpha* <= 5 and
alpha + alpha* <= 6 on every pair. Put T := {u in W : alpha_zu = 3} and T* := {u in W : alpha*_zu = 3}. For a
vertex u in W and x in {alpha, alpha*}, the **x-row at u** is (x_uv)_(v in W\{u}) together with c := x_uz, e := x_ut.
W3 := {u in W : alpha_uv = 3 for some v in W}, W3* likewise for alpha*.

**Accepted imports (exact uses).**
- R0, K7 definition, L0.1 (|XY| = |X||Y|/|X cap Y|) and Lagrange: `six-lane-20261016/sun-coset7/README.md` sha256
  2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1, sections 0, 1, 5.
- LFC (a)-(d), INV (a)-(b), erratum E1 (1 <= alpha <= g - 1), E2 (Sun(2)), E6 (the inverted configuration has the
  same labelled indices and markers; inversion is an involution), E7 (alpha + alpha* <= g), and the ROW-U class
  analysis with its standard weights and the subset value bound min(N, 4) of E8: `K7-LFC-INV-v1.md` sha256
  45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c + `K7-LFC-INV-erratum-v1.md` sha256
  7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5; verdict `RUN/review/sun7-lfc-inv-parent-verdict-v1.md`
  sha256 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18 (item 6: R0 also preserves alpha*).
- L1 (T1)-(T3) with tau_min / tau_max and VFC (V1)-(V4): `six-lane-20261016/sun-coset7/rules-k7-v1.md` sha256
  77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee, accepted by
  `six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` sha256
  73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35; applied to the inverted configuration as in
  `K7-Z2-erratum-v1.md` G5 (sha256 3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9).
- D23-MIX (accepted): `K7-D23-NO4-v1.md` sha256 a3b47626687141dac49daf30aab302c1ea66f15a74f28ee638b2212258de189d +
  `K7-D23-NO4-erratum-v1.md` sha256 594c28aab89a269b32f79385552fd226eb22c41e8be538cc5bebf895acc54d6a; verdict
  `RUN/review/sun7-D23-parent-verdict-v1.md` sha256 d3453de10eafab4d4666eb1902e18a13140beb4aee511df3c35febf21e4f37db. Used
  conclusion in (a1): **alpha_zu, alpha*_zu in {1,2,3} for u in W; |T|, |T*| >= 3; alpha_zt, alpha*_zt in {1,2}.**
- Sun(2), Sun(3), Sun(4) inside a subgroup only through LFC (c) / VFC (V3); Sun(5), Sun(6) only inside the imported
  ROW-U class analysis (E8). No Sun(7).
- **Not used:** K63-RES / K62 FG files (FG is re-proved here in this scope), TG (its one-line inequality is re-derived as
  G0), F7, RPLP, Ppair, K, ROW-1, ROW-2, the lemmas of K7-U1 / K7-Z2 / K7-Z23-P5, any probe or census.
RUN = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.

Conventions: at an apex v and orientation x, labels are lambda^x_j = n_j x_vj / 6 (LFC (a)); a weight vector y >= 0 is
*feasible* if its sum over every lambda^x-allowed set is <= 1; val(y) := sum_j y_j x_vj (units of 1/6). LFC (d):
val(y) < 6 for feasible y. Allowedness is hereditary; zero weights may be ignored when checking feasibility. Since the
w_j are pairwise coprime and coprime to 30, and every entry is <= 5, the w's never enter a label gcd.

## 1. Granularity and Lemma FG7 [NEW in this scope]

**G0.** For subgroups H, Y of a finite group G, mu(HY) = [G : H cap Y] / ([G:H][G:Y]) >= 1 / gcd([G:H], [G:Y]).
*Proof.* L0.1; [G : H cap Y] is a common multiple of [G:H] and [G:Y] (Lagrange), hence >= their lcm. QED

**Lemma FG7.** Let u in W, N := V \ {u}, and let (V_j)_(j in N) be subgroups of G with [G : V_j] = n_j and
beta_jk := [G : V_j cap V_k] / lcm(n_j, n_k) <= 5 for all j != k in N. For non-empty Q subset N put
T_Q := [G : intersection of V_j (j in Q)]. Then the prime-to-30 part of T_Q is the product of the w_j (j in Q);
hence gcd(n_u, T_Q) divides 6.

*Proof.* Order Q as: z (if in Q), then t (if in Q), then the unmarked vertices of Q in any order; write W_m for the
intersection of the first m groups and T_m = [G : W_m]. Base: T_1 = n_(j_1); if z, t in Q then
T_2 = lcm(n_z, n_t) beta_zt with beta_zt <= 5. Both have prime-to-30 part the product of their w's. Step: let e be the
next (unmarked) vertex, n_e = 6 w_e. T_(m+1) = [G : V_e cap W_m] is a common multiple of n_e and T_m, so
T_(m+1) = lcm(n_e, T_m) k with k a positive integer. By L0.1, mu(V_e W_m) = T_(m+1)/(n_e T_m) = k / gcd(n_e, T_m),
and V_e W_m subset V_e V_(j_1), whose measure is beta_(e j_1)/6 <= 5/6. By induction w_e is coprime to T_m, and
6 | T_m, so gcd(n_e, T_m) = 6 and k <= 5. Hence no prime > 5 divides k and the prime-to-30 part of T_(m+1) is that of
lcm(n_e, T_m). Finally gcd(n_u, T_Q) = gcd(6 w_u, T_Q) divides 6 because w_u is coprime to every other w. QED

FG7 applies to V_j = U_j (beta = alpha <= 5, E1) and to V_j = g_jU_jg_j^-1 (beta = alpha* <= 5, INV (b) with E1).

**Corollary 5/6.** For u in W, x in {alpha, alpha*} and every feasible y at u: **val(y) <= 5**. If val(y) = 5, then
every left fibre at u (orientation x) that meets one of the cosets carries weight exactly 1.

*Proof.* x = alpha. Normalise g_u = 1 (left translation changes nothing used). Put W* := intersection of the
g_jU_jg_j^-1 (j in N). W*U_u is a union of left U_u-cosets containing U_u. It meets no L_j := g_jU_jU_u: if wv lies in
L_j with w in W*, v in U_u, write w = g_j a g_j^-1 (a in U_j); then g_j a g_j^-1 lies in g_jU_jU_u, so g_j^-1 lies in
U_jU_u, so g_j lies in U_uU_j and g_jU_j meets U_u = g_uU_u, contradicting disjointness. By G0 and FG7 (with
V_j = g_jU_jg_j^-1, Q = N), M := #fibres in W*U_u = n_u mu(W*U_u) = n_u mu(U_uW*) >= n_u/6. LFC (a)-(c): with
t_j = n_u alpha_uj/6 fibres met by g_jU_j and S_C the set of j whose coset meets fibre C,
(n_u/6) val(y) = sum_j y_j t_j = sum_C sum_(j in S_C) y_j <= #{C : S_C non-empty} <= n_u - M <= 5 n_u/6. If
val(y) = 5, all inequalities are equalities, so every fibre outside W*U_u (in particular every fibre meeting a coset)
has weight exactly 1. x = alpha*: the same for the inverted configuration (INV (a), E6). QED

## 2. Lemma NO5 [NEW in this scope]

For u in W, v in W \ {u}: alpha_uv != 5 and alpha_ut != 5; the same for alpha*.

*Labels at u.* lambda_v = alpha_uv w_v (v in W), lambda_z = 2^E 5^Bz c w_z, lambda_t = 3^A 5^Bt e w_t, with
c = alpha_uz in {1,2,3} (D23-MIX), e = alpha_ut.

*(a) No W-five.* Suppose alpha_uv = 5 for some v; F5 := {v' in W\{u} : alpha_uv' = 5}.
- Bz = 0: lambda_z has no factor 5, so gcd(lambda_v, lambda_z) = 1; y_v = y_z = 1 (else 0) is feasible and
  val = 5 + c >= 6, contradicting LFC (d).
- Bz >= 1 (so Bt = 0). If 5 does not divide e, lambda_t is coprime to lambda_v: y_v = y_t = 1 gives 5 + e >= 6. If e = 5
  and some b in W\{u} has alpha_ub != 5, then gcd(lambda_v, lambda_b) = 1: y_v = y_b = 1 gives >= 6. If e = 5 and all four
  W-entries are 5: if c != 3, all fifteen pairwise label gcds equal exactly 5, so no allowed set has six elements
  (a 6-set needs a pair with gcd >= 6) and y = 1/5 on all six is feasible with val = 5 + c/5 > 5, contradicting
  Corollary 5/6. If c = 3, every v in W\{u} has alpha_vu = 5, and the same case analysis at v forces all W-entries of v
  to be 5 and alpha_vz = 3, alpha_vt = 5. So alpha = 5 on all W-W and W-t pairs and alpha_wz = 3 (w in W). Then
  alpha* = 1 on all W-W and W-t pairs and alpha*_uz <= 3. In the inverted configuration at u the labels w_v (four
  W-neighbours) are coprime to all labels, and lambda*_t = 3^A w_t, lambda*_z = 2^E 5^Bz alpha*_uz w_z share a prime only if
  alpha*_uz = 3. Put y = 1 on the four W-neighbours and y_z = 1, plus y_t = 1 if alpha*_uz != 3: val >= 4 + 3 or
  >= 4 + 1 + 1, contradicting LFC (d) for the inverted configuration.
- 5-marker on t (Bt >= 1, Bz = 0): as in the case Bz = 0.

*(b) No t-five.* Suppose e = 5; by (a) every W-entry lies in {1,2,3,4}. An entry a in {1,2,4} gives a label coprime to
lambda_t = 3^A 5^(Bt+1) w_t: y_t = y_b = 1 gives >= 6. So all four W-entries are 3. If lambda_z is coprime to lambda_t
(c != 3 and Bz = 0): y_t = y_z = 1 gives >= 6. Otherwise:
- c in {1,2}, Bz >= 1: lambda_z shares only 5 with lambda_t and nothing with the threes; y = 1/3 on the threes and on t,
  y_z = 2/3 is feasible ({z,t}: 1; {t,3,3}: 1; z never with a three) and val = 4 + 5/3 + 2c/3 > 5.
- c = 3, Bz = 0: all six labels have pairwise gcd 3; y = 1/3 on all: val = (12 + 3 + 5)/3 > 5.
- c = 3, Bz >= 1: gcd(lambda_z, lambda_t) = 15, all other pairs 3. Allowed sets: size <= 3, and 4-sets containing z and t
  (5-sets would contain a 4-subset missing z or t with all gcds 3). y = 1/3 on the threes and on t, y_z = 0:
  val = 4 + 5/3 > 5.
Each case contradicts Corollary 5/6 or LFC (d). The inverted configuration is in the same setting (E6). QED

## 3. Lemma R3 (rows with a W-three) [NEW]

Fix u in W and an orientation x; write the x-row as W-entries a_v (v in W\{u}), c = x_uz, e = x_ut. By D23-MIX and NO5:
a_v in {1,2,3,4}, c in {1,2,3}, e in {1,2,3,4}; no entry is 5, so no 5-marker enters any label gcd at u. Label gcds:
(a,a') -> gcd(a,a'); (z,a) -> 1, 2, [3 if c = 3 else 1], 2^min(E + v2 c, 2) for a = 1, 2, 3, 4; (t,a) -> 1,
[2 if e even else 1], 3, gcd(e,4) for a = 1, 2, 3, 4; (z,t) -> 2^min(E + v2 c, v2 e) * 3^[c = 3]. Let k3 be the number
of W-entries equal to 3 (R3 their set).

**Statement.** If k3 >= 1 then c = 3, e = 2 and the W-part is one of (3,3,3,3), (3,3,3,1), (3,3,1,1), (3,3,2,2)
(survivors S1-S4). For each survivor there is a feasible y with val(y) = 5 such that **every allowed set containing t of
weight 1 contains z**. Consequently (Corollary 5/6, equality clause) every fibre at u (orientation x) that meets the
coset of t also meets the coset of z.

*Proof.* Every listed weight vector is feasible by the stated reasons; "standard weights" are those of the ROW-U class
analysis on unmarked neighbours (E8: N such neighbours with entries in {1,2,4} contribute >= min(N, 4)).

(1) **c in {1,2}.** Threes are compatible only with threes and t.
- k3 = 1 (R3 = {a}): y_a = 1, standard weights on the other three (>= 3), y_z = y_t = 0: val >= 6.
- k3 = 2, others b1, b2 in {1,2,4}; y = 1/2 on R3 (value 3), y_t = 0. (1,1): y = 1 on the ones and y_z = 1 (z shares
  nothing with ones or threes): val >= 3 + 2 + 1. (1,b), b in {2,4}: y = 1 on both: val >= 3 + 1 + 2. (2,2): y = 1/2 on
  both and y_z = 1/2 ({z,2,2} has all gcds 2, not allowed): val = 5 + c/2. (2,4), (4,4): y = 1/2 on the pair: >= 3 + 3.
- k3 = 3, other b: y = 1/3 on R3 and on t (value 3 + e/3; R3 cup {t} has pairwise gcds 3, so at most three per set).
  b = 1: y_b = 1, and y_z = 1 if e is odd (z then isolated), y_z = 2/3 if e is even (z partners only t): val >= 5 + 1/3.
  b in {2,4}, e odd: b shares nothing with t or the threes; y_b = 1: val >= 3 + 1/3 + 2. e = 2, b = 2: y_b = 2/3,
  y_z = 1/3 ({b,z,t} has all gcds 2, not allowed; {b,t}, {b,z} weigh 1): val = 5 + c/3. e = 2, b = 4 or e = 4: y_b = 2/3,
  y_z = 0: val >= 3 + 2/3 + 8/3 or >= 3 + 4/3 + 4/3.
- k3 = 4: y = 1/3 on R3 and t (value 4 + e/3); y_z = 1 (e odd) or 2/3 (e even): val > 5.
(2) **c = 3.** Then R3' := R3 cup {z, t} has pairwise gcds 3, except gcd(z,t) = 3 (e odd), 6 (e = 2), 6 or 12 (e = 4).
- k3 = 1: y_a = 1, standard weights on the other three, y_z = y_t = 0: val >= 6.
- k3 = 2, e odd: y = 1/3 on R3' (no allowed 4-set): value 3 + e/3. Others: (1,1): 1 each, val > 5. (1,b): y_b = 2/3 (b
  partners only z): val >= 3 + 1/3 + 1 + 4/3. (2,2): y = 1/2 each ({2,2,z} not allowed; {b,z} = 5/6): val >= 3 + 1/3 + 2.
  (2,4): E = 1: {2,4,z} not allowed, y = 1/2 each: val > 5; E >= 2: y_4 = 2/3, y_2 = 0: val >= 3 + 1/3 + 8/3. (4,4):
  y = 1/3 each ({4,4,z} weighs 1): val >= 3 + 1/3 + 8/3.
- k3 = 2, e even: R3' is itself allowed (z-t gives the pair >= 4). y = 1/2 on R3, 0 on z, t (value 3). (1,b) with b in
  {2,4}: y = 1 on both: val >= 6. (2,4), (4,4): y = 1/2 on the pair: >= 6. (1,1): R3' contributes at most max(3, e) and the
  ones 2; e = 4: y_t = 1, ones 1: val = 6; e = 2: survivor **S3**. (2,2): e = 4: y = (R3: 1/4, 1/4; z: 0; t: 1/2; twos:
  1/2, 1/2) is feasible (R3' = 1; {b,z,t} = 1; {b1,b2} = 1; {b1,b2,z}, {b1,b2,t} not allowed) with val = 11/2; e = 2:
  survivor **S4**.
- k3 = 3, e odd: y = 1/3 on R3' (five elements, pairwise gcd 3): value 4 + e/3; the other b adds 1 (b = 1) or >= 4/3
  (b in {2,4}, y_b = 2/3, partner z only): val > 5.
- k3 = 3, e even: allowed sets in R3' are the triples and the 4-sets containing z and t. b = 1, e = 4: y = (R3: 1/3;
  t: 1/3; z: 0; b: 1): val = 3 + 4/3 + 1 > 5; b = 1, e = 2: survivor **S2**. b in {2,4}: b partners z and t only, and
  {b, z, t} is allowed; y = (R3: 1/3; z: 1/3; t: 0; b: 2/3): val >= 3 + 1 + 4/3.
- k3 = 4, e odd: y = 1/3 on all six: > 5. e = 4: y = (R3: 1/3; t: 1/3; z: 0): val = 4 + 4/3. e = 2: survivor **S1**.
(3) **The survivors and their weights** (all with c = 3, e = 2; gcd(z,t) = 6):
- S1 (3,3,3,3): y = 1/3 on the threes and z, y_t = 0. Feasible (triples weigh <= 1; 4-sets {z,t,a,a'} weigh 1). val = 5.
  A set containing t of weight 1 must contain three elements of weight 1/3, i.e. be {z,t,a,a'} (the only allowed 4-sets
  contain z and t).
- S2 (3,3,3,1): the same weights plus 1 on the one (isolated). val = 5; t never shares a fibre with the one, so the same
  conclusion.
- S3 (3,3,1,1): y_z = 1, y = 0 on the threes and t, 1 on the ones. Feasible (R3' weighs 1). val = 3 + 2 = 5. Sets with t
  lie in R3' and weigh 1 iff they contain z.
- S4 (3,3,2,2): y = (threes: 1/4, 1/4; z: 1/2; t: 0; twos: 1/2, 1/2). Feasible: R3' weighs 1; {b,z,t} weighs 1; {b1,b2}
  weighs 1; {b1,b2,z}, {b1,b2,t} are not allowed (all gcds 2); twos and threes are incompatible. val = 3/2 + 3/2 + 2 = 5.
  Sets containing t of weight 1: R3' and {b,z,t}; both contain z.
By Corollary 5/6, val(y) = 5 forces every fibre meeting the coset of t to carry weight 1, hence to contain z. QED

**Corollary R3.** (i) If c = x_uz in {1,2}, the x-row at u has no W-three. (ii) W3 subset T and W3* subset T*.
(iii) Every u in W3 has alpha_ut = 2 and no W-entry 4 (similarly for W3*).

## 4. Lemma TR (transfer) [NEW]

For u in W: every left U_u-coset meeting g_tU_t meets g_zU_z **iff**, after normalising g_z = 1,
D_t := U_z g_t U_t is contained in X_u := U_zU_u. In that case D_t cap D_u is empty, where D_u := U_z g_u U_u.

*Proof.* Both statements are invariant under a common left translation, so take g_z = 1. The union of the left
U_u-cosets meeting g_tU_t is g_tU_tU_u, and those meeting U_z form U_zU_u. If g_tU_tU_u subset U_zU_u then
D_t = U_z g_t U_t subset U_z g_t U_t U_u subset U_zU_zU_u = U_zU_u. Conversely, if U_z g_t U_t subset U_zU_u then
g_tU_tU_u subset U_z g_t U_t U_u subset U_zU_uU_u = U_zU_u. Finally D_u cap X_u is empty (VFC (V1)). QED

## 5. Lemma CC (centre count) [NEW]

If D_t cap D_u is empty for every u in T* (apex z, g_z = 1), there is no such configuration.

*Proof.* VFC at z with q = alpha* (INV (b)): mu(D_j) = alpha*_zj/6, local indices d_u = alpha*_zu w_u (u in W),
d_t = alpha*_zt 3^A 5^Bt w_t, and alpha*_zu in {1,2,3}, alpha*_zt in {1,2} (D23-MIX). Pairwise gcds: 3 inside T* and
between T* and t; 1 between T* and O* := W \ T*; gcd(alpha*, alpha*') in {1,2} inside O* cup {t}. Weights: y = 1/3 on T*,
y = 1 on vertices of O* cup {t} with alpha*_z. = 1, y = 1/2 on those with alpha*_z. = 2. For a right coset R of U_z,
S_R := {j : R subset D_j} is allowed (V3) and, by hypothesis, never contains t together with an element of T*. If S_R
meets T*, then S_R subset T*, of size <= 3 (Sun(4)): weight <= 1. Otherwise S_R lies in O* cup {t}; an element with
local index of alpha*-value 1 is alone (Sun(2)), and elements of value 2 have pairwise gcd 2, so at most two (Sun(3)):
weight <= 1. Hence sum_j y_j mu(D_j) <= mu(union of the D_j) <= 1 - 1/n_z (V4). But
sum_j y_j mu(D_j) = |T*|/6 + |O*|/6 + 1/6 = 1. Contradiction. QED

## 6. Theorem K7-D23-RICH [NEW]

**In (a1) there is no configuration in which every u in T* lies in W3 (has some v in W with alpha_uv = 3). By
inversion, there is none in which every u in T lies in W3*.** (Arbitrary groups via R0, which preserves alpha and
alpha*: LFC verdict item 6.)

*Proof.* Let u in T*. As u in W3, the alpha-row at u has a W-three, so by Lemma R3 every left U_u-coset meeting g_tU_t
meets g_zU_z. By Lemma TR, D_t cap D_u is empty. This holds for every u in T*, and Lemma CC gives the contradiction. The
second statement is the first for the inverted configuration (INV (a), E6: same z, t, markers; alpha and alpha*,
T and T*, W3 and W3* exchange). QED

The abstract pattern of `K7-D23-obstruction-v1.md` (sha256 9a6d1e609c3ed95e2dc77ffcb5fada5b35b1beded4593662ce4e7396fc514863;
navigation only) has T* = W = W3 and is therefore not realisable.

## 7. Lemma TZ (triangles at z) [NEW]

(i) If u in T and v in W \ T, then alpha_uv in {3, 4}. (ii) If T != W, then W3 is empty and alpha_uv = 4 for all
u in T, v in W \ T. (iii) T = W or T* = W. (All statements also hold with alpha, T, W3 replaced by alpha*, T*, W3*.)

*Proof.* (i) Triangle {z,u,v}: g = gamma = 6, ell_z = r_z = 2^E 5^Bz w_z, ell_u = w_u, ell_v = w_v. With s := alpha_zv in
{1,2} and x := alpha_uv (<= 4 by NO5): tau_min is a multiple of lcm(3, s) = 3s (the terms alpha_zu/gcd(3, w_v) = 3 and
alpha_zv/gcd(s, w_u) = s), while tau_max <= x s (apex z: opposite x, adjacent min(3, s) = s). x = 1 or 2 gives
tau_max <= 2s < 3s. So x in {3, 4}. (ii) Let u in T, v in W \ T. If alpha_uv = 3, then v in W3 and Corollary R3 (ii)
gives v in T, false; so alpha_uv = 4. Every u in T then has a W-entry 4, so u is not in W3 (Corollary R3 (iii));
with W3 subset T this gives W3 empty. (iii) Otherwise (ii) holds for alpha and for alpha*: alpha = 4 on all pairs of
T x (W\T) and alpha* = 4 on all pairs of T* x (W\T*). No pair has alpha = alpha* = 4 (INV). The complete bipartite
graph on T, W \ T (both non-empty) is connected and spans W, so none of its edges crosses (T*, W \ T*) only if T* is
empty or W; |T*| >= 3 gives T* = W, a contradiction. QED

## 8. Lemma LZ (light fibres at z) [NEW]

If T = W, put s := alpha_zt and T*_W := [G : intersection of g_uU_ug_u^-1 (u in W)]. Then v2(T*_W) >= 2, and if s = 2
then E >= 2 and v2(T*_W) >= 3. In particular the graph Gamma*_1 := {uv subset W : alpha*_uv = 1} is not connected on W.
(With alpha and alpha* exchanged when T* = W.)

*Proof.* Normalise g_z = 1 and let W* be the intersection above. As in Corollary 5/6, W*U_z is a union of left
U_z-cosets containing U_z and meeting no g_uU_uU_z (u in W); its fibres carry at most the piece of t. Let M be their
number; by G0, M >= n_z / g with g := gcd(n_z, T*_W). At z the labels are 3 w_u (u in W) and s 3^A 5^Bt w_t: all pairwise
gcds 3, so every fibre holds at most three pieces (Sun(4)), and at most two W-pieces if it holds t. Counting W-pieces
(t_u = n_z/2 each) and t-pieces (t_t = n_z s/6, at most M - 1 of them in W*U_z, as U_z holds none):
5 n_z/2 <= 3(n_z - M) - (n_z s/6 - (M - 1)), i.e. M <= n_z (3 - s)/12 - 1/2. Hence g > 12/(3 - s). Now
T*_W = 6 (product of the w_u) alpha*_(j1 j2) k_3 k_4 k_5 along any order of W (FG7 chain with V_j = g_jU_jg_j^-1), with
k_m <= alpha*_(e j) <= 4 for every earlier j (NO5); so 5 does not divide T*_W, the prime-to-30 part is coprime to w_z,
and g = 3 * 2^min(1 + E, v2(T*_W)). g > 6 (s = 1) or g > 12 (s = 2) gives the first two claims. If Gamma*_1 were
connected, order W along a spanning tree starting with an edge of Gamma*_1: alpha*_(j1 j2) = 1 and every k_m <= 1, so
v2(T*_W) = 1, contradicting v2(T*_W) >= 2. QED

## 9. Scope, exact residue and limits

- **Excluded (if accepted):** every (a1) configuration with T* subset W3, and every one with T subset W3*; any
  exponents; arbitrary groups.
- **Residue of (a1) after this file** (every surviving configuration satisfies all of): T = W or T* = W (TZ (iii));
  some u in T* has an alpha-row without a W-three and some u' in T has an alpha*-row without a W-three (Theorem);
  if T != W then W3 = empty and alpha = 4 on T x (W\T) (and dually); if T = W then Gamma*_1 is disconnected and
  alpha_zt = 2 forces E >= 2 (and dually); no alpha or alpha* equals 5 on W-W or W-t pairs; every row with a W-three is
  one of S1-S4 with e = 2. Rows without a W-three (W-entries in {1,2,4}) are NOT classified here; several of them pass
  Corollary 5/6 while putting zero weight on z in every optimal y, so Lemma TR cannot be invoked for them. **Exact
  missing lemma:** for u in T* whose alpha-row has no W-three, show D_t cap D_u = empty (or replace Lemma CC by a count
  that tolerates such u).
- **Not covered:** (a2) (5-marker on a third vertex p); K6.2*; full Sun(7).
- Verification boundary: written, single author, unreviewed. Requested checks: FG7 ordering (marked first) and the
  k-bound; the equality clause of Corollary 5/6; NO5 (a) last case (propagation and the inverse row); every weight in R3;
  Lemma CC's weight table; TZ (i) tau bounds; LZ count. No novelty, Lean or human-review claim.
