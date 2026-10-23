"""Aid: z3 check of (9.1) for aligned / balanced t, and of variants, mixed all-odd pure/(1,1)."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, B, A, k, Dj1, dt, nP, RP, rt = [Int(x) for x in 'p kap B A k Dj1 dt nP RP rt'.split()]
R = A + B; kB = kap - B
bP2 = RP - Dj1; bt2 = rt - dt
base = [p >= 5, B >= 1, B <= kap, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
        k >= 3, nP >= 1, nP <= k - 2, RP >= nP, rt >= 1,
        bP2 >= 0, bt2 >= 0, (RP + Dj1) >= 0, (rt + dt) >= 0, bP2 % 2 == 0, bt2 % 2 == 0,
        bP2 + bt2 <= 2 * B, (RP + Dj1) + (rt + dt) <= 2 * A, RP + rt + (k - nP - 1) <= R,
        Or(dt == rt, dt == -rt, And(dt == 0, rt == 2)),
        dt <= 2 * kB - 2]
S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
for nm, extra in [('aligned t, any start', [dt >= 1]),
                  ('aligned t, cycle start', [dt >= 1, Dj1 >= 1]),
                  ('balanced t, cycle start', [dt == 0, Dj1 >= 1]),
                  ('aligned t, prefix all aligned', [dt >= 1, bP2 == 0]),
                  ('anti t, prefix all aligned', [dt <= -1, bP2 == 0])]:
    mdl = prove(base + extra, S >= p - 1, nm)
    if mdl is not None:
        print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, Dj1, dt, nP, RP, rt]})
