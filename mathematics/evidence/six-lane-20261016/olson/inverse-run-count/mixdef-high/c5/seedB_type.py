#!/usr/bin/env python3
"""seedB_type.py -- [F] EXPLORATORY (c5 README Sec. 8): does the B = 1 recipe of c5/proof-SEED-r2.md (pair seed for aligned
runs, plain canonical range for anti runs, Lemma CW removal order, pin through one anti run and its complement) extend to
all-singleton item-(iii) words with B >= 2 anti runs?  Type-level check over all (j, e, m) (a superset of the realisable
types; anti-only patterns remove an anti run).  All-singleton arcs: lam(y, m) = min(p - m + 1, y + m - kB, floor((y + B)/2) + 1),
lamc(y, m) = min(p - m + 1, p - B - y + m, floor((p + kB - y)/2) + 1) (k = p + kB + B, y = D_Q).  Pair seed with
m0 = ceil((kB + floor(B/2) + 1)/2) pairs (realisability NOT checked).  Output: per prime, the classes where the recipe passes
and the first failing step type of the others.  This is not used by any written proof.
"""
from collections import Counter
def isprime(n): return n > 1 and all(n % r for r in range(2, int(n ** 0.5) + 1))
def mk(p, kB, B):
    lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
    lamc = lambda y, m: min(p - m + 1, p - B - y + m, (p + kB - y) // 2 + 1)
    return lam, lamc, (lambda y, m: p - lamc(y, m))
def check(p, kB, B):
    lam, lamc, U = mk(p, kB, B)
    n = p + kB; k = n + B
    m0 = -(-(kB + B // 2 + 1) // 2)
    lo = lam(2 * m0 + 1, m0) - U(2 * m0, m0); hi = U(2 * m0 + 1, m0) - lam(2 * m0, m0)
    L1, U1 = lam(1, 1), U(1, 1)
    if hi - lo + 1 >= p: return ('seed-wide', None)
    vals = sorted(set(((y - L1) % p) + L1 for y in range(lo, hi + 1)))
    vals = [v for v in vals if v <= U1]
    if not vals: return ('seed-empty', None)
    if vals[-1] - vals[0] + 1 != len(vals): return ('seed-noncontiguous', None)
    a, b = vals[0], vals[-1]; a0, b0 = lam(-1, 1), U(-1, 1)
    for s in range(2, k):
        for e in range(0, min(B, s) + 1):
            j = s - e
            if j > n: continue
            for m in range(1, min(s, k - s) + 1):
                y = j - e; mp = m if m < s else m - 1
                if mp < 1: continue
                if j >= 1: yp, at, bt = y - 1, a, b
                else: yp, at, bt = y + 1, a0, b0
                if s - 1 == 1: lo1, hi1 = ((a, b) if (j >= 1 and e == 0) else (a0, b0)) if j >= 1 else (a0, b0)
                else: lo1, hi1 = lam(yp, mp), U(yp, mp)
                okA = lo1 + at >= U(y, m) + 1 - p; okB = hi1 + bt <= p + lam(y, m) - 1
                if not (okA and okB):
                    kind = 'anti-only' if j == 0 else ('pair' if s == 2 else 'mixed' if e > 0 else 'aligned')
                    return ('step-fail:' + kind, (s, j, e, m))
    yc = n - (B - 1)
    if lam(yc, 1) + a0 >= 1 and U(yc, 1) + b0 <= 2 * p - 1: return ('pass', None)
    return ('pin-fail', None)
tot = Counter()
for p in [q for q in range(11, 44) if isprime(q)]:
    c = Counter(); ex = {}
    for k in range(p + 2, 2 * p - 2):
        for B in range(1, k - p):
            kB = k - p - B
            r, info = check(p, kB, B)
            key = (r, 'B=1' if B == 1 else 'B>=2'); c[key] += 1; tot[key] += 1
            ex.setdefault(key, (k, B, kB, info))
    print(p, sorted(c.items()), {str(kk): v for kk, v in ex.items() if kk[0] != 'pass'})
print('TOTAL', sorted(tot.items()))
