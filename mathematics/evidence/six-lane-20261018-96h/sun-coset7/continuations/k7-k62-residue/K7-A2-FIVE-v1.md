# K7-A2-FIVE: in (a2) a five can only sit on z-t, with a forced z-row; granularity and 3-type z-rows in (a2); without fives, (a2) carries the (a1) data with W = W' cup {p}

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:33:35-0700.
- **Owner:** Sun7K62Successor (continuation `k7-k62-residue`). Single author, unreviewed. No computation was run; no probe
  is a premise. "[NEW]" = written here, not a novelty claim.
- **Status:** CANDIDATE written mathematics. Sections 1-4 import only accepted results; Corollary K7-A2-TRANSFER
  (section 4) is **conditional** on the unreviewed candidates K7-A1-STRUCT, K7-TC and K7-TC-A22. (a2) is NOT excluded;
  full Sun(7) remains OPEN.

## 0. Setting and imports

**Setting (a2).** Class K7 with three distinct marked vertices, r_z = 2^E w_z, r_t = 3^A w_t, r_p = 5^B w_p (E, A, B >= 1,
actual and unbounded), and W' := V \ {z, t, p}, four unmarked vertices (n_u = 6 w_u); the w's are pairwise coprime and
prime to 30, and every pair of indices has gcd 6. alpha, alpha* are symmetric, 1 <= alpha, alpha* <= 5 and
alpha + alpha* <= 6. x ranges over {alpha, alpha*} and x* is the other one; C^alpha is the configuration and C^alpha* its
inverse (INV (a), E6: same labelled indices and markers; alpha** = alpha). At an apex v of C^x the label of j is r_j x_vj;
y >= 0 is feasible if its sum over every allowed set is <= 1 (allowedness is hereditary, so zero weights can be ignored);
val(y) := sum_j y_j x_vj, and LFC (d) gives val(y) < 6. At u in W' write c := x_uz and e := x_ut.
**Label facts.** r_j x_vj is divisible by 5 iff j = p or x_vj = 5, by 3 iff j = t or x_vj = 3, by 2 iff j = z or
x_vj in {2, 4}; the w's never enter a gcd (entries <= 5).

**Accepted imports (exact uses).**
- `K7-D23P-v1.md` (sha256 89739dc2de4d174ab695146a4c6bd781e09044732cbdbb10269bfb497e337880) with
  `K7-D23RICH-D23P-erratum-v1.md` (sha256 55cb66ca55008fa7219451d2e45458726282abce618cdcdba134a7d97a94d428), accepted by
  `RUN/review/sun7-K7-D23RICH-D23P-parent-verdict-v1.md` (sha256 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0).
  Used: for each x, **x_zu in {1,2,3} (u in W'), at least two u in W' have x_zu = 3, x_zt != 4, and if exactly two do,
  then x_zp = 3 and the two other W'-entries are equal and lie in {1,2}.**
- `K7-D23-RICH-v1.md` (sha256 ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3) with erratum-1
  (sha256 8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69) and the consolidated erratum, same verdict:
  G0, the proof of FG7 (chain form) and the proof of Corollary 5/6 (re-run in section 2), and, for section 4, all its
  statements and proofs.
- LFC (a)-(d), INV (a)-(b), E1, E2, E6, E7, E8 (`K7-LFC-INV-v1.md` + erratum; verdict sha256
  8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18, item 6 for R0); L0.1, L0.3, L1 (tau_min/tau_max) and
  VFC (V1)-(V4) of `rules-k7-v1.md` (written verdict sha256 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35).
- Direct Sun instances: Sun(2), Sun(3), Sun(4), only through LFC (c). Transitive closure as recorded in the RICH/D23P
  verdict (it reaches the computer-assisted Sun(5)/Sun(6) records). No Sun(7), no computation.

## 1. Lemma F (fives) [NEW]

For x in {alpha, alpha*}:
- **(F1)** x_uv != 5 for u != v in W'.
- **(F2)** x_up != 5 for u in W'.
- **(F3)** x_zp != 5; and if x_zt = 5, then x_zu = 3 for every u in W' and x_zp = 3.
- **(F4)** x_tp != 5.
- **(F5)** If x_zt = 5, then x_tu is not in {1, 3} (u in W').
- **(F6)** x_ut != 5 for u in W'.
- **(F7)** If x_zt = 5, then x_tu in {2, 4} for every u in W', and x_tp in {1, 2, 4}.
Consequently **the only entry of alpha or alpha* that can equal 5 is the z-t entry, in at most one orientation**
(x_zt + x*_zt <= 6).

*Proofs.* Each item exhibits a feasible y with val(y) >= 6, against LFC (d) of C^x, unless stated otherwise.

(F1) At u in W': c in {1,2,3} (D23P). Let F5 := {v in W' \ {u} : x_uv = 5}, assumed non-empty. A label 5 w_v (v in F5) has
gcd 1 with z's label 2^E c w_z and with every W'-label whose entry is not 5, so an allowed set meeting F5 has its other
positive-weight elements inside F5. If |F5| <= 2, pick b in W' \ ({u} cup F5): y = 1/|F5| on F5 and y_b = 1:
val >= 5 + 1. If |F5| = 3: y = 1/3 on F5 and y_z = 1: val = 5 + c >= 6.

(F2) If x_up = 5, p's label 5^(B+1) w_p has gcd 1 with z's label (c <= 3) and with every W'-label (entries <= 4 by F1);
it can share 5 only with t. y_p = y_z = 1: val = 5 + c >= 6.

(F3) At z the W'-labels are w_u x_zu with x_zu in {1,2,3} (D23P); let k3 >= 2 be the number of W'-threes.
- x_zt != 5 and x_zp = 5: p's label 5^(B+1) w_p is coprime to every other label. y_p = 1 and y = 1/2 on two W'-threes:
  val = 5 + 3.
- x_zt = 5: t's label 5 3^A w_t shares 3 with the W'-threes, 5 or 15 with p, and nothing with W'-ones or W'-twos.
  k3 = 2: then x_zp = 3 and the two other W'-entries equal o in {1,2} (D23P); y_t = 1 and y = 1 on both ones, resp. 1/2
  on both twos (twos pair only with each other): val = 7. k3 = 3 with fourth entry o in {1,2}: y_t = y_o = 1: val >= 6.
  k3 = 4 and x_zp != 3: p's label shares only 5 with t and nothing with the threes; y = 1/3 on the threes and on t
  (pairwise gcd 3, at most three per allowed set, Sun(4)) and y_p = 2/3 (allowed sets through p: {p}, {p, t}):
  val = 4 + 5/3 + 2 x_zp/3 > 6. Hence k3 = 4 and x_zp = 3. In particular x_zp != 5 in every case.

(F4) Suppose x_tp = 5. At p: t's label is 5 3^A w_t, z's label 2^E x_pz w_z, the W'-labels w_u x_pu (x_pu != 5 by F2).
If some x_pu lies in {1,2,4}, that label is coprime to t's: y_t = y_u = 1, val >= 6. Otherwise every x_pu = 3. If
x_pz in {1,2,4}: z is coprime to t: y_t = y_z = 1, val >= 6. If x_pz = 3: the six labels have pairwise gcd 3: y = 1/3 on
all, val = (12 + 3 + 5)/3 > 6. If x_pz = 5: z shares only 5 with t: y = 1/3 on the threes and on t, y_z = 2/3:
val = 4 + 5/3 + 10/3 = 9.

(F5) At t with x_tz = 5, z's label 5 2^E w_z is coprime to a W'-label w_u x_tu with x_tu in {1, 3}: y_z = y_u = 1,
val >= 6.

(F6) Suppose x_ut = 5 (u in W'); t's label at u is 5 3^A w_t.
- c in {1,2}: z's label is coprime to t's: y_t = y_z = 1, val = 5 + c >= 6.
- c = 3 and some W'-neighbour b has x_ub in {1,2,4}: b's label is coprime to t's: y_t = y_b = 1, val >= 6.
- c = 3, the three W'-entries are 3 (not 5 by F1) and x_up in {1,2,4} (not 5 by F2): the threes, z (label 3 2^E w_z) and
  t have pairwise gcd 3; p's label 5^B w_p x_up shares 5 with t, a power of 2 with z when x_up is even, nothing with the
  threes. y = 1/3 on the threes, z and t, and y_p = 2/3 if x_up = 1 (allowed sets through p: {p}, {p, t}) or y_p = 1/3 if
  x_up in {2,4} (allowed sets through p: {p}, {p,t}, {p,z}, {p,z,t}): val = 3 + 1 + 5/3 + 2/3 = 19/3, resp.
  >= 3 + 1 + 5/3 + 2/3.
- c = 3, the three W'-entries are 3 and x_up = 3: all labels have pairwise gcd 3 except gcd(t, p) = 15. Here
  y = 1/3 on the threes, z and t, y_p = 0 is feasible with val = 17/3 < 6, so LFC (d) alone does not decide. INV (b) gives
  x*_ut = 1. If x*_zt = 5, then (F5) for x* (at t in C^x*) says x*_tu is not 1: contradiction. Otherwise 5 does not divide
  x*_zt, and Corollary 5/6-a2 (section 2; condition (a) for beta = x*) gives val <= 5 for every feasible y of the x-row at
  u, contradicting 17/3. (Section 2 does not use F6.)

(F7) Let x_zt = 5. (F5) and (F6) give x_tu in {2, 4}, and (F4) gives x_tp != 5. If x_tp = 3: at t, p's label
3 5^B w_p is coprime to every W'-label (entries 2, 4) and shares 5 with z. The four W'-labels form a two/four class whose
standard weights (E8 with N = 4; with four elements only Sun(2)-Sun(4) decide allowedness) have value >= 4; with y_z = 0
and y_p = 1: val >= 4 + 3 = 7. QED

## 2. Lemma FG-a2 and Corollary 5/6-a2 [NEW]

Let (V_j)_(j in V) be subgroups of G with [G : V_j] = n_j and beta_jk := [G : V_j cap V_k] / lcm(n_j, n_k) <= 5, and for
Q subset V put T_Q := [G : intersection of V_j (j in Q)].
- **(a)** Let u in W' and Q := V \ {u}. If 5 does not divide beta_zt, or 3 does not divide beta_zp, or beta_tp is odd,
  then gcd(n_u, T_Q) = 6.
- **(b)** Let Q := V \ {p}. If beta_zt != 5 and beta_zu <= 3 for every u in W', then gcd(n_p, T_Q) = 6.

*Proof.* As in the proof of FG7 (chain form): when a vertex e is added to the intersection W_m of index T_m,
T_(m+1) = lcm(n_e, T_m) k with k a positive integer, and mu(V_e W_m) = k / gcd(n_e, T_m) <= mu(V_e V_j) = beta_ej / 6 for
every earlier j (L0.1, gcd(n_e, n_j) = 6), so k <= beta_ej gcd(n_e, T_m) / 6.
(a) Put the three marked vertices first, in the order (z, t, p), (z, p, t) or (t, p, z) according as the first, second or
third condition holds, and then W' \ {u}. The first two give T_2 = lcm(n_j1, n_j2) beta_j1j2, whose prime-to-30 part is
w_j1 w_j2. The third marked vertex e has gcd(n_e, T_2) = 6 5^min(B, v5 beta_zt), 6 3^min(A, v3 beta_zp), resp.
6 2^min(E, v2 beta_tp), which is 6 under the corresponding condition; so k <= 5 and the prime-to-30 part of T_3 is
w_z w_t w_p. Every later (unmarked) e has w_e coprime to T_m and 6 | T_m, so gcd(n_e, T_m) = 6 and k <= 5. Hence the
prime-to-30 part of T_Q is the product of the w_j (j in Q), coprime to w_u, and gcd(n_u, T_Q) = gcd(6 w_u, T_Q) = 6.
(b) Order z, t, then W'. T_2 = lcm(n_z, n_t) beta_zt with 5 not dividing beta_zt; each W'-step has gcd(n_e, T_m) = 6 and
k <= beta_ez <= 3 (z is earlier). So 5 does not divide T_Q, its prime-to-30 part is the product of the w_j (j != p), and
gcd(n_p, T_Q) = gcd(6 5^B w_p, T_Q) = 6. QED

**Corollary 5/6-a2.** Let x in {alpha, alpha*} and let u in W' (resp. u = p). If the condition of (a) (resp. of (b))
holds for beta = x*, then every feasible y at u in C^x has val(y) <= 5, and if val(y) = 5, every fibre C at u with S_C
non-empty has sum_(j in S_C) y_j = 1. For u = p the condition of (b) reduces to x*_zt != 5 (D23P gives x*_zu <= 3).
*Proof.* The proof of RICH Corollary 5/6 (consolidated-erratum form) uses only gcd(n_u, [G : W*]) = 6, where
W* = intersection of the g_jU_jg_j^-1 (j != u) with pairwise beta = alpha* for x = alpha (INV (b)), and W* is a conjugate of
the intersection of the U_j (beta = alpha) for x = alpha*. Lemma FG-a2 supplies this. QED

## 3. Lemma D23-a2 [NEW]

**If x_zt != 5, the x-row at z is 3-type relative to W := W' cup {p}: x_zt in {1, 2}, x_zj in {1,2,3} for every j in W,
and x_zj = 3 for at least three j in W.**

*Proof.* D23P gives x_zu in {1,2,3} (u in W'), k3 >= 2 W'-threes, x_zt != 4; (F3) gives x_zp != 5.
(i) x_zp != 4. Suppose x_zp = 4: p's label 4 5^B w_p shares 2 with W'-twos, gcd(4, x_zt) with t, and nothing with W'-ones
or W'-threes. k3 = 2 is impossible (D23P would give x_zp = 3). k3 = 4: y = 1/3 on the threes, y_p = 1: val = 4 + 4.
k3 = 3 with fourth entry o: o = 1: y = 1/3 on the threes, y_o = y_p = 1: val = 3 + 1 + 4; o = 2: y = 1/3 on the threes,
y_o = y_p = 1/2 ({o, p, t} is not allowed: its gcds are all 2 if x_zt = 2, and gcd(o, t) = 1 if x_zt is odd):
val = 3 + 1 + 2 = 6.
(ii) x_zt != 3. Suppose x_zt = 3: t's label 3^(A+1) w_t has gcd 3 with every three-label and with p's label if x_zp = 3,
and gcd 1 with W'-ones, W'-twos and with p if x_zp in {1,2} (x_zp in {1,2,3} by (i) and F3).
k3 = 4: if x_zp = 3, the six labels have pairwise gcd 3 and y = 1/3 on all gives val = (12 + 3 + 3)/3 = 6; if
x_zp in {1,2}, y = 1/3 on the threes and t and y_p = 1 (p coprime to all): val = 5 + x_zp >= 6.
k3 = 3 with fourth entry o in {1,2}: y = 1/3 on the threes and t (value 4). If o = 1 (isolated): y_o = 1, and y_p = 1/3
(x_zp = 3: p joins the gcd-3 clique), y_p = 1 (x_zp = 1: isolated; x_zp = 2: no W'-two to pair with): val >= 6. If o = 2:
for x_zp in {1, 3}, y_o = 1 (o coprime to all) and y_p as before: val >= 4 + 2 + 1; for x_zp = 2, y_o = y_p = 1/2 (they
pair only with each other): val = 4 + 1 + 1 = 6.
k3 = 2: x_zp = 3 and the two other W'-entries equal o in {1,2} (D23P): y = 1/3 on the two threes, t and p (pairwise
gcd 3) and y = 1 on the ones, resp. 1/2 on the twos: val = 2 + 1 + 1 + 2 = 6.
(iii) Hence x_zt in {1,2}, x_zp in {1,2,3}, and W' cup {p} carries at least three threes (k3 >= 3, or k3 = 2 and
x_zp = 3). QED

## 4. The split of (a2), the branch (a2-zt5), and the bridge (a2-no5) -> (a1)

By Lemma F, every (a2) configuration lies in exactly one of:
- **(a2-zt5):** some orientation x has x_zt = 5;
- **(a2-no5):** no entry of alpha or alpha* equals 5.

**Proposition K7-A2-ZT5 (structure) [NEW].** In (a2-zt5), with x the orientation of the five:
- **(S1)** the x-row at z is (3,3,3,3 | p 3 | t 5) (F3);
- **(S2)** x*_zt = 1, and the x*-row at z is 3-type relative to W' cup {p} (D23-a2 for x*);
- **(S3)** x_tu in {2,4} for u in W', and x_tp in {1,2,4} (F7);
- **(S4)** no other entry of alpha or alpha* equals 5 (Lemma F);
- **(S5)** E >= 2.
*Proof of (S5).* In C^x normalise g_z = 1 and let W* := intersection of the g_jU_jg_j^-1 (j != z), pairwise beta = x*.
As in the proof of Corollary 5/6, W*U_z is a union of M left U_z-cosets that contains U_z and meets no g_jU_jU_z
(j != z), and G0 gives M >= n_z / gcd(n_z, [G : W*]). At z, y = 1/3 on W' and on t, y_p = 0, is feasible (pairwise gcds 3
except gcd(t, p) = 15; the allowed sets are those of size <= 3 and the 4-sets containing t and p, Sun(4)) with
val = 17/3. The LFC count (n_z/6) val(y) <= n_z - M gives M <= n_z/18, so gcd(n_z, [G : W*]) >= 18. Ordering t, p first
and then W' (as in section 2: T_2 = lcm(n_t, n_p) x*_tp, every later k <= 5), the prime-to-30 part of [G : W*] is
w_t w_p (product of the w_u), coprime to w_z, and 3 divides [G : W*]; so gcd(n_z, [G : W*]) = 3 2^min(E+1, v2[G : W*])
with n_z = 2^(E+1) 3 w_z. This is >= 18 only if E + 1 >= 3. QED

**Theorem K7-A2-BRIDGE [NEW].** In (a2-no5) put W := W' cup {p}, T := {j in W : alpha_zj = 3}, T* := {j in W :
alpha*_zj = 3}, and W3, W3* as in RICH with this W. Then every conclusion of K7-D23-RICH (with erratum-1 and the
consolidated erratum) holds: **no (a2-no5) configuration has T* subset W3 or T subset W3***, and G0, Corollary 5/6 at
every u in W (both orientations), NO5, R3 with Corollary R3, TR, CC, TZ (i)-(iii) and LZ hold with this W.

*Proof (dictionary).* The proofs of RICH read the (a1) data only through the following facts, each of which holds in
(a2-no5):
- **(B1)** r_z = 2^E w_z and r_t = 3^A w_t (the (a1) case Bz = Bt = 0), and every j in W has n_j = 6 w'_j with w'_j := w_j
  (j in W'), w'_p := 5^B w_p; the w'_j are pairwise coprime and coprime to 6 r_z r_t.
- **(B2)** No entry is 5, so every label r_j x_vj, every VFC local index r_j q_j (q <= 4) and every triangle quantity
  x/gcd(x, ell_j) (x <= 4, ell_j dividing r_j) is divisible by 5 only through r_p. Hence each gcd of two labels, of two
  local indices, or of an entry with an ell, which the (a1) proofs evaluate treating w'_p like a w prime to 30, is
  correct: the factor 5^B of w'_p meets no other factor 5. (Ones, twos, fours, threes keep their meaning for p.)
- **(B3)** FG7 (b) at u in W, as used by Corollary 5/6 in both orientations: Lemma FG-a2 (a) for u in W' and (b) for
  u = p, whose conditions hold since no beta equals 5 (and beta_zu <= 3 by D23P). The other use of FG7, the chain (a) for
  intersections over W in LZ, has every step factor k <= 4 (no fives); when p enters after earlier W'-vertices,
  gcd(n_p, T_m) = 6 because 5 does not divide T_m.
- **(B4)** The D23-MIX conclusion used by RICH (alpha_zu, alpha*_zu in {1,2,3} on W; |T|, |T*| >= 3;
  alpha_zt, alpha*_zt in {1,2}) is Lemma D23-a2 for both orientations.
- **(B5)** NO5 holds trivially by (B2).
- **(B6)** Where LZ states that 5 does not divide T*_W, this is used only to evaluate g = gcd(n_z, T*_W); in (a2) n_z is
  prime to 5, so g = 3 2^min(1+E, v2(T*_W)) holds although 5^B divides T*_W.
- **(B7)** All remaining ingredients (LFC, INV, VFC, L1, G0, Lemma TR, and the VFC count of Lemma CC with local indices
  alpha*_zj r_j) hold for every K7 configuration.
The inverted configuration of an (a2-no5) configuration is again one (E6). QED

**Corollary K7-A2-TRANSFER (conditional on the acceptance of K7-A1-STRUCT sections 1-5, K7-TC and K7-TC-A22).** Their
conclusions hold in (a2-no5) with W := W' cup {p}. *Proof.* They read the same facts (B1)-(B7): the two/four classes and
ones of A1-STRUCT section 0 via (B2) (p's labels are 2^i 5^B w_p or 5^B w_p), its triangle evaluation via (B2) (every ell
of a vertex in W, including ell_p = 5^B w_p, is odd), Corollary 5/6 and FG7 at apexes in W via (B3), and PFG-t (i), whose
statement "5 does not divide T_W" is used only to get gcd(n_t, T_W) = 6, which holds because n_t = 6 3^A w_t is prime to
5 and v3(T_W) = 1 (as in (B6)). QED

## 5. Scope

- **Proved here (imports accepted):** Lemma F (F1)-(F7); Lemma FG-a2 with Corollary 5/6-a2; Lemma D23-a2; Proposition
  K7-A2-ZT5; Theorem K7-A2-BRIDGE. In particular no (a2) configuration has a five other than on z-t, and no (a2-no5)
  configuration has T* subset W3 or T subset W3* (W = W' cup {p}).
- **Conditional:** Corollary K7-A2-TRANSFER (on K7-A1-STRUCT, K7-TC, K7-TC-A22).
- **Open:** (a2-zt5) beyond (S1)-(S5); the (a1)-type residue in (a2-no5); the (a1) residue itself; K6.2*; full Sun(7).
- Requested checks: every weight vector of Lemma F and D23-a2 against the label gcds; the three orders of FG-a2 (a) and
  the gcd of the third marked vertex; the last branch of (F6) (inverse step and FG condition for beta = x*); the
  light-fibre count of (S5); each item (B1)-(B7) against the text of RICH. No novelty, Lean or human-review claim.
