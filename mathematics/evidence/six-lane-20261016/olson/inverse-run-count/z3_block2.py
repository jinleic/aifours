"""Aid: block-level Step-1 inequality (9.1) and split (A'),(B') with blocks of net mass >= 1,
j = k - kb merges, j <= 2B (block construction bound), kappa_B >= 1 (the agreed range kappa > B)."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, B, A, k, kb, Dj1, dt, nb = [Int(x) for x in 'p kap B A k kb Dj1 dt nb'.split()]
R = A + B; kB = kap - B; D = A - B
base = [p >= 5, B >= 1, kB >= 1, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
        kb >= 3, kb <= k, nb >= 1, nb <= kb - 2, Dj1 >= nb, dt >= 1, D - Dj1 - dt >= kb - nb - 1,
        D >= kb, k - kb <= 2 * B, kap <= p - 2]
S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
UP = g(p, 1, B + Dj1, kap); LP = g(p, 1, A - Dj1, kap); Ut = g(p, 1, B + dt, kap); Lt = g(p, 1, A - dt, kap)
UQ = g(p, 1, B + Dj1 + dt, kap); LQ = g(p, 1, A - Dj1 - dt, kap)
for nm, goal, extra in [('(9.1) defect t', S >= p - 1, [dt <= 2 * kB - 2]),
                        ("A'", UP + Ut + LQ >= -2, []), ("B'", LP + Lt + UQ >= p - 2, [])]:
    mdl = prove(base + extra, goal, nm)
    if mdl is not None:
        print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, kb, Dj1, dt, nb]})
