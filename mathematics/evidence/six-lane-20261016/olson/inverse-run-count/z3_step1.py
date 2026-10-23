"""Aid: z3 exploration of Step 1 (split at a chain step) for mixed all-odd words.
Mass bookkeeping: prefix P_{j-1} has nP >= 1 runs, rotation mass RP, net Dj1; run t has rt, dt;
bP = (RP - Dj1)/2 letters rho_-1 in the prefix, bt = (rt - dt)/2; the k - nP - 1 other runs have
mass >= 1 each."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, B, A, k, Dj1, dt, nP, RP, rt = [Int(x) for x in 'p kap B A k Dj1 dt nP RP rt'.split()]
R = A + B
bP2 = RP - Dj1; bt2 = rt - dt          # twice the rho_-1 counts
base = [p >= 5, B >= 1, B <= kap, A >= B, A <= 2 * p - 2, kap <= p - 1, 2 * kap == R + k - 2 * p,
        k >= 3, nP >= 1, nP <= k - 2, RP >= nP, rt >= 1,
        bP2 >= 0, bt2 >= 0, (RP + Dj1) >= 0, (rt + dt) >= 0,
        bP2 % 2 == 0, bt2 % 2 == 0,
        bP2 + bt2 <= 2 * B, (RP + Dj1) + (rt + dt) <= 2 * A,
        RP + rt + (k - nP - 1) <= R]
cyc = [Dj1 >= 1, Dj1 + dt >= 1]
Bp = g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap) + g(p, 1, B + Dj1 + dt, kap) >= p - 2
Ap = g(p, 1, B + Dj1, kap) + g(p, 1, B + dt, kap) + g(p, 1, A - Dj1 - dt, kap) >= -2
for name, hyp in [('plain', base), ('cycle-start', base + cyc)]:
    for gname, goal in [("B'", Bp), ("A'", Ap)]:
        mdl = prove(hyp, goal, name + ' ' + gname)
        if mdl is not None:
            print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, Dj1, dt, nP, RP, rt]})
