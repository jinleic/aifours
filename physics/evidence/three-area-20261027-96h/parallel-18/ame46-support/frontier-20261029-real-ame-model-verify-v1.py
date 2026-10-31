#!/usr/bin/env python3
"""Exact verifier for models of frontier-20261029-real-zero-excess-cnf-v1.py.

Decodes E (e_w = 1+id), P (p_w = 1297+id) and E signs (t_w = 2593+id), builds the
unnormalized real tensor F = sqrt(72) psi with entries -1/+1 on E and sqrt2 on P,
represented exactly in Z[sqrt2], and checks F F^T = 2 I_36 for all three 2|2 cuts.
For psi = F/sqrt72 this is exactly: every two-party marginal equals I_36/36, i.e.
psi is AME(4,6).  Independent of the CNF encoding; reads only the model words.
"""
import argparse
from collections import defaultdict
import hashlib
import itertools
import json
from pathlib import Path

CUTS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
WORDS = list(itertools.product(range(6), repeat=4))


def decode(path):
    true = set()
    for line in path.read_text().splitlines():
        if line.startswith('v '):
            true.update(int(t) for t in line[2:].split() if int(t) > 0)
    E = {w for k, w in enumerate(WORDS) if 1 + k in true}
    P = {w for k, w in enumerate(WORDS) if 1297 + k in true}
    T = {w for k, w in enumerate(WORDS) if 2593 + k in true}
    return E, P, T


def gram_ok(coef):
    report = []
    for rows, cols in CUTS:
        F = defaultdict(dict)
        for w, v in coef.items():
            F[(w[rows[0]], w[rows[1]])][(w[cols[0]], w[cols[1]])] = v
        keys = list(itertools.product(range(6), repeat=2))
        bad = 0
        for r1 in keys:
            for r2 in keys:
                a = b = 0
                for c, (x0, x1) in F[r1].items():
                    if c in F[r2]:
                        y0, y1 = F[r2][c]
                        a += x0 * y0 + 2 * x1 * y1
                        b += x0 * y1 + x1 * y0
                if (a, b) != ((2 if r1 == r2 else 0), 0):
                    bad += 1
        report.append(bad)
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('model', type=Path)
    ap.add_argument('out', type=Path)
    a = ap.parse_args()
    if a.out.exists():
        raise SystemExit('refusing to overwrite')
    E, P, T = decode(a.model)
    coef = {w: ((-1 if w in T else 1), 0) for w in E}
    if E & P:
        raise SystemExit('E and P overlap')
    coef.update({w: (0, 1) for w in P})
    bad = gram_ok(coef)
    res = {'model_sha256': hashlib.sha256(a.model.read_bytes()).hexdigest(),
           'support': len(coef), 'E_plus1': len(E - T), 'E_minus1': len(E & T), 'P_sqrt2': len(P),
           'gram_entry_failures_by_cut': bad, 'is_AME': bad == [0, 0, 0],
           'tensor_sqrt72_times_psi': {'plus1': sorted(E - T), 'minus1': sorted(E & T), 'sqrt2': sorted(P)}}
    with a.out.open('x') as f:
        f.write(json.dumps(res, indent=1) + '\n')
    print(json.dumps({k: v for k, v in res.items() if k != 'tensor_sqrt72_times_psi'}))


if __name__ == '__main__':
    main()
