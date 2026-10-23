# Written facts v3 (adds E7, E8; corrects E5) -- written 2026-10-17 15:28:04 PDT

## E5 corrections (facts-v2.md E5 ignored the translation part of "fixed modulo constants")
* mu = 1, pi = two 3-cycles [T4]: fixed columns satisfy c_pi(i) = c_i + g with 3g = 0, so g in {0, 9, 18}; the
  pair (i, pi(i)) has difference -g there, hence N_fix <= 3, and N_fix = 27 mod 3 = 0 => N_fix in {0, 3}
  (variants T4a: zero column + 2 fixed + 8 orbits of size 3; T4b: 9 free orbits). Same for mu = 10 [T5a/T5b]
  (fixed columns have c_0 - c_2 in {0, 9, 18}).
* mu = 1, pi a 6-cycle is NOT excluded by counting: orbits N1 + 2 N2 + 6 N6 = 27 with N1 + 2N2 <= 3 (s^2-fixed) and
  N1 <= 1 (s^3-fixed) give N1 = N2 = 1, N6 = 4. (Not normal-form linear; not yet searched.)
* T6 (mu = 17, two 3-cycles): the zero column exists and exactly one orbit of size 2, four of size 6 (as used).

## E7 (no linear rows when 3 | n) [written proof; cross-checked by exhaustive search]
Q := sum_{z=0}^{n-1} z^2 = n(n-1)(2n-1)/6. If n is odd and 3 | n then Q is NOT 0 mod n (n = 3m: Q = m(3m-1)(6m-1)/2
and (3m-1)(6m-1) = 1 mod 3). n = 27: Q = 6201 = 18 mod 27.
Claim: if n is odd, 3 | n, then a (Z_n, k; 1)-DM containing (after normalising one row to 0 and one row to the
identity) a row c*x has k <= 3. Equivalently no CFR(3, n) normal form {id, c x, f} exists, whatever f.
Proof. Any bijection g of Z_n has sum_t g(t)^2 = Q (mod n). Apply to f, f - x, f - c x (columns t):
2 sum_t t f(t) = Q and 2c sum_t t f(t) = c^2 Q, so c(c-1) Q = 0 (mod n); c and c - 1 are units (c x and
(c-1) x are bijections), so Q = 0 (mod n), contradiction. QED.
Cross-check (code/cfr_odd_search_v4.c, mode linear:c, exhaustive, controls/linear-row-v4/): odd f orthogonal to
{id, c x}: none for n = 27 (c = 2, 5), n = 15, 21 (c = 2); found for n = 25 (c = 7, coprime to 6).
The anharmonic orbits {2, 14, 26} and {5, 8, 11, 17, 20, 23} cover all admissible c at n = 27.
Consequence: Kirtchakov's pattern (a linear row t -> 7t in CFR(5,25)) has no analogue when 3 | n.

## E8 (Gram constraint; linear relations among rows) [written proof]
Normalise a (Z_n, k; 1)-DM so row 0 = 0; let r_1..r_(k-1) be the other rows as vectors indexed by the columns and
b(u, v) = sum_t u(t) v(t) (mod n). From the pairs (0, i), (0, j), (i, j): b(r_i, r_i) = Q and b(r_i, r_j) = q :=
Q/2 for i != j (n odd). For n = 27, q = 9 (order 3 in Z_27).
If r_m = sum_{i in S} lambda_i r_i pointwise (m not in S) then b(r_m, r_m) gives (sum lambda_i - 2) q = 0, and any
further row p not in S + {m} gives (sum lambda_i - 1) q = 0. For 3 | n (q has order 3 modulo n/(n/3)... at n = 27:
q = 9) these force sum lambda_i = 2 (mod 3) and, if an outside row exists, sum lambda_i = 1 (mod 3): contradiction.
So at n = 27 with k = 6 a linear relation among the five nonzero rows must involve all five of them with coefficient
sum = 2 (mod 3). Examples excluded: T7 (f_2 = id - f_1: sum = 0), any linear row (E7).
