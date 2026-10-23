"""Aid: z3 check of the C0 Step-1 inequality (9.1) for mixed all-odd pure/(1,1) words in regime
R <= 2p-3 (no full windows possible), for potential defects t, with / without cycle start."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, B, A, k, Dj1, dt, nP, RP, rt = [Int(x) for x in 'p kap B A k Dj1 dt nP RP rt'.split()]
R = A + B; kB = kap - B
bP2 = RP - Dj1; bt2 = rt - dt
base = [p >= 5, B >= 1, B <= kap, A >= B, R <= 2 * p - 3, kap <= p - 1, 2 * kap == R + k - 2 * p,
        k >= 3, nP >= 1, nP <= k - 2, RP >= nP, rt >= 1,
        bP2 >= 0, bt2 >= 0, (RP + Dj1) >= 0, (rt + dt) >= 0, bP2 % 2 == 0, bt2 % 2 == 0,
        bP2 + bt2 <= 2 * B, (RP + Dj1) + (rt + dt) <= 2 * A, RP + rt + (k - nP - 1) <= R,
        Or(dt == rt, dt == -rt, And(dt == 0, rt == 2)),
        dt <= 2 * kB - 2]
S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
for nm, extra in [('any t, any start', []), ('any t, cycle start', [Dj1 >= 1, Dj1 + dt >= 1]),
                  ('aligned t', [dt >= 1]), ('anti t', [dt <= -1]), ('k >= p+1', [k >= p + 1])]:
    mdl = prove(base + extra, S >= p - 1, nm)
    if mdl is not None:
        print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, Dj1, dt, nP, RP, rt]})
