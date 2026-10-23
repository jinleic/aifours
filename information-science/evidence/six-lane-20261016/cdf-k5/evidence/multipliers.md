# Exact multiplier analysis for the six orders (generated 2026-10-16 22:50-22:57 PDT)

Producer: `code/multipliers.py` (stdlib), run as `python3 code/multipliers.py 321 501 621 681 801 901 --out
evidence/multipliers-targets.json > evidence/multipliers-targets.txt` (6 min) and on calibration orders
`261 381 341` (`evidence/multipliers-calibration.json`; it reproduces the ACF 2004 structures: 261 with m = 28 as
1 T5' + 1 T3 + 1 T3' + 5 free orbits, 381 with m = 19 as one {0,127} + 3-cycle block + 6 orbits, 341 with m = 4 as two
5-cycles + 3 orbits).

Notion analysed: a unit mu with mu*B_i = e_i*B_s(i) + t_i (e_i = +-1, s a permutation of the base blocks). This
contains the Hetman-Baicheva-Topalova Definition 1.2 multipliers (all e_i = +1), so "impossible" below also rules
those out. "Feasible counting" is only a necessary condition, not existence.

Facts (proved in the script docstring; finite parts enumerated): -1 is never a multiplier (F1); every mu-fixed class
lies in a mu-stable block (F2); a mu-stable block is invariant under an affine map whose fixed points lie in one
coset of ker(e*mu - 1) (F3). Stable-block types were enumerated exhaustively over their parameters, except four
3-fixed-point families sampled with 10^6 draws (`enumeration` field in the JSON); sampling only affects which
types are listed as present, and every listed type has an explicit example.

| v | prime-order classes of Z_v^*/{+-1} | verdict |
|---|---|---|
| 321 = 3*107 | order 53 (mu=4): impossible (orbit counting); order 2 (mu=106): impossible (3Z_v classes all fixed -> every block has a fixed class -> no free blocks; counting 4a5' = 10 has no solution) | no multiplier of any order |
| 501 = 3*167 | order 83: impossible; order 2 (mu=166): feasible only with every block stable: 20 T1 + 4 T5' + 1 T3', 0 free orbits | found family has exactly this shape (difference-multiset stable, not a Definition 1.2 multiplier) |
| 621 = 27*23 | order 11: impossible; order 3 (mu=208): impossible ((mu-1)^2 = 0, so the 3-cycle type repeats a class; 10b = 103 impossible); order 2 (mu=298): feasible counting, min 10 free orbits | open |
| 681 = 3*227 | order 113: impossible; order 2 (mu=226): impossible (as 321) | no multiplier of any order |
| 801 = 9*89 | order 11: impossible; order 3 (mu=268): impossible (as 621); order 2 (mu=179): feasible counting, min 8 free orbits (22 T1 + 2 T1') | open |
| 901 = 17*53 | order 13: impossible; mu^2 = -1 (mu = 30, 242): impossible (n = 45 odd); order 2 (mu=52): feasible counting, min 14 free orbits | open |

Order-4 elements of Q for 901 contain the involution; an extra parity argument (no block can be stable under an
order-4 element, so blocks come in orbits of even size, but n = 45 is odd) also excludes them.
