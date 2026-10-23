#!/usr/bin/env python3
"""Independent permutation audit of v2 H affine representatives and full V sets.
Usage: involution_v2_crosscheck.py CALIBDIR OUT.json
All checks are n7/n9 finite permutations, without using the native DLX/options.
"""
import itertools
import json
from math import gcd
from pathlib import Path
import re
import sys


def perm(values, n):
    return len(set(values)) == n


def main():
    root = Path(sys.argv[1])
    receipts = []
    for n, mu in [(7, 1), (7, 6), (9, 1), (9, 8)]:
        hs = []
        for p in itertools.permutations(range(1, n)):
            h = (0,) + p
            if all(h[h[t]] == t for t in range(n)) and perm([(t - mu * h[t]) % n for t in range(n)], n):
                hs.append(h)
        units = [u for u in range(1, n) if gcd(u, n) == 1]
        representatives = set()
        for h in hs:
            images = []
            for u in units:
                inv = pow(u, -1, n)
                for a in range(n):
                    if h[a] == a:
                        images.append(tuple((u * (h[(inv * t + a) % n] - a)) % n for t in range(n)))
            representatives.add(min(images))
        hlog = (root / ('n%d-mu%d-hcount.out' % (n, mu))).read_text()
        m = re.findall(r'c final .*?hcount (\d+) hcanonical (\d+)', hlog)
        if not m or tuple(map(int, m[-1])) != (len(hs), len(representatives)) or 's HCOUNT COMPLETE' not in hlog:
            raise AssertionError('H count/canonical mismatch')
        # Audit a fixed explicit h: -id for mu1, id for mu=-1.
        h = tuple((-t) % n for t in range(n)) if mu == 1 else tuple(range(n))
        V = set()
        for p in itertools.permutations(range(1, n)):
            g = (0,) + p
            maps = [g, tuple((g[t] - t) % n for t in range(n)),
                    tuple((g[t] - mu * h[t]) % n for t in range(n)),
                    tuple((g[t] - mu * g[h[t]]) % n for t in range(n))]
            if all(perm(x, n) for x in maps):
                twin = tuple((mu * g[h[t]]) % n for t in range(n))
                V.add(min(g, twin))
        audit = (root / ('n%d-mu%d-audit.out' % (n, mu))).read_text()
        native = {tuple(map(int, line.split()[1:])) for line in audit.splitlines() if line.startswith('gv ')}
        if V != native or 's VCOUNT COMPLETE' not in audit:
            raise AssertionError('V set mismatch')
        pairs = sum(perm([(g[t] - j[t]) % n for t in range(n)], n)
                    and perm([(g[t] - mu * j[h[t]]) % n for t in range(n)], n)
                    for g, j in itertools.combinations(V, 2))
        m = re.findall(r'c final .*?vtotal (\d+).*?pairs (\d+)', audit)
        if not m or tuple(map(int, m[-1])) != (len(V), pairs):
            raise AssertionError('V/pair counts mismatch')
        receipts.append({'n': n, 'mu': mu, 'hcount': len(hs), 'affine_h_reps': len(representatives),
                         'V_count': len(V), 'compatible_pairs': pairs})
    with open(sys.argv[2], 'x') as f:
        json.dump({'all_as_expected': True, 'cases': receipts}, f, indent=1)
    print('NESTED DLX CROSSCHECK PASS', receipts)


if __name__ == '__main__':
    main()
