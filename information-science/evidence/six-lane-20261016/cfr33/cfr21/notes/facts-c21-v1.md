# Facts c21-v1: (Z_21, 7; 1) difference matrices = CFR(6,21) (worker InfoCFR27Lift; written 2026-10-17 18:50 PDT)

Proofs are by hand unless marked [computation] or [HEURISTIC]. Earlier lane facts are cited as ../../notes/facts-vN.md.
Notation: a DM has k = 7 rows (r = 6 CFR rows, facts-v1 E2); columns modulo constants; group elements (mu, pi[, t])
act on a column by (s c)_x = mu c_{pi^-1(x)} (+ t_x); pi[i] = image of row i.

## C1 Constants
Q = sum_{z in Z_21} z^2 = 21*20*41/6 = 2870 = 14 (mod 21); q = Q/2 = 14 * 11 = 7 (mod 21) (11 = 2^-1). Q != 0, as
facts-v3 E7 states for every odd n with 3 | n. Gram (facts-v3 E8): if row 0 is normalised to 0 then b(r_i, r_i) = 14
and b(r_i, r_j) = 7 (mod 21) for distinct nonzero rows, where b(u, v) = sum_t u(t) v(t).
Units mod 21 (12, group Z_2 x Z_6) and h(mu) = |Fix(mu)| = gcd(mu - 1, 21):
h = 21 for mu = 1; h = 3 for mu in {4, 10, 13, 16, 19} (mu = 1 mod 3, not mod 7); h = 7 for mu = 8; h = 1 for
mu in {2, 5, 11, 17, 20}. Elements of order 3: 4, 16; of order 2: 8, 13, 20; of order 6: 2, 5, 10, 11, 17, 19.
kmax(Z_3) = 3 and kmax(Z_7) = 7 (Jungnickel m <= lambda |G|, attained by the field tables); trivial group: no bound.

## C2 Dead elements (an element whose presence in G forces G-invariant DMs not to exist)
* E3 (facts-v1, any n): pi with F >= 2 fixed rows forces an (H, F; 1)-DM, H = Fix(mu): dead if F > kmax(h).
* E3b (facts-v2, any n): pi != id with F >= 2 fixed rows: dead if h^2 > n. At n = 21: mu in {1, 8} with pi != id and
  F >= 2 is dead; mu with h = 3 needs F <= 3.
* G1 (new; any odd n with 3 | n, k >= 4): (-1, pi) with pi an involution != id is dead.
  Proof. Relabel so that pi swaps rows 0 and 1; normalise row 0 to 0 and row 1 to the column index t (row 1 - row 0 is
  a bijection). s(c) = (-t, 0, ..., -c_{pi(x)}, ...) renormalised is (0, t, ..., t - c_{pi(x)}(t), ...), which has row-1
  entry t, so invariance gives f_x + f_{pi(x)} = id for all rows x >= 2. A fixed row x >= 2 gives f_x = 2^-1 id, a
  linear row, impossible with k >= 4 by facts-v3 E7. Otherwise pi swaps some x <-> y (x, y >= 2) and
  b(f_x, f_y) = b(f_x, id) - b(f_x, f_x) = q - Q = -q, while E8 requires q; -q = q means Q = 0, false (E7). QED.
  (At n = 27, k = 6 this contains facts-v7 F1 (fixed-point-free case) and also kills S3b = <(1,(012)(345)),
  (26,(12)(45))>, consistent with the xc result "no valid orbit" in ../../cfr27/README.md section 7.)
* An element is dead if any of its powers is dead; the enumerator closes groups and rejects any dead element.
[computation] ../code/groups_enum_c21v1.c implements E3, E3b, G1. Calibration at n = 27, k = 6, order 6
(../calib/groups-v1/): with G1 exactly the 5 classes T8, T6, T10, T4odd, S3a; without G1 exactly 9 = those 5 plus
T9, T8neg, S3b and <(1,(012)(345)), (26,(03)(15)(24))>, i.e. precisely the groups killed by hand (facts-v7 F1/F4 and
G1). This agrees with the hand classification of ../../notes/facts-v7.md F3/F4 (which had listed S3b as alive; G1
explains why its xc run had no valid orbit).

## C3 Per-row multiplier models (pi = id: every f-row satisfies f(mu x) = mu f(x) for mu in K)
(mu, id) is alive iff 7 <= kmax(h(mu)): excluded h = 3, i.e. mu in {4, 10, 13, 16, 19}; allowed 8 (h = 7) and
{2, 5, 11, 17, 20} (h = 1). Every element of order 3 (4, 16) is excluded, and every element of order 6 has an excluded
square; so K lies in the 2-torsion {1, 8, 13, 20} and avoids 13: K in { {1}, <20> (odd model), <8> }.
<8>-model structure: Fix(8) = 3Z_21 (7 elements); f(8x) = 8 f(x) forces f(3Z_21) = 3Z_21, and the 7 DM rows restricted
to the 7 columns of 3Z_21 form a (Z_7, 7; 1)-DM (E3 with F = all rows); the other 14 columns form 7 orbits {x, 8x}.

## C4 Twists
Twisted elements (mu, pi, t): conjugation by row translations u changes t by (L - 1)u; classes = H^1(G, Z_21^7/diag).
Since 21 is squarefree, H^1 = H^1 over GF(3) (+) H^1 over GF(7) (CRT). [computation] ../code/twist_h1_c21v1.py
(linear algebra) agrees with the brute-force copies of the n = 27 tools on 8 cyclic and 3 S_3 groups at n = 21, k = 4
(class counts 1, 1, 1, 3, 1, 1, 1, 9 and 1, 1, 1; cocycle and coboundary counts 3^a 7^b match), ../calib/h1-v1/.
A twisted group with a G-fixed column is conjugate to the untwisted group (translate by that column), so for a
nontrivial class only DMs without a G-fixed column are new (xc mode nozero).

## C5 Remarks on specific models
* <(1, (0 1 2 3 4 5))>, row 6 fixed (the shape of Sage DM_55_7_1 over Z_55, Handbook III.3.72, and of DM_21_6_1 with a
  5-cycle): a G-fixed column has all differences 0 among rows 0..5, a column of an orbit of size 2 (resp. 3) has
  difference 0 on the pairs {0,2},{2,4},{0,4},{1,3},{3,5},{1,5} (resp. {0,3},{1,4},{2,5}). Counting 21 = N1 + 2N2 + 3N3 +
  6N6 with these collisions forces N1 = N2 = 0, N3 = 1, N6 = 3 (orbit sizes [3,6,6,6], no fixed column).
* (mu, 7-cycle): the 7th power is (mu, id) (mu^7 = mu since mu^6 = 1), so mu in {1, 8, 20}.
* [HEURISTIC] The independence model of facts-v2 E6 predicts ~1e-32 unrestricted normal forms of a (Z_21,7;1)-DM and
  ~1e-9 for a (Z_21,6;1)-DM, yet the 5-cycle model alone has 96 solutions for k = 6 (cfr27 calib-xc): solutions at
  n = 21 are far from random and symmetric models are the realistic search space. No probability statement is made.
* Consequence of existence (facts-v1 E2): a (Z_21, 7; 1)-DM gives a TD(8, 21), i.e. 6 MOLS(21). Whether this exceeds the
  published lower bound for N(21) is for the parent's priority/viability screen; no claim here.
