"""Aid: z3 check of split conditions (A'),(B') at an interval-chain step (P, t) for mixed all-odd
pure/(1,1) words, adding non-fullness of the windows of P, P+t, {t} (implied by 'no full window')."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, B, A, k, Dj1, dt, nP, RP, rt = [Int(x) for x in 'p kap B A k Dj1 dt nP RP rt'.split()]
R = A + B; kB = kap - B; bP2 = RP - Dj1; bt2 = rt - dt
base = [p >= 5, B >= 1, B <= kap, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
        k >= 3, nP >= 1, nP <= k - 2, RP >= nP, rt >= 1,
        bP2 >= 0, bt2 >= 0, (RP + Dj1) >= 0, (rt + dt) >= 0, bP2 % 2 == 0, bt2 % 2 == 0,
        bP2 + bt2 <= 2 * B, (RP + Dj1) + (rt + dt) <= 2 * A, RP + rt + (k - nP - 1) <= R,
        Or(dt == rt, dt == -rt, And(dt == 0, rt == 2))]
UP = g(p, 1, B + Dj1, kap); LP = g(p, 1, A - Dj1, kap)
Ut = g(p, 1, B + dt, kap); Lt = g(p, 1, A - dt, kap)
UQ = g(p, 1, B + Dj1 + dt, kap); LQ = g(p, 1, A - Dj1 - dt, kap)
nf = [UP + LP <= p - 2, Ut + Lt <= p - 2, UQ + LQ <= p - 2, UP + LP >= 0, Ut + Lt >= 0, UQ + LQ >= 0]
Ap = UP + Ut + LQ >= -2
Bp = LP + Lt + UQ >= p - 2
for nm, extra in [('no extra', []), ('cycle start', [Dj1 >= 1, Dj1 + dt >= 1]),
                  ('k>=p+1', [k >= p + 1]), ('k>=p+1, cycle', [k >= p + 1, Dj1 >= 1, Dj1 + dt >= 1])]:
    for gn, goal in [("A'", Ap), ("B'", Bp)]:
        mdl = prove(base + nf + extra, goal, nm + ' ' + gn)
        if mdl is not None:
            print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, Dj1, dt, nP, RP, rt]})
