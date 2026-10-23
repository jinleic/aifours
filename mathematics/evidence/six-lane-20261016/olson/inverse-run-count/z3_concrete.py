"""Aid: find a (9.1)-failing chain step for mixed all-odd pure/(1,1) words with p prime and
R <= 2p-3, build a concrete word, and test chain-lift canonicity on interval-feasible phi."""
from z3 import Int, And, Or, Solver, sat
from z3lib import g
import random
from scl_closure import tables
from chainlift_test import run as hws
for pp in [7, 11, 13]:
    p, kap, B, A, k, Dj1, dt, nP, RP, rt = [Int(x) for x in 'p kap B A k Dj1 dt nP RP rt'.split()]
    R = A + B; kB = kap - B; bP2 = RP - Dj1; bt2 = rt - dt
    s = Solver()
    s.add(p == pp, B >= 1, B <= kap, A >= B, R <= 2 * p - 3, kap <= p - 1, 2 * kap == R + k - 2 * p,
          k >= p + 1, nP >= 1, nP <= k - 2, RP >= nP, rt >= 1, bP2 == 0, Dj1 == RP,
          bt2 >= 0, (rt + dt) >= 0, bt2 % 2 == 0, bt2 <= 2 * B, 2 * RP + (rt + dt) <= 2 * A,
          RP + rt + (k - nP - 1) <= R, Or(dt == rt, dt == -rt, And(dt == 0, rt == 2)),
          dt <= 2 * kB - 2, RP <= 2 * nP)
    S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
    s.add(S < p - 1)
    if s.check() != sat:
        print(pp, 'no counterexample'); continue
    m = s.model(); v = {str(x): m[x].as_long() for x in [kap, B, A, k, Dj1, dt, nP, RP, rt]}
    print(pp, v)
    k_ = v['k']; nP_ = v['nP']; RP_ = v['RP']
    # prefix: nP aligned runs with total RP (spread), then t, then the rest: remaining aligned and anti
    a = []; b = []
    pre = [1] * nP_
    for i in range(RP_ - nP_):
        pre[i % nP_] += 1
    a += pre; b += [0] * nP_
    if v['dt'] > 0: a.append(v['rt']); b.append(0)
    elif v['dt'] < 0: a.append(0); b.append(v['rt'])
    else: a.append(1); b.append(1)
    remA = v['A'] - sum(a); remB = v['B'] - sum(b); rest = k_ - nP_ - 1
    # rest runs: anti runs to absorb remB, aligned runs absorb remA
    ra = []; rb = []
    nanti = min(remB, rest - 1) if remA > 0 else rest
    if remA <= 0: nanti = rest
    for i in range(rest):
        ra.append(0); rb.append(0)
    for i in range(nanti):
        rb[i] = 1
    extraB = remB - nanti
    if nanti > 0:
        rb[0] += max(0, extraB)
    al_idx = list(range(nanti, rest))
    if al_idx:
        for i in al_idx: ra[i] = 1
        extraA = remA - len(al_idx)
        ra[al_idx[0]] += extraA
    a += ra; b += rb
    if min(x + y for x, y in zip(a, b)) < 1 or sum(a) != v['A'] or sum(b) != v['B'] or min(a + b) < 0:
        print('   construction failed', a, b); continue
    F = 4 * pp - 2 - sum(a) - sum(b); H = pp - 1 - v['kap']
    l = [1] * k_
    for i in range(H): l[i % k_] += 2
    assert sum(l) == F
    U, L = tables(a, b, l, pp)
    full = (1 << k_) - 1
    print('   a', a, 'b', b, 'l', l, 'anyfull', any(U[P] + L[P] + 1 >= pp for P in range(1, full)))
    sols = hws(pp, 1, a, b, l, 2000, 2000)
    tt = nP_; bad = 0; tot = 0
    d = [x - y for x, y in zip(a, b)]
    for phi in sols:
        prev = 0; x = [0] * k_; ok = True
        for j in range(1, k_ + 1):
            P = (1 << j) - 1; s_ = sum(phi[:j]) % pp
            if j == k_: cand = pp
            else:
                lo, hi = -L[P], U[P]
                cand = hi + 1 + ((s_ - (hi + 1)) % pp)
            x[j - 1] = cand - prev; prev = cand
        lo, hi = -L[1 << tt], U[1 << tt]
        xc = hi + 1 + ((phi[tt] - (hi + 1)) % pp)
        tot += 1
        if xc != x[tt]: bad += 1
    print('   interval-feasible phi:', tot, 'non-canonical at t:', bad)
