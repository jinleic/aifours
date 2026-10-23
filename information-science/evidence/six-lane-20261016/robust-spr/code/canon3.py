"""Experiment CANON3 (exploratory): test candidate rules "contact kernel + two extra linear
conditions" on realizable fully-closed boxes.  Rules are given as functions returning two rows
(linear forms in b's s-coefficients).  For each box the unique b (up to sign) is tested for
closed feasibility with code/canon.check (both signs).  Also reports, for each box, whether the
closed problem is feasible at all (preconditioned LP margin) so failures are attributable to
the rule, not the box.
"""
from __future__ import annotations

import json
import sys

import numpy as np

from fclosed import contact_matrix, kernel_scaled, residual_rows, lp_margin_precond
from boxsearch import build
from canon import check


def e_row(n, k):
    r = np.zeros(n + 1); r[k] = 1.0
    return r


def E_at(n, t):
    r = np.zeros(n + 1)
    for k in range(0, n + 1, 2):
        r[k] = (-1) ** (k // 2) * t ** (k // 2)
    return r


def O_at(n, t):
    r = np.zeros(n + 1)
    for k in range(1, n + 1, 2):
        r[k] = (-1) ** (k // 2) * t ** (k // 2)
    return r


RULES = {
    'b0=0,bn=0': lambda x, n: [e_row(n, 0), e_row(n, n)],
    'b0=0,E(x1)=0': lambda x, n: [e_row(n, 0), E_at(n, x[1])],
    'bn=0,O(x_last)=0': lambda x, n: [e_row(n, n), O_at(n, x[-1])],
    'E(sqrt(x0x1))=0,O(sqrt(x5x6))=0': lambda x, n: [E_at(n, np.sqrt(x[0] * x[1])),
                                                     O_at(n, np.sqrt(x[-2] * x[-1]))],
    'b0=0,O(x_last)=0': lambda x, n: [e_row(n, 0), O_at(n, x[-1])],
    'bn=0,E(x0)=0': lambda x, n: [e_row(n, n), E_at(n, x[0])],
}


def unique_b(x, n, Em, Ep, Om, Op, extra):
    A = list(contact_matrix(x, n, Em, Ep, Om, Op))
    S = np.sqrt(x[0] * x[-1]); tau = np.sqrt(S)
    D = np.diag(tau ** (-np.arange(n + 1.0)))
    rows = [r / np.abs(r).max() for r in A] + [r / (np.abs(r).max() + 1e-300) for r in extra]
    M = np.array(rows) @ D
    M = M / np.linalg.norm(M, axis=1, keepdims=True)
    u, s, vt = np.linalg.svd(M)
    return D @ vt[-1], s[-1] / s[0]


def main():
    n = int(sys.argv[1]); starts = json.load(open(sys.argv[2]))
    stats = {k: [0, 0] for k in RULES}
    feas_boxes = 0
    for p in starts:
        p = np.array(p)
        if p.size == n + 1:
            p = np.concatenate([p[:n - 1], [p[n] - p[n - 1]]])
        x = np.concatenate([[1.0], 1.0 + np.cumsum(np.exp(p[:n - 1]))])
        la = np.array([1.0, np.exp(p[-1])])
        Em, Ep, Om, Op = build(x, n, la)
        K, sv = kernel_scaled(x, n, Em, Ep, Om, Op)
        R, keys, tv = residual_rows(x, n, Em, Ep, Om, Op, K)
        m, _ = lp_margin_precond(R)
        if m is None or m <= 1e-6:
            continue
        feas_boxes += 1
        for name, rule in RULES.items():
            b, cond = unique_b(x, n, Em, Ep, Om, Op, rule(x, n))
            best = max(min(v[0] for v in check(x, n, Em, Ep, Om, Op, s * b).values())
                       for s in (1, -1))
            stats[name][0] += 1
            stats[name][1] += int(best > -1e-9)
    print('n', n, 'closed-feasible boxes', feas_boxes)
    for k, (tot, ok) in stats.items():
        print(f'  {k:35s} works on {ok}/{tot}')


if __name__ == '__main__':
    main()
