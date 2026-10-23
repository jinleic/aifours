"""Aid: kappa_B = 0 (B = kappa) all-odd mixed: (9.1) for potential defects (anti runs with r >= 2)."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, B, A, k, Dj1, dt, nP, RP, rt = [Int(x) for x in 'p kap B A k Dj1 dt nP RP rt'.split()]
R = A + B; bP2 = RP - Dj1; bt2 = rt - dt
base = [p >= 5, B >= 1, B == kap, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
        k >= 3, nP >= 1, nP <= k - 2, RP >= nP, rt >= 1,
        bP2 >= 0, bt2 >= 0, (RP + Dj1) >= 0, (rt + dt) >= 0, bP2 % 2 == 0, bt2 % 2 == 0,
        bP2 + bt2 <= 2 * B, (RP + Dj1) + (rt + dt) <= 2 * A, RP + rt + (k - nP - 1) <= R,
        Or(dt == rt, dt == -rt, And(dt == 0, rt == 2)), dt <= -2]
S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
for nm, extra in [('any start', []), ('cycle start', [Dj1 >= 1, Dj1 + dt >= 1]), ('k>=p+1', [k >= p + 1])]:
    mdl = prove(base + extra, S >= p - 1, 'kappa_B=0 ' + nm)
    if mdl is not None:
        print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, Dj1, dt, nP, RP, rt]})
