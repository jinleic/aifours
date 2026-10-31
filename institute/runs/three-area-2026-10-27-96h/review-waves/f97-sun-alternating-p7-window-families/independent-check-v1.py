#!/usr/bin/env python3
"""Independent integer-only checks for f97; no source or subgroup enumeration."""
from itertools import combinations, product
from math import comb, factorial, gcd, isqrt, lcm
import json


def prime(n):
    return n >= 2 and all(n % p for p in range(2, isqrt(n) + 1))


def prime_power(n):
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
    return True


def eligible(r):
    if not prime(r) or r < 419:
        return False
    # d=2 forces q=r-1; d>=3 forces q^2 < r.
    if prime_power(r - 1):
        return False
    for q in range(2, isqrt(r) + 1):
        if not prime_power(q):
            continue
        term, total = q*q, 1 + q + q*q
        while total <= r:
            if total == r:
                return False
            term *= q
            total += term
    return True


def four_type_check(r):
    per_subset = {}
    for types in combinations(range(1, 6), 4):
        count = 0
        for choices in product(*(range(1, j + 1) for j in types)):
            minima = [lcm(7, comb(r+j, u)) for j, u in zip(types, choices)]
            assert any(gcd(a, b) > 7 for a, b in combinations(minima, 2))
            count += 1
        per_subset[''.join(map(str, types))] = count
    assert sum(per_subset.values()) == 274
    return per_subset


def window_check(r, t):
    # Enumerate disjoint intervals by choosing each next start after the last end.
    # No recurrence or checker from the candidate is imported or executed.
    F = {h: (r+h)//gcd(r+h, factorial(t)) for h in range(1, t+1)}
    for a in range(1, t+1):
        for b in range(a, t+1):
            value = comb(r+b, b-a+1)
            assert all(value % F[h] == 0 for h in range(a, b+1))
    if r+1 > 7*factorial(t):
        assert min(F.values()) > 7
    out = {'visited': 0, 'max_even_only': 0, 'max_even_and_3': 0,
           'max_pair_gcd7': 0, 'saturated_even_only': 0,
           'all_saturated_tags_full_factors': True, 'min_overlap_divisor': min(F.values()),
           'large_size_hypothesis': r+1 > 7*factorial(t)}
    chosen = []

    def visit(next_start, even_count, three_count, exact):
        out['visited'] += 1
        size = len(chosen)
        out['max_even_only'] = max(out['max_even_only'], size)
        if three_count <= 1:
            out['max_even_and_3'] = max(out['max_even_and_3'], size)
        if exact:
            out['max_pair_gcd7'] = max(out['max_pair_gcd7'], size)
        if size == 6 and t in (10, 11):
            out['saturated_even_only'] += 1
            tags = {}
            for a, b, v in chosen:
                if b % 2 == 0:
                    k = b
                elif v % 2:
                    k = b - 1
                else:
                    continue
                if k in tags:
                    out['all_saturated_tags_full_factors'] = False
                tags[k] = v
            if set(tags) != {2, 4, 6, 8, 10}:
                out['all_saturated_tags_full_factors'] = False
            if any(v % (r+k) for k, v in tags.items()):
                out['all_saturated_tags_full_factors'] = False
        for a in range(next_start, t+1):
            for b in range(a, t+1):
                v = comb(r+b, b-a+1)
                e, z = int(v % 2 == 0), int(v % 3 == 0)
                if even_count + e > 1:
                    continue
                minimal = lcm(7, v)
                next_exact = exact and all(gcd(minimal, lcm(7, w)) == 7
                                           for _, _, w in chosen)
                chosen.append((a, b, v))
                visit(b+1, even_count+e, three_count+z, next_exact)
                chosen.pop()

    visit(1, 0, 0, True)
    assert out['max_even_only'] <= t//2 + 1
    if t in (10, 11):
        assert out['all_saturated_tags_full_factors']
        assert out['max_even_and_3'] <= 5
    return out


# The old 7*a control can spuriously report a collision.
assert gcd(7*7, 7*14) > 7 and gcd(lcm(7,7), lcm(7,14)) == 7
assert prime(65537) and prime_power(65536) and not eligible(65537)
assert prime(8191) and not prime_power(8190) and not eligible(8191)
assert not prime_power(20) and 1+20+20**2 == 421
main_r = (419, 421, 431, 1000000007)
extra_r = (2540173, 279417613)
result = {'note': 'Integer checks only: no subgroup enumeration or imported source proof.',
          'old_checker_counterexample_a_b': [7, 14], 'cases': {}}
for r in main_r + extra_r:
    assert eligible(r)
    case = {'prime_and_eligible': True, 'd1_to_d7': [], 'windows': {}}
    for j in range(1, 12):
        dj = (r+j)//gcd(r+j, lcm(*range(1, j+1)))
        assert all(comb(r+j, u) % dj == 0 for u in range(1, j+1))
        if j <= 7:
            case['d1_to_d7'].append(dj)
    if r in main_r:
        assert case['d1_to_d7'][6] > 7
        case['four_type_counts'] = four_type_check(r)
        ts = (7, 9, 10, 11)
    else:
        ts = (9,) if r == 2540173 else (10, 11)
    for t in ts:
        case['windows'][str(t)] = window_check(r, t)
    result['cases'][str(r)] = case
print(json.dumps(result, indent=2, sort_keys=True))
