# K62-FULL-v1: class K6.2* has no configuration — uniform i*-free subset-granularity proof for every orientation and marker placement [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T13:18:01-0700, immediately before this exclusive write.
- **Author:** SunM13MixedFibres; single author; written mathematics only. No computation, enumeration, solver, Lean, model
  call or nested agent. **Label of every new claim: CANDIDATE_UNVERIFIED.**
- **Frozen scope:** `K62-FULL-SCOPE-v1.md` (this directory), sha256 8ee636479aa4742a260f3248343b2a04a30ab447a4f9b8af3572f52a62878303,
  frozen at 13:14 before any derivation in this directory (its section 3 discloses the pre-freeze expectations). **Outcome
  against it: the primary target Theorem K62X is proved in writing (section 9); the fallback is not used.**
- **Premises.** Parent-accepted statements only, at their original scopes (section 1). The pending candidates K62-M13X-v1 (my
  own, b86bb186…2db9, untouched), K62-MK-v2, K62-R2MIX-v2 and K62-M3R-v2 are NOT premises: every step taken from them is
  re-proved below in the wider setting and attributed in section 10 as an old argument, not as new progress.
- RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`; R16 := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`;
  S := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`; K62 := S/continuations/k63-residue/k62-followon;
  O16 := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7`.

## 0. Setting and notation
**Class K6.2*** (O16/README.md section 5): a group G with pairwise disjoint left cosets g_jU_j (j in V) of finite-index
subgroups, n_j := [G : U_j], V = {d, i*} disjoint-union O, |O| = 5, C := {i*} cup O, with (README sections 2-5, P0-P1):
- n_d = 2^(e_d) 5^(h_d) w_d (no factor 3), n_(i*) = 2^(e*) 3^(f*) 5^(h*) w_* (e* >= 2, f* >= 1), n_c = 2 * 3^(f_c) 5^(h_c) w_c with
  f_c >= 1 for c in O; min(e_d, e*) = 2; at most one vertex has f >= 2, at most one has h >= 1; the w's are pairwise coprime
  and coprime to 30; g_jk := gcd(n_j, n_k) = 6 inside C, 4 for d-i*, 2 for d-c (c in O).
- **Markers, all placements allowed:** the 3-marker (the vertex with f >= 2) is on some **t in O**, on i* (any f* >= 2), or
  absent; the 5-marker is on d, on i*, on some vertex of O, or absent. Write O' := O minus {t} if t exists and O' := O
  otherwise; "t" below is void when no 3-marker lies on O.
By R0 (README section 1; LFC/INV verdict item 6) we assume **G finite** until section 9; mu(Y) := |Y| / |G|. By the accepted
K62-E3 theorem, **e_d >= 4 and e* = 2** in every K6.2* configuration.
For c in O put **ell_c := n_c / 6 = 3^(f_c - 1) 5^(h_c) w_c**: odd and pairwise coprime, prime to 3 unless c = t. The odd part
5^(h_d) w_d of n_d is coprime to every ell_c (3 does not divide n_d; one 5-marker; coprime w's).

**Families.** Gamma := (g_jU_j), Gamma* := (g_j^-1 U*_j) with U*_j := g_jU_jg_j^-1. By INV (a)-(b) with E6, Gamma* consists of
pairwise disjoint left cosets with the same labelled index tuple (so it is of class K6.2* with the same markers), its
alpha-matrix is alpha*(Gamma), and (Gamma*)* = Gamma, so its alpha*-matrix is alpha(Gamma). For x in {alpha, alpha*} the
**x-configuration** is Gamma (x = alpha) or Gamma* (x = alpha*); x' is the other family; Phi^x_j, h^x_j denote the subgroup and
representative of j there. Then h^x_jPhi^x_j(h^x_j)^-1 = Phi^x'_j (U*_j for x = alpha; g_j^-1U*_jg_j = U_j for x = alpha*). In the
x-configuration the alpha-matrix is x and the alpha*-matrix (= VFC q-matrix, INV (b)) is x'.

**Indices.** T_x(S) := [G : intersection of the Phi^x_j, j in S] for non-empty S in V (unchanged under a common conjugation);
delta_x(S) := v2 T_x(S) for S in O; tau_x(R) := T_x(R) / lcm(n_j : j in R) for an O-triple R; its **type** is its sorted
x-values; R is **deep** if delta_x(R) >= 4 (as e_d >= 4 this is DG's capped depth min(e_d, delta_x(R)) >= 4).
X^v_j := Phi^x_vPhi^x_j. E1 for the x-configuration: T_x({j,k}) = lcm(n_j, n_k) x_jk, 1 <= x_jk <= g_jk - 1,
mu(Phi^x_jPhi^x_k) = x_jk / g_jk; hence **x_dc = 1 for every c in O and both families.**
H_x: graph on O of the pairs with x = 4; n_k(x): number of O-pairs with x = k; an x-4-pair uv is tight if x'_uv = 2 and
non-tight if x'_uv = 1 (P1); u(x): number of non-tight x-4-pairs.
**Fibres (LFC).** At v in the x-configuration: the n_v left cosets of Phi^x_v; S_F := {j != v : h^x_jPhi^x_j meets F}. LFC (a)-(c):
the j-piece meets exactly deg_v(j) = n_v x_vj / g_vj fibres, never v's own coset; label lambda_j = n_j x_vj / g_vj; every S_F is
lambda-allowed (every T in S_F with |T| >= 2 has j != k with gcd(lambda_j, lambda_k) >= |T|; Sun(|T|) inside Phi^x_v); subsets of
allowed sets are allowed. y >= 0 on V minus {v} is feasible if its sum over every allowed set is <= 1; val(y) := sum_j y_j x_vj / g_vj.

## 1. Interface table (every import at its original accepted scope)
| tag | exact statement used | source (path; sha256; location) | status / scope | used in |
|---|---|---|---|---|
| R0, L0.1, L0.2, Lagrange | finite quotient by the intersection of cores preserves indices, intersection indices, disjointness, conjugated intersections; \|XY\| = \|X\|\|Y\|/\|X cap Y\| | O16/README.md 2a6d6d6e…3fd1 sections 0-1; RUN/review/sun7-lfc-inv-parent-verdict-v1.md 8621e744…cca18 item 6 | accepted | all |
| class K6.2*, P0, P1 | prime-incidence structure, gcd matrix, marker uniqueness | O16/README.md lines 31-52, 85-96; R16/sun-coset7-written-parent-verdict-v1.md 73a25ba6…9f35 | accepted | 0, 2 |
| Sun(2), Sun(3), Sun(4); Sun(5), Sun(6) | Sun(k), k <= 6, every group | README section 0; R16 written verdict | accepted; Sun(5)/(6) computer-assisted (2cf02436…5301, efe1d849…1e29), transitive only | 3-6 (Sun(2), Sun(3) direct) |
| E1 | 1 <= alpha <= g - 1; mu(U_jU_k) = alpha/g; pair index | S/K7-LFC-INV-erratum-v1.md 7af9acf0…75bd5 lines 12-19; verdict 8621e744 | accepted | 0, 2, 4 |
| LFC (a)-(d) | fibre degrees, labels, allowed sets, count | S/K7-LFC-INV-v1.md 45be9162…726c lines 18-45 (+ erratum E3); verdict item 1 | accepted, k <= 7 | 2, 3, 5 |
| INV (a)-(b), E6, E7 | inversion; alpha + alpha* <= g; q = alpha*; same class; inverting twice returns | S/K7-LFC-INV-v1.md lines 52-71; erratum lines 47-63; verdict item 2 | accepted | 0, 2, 6, 9 |
| VFC (V1)-(V4) | D_j disjoint from U_vU_j, measure q_j/g_vj, union of right U_v-cosets; (V3) | O16/rules-k7-v1.md 77b9afec…3cee lines 38-46; R16 written verdict | accepted, either configuration | 3, 6 |
| E3-T | every K6.2* configuration has e_d >= 4, e* = 2 | K62/K62-E3-v1.md 70a60d55…7372 lines 22-23; RUN/review/sun7-K62E3-parent-verdict-v1.md 576969dd…bb0f line 5 | accepted, whole class | 0 |
| E3-L1 | x_(d i*) != 2; x_(d i*) = 3 only if the 3-marker lies on some t in O (x in {alpha, alpha*}) | K62-E3-v1.md lines 25-34 with K62/K62-E3-erratum-v2.md f9f52e1b…dd4c Z2 lines 82-88; E3 verdict line 19 | accepted, whole class | 2 |
| E3-L2 | at an O-vertex, both families: x_vu != 3; at most two entries 1; x_vu != 5 if h_d >= 1 | K62-E3-v1.md lines 36-55; E3 verdict line 20 | accepted, whole class, any orientation | 2 (P1) |
| E3-C2 | n_4(alpha*) >= 2 n_1(alpha*) + 2 when alpha_(d i*) = 1; for alpha when alpha*_(d i*) = 1 (inverted configuration) | K62-E3-v1.md lines 91-105 (line 105 for the swap) with erratum v2 Z11 lines 276-297; E3 verdict line 25 | accepted at these orientation scopes | 2 (FAM) |
| DG | Theorem DG (a)-(b) for the alpha*-family when alpha_(d i*) = 1, under min(e_d, delta(Q)) <= 4 for all 4-subsets; the same for alpha when alpha*_(d i*) = 1 | K62/K62-DG-v1.md a4bfc41e…1e84f52 lines 50-61 with K62/K62-SH-DG-erratum-v1.md 755edc21…1d75 G5/G6 (lines 240-268) and notes (lines 323-327); RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md cae455c3…ddda item 4 | accepted at these orientation scopes | 2 (FAM) |
| M13-A | in (1,3): DG* (a)-(b) for alpha under its own four-subset hypothesis; C2*: n_4(alpha) >= 2 n_1(alpha) + 2 | K62/K62-M13-A-v1.md 77ce4077…6a8d lines 85-104; RUN/review/sun7-K62-M13-parent-verdict-v1.md 2fac7a30…4c34 items 1-2 (+ parent erratum 99276f6d…9e29) | accepted at the (1,3) scope | 2 (FAM) |
| GS | in G (no O-marker): FB, Theorem GE (G empty), Corollary OM | S/continuations/k62-regimes/K62-GS-v1.md 020fdc7a…4627; RUN/review/sun7-K62-GS-parent-verdict-v1.md 3a01c9e4…dfc2 (+ erratum 9c60e418…616b) | accepted; **cross-check only**, not a premise | 10 |
Pending, NOT premises (re-proved and attributed, section 10): K62-M13X-v1 (b86bb186…2db9), K62-MK-v2 (ab7cfcb6…bee9), K62-R2MIX-v2
(b75e6dc7…0806), K62-M3R-v2 (af2b965b…88b3). Not used: CAP C1/C2/RC, DT-A/B/C, SH, M13 B/C/D, HD, GX, FH, Sun(7), any computation.

## 2. Orientation partition, family inputs and the O-values
**Lemma OR (exact d-i* orientations).** In every K6.2* configuration: (i) alpha_(d i*) and alpha*_(d i*) lie in {1, 3}; (ii) they
are not both 3; (iii) if one of them is 3, the 3-marker lies on some t in O, so f_t >= 2 and f* = 1. Hence
(alpha_(d i*), alpha*_(d i*)) is (1,1), or (1,3) or (3,1) with t in O.
*Proof.* g_(d i*) = 4, so 1 <= x_(d i*) <= 3 for x in {alpha, alpha*} (E1). E3-L1 (for x and, by its statement, for both
families) excludes 2 and allows 3 only if the 3-marker lies on a vertex t of O. INV (b): alpha_(d i*) + alpha*_(d i*) <= 4, so not
both are 3. If one is 3, t exists; at most one vertex has f >= 2, so f* = 1. QED

**Reduction R.** If alpha_(d i*) = 3, the actual inverted configuration Gamma* is of class K6.2* with the same indices and
markers, and its pair is (alpha*_(d i*), alpha_(d i*)) = (1, 3) by OR (i)-(ii). So it suffices to exclude configurations with
**alpha_(d i*) = 1**; then alpha*_(d i*) = 1, or alpha*_(d i*) = 3 with t in O and f* = 1. All marker placements of section 0
remain allowed in the case alpha*_(d i*) = 1, including f* >= 2.

**Lemma FAM (both-family inputs).** Let alpha_(d i*) = 1. For both families x:
(C2_x) n_4(x) >= 2 n_1(x) + 2;
(DG_x) if min(e_d, delta_x(Q)) <= 4 for all five 4-subsets Q of O, then at least two O-triples R have min(e_d, delta_x(R)) >= 4,
or exactly one does and it has min(e_d, delta_x(R)) = 5, type (4,4,4) and tau_x(R) = 16.
*Proof.* x = alpha*: E3-C2 and Theorem DG (b) (with G6) for the alpha*-family, whose hypothesis alpha_(d i*) = 1 holds; DG's
depths are v2 T*_Q = delta_alpha*(Q) (T*_Q is the index of the intersection of the U*_c, unchanged by the normalisation g_d = 1).
x = alpha, case alpha*_(d i*) = 1: apply the same accepted statements to the actual configuration Gamma*, which is of class
K6.2* with e_d >= 4 and whose distinguished entry alpha_(d i*)(Gamma*) = alpha*_(d i*) = 1; its alpha*-family is alpha (section 0) and
its conjugated family is (U_j), so its depths are delta_alpha. (These are also the literal swapped statements E3-v1 line 105 and
DG-v1 line 61, accepted by the E3 and SH-DG verdicts; GS uses the same both-family reading in G.) x = alpha, case
alpha*_(d i*) = 3: then t is in O and f* = 1 (OR), and M13-A gives C2* and DG* (b) for alpha at its accepted (1,3) scope. QED

**P1 (O-values) [E3-L2 plus the argument of E3 Z11 (a), re-proved for both families in every orientation].** For every
O-pair uv and both families: x_uv lies in {1, 2, 4} and x_uv + x'_uv <= 6. Hence H_alpha and H_alpha* are edge-disjoint, and on
an x-4-pair x' lies in {1, 2}.
*Proof.* 1 <= x_uv <= 5 (E1), x_uv != 3 and (if h_d >= 1) x_uv != 5 by E3-L2, which is stated for both families with no
orientation hypothesis. If h_d = 0 and x_vu = 5: in the x-configuration at v, lambda_u = 5 ell_u is odd and lambda_d =
n_d x_vd / 2 = 2^(e_d - 1) w_d, so gcd(lambda_u, lambda_d) = 1 and {u, d} is not allowed (Sun(2)); y_u = y_d = 1 (else 0) is
feasible and val = 5/6 + 1/2 > 1, contrary to LFC (d). INV (b) gives x + x' <= g_uv = 6. QED

## 3. General lemmas (any finite group, any k <= 7 pairwise disjoint left cosets (h_jPhi_j))
**Lemma 1 (subset light fibres; LFC form).** Let v be a vertex, Q a non-empty set of vertices not containing v and
W_Q := intersection of the h_jPhi_jh_j^-1 (j in Q). (a) At least n_v / gcd(n_v, [G : W_Q]) left Phi_v-cosets meet no h_jPhi_j with
j in Q (h_vPhi_v is one). (b) Every feasible y at v vanishing off Q has sum_j y_j alpha_vj / g_vj <= 1 - 1/gcd(n_v, [G : W_Q]).
(c) In the x-configuration, [G : W_Q] = T_x'(Q).
*Proof.* (a) W_Qh_vPhi_v is the union of the cosets wh_vPhi_v (w in W_Q); wh_vPhi_v = w'h_vPhi_v iff w^-1w' lies in
Psi := h_vPhi_vh_v^-1 (index n_v); so there are [W_Q : W_Q cap Psi] = [G : W_Q cap Psi] / [G : W_Q] of them, and [G : W_Q cap Psi] is
divisible by lcm(n_v, [G : W_Q]) (Lagrange). w = 1 gives h_vPhi_v. If wh_vu lay in h_jPhi_j (w in W_Q, u in Phi_v, j in Q), then
w = h_jah_j^-1 (a in Phi_j) and h_j^-1h_vu lies in Phi_j, so h_vu lies in h_jPhi_j cap h_vPhi_v = empty. (b) LFC (a)-(b):
sum_j y_j deg_v(j) = sum over fibres F of the sum of y over S_F; this inner sum is 0 on the fibres of (a) (S_F misses Q, y
vanishes off Q) and <= 1 on every other fibre (LFC (c)). (c) Section 0. QED

**Lemma 1' (subset light set; VFC form).** Translate the x-configuration so that h^x_v = 1 (subgroups unchanged); D_j :=
Phi_vh_jPhi_j and X_j := Phi_vPhi_j (Phi = Phi^x, j != v). For non-empty Q not containing v and W := intersection of the Phi_j (j in Q):
Phi_vW lies in every X_j (j in Q), hence misses every D_j (j in Q) by (V1), and mu(Phi_vW) = [G : Phi_v cap W] / (n_v T_x(Q))
>= 1/gcd(n_v, T_x(Q)). So the union of the D_j (j in Q) has measure <= 1 - 1/gcd(n_v, T_x(Q)). QED

**Lemma 2 (product separation).** If v, j, k are distinct and (Phi_v cap Phi_j)(Phi_v cap Phi_k) = Phi_v, no left Phi_v-coset meets
both h_jPhi_j and h_kPhi_k. *Proof.* If p in h_jPhi_j and q in h_kPhi_k lie in one left Phi_v-coset, then p^-1q = ab with
a in Phi_v cap Phi_j, b in Phi_v cap Phi_k, and pa = qb^-1 lies in pPhi_j cap qPhi_k = h_jPhi_j cap h_kPhi_k = empty. QED

## 4. Proposition SG (i*-free subset granularity, every placement and orientation)
**Statement.** In every K6.2* configuration, for both families z and every non-empty R in O:
T_z({d} cup R) = lcm(n_d, n_j : j in R) * 2^s for some integer s >= 0. Consequently, **for every v in O: gcd(n_v, T_z(V minus {v, i*})) = 6.**
*Proof.* Pi_j := Phi^z_j; order R as c_1, ..., c_m; S_r := {d, c_1, ..., c_r}; W_r, T_r := [G : W_r]; L_r := lcm(n_d, n_(c_1), ..., n_(c_r)).
- r = 1: T_1 = lcm(n_d, n_(c_1)) z_(d c_1) = L_1 (E1, z_dc = 1).
- r >= 2, e := c_r: T_r = lcm(n_e, T_(r-1)) k (Lagrange) with k / gcd(n_e, T_(r-1)) = mu(Pi_eW_(r-1)) (L0.1). By induction
  T_(r-1) = L_(r-1) 2^s, and gcd(n_e, T_(r-1)) = 6: 2-part 2 (v2 n_e = 1 <= e_d); 3-part 3^(min(f_e, v3 L_(r-1))) = 3, because
  v3 L_(r-1) >= 1 and either f_e = 1, or e = t and then all earlier c's have f = 1, so v3 L_(r-1) = 1; 5-part 1 (if h_e >= 1 no
  other vertex has a 5, and 2^s has none); w-part 1. So k = 6 mu(Pi_eW_(r-1)) <= 6 mu(Pi_ePi_d) = 6 z_ed / 2 = 3 (W_(r-1) lies in Pi_d).
  If k = 3, then Pi_eW_(r-1) = Pi_ePi_d (inclusion, equal measure 1/2); every x in Pi_d is ab with a in Pi_e, b in W_(r-1) (contained in
  Pi_d cap Pi_(c_1)), so a lies in Pi_d and Pi_d = (Pi_d cap Pi_e)(Pi_d cap Pi_(c_1)). Lemma 2 in the z-configuration at d then forbids a
  fibre at d meeting both the e- and c_1-pieces; but each meets exactly n_d z_dc / 2 = n_d / 2 fibres and neither meets d's own
  coset, so #(both) = #(neither) >= 1. Hence k is 1 or 2, and lcm(n_e, L_(r-1) 2^s) = lcm(n_e, L_(r-1)) 2^s (v2 n_e = 1 <= v2 L_(r-1)),
  so T_r = L_r 2^(s + v2 k).
- For v in O and R := O minus {v}: {d} cup R = V minus {v, i*}, T := L 2^s, and gcd(n_v, T) = 6: 2-part 2; 3-part
  3^(min(f_v, max over R of f)) = 3 (if v = t, every vertex of R has f = 1; otherwise f_v = 1); 5-part 1; w-part 1. QED
*Remarks.* f*, h*, e*, the entries at i* and the d-i* entries never enter: i* is not in Q. The product-separation step is
needed only when v = t; without a 3-marker on O, the bound k <= 3 already gives gcd 6. For the x-row at v, Lemma 1 (c) needs the
granularity of x' (the opposite configuration's d-fibres enter: mixed families); for VFC at v, Lemma 1' needs that of x.

## 5. Rows at every O-vertex
**Lemma R4S.** For both families x and every v in O, the four O-entries x_vu (u in O minus {v}) do not all lie in {1, 2}.
*Proof.* x-configuration at v: lambda_u = ell_u x_vu (u in O minus {v}), lambda_d = n_d / 2 = 2^(e_d - 1) 5^(h_d) w_d (x_vd = 1); their odd
parts are pairwise coprime (section 0), so gcds are gcds of 2-parts. If all x_vu lie in {1, 2}, put y_u := 1/x_vu, y_d := 1/2,
y_(i*) := 0. Feasible: the positive part P of an allowed set is allowed; an entry-1 label is odd, hence coprime to every other
positive label, so such a P is a singleton (Sun(2)); otherwise P lies among the entries 2 and d, of pairwise gcd exactly 2, so
|P| <= 2 (Sun(3)). val(y) = (#entries 1)/6 + (#entries 2)(1/2)(2/6) + (1/2)(1/2) = 4/6 + 1/4 = 11/12. As y vanishes off
V minus {v, i*}, Lemma 1 (b)-(c) and SG (for z = x') give val(y) <= 5/6: contradiction. QED

**Lemma DEG.** For each family x: (a) every v in O has H_x-degree 1, 2 or 3; (b) if v has H_x-degree 3 and e is its fourth
O-neighbour, then x'_ve = 4; (c) H_x has no K4 and no two triangles sharing exactly one vertex.
*Proof.* (a) Degree 0: the x-row at v has O-entries in {1, 2} (P1): R4S. Degree 4: the x'-row at v has O-entries <= 2 (P1):
R4S. (b) Else the x'-row at v has all O-entries in {1, 2}: R4S. (c) A K4 on Q: each v in Q has degree 3 with fourth neighbour the
fifth vertex e, so x'_ve = 4 for four v and e has H_x'-degree 4, against (a). Two triangles sharing exactly one vertex give it
degree 4. QED

## 6. Cherries at every O-vertex
**Lemma CIS.** For a family x, v in O and a != b in O minus {v} with x_va = x_vb = 4, X^v_a = X^v_b and x'_va = x'_vb = 2: contradiction.
*Proof.* Translate the x-configuration so that h_v = 1. VFC (V1)-(V4) with q = x' (INV (b)): D_j := Phi_vh_jPhi_j is a union of right
Phi_v-cosets disjoint from X_j, of measure x'_vj / g_vj; for a right coset R, every T in S_R := {j : R in D_j} with |T| >= 2 has
j != j' with gcd(d_j, d_j') >= |T|, d_j := n_j x'_vj / g_vj: d_u = ell_u x'_vu (u in O minus {v}), d_d = n_d / 2; odd parts pairwise
coprime. Two unions of right Phi_v-cosets that meet share a right coset. Q := V minus {v, i*}: by Lemma 1' and SG (z = x), the
union of the D_j over Q has measure <= 5/6.
1. D_a = G minus X_a (inclusion, equal measure 2/6); likewise D_b = G minus X_b = D_a =: D.
2. For j in {d} cup (O minus {v, a, b}), D misses D_j: else a right coset carries a, b, j with d_a = 2 ell_a, d_b = 2 ell_b of 2-part 2,
   so all three gcds are <= 2 (Sun(3) via (V3)).
3. mu(D_d) = 1/2, so D cup D_d (disjoint) has measure 5/6 and equals the union over Q; for each of the two c in O minus {v, a, b},
   D_c lies in D cup D_d and misses D, so D_c lies in D_d.
4. D_c is non-empty; a right coset in it carries c, d, so d_c is even (Sun(2)); mu(D_c) = x'_vc / 6 <= mu(D_d) = 1/2 gives
   x'_vc <= 3; so x'_vc = 2 (P1).
5. D_c and D_c' are disjoint (labels 2 ell_c, 2 ell_c', d_d of pairwise gcd 2: Sun(3)) and lie in D_d: 2/6 + 2/6 <= 1/2, false. QED

**Lemma EQS.** For a family x, v in O and a != b in O minus {v} with x_va = x_vb = 4 and X^v_a = X^v_b: x'_va = x'_vb = 1.
*Proof.* Both x' lie in {1, 2} (P1). Both 2: CIS. If x'_vb = 2 and x'_va = 1: D_b = G minus X_b, and the non-empty D_a lies in
G minus X_a = D_b; a right coset in D_a carries a, b with labels ell_a and 2 ell_b, of gcd 1 (Sun(2)). QED

## 7. Triangles, chain steps, budget (one fixed family x, Phi := Phi^x; P1 used freely)
**P4 (apex identity).** For distinct a, b, c in O: mu(Phi_b(Phi_a cap Phi_c)) = tau_x({a,b,c}) / (6 x_ac). Hence if x_ba = x_bc = 4 and
tau_x({a,b,c}) = 4 x_ac, then X^b_a = X^b_c. *Proof.* lcm(n_a, n_b, n_c) = 6 ell_a ell_b ell_c and T_x({a,c}) = 6 ell_a ell_c x_ac (E1);
L0.1 gives mu = T_x({a,b,c}) / (n_b T_x({a,c})) = tau / (6 x_ac). In the second case the set lies in X^b_a cap X^b_c and has their
common measure 4/6. QED (Instances: (2,4,4), tau 8, apex opposite the 2-pair; (4,4,4), tau 16, every apex.)

**P2 (triangles).** For an O-triple R with values x1 <= x2 <= x3: T_x(R) = 6 ell_a ell_b ell_c tau_x(R); tau_x(R) is divisible by each
value and tau_x(R) <= x1 x2; delta_x(R) = 1 + v2 tau_x(R). *Proof.* T_x({a,b}) = 6 ell_a ell_b x_ab divides T_x(R), so x_ab | ell_c tau,
hence x_ab | tau (power of 2, ell_c odd). P4: tau / (6 x_ab) = mu(Phi_c(Phi_a cap Phi_b)) <= min(x_ca, x_cb) / 6; minimise over apexes. QED

**P3 (chain step at e != t).** For non-empty S in O and e in O minus S, e != t: gcd(n_e, T_x(S)) = 6;
T_x(S cup {e}) = lcm(n_e, T_x(S)) k with k = 6 mu(Phi_eW_S) <= x_ej for every j in S (equality iff Phi_eW_S = X^e_j);
delta_x(S cup {e}) = delta_x(S) + v2 k; and v2 k <= v2 m whenever m is a power of 2 with k <= m.
*Proof.* With ell°_j the prime-to-6 part of ell_j, the prime-to-6 part of T_x(S) is the product of the ell°_j (j in S): build S
from t (if present) and add vertices e' != t; each step has gcd(n_e', T) = 6 (ell_e' is prime to 6 and to the earlier ell°) and
multiplier 6 mu(Phi_e'W) <= x_e'j <= 4. For e != t the same computation gives the statement; v2 lcm(n_e, T_x(S)) = v2 T_x(S);
2^(v2 k) <= k <= m. QED

**BUD.** For each family x (with alpha_(d i*) = 1): n_4(x) <= 8 - 2 u(x). *Proof.* (C2_x') of FAM: n_4(x') >= 2 n_1(x') + 2; a
non-tight x-4-pair has x' = 1, so u(x) <= n_1(x'); n_4(x) + n_4(x') <= 10 (P1). QED

**T16.** No O-triple has type (4,4,4) with tau_x = 16; hence delta_x(R) <= 4 for every O-triple, with equality iff tau_x(R) = 8, which
needs type (2,4,4) or (4,4,4). *Proof.* P4 at the three apexes and EQS make all three pairs non-tight: u(x) >= 3 and n_4(x) <= 2
(BUD) < 3. Then tau <= x1 x2 <= 16 with 16 only for (4,4,4), so v2 tau <= 3, and v2 tau = 3 iff tau = 8. QED

**ONE.** At most one O-triple has type (2,4,4) with tau_x = 8; if one exists, u(x) >= 2 and n_4(x) <= 4. *Proof.* At its apex b
(opposite the 2-pair ac) P4 gives X^b_a = X^b_c and EQS makes ba, bc non-tight; BUD. Two such triples have distinct apex pairs
(two pairs sharing a vertex determine the triple), giving three non-tight x-4-pairs: n_4(x) <= 2 < 3. QED

**TRI.** A graph on five vertices with maximum degree <= 3, no K4 and no two triangles sharing exactly one vertex has at most
two triangles, and any two distinct triangles share an edge (so two triangles form a diamond). *Proof.* Distinct triangles
on five vertices share >= 1 vertex, hence exactly two. Given {A,B,C}, {A,B,D} and a third T: if T contains A, B then T = {A,B,E}
and A has degree 4; otherwise T shares BC (or AC, symmetric) with the first, T = {B,C,Y}, Y != A, and sharing two vertices with
{A,B,D} forces Y = D: K4 on {A,B,C,D}. QED

## 8. Four-subset bound
**Lemma FB.** For each family x and every 4-subset Q of O: delta_x(Q) <= 4.
*Proof.* Suppose delta(Q) >= 5 (delta := delta_x). For e in Q: R_e := Q minus {e}, m_e := min over j in R_e of x_ej.
- (N) For e in Q, e != t: P3 gives delta(Q) = delta(R_e) + v2 k_e, 1 <= k_e <= m_e, v2 k_e <= v2 m_e; T16: delta(R_e) <= 4; so
  v2 k_e >= 1 and m_e >= 2.
- (i) No pair of Q has x = 1 (each pair has an endpoint e != t with m_e >= 2).
- (ii) Not all six pairs of Q are x-4-pairs (DEG (c)); so the set N of pairs with x = 2 is non-empty (P1, (i)); I := its endpoints.
- (iii) For v in I minus {t}: m_v = 2, so v2 k_v <= 1 and delta(R_v) >= 4: R_v is deep, of type (2,4,4) or (4,4,4) with tau 8 (T16);
  its x = 2 pairs are the N-pairs avoiding v: none for (4,4,4), one for (2,4,4).
- (iv) Distinct v give distinct R_v; by ONE at most one v in I minus {t} has R_v of type (2,4,4), and every other lies on every
  N-pair. If |I minus {t}| >= 3, two of them lie on every N-pair, so N is their single pair and |I| = 2: impossible. So:
  (a) t not in I (in particular if t does not exist): I = {a, b}, N = {ab}; (b) I = {t, a}, N = {ta}; (c) I = {t, a, b}, N in
  {{ta, tb}, {ta, tb, ab}, {ta, ab}, {tb, ab}}, and the fourth vertex q of Q gives x-4-pairs tq, aq, bq.
- (v) Case (a), Q = {a, b, c, q}: R_b = {a, c, q} has type (4,4,4) and is deep (iii), tau 8, delta 4; by (N) k_b = 2 = x_ba = m_b, so
  Phi_bW_(R_b) = X^b_a (measure 2/6, P3). For j in {c, q}: W_(R_b) lies in Phi_a cap Phi_j, so tau({a,b,j}) / 24 >= 2/6 (P4); values
  (2,4,4) give tau = 8 (P2): two such triples, against ONE.
- (vi) Case (b), Q = {t, a, c, q}: R_a = {t, c, q} has type (4,4,4), deep, tau 8; (N) at a != t: k_a = 2 = x_at, Phi_aW_(R_a) = X^a_t;
  P4 at apex a: tau({t,a,j}) / 24 >= 2/6 for j in {c, q}; type (2,4,4), tau = 8: two such triples, against ONE.
- (vii) Case (c): if ta, tb are in N, R_a = {t,b,q} and R_b = {t,a,q} are deep of type (2,4,4): against ONE. If N = {ta, ab}: R_b =
  {t,a,q} is deep (2,4,4), so n_4(x) <= 4 (ONE); the x-4-pairs of Q are tb, tq, aq, bq, hence all of H_x, and the fifth vertex of
  O has H_x-degree 0: against DEG (a). N = {tb, ab} is symmetric. QED

## 9. Theorem K62X
**Lemma DEEP.** (alpha_(d i*) = 1.) For each family x at least two O-triples are deep; each has type (2,4,4) or (4,4,4) and tau_x = 8.
*Proof.* FB gives min(e_d, delta_x(Q)) <= 4 for all 4-subsets, so (DG_x) of FAM applies; its second alternative ((4,4,4) with
tau_x = 16) is excluded by T16; so at least two triples have delta_x >= 4, and T16 gives delta_x = 4, tau_x = 8 and the types. QED

**Theorem K62X.** No group with finite-index subgroups contains a configuration of class K6.2*: every orientation, every
admissible placement of the 3- and 5-markers (including f* >= 2 and the 5-marker on d, i* or a vertex of O), all exponents
e_d, e*, f's, h's and all w-cofactors.
*Proof.* By R0 take G finite; by Reduction R assume alpha_(d i*) = 1. **Step 1 (each H_x contains a diamond).** Fix x. Deep
(4,4,4) triples are triangles of H_x, at most two by DEG and TRI; deep (2,4,4) triples number at most one (ONE). DEEP gives two
deep triples, so H_x has a triangle. If it has exactly one, {c1, c2, c3}, a deep (2,4,4) triple exists, n_4(x) <= 4 (ONE), c4 and c5
have H_x-degree >= 1 (DEG (a)), so H_x = {c1c2, c1c3, c2c3, c4c5}; two x-4-pairs sharing a vertex then span {c1, c2, c3}, whose third
pair has x = 4, so no (2,4,4) triple exists: contradiction. So H_x has two triangles, sharing an edge (TRI): a diamond.
**Step 2.** H_alpha contains a diamond with triangles {a, c, q}, {b, c, q}; with e the fifth vertex, H_alpha* lies in
{ab, ae, be, ce, qe} (P1), whose only triangle is {a, b, e}: against Step 1 for alpha*. QED
Arbitrary groups: R0 (LFC/INV verdict item 6) passes to the finite quotient by the intersection of the cores, preserving indices,
intersection indices, disjointness and conjugated intersections, hence alpha, alpha*, the class and the markers.

## 10. Provenance (old arguments attributed), new obligations, checks and scope
| item here | origin of the argument | status of origin | what this file adds |
|---|---|---|---|
| Lemma OR, Reduction R | E1, INV (b), E3-L1 | accepted | the exact partition written out (sub-obligation (a)); INV for (3,1) |
| FAM | E3-C2, DG (and their inverted forms), M13-A | accepted | both-family availability checked per orientation, applied to actual configurations |
| P1 | E3-L2; E3 Z11 (a) 5-argument | accepted; Z11 (a) only as a C2 proof sub-claim | the 5-argument re-proved for both families in every orientation |
| Lemmas 1, 1', 2 | K62-E3 step 3, CAP RC / CI light set (accepted instances); R2MIX Lemmas 1-2; M13X Lemmas 1, 1', 2 | accepted instances; R2MIX, M13X pending | re-proved; nothing new |
| SG | M13X Proposition SG | pending (my own, frozen 13:04) | re-proved for every placement/orientation: no-t case, f* >= 2, 5-marker on i*/d/t/O', e = t ordering |
| R4S, DEG | DT-B (R4) certificate (accepted in G); MK-v2 R4*, DEG; M13X | accepted in G; MK, M13X pending | re-proved with SG at every O-vertex |
| CIS, EQS | DT-A CI (accepted at unmarked v, own entry 1); MK-v2 3.3-3.4; M13X | accepted instance; MK, M13X pending | re-proved with SG |
| P2-P4, BUD, T16, ONE, TRI, FB, DEEP, Steps 1-2 | GS (accepted in G); MK-v2 sections 2-6; M13X sections 6-8 | GS accepted; MK, M13X pending | re-proved; BUD/DEEP inputs via FAM in each orientation |
- **New relative to accepted results:** the closure of the O-marked classes — 5-marker in O without 3-marker on O ("M5"),
  t in O in (1,1) ("M3(1,1)"), and t in O in (1,3)/(3,1) ("M13") — by one uniform argument; G is the accepted GS Theorem GE,
  re-derived here only as a special case (no new progress claimed for G). The mechanism is M13X's (pending): SG makes the
  i*-free R4/CI arguments available at the marked vertices t and p, which removes hypothesis NR from MK's chain.
- **Mutation checks (thought experiments; nothing run).** (1) Use V minus {t} instead of V minus {t, i*}: when the d-i* entry of
  the opposite family is 3, or some e has x'_(e i*) = 3, 9 divides T and gcd(n_t, .) >= 18, so 11/12 is not excluded at t. (2) Drop
  Lemma 2 in SG: at t a multiplier 3 is possible, R4S/CIS at t fail, and DEG at t (used in FB (vii) and Step 1) is lost. (3) Drop
  d's own fibre: #both = #neither >= 0 only. (4) Give i* weight: Lemma 1 (b) loses the subset bound. (5) DG in one family only:
  Step 2 fails. (6) In (1,3) without M13-A: BUD for alpha* and DEEP for alpha lack inputs. (7) Assume f* = 1 everywhere: not used;
  SG never involves i*.
- **Sun provenance.** Direct new Sun instances: Sun(2) (P1, R4S, CIS step 4, EQS), Sun(3) (R4S, CIS steps 2, 5) via LFC (c) and VFC
  (V3). Through imports: Sun(4) (K62-E3, DG, M13-A). Sun(5), Sun(6) are computer-assisted (2cf02436…5301, efe1d849…1e29) and stay
  in the transitive closure (LFC/VFC packages, class reduction). FH and Sun(7) are not used.
- **Dependency order.** OR -> R; FAM; P1; Lemmas 1, 1', 2 -> SG -> R4S -> DEG; SG -> CIS -> EQS; P2-P4; BUD (FAM) -> T16, ONE; TRI;
  FB -> DEEP (FAM) -> Theorem K62X.
- **Scope.** Claimed (CANDIDATE_UNVERIFIED): Lemma OR, Reduction R, FAM, P1, Lemmas 1, 1', 2, SG, R4S, DEG, CIS, EQS, P2-P4, BUD,
  T16, ONE, TRI, FB, DEEP, Theorem K62X. Not claimed: K7, K6.3, K5.2*, KII or Sun(7); acceptance of any pending packet; novelty,
  priority, significance, Lean or human review. Requested: parent re-derivation of OR/FAM scopes, SG in the no-t and t cases,
  R4S/CIS at t and at a 5-marked O-vertex, FB; hostile dual review of this exact file.
