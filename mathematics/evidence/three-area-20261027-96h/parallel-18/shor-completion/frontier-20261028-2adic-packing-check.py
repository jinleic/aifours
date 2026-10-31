#!/usr/bin/env python3
"""Check bounded instances of the exact 2-adic Shor-prefix packing argument.

The mathematical proof covers all orders; this program checks its residue
multiplicities, hole bounds and the explicit tiling family over a finite range.
"""
import json
import sys

A = (0, 3, 8, 11)


def valuation2(n):
    k = 0
    while n % 2 == 0:
        k += 1
        n //= 2
    return k


def check(max_n):
    if not 1320 <= max_n <= 10000:
        raise ValueError('require 1320 <= MAX_N <= 10000')
    groups = {1: 0, 2: 0, 3: 0}
    samples = {}
    for n in range(26, max_n + 1):
        k = valuation2(n)
        if not 1 <= k <= 3:
            continue
        d = 1 << k
        residue_counts = [sum(a % d == r for a in A) for r in range(d)]
        if any(c % 2 for c in residue_counts) or (n // d) % 2 != 1:
            raise AssertionError((n, k, residue_counts))
        bound = n - 4 * ((n - d) // 4)
        if bound < d:
            raise AssertionError((n, k, bound))
        groups[k] += 1
        if n in (660, 1320):
            samples[n] = {'v2': k, 'quotient': d, 'class_size': n // d,
                          'row_holes_at_least': d,
                          'new_one_b_atoms_at_least': bound}
    tilings = []
    for n in range(16, max_n + 1, 16):
        J = tuple(16 * k + y for k in range(n // 16) for y in (0, 2, 4, 6))
        sums = [(a + j) % n for a in A for j in J]
        if len(sums) != n or len(set(sums)) != n:
            raise AssertionError(('bad explicit tiling', n))
        tilings.append(n)
    return {'checked_n_range': [26, max_n], 'checked_by_v2': groups,
            'samples': samples, 'explicit_tiling_orders_count': len(tilings),
            'tiling_first_and_last': [tilings[0], tilings[-1]],
            'scope': 'finite validation of residue-count identities and explicit cyclic tilings; no full Shor completion'}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: 2adic-packing-check.py MAX_N')
    print(json.dumps(check(int(sys.argv[1])), indent=2, sort_keys=True))
