"""Aid: z3 check of (9.1) for B = 1 all-odd words: one special run s (d_s in {-1, 0}) placed LAST in
the interval chain; t aligned, prefix aligned (no rho_-1 in P_j)."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, A, k, Dj1, dt, nP, RP, rt, ds = [Int(x) for x in 'p kap A k Dj1 dt nP RP rt ds'.split()]
B = 1
R = A + B; kB = kap - B
base = [p >= 5, kap >= 1, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
        k >= p + 1, nP >= 1, nP <= k - 2, Dj1 == RP, RP >= nP, rt == dt, dt >= 1,
        Or(ds == -1, ds == 0),
        RP + rt + (k - nP - 2) + (2 if True else 0) <= R + (1 if True else 0),   # loose mass bound
        Dj1 + dt <= A, dt <= 2 * kB - 2]
# exact mass bookkeeping: aligned mass A = RP + rt + (others aligned, >= k - nP - 2 runs of mass >= 1) + a_s
base += [A >= RP + rt + (k - nP - 2) + If_(True)] if False else []
S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
mdl = prove(base + [RP + rt + (k - nP - 2) <= A], S >= p - 1, 'B=1, s last, t aligned')
if mdl is not None:
    print('   ', {str(v): mdl[v] for v in [p, kap, A, k, Dj1, dt, nP, RP, rt, ds]})
