"""Realise z3 MFE violations (z3_mfe.py) as concrete MIX_DEF words with p prime, check them exactly
(no full window, the violated local inequalities recomputed from the exact windows), and test IL
on all interval-feasible phi of the concrete word.  Aid only; scope = lemmas MFE / IL."""
import sys, os
from z3 import Int, And, Or, If, Solver, sat, Not
sys.path.insert(0, '..')
from z3lib import g
from scl_closure import tables
from il_check import feasible_phis, gap_rep

found = []
for pp in [5, 7, 11, 13]:
    for side in ['plus', 'minus']:
        p, kap, B, A, k = Int('p'), Int('kap'), Int('B'), Int('A'), Int('k')
        dM, d1, d2, nM, rM, r1, r2 = [Int(x) for x in 'dM d1 d2 nM rM r1 r2'.split()]
        R = A + B; kB = kap - B
        ok = lambda d, r: Or(d == r, d == -r, And(d == 0, r == 2))
        H = [p == pp, B >= 1, kB >= 1, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
             k >= 3, k <= 2 * p - 2, nM >= 0, nM + 2 <= k - 1, ok(d1, r1), ok(d2, r2), r1 >= 1, r2 >= 1,
             rM >= nM, rM <= 2 * nM, (rM - dM) % 2 == 0, rM - dM >= 0, rM + dM >= 0,
             If(nM == 0, And(rM == 0, dM == 0), rM >= 1), dM == rM,          # middle: aligned runs
             (r1 - d1) + (r2 - d2) <= 2 * B, (rM + dM) + (r1 + d1) + (r2 + d2) <= 2 * A,
             rM + r1 + r2 + (k - nM - 2) <= R]
        Uiv = lambda Dx: g(p, 1, B + Dx, kap); Liv = lambda Dx: g(p, 1, A - Dx, kap)
        DQ = dM + d1 + d2
        UM = If(nM == 0, g(p, 0, B, kap), Uiv(dM)); LM = If(nM == 0, g(p, 0, A, kap), Liv(dM))
        if side == 'plus':
            viol = Not(Or(Liv(DQ - d2) + Liv(d2) + Uiv(DQ) >= p - 2, Liv(DQ - d1) + Liv(d1) + Uiv(DQ) >= p - 2,
                          LM + Liv(d1) + Liv(d2) + Uiv(DQ) >= 2 * p - 3))
        else:
            viol = Not(Or(Uiv(DQ - d2) + Uiv(d2) + Liv(DQ) >= -2, Uiv(DQ - d1) + Uiv(d1) + Liv(DQ) >= -2,
                          UM + Uiv(d1) + Uiv(d2) + Liv(DQ) >= -3))
        s = Solver(); s.add(*H); s.add(viol)
        tries = 0
        while tries < 6 and s.check() == sat:
            tries += 1
            m = s.model(); v = {str(x): m[x].as_long() for x in [kap, B, A, k, dM, d1, d2, nM, rM, r1, r2]}
            s.add(Or(kap != m[kap], B != m[B], d1 != m[d1], d2 != m[d2], nM != m[nM], k != m[k]))
            # concrete word: runs 0 = t', 1..nM = M (aligned, masses spread), nM+1 = t, then the rest
            kk = v['k']; a = []; b = []
            def put(d, r):
                if d > 0: a.append(r); b.append(0)
                elif d < 0: a.append(0); b.append(r)
                else: a.append(1); b.append(1)
            put(v['d1'], v['r1'])
            Mm = [1] * v['nM']
            for i in range(v['rM'] - v['nM']): Mm[i % max(1, v['nM'])] += 1
            for x in Mm: a.append(x); b.append(0)
            put(v['d2'], v['r2'])
            rest = kk - v['nM'] - 2
            remA = v['A'] - sum(a); remB = v['B'] - sum(b)
            if rest <= 0 or remA < 0 or remB < 0 or remA + remB < rest:
                continue
            # rest: anti singletons for remB (as far as possible), aligned for remA
            ra = [0] * rest; rb = [0] * rest
            nanti = min(remB, rest - (1 if remA > 0 else 0))
            for i in range(nanti): rb[i] = 1
            if nanti: rb[0] += remB - nanti
            elif remB: continue
            al = list(range(nanti, rest))
            if al:
                if remA < len(al): continue
                for i in al: ra[i] = 1
                ra[al[0]] += remA - len(al)
            elif remA: continue
            a += ra; b += rb
            Hh = pp - 1 - v['kap']; l = [1] * kk
            for i in range(Hh): l[(i * 3) % kk] += 2
            if sum(a) + sum(b) + sum(l) != 4 * pp - 2: continue
            U, L = tables(a, b, l, pp); full = (1 << kk) - 1
            if any(U[P] + L[P] + 1 >= pp for P in range(1, full)):
                continue
            Q = sum(1 << i for i in range(v['nM'] + 2))
            phis = feasible_phis(pp, a, b, l, 4000)
            ilfail = 0
            for phi in phis:
                x = [gap_rep(U, L, 1 << t, phi[t], pp) for t in range(kk)]
                sQ = sum(phi[t] for t in range(kk) if (Q >> t) & 1) % pp
                if gap_rep(U, L, Q, sQ, pp) != sum(x[t] for t in range(kk) if (Q >> t) & 1):
                    ilfail += 1
            found.append((pp, side, a, b, l, 'Q=runs 0..%d' % (v['nM'] + 1), 'phis', len(phis), 'IL_fail_at_Q', ilfail))
            print(found[-1], flush=True)
print('done', len(found))
