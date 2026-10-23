#!/usr/bin/env python3
"""Aid only.  Strong canonical lifting (SCL) closure test (proof-RUNS.md, idea).
For run data, U_P = g_P(E+), L_P = g_P(E-).  A pattern P (|P|>=2, nonempty non-full window)
is DERIVED if some t in P has Q = P - {t} derived (or |Q| = 1 with nonempty window) and
  (A) U_Q + U_t + L_P >= -2   and   (B) L_Q + L_t + U_P >= p - 2.
Singletons with nonempty windows are derived.  Report patterns (nonempty window) not derived.
"""
import random, sys
from collections import Counter


def tables(a, b, l, p):
    k = len(a); R = sum(a) + sum(b)
    U = {}; L = {}
    for P in range(1, (1 << k) - 1):
        z = [(P >> i) & 1 for i in range(k)]
        f = [1 if z[j] != z[(j + 1) % k] else 0 for j in range(k)]
        m = sum(f) // 2
        h = sum((l[j] - f[j]) // 2 for j in range(k))
        Ep = sum(a[i] if z[i] else b[i] for i in range(k)); Em = R - Ep
        g = lambda E: min(p - m, E + m + h - p, E // 2)
        U[P] = g(Ep); L[P] = g(Em)
    return U, L


def closure(a, b, l, p):
    k = len(a)
    U, L = tables(a, b, l, p)
    nonempty = {P for P in U if U[P] + L[P] >= 0}
    full = {P for P in U if U[P] + L[P] + 1 >= p}
    derived = set()
    order = sorted(U, key=lambda P: bin(P).count('1'))
    for P in order:
        if P not in nonempty or P in full:
            continue
        if bin(P).count('1') == 1:
            derived.add(P); continue
        for t in range(k):
            if not (P >> t) & 1:
                continue
            Q = P ^ (1 << t); T = 1 << t
            if Q not in derived or T not in derived:
                continue
            if U[Q] + U[T] + L[P] >= -2 and L[Q] + L[T] + U[P] >= p - 2:
                derived.add(P); break
    bad = [P for P in nonempty if P not in full and P not in derived]
    return bad, len(nonempty), len(full)


if __name__ == '__main__':
    from sample_famtest import inherited
    p = int(sys.argv[1]); T = int(sys.argv[2]); seed = int(sys.argv[3]); kmin = int(sys.argv[4]); kmax = int(sys.argv[5])
    rng = random.Random(seed); N = 4 * p - 2
    stats = Counter(); ex = []
    done = 0
    while done < T:
        k = rng.randint(kmin, kmax)
        cuts = sorted(rng.sample(range(1, N), 2 * k - 1))
        parts = [y - x for x, y in zip([0] + cuts, cuts + [N])]
        r = parts[0::2]; l = parts[1::2]
        a = [rng.randint(0, x) for x in r]; b = [x - y for x, y in zip(r, a)]
        if sum(a) < sum(b):
            a, b = b, a
        if not inherited(a, b, l, p):
            continue
        done += 1
        bad, ne, fu = closure(a, b, l, p)
        if fu:
            stats['has_full'] += 1
        stats['data'] += 1
        stats['bad_patterns'] += len(bad)
        if bad:
            stats['data_with_bad'] += 1
            if len(ex) < 3:
                ex.append((a, b, l, bad[:5]))
    print(dict(stats))
    for e in ex:
        print(e)
