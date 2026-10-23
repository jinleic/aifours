"""EXPLORATION ONLY: optimise m-atom warning laws to locate Psi_T zero crossings.

For fixed (k, m, T) alternate (i) BFGS minimisation of Psi_T over atom
locations/weights at the current density and (ii) a secant solve for the
density where the optimised law has Psi_T = 0. Output is a JSON candidate
record (floating values). Certification is done separately in exact
outward-rounded arithmetic by code/certify_a.py and code/certify_b.py.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from explore_moments import MomentEvaluator, bfgs, pack, unpack  # noqa: E402


def crossing(ev, rates, weights, a0, a1, tol=1e-10):
    f0 = ev.evaluate(rates, weights, a0)[0]
    f1 = ev.evaluate(rates, weights, a1)[0]
    for _ in range(60):
        a2 = a1 - f1 * (a1 - a0) / (f1 - f0)
        f2 = ev.evaluate(rates, weights, a2)[0]
        a0, f0, a1, f1 = a1, f1, a2, f2
        if abs(a1 - a0) < tol:
            break
    return a1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--k', type=int, required=True)
    ap.add_argument('--T', type=int, required=True)
    ap.add_argument('--alpha', type=float, required=True, help='starting density')
    ap.add_argument('--init', required=True, help='JSON file with rates/weights')
    ap.add_argument('--rounds', type=int, default=4)
    ap.add_argument('--iters', type=int, default=300)
    ap.add_argument('--fixed-alpha', action='store_true', help='only minimise at --alpha')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    init = json.loads(Path(a.init).read_text())
    rates, weights = init['rates'], init['weights']
    m = len(rates)
    ev = MomentEvaluator(a.k, a.T)
    th = pack(rates, weights)
    alpha = a.alpha
    hist = []
    t0 = time.time()
    for rd in range(a.rounds):
        th, f, g = bfgs(ev, th, m, alpha, iters=a.iters)
        R, W = unpack(th, m)
        rec = dict(round=rd, alpha=alpha, psi=f, gmax=float(np.max(np.abs(g))),
                   elapsed=round(time.time() - t0, 1))
        if a.fixed_alpha:
            hist.append(rec)
            break
        ac = crossing(ev, list(R), list(W), alpha, alpha - 0.002)
        rec['crossing'] = ac
        hist.append(rec)
        print(json.dumps(rec), flush=True)
        if abs(ac - alpha) < 1e-8:
            break
        alpha = ac
    R, W = unpack(th, m)
    out = dict(k=a.k, T=a.T, m=m, rates=[float(x) for x in R], weights=[float(x) for x in W],
               history=hist, final_alpha=alpha, elapsed=round(time.time() - t0, 1),
               note='floating exploration only; not a certificate')
    Path(a.out).write_text(json.dumps(out, indent=1) + '\n')
    print('done', a.out, alpha, round(time.time() - t0, 1), flush=True)


if __name__ == '__main__':
    main()
