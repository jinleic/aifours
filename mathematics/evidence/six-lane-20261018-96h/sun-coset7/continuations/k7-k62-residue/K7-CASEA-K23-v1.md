# K7-CASEA-K23: in (a1) Case A only the K_{2,3} structure survives; in Case B every t-a entry is forced

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:26:58-0700.
- **Owner:** Sun7K62Successor. Single author, unreviewed. No computation was run; no probe is a premise.
- **Status:** CANDIDATE, **conditional** on the unreviewed candidates `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf: section 0
  triangle rule and two/four classes, Corollary W3, Lemma E3, Lemma PFG-t with Corollary L, Lemma B, Theorem CASEB),
  `K7-TC-v1.md` (cc48340d...e117: Lemma TC, rows R1 (every E >= 1) and R3, Lemma FG-V, Theorem K7-TC-B) and
  `K7-TC-A22-v1.md` (9ebec279...1b46b41: the all-(2,2) case), all read through the overlay `K7-A1-A2-delta-erratum-v1.md`
  (sha256 0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e). (a1) is NOT excluded; full Sun(7) remains
  OPEN.
- **Accepted imports:** RICH (verdict sha256 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0):
  Corollary 5/6 with its equality clause, FG7, NO5; D23-MIX; LFC, INV, VFC (V1)-(V4), L1; R0. Direct Sun instances:
  Sun(2), Sun(3) (Corollary L enters only through "at least two entries 4", which is Sun(5)-free); transitive closure as
  in A1-STRUCT section 0 (as amended).

## 0. Setting and conventions

(a1), **Case A**: T = T* = W. By Corollary W3, E3 and NO5 every W-W and W-t entry of alpha and alpha* lies in {1,2,4},
and x_uz = 3 for every u in W and x in {alpha, alpha*}. F := {uv in W : alpha_uv = 4}, F* := {uv : alpha*_uv = 4}
(disjoint, INV), N := the pairs of W in neither; d(u), d*(u) are the F- and F*-degrees in W; P := {u : alpha_tu = 4},
P* := {u : alpha*_tu = 4} (disjoint). A row is written (W-multiset | e) with e = x_ut (x_uz = 3 understood); its fours,
twos, ones are its W-entries 4, 2, 1. C^x is the configuration whose alpha-matrix is x. In C^x the rows at u are x-rows,
and at an apex a in W the VFC sets D_j = D_j^(a) have measure x*_aj/6 and local indices x*_aj r_j (INV (b)); **Lemma
FG-V** gives mu(union of the D_j^(a)) <= 5/6 for a in W, in C^alpha and in C^alpha*. "u is single-x-four" means
d(u) = 1 (x = alpha), resp. d*(u) = 1 (x = alpha*). L_j denotes the union of the fibres at u meeting j's coset.

## 1. Tools

**(R) Rows** (x in {alpha, alpha*}, u in W; values in units 1/6 are <= 5 by Corollary 5/6):
- (R-a) Every x-row has a W-four (otherwise it has >= 3 entries <= 2 and Lemma B forces exactly one four), so d, d* lie
  in {1,2,3}. A single-four row is **R3 = (2,2,2,4 | 4)** or **R3' = (1,2,2,4 | 4)** and then E >= 2 (Lemma B); hence a
  single-alpha-four vertex lies in P, a single-alpha*-four vertex in P*, and (d, d*) = (1,1) is impossible (INV on t-u).
  Every row has at most one entry 1: (1,1,4,4) has value >= 6 (y = 1 on the ones, 1/2 on the fours), and the other
  multisets with two ones are excluded by Lemma B or by having no four.
- (R-b) **Twin rule.** x_uv = 1 forces x_uw = x_vw for every other w in W cup {t} (triangle rule of A1-STRUCT section 0;
  the ell's of W and t are odd); so x-twins have the same F_x-neighbourhood. In particular, **if all F-neighbourhoods
  (resp. F*-neighbourhoods) of distinct vertices differ, alpha (resp. alpha*) has no W-entry 1.**
- (R-c) **Rigid rows.** For each row below two feasible weight vectors of value 5 are displayed; by the equality
  clause every occupied fibre C at u has weight 1 under both, which gives the stated containment.
  - R1 = (2,2,4,4 | 2) (K7-TC, every E >= 1) and **R1- = (2,2,4,4 | 1)** (y = (f 1/2, f' 1/2, t 1) and
    (s 1/2, s' 1/2, f 1/2, t 1); t's label 3^A w_t meets only z): **L_f = L_f'** for the two fours.
  - **R5 = (1,2,4,4 | e)** and **R4 = (1,4,4,4 | e)**, e in {2,4} (y_i = (o 1, f_i 1); o's label is prime to all): every
    occupied fibre C with o not in S_C contains every four; so **L_j subset L_f for every four f and every j != o**.
  - **R6 = (2,4,4,4 | 1)** (y_i = (f_i 1, t 1)): every occupied fibre other than those with S_C in {{t}, {t, z}}
    contains all three fours; so **L_s subset L_f** for the two s and every four f.
  - R3 (K7-TC) and **R3'** (y = (o 1, f 1/2, s 1/2, s' 1/2) and (o 1, s 1/2, s' 1/2, t 1); {f,s,s'}, {t,s,s'}, {z,s,s'} have
    all gcds 2; {f,t,s}, {z,t,s}, {z,f,s}, {z,f,t,s} are allowed of weight 1 (E >= 2)): **L_f = L_t and L_z subset L_t**.
  - (1,2,4,4 | 1) and (1,4,4,4 | 1) do not occur (y = (o 1, fours 1/2 resp. 1/3, t 1) has value 6). The remaining rows,
    R2 = (2,2,4,4 | 4) and (2,4,4,4 | e) with e in {2,4}, are called slack; nothing is claimed for them.

**Lemma K3 (transfer kill) [NEW].** If u in W has a rigid x-row forcing L_j subset L_a (a in W \ {u}, j != u), then in
C^x at apex a, D_j cap D_u = empty (Lemma TC), so by Lemma FG-V **x*_aj + x*_au <= 5**. In particular x*_aj = 4 and
x*_au >= 2 is impossible.

**Lemma K2 [NEW].** There is no pair (a, s) with a single-x-four and s single-x*-four whose x*-four is a.
*Proof.* s's x*-row is R3/R3' (in C^x*), so L*_a = L*_t at s. At apex a in C^x* the masses are x_at/6 = 4/6 (a's
single-four row has e = 4) and x_as/6 with x_as = 2: x_as <= 2 as x*_as = 4, and x_as = 1 would make s an x-twin of a,
hence single-x-four, of type (1,1). Lemma K3 with x and x* exchanged. QED

**Lemma CL.** If F contains neither K_{1,4} nor K_{2,3} (equivalently Gamma^alpha, the complement of F in W, is
connected), Corollary L in C^alpha gives |P*| >= 2. Dually, if F* contains neither, |P| >= 2.

## 2. Degree types

Let n_ij be the number of W-vertices of type (d, d*) = (i, j); by (R-a) the types are (1,2), (1,3), (2,1), (3,1),
(2,2). Parity of the degree sums gives: n12 + n13 + n31 and n13 + n21 + n31 are even.
**Lemma S.** (i) If n31 >= 1 then n12 = n13 = 0; dually, n13 >= 1 implies n21 = n31 = 0. (ii) Up to inversion
(alpha <-> alpha*) and apart from the all-(2,2) case, the type vector is one of: without 3-vertices,
(n12, n21, n22) in {(2,0,3), (2,2,1), (4,0,1)}; with 3-vertices, (n31, n21, n22) in {(2,0,3), (2,2,1), (4,0,1)}.
*Proof.* (i) Let v be of type (3,1) with alpha*-four g. If d(g) = 1, the pair (g, v) contradicts K2. If an
alpha-four-neighbour a of v had d(a) = 1, its alpha-four would be v, and (v, a) contradicts K2 (with x = alpha*). So all
four other vertices have d >= 2, i.e. none is of type (1,2) or (1,3). (ii) Enumerate with the parities. QED

## 3. Exclusion of every type vector except one

**(S-a) (4,0,1).** F has degrees (2,1,1,1,1), i.e. F = P3 + P2, which contains neither K_{1,4} nor K_{2,3}; CL gives
|P*| >= 2. The four single-alpha-four vertices lie in P (R-a), so |P*| <= 1. Contradiction. (0,4,1): by inversion.

**(S-b) (2,0,3).** F* is 2-regular, hence a 5-cycle; F has four edges inside the complementary 5-cycle, hence is a path
u0 - a - b - c - u1, F* = {u0 b, u0 c, a c, a u1, b u1} and N = {u0 u1}. All F- and all F*-neighbourhoods differ, so (R-b)
there are no W-entries 1. So u0, u1 have R3 alpha-rows (fours a, c), alpha_tu0 = alpha_tu1 = 4, and the t-triangle
(alpha_tu1, alpha_u1a, alpha_ta) = (4, 2, alpha_ta) excludes alpha_ta = 1. a's alpha*-row is (2,2,4,4 | alpha*_ta) with fours
c, u1; if alpha*_ta is 1 or 2 it is R1-* or R1*, so L*_c = L*_u1 at a, and at apex u1 in C^alpha* the masses
alpha_u1c = 4 and alpha_u1a = 2 contradict K3. So alpha*_ta = 4, alpha_ta = 2, and a's alpha-row (fours u0, b; twos c, u1)
is R1: L_u0 = L_b at a; at apex b in C^alpha the masses alpha*_bu0 = 4 (u0 b in F*) and alpha*_ba = 2 contradict K3.
(0,2,3): by inversion.

**(S-c) (2,2,1) without 3-vertices.** Types A1, A2 = (1,2); B1, B2 = (2,1); C = (2,2). C has no N-pair, A's and B's one
each. F has degrees (1,1,2,2,2): a triangle on {B1, B2, C} plus the edge A1A2, or a path with ends A1, A2.
- Triangle: C's two non-F pairs are A1C, A2C, so F* = {A1C, A2C, A1B1, A2B2}, N = {A1B2, A2B1} (up to B1 <-> B2). A1 is
  single-alpha-four and B1 single-alpha*-four with alpha*-four A1: K2.
- Path A1 - B1 - C - B2 - A2: either F* = {A1C, A2C, A1A2, B1B2}, N = {A1B2, A2B1}: B1 is single-alpha*-four and A1 is
  single-alpha-four with alpha-four B1: K2 (x = alpha*); or F* = {A1C, A2C, A1B2, A2B1}, N = {A1A2, B1B2}: B2 is
  single-alpha*-four with alpha*-four A1 and A1 is single-alpha-four: K2.
- Path A1 - C - B1 - B2 - A2 (the mirror position is symmetric): F* = {CB2, CA2, A1B1, A1A2}, N = {A1B2, A2B1}: B1 is
  single-alpha*-four with alpha*-four A1 and A1 is single-alpha-four: K2.

**(S-d) (n31, n21, n22) = (2,0,3).** N is empty and F* has degrees (1,1,2,2,2): a path v1 - x - y - w - v2 (v1, v2 the
3-vertices) or a triangle {x, y, w} plus the edge v1 v2.
- Path: all F- and F*-neighbourhoods differ, so there are no W-entries 1. x's alpha-row (fours w, v2; twos v1, y) is
  rigid unless alpha_tx = 4; if rigid, L_w = L_v2 at x, and at apex w in C^alpha the masses alpha*_wv2 = 4 (w v2 in F*)
  and alpha*_wx = 2 contradict K3. So alpha_tx = 4, hence alpha*_tx <= 2 and x's alpha*-row (fours v1, y; twos w, v2) is
  R1* or R1-*: L*_v1 = L*_y at x, and at apex y in C^alpha* the masses alpha_yv1 = 4 (y v1 in F) and alpha_yx = 2
  contradict K3.
- Triangle plus edge: F = K_{2,3}; see section 4.

**(S-e) (n31, n21, n22) = (2,2,1).** Let b1, b2 be the (2,1)-vertices, c the (2,2)-vertex; N = {b1 b2}, and F* is a path
of length 2 centred at c plus a disjoint edge other than b1 b2.
- F* = {c b1, c b2, v1 v2}: b1's alpha-row has fours v1, v2. If it is not R2 it is R1, R1- or R5 (by (R-c); (1,1,4,4) and
  (1,2,4,4 | 1) do not occur), so L_v1 = L_v2 at b1, and at apex v1 in C^alpha the masses alpha*_v1v2 = 4 and
  alpha*_v1b1 = 2 (no alpha*-twins: N_F*(v1) = {v2}, N_F*(b1) = {c}) contradict K3. So b1's alpha-row is R2 and
  alpha_tb1 = 4; but b1 is single-alpha*-four, so alpha*_tb1 = 4, contradicting INV.
- Otherwise (up to symmetry) F* = {c v1, c b1, v2 b2}: v1, v2, b1, b2 are single-alpha*-four, so |P*| >= 4 and |P| <= 1,
  while F* (three edges) contains neither K_{1,4} nor K_{2,3}, so CL gives |P| >= 2. Contradiction.

**(S-f) (n31, n21, n22) = (4,0,1).** F* = {c v1, c v2, v3 v4} with c the (2,2)-vertex.
- c's alpha-row (fours v3, v4; twos v1, v2): if it is not R2, L_v3 = L_v4 at c, and at apex v3 in C^alpha the masses
  alpha*_v3v4 = 4 and alpha*_v3c = 2 contradict K3. So alpha_tc = 4.
- v1's alpha-row is (2,4,4,4 | alpha_tv1) (fours v2, v3, v4; alpha_v1c = 2 as v1, c are not alpha-twins), with
  alpha_tv1 <= 2 (v1 is single-alpha*-four). If alpha_tv1 = 1 it is R6: L_c subset L_v2 at v1, and at apex v2 in
  C^alpha the masses alpha*_v2c = 4 (c v2 in F*) and alpha*_v2v1 = 2 contradict K3. So alpha_tv1 = 2; likewise
  alpha_tv2 = 2.
- v3's alpha-row has fours v1, v2, c and alpha_v3v4 in {1,2}. If alpha_v3v4 = 1 it is R4 with e = alpha_tv3 = 2 (e <= 2,
  e != 1): L_t subset L_v1 at v3, and at apex v1 in C^alpha the masses alpha*_v1t = 4 and alpha*_v1v3 = 2 contradict K3.
  If alpha_v3v4 = 2 and alpha_tv3 = 1 it is R6: L_c subset L_v1, and at apex v1 the masses alpha*_v1c = 4,
  alpha*_v1v3 = 2 contradict K3. So alpha_tv3 = 2; likewise alpha_tv4 = 2.
- Hence P = {c}; but F* (three edges) contains neither K_{1,4} nor K_{2,3}, so CL gives |P| >= 2. Contradiction.

## 4. Theorem K7-CASEA-K23 (conditional) [NEW]

**In (a1) Case A, every configuration not of the all-(2,2) type (excluded by K7-TC-A22) has, up to inversion
(alpha <-> alpha*), F = K_{2,3} with two-side {v1, v2} and three-side {x, y, w}, F* = {xy, yw, wx, v1 v2}, N empty, and
moreover: E >= 2; alpha* has no W-entry 1; the alpha-rows of x, y, w are R2 = (2,2,4,4 | 4), so alpha_t = 4 on {x, y, w}
and alpha = 2 inside {x, y, w}; alpha_v1v2 = 2; alpha*_tv1 = alpha*_tv2 = 4 and alpha_tv1, alpha_tv2 lie in {1, 2}, not
both 1; t's alpha-row on W is 44412 or 44422.**

*Proof.* Sections 2-3 leave only (n31, n21, n22) = (2,0,3) with F* = triangle + edge (or its inverse), i.e. F = K_{2,3}.
E >= 2 and alpha*_tv_i = 4 by (R-a) (v1, v2 are single-alpha*-four). N_F*-neighbourhoods are distinct, so alpha* has no
entry 1 on W, and alpha* = 2 on F. If x's alpha-row (fours v1, v2) is not R2, then L_v1 = L_v2 at x, and at apex v1 in
C^alpha the masses alpha*_v1v2 = 4 and alpha*_v1x = 2 contradict K3; so it is R2, likewise for y, w. If alpha_v1v2 = 1,
v1 and v2 are alpha-twins with alpha-rows R4 = (1,4,4,4 | 2) (alpha_tv_i <= 2 and != 1), so L_z, L_t subset L_x at v1 and
at v2; at apex x in C^alpha the masses are y, w: 4/6, v1, v2: 2/6, z: 3/6, and D_z is disjoint from D_v1 and D_v2. By
Lemma FG-V the part of the union outside D_z has measure <= 2/6, so it equals D_v1 = D_v2; y has mass 4/6 > 3/6, so
some coset outside D_z holds y, v1 and v2, whose local indices 4 w_y, 2 w_v1, 2 w_v2 have all pairwise gcds 2 (Sun(3)).
Contradiction; so alpha_v1v2 = 2. Finally F* contains neither K_{1,4} nor K_{2,3}, so Corollary L in C^alpha* puts t's
alpha-row in its list; with entries 4 on {x, y, w} and <= 2 on v1, v2 only 44412 and 44422 remain. QED

## 5. Proposition K7-CASEB-T (conditional) [NEW]

**In Case B (Theorem CASEB and Theorem K7-TC-B), alpha_ta = 2 and alpha*_ta = 4 for every a in T*.**
*Proof.* v1's alpha-row is R3 (four v2; twos a1, a2, a3), with alpha_tv1 = 4. For a in T*, the alpha*-row of a is
(2,2,4,4 | alpha*_ta) (alpha*_za = 3; fours v1, v2; twos the other two a's, by K7-TC-B). If alpha*_ta is 1 or 2 it is R1-* or
R1*, so L*_v1 = L*_v2 at a, and at apex v1 in C^alpha* the masses alpha_v1v2 = 4 and alpha_v1a = 2 contradict K3. So
alpha*_ta = 4, alpha_ta <= 2, and alpha_ta = 2 (CASEB: alpha_ta in {2, 4}). QED

## 6. Scope

- **Proved here, conditional on the imports in the header:** Lemmas K3, K2, CL, S; the exclusions (S-a)-(S-f); Theorem
  K7-CASEA-K23; Proposition K7-CASEB-T. The (a1) Case-A residue is the K_{2,3} family of section 4 (and its inverse); the
  Case-B residue keeps the data of K7-TC-B with every t-a entry alpha = 2, alpha* = 4.
- **Not covered:** the K_{2,3} family and the Case-B family themselves (no exclusion is claimed; no closure wording);
  (a2) (no transfer to (a2-no5) is claimed here); K6.2*; full Sun(7). No novelty, Lean or human-review claim.
- Requested checks: each (S-*) kill (structure, masses, the K3 transfer orientation); the alpha_v1v2 = 1 count in
  section 4; the use of Lemma FG-V and of R1 for E >= 1 only through the overlay.
