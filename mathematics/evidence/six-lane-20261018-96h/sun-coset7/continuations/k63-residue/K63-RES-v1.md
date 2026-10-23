# K63-RES-v1: full granularity at an unmarked odd C-vertex; no K6.3 configuration with the 3-marker on d and a 2-marker in C [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:21:03-0700.
- **Author:** worker Sun63Successor (continuation `continuations/k63-residue`). Single author, unreviewed.
- **Status:** CANDIDATE written mathematics. No computation was run for it and no computation is a premise. "[NEW]"
  means written in this continuation; it is not a novelty claim. Full Sun(7) stays OPEN (K7 and K6.2* are untouched).
- **Premises (accepted, at these scopes).**
  - R0 (finite quotient; old README section 1) and the K6.3 class definition with P0/P1 (old README sections 2 and 5),
    as used in the accepted `K63-D-v1.md` section 1 and `K63-E-v1.md` section 1.
  - L0.3 identity and range (`K7-LFC-INV-erratum-v1.md` E1): for subgroups A, B of a finite group,
    mu(AB) = [G : A cap B] / ([G : A][G : B]); for disjoint cosets 1 <= alpha <= g - 1.
  - LFC (a)-(d) and INV (a)-(b) (`K7-LFC-INV-v1.md` + erratum; parent verdict sha256 8621e744...ca18).
  - VFC (V1)-(V4) and the VFC-count argument (rules-k7-v1 section 2, sha256 77b9afec...; accepted).
  - TG (parent verdict `RUN/review/sun7-K62A-TG-parent-verdict-v1.md`, sha256
    c792dc68884a0c99632f218fd03833f60b80b89fd2c194137331d35fb4f3fc61), used only in its general computational form:
    for subgroups H, W of a finite group, mu(HW) >= 1 / gcd([G : H], [G : W]). Disjoint cosets are not needed for it.
  - Sun(t), t <= 6, only inside LFC (c) and VFC (V3).
  - **Not used:** K63-CLIQUE, D-ROW, Ppair, K, RPLP, F7, the T rule L1, two-orbit facts, Sun(7), least-order
    frames, any probe output.

## 0. Setting and statement

The K6.3 residue (README section 5 with P0/P1, as in K63-D section 1): V = C disjoint-union {d}, C = {i*}
disjoint-union O with |O| = 5, and
- n_d = 3 r_d, r_d = 3^F 5^(h_d) w_d with F = f_d - 1 >= 1 (the 3-marker is on d);
- n_(i*) = 6 r_(i*), r_(i*) = 2^E 5^(h_*) w_* with E = e_(i*) - 1 >= 1 (the 2-marker is on i*);
- n_c = 6 r_c, r_c = 5^(h_c) w_c for c in O (e_c = f_c = 1: at most one vertex has e >= 2 and at most one has f >= 2);
- the w's are pairwise coprime and coprime to 30; at most one of h_d, h_*, h_c (c in O) is positive;
- g = 6 on C-pairs and g = 3 on the six d-pairs.
For j in V let w_j be the prime-to-30 part of n_j (so w_j = w_d, w_*, w_c above). Call **p** the vertex of O with
h_p >= 1, if the 5-marker lies in O.

For a family V = (V_j) of subgroups of a finite group G with [G : V_j] = n_j put
beta_jk(V) := [G : V_j cap V_k] / lcm(n_j, n_k), a positive integer (Lagrange). Hypothesis
**(B): beta_jk(V) <= g_jk - 1 for all j != k.**
(B) holds for V = U (L0.3, since the cosets g_jU_j are disjoint), and for the conjugate family
U* = (g_jU_jg_j^-1): beta(U*) = alpha* by definition of alpha* (INV), and alpha* <= g - alpha <= g - 1 by INV (b).

**Fix v in O with h_v = 0.** It exists (|O| = 5, at most one 5-marked vertex), and n_v = 6 w_v. Put
N := V minus {v}.

**Theorem K63-RES [NEW].** No configuration of this setting exists, in any group with finite-index subgroups (R0).
Equivalently: no K6.3 configuration has f_d >= 2 and a C-vertex with e >= 2.

## 1. Lemma FG (full granularity at v) [NEW]

Let V satisfy (B) and let Q be a non-empty subset of N. Put W_Q = intersection of the V_j (j in Q) and
T_Q = [G : W_Q]. Then the prime-to-30 part of T_Q is the product of the w_j (j in Q); hence gcd(n_v, T_Q) divides 6,
and for every subgroup H of index n_v: **mu(H W_Q) >= 1/6.**

*Proof.* Order Q as follows: first the vertices of Q cap {i*, d} (if both are present, i* then d); then p, if
p is in Q; then the remaining vertices of Q, which are vertices of O with h = 0, in any order. Write
Q = (j_1, ..., j_s), W_m = V_(j_1) cap ... cap V_(j_m), T_m = [G : W_m].

*Claim:* T_m is divisible by L_m := lcm(n_(j_1), ..., n_(j_m)) and T_m / L_m has no prime factor > 5.
- Base. If j_1, j_2 = i*, d: T_2 = lcm(n_*, n_d) beta_(*d) with beta_(*d) <= g_(*d) - 1 = 2. If Q contains exactly
  one of i*, d, or neither: T_1 = n_(j_1). In all cases the claim holds at the base. Moreover, if p exists, then
  h_* = h_d = 0, so the base index (T_2, or T_1 = n_*, or T_1 = n_d) is **not divisible by 5**; if Q contains no
  vertex of {i*, d} and contains p, take j_1 = p and the base T_1 = n_p.
- Step m -> m + 1 with e := j_(m+1). W_(m+1) = V_e cap W_m, so T_(m+1) is a common multiple of n_e and T_m:
  T_(m+1) = lcm(n_e, T_m) k for a positive integer k. By the L0.3 formula, mu(V_e W_m) = T_(m+1) / (n_e T_m), and
  V_e W_m is contained in V_e V_(j_1), of measure beta_(e j_1) / g_(e j_1) <= 5/6 (L0.3 formula and (B): beta <= 5
  if g = 6, beta <= 2 if g = 3). Hence k <= gcd(n_e, T_m) * 5/6. Now gcd(n_e, T_m) divides 6:
  n_e = 6 * 5^(h_e) * w_e; w_e is coprime to T_m (by the claim, the prime-to-30 part of T_m is the product of the
  w_(j_i), i <= m, all coprime to w_e); and either h_e = 0, or e = p is added directly after the base, where
  5 does not divide T_m. So k <= 5. Since k has no prime factor > 5, the prime-to-30 part of T_(m+1) equals that of
  lcm(n_e, T_m), namely the product of w_(j_1), ..., w_(j_(m+1)), which is the prime-to-30 part of L_(m+1); and
  L_(m+1) divides T_(m+1) because W_(m+1) lies in every V_(j_i). This proves the claim for m + 1.
(If p is the first vertex, i.e. Q avoids i* and d, every later vertex has h = 0 and the step needs no 5-condition.)

For m = s: the prime-to-30 part of T_Q is the product of the w_j (j in Q), coprime to w_v, and the other primes of
T_Q are 2, 3, 5. As n_v = 6 w_v, gcd(n_v, T_Q) = gcd(6, T_Q) divides 6. Finally
mu(H W_Q) = [G : H cap W_Q] / (n_v T_Q) >= lcm(n_v, T_Q) / (n_v T_Q) = 1 / gcd(n_v, T_Q) >= 1/6. QED

*Remark.* For |Q| = 3 this is triple granularity 1/6 for **every** triple of N, with no hypothesis on the alpha-values
of the triple. Only (B) is used, i.e. alpha, alpha* <= g - 1.

## 2. Corollary 5/6 (the LFC and VFC counts at v with 5/6 in place of 1) [NEW]

Left-translate so that g_v = 1 (indices, intersections and disjointness are unchanged).

**(a) VFC side.** Let W = W_N(U). Then U_v W is contained in every U_vU_j (j in N), hence disjoint from every
D_j = U_v g_j U_j (VFC (V1)). By FG for V = U and H = U_v, mu(union of the D_j) <= 1 - mu(U_v W) <= 5/6. By the
VFC-count argument (rules-k7-v1 section 2: the sum over j of y_j mu(D_j) equals the sum over right cosets R of
mu(R) times the sum of y_j over S_R, and each S_R is allowed by (V3)) and INV (b) (mu(D_j) = alpha*_vj / g_vj,
local indices lambda*_j = n_j alpha*_vj / g_vj):
for every y >= 0 with sum over T of y_j <= 1 for every lambda*-allowed T, **sum_j y_j alpha*_vj / g_vj <= 5/6.**

**(b) LFC side.** Let W* = W_N(U*) = intersection of the g_jU_jg_j^-1 (j in N), and L_j := g_jU_jU_v, the union of
the left U_v-cosets meeting g_jU_j (LFC (b)). The set W*U_v is a union of left U_v-cosets, contains U_v, and is
disjoint from every L_j: if w u is in L_j with w in W* and u in U_v, then w = g_j a g_j^-1 (a in U_j) lies in
g_jU_jU_v, so a g_j^-1 is in U_jU_v, so g_j^-1 is in U_jU_v, i.e. g_j is in U_vU_j, i.e. g_jU_j meets U_v = g_vU_v,
contradicting disjointness. By FG for V = U* (hypothesis (B) holds by INV) and the L0.3 formula,
mu(W*U_v) = mu(U_vW*) >= 1/6. Hence at most (5/6) n_v left U_v-cosets meet the union of the g_jU_j, and the LFC (d)
count (sum_j y_j t_j = sum over cosets C of the sum of y_j over S_C, t_j / n_v = alpha_vj / g_vj, LFC (a)-(c))
gives: for every y >= 0 with sum over T of y_j <= 1 for every lambda-allowed T
(lambda_j = n_j alpha_vj / g_vj), **sum_j y_j alpha_vj / g_vj <= 5/6.**

**Unified form.** For x in {alpha, alpha*} and labels lambda^x_j = n_j x_vj / g_vj, every lambda^x-feasible y
satisfies, in units of 1/6,

  val(y) := sum over c in C minus {v} of y_c x_vc  +  2 y_d x_vd  <=  5.        (5/6-bound)

## 3. Row Lemma: x_vd = 2 for x = alpha and for x = alpha* [NEW]

Fix x in {alpha, alpha*} and suppose **x_vd = 1**. We exhibit a lambda^x-feasible y with val(y) > 5,
contradicting the 5/6-bound.

*Types.* Since the w's are pairwise coprime, coprime to 30 and to every x <= 5, gcd(lambda_j, lambda_k) =
gcd(type(j), type(k)) with (O' := O minus {v}, x_* := x_(v i*), x_u := x_vu):
- type(u) = 5^(h_u) x_u for u in O';
- type(i*) = 2^(E + v2(x_*)) 3^(v3(x_*)) 5^(h_* + v5(x_*));
- type(d) = 3^F 5^(h_d) (as x_vd = 1; F >= 1).
j and k are *compatible* if gcd >= 2. An allowed set never contains an incompatible pair, and an allowed set all of
whose pairwise gcds equal 3 (resp. 5) has at most 3 (resp. 5) elements (a 4-set needs a pair with gcd >= 4, a 6-set a
pair with gcd >= 6). Weight 0 on an element never creates infeasibility (allowedness is hereditary). Put
T3 = {u in O' : x_u = 3}, T5 = {u in O' : x_u = 5}, k3 = |T3|, k5 = |T5|.

*Standing facts* (at most one positive h among h_d, h_*, h_u):
- (F1) d is compatible with u in O' iff x_u = 3, or x_u = 5 and h_d >= 1; d is compatible with i* iff 3 | x_*, or
  x_* = 5 and h_d >= 1.
- (F2) The elements of T3 together with d have all pairwise gcds exactly 3; if moreover x_* = 3, the same holds for
  T3, d and i* together.
- (F3) u in O' with x_u in {1, 2, 4} is compatible with no element of T3, of T5, nor with d. Two such elements u, u'
  have gcd(x_u, x_u').
- (F4) i* is compatible with u in O' with x_u even (2-part >= 2). If 3 does not divide x_*, then among T3 and d,
  i* is compatible with at most one element q, and only if x_* = 5 and q is 5-marked (q = d with h_d >= 1, or
  q = p in T3).

*Standard weights* on a set Z of elements of O' with values in {1, 2, 4} (ROW-U, `K7-LFC-INV-v1.md` section 3,
re-derived): ones y = 1; if Z has at most two fours, twos y = 1/2 and fours y = 1/4; if Z has three or four fours,
y = 1/min(b, 4) on its b fours and 0 on its twos. By (F3) the allowed subsets of Z are those of ROW-U for labels
with alpha-gcds, so these weights are feasible on Z, and their value is >= min(|Z|, 4) (LFC-erratum E8).

**(1) k5 >= 1.**
- (1a) h_d = 0: y = 1/k5 on T5, y_d = 1, all else 0. d and a five are incompatible (type(d) = 3^F), so every
  allowed set has sum <= 1. val = 5 + 2 = 7.
- (1b) h_d >= 1 (so all C-vertices have h = 0), and some z in O' minus T5: y = 1/k5 on T5, y_z = 1, all else 0
  (z is incompatible with every five). val >= 5 + 1 = 6.
- (1c) h_d >= 1 and O' = T5: if x_* != 5, i* is compatible with no five and at most with d; take y = 1/5 on T5 and
  d (five elements) and y_* = 4/5; every allowed set containing i* lies in {i*, d}. val = 4 + 2/5 + (4/5) x_* >= 26/5.
  If x_* = 5, the six types 5 (four times), 3^F 5^(h_d), 2^E 5 have all pairwise gcds exactly 5, so allowed sets have
  at most 5 elements; y = 1/5 on all six gives val = (20 + 2 + 5)/5 = 27/5.

From now on k5 = 0, so every entry of O' lies in {1, 2, 3, 4}.

**(2) k3 = 4.** If x_* = 3: by (F2) all six neighbours have pairwise gcd 3; y = 1/3 on all gives
val = (12 + 3 + 2)/3 = 17/3. If x_* != 3: y = 1/3 on T3 and d (allowed sets there have size <= 3 by (F2)); by (F4),
i* is compatible with at most one q in T3 cup {d}; put y_* = 2/3 if q exists (then x_* = 5) and y_* = 1 otherwise.
Sets containing i* lie in {i*, q}. val >= 4 + 2/3 + min(10/3, 1) = 17/3.

**(3) k3 = 3, O' = T3 cup {z}, x_z in {1, 2, 4}.**
- (3a) x_* = 3: K := T3 cup {d, i*} has pairwise gcds 3 (F2), y = 1/3 on K (value 14/3). z is compatible only
  with i*, and with i* iff x_z is even (F3, F4; the 5-part of gcd(z, i*) is trivial as x_* = 3). Put y_z = 1 if
  x_z = 1 and y_z = 2/3 otherwise; sets containing z lie in {z, i*}. val >= 14/3 + min(1, 4/3) = 17/3.
- (3b) x_* != 3: y = 1/3 on T3 cup {d} (value 11/3). If the q of (F4) exists (x_* = 5, q 5-marked, hence z
  unmarked): y_* = 2/3, y_z = 0; sets containing i* lie in {i*, q} or {i*, z}; val = 11/3 + 10/3 = 7. If no q:
  i* and z are compatible with nothing of positive weight except possibly each other; put y_* = y_z = 1/2 if they
  are compatible (then x_z is even, or z = p and x_* = 5), giving val >= 11/3 + min(1 + 1/2, 5/2 + 1/2) = 31/6, and
  y_* = y_z = 1 otherwise, giving val >= 11/3 + 2.

**(4) k3 = 2, O' = T3 cup {z1, z2}, x_z in {1, 2, 4}.**
Basic certificate: y = 1/2 on T3; on {z1, z2} (compatible iff both even, F3) y = 1 on the larger of the two if
both are even, y = 1 on both otherwise; y_d = y_* = 0. By (F3) the T3-sets and the z-sets do not mix; sets inside
T3 cup {d, i*} have sum <= 1. val = 3 + V_Z with V_Z = max(x_z1, x_z2) (both even) or x_z1 + x_z2 (otherwise);
V_Z > 2, hence val > 5, unless {x_z1, x_z2} = {1, 1} or {2, 2}.
- (4a) {1, 1}. If x_* = 3: y = 1/3 on K = T3 cup {d, i*} (pairwise gcds 3), and the ones are isolated (their
  types 5^(h_z) share no prime with any other type: at most one marker, x_* = 3); val = 11/3 + 2 = 17/3. If
  x_* != 3: y = 1/2 on T3, y = 1 on the ones, y_d = 0. If x_* != 5, i* is isolated (no 2, 3 or 5 in common with
  T3, the ones or d): y_* = 1, val >= 3 + 2 + 1 = 6. If x_* = 5, i* is compatible with at most one element q (the
  5-marked one among T3, the ones and d): q in T3 gives y_* = 1/2 (val = 3 + 2 + 5/2); q a one gives y_q = 0,
  y_* = 1 (val = 3 + 1 + 5); q = d or no q gives y_* = 1 (val = 10).
- (4b) {2, 2}. The twos are compatible with each other and with i*, with nothing else (F3).
  If x_* = 3: y = 1/3 on K (pairwise gcds 3), y = 1/2 on the twos; {z1, z2, i*} is not allowed (all three gcds are
  2: the 5-part of gcd(z, i*) is trivial because x_* = 3). val = 11/3 + 2 = 17/3.
  If x_* != 3: y = 1/3 on T3 cup {d} (value 8/3) and y = 1/2 on the twos (value 2). If {z1, z2, i*} is not
  allowed, put y_* = 1/2: sets through i* are {i*, z} (sum 1), {i*, q} for the q of (F4) (sum 5/6), and no
  larger allowed set contains i* (q and z are incompatible); val >= 14/3 + 1/2 = 31/6. If {z1, z2, i*} is allowed,
  then some gcd(z, i*) >= 3, which forces z = p and x_* = 5; then h_d = 0 and p is not in T3, so i* is compatible
  with nothing in T3 cup {d}; put y_z1 = y_z2 = 0, y_* = 1: val = 8/3 + 5.

**(5) k3 = 1, O' = {t} cup Z, |Z| = 3, values in {1, 2, 4}.** y_t = 1 (t is compatible with no element of Z,
F3), standard weights on Z (value >= 3), y_d = y_* = 0. val >= 3 + 3 = 6.

**(6) k3 = 0.** y_d = 1 (d is compatible with no element of O', F1/F3; sets through d lie in {d, i*}), y_* = 0,
standard weights on O' (value >= 4). val >= 2 + 4 = 6.

Every case gives val > 5. Hence x_vd != 1, i.e. **x_vd = 2**. QED

## 4. Proof of Theorem K63-RES

By the Row Lemma for x = alpha (using Corollary 5/6 (b)) and for x = alpha* (using (a)), alpha_vd = alpha*_vd = 2.
INV (b) gives alpha_vd + alpha*_vd <= g_vd = 3, a contradiction. So no finite group carries such a configuration,
and by R0 no group does. QED

## 5. Scope and consequences

- **Covered:** every K6.3 configuration with the 3-marker on d (f_d >= 2) and a 2-marker on a C-vertex (e >= 2),
  with any position of the 5-marker (none, d, i*, or a vertex of O) and arbitrary exponents E, F, h, arbitrary w's.
  Capped profiles play no role.
- **If accepted:** together with the accepted K63-U0, K63-D and K63-E, **class K6.3 is excluded entirely.** The
  accepted K63-CLIQUE is the special case of the residue with the full all-3 clique and is not used here.
- **Not covered:** K7 and K6.2*. (Lemma FG uses only (B), the index shapes and an unmarked vertex v; whether a
  similar bound helps there has not been examined in this file; no claim.)
- **Where the strength comes from.** With LFC's original bound (< 1, i.e. val < 6) the cases (1c), (2), (3), (4)
  are not killed (for example the all-3 C-row with x_vd = 1 and x_* = 3 has val = 17/3 < 6). Cases (1a), (1b), (5),
  (6) already die under the original bound (val >= 6).

## 6. Work item 1: TG / CLIQUE re-derivation and the star question

- I re-derived TG and the corrected CLIQUE proof (`K63-TG-v1.md` with errata v1-v3) line by line and agree with the
  accepted statements; no defect found.
- **Star question.** Lemma FG with |Q| = 3 gives mu(X_a cap X_b cap X_c) >= 1/6 at every v in O with h_v = 0 and for
  every triple {a, b, c} of N, with no hypothesis on the inner alpha-values. Hence step (i) of the CLIQUE proof holds
  under the original star hypothesis alone (alpha_vc = alpha*_vc = 3 for c in C minus {v}, with v in O and
  h_v = 0), and steps (ii)-(v) use only v's row; so the withdrawn star statement is valid for such v. For a 5-marked
  v the granularity can drop (5 may divide gcd(n_v, T)); no claim there. Both statements are superseded by
  Theorem K63-RES, which needs neither the star nor the clique hypothesis.

## 7. Work item 3 (certificate architecture)

Not triggered: a written closure is proposed. No computation was run, requested or needed for this file.

## 8. Verification boundary and requested checks

Written, single author, unreviewed. Requested: parent re-derivation of (i) the bookkeeping in Lemma FG (the order
i*, d, p, rest; the step bound k <= gcd(n_e, T_m) * 5/6; why gcd(n_e, T_m) divides 6), (ii) the disjointness of W*U_v
from every L_j in Corollary 5/6 (b), (iii) the case tables of the Row Lemma; and hostile Codex and Claude reviews of
this exact file. Suggested mutation controls:
1. Take v = p (h_v >= 1): gcd(n_v, T_Q) may contain 5, the bound 1/6 fails, and the Row Lemma loses its 5/6-bound.
2. In FG, add p after an unmarked vertex: then 5 may divide T_m, gcd(n_p, T_m) may be 30, and k <= 25 is not 5-smooth.
3. Replace the 5/6-bound by LFC's < 1: case (2) with x_* = 3 (val 17/3) is no longer a kill.
4. Put the 3-marker elsewhere (F = 0 at d): d is no longer compatible with threes, and (F1), (F2) fail.
5. Drop INV in section 4: x_vd = 2 in one orientation alone is not contradictory.
No novelty, priority, Lean or human-review claim.
