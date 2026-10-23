#!/usr/bin/env python3
"""Aid (phi-independent): for MIX_DEF data without full windows, test the interval induction for IL:
every proper interval Q with |Q| >= 2 must have SOME cut Q = Q1 + Q2 (two consecutive sub-intervals)
satisfying (B') L_Q1 + L_Q2 + U_Q >= p-2, and SOME cut satisfying (A') U_Q1 + U_Q2 + L_Q >= -2.
If both hold for every Q, IL follows by induction on |Q| (no -p / +p jump can occur at Q).
Usage: anycut.py p trials seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scl_closure import tables


def main():
    p, T, seed = map(int, sys.argv[1:4]); N = 4 * p - 2
    rng = random.Random(seed); st = Counter(); done = 0; ex = []
    while done < T:
        k = rng.randint(3, 2 * p - 3); R = rng.randint(k, 3 * p - 2); F = N - R
        if F < k or (F - k) % 2:
            continue
        H = (F - k) // 2; kappa = p - 1 - H
        if kappa < 2:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
        a, b = [], []
        for x in r:
            u = rng.random()
            if x == 2 and u < 0.15: a.append(1); b.append(1)
            elif u < 0.35: a.append(0); b.append(x)
            else: a.append(x); b.append(0)
        A, B = sum(a), sum(b)
        if B < 1 or B >= kappa or A < B or A >= 2 * p:
            continue
        l = [1] * k
        for _ in range(H): l[rng.randrange(k)] += 2
        U, L = tables(a, b, l, p); full = (1 << k) - 1
        if any(U[P] + L[P] + 1 >= p for P in range(1, full)):
            continue
        done += 1
        for i in range(k):
            for ln in range(2, k):
                Q = sum(1 << ((i + j) % k) for j in range(ln))
                okB = okA = False
                for c_ in range(1, ln):
                    Q1 = sum(1 << ((i + j) % k) for j in range(c_)); Q2 = Q & ~Q1
                    if L[Q1] + L[Q2] + U[Q] >= p - 2: okB = True
                    if U[Q1] + U[Q2] + L[Q] >= -2: okA = True
                st['Q'] += 1
                if not okB: st['noB_cut'] += 1
                if not okA: st['noA_cut'] += 1
                if (not okA or not okB) and len(ex) < 4: ex.append((a, b, l, i, ln, okA, okB))
    print(dict(st))
    for e in ex: print(e)


if __name__ == '__main__':
    main()
