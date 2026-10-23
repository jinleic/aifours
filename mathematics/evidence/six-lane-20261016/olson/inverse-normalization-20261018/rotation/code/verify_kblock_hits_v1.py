#!/usr/bin/env python3
"""Independent raw-DP re-verification of 'HIT' lines printed by kblock_exact_v2 (C++), rotation slice 2026-10-18.
Each HIT gives F, the run multiplicity vectors and theta; the word is built with block lengths (F-k+1, 1, ..., 1),
block values y_i = y_(i-1) - theta_i (y_(k-1) = 0), runs in the order run_i then block_i.  The fresh raw DP
(rawdp.has_identity, no window formula) must report NO identity 2p-subword, and the rotation values must be
non-rigid.  Usage: verify_kblock_hits_v1.py p FILE   -> one JSON summary line.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rawdp  # noqa: E402
from sharp_search_v1 import nonrigid  # noqa: E402


def main():
    p, path = int(sys.argv[1]), sys.argv[2]
    n = ok = bad = 0
    examples = []
    for line in open(path):
        if not line.startswith('HIT'):
            continue
        n += 1
        parts = dict(tok.split('=', 1) for tok in line.split()[1:])
        F = int(parts['F'])
        runs = [[int(x) for x in r.split(',')] for r in parts['runs'].split('|')]
        theta = [int(x) for x in parts['theta'].split(',')]
        k = len(runs)
        ls = [F - k + 1] + [1] * (k - 1)
        y, prev = [0] * k, 0
        for i in range(k):
            y[i] = (prev - theta[i]) % p
            prev = y[i]
        w = []
        for i in range(k):
            for v in range(p):
                w += [('r', v)] * runs[i][v]
            w += [('s', y[i])] * ls[i]
        avoid = not rawdp.has_identity(w, p, 2 * p)
        nr = nonrigid(w, p)
        if avoid and nr:
            ok += 1
            if len(examples) < 3:
                examples.append(rawdp.fmt(w))
        else:
            bad += 1
    print(json.dumps({'p': p, 'file': path, 'hits': n, 'dp_confirmed_nonrigid_avoiders': ok, 'failed': bad,
                      'examples': examples}))


if __name__ == '__main__':
    main()
