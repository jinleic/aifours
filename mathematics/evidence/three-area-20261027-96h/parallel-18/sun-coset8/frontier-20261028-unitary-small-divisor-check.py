#!/usr/bin/env python3
"""All-divisor compatibility graphs for PSU(3,3) and PSU(3,5).

A Sun8 counterconfiguration needs eight DISTINCT subgroup indices >=8 with
pairwise gcd in [2,7].  This is a necessary arithmetic test, not group search.
"""
from math import gcd, isqrt


def divisors(n):
    lo, hi = [], []
    for d in range(1, isqrt(n)+1):
        if n % d == 0:
            lo.append(d)
            if d*d != n:
                hi.append(n//d)
    return lo + hi[::-1]


def max_clique(values):
    adj = [0] * len(values)
    for i, x in enumerate(values):
        for j in range(i):
            if 2 <= gcd(x, values[j]) <= 7:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    best, nodes = [], 0

    def color(mask):
        order, bounds = [], []
        k = 0
        while mask:
            k += 1
            available = mask
            while available:
                low = available & -available
                i = low.bit_length()-1
                order.append(i)
                bounds.append(k)
                mask &= ~low
                available &= ~low
                available &= ~adj[i]
        return order, bounds

    def visit(selected, candidates):
        nonlocal best, nodes
        nodes += 1
        if len(selected) > len(best):
            best = selected
        order, bounds = color(candidates)
        for j in range(len(order)-1, -1, -1):
            if len(selected) + bounds[j] <= len(best):
                return
            i = order[j]
            visit(selected + [i], candidates & adj[i])
            candidates &= ~(1 << i)

    visit([], (1 << len(values))-1)
    return [values[i] for i in best], nodes


def main():
    for q in (3, 5):
        n = q**3*(q**3+1)*(q*q-1)//gcd(3, q+1)
        values = [d for d in divisors(n) if d >= 8]
        clique, nodes = max_clique(values)
        print(f"q={q}, group_order={n}, candidate_divisors={len(values)}, "
              f"max_compatibility_clique={len(clique)}, search_nodes={nodes}")
        print("one_max_clique:", sorted(clique))
        if len(clique) >= 8:
            raise SystemExit("UNRESOLVED: arithmetic 8-clique exists")
    print("PASS: neither divisor graph admits eight indices")


if __name__ == "__main__":
    main()
