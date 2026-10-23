#!/usr/bin/env python3
"""Produce small exact controls and direct difference-collision witnesses."""
import json
import math
from pathlib import Path

KNOWN = [2, 8, 24, 90, 512, 134217728, 297474474]


def prime_trial(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p)+1))


def small_prime_factors(x):
    return [r for r in range(2, x+1) if x % r == 0 and prime_trial(r)]


def roots_group(n):
    p, k = n*n+n+1, n+1
    assert prime_trial(p)
    factors = small_prime_factors(k)
    for a in range(2, p):
        g = pow(a, n, p)
        if pow(g, k, p) == 1 and all(pow(g, k//r, p) != 1 for r in factors):
            roots = sorted({pow(g, j, p) for j in range(k)})
            assert len(roots) == k and all(pow(x, k, p) == 1 for x in roots)
            return roots
    raise AssertionError('no subgroup generator')


def direct_result(n):
    p = n*n+n+1
    roots = roots_group(n)
    seen = {}
    for a in roots:
        for b in roots:
            if a == b:
                continue
            d = (a-b) % p
            if d in seen:
                return dict(kind='difference-collision', pair1=list(seen[d]), pair2=[a, b], difference=d)
            seen[d] = (a, b)
    assert len(seen) == p-1
    return dict(kind='planar-direct', D=roots, difference_count=len(seen))


def main():
    rows = []
    for n in KNOWN:
        p = n*n+n+1
        r = pow(2, n+1, p)
        assert r == 1
        if n <= 512:
            result = direct_result(n)
        elif n == 134217728:
            factors = [2593, 71119, 97685839]
            assert math.prod(factors) == p
            result = dict(kind='proper-factor', factor=2593, cofactor=p//2593, factorization=factors)
        else:
            assert n % 24 != 8
            result = dict(kind='necessary-congruence-failure', remainder_mod_8=n % 8,
                          remainder_mod_3=n % 3, remainder_mod_24=n % 24,
                          witness_divisor=n, witness_residue=pow(n, n+1, p))
            assert result['witness_residue'] != 1
        rows.append(dict(n=n, p=str(p), full_base_two_residue=str(r), result=result))
    data = dict(scope='Seven isolated exact controls and their direct classifications; full interval coverage is in the separate C control log.', controls=rows)
    Path('evidence/controls.json').write_text(json.dumps(data, indent=2)+'\n')
    broken = json.loads(json.dumps(data))
    broken['controls'][4]['result']['pair2'][0] += 1
    Path('evidence/controls-broken.json').write_text(json.dumps(broken, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
