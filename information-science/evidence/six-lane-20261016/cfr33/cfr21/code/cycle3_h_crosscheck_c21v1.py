#!/usr/bin/env python3
"""Independent hcount calibration: brute-force permutations, not DLX/orbit options.
Usage: cycle3_h_crosscheck_c21v1.py CALIBDIR OUT.json
Reads hcount-{n}-{mu}-{mode}.out and compares exact h counts at n7/n9.
Also checks all six row-pair permutations of the four-row top submatrix for
every passing h, independently of the derived single-difference reduction.
"""
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys


def main():
    root = Path(sys.argv[1])
    rec = []
    for n, mu, mode in [(7, 1, 'fixed'), (7, 2, 'fixed'), (9, 4, 'fixed'), (9, 4, 'free')]:
        count = 0
        perms = ((0,) + p for p in itertools.permutations(range(1, n))) if mode == 'fixed' else itertools.permutations(range(n))
        for h in perms:
            if mode == 'free' and any(h[x] == x for x in range(n)):
                continue
            if any(h[h[h[x]]] != x for x in range(n)):
                continue
            top = [[0] * n, list(range(n)), [(mu * h[h[x]]) % n for x in range(n)],
                   [(mu * mu * h[x]) % n for x in range(n)]]
            reduced = len({(x - mu * h[h[x]]) % n for x in range(n)}) == n
            direct = all(len({(top[i][x] - top[j][x]) % n for x in range(n)}) == n
                         for i in range(4) for j in range(i))
            if direct != reduced:
                raise AssertionError('top-pair equivalence mismatch')
            count += direct
        log = root / ('hcount-%d-%d-%s.out' % (n, mu, mode))
        data = log.read_bytes()
        matches = re.findall(r'c final .*?hcount (\d+)', data.decode())
        if not matches or int(matches[-1]) != count or b's HCOUNT COMPLETE' not in data:
            raise AssertionError('independent count mismatch %d %d %s: %d' % (n, mu, mode, count))
        rec.append({'n': n, 'mu': mu, 'mode': mode, 'hcount': count, 'c_stdout_sha256': hashlib.sha256(data).hexdigest()})
    with open(sys.argv[2], 'x') as f:
        json.dump({'all_as_expected': True, 'cases': rec}, f, indent=1)
    print('HCOUNT CROSSCHECK PASS', rec)


if __name__ == '__main__':
    main()
