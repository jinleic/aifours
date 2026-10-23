"""Aid: z3 search for chain steps where (9.1) S = U_j + L_{j-1} + L^t >= p-1 fails, for a run t that can
be a defect (d_t <= 2 kappa_B - 2), mixed all-odd words with pure/(1,1) runs, cycle-lemma start."""
from z3 import Int, And, Or, Solver, Not, sat
from z3lib import g
p, kap, B, A, k, Dj1, dt, nP, RP, rt = [Int(x) for x in 'p kap B A k Dj1 dt nP RP rt'.split()]
R = A + B; kB = kap - B
bP2 = RP - Dj1; bt2 = rt - dt
base = [p >= 5, p <= 41, B >= 1, B <= kap, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
        k >= p + 1, nP >= 1, nP <= k - 2, RP >= nP, rt >= 1,
        bP2 >= 0, bt2 >= 0, (RP + Dj1) >= 0, (rt + dt) >= 0, bP2 % 2 == 0, bt2 % 2 == 0,
        bP2 + bt2 <= 2 * B, (RP + Dj1) + (rt + dt) <= 2 * A, RP + rt + (k - nP - 1) <= R,
        Or(dt == rt, dt == -rt, And(dt == 0, rt == 2)),           # pure or (1,1) run
        Dj1 >= 1, Dj1 + dt >= 1,                                     # cycle-lemma start
        dt <= 2 * kB - 2]                                            # t can be a defect
S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
s = Solver(); s.add(*base); s.add(S < p - 1)
seen = 0
while seen < 12 and s.check() == sat:
    m = s.model(); vals = {str(v): m[v].as_long() for v in [p, kap, B, A, k, Dj1, dt, nP, RP, rt]}
    print(vals, 'S=', m.eval(S), 'p-1=', vals['p'] - 1)
    s.add(Or(p != m[p], kap != m[kap], B != m[B], dt != m[dt], Dj1 != m[Dj1]))
    seen += 1
print('done', seen)
