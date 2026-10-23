#!/usr/bin/env python3
"""Independent brute-permutation calibration of involution_pair_c21v1's H enumeration.
Usage: involution_h_crosscheck_c21v1.py CALIBDIR OUT.json
No reuse of its orbit options or DLX code. Enumerates permutations fixing0,
requires h^2=id and directly checks all row pairs of [0,id,mu*h].
"""
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys


def main():
    root = Path(sys.argv[1])
    cases = []
    for n, mu in [(7, 1), (7, 6), (9, 1), (9, 8)]:
        count = 0
        for p in itertools.permutations(range(1, n)):
            h = (0,) + p
            if any(h[h[t]] != t for t in range(n)):
                continue
            rows = [[0] * n, list(range(n)), [(mu * h[t]) % n for t in range(n)]]
            direct = all(len({(rows[i][t] - rows[j][t]) % n for t in range(n)}) == n
                         for i in range(3) for j in range(i))
            reduced = len({(t - mu * h[t]) % n for t in range(n)}) == n
            if direct != reduced:
                raise AssertionError('top-pair equivalence')
            count += direct
        data = (root / ('n%d-mu%d-hcount.out' % (n, mu))).read_bytes()
        m = re.findall(r'c final .*?hcount (\d+)', data.decode())
        if not m or int(m[-1]) != count or b's HCOUNT COMPLETE' not in data:
            raise AssertionError('count mismatch n%d mu%d expected%d' % (n, mu, count))
        cases.append({'n': n, 'mu': mu, 'hcount': count, 'stdout_sha256': hashlib.sha256(data).hexdigest()})
    with open(sys.argv[2], 'x') as f:
        json.dump({'all_as_expected': True, 'cases': cases}, f, indent=1)
    print('INVOLUTION HCOUNT CROSSCHECK PASS', cases)


if __name__ == '__main__':
    main()
