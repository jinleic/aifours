# K62-MK-v2: the O-marked (1,1) part of the K6.2* residue — M5 is empty; M3(1,1) reduces to two t-local residual configurations [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T11:19:33-0700.
- **Author:** SunK62Regimes; single author; written mathematics only. No computation of any kind was run (no compute GO;
  global runtime HOLD respected). **Label of every new claim: CANDIDATE_UNVERIFIED.**
- **Supersedes** the undelivered draft `K62-MK-v1.md` (sha256 898ad8656961e3b6bd5ab7bea13c0554871d4ddcdefeb7d3b3ac9b4434ea39ab,
  frozen, unchanged). Differences, from my own re-read before delivery: the mapping of the scope items in the next bullet
  (v1 called Corollary 6.5 item (c)); the chain description in the proof of Lemma 3.2 ("t, if t exists and t != v"). No
  statement, case or argument changes.
- **Frozen scope (written before the derivation):** `K62-MK-SCOPE-v1.md` in this directory, sha256
  12cad4f7e9f7d29c5aa7d7520bda50534b3ecd64702cf4198ff01050ef0ef1bd. Theorem 6.3 is its Theorem M5. Section 7 is its M3(1,1)
  obstruction note with exactly the contents (a)-(d) fixed there: item (d) consists of Theorem 6.4 and Corollary 6.5
  (unconditional sub-case statements); item (c) is section 7 (c).
- **Premises.** Only parent-accepted results are imported (section 1). The pending candidates K62-GS-v1, K62-HD-v1/v2 and
  K62-GX-v1 are **not** imported: every step needed from them is re-proved here in a form valid with markers on O.
- RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`;
  K62 := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon`.

## 0. Setting and notation
**Class K (O-marked (1,1)).** The CAP setting of the accepted CAP-DT verdict (`RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md`,
sha256 84061c6fbdbd9fa834810efa43843024e04c2abce794df28446865ef635234a0): V = {d, i*} disjoint-union O, |O| = 5;
n_d = 2^(e_d) 5^(h_d) w_d, e_d >= 4, e* = 2; n_(i*) = 4 * 3^(f*) 5^(h*) w_*; n_c = 2 * 3^(f_c) 5^(h_c) w_c (c in O); w's pairwise
coprime and coprime to 30; at most one vertex with f >= 2 and at most one with h >= 1; **(alpha_(d i*), alpha*_(d i*)) = (1,1)**;
and **some vertex of O is marked**. Two disjoint sub-classes exhaust K:
- **M5:** the 5-marker is on p in O (h_p >= 1) and no 3-marker is on O. (Then h_d = h* = 0, and K62-E3 Lemma 1 makes the
  orientation automatically (1,1).)
- **M3(1,1):** the 3-marker is on t in O (f_t >= 2, so f* = 1); the 5-marker is on d, on i*, on t, on some p in O minus {t},
  or absent.
**Labels.** For c in O put **ell_c := n_c / 6 = 3^(f_c - 1) 5^(h_c) w_c**: odd, pairwise coprime (one 3-marker, one
5-marker, coprime w's), and coprime to 6 except ell_t (3 divides ell_t). ell°_c := the prime-to-6 part of ell_c (= ell_c for
c != t; ell°_t = 5^(h_t) w_t).

**Families.** For x in {alpha, alpha*}, x' is the other one; the *x-configuration* is (g_jU_j) for x = alpha and the inverted
configuration (g_j^-1 U*_j), U*_j := g_jU_jg_j^-1, for x = alpha*: pairwise disjoint cosets with the same indices, alpha-matrix
x and alpha*-matrix x' (INV (a)-(b) with E6). Phi_j := the subgroup of j in it; [G : Phi_i cap Phi_j] = lcm(n_i, n_j) x_ij.
For non-empty S in V: W_S := intersection of the Phi_j (j in S), T_x(S) := [G : W_S]; for S in O the **raw depth** is
delta(S) := v2 T_x(S). For an O-triple R = {a, b, c}: tau(R) := T_x(R) / lcm(n_a, n_b, n_c); its **type** is its sorted x-values;
R is **deep** if delta(R) >= 4. X^v_j := Phi_vPhi_j. mu(Y) := |Y| / |G| (finite G). L0.1 (old README section 0):
|XY| = |X||Y| / |X cap Y| for subgroups; used with Lagrange; so mu(Phi_iPhi_j) = x_ij / g_ij. For v in O:
**Gamma_y(v) := gcd(n_v, T_y(V minus {v}))**.
**Graphs.** H_x: the graph on O of the pairs with x = 4; n_k(x): number of O-pairs with x = k; an x-4-edge is tight if x' = 2,
non-tight if x' = 1; u(x): number of non-tight x-4-edges; tri(H_x): number of triangles of H_x (O-triples of type (4,4,4)).
For a 4-subset Q of O and e in Q: R_e := Q minus {e}, m_e := min over j in R_e of x_ej.

**Residual instances (M3(1,1) only).**
- An **R1-instance** is (x; a, b) with x a family and a != b in O minus {t} such that x_ta = x_tb = 4, X^t_a = X^t_b and
  x'_ta = x'_tb = 2.
- An **R2-instance** is a family y such that the four O-entries y_tu (u in O minus {t}) of the y-row at t lie in {1, 2}.
- **Hypothesis NR:** the configuration has no R1-instance and no R2-instance. In M5 (no t) NR holds vacuously.

## 1. Imports (parent-accepted; original scopes)
| tag | source (verdict path, sha256, item) | used for |
|---|---|---|
| R0, L0.1 | old README sections 0-1 (`six-lane-20261016/sun-coset7/README.md`); verdict 73a25ba6… | finite reduction; product formula |
| E3-L1, E3-L2, E3-a, E3-C2 | RUN/review/sun7-K62E3-parent-verdict-v1.md `576969dd…bb0f`: K62-E3 Lemma 1, Lemma 2, C2 sub-claim (a) (erratum v2 Z11), Corollary C2; whole class, any markers | orientation in M5; at most two 1s per O-row; O-O values in {1,2,4}; n_4(y) >= 2 n_1(y) + 2 when y'_(d i*) = 1 |
| INV, LFC | RUN/review/sun7-lfc-inv-parent-verdict-v1.md `8621e744…cca18`, items 1-2, 6; K7-LFC-INV-v1 with erratum E1, E3, E6, E7 | inverted configuration, x + x' <= g, q = alpha*, 1 <= alpha <= g - 1; LFC (a)-(d); arbitrary groups |
| L1, VFC | rules-k7-v1.md L1 (T1)-(T3) and §2 (V1)-(V4); RUN-2026-10-16 verdict `73a25ba6…9f35` line 23 | T rule on {d, i*, t}; Lemmas 3.3-3.4 |
| DG-3, DG | SH-DG verdict `cae455c3…ddda` items 3-4 (with both DG errata): triangle table (markers included), Theorem DG (a)/(b), any markers, orientation and four-subset hypothesis | P2 (re-derived); Lemma 6.1 |
| C1, RC-O, CI | CAP-DT verdict `84061c6f…34a0` items 2, 3, 5 (unmarked O-vertex) | cross-checks; Lemmas 3.1-3.3 re-prove them for every v in O |
DT-B/DT-C (accepted only in G) are **not** imported; the facts needed from them are re-proved (Lemmas 3.6-3.7).

## 2. Basic facts (re-proved for K)
**P1.** For an O-pair uv and both families, x_uv lies in {1, 2, 4} (E3-a, any markers) and x_uv + x'_uv <= 6 (INV (b)); so
H_x and H_x' are edge-disjoint, and an x-4-edge is tight or non-tight.

**P2 (triangles; DG-3).** For an O-triple R = {a, b, c}: T_x(R) = 6 ell_a ell_b ell_c tau(R) (the lcm of 6 ell_a, 6 ell_b,
6 ell_c), so delta(R) = 1 + v2 tau(R); tau(R) is a multiple of each of its x-values; tau(R) <= x1 x2 (sorted values). Hence a
deep triple has type (2,4,4) with tau 8 or type (4,4,4) with tau 8 or 16, and delta(R) <= 5.
*Proof.* T_x(R) is divisible by [G : Phi_a cap Phi_b] = 6 ell_a ell_b x_ab, so x_ab divides ell_c tau(R), hence tau(R) (x_ab is a
power of 2, ell_c odd). P4 gives tau(R) / (6 x_ab) = mu(Phi_c(Phi_a cap Phi_b)) <= min(x_ca, x_cb) / 6; minimise over apexes. QED

**P3 (chain step).** (a) For every non-empty S in O, 6 divides T_x(S) and the prime-to-6 part of T_x(S) is the product of
the ell°_j (j in S). (b) For S in O and e in O minus S with **e != t**: gcd(n_e, T_x(S)) = 6, T_x(S + e) = lcm(n_e, T_x(S)) k with
**k = 6 mu(Phi_e W_S) <= x_ej** for every j in S, **k = x_ej iff Phi_e W_S = X^e_j**, and **delta(S + e) = delta(S) + v2 k**;
if m is a power of 2 with k <= m, then v2 k <= v2 m.
*Proof.* Build S one vertex at a time, starting with t if t is in S. Start: n_j = 2 * 3^(f_j) 5^(h_j) w_j has prime-to-6 part
ell°_j and is divisible by 6. Adding e != t to S: n_e and T_x(S) divide T_x(S + e) (Lagrange); write T_x(S + e) =
lcm(n_e, T_x(S)) k. By L0.1, mu(Phi_e W_S) = k / gcd(n_e, T_x(S)). ell_e is coprime to 6 and to every ell°_j (j in S), hence to
T_x(S) by (a); so gcd(n_e, T_x(S)) = gcd(6 ell_e, T_x(S)) = 6 and k = 6 mu(Phi_e W_S). W_S lies in Phi_j, so Phi_e W_S lies in
X^e_j (measure x_ej / 6): k <= x_ej, with equality iff the finite sets coincide. As x_ej <= 4 (P1), k has no prime factor > 3, so
(a) passes to S + e. T_x(S) depends only on S, so (a) holds for every S, and (b) for every S and e != t. Valuations:
v2 n_e = 1 <= v2 T_x(S); and k >= 2^(v2 k). QED

**P4 (apex identity).** For an O-triple {a, b, c}: mu(Phi_b(Phi_a cap Phi_c)) = tau({a, b, c}) / (6 x_ac); hence if x_ba = x_bc = 4
and tau = 4 x_ac, then X^b_a = X^b_c. *Proof.* L0.1: T_x({a,b,c}) / (n_b [G : Phi_a cap Phi_c]) = 6 ell_a ell_b ell_c tau /
(6 ell_b * 6 ell_a ell_c x_ac) (this is L1 (T3), gamma_b = 6). Equal measure 4/6 with inclusion gives the equality. QED
*Instances:* (2,4,4) with tau 8 at the apex opposite the 2-edge; (4,4,4) with tau 16 at each apex.

## 3. Fibre lemmas with explicit vertex conditions
**3.1 Lemma RC (light fibres; re-proved, any vertex).** For a family x and v in V, every y >= 0 on V minus {v} feasible for
the lambda^x-allowed sets at v (LFC (c); lambda^x_j = n_j x_vj / g_vj) satisfies sum_(j != v) y_j x_vj / g_vj <=
1 - 1 / gcd(n_v, T_x'(V minus {v})).
*Proof.* x = alpha: translate so that g_v = 1 (all U*_j are conjugated by one element; U*_v = U_v). For j != v, L_j := g_jU_jU_v is
the union of the t_j = n_v alpha_vj / g_vj fibres (left U_v-cosets) meeting g_jU_j (LFC (a)-(b)). Put W' := intersection of the
U*_j (j != v), T := [G : W'] = T_alpha*(V minus {v}). If wu lies in L_j (w in W', u in U_v), then w lies in L_jU_v = L_j; with
w = g_j a g_j^-1 (a in U_j) we get g_j^-1 in U_jU_v, i.e. g_j in U_vU_j, so g_jU_j meets U_v = g_vU_v: impossible. So the
M := [W' : W' cap U_v] fibres inside W'U_v meet no g_jU_j, and M = [G : W' cap U_v] / T >= lcm(n_v, T) / T = n_v / gcd(n_v, T).
Every other fibre F has S_F allowed (LFC (c)), so sum_(j in S_F) y_j <= 1; hence sum_j y_j t_j <= n_v - M. Divide by n_v.
x = alpha*: apply this to the inverted configuration (its conjugated family is (U_j)). QED (RC-O is the case v unmarked.)

**3.2 Lemma GR (granularity at O-vertices).** Let y be a family. (a) If v in O and v != t, then Gamma_y(v) = 6. (b) In M3(1,1):
Gamma_y(t) = 6 iff 9 does not divide T_y(V minus {t}); and if y_(e i*) <= 2 for every e in O minus {t}, then 9 does not divide
T_y(V minus {t}). (c) In M3(1,1): if y_(e i*) = 3 for some e in O minus {t}, then 9 divides T_y(V minus {t}), so Gamma_y(t) >= 18.
*Proof.* Chain for V minus {v}: d, i*, then t (if t exists and t != v), then the other O-vertices. T_y({d, i*}) =
lcm(n_d, n_(i*)) y_(d i*) = lcm(n_d, n_(i*)) (orientation (1,1)); it is divisible by 3. Adding an O-vertex e: T_(m+1) =
lcm(n_e, T_m) k with k / gcd(n_e, T_m) = mu(Phi_e W_m) <= mu(Phi_e Phi_d) = 1/2 and <= mu(Phi_e Phi_(i*)) = y_(e i*) / 6. Here
gcd(n_e, T_m) = 6: the 2-part is 2; the 3-part is 3 (for e = t added third, v3 T_2 = f* = 1; for e != t, f_e = 1); the 5-part is
1 (if h_e >= 1 then e is the only 5-marked vertex, and no earlier factor or k contributes 5, since every k <= 3); the w-part is
1 (inductively the prime-to-30 part of T_m is the product of the included w's). So every k <= 3, and, for e != t, k <= y_(e i*).
(a) gcd(n_v, T_y(V minus {v})): 2-part 2, 3-part 3 (f_v = 1), 5-part 1 (if h_v >= 1, no other factor has 5), w-part 1: equal to 6.
(b) For v = t the chain adds only vertices e != t, so v3 T_y(V minus {t}) = 1 + sum of v3 k, and Gamma_y(t) =
2 * 3^(min(f_t, v3 T)) (5- and w-parts trivial as in (a)); since f_t >= 2 this is 6 iff v3 T = 1. If every y_(e i*) <= 2, every k <= 2.
(c) [G : Phi_e cap Phi_(i*)] = lcm(n_e, n_(i*)) * 3 has 3-adic valuation max(f_e, f*) + 1 = 2 and divides T_y(V minus {t}). QED

**3.3 Lemma CI* (re-proved at any O-vertex with granularity 6).** Let x be a family, v in O with Gamma_x(v) = 6, and a != b in O
minus {v} with x_va = x_vb = 4, X^v_a = X^v_b and x'_va = x'_vb = 2. Contradiction.
*Proof (CI's argument).* In the x-configuration translated so that v's representative is 1, VFC (V1)-(V4) and INV (b) give
sets D'_j (j != v), unions of right Phi_v-cosets, disjoint from X^v_j, of measure x'_vj / g_vj, with local indices
lambda'_j = n_j x'_vj / g_vj: ell_j x'_vj for j in O minus {v}, and n_d / 2 = 2^(e_d - 1) 5^(h_d) w_d for d (x'_vd = 1). These odd
parts are pairwise coprime (one 3- and one 5-marker; 3 does not divide n_d), so gcds of these labels are gcds of their 2-parts.
W := intersection of the Phi_j (j != v) gives Phi_vW inside every X^v_j, hence outside every D'_j, of measure
>= 1 / Gamma_x(v) = 1/6 (L0.1, Lagrange); so the union of the D'_j has measure <= 5/6.
1. D := D'_a = D'_b = G minus X^v_a (tightness), measure 2/6.
2. For j in {d} cup (O minus {v, a, b}): D cap D'_j is empty, since a right coset there would carry a, b, j with pairwise label
   gcds <= 2 (2-parts 2, 2 and x'_vj in {1,2,4} or >= 8), violating (V3) (Sun(3)).
3. mu(D'_d) = 1/2, so mu(D cup D'_d) = 5/6 and every D'_c (c in O minus {v, a, b}) lies in D'_d.
4. A right coset in D'_c carries c and d, so x'_vc is even; mu(D'_c) <= 1/2 gives x'_vc = 2.
5. The two such c, c' have D'_c cap D'_c' empty ({c, c', d}: label gcds 2, 2, 2), so 2/6 + 2/6 <= 1/2: false. QED

**3.4 Lemma EQ*.** Let v, a, b be distinct vertices of O, x a family, x_va = x_vb = 4 and X^v_a = X^v_b. Then exactly one of
va, vb tight is impossible; if v != t, both are non-tight; if v = t and both are tight, (x; a, b) is an R1-instance, and then
9 divides T_x(V minus {t}) and x_(e i*) >= 3 for some e in O minus {t}.
*Proof.* One tight, say x'_vb = 2, x'_va = 1: in the notation of 3.3, D'_b = G minus X^v_b (equal measure 2/6), D'_a lies in
G minus X^v_a = D'_b and is non-empty, so a right coset carries a and b with labels ell_a and 2 ell_b, which are coprime: (V3)
fails (Sun(2)). Both tight: CI* if Gamma_x(v) = 6, which holds for v != t (GR (a)); for v = t, CI* and GR (b) give
9 | T_x(V minus {t}), and the contrapositive of GR (b) gives the i*-entry >= 3. QED

**3.5 Lemma BUD.** For each family x: n_4(x) <= 8 - 2 u(x). *Proof.* E3-C2 for x' (needs x_(d i*) = 1: true in K):
n_4(x') >= 2 n_1(x') + 2; n_1(x') >= u(x); n_4(x) + n_4(x') <= 10 (P1). QED

**3.6 Lemma R4*.** Let y be a family and v in O such that the four O-entries of the y-row at v lie in {1, 2}. Then v = t (so the
configuration is in M3(1,1) and y is an R2-instance), y_(t i*) = 2, 9 divides T_y'(V minus {t}), and y'_(e i*) >= 3 for some e in
O minus {t}.
*Proof.* Labels at v: lambda_u = ell_u y_vu (u in O minus {v}), lambda_d = 2^(e_d - 1) 5^(h_d) w_d, lambda_(i*) = n_(i*) z / 6 with
z := y_(v i*). Values in units of 1/6: val(c) = sum over O of c_u y_vu + 3 c_d + z c_(i*). At most two entries are 1 (E3-L2).
Certificate c0: 1 on entries 1, 1/2 on entries 2 and on d, 0 on i*. Its positive labels are the ell_u (entries 1), the 2 ell_u
(entries 2) and lambda_d; odd parts are pairwise coprime (as in 3.3), so an entry 1 lies in no allowed set with another
positive label (Sun(2)) and three of the others (pairwise gcd 2) form no allowed set (Sun(3)); by heredity every allowed set
has positive weight <= 1. val(c0) = 4 + 3/2 = 11/2. By RC, val <= 6 (1 - 1 / Gamma_y'(v)); if Gamma_y'(v) = 6 this is 5 < 11/2.
By GR (a), Gamma_y'(v) = 6 unless v = t; so v = t and Gamma_y'(t) != 6, i.e. 9 | T_y'(V minus {t}) (GR (b)), and by GR (b)
some y'_(e i*) >= 3. Now v = t, f* = 1, lambda_(i*) = 2 * 5^(h*) w_* z, and LFC (d) at t gives val < 6 for every feasible
certificate. Note z = 5 forces h_d >= 1: otherwise L1 on {d, i*, t} (y-configuration) has 5 | tau (from (T1) on the edge t i*:
5 divides (n_d / 4) tau, and n_d / 4 = 2^(e_d - 2) w_d) while tau <= 3 ((T3), (T2) at apex t: tau / 6 <= mu(Phi_tPhi_d) = 1/2).
- z in {1, 3}: c1 := c0 plus 1/2 on i*. The i*-label has 2-part 2 and odd part 3^(v3 z) 5^(h*) w_*, coprime to every ell_u
  (u != t has no 3; 5 is on one vertex) and to the odd part of lambda_d; so the argument for c0 applies. val = 11/2 + z/2 >= 6.
- z in {4, 5}: c2 := 1 on entries 1, 1/2 on entries 2 and on i*, 0 on d. The i*-label (2-part 8 or 2; odd part 5^(h* + v5 z) w_*)
  is coprime in odd part to every ell_u (for z = 5, h_d >= 1, so no ell_u has 5); so pairwise gcds of positive labels other
  than entries 1 are 2, and c2 is feasible. val = 4 + z/2 >= 6.
Both contradict LFC (d) at t, so z = 2. QED

**3.7 Lemma DEG (under NR).** If NR holds then, for each family x: every vertex of O has H_x-degree in {1, 2, 3}; a vertex of
H_x-degree 3 with fourth O-neighbour e has x'_ve = 4; H_x has no K4 and no two triangles sharing exactly one vertex.
*Proof.* Under NR, R4* says that no row (either family, any O-vertex) has its four O-entries in {1, 2}. Degree 0 in H_x: the
x-row at v has entries in {1, 2} (P1). Degree 4: the x'-row has entries x' <= 2 (P1). Degree 3 with x'_ve <= 2: the x'-row again.
K4 on four vertices: each has degree 3 with fourth neighbour the fifth vertex e, so x' = 4 on four pairs at e: degree 4 in
H_x'. Two triangles sharing one vertex: degree 4 there. QED

## 4. Triples and graphs
**4.1 Lemma T16 (no hypothesis).** In K, for both families, no O-triple has type (4,4,4) with tau = 16; so every O-triple has
raw depth <= 4, and the deep O-triples are those of type (2,4,4) or (4,4,4) with tau 8.
*Proof.* At each apex P4 gives equal X-sets; EQ* at each apex != t makes its two edges non-tight; at most one apex is t, and
the other two apexes cover all three edges. So u(x) >= 3 and n_4(x) <= 2 (BUD) < 3. QED

**4.2 Lemma ONE (under NR).** For each family x, at most one O-triple has type (2,4,4) with tau 8; if one exists, u(x) >= 2 and
n_4(x) <= 4. *Proof.* Its apex has equal X-sets (P4); under NR, EQ* makes both apex edges non-tight (at t, both tight would
be an R1-instance, one tight is impossible). Two such triples give at least three non-tight edges (each edge pair determines
its triple), so n_4(x) <= 2 < 3. QED

**4.3 Lemma TRI.** A graph on a 5-set with maximum degree <= 3, no K4 and no two triangles sharing exactly one vertex has at
most two triangles, and two of its triangles share an edge (a diamond).
*Proof.* Two triangles share exactly two vertices. Let T_1 = {A, B, C}, T_2 = {A, B, D} and a third triangle T_3. If T_3
contains A and B, A has degree 4. Otherwise T_3 shares BC or AC with T_1, say BC (symmetry A <-> B): T_3 = {B, C, Y},
Y != A; T_3 must share an edge with T_2, necessarily BY, so Y = D and {A, B, C, D} is a K4. QED

## 5. Theorem FB-M (four-subset bound under NR) [NEW; CANDIDATE_UNVERIFIED]
**Statement.** If a configuration of K satisfies NR, then for both families x and every 4-subset Q of O: delta(Q) <= 4.
*Proof.* Fix x and suppose delta(Q) >= 5. For e in Q with e != t, P3 gives **(N_e)** delta(Q) = delta(R_e) + v2 k_e with
1 <= k_e <= m_e and v2 k_e <= v2 m_e; by T16, delta(R_e) <= 4, so v2 k_e >= 1 and m_e >= 2. (No statement (N_t) is used.)
(i) No pair of Q has x = 1: each pair has an endpoint a != t, and m_a >= 2.
(ii) Not all six pairs are x-4-edges (no K4, DEG). Let N != empty be the set of pairs of Q with x = 2, I the set of their
endpoints.
(iii) For v in I minus {t}: m_v = 2, so delta(R_v) >= 4 by (N_v): R_v is deep, of type (2,4,4) or (4,4,4) with tau 8 (T16). Its
pairs with x = 2 are the N-edges avoiding v; so at most one N-edge avoids v, and exactly one iff R_v has type (2,4,4).
(iv) By ONE at most one v in I minus {t} has R_v of type (2,4,4); every other v in I minus {t} lies on every N-edge. If
|I minus {t}| >= 3, two of them lie on every N-edge, so N is the single pair they form and |I| = 2: impossible. Hence
|I minus {t}| <= 2, and one of the following holds.
- (iv-a) t not in I: N = {ab} with a, b != t.
- (iv-b) I = {t, a}: N = {ta}.
- (iv-c) I = {t, a, b} and N is one of {ta, tb}, {ta, tb, ab}, {ta, ab}, {tb, ab}; write Q = {t, a, b, q}; q is on no N-edge,
  so tq, aq, bq are x-4-edges (by (i)).
(v) Case (iv-a), Q = {a, b, c, q}: R_b = {a, c, q} has type (4,4,4), is deep by (iii), so tau = 8 and delta(R_b) = 4; (N_b) gives
v2 k_b >= 1 and k_b <= m_b = 2, so k_b = 2 = x_ba and (P3 equality) Phi_b W_(R_b) = X^b_a, of measure 2/6. For j in {c, q},
W_(R_b) lies in Phi_a cap Phi_j, so P4 gives tau({a, b, j}) / 24 >= 2/6; {a, b, j} has type (2,4,4), so tau = 8. Two distinct
(2,4,4) tau-8 triples contradict ONE.
(vi) Case (iv-b), Q = {t, a, c, q}: R_a = {t, c, q} has type (4,4,4) and is deep by (iii) (a != t), so tau = 8; (N_a) gives
k_a = 2 = x_at, so Phi_a W_(R_a) = X^a_t (measure 2/6); P4 at apex a gives tau({t, a, j}) >= 8 for j in {c, q}, and {t, a, j} has
type (2,4,4): two (2,4,4) tau-8 triples, contradicting ONE.
(vii) Case (iv-c). If tb in N (N = {ta, tb} or {ta, tb, ab}) and ta in N: a is avoided by tb and b by ta, so R_a = {t, b, q} and
R_b = {t, a, q} both have type (2,4,4) (by (iii)): contradicts ONE. If N = {ta, ab}: b is avoided by ta, so R_b = {t, a, q} is a
(2,4,4) tau-8 triple and n_4(x) <= 4 (ONE); the x-4-edges of Q are tb, tq, aq, bq, so H_x has exactly these four edges and the
fifth vertex of O has H_x-degree 0, contradicting DEG. N = {tb, ab} is symmetric. QED

## 6. Main results
**6.1 Lemma DEEP (under NR).** For each family x, at least two O-triples have type (2,4,4) or (4,4,4) with tau 8.
*Proof.* Theorem DG applies to both families (orientation (1,1)), its four-subset hypothesis by FB-M. DG (b): an O-triple of
capped depth >= 4 exists, and if only one does, its capped depth is 5, hence raw depth 5, excluded by T16. So two O-triples
have capped, hence raw, depth >= 4; T16 gives their types. QED

**6.2 Theorem MK [NEW; CANDIDATE_UNVERIFIED].** No configuration of K (in a finite group) satisfies NR.
*Proof.* Step 1: for each family x, H_x contains a diamond. Deep (4,4,4) triples are triangles of H_x, at most tri(H_x) <= 2 of
them (DEG, TRI); deep (2,4,4) triples are at most one (ONE). If tri(H_x) <= 1, DEEP forces tri(H_x) = 1 and a (2,4,4) tau-8 triple,
so n_4(x) <= 4 (ONE); with triangle {c1, c2, c3}, the vertices c4, c5 have H_x-degree >= 1 (DEG), so H_x = {c1c2, c2c3, c1c3, c4c5};
then every O-triple with two x-4-edges is {c1, c2, c3}, and no (2,4,4) triple exists: contradiction. So tri(H_x) = 2 and H_x
contains a diamond (TRI). Step 2: if H_alpha contains the diamond ac, aq, bc, bq, cq, then H_alpha* lies in {ab, ae, be, ce, qe}
(P1), whose only triangle is {a, b, e}: contradiction with Step 1 for alpha*. QED

**6.3 Theorem M5 [NEW; CANDIDATE_UNVERIFIED].** M5 has no configuration, for every e_d >= 4 and all exponents (f*, h_p, w's)
unbounded; in any group with finite-index subgroups (R0; LFC/INV verdict item 6). *Proof.* NR holds vacuously in M5 (no t). QED

**6.4 Theorem M3R (residual classification) [NEW; CANDIDATE_UNVERIFIED].** Every configuration of M3(1,1) (any group, via R0)
has an R1-instance or an R2-instance. Moreover every R1-instance (x; a, b) has 9 | T_x(V minus {t}) and x_(e i*) >= 3 for some e
in O minus {t} (EQ*); every R2-instance y has y_(t i*) = 2, 9 | T_y'(V minus {t}) and y'_(e i*) >= 3 for some e in O minus {t} (R4*).
*Proof.* Theorem MK. QED

**6.5 Corollary M3G [CANDIDATE_UNVERIFIED].** M3(1,1) has no configuration in which 9 divides neither T_alpha(V minus {t}) nor
T_alpha*(V minus {t}); in particular none in which alpha_(e i*) and alpha*_(e i*) lie in {1, 2} for every e in O minus {t}.
*Proof.* Such a configuration has no R1- or R2-instance (6.4), contradicting MK; the second clause is GR (b). QED

## 7. Obstruction note for M3(1,1) (scope section 2, items (a)-(d))
- **(a) Steps of the unmarked/M5 route that fail or are unproved at t.** (1) Granularity at t: Gamma_y(t) = 2 * 3^(min(f_t, v3 T)),
  and 9 | T_y(V minus {t}) is forced whenever some e in O minus {t} has y_(e i*) = 3 (GR (c)); then RC at t gives only
  1 - 1/18 or weaker. (2) Hence CI at t (EQ's both-tight case at apex t) is unproved. (3) The (R4) row exclusion at t survives
  without granularity except for i*-entry 2 (R4*). (4) The chain step that adds t has gcd(n_t, T_x(S)) = 2 * 3^(min(f_t, v3 T_x(S)))
  (for example 18 when S is a (4,4,4) triangle with tau 12); FB-M avoids it. (5) The DT-B (R3) certificate is not usable at an
  O-vertex whose 4-neighbour is t when its i*-entry is 3 (t's label and the i*-label share the prime 3); it is not used here.
  EQ's one-tight coprimality and the gcd 6 at p survive every marker.
- **(b) Smallest missing lemma(s).** Exclude R1-instances and R2-instances in M3(1,1): (L-R1) for a family x, a tight
  equal-X pair at t (x_ta = x_tb = 4, X^t_a = X^t_b, x'_ta = x'_tb = 2) is impossible; (L-R2) for a family y, a y-row at t with all
  four O-entries in {1, 2} and i*-entry 2 is impossible. A single sufficient lemma is (Gt): 9 divides neither T_alpha(V minus {t})
  nor T_alpha*(V minus {t}).
- **(c) Conditional statement.** CONDITIONAL ON (L-R1) and (L-R2) (or on (Gt)): M3(1,1) is empty (Theorem MK; Corollary 6.5).
- **(d) Unconditional sub-cases.** M3(1,1) intersected with "no R1- and no R2-instance" is empty (Theorem 6.4); in particular
  M3(1,1) with every i*-entry alpha_(e i*), alpha*_(e i*) (e in O minus {t}) in {1, 2} is empty (Corollary 6.5).
No other claim about M3(1,1); no pattern realisability claim.

## 8. Scope, dependency order, provenance, checks
- **Dependency order:** P1-P4 -> RC, GR -> CI* -> EQ*, BUD -> R4* -> DEG (under NR) -> T16 (no hypothesis), ONE (NR), TRI ->
  FB-M (NR) -> DEEP (DG) -> MK -> M5, M3R, M3G.
- **Not claimed:** M13 ((1,3)/(3,1)); K7; Sun(7); any statement for M3(1,1) beyond section 7; acceptance of GS/HD/GX.
- **Sun provenance.** Direct new Sun instances: Sun(2) (EQ*, R4*), Sun(3) (CI*, R4*). Through imports: Sun(2), Sun(4) (K62-E3).
  The accepted LFC/VFC package cites Sun(t), t <= 6, and the class reduction uses the computer-assisted Sun(5) (2cf02436…5301)
  and Sun(6) (efe1d849…1e29); both remain in the transitive import closure.
- **Mutation checks (thought experiments; nothing run):** (1) give t granularity 18 (some y_(e i*) = 3): RC at t yields
  17/18 and c0's 11/2 is no contradiction, so R2-instances with i*-entry 2 are not excluded; (2) use the chain step (N_t) in
  FB-M: it fails when R_t is a (4,4,4) triangle with tau 12; (3) drop the T rule in R4*: z = 5 with h_d = 0 would need a
  separate certificate (the i*-label shares 5 with a 5-marked O-label); (4) drop E3-L2: three entries 1 in a row would change
  val(c0); (5) drop the edge-disjointness: both families could carry diamonds.
- No computation, enumeration, novelty, priority, Lean or human-review claim.
