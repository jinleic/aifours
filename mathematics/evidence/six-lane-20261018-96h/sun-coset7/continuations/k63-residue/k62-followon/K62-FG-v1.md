# K62-FG-v1: the granularity mechanism in the remaining K6.2* classes — partial exclusion and exact obstruction [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T03:47:59-0700.
- **Author:** Sun63Successor. Single author, unreviewed, no computation. Setting and import boundary: `SETTING-v1.md`
  (sha256 3bff4e6618cb6591683f7adcc1fbd52fbd3dd16e306b024be6181c332f42bb8d) in this directory. The candidate
  `../K63-RES-v1.md` is NOT imported; its mechanism is re-proved below for K6.2* (Lemma FG-62).
- Notation: units of 1/6 for LFC/VFC values; for a vertex v of O and x in {alpha, alpha*}, val(y) =
  sum over C-neighbours c of y_c x_vc + 3 y_d (since g_vd = 2 and x_vd = 1, d has weight 1/2 = 3 units).
  LFC (resp. VFC) gives val(y) < 6 for every lambda^x-feasible y (lambda^x_j = n_j x_vj / g_vj).
  "type" = the {2,3,5}-part of a label; gcds of labels are gcds of types (w's pairwise coprime, coprime to 30
  and to entries <= 5).

## 1. Lemma D (the d-i* entry) [NEW; generalises K62-A Step 1]
For x in {alpha, alpha*}: x_(d i*) != 2; and x_(d i*) = 1 unless the 3-marker lies on a vertex t of O.
Hence (alpha_(d i*), alpha*_(d i*)) is (1,1), (1,3) or (3,1), and (1,1) when no 3-marker lies in O.

*Proof.* At d: lambda_c = n_c / 2 = 3^(f_c) 5^(h_c) w_c (c in O, weight 1/2) and
lambda_(i*) = n_(i*) x / 4 = 2^(e* - 2) 3^(f*) 5^(h*) w_* x (weight x/4), x = x_(d i*) in {1,2,3}. The lambda_c are odd,
so no pair shares a 2; at most one vertex has h >= 1 and x <= 3, so no pair shares a 5. The 3-parts: 3 for every
pair, except gcd(lambda_t, lambda_(i*)) = 3^(min(f_t, 1 + v3(x))) = 9 when t exists (then f* = 1) and x = 3. So unless
(t exists and x = 3) all pairwise gcds equal 3, allowed sets have at most 3 elements, y = 1/3 on all six is
feasible and sum y x/g = 5/6 + x/12, which LFC (d) at d forces below 1: x = 1. For x = alpha* use INV (a) (the inverted
configuration has the same indices and markers). The sum is at most 4 by INV (b). QED

## 2. Lemma OO (the O-O entries; plain LFC) [NEW]
For every v in O, every u in O minus {v} and x in {alpha, alpha*}: **x_vu in {1, 2, 4}**, and for each v at most two
u in O minus {v} have x_vu = 1.

*Proof.* At v the labels are lambda_u = 3^(f_u - 1) 5^(h_u) w_u x_vu (u in O), lambda_(i*) = 2^(e* - 1) 3^(f* - 1)
5^(h*) w_* x_(v i*), lambda_d = n_d / 2 = 2^(e_d - 1) 5^(h_d) w_d (weight 1/2, 3 units). lambda_u is odd iff x_vu is odd.
- *No 3.* If x_vu = 3, lambda_u is odd and has no 5 in common with lambda_d (at most one marker; 5 does not divide 3),
  so u and d are incompatible: y_u = y_d = 1 (all else 0) is feasible and val = 3 + 3 = 6.
- *At most two 1s.* Labels with x = 1 are 3^(f_u - 1) 5^(h_u) w_u: pairwise coprime (at most one 3-marker and one
  5-marker) and coprime to lambda_d (odd; a common 5 would need two markers). Three of them with y = 1 and y_d = 1:
  val = 3 + 3 = 6.
- *No 5.* If h_d = 0, a five u (x_vu = 5) is incompatible with d (odd, no common 5): y_u = y_d = 1 gives val = 8.
  If h_d >= 1 (no C-vertex has h >= 1, so 5 divides lambda_u iff x_vu = 5): let F5 be the fives at v. If some
  u' in O minus {v} is not a five, it has no 3 (threes are excluded) unless it is t with ... — more precisely
  gcd(lambda_u', lambda_f) for a five f can contain 3 only if f = t and 3 | x_vu', i.e. x_vu' = 3, excluded — and no 5,
  so u' is incompatible with every five: y = 1/|F5| on F5 and y_u' = 1 give val >= 5 + 1. If all four are fives:
  if 5 does not divide x_(v i*), i* is compatible with at most the five t (through a 3, when x_(v i*) = 3);
  y = 1/4 on F5 and y_(i*) = 3/4 give val >= 5 + 3/4 * 1... (if i* meets no five, y_(i*) = 1 and val >= 6; if it meets
  only t, then 3 | x_(v i*), i.e. x_(v i*) = 3, and val = 5 + 9/4 > 6). If x_(v i*) = 5, then x*_vu = 1 for the four
  fives (INV (b): x + x* <= 6), and the inverted orientation has four 1s, excluded by the previous item.
In each case LFC (resp. VFC) is violated. QED

## 3. Lemma FG-62 (granularity at an unmarked vertex of O) [NEW; mechanism of K63-RES section 1]
Let V = (V_j) be U or U* = (g_jU_jg_j^-1); beta_jk(V) = [G : V_j cap V_k] / lcm(n_j, n_k) equals alpha_jk resp.
alpha*_jk, so 1 <= beta <= g - 1 (L0.3, INV (b)). Let v in O be unmarked (n_v = 6 w_v) and N = V minus {v}.
**If no 3-marker lies in O, or beta_(d i*)(V) <= 2, then the prime-to-30 part of T := [G : intersection of V_j, j in N]
is the product of the w_j (j in N); hence gcd(n_v, T) divides 6 and mu(H W) >= 1/6 for every H of index n_v
(W = intersection of the V_j, j in N).**

*Proof.* Add the vertices of N in the order d, i*, t (if t exists), p (if p exists and p != t), then the unmarked
vertices of O minus {v}. With T_m the index of the running intersection, T_(m+1) = lcm(n_e, T_m) k with
k <= gcd(n_e, T_m) * min over earlier j of beta_ej / g_ej (L0.3 formula for mu(V_e W_m) and V_e W_m in V_e V_j); the
prime-to-30 part of T_m stays the product of the w's added so far as long as every k has no prime factor > 5.
- T_1 = n_d; T_2 = lcm(n_d, n_(i*)) beta_(d i*) (pair), beta_(d i*) <= 3.
- t (if present; then f* = 1): v3(T_2) = 1 + v3(beta_(d i*)) = 1 when beta_(d i*) <= 2; v5(T_2) = 0 if t is 5-marked
  (then h_d = h* = 0). So gcd(n_t, T_2) = 2 * 3 = 6 and k <= 6 * (beta_td / g_td) = 6 * 1/2 = 3.
- p (if present, p != t; f_p = 1): no index so far is divisible by 5 and every k so far is <= 3, so
  gcd(n_p, T_m) = 6 and k <= 6 * 1/2 = 3.
- unmarked e: gcd(6 w_e, T_m) = gcd(6, T_m) divides 6, so k <= 6 * 1/2 = 3.
(Without t the second bullet is skipped and beta_(d i*) <= 3 suffices.) All k <= 3. The final gcd and the measure
bound are as in K63-RES section 1. QED

**Corollary 5/6-62.** At an unmarked v in O: if FG-62 holds for V = U* then every lambda^alpha-feasible y has
val(y) <= 5 (LFC side, via W*U_v disjoint from every g_jU_jU_v); if FG-62 holds for V = U then every
lambda^(alpha*)-feasible y has val(y) <= 5 (VFC side, via U_vW disjoint from every D_j). Proofs verbatim as
K63-RES section 2 (a), (b). By Lemma D, both hold when (alpha_(d i*), alpha*_(d i*)) = (1, 1), in particular in R1
without a 3-marker in O, and the alpha-side holds when alpha*_(d i*) = 1.

## 4. Theorem R2-11 [NEW]: no R2 configuration with alpha_(d i*) = alpha*_(d i*) = 1
*Row lemma (R2, 5/6-bound).* In R2 (e_d = 2), at an unmarked v in O, if every lambda^x-feasible y has val(y) <= 5,
then at least three u in O minus {v} have x_vu = 4.

*Proof.* By Lemma OO the four O-entries lie in {1, 2, 4}. Suppose at most two are 4. Weights: y = 1 on 1-entries,
1/2 on 2-entries, 1/4 on 4-entries, y_d = 1/2, y_(i*) = 0. Types: a 1-entry has an odd type (3^(F) or 5^(h) at most),
coprime to the types of every other O-entry and of d (one 3-marker, one 5-marker); an even entry has 2-part 2 or 4
and shares no 3 or 5 with another O-entry or with d; d has type 2 * 5^(h_d), so gcd(d, even entry) = 2. Hence, up to
the weight-0 vertex i*, the allowed sets are: {1-entry}; pairs of even elements of O' cup {d}; triples containing the
two 4-entries; no 4-set (it would need three elements of pairwise gcd 4 among each 3-subset). All have sum <= 1. val =
(number of O-entries, each contributing 1) + 3/2 = 4 + 3/2 > 5. QED

*Proof of R2-11.* Choose an unmarked v in O (at least three exist). By Lemma D and Corollary 5/6-62 both 5/6-bounds
hold at v. By the row lemma, alpha_vu = 4 for at least three u and alpha*_vu = 4 for at least three u among the four
u in O minus {v}; some u has alpha_vu = alpha*_vu = 4, contradicting INV (b) (sum <= 6). R0 lifts. QED

## 5. Exact obstruction in R1 (single-vertex method)
The single-vertex constraints used above do **not** exclude R1 (e_d >= 3, e* = 2), even where FG-62 holds in both
orientations. Example (any R1 configuration data with e_d >= 3, e* = 2, the 5-marker absent, the 3-marker on i* or
on a vertex of O with entry 2): at an unmarked v, the joint row
  alpha_v(u1, u2, u3, u4) = (4, 4, 2, 2), alpha*_v(u1, u2, u3, u4) = (2, 2, 4, 4), alpha_(v i*) = alpha*_(v i*) = 1,
  alpha_vd = alpha*_vd = 1
satisfies INV at v, Lemma OO, and val(y) <= 5 for every feasible y in both orientations. Certificate for the alpha-row
(the alpha*-row is the same up to renaming): types u1, u2: 4 (load 4); u3, u4: 2 (load 2); i*: 2 * 3^(f* - 1) (load 1);
d: 2^(e_d - 1), divisible by 4 (load 3). Allowed sets: pairs; triples containing two of {u1, u2, d}; the 4-sets
{u1, u2, d, z}; no 5-set (no gcd >= 5). The dual weights 2 on {u1, u2, d, u3}, 2 on {u1, u2, d, u4}, 1 on {i*} cover
every load (u1, u2: 4; d: 4 >= 3; u3, u4: 2; i*: 1), so every feasible y has val(y) <= 2 + 2 + 1 = 5.
So closing R1 needs constraints coupling several vertices (for example the rows of i* and d, or triangle/RPLP-type
facts); FG-62 + LFC at one vertex cannot do it.

## 6. Exact remaining gap after this file (if its candidates are accepted)
- **R1** (e_d >= 3): open in all sub-cases (Lemma D gives alpha_(d i*) = alpha*_(d i*) = 1 when no 3-marker is in O;
  Lemma OO restricts O-O entries to {1, 2, 4}; FG-62 gives both 5/6-bounds at unmarked O-vertices when no 3-marker is
  in O; section 5 shows this is not enough at one vertex).
- **R2** with {alpha_(d i*), alpha*_(d i*)} = {1, 3}: open. Here FG-62 gives the 5/6-bound only in the orientation
  whose d-i* entry is 1 (the row lemma then forces three 4-entries in that orientation at every unmarked v); the other
  orientation needs another argument (FG-62 can fail there only through a T-factor 7 in the step that adds t or i*).
- Full Sun(7) OPEN; K7 not examined (owned by Sun7K62Successor).

## 7. Verification boundary
Written, single author, unreviewed; no computation. Requested: parent re-derivation of Lemma D (the single gcd 9),
Lemma OO (the h_d >= 1 five case, which uses both orientations), the step bounds of FG-62 (t requires
beta_(d i*) <= 2), and the R2 row-lemma weights.
