# K62-CAP-v1: Lemma CAP-62 — pattern representation for the K6.2* residue e_d >= 4, e* = 2 [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:23:44-0700.
- **Author:** Sun63Successor; single author, unreviewed; written only (HOLD 6c1d8440… in force; nothing run).
- **Purpose:** the completeness lemma named in `K62-ARCH-v1.md` (sha256
  b0f5face7242ce572aa4d0b011b463e808fd4a97978b59a4449a30fe7383cf03): every configuration of the residue is represented by
  a pattern in a finite set U62, and the quantities read by the rules are functions of the pattern. It proves no
  exclusion by itself.
- **Imports (accepted, at these scopes):** R0 (old README section 1); the K6.2* class definition with P0/P1 (old README
  sections 2, 5); old README section 0 L0.1 (|XY| = |X||Y|/|X cap Y|) with Lagrange; `K7-LFC-INV-erratum-v1.md` E1
  (1 <= alpha <= g - 1); LFC (a)-(d) and INV (a)-(b) with E6 (verdict sha256
  8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18); rules-k7-v1 L1 (T rule: (T1)-(T3), tau_min, tau_max),
  VFC (V1)-(V4) with the count, and section 4 Lemma CAP (its capping argument), accepted in
  `six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` (sha256
  73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35); K62-E3 with errata v1-v2 (verdict sha256
  576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f): Lemma 1, Lemma 2, C2 sub-claim (a), Lemma 3 in its
  proof form for every non-empty Q contained in O. **Not used:** K62-DG, K62-SH, K62-FG (whose chain lemma is re-proved
  below in the form needed), any computation.

## 0. Setting
Class K6.2* with e_d >= 4 (so e* = 2): V = {d, i*} disjoint-union O, |O| = 5; n_d = 2^(e_d) 5^(h_d) w_d;
n_(i*) = 4 * 3^(f*) 5^(h*) w_*; n_c = 2 * 3^(f_c) 5^(h_c) w_c (c in O); w's pairwise coprime and coprime to 30; at most
one vertex with f >= 2 (m3; if m3 lies in O call it t, and then f* = 1) and at most one with h >= 1 (m5; if in O call
it p). Families: Phi^alpha = (U_j) and Phi^alpha* = (U*_j), U*_j := g_jU_jg_j^-1 (indices n_j; a common left translation
conjugates Phi^alpha* by one element and changes no index below). For a family x in {alpha, alpha*} and non-empty S in V:
T_x(S) := [G : intersection of Phi^x_j, j in S]. For a triangle R: tau_x(R) := T_x(R) / lcm(n_j : j in R).

## 1. Definition (the pattern pi(Gamma) of a configuration Gamma)
- (pi1) Marker data: m3 in {i*} cup O cup {none}, m5 in {d, i*} cup O cup {none}, with capped exponents
  min(f_(m3), 2), min(h_(m5), 2), and **e^_d := min(e_d, 10)**.
- (pi2) The joint matrix (alpha_jk, alpha*_jk) for all 21 pairs of V.
- (pi3) tau_x(R) for every triangle R in V and x in {alpha, alpha*}.
- (pi4) delta_x(Q) := v2(T_x(Q)) for every Q in O with |Q| in {4, 5} and x in {alpha, alpha*}.

## 2. Lemma CAP-62
**(A) Ranges.** pi(Gamma) lies in the finite set U62 of tuples with:
- (A1) finitely many marker data (class constraints of section 0);
- (A2) d-O entries (1, 1); d-i* entry in {(1,1), (1,3), (3,1)}, and different from (1,1) only if m3 = t lies in O
  (K62-E3 Lemma 1); O-O entries in J_O = {(a, b) in {1,2,4}^2 : a + b <= 6} (K62-E3 Lemma 2 and C2 sub-claim (a));
  i*-O entries with 1 <= alpha, alpha* and alpha + alpha* <= 6 (E1, INV (b));
- (A3) tau_x(R) a multiple of tau_min in [tau_min, tau_max], both computed from (pi1, pi2) (L1);
- (A4) 1 <= delta_x(Q) <= 9.
*Proof of (A4).* n_c is even, so v2 >= 1. Upper bound (K62-E3 Lemma 3 proof, valid for x = alpha and x = alpha* since
both families have [G : Phi_j cap Phi_k] = lcm(n_j, n_k) x_jk): order Q with its marked vertices first; T over one
vertex has v2 = 1; a starting pair of marked vertices t != p gives lcm(n_t, n_p) x_tp with v2 <= 1 + 2; each further
(unmarked) vertex e multiplies by an integer k <= min x_(ej) <= 4 (L0.1, Lagrange, gcd(n_e, T) = 6), adding at most 2 to
v2. So v2 <= 1 + 2(|Q| - 1) <= 9. QED

**(B) Determination.** Each of the following is a function of pi(Gamma):
- (B1) all g_jk, all gamma_y, and every gcd(x_xy, ell_z) entering tau_min (ell_z = n_z / gamma_z);
- (B2) at every vertex v and orientation x, the gcd of any two LFC labels lambda^x_j = n_j x_vj / g_vj (equivalently the
  VFC local indices of the other orientation);
- (B3) tau_min, tau_max, every apex measure mu(Phi_y(Phi_x cap Phi_z)) = tau_x(xyz) / (gamma_y x_xz) (L1 (T3)) and every pair
  measure mu(Phi_xPhi_y) = x_xy / g_xy (L0.1);
- (B4) at d, for every non-empty Q in O: gcd(n_d, T_x(Q)) = 2^(min(e_d, v2 T_x(Q))) (K62-E3 Lemma 3 proof form), with
  v2 T_x(Q) = 1, 1 + v2 x_ab, 1 + v2 tau_x(R), delta_x(Q) for |Q| = 1, 2, 3, >= 4; since v2 T_x(Q) <= 9 by (A4),
  min(e_d, v2 T_x(Q)) = min(e^_d, v2 T_x(Q));
- (B5) the fibre counts at every vertex v: t_j / n_v = x_vj / g_vj (LFC (a)).
*Proof of (B1), (B2).* The w-parts are pairwise coprime, coprime to 30 and to every entry <= 5, so only {2,3,5}-parts
matter. 2-parts: v2 n_c = 1, v2 n_(i*) = 2, v2 n_d = e_d; at an O-vertex the d-label has 2-part 2^(e_d - 1) >= 8 and every
other label has 2-part <= 2^(1 + v2 4) = 8; at i* the d-label has 2-part >= 2^(e_d - 2) >= 4 and the O-labels <= 4; at d the
labels do not involve n_d. So every gcd involving e_d is the same for all e_d >= 4. 3- and 5-parts: only m3 (resp. m5)
has exponent >= 2 (resp. >= 1); every other label in a gcd with it has 3-part (resp. 5-part) <= 3 (resp. 5), so the gcd
depends on f_(m3) (resp. h_(m5)) only through min(., 2), as in rules-k7-v1 Lemma CAP. gamma and ell-gcds likewise. QED
(B3)-(B5) are the cited identities.

**(C) Two global granularity bounds (proved here).**
- (C1) Let v in O be unmarked and x a family with x_(d i*) = 1. Then gcd(n_v, T_x(V minus {v})) divides 6.
- (C2) If f* = 1, then gcd(n_(i*), T_x(V minus {i*})) divides 12, for both families.
*Proof.* Write T_m for the index of the running intersection; T_(m+1) = lcm(n_e, T_m) k with k / gcd(n_e, T_m) =
mu(Phi_e W_m) <= mu(Phi_e Phi_j) for every earlier j (L0.1, Lagrange). It suffices that every k has no prime > 5 (then
the prime-to-30 part of the final index is the product of the w_j, coprime to w_v resp. w_*).
(C1) order d, i*, t, p, then the unmarked rest (omit absent vertices). T_2 = lcm(n_d, n_(i*)) x_(d i*) = lcm(n_d, n_(i*)).
Adding t (then f* = 1): gcd(n_t, T_2) = 2 * 3 (v3 T_2 = f* = 1; no common 5: if t is 5-marked then h_d = h* = 0), so
k <= 6 * (x_td / 2) = 3. Adding p != t: T_m has no factor 5 (d, i*, t are not 5-marked and all k <= 3), so
gcd(n_p, T_m) = 6 and k <= 3. Adding an unmarked e: gcd(6 w_e, T_m) = 6 and k <= 3. (Without the hypothesis x_(d i*) = 1,
v3 T_2 could be 2 and the step for t would only give k <= 9.)
(C2) order d, t, p, unmarked rest. Adding t: gcd(n_t, n_d) = 2, k <= 2 * (1/2) = 1. Adding p != t: gcd(n_p, lcm(n_d, n_t)) = 6,
k <= 3. Unmarked: gcd 6, k <= 3. Then gcd(n_(i*), T): 2-part min(2, v2 T) = 2 (v2 T >= e_d); 3-part 3^(min(f*, v3 T)) = 3
(f* = 1, v3 T >= 1); 5-part 1 (if h* >= 1, neither d nor an O-vertex is 5-marked and all k <= 3). QED
*Consequences (used by rules R1).* With the light-set argument of K62-E3 step 3 (and its VFC analogue: U_vW is
contained in every U_vU_j, hence disjoint from every D_j by (V1)): at an unmarked v in O, the alpha-row count holds with
bound 5/6 when alpha*_(d i*) = 1 (granularity of Phi^alpha*), and the alpha*-row count holds with bound 5/6 when
alpha_(d i*) = 1 (granularity of Phi^alpha); at i*, if f* = 1, both counts hold with bound 11/12.

**(D) Transfer.** Call a *rule* a statement, proved from accepted imports, of the form "every configuration Gamma of
the residue satisfies P(pi(Gamma))" with P a predicate on U62 built from the quantities in (B) and the bounds in (C).
If every element of U62 violates some rule, the residue has no configuration in any finite group, hence (R0) in any
group. QED

## 3. Scope and limits
- Not covered: grids of proper subsets at O-vertices or at i* (atom-level "6-point" or "12-point" models); a rule using
  them needs its own lemma (for example a chain for every subset S, which (C1) does not provide when d is not in S).
- The universe U62 is finite but large; CAP-62 makes no claim that its elements are all excluded. Full K6.2*
  (e_d >= 4) and full Sun(7) remain OPEN. No novelty claim.
