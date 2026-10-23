# K62-R2MIX-v2: no R2-row in M3(1,1) — a mixed-family d-fibre count proves the missing lemma (L-R2); R1-instances excluded; M3(1,1) empty only conditionally [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T12:19:10-0700, immediately before composing and writing this file.
- **Author:** SunR2MixedFibres; single author; written mathematics only. No computation of any kind was run (no compute
  GO; global runtime HOLD respected); no model call. **Label of every new claim: CANDIDATE_UNVERIFIED.**
- **Supersedes** the undelivered draft `K62-R2MIX-v1.md` (sha256 90d399eba279d6af7066bec80f70357074fedb1cd54283d4d411aa8d332f6f80,
  frozen, unchanged). Differences, from my own re-read before delivery: (1) a garbled sentence in the proof of Lemma 3 (b) is
  replaced by the inclusion-exclusion identity; (2) the E3-a interface row states its scope as the accepted C2 proof
  sub-claim Z11 (a), as in the parent MK erratum f84defc8; (3) Remark (1) after Theorem R2X names the two K62-E3 facts that are
  re-derived instead of saying E3 is unused; (4) mutation check 2 is reworded; (5) section 7 no longer calls Proposition 5 (a)
  vacuous after R2X. No statement, case or argument changes.
- **Frozen scope (written before the derivation):** `K62-R2MIX-SCOPE-v1.md` in this directory, sha256
  12a64d8e4c19cd6dd8f7d04d6ee7dabef06bd23707522fae07d27a2b4651e4e5 (12:01:42). **Outcome against it:** the primary target
  Theorem R2X is proved in writing for the full class M3(1,1) (section 4); Corollary R1X is proved with Theorem RR re-proved
  here (section 5), so neither uses a pending premise; Corollary M3E is stated only CONDITIONAL ON K62-MK-v2 Theorem M3R
  (section 6). The scope's fallback is not used.
- **Premises.** Parent-accepted results only, at their original scopes (section 1). Pending texts: K62-M3R-v2 (af2b965b…,
  parent erratum cb42f3e7…) and K62-MK-v2 (ab7cfcb6…, parent erratum f84defc8…) supply the definitions repeated in section 0;
  M3R-v2's Lemma A, Lemma C and Theorem RR are re-proved here (Lemma 6, Lemma 4, Theorem 7, arguments attributed);
  M3R-v2's Proposition R2N is **not** used; MK-v2's Theorem M3R is used only in Corollary M3E, as a labelled conditional
  premise. Not used: M13, GS, HD, GX, FH, DT-B/C, RC as a pattern rule.
- RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`;
  K62R := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-regimes`;
  K62 := `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/k62-followon`.

## 0. Setting and notation (definitions, repeated from K62-MK-v2 section 0 and K62-M3R-v2 section 0)
**Class M3(1,1).** The CAP setting of the accepted CAP-DT verdict (RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md, sha256
84061c6fbdbd9fa834810efa43843024e04c2abce794df28446865ef635234a0, line 21) restricted as in K62-MK-v2 section 0: pairwise
disjoint left cosets g_jU_j (j in V) of finite-index subgroups of a group G, n_j := [G : U_j], V = {d, i*} disjoint-union O,
|O| = 5; n_d = 2^(e_d) 5^(h_d) w_d with **e_d >= 4**; n_(i*) = 4 * 3 * 5^(h*) w_* (e* = 2, f* = 1); n_c = 2 * 3^(f_c) 5^(h_c) w_c
(c in O); the 3-marker on **t in O** (f_t >= 2; f_c = 1 for c in **O' := O minus {t}**); at most one vertex with h >= 1 (the
5-marker: on d, on i*, on t, on some p in O', or absent); w's pairwise coprime and coprime to 30;
**(alpha_(d i*), alpha*_(d i*)) = (1, 1)**. Exponents and w's are unbounded. By R0 with LFC/INV verdict item 6, G may be
taken finite (the finite quotient preserves indices, intersection indices, coset disjointness and, by normality, the
conjugated intersections of INV; so the class, alpha and alpha* are preserved). From here on G is finite; mu(Y) := |Y| / |G|.

**Arithmetic.** For c in O, ell_c := n_c / 6 = 3^(f_c - 1) 5^(h_c) w_c: odd, pairwise coprime; for c in O', ell_c = 5^(h_c) w_c
is coprime to 6. g_jk := gcd(n_j, n_k): g_jk = 6 for j != k in {i*} cup O, g_(d i*) = 4, g_(dc) = 2 (c in O). For disjoint
cosets alpha_jk := [G : U_j cap U_k] / lcm(n_j, n_k) is an integer with 1 <= alpha_jk <= g_jk - 1 and
mu(U_jU_k) = alpha_jk / g_jk (E1 / L0.3); hence alpha_dc = alpha*_dc = 1 for c in O.

**Families.** For a configuration Gamma = (g_jU_j), its inversion is Gamma* := (g_j^-1 U*_j), U*_j := g_jU_jg_j^-1: pairwise
disjoint left cosets with the same indices and markers, with alpha-matrix alpha*(Gamma) (INV (a), (b), E6); (Gamma*)* = Gamma
(INV (a)). For z in {alpha, alpha*} the *z-configuration* is Gamma for z = alpha and Gamma* for z = alpha*, and z' is the other
family; so in both cases **the z'-configuration is the inversion of the z-configuration**, with alpha-matrix z'. Pi^z_j denotes
the subgroup of j in the z-configuration; for non-empty S in V, T_z(S) := [G : intersection of the Pi^z_j, j in S]; for a
triple R, tau_z(R) := T_z(R) / lcm(n_j : j in R).

**Fibres.** For a configuration (g_jU_j) with alpha-matrix x and a vertex v, the *fibres at v* are the n_v left cosets of U_v;
v's own coset g_vU_v is one of them. For a fibre F, S_F := {j != v : g_jU_j cap F != empty}. LFC (a)-(c) (LFC/INV verdict
item 1): g_jU_j meets exactly **deg_v(j) := n_v x_vj / g_vj** fibres, none of them g_vU_v (so S_(g_vU_v) is empty); the
label lambda_j := n_j x_vj / g_vj equals [U_v : U_v cap U_j]; and for every fibre F, S_F is *lambda-allowed*: every T in S_F
with |T| >= 2 has j != k in T with gcd(lambda_j, lambda_k) >= |T| (Sun(|T|) inside U_v).

**Rows.** An **R2-row** (the R2-instance of K62-MK-v2 section 0) is a family y whose four O-entries y_tu (u in O') lie in
{1, 2}. An **R1-instance** is (x; a, b): a family x and a != b in O' with x_ta = x_tb = 4, Pi^x_tPi^x_a = Pi^x_tPi^x_b and
x'_ta = x'_tb = 2.

## 1. Interface table (every import at its original scope)
| tag | exact statement used | source (path, sha256, location) | status / scope | used in |
|---|---|---|---|---|
| R0, L0.1, L0.2, L0.6 = Sun(2); Sun(3), Sun(4); Sun(5), Sun(6) | finite quotient; \|XY\| = \|X\|\|Y\|/\|X cap Y\|; disjointness criterion; Sun(k), k <= 6, in every group | `six-lane-20261016/sun-coset7/README.md` 2a6d6d6e…3fd1, lines 9-29; RUN-2026-10-16 written verdict 73a25ba6…9f35 lines 58-60 | accepted; Sun(5)/Sun(6) computer-assisted (2cf02436…5301, efe1d849…1e29), transitive | sections 0, 2-5 |
| E1 (L0.3) | lcm(n_j, n_k) divides [G : U_j cap U_k]; 1 <= alpha <= g - 1; mu(U_jU_k) = alpha / g | K7-LFC-INV-erratum-v1 7af9acf0…75bd5 lines 12-19; LFC/INV verdict 8621e744…cca18 line 31 | accepted, any disjoint pair | 0, 3, 4, 5 |
| LFC (a)-(d) | fibre counts deg_v(j); labels; allowed sets via Sun(t), t <= 6, inside U_v; count | K7-LFC-INV-v1 45be9162…726c lines 18-45 with erratum E3; verdict 8621e744 line 18 | accepted, k <= 7, finite G | 0, 3, 4 |
| INV (a)-(b), E6, E7 | inversion; alpha* = q; same class/markers; inverting twice returns | K7-LFC-INV-v1 lines 52-71; erratum lines 47-67; verdict line 19 | accepted | 0, 2, 4, 5 |
| R0 lift | quotient preserves indices, intersections, disjointness, conjugated intersections | verdict 8621e744 line 23 | accepted, arbitrary groups | 0 |
| L1 (T1)-(T3) | triangle divisibility and apex measure | rules-k7-v1.md 77b9afec…3cee lines 19-24; verdict 73a25ba6 line 23 ("Active triangle T … VFC … rules are sound necessary conditions") | accepted, general indices | Lemma 6 |
| VFC (V1)-(V4) | D_j = U_vg_jU_j disjoint from U_vU_j, measure q_j / g_vj, left U_v-invariant; right-coset Sun condition on d_j = q_jn_j / g_vj | rules-k7-v1.md lines 38-46; verdict 73a25ba6 lines 23, 34 | accepted | Theorem 7 |
| E3-a | every O-O entry of alpha and of alpha* lies in {1, 2, 4} | K62/K62-E3-erratum-v2.md f9f52e1b…dd4c lines 278-283 (Z11 (a); with K62-E3-v1 70a60d55…7372 Lemma 2, lines 36-55); E3 verdict 576969dd…bb0f lines 5, 25 | accepted only as the proof sub-claim Z11 (a) inside the accepted C2 proof (not a strengthened Lemma 2); its marker and orientation hypotheses hold in M3(1,1) for both families (orientation (1,1)) | Theorem 7 (ii), (iv) |
| E3 light fibres, C2 (b) | fibres in W*_Q U_d avoid Q; pair granularity | K62-E3-v1 lines 80-88; erratum v2 lines 284-290; E3 verdict line 22 | accepted at d in E3's direction; **re-proved here in general** (Lemmas 1, 3) | 2, 3 |
| RC (light-fibre row count) | general light-fibre arithmetic | K62/K62-CAP-DT-erratum-v1.md 996f924c…466d lines 131-154; CAP-DT verdict 84061c6f line 25 | accepted only as RC-O / RC-i* instances; general form "proof context" — **re-proved** (Lemma 1, Theorem R2X step 2) | 4 |
| setting | CAP section 0 | CAP-DT verdict 84061c6f line 21 | accepted | 0 |
| M3R-v2 Lemma A, Lemma C, RR | — | K62R/K62-M3R-v2.md af2b965b…88b3 lines 55-95; parent erratum cb42f3e7…34c7 | **PENDING** (one Codex family returned, second queued): **re-proved** here, not imported | 3, 5 |
| M3R-v2 R2N | — | K62-M3R-v2.md lines 121-150 | PENDING: **not used** (cross-reference only, section 7) | — |
| MK-v2 definitions, Theorem M3R | R1-/R2-instance definitions; every M3(1,1) configuration has an R1- or R2-instance | K62R/K62-MK-v2.md ab7cfcb6…abee9 lines 45-49, 230-234; parent erratum f84defc8…983b | **PENDING**: definitions repeated in section 0; M3R only as the CONDITIONAL premise of Corollary M3E | 0, 6 |

## 2. Two general lemmas (any finite configuration of pairwise disjoint left cosets)
**Lemma 1 (light fibres; re-proved).** Let (g_jU_j)_(j in V) be pairwise disjoint left cosets in a finite group G, v in V,
Q a non-empty subset of V minus {v}, and W := intersection of the g_jU_jg_j^-1 (j in Q). Then W g_vU_v is a union of fibres at
v containing g_vU_v; none of these fibres meets any g_jU_j with j in Q; and their number is at least n_v / gcd(n_v, [G : W]).
If (g_jU_j) is the z-configuration, then [G : W] = T_z'(Q).
*Proof.* W g_vU_v is the union of the left U_v-cosets w g_vU_v (w in W); w = 1 gives g_vU_v. Since w g_vU_v = w' g_vU_v iff
w^-1 w' lies in U*_v := g_vU_vg_v^-1, their number is [W : W cap U*_v] = [G : W cap U*_v] / [G : W] (Lagrange); [G : W cap U*_v]
is divisible by [G : U*_v] = n_v and by [G : W], hence by their lcm, so the number is at least n_v / gcd(n_v, [G : W]). If
w g_v u lay in g_jU_j (w in W, u in U_v, j in Q), write w = g_j b g_j^-1 with b in U_j; then g_j b g_j^-1 g_v u in g_jU_j gives
g_j^-1 g_v u in U_j, i.e. g_v u in g_jU_j cap g_vU_v = empty: impossible. Finally W is the Q-intersection of the subgroups of
the inverted configuration, which for the z-configuration is the z'-configuration (section 0). QED
(This is the argument of accepted K62-E3 section 4 step 3 and C2 (b), there at v = d in one direction, written here for any
vertex, any Q and either direction.)

**Lemma 2 (product separation) [NEW].** In the setting of Lemma 1 let v, j, k be distinct. If
(U_v cap U_j)(U_v cap U_k) = U_v, then no fibre at v meets both g_jU_j and g_kU_k.
*Proof.* Let p in g_jU_j cap F and q in g_kU_k cap F for a fibre F. Then F = pU_v = qU_v, so p^-1 q lies in U_v, and
g_jU_j = pU_j, g_kU_k = qU_k. Write p^-1 q = ab with a in U_v cap U_j and b in U_v cap U_k. Then pa = qb^-1 lies in
pU_j cap qU_k = g_jU_j cap g_kU_k = empty: impossible. QED

## 3. Three lemmas in M3(1,1)
**Lemma 3 (the d-system of either family).** Let z be a family and consider the z-configuration at d.
(a) Every c in O meets exactly n_d / 2 fibres, i* meets exactly n_d / 4 fibres, d's own fibre meets no other coset, and
|S_F| <= 3 for every fibre F.
(b) For c != c' in O: #{F : c, c' in S_F} = #{F : c, c' not in S_F} >= n_d / gcd(n_d, lcm(n_c, n_c') z'_cc'); if
z'_cc' lies in {1, 2}, the right side equals n_d / 2^(1 + v2 z'_cc') >= n_d / 4.
*Proof.* (a) z_dc = 1 (g_dc = 2) and z_(d i*) = 1 (orientation (1,1)), so deg_d(c) = n_d / 2 and deg_d(i*) = n_d / 4; d's own
fibre: LFC (b). Labels: lambda_c = n_c / 2 = 3^(f_c) 5^(h_c) w_c (c in O) and lambda_(i*) = n_(i*) / 4 = 3 * 5^(h*) w_*. Any
two of these six labels have gcd exactly 3 (each 3-exponent is >= 1 and at most one exceeds 1, since f* = 1 and only t has
f >= 2; at most one has a factor 5; w's coprime). A four-element allowed set would need a pair with gcd >= 4 (LFC (c), Sun(4)
inside the subgroup of d), so |S_F| <= 3. (This is the computation of accepted K62-E3 Lemma 1 with x = 1 and section 4
step 2.)
(b) Inclusion-exclusion over the n_d fibres: #{F : c, c' not in S_F} = n_d - deg_d(c) - deg_d(c') + #{F : c, c' in S_F}, and
deg_d(c) = deg_d(c') = n_d / 2, so the two numbers are equal. Lemma 1 with v = d and Q = {c, c'}: [G : W] = T_z'({c, c'}) =
lcm(n_c, n_c') z'_cc', and the at least n_d / gcd(n_d, [G : W]) fibres it provides meet neither c nor c'. If z'_cc' is 1 or 2,
the gcd has 2-part 2^(min(e_d, 1 + v2 z'_cc')) = 2^(1 + v2 z'_cc'), 3-part 1 (3 does not divide n_d), 5-part 1 (if h_d >= 1
then h_c = h_c' = 0, and 5 does not divide z'_cc'), and w-part 1. QED (Part (b) is accepted K62-E3 C2 (b) of erratum v2 Z11,
re-derived because both family directions are used below.)

**Lemma 4 (the chain at t; K62-M3R-v2 Lemma C, re-proved).** Let z be a family, Pi_j := Pi^z_j and T := T_z(V minus {t}).
(a) For any order d, i*, e_1, ..., e_4 of V minus {t}: T = lcm(n_d, n_(i*)) * product over e in O' of (ell_e k_e) with
integers k_e in {1, 2, 3} defined by the chain below; v3 T = 1 + #{e in O' : k_e = 3}; and
gcd(n_t, T) = 2 * 3^(min(f_t, v3 T)).
(b) If k_e = 3, then Pi_e(Pi_d cap Pi_(i*)) = Pi_ePi_d and (Pi_d cap Pi_e)(Pi_d cap Pi_(i*)) = Pi_d.
(c) For e in O': |(Pi_d cap Pi_e)(Pi_d cap Pi_(i*))| / |Pi_d| = tau_z({d, i*, e}) / 3. So tau_z({d, i*, e}) <= 3, with equality
iff (Pi_d cap Pi_e)(Pi_d cap Pi_(i*)) = Pi_d.
(d) Hence: if 9 divides T, some e in O' has (Pi_d cap Pi_e)(Pi_d cap Pi_(i*)) = Pi_d (equivalently tau_z({d, i*, e}) = 3);
if no e in O' has it, then gcd(n_t, T) = 6.
*Proof.* (a) S_0 := {d, i*}, S_r := S_(r-1) plus e_r, W_r := intersection of the Pi_j (j in S_r), T_r := [G : W_r].
T_0 = lcm(n_d, n_(i*)) z_(d i*) = lcm(n_d, n_(i*)) (orientation (1,1)); v3 T_0 = 1. Step r, e := e_r: n_e and T_(r-1) divide
T_r (Lagrange), so T_r = lcm(n_e, T_(r-1)) k_e with k_e a positive integer, and L0.1 gives
mu(Pi_eW_(r-1)) = T_r / (n_e T_(r-1)), i.e. k_e = gcd(n_e, T_(r-1)) mu(Pi_eW_(r-1)). Inductively T_(r-1) =
lcm(n_d, n_(i*)) * product over s < r of (ell_(e_s) k_(e_s)) with every k <= 3; then gcd(n_e, T_(r-1)) = 6: n_e = 2 * 3 * 5^(h_e) w_e,
4 and 3 divide T_(r-1); if h_e >= 1, e is the only 5-marked vertex, so n_d, n_(i*), the earlier ell's and the k's <= 3 are
5-free; w_e is coprime to every other factor. So lcm(n_e, T_(r-1)) = ell_e T_(r-1) and k_e = 6 mu(Pi_eW_(r-1)) <=
6 mu(Pi_ePi_d) = 6 z_ed / g_ed = 3, as W_(r-1) lies in Pi_d. Since ell_e is prime to 3, v3 T_r = v3 T_(r-1) + [k_e = 3]. For the
gcd: n_t = 2 * 3^(f_t) 5^(h_t) w_t; the 2-part is 2 (4 divides T), the 3-part 3^(min(f_t, v3 T)), the 5-part 1 (if h_t >= 1 every
factor of T is 5-free), the w-part 1.
(b) k_e = 3 gives mu(Pi_eW_(r-1)) = 1/2 = mu(Pi_ePi_d); as W_(r-1) lies in Pi_d cap Pi_(i*), Pi_eW_(r-1) lies in
Pi_e(Pi_d cap Pi_(i*)), which lies in Pi_ePi_d; equal cardinalities make all three equal. For x in Pi_d write x = ab with a in Pi_e,
b in Pi_d cap Pi_(i*); then a = xb^-1 lies in Pi_d, so x lies in (Pi_d cap Pi_e)(Pi_d cap Pi_(i*)).
(c) In the group Pi_d put A := Pi_d cap Pi_e, B := Pi_d cap Pi_(i*). LFC (a): [Pi_d : A] = n_e z_de / g_de = 3 ell_e and
[Pi_d : B] = n_(i*) z_(d i*) / g_(d i*) = 3 * 5^(h*) w_*; and [Pi_d : A cap B] = T_z({d, e, i*}) / n_d =
tau * lcm(n_d, n_e, n_(i*)) / n_d = tau * 3 * 5^(h_e + h*) w_e w_* (at most one of h_d, h_e, h* is positive). By L0.1 in Pi_d,
|AB| / |Pi_d| = [Pi_d : A cap B] / ([Pi_d : A][Pi_d : B]) = tau / 3.
(d) 9 | T means v3 T >= 2, so some k_e = 3; apply (b), (c). If no e has the equality, (b) excludes k_e = 3, so v3 T = 1 and
gcd(n_t, T) = 6 by (a). QED

**Proposition 5 (mixed-family d-count) [NEW].** Let y be a family. Work in the **y'-configuration at d**, put
s := #{F : t, i* in S_F} and N_u := #{F : t, u in S_F} (u in O').
(a) Let e in O'. If y_tu lies in {1, 2} for the three u in O' minus {e}, then some fibre at d meets both e and i*;
consequently (Pi^(y')_d cap Pi^(y')_e)(Pi^(y')_d cap Pi^(y')_(i*)) != Pi^(y')_d, and tau_y'({d, i*, e}) lies in {1, 2}.
(b) If y is an R2-row, then y_tu = 2 for every u in O', s = 0, N_u = n_d / 4 for every u in O', every fibre at d meeting t has
S_F = {t, u, u'} with u != u' in O', and (a) applies to every e in O'.
*Proof.* Lemma 3 (a) for the family y' (whose other family is y): t and each u in O' meet n_d / 2 fibres, i* meets n_d / 4,
every |S_F| <= 3, and d's own fibre F_d has S_(F_d) empty.
(i) Counting the pairs (F, u) with t, u in S_F: sum over u in O' of N_u = sum over F with t in S_F of |S_F cap O'|. Such an S_F
lies in {t, i*} cup O' and has at most 3 elements, so |S_F cap O'| <= 2 - [i* in S_F]; summing over the n_d / 2 fibres meeting
t: **sum over u in O' of N_u <= n_d - s.**
(ii) Lemma 3 (b) for the family y' (so z' = y): **N_u >= n_d / 2^(1 + v2 y_tu)** whenever y_tu lies in {1, 2}.
(a) Suppose no fibre at d meets both e and i*. By (i) and (ii) for the three u != e: N_e <= n_d - s - 3 n_d / 4 = n_d / 4 - s.
A fibre meeting e but not t then meets neither t nor i*, and it is not F_d. The fibres meeting neither t nor i* number
n_d - n_d / 2 - n_d / 4 + s = n_d / 4 + s, and F_d is one of them. Hence
deg_d(e) <= (n_d / 4 - s) + (n_d / 4 + s - 1) = n_d / 2 - 1 < n_d / 2 = deg_d(e): a contradiction. The consequences follow from
Lemma 2 (v = d, j = e, k = i*, in the y'-configuration) and Lemma 4 (c) for z = y'.
(b) By (ii), sum over u of N_u >= 4 (n_d / 4) + (number of entries y_tu = 1) * n_d / 4; with (i) this is <= n_d - s. So no entry
is 1, s = 0, every N_u equals n_d / 4 (each is >= n_d / 4 and their sum is <= n_d), and (i) is an equality fibre by fibre:
every fibre meeting t has |S_F cap O'| = 2 and does not meet i*. The hypothesis of (a) holds for every e in O'. QED

## 4. Theorem R2X [NEW; CANDIDATE_UNVERIFIED]
**Statement.** No configuration of M3(1,1) — e_d >= 4, f_t >= 2, every admissible 5-marker position (d, i*, t, p in O', or
none), all exponents and w-parts unbounded, in any group with finite-index subgroups — has an R2-row: there is no family y
with y_tu in {1, 2} for all four u in O'. This is the lemma (L-R2) of K62-M3R-v2 section 7 (c) and K62-MK-v2 section 7 (b).
*Proof.* By R0 let G be finite. Let y be an R2-row, let (g_jU_j) be the y-configuration (alpha-matrix y) and recall that the
y'-configuration is its inversion (section 0).
- *Step 1 (granularity 6 at t for y').* By Proposition 5 (b) and (a), no e in O' has
  (Pi^(y')_d cap Pi^(y')_e)(Pi^(y')_d cap Pi^(y')_(i*)) = Pi^(y')_d. By Lemma 4 (d) for z = y',
  gcd(n_t, T_y'(V minus {t})) = 6.
- *Step 2 (light fibres at t).* Lemma 1 for the y-configuration with v = t and Q = V minus {t}: [G : W] = T_y'(V minus {t}), so
  at least n_t / 6 fibres at t meet no coset g_jU_j (j != t).
- *Step 3 (the count at t).* By Proposition 5 (b), y_tu = 2 for u in O'; y_td = 1. In the y-configuration at t the labels are
  lambda_u = n_u * 2 / 6 = 2 ell_u (u in O') and lambda_d = n_d / 2 = 2^(e_d - 1) 5^(h_d) w_d, and any two of these five have gcd
  exactly 2 (odd parts pairwise coprime: the ell_u (u in O') are prime to 3 and to each other, a 5 lies on at most one
  vertex, w's coprime). Put c_j := 1/2 for j in O' cup {d} and c_(i*) := 0. For every fibre F, S_F is allowed (LFC (c)), and an
  allowed set contains at most two vertices of O' cup {d}: three of them would form an allowed 3-subset (heredity), which needs
  a pair with gcd >= 3 (Sun(3) inside U_t). So the sum of c_j over j in S_F is at most 1 for every fibre, and it is 0 on the
  fibres of Step 2. Double counting incidences (LFC (a)-(b)):
  n_t * sum over j of c_j y_tj / g_tj = sum over j of c_j deg_t(j) = sum over fibres F of (sum over j in S_F of c_j)
  <= n_t - n_t / 6.
  The left side is n_t (4 * (1/2)(2/6) + (1/2)(1/2)) = 11 n_t / 12 > 10 n_t / 12. Contradiction. QED
*Remarks.* (1) The entry y_(t i*) is never used; neither are Lemma A nor R2N. Nothing is imported from K62-E3 here: the two
E3 facts used (the three-piece cap at d and pair granularity at d) are re-derived in Lemma 3. (2) Step 3 is the certificate c0
of K62-MK-v2 Lemma R4* at granularity 6 (pending there), re-done here with the light-fibre count of Lemma 1; what was missing
was granularity 6 at t, i.e. Step 1, which Proposition 5 supplies.

## 5. R1-instances
**Lemma 6 (K62-M3R-v2 Lemma A, re-proved).** For a family z: if z_(t i*) = 5, then h_d >= 1.
*Proof.* L1 for the triangle {d, i*, t} in the z-configuration, tau := T_z({d, i*, t}) / lcm(n_d, n_(i*), n_t). (T1) for the
edge t i*: z_(t i*) divides (n_d / gamma_d) tau with gamma_d = gcd(n_d, lcm(n_t, n_(i*))) = lcm(g_dt, g_(d i*)) = 4, i.e.
5 divides 2^(e_d - 2) 5^(h_d) w_d tau. (T3) with (T2) at apex t: tau / (gamma_t z_(d i*)) = mu(Pi_t(Pi_d cap Pi_(i*))) <=
mu(Pi_tPi_d) = 1/2, with gamma_t = lcm(g_td, g_(t i*)) = 6 and z_(d i*) = 1; so tau <= 3 and 5 does not divide tau. Hence
h_d >= 1. QED

**Theorem 7 (K62-M3R-v2 Theorem RR, re-proved in the form needed).** If (x; a, b) is an R1-instance, then x'_tu = 2 for every
u in O'; so x' is an R2-row.
*Proof* (the argument of K62-M3R-v2 section 3, steps 1-4). Let (g_jU_j) be the x-configuration (U_j = Pi^x_j), left-translated
so that g_t = 1; subgroups are unchanged, so X_j := U_tU_j has mu(X_j) = x_tj / g_tj. VFC at v = t ((V1)-(V4); q_j = x'_tj by
INV (b), as the inversion of the x-configuration is the x'-configuration): D_j := U_t g_j U_j (j != t) is disjoint from X_j, has
measure x'_tj / g_tj and is a union of right cosets U_t y; and for a right coset R, every T in S_R := {j : R in D_j} with
|T| >= 2 contains j != j' with gcd(d_j, d_j') >= |T|, where d_j = n_j x'_tj / g_tj: d_u = ell_u x'_tu (u in O'),
d_(i*) = 2 * 5^(h*) w_* x'_(t i*), d_d = n_d / 2. Ranges: x'_tu in {1, 2, 4} for u in O' (E3-a), 1 <= x'_(t i*) <= 5 (E1),
x'_td = 1. Two unions of right U_t-cosets meet only if some right coset lies in both.
(i) D := G minus X_a has measure 2/6 and contains D_a, of measure x'_ta / 6 = 2/6; so D_a = D, and likewise
D_b = G minus X_b = D (X_a = X_b).
(ii) For j in V minus {t, a, b}, D cap D_j is empty: otherwise a right coset R has {a, b, j} in S_R, which needs a pair with
gcd >= 3. But gcd(d_a, d_b) = gcd(2 ell_a, 2 ell_b) = 2, and gcd(d_a, d_j) <= 2: for j in O', d_j = ell_j x'_tj with x'_tj a
power of 2 and ell_j coprime to ell_a; for j = d, the odd part 5^(h_d) w_d is coprime to ell_a = 5^(h_a) w_a (one 5-marker);
for j = i*, the odd part of d_(i*) divides 3 * 5^(h* + 1) w_*, coprime to ell_a unless h_a >= 1 and x'_(t i*) = 5, and that
is excluded because h_a >= 1 forces h_d = 0 while x'_(t i*) = 5 forces h_d >= 1 (Lemma 6 for z = x'). The same holds for b.
(iii) W_t := intersection of the U_j (j != t) and L := U_tW_t, a union of right U_t-cosets containing U_t and lying in every
X_j, hence disjoint from every D_j (V1) and from D. R := G minus (D cup L) has mu(R) <= 1 - 2/6 - 1/n_t < 4/6, and by (ii)
D_j lies in R for every j not in {t, a, b}; mu(D_d) = 1/2.
(iv) Let c in O' minus {a, b}. If x'_tc = 4, then mu(D_c) = 4/6 > mu(R): impossible. If x'_tc = 1, then d_c = ell_c and d_d are
coprime, so no right coset lies in D_c cap D_d ((V3) with |T| = 2, Sun(2)); D_c lies in R minus D_d, and
1/6 = mu(D_c) <= mu(R) - 1/2 < 1/6: impossible. So x'_tc = 2 for both such c, and x'_ta = x'_tb = 2 by hypothesis. QED

**Corollary R1X [CANDIDATE_UNVERIFIED].** No configuration of M3(1,1) (same full scope as Theorem R2X) has an R1-instance.
*Proof.* Theorem 7 and Theorem R2X. QED

## 6. Corollaries for the K62-MK-v2 residual
- **6.1 [CANDIDATE_UNVERIFIED].** Every configuration of M3(1,1) satisfies hypothesis NR of K62-MK-v2 section 0 (no
  R1-instance and no R2-instance). (R1X and R2X; NR is a definition, not an import.)
- **6.2 Corollary M3E (CONDITIONAL ON K62-MK-v2 Theorem M3R = Theorem 6.4, PENDING; read with parent erratum f84defc8…).**
  If every configuration of M3(1,1) has an R1-instance or an R2-instance, then M3(1,1) has no configuration. *Proof.* 6.1.
  Navigation only: nothing is stated here about M13, the remaining K6.2* classes, K7 or Sun(7).

## 7. What is new, and how the recorded obstruction is passed
- The obstruction note of K62-M3R-v2 section 7 (b) (with parent erratum m1-m5) records single-family, t-local routes: the
  displayed LFC certificate value 11/2 (units 1/6), the light-fibre bound once tau_y'({d, i*, e}) = 3 gives granularity 18,
  the incidence count E <= n_t / 12, MK's structural route, and the W6 subgroup argument. None of them is repeated as progress
  here; Step 3 is the old certificate, and it now suffices because Step 1 removes granularity 18.
- **New ingredients:** (1) Lemma 2 turns the opposite-family product equality (Pi'_d cap Pi'_e)(Pi'_d cap Pi'_(i*)) = Pi'_d
  (equivalently Pi'_e(Pi'_d cap Pi'_(i*)) = Pi'_ePi'_d, equivalently tau_y'({d, i*, e}) = 3; Lemma 4 (b), (c)) into a statement
  about **occupied fibres**: e and i* never share a d-fibre of the y'-configuration. (2) Proposition 5 couples this with the
  three-piece cap of the y'-d-system (Lemma 3 (a)) and with the pair granularity carried from y to the d-fibres of y'
  (Lemma 3 (b)): the R2 entries y_tu force at least n_d / 4 d-fibres shared by t and each u in O', which saturates the d-fibres
  of t and leaves e too few fibres, missing exactly d's own fibre. The contradiction needs both families: y at t (Steps 2-3)
  and y' at d (Proposition 5).
- **Relation to pending R2N.** Proposition 5 shows that an R2-row has tau_y'({d, i*, e}) <= 2 for every e in O'; K62-M3R-v2
  R2N (iii) (pending) asserts that an R2-row has tau_y'({d, i*, e}) = 3 for some e. Their conjunction is a second route to
  R2X; the proof above does not use R2N.
- **Necessary fact beyond R2-rows:** Proposition 5 (a) is not vacuous after R2X: for any family y and e in O' whose three
  t-entries y_tu (u != e) lie in {1, 2} (for example with y_te = 4), tau_y'({d, i*, e}) lies in {1, 2}. Proposition 5 (b) is
  vacuous after R2X.

## 8. Mutation checks (thought experiments; nothing run)
1. *Drop Lemma 2* (allow e and i* to share d-fibres): in Proposition 5 (a) the fibres meeting e but not t are bounded only by
   n_d / 2 - 1, so deg_d(e) <= 3 n_d / 4 - s - 1, no contradiction. The opposite-family product equality is load-bearing.
2. *Use one family only.* If the d-system of the y-configuration itself were used, Lemma 3 (b) would give N_u >= n_d /
   2^(1 + v2 y'_tu) with y'_tu in {1, 2, 4} not constrained by the R2 hypothesis (only n_d / 8 when y'_tu = 4), so (i)-(ii) force
   nothing; and the granularity needed at t (Step 1) concerns T_y', whose product equalities live in the y'-configuration, so
   separation in the y-configuration would not help. The proof needs y at t and y' at d.
3. *Drop Sun(4) at d* (four pieces per d-fibre): (i) weakens to sum of N_u <= 3 n_d / 2 - s, and the four lower bounds n_d / 4
   force nothing.
4. *Only three R2 entries:* Proposition 5 (a) for a given e uses the three entries off e only; Step 1 needs it for every
   e in O', hence all four entries; Step 3 uses all four entries equal to 2 (Proposition 5 (b)).
5. *Drop Step 2* (light fibres at t): 11/12 < 1 is compatible with plain LFC (d) (K62-M3R-v2 obstruction (1), erratum m1).
6. *Granularity 18 at t* (some tau_y' = 3): Step 3 gives only 11/12 <= 17/18, no contradiction (K62-MK-v2 mutation (1)); this
   is exactly the case Proposition 5 excludes.
7. *Drop d's own fibre* in Proposition 5 (a): the count gives deg_d(e) <= n_d / 2, no contradiction; the deficit of one is d's
   own coset (LFC (b)).
8. *Orientation (3,1) or (1,3)* (y'_(d i*) = 3): i* would meet 3 n_d / 4 d-fibres and the labels of t and i* at d would have
   gcd 9, so four-element allowed sets {t, i*, c, c'} may occur and Lemma 3 (a) fails. Nothing is claimed there (M13 untouched).

## 9. Scope, provenance, verification boundary
- **Claimed (all CANDIDATE_UNVERIFIED, written, single author):** Lemma 2, Proposition 5, Theorem R2X, Corollary R1X,
  Corollary 6.1 (new); Lemmas 1, 3, 4, 6 and Theorem 7 (re-proved; arguments of accepted K62-E3 and of pending K62-M3R-v2 /
  K62-MK-v2, attributed); Corollary M3E only CONDITIONAL ON K62-MK-v2 Theorem M3R.
- **Not claimed:** acceptance of K62-MK-v2 or K62-M3R-v2; anything about M13 ((1,3)/(3,1)), M5, G, the rest of K6.2*, K7 or
  Sun(7); novelty, priority, significance, Lean, human review.
- **Sun provenance.** Direct new Sun instances: Sun(2) (Theorem 7 (iv), via (V3)); Sun(3) (Theorem R2X step 3 inside U_t via
  LFC (c); Theorem 7 (ii) via (V3)); Sun(4) (Lemma 3 (a) inside the d-subgroup via LFC (c)). Through the import E3-a: Sun(2).
  The accepted LFC/VFC package cites Sun(t), t <= 6, and the K6.2* class reduction uses the computer-assisted Sun(5)
  (2cf02436…5301) and Sun(6) (efe1d849…1e29); both stay in the transitive closure. FH and Sun(7) are not used.
- **Dependency order:** Lemma 1, Lemma 2 -> Lemma 3 -> Lemma 4 -> Proposition 5 -> Theorem R2X; Lemma 6 -> Theorem 7 ->
  Corollary R1X -> 6.1 -> 6.2 (conditional).
- No computation, enumeration, novelty, priority, Lean or human-review claim.
