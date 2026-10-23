#!/usr/bin/env python3
"""Aid: for mixed all-odd pure/(1,1) data (no full window), at every interval-chain step (P, t)
test whether the split lemma certifies lift(P+t) = lift(P) + lift(t) [(A'),(B')], and if not,
whether the cocycle decomposition P = Q + s (s adjacent to t) certifies it via the three pairs
(s,t), (Q, s+t), (Q, s).  Phi-independent.  Usage: split_cert.py p trials seed kmin"""
import random, sys
from collections import Counter
from scl_closure import tables


def main():
    p, T, seed, kmin = map(int, sys.argv[1:5])
    rng = random.Random(seed); N = 4 * p - 2
    st = Counter(); done = 0; ex = []
    while done < T:
        k = rng.randint(kmin, 2 * p - 3)
        R = rng.randint(k, 3 * p - 2); F = N - R
        if F < k or (F - k) % 2:
            continue
        H = (F - k) // 2; kappa = p - 1 - H
        if kappa < 2:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
        a = []; b = []
        for x in r:
            u = rng.random()
            if x == 2 and u < 0.15: a.append(1); b.append(1)
            elif u < 0.3: a.append(0); b.append(x)
            else: a.append(x); b.append(0)
        A, B = sum(a), sum(b)
        if A < B: a, b = b, a; A, B = B, A
        if B < 1 or B > kappa or A >= 2 * p:
            continue
        l = [1] * k
        for _ in range(H): l[rng.randrange(k)] += 2
        U, L = tables(a, b, l, p)
        full = (1 << k) - 1
        if any(U[P] + L[P] + 1 >= p for P in range(1, full)):
            continue
        done += 1
        def ok(Q1, Q2):
            Q = Q1 | Q2
            if Q == full: return True
            if U[Q1] + L[Q1] < 0 or U[Q2] + L[Q2] < 0 or U[Q] + L[Q] < 0: return False
            return U[Q1] + U[Q2] + L[Q] >= -2 and L[Q1] + L[Q2] + U[Q] >= p - 2
        for start in range(k):
            for j in range(2, k):
                P = sum(1 << ((start + i) % k) for i in range(j - 1)); t = 1 << ((start + j - 1) % k)
                if ok(P, t):
                    st['direct'] += 1; continue
                s = 1 << ((start + j - 2) % k); Q = P & ~s
                if Q and ok(s, t) and ok(Q, s | t) and ok(Q, s):
                    st['cocycle_left'] += 1; continue
                st['UNCERT'] += 1
                if len(ex) < 4: ex.append((a, b, l, start, j))
    print(dict(st))
    for e in ex: print(e)


if __name__ == '__main__':
    main()
