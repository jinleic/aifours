# Written facts v7 (worker InfoCFR27Lift; written 2026-10-17 17:05 PDT) -- symmetry models of order 6 for a (Z_27, 6; 1)-DM

Setting: D a (Z_27, 6; 1)-DM, columns modulo constants, G a finite group of maps s = (mu, pi):
(s c)_i = mu * c_{pi^-1(i)} (mu a unit of Z_27, pi a permutation of the 6 DM rows), D invariant as a column multiset.
NOTE: these are UNTWISTED actions (no row-translation part). Twisted actions (s c)_i = mu c_{pi^-1(i)} + t_i are a
different family; for elements of order 2 the twist is removable (conjugate by u = t/2), for elements of order 3 it is
not in general (the cycle sums of t modulo 3 are an invariant). Twisted models are NOT covered by anything below.

## F1 (an element (-1, fixed-point-free involution) is impossible) [written proof]
Relabel rows so that pi = (0 1)(2 3)(4 5) and normalise rows 0, 1 to zero and id (rows translated, columns indexed by
t = entry of row 1). Column c = (0, t, f_1, f_2, f_3, f_4)(t); s(c) = (-t, 0, -f_2, -f_1, -f_4, -f_3)(t), renormalised
(0, t, t - f_2(t), t - f_1(t), t - f_4(t), t - f_3(t)); this is the column with row-1 entry t, so f_1 = id - f_2
pointwise. Gram (facts-v3 E8): b(r, r') = sum_t r(t) r'(t); b(r_i, r_i) = Q = 18, b(r_i, r_j) = q = 9 (mod 27) for
distinct nonzero DM rows. Then b(r_{f1}, r_{f2}) = b(r_id - r_{f2}, r_{f2}) = q - Q = -9 = 18 != 9: contradiction.
Consequences: T8neg = <(26, (0 1 2 3 4 5))> and T9 = <(17, (0 1 2 3 4 5))> are EMPTY (their cube is
(-1, (0 3)(1 4)(2 5))); so is every G containing (-1, id) together with any (1, fixed-point-free involution).

## F2 (other dead element types, from facts-v1 E3, facts-v2 E3b/E5)
(1, pi) with pi != id having >= 2 fixed rows: all columns fixed, a moved pair (i, pi(i)) has difference 0 everywhere.
(10 or 19, pi) with >= 2 fixed rows: E3 (pi = id) or E3b (pi != id, 81 > 27). mu of order 9 or 18: E5.

## F3 (cyclic groups of order 6 that avoid F1/F2) [derivation]
pi two 3-cycles (pi3 = (0 1 2)(3 4 5)): mu of order 2 -> T4odd = <(26, pi3)>; mu of order 6 -> T6 = <(17, pi3)>
(8 gives the same group up to the generator). pi a 6-cycle (pi6): mu = 1 -> T8; mu of order 3 -> T10 = <(10, pi6)>
(cube (1, pi6^3) of type T3, square (19, pi6^2) of type T5; <(19, pi6)> is conjugate by reversing the cycle);
mu of order 2 or 6 -> cube (-1, pi6^3) dead (F1). pi of cycle type (3,2,1) or (3,1,1,1): square has >= 2 fixed rows
and multiplier 1, 10 or 19 -> dead (F2). pi of order 2 with mu of order 3 or 6: a power is (10 or 19, id) -> dead.
So the cyclic order-6 models are exactly T4odd, T6, T8, T10 (up to conjugation by row permutations and generator).

## F4 (non-abelian groups of order 6) [derivation]
G = <sigma, tau>, tau sigma tau^-1 = sigma^-1: multipliers commute, so mu_sigma = mu_sigma^-1 and mu_sigma^3 = 1, hence
sigma = (1, pi3) (pi3 fixed-point-free by F2). tau = (+-1, involution inverting pi3): (1, fixed-point-free) = S3a
(tau = (0 3)(1 5)(2 4)); (-1, involution fixing one row in each 3-cycle) = S3b (tau = (1 2)(4 5)); (-1, fixed-point-
free) dead (F1); (1, 2 fixed rows) dead (F2). Groups of order >= 12 were NOT enumerated.

## F5 (normalisation of G-fixed columns)
If a column c is fixed by G (modulo constants), translating the rows by -c turns it into the zero column and keeps the
untwisted action of every element (the translation parts mu c_{pi^-1(i)} - c_i are constant by the fixed-point
condition). Hence "contains the zero column" covers every G-invariant DM that has at least one G-fixed column; the
remaining case is "no G-fixed column at all" (nozero mode of dmorbit_xc_v1).
