"""z3 check (symbolic p) of the minimal-failure exclusion MFE for interval lifts in MIX_DEF words.
Q = t' + M + t is a proper cyclic interval with ends t', t and middle M (possibly empty).  If all
proper sub-intervals of Q have lift = sum of canonical singleton lifts, then lift(Q) = sum as
well, provided (no +p jump)  some upper bound on s(Q) is <= p + U_Q  and (no -p jump) some lower
bound is >= -L_Q, using the three decompositions (Q-t)+t, t'+(Q-t'), t'+M+t.
Run data: all reflection runs odd, every run pure or a (1,1)-pair, 1 <= B < kappa, B <= A."""
from z3 import Int, And, Or, If, Not, Solver, sat, unsat
import sys
sys.path.insert(0, '..')
from z3lib import g, prove

p, kap, B, A, k = Int('p'), Int('kap'), Int('B'), Int('A'), Int('k')
dM, d1, d2 = Int('dM'), Int('d1'), Int('d2')          # d1 = d_{t'}, d2 = d_t
nM, rM, r1, r2 = Int('nM'), Int('rM'), Int('r1'), Int('r2')
R = A + B; kB = kap - B; D = A - B


def run_ok(d, r):
    return Or(d == r, d == -r, And(d == 0, r == 2))


hyp = [p >= 5, B >= 1, kB >= 1, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p, k >= 3,
       nM >= 0, nM + 2 <= k - 1, run_ok(d1, r1), run_ok(d2, r2), r1 >= 1, r2 >= 1,
       rM >= nM, (rM - dM) % 2 == 0, rM - dM >= 0, rM + dM >= 0,
       If(nM == 0, And(rM == 0, dM == 0), rM >= 1),
       # rho_{-1} letters: in M (rM-dM)/2, in t', t, total <= B; rho_1 similarly <= A
       (rM - dM) + (r1 - d1) + (r2 - d2) <= 2 * B, (rM + dM) + (r1 + d1) + (r2 + d2) <= 2 * A,
       rM + r1 + r2 + (k - nM - 2) <= R]


def Uiv(Dx):
    return g(p, 1, B + Dx, kap)


def Liv(Dx):
    return g(p, 1, A - Dx, kap)


DQ = dM + d1 + d2
UQ, LQ = Uiv(DQ), Liv(DQ)
UQt, LQt = Uiv(DQ - d2), Liv(DQ - d2)        # Q - t
UQs, LQs = Uiv(DQ - d1), Liv(DQ - d1)        # Q - t'
U1, L1 = Uiv(d1), Liv(d1)
U2, L2 = Uiv(d2), Liv(d2)
UM = If(nM == 0, g(p, 0, B, kap), Uiv(dM))
LM = If(nM == 0, g(p, 0, A, kap), Liv(dM))
nonempty = [UQ + LQ >= 0, UQt + LQt >= 0, UQs + LQs >= 0, U1 + L1 >= 0, U2 + L2 >= 0, UM + LM >= 0]
nonfull = [UQ + LQ <= p - 2, UQt + LQt <= p - 2, UQs + LQs <= p - 2, U1 + L1 <= p - 2,
           U2 + L2 <= p - 2, If(nM == 0, True, UM + LM <= p - 2)]
plus_excl = Or(LQt + L2 + UQ >= p - 2, LQs + L1 + UQ >= p - 2, LM + L1 + L2 + UQ >= 2 * p - 3)
minus_excl = Or(UQt + U2 + LQ >= -2, UQs + U1 + LQ >= -2, UM + U1 + U2 + LQ >= -3)
for name, goal in [('MFE no +p jump', plus_excl), ('MFE no -p jump', minus_excl)]:
    for hname, H in [('base', hyp), ('base+nonfull', hyp + nonfull), ('base+nonfull+nonempty', hyp + nonfull + nonempty)]:
        m = prove(H, goal, name + ' [' + hname + ']')
        if m is not None:
            print('    ', {str(v): m[v] for v in [p, kap, B, A, k, dM, d1, d2, nM, rM, r1, r2]})
