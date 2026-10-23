#!/usr/bin/env python3
"""Consistency check of Theorem ELT0 (proof-ELT0-v1.md) against existing classifier outputs (aid, not a premise).
For every HIT line (non-rigid avoiding all-odd k-block datum, word built as in verify_kblock_hits_v1.py, runs
nonempty or not) with kappa = 0 and all runs NONEMPTY (RGR shape), and for every generator g = (1, c), compute the
weights a_x, W, E = W - R and (FULL); ELT0 predicts N + E <= 4p-2 whenever (FULL) holds.  Also reports how many
kappa = 0 RGR-shape hits exist and how many (g, hit) pairs satisfy (FULL).
Usage: check_elt0_v1.py p N FILE [FILE ...]
"""
import json, sys


def full(ws):
    tot = 0
    for a in sorted(ws):
        if a > tot + 1:
            return False
        tot += a
    return True


def main():
    p, N = int(sys.argv[1]), int(sys.argv[2])
    res = {'p': p, 'N': N, 'hits': 0, 'kappa0_rgrshape': 0, 'pairs_full': 0, 'violations': 0, 'max_N_plus_E_full': None}
    for path in sys.argv[3:]:
        for line in open(path):
            if not line.startswith('HIT'):
                continue
            res['hits'] += 1
            parts = dict(t.split('=', 1) for t in line.split()[1:])
            F = int(parts['F'])
            runs = [[int(x) for x in r.split(',')] for r in parts['runs'].split('|')]
            k = len(runs)
            H = (F - k) // 2
            if p - 1 - H != 0 or any(sum(r) == 0 for r in runs):
                continue
            res['kappa0_rgrshape'] += 1
            vals = []
            for r in runs:
                for v in range(p):
                    vals += [v] * r[v]
            R = len(vals)
            for c in range(1, p):
                ws = [next(a for a in range(1, 2 * p, 2) if (a * c - v) % p == 0) for v in vals]
                if full(ws):
                    res['pairs_full'] += 1
                    E = sum(ws) - R
                    m = res['max_N_plus_E_full']
                    res['max_N_plus_E_full'] = N + E if m is None else max(m, N + E)
                    if N + E > 4 * p - 2:
                        res['violations'] += 1
    print(json.dumps(res))


if __name__ == '__main__':
    main()
