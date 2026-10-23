#!/usr/bin/env python3
"""Independently check exact isolated controls, never importing the producer."""
import json
from math import isqrt
from pathlib import Path
import sys


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'evidence/controls.json'
    data = json.loads(Path(path).read_text())
    controls = data['controls']
    require([r['n'] for r in controls] == [2, 8, 24, 90, 512, 134217728, 297474474], 'wrong isolated control list')
    for row in controls:
        n = row['n']; p = n*n+n+1
        require(int(row['p']) == p, 'wrong p')
        require(int(row['full_base_two_residue']) == pow(2, n+1, p) == 1, 'wrong base-two residue')
        w = row['result']
        if w['kind'] in ('difference-collision', 'planar-direct'):
            # Exhaustive trial division is small here (p<=262657).
            require(all(p % d for d in range(2, isqrt(p)+1)), 'p is not prime')
        if w['kind'] == 'difference-collision':
            ab = tuple(w['pair1']); cd = tuple(w['pair2'])
            require(len(ab) == len(cd) == 2 and ab != cd and ab[0] != ab[1] and cd[0] != cd[1], 'pairs not distinct')
            require(all(0 < x < p and pow(x, n+1, p) == 1 for x in ab+cd), 'collision element not in D')
            require((ab[0]-ab[1]) % p == (cd[0]-cd[1]) % p == w['difference'] != 0, 'false difference collision')
        elif w['kind'] == 'planar-direct':
            D = w['D']
            require(len(set(D)) == len(D) == n+1, 'D size')
            require(all(0 < x < p and pow(x, n+1, p) == 1 for x in D), 'not roots of unity')
            # Count EVERY ordered difference rather than using a collision map.
            counts = [0] * p
            for x in D:
                for y in D:
                    if x != y:
                        counts[(x-y) % p] += 1
            require(counts[0] == 0 and all(c == 1 for c in counts[1:]), 'D is not planar')
            require(w['difference_count'] == p-1, 'wrong difference count')
        elif w['kind'] == 'proper-factor':
            q = w['factor']
            require(1 < q < p and q*w['cofactor'] == p, 'not a proper factor')
            product = 1
            for f in w['factorization']:
                product *= f
            require(product == p, 'wrong factorization')
        elif w['kind'] == 'necessary-congruence-failure':
            d = w['witness_divisor']
            require(d > 0 and n % d == 0, 'not a divisor of n')
            require(w['witness_residue'] == pow(d, n+1, p) != 1, 'no divisor-congruence failure')
            require(w['remainder_mod_8'] == n % 8 != 0, 'no mod-8 failure')
            require(w['remainder_mod_3'] == n % 3 != 2, 'no mod-3 failure')
            require(w['remainder_mod_24'] == n % 24 != 8, 'no mod-24 failure')
        else:
            raise ValueError('unknown control type')
    print('PASS: all seven isolated controls and their exact witnesses; this does not reproduce interval coverage.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, AssertionError, KeyError, IndexError) as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
