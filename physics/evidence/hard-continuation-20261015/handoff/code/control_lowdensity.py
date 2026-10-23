#!/usr/bin/env python3
"""Satisfiable-region optimisation control (floating EXPLORATION, sanity only).

At alpha=7.9 (k=4) and alpha=18.7 (k=5), below the Achlioptas-Peres
satisfiability lower bounds 7.91 and 18.79, and at alpha=0.95 for k=2
(below the proven 2-SAT threshold 1), the theorem of notes/PROOF.md
implies Psi_T(rho) >= 0 for EVERY trial law rho and every T (otherwise the
formula would be UNSAT whp at a density where it is SAT whp). We therefore
minimise Psi_T over finite laws from many starts and record the minimum found.
A negative value beyond floating noise would indicate a bug in the functional
or the proof. Finding none is weak sanity evidence, not a proof.

Modes per (k, alpha): unconstrained m-atom laws (may collapse toward the
trivial law delta_0, where Psi=0), laws with every atom in [r_floor, 1),
and a warm start from the certified law.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from explore_moments import MomentEvaluator  # noqa: E402


def make_obj(ev, m, alpha, rfloor):
    def unpack(th):
        a, b = th[:m], th[m:]
        s = 1.0 / (1.0 + np.exp(-a))
        rates = rfloor + (1.0 - rfloor) * s
        bb = b - b.max()
        w = np.exp(bb)
        return rates, w / w.sum(), s

    def f(th):
        rates, w, s = unpack(th)
        psi, g_r, g_w = ev.evaluate(list(rates), list(w), alpha, grad=True)
        da = g_r * (1.0 - rfloor) * s * (1 - s)
        db = w * (g_w - float(np.dot(g_w, w)))
        return psi, np.concatenate([da, db])
    return f, unpack


def bfgs(f, th, iters=200):
    val, g = f(th)
    n = len(th)
    Hinv = np.eye(n) * 0.5
    for _ in range(iters):
        p = -Hinv @ g
        if np.dot(p, g) >= 0:
            Hinv = np.eye(n) * 0.5
            p = -Hinv @ g
        step = 1.0
        accepted = False
        while step >= 1e-10:
            th2 = th + step * p
            with np.errstate(all='ignore'):
                v2, g2 = f(th2)
            if np.isfinite(v2) and np.all(np.isfinite(g2)) and v2 <= val + 1e-4 * step * np.dot(g, p):
                accepted = True
                break
            step *= 0.5
        if not accepted:
            break                      # keep the last finite point
        s, yv = th2 - th, g2 - g
        sy = float(np.dot(s, yv))
        th, oldval, val, g = th2, val, v2, g2
        if sy > 1e-30:
            r = 1.0 / sy
            I = np.eye(n)
            Hinv = (I - r * np.outer(s, yv)) @ Hinv @ (I - r * np.outer(yv, s)) + r * np.outer(s, s)
        if abs(oldval - val) < 1e-18 and np.max(np.abs(g)) < 1e-12:
            break
    return th, val


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--T', type=int, default=256)
    ap.add_argument('--starts', type=int, default=6)
    ap.add_argument('--seed', type=int, default=20261015)
    ap.add_argument('--trials', default='certificates/trials.json')
    ap.add_argument('--reference', default='certificates/reference-trials.json')
    ap.add_argument('--cases', default='k4,k5', help='comma list from k2,k4,k5')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    trials = {t['name']: t for t in json.loads(Path(a.trials).read_text())['trials']}
    from fractions import Fraction
    ref = {t['name']: t for t in json.loads(Path(a.reference).read_text())['trials']}
    all_cases = {'k4': (4, 7.9, trials['k4_T512']), 'k5': (5, 18.7, trials['k5_T512']),
                 'k2': (2, 0.95, ref['k2_T128_at_1.1'])}
    cases = [all_cases[c] for c in a.cases.split(',')]
    report = dict(T=a.T, seed=a.seed, starts_per_config=a.starts, note=__doc__.strip().splitlines()[0], cases=[])
    t0 = time.time()
    for k, alpha, cert in cases:
        ev = MomentEvaluator(k, a.T)
        runs = []
        for rfloor in (0.0, 0.05, 0.2):
            for m in (2, 3, 4, 6):
                for s in range(a.starts):
                    th0 = np.concatenate([rng.normal(0.0, 1.5, m), rng.normal(0.0, 1.0, m)])
                    f, unpack = make_obj(ev, m, alpha, rfloor)
                    th, val = bfgs(f, th0)
                    rates, w, _ = unpack(th)
                    runs.append(dict(rfloor=rfloor, m=m, start=s, psi=val,
                                     mean_rate=float(np.dot(rates, w)), max_rate=float(rates.max())))
        # warm start from the certified law (rates unconstrained)
        rates0 = np.array([float(Fraction(x)) for x in cert['rates']])
        w0 = np.array([float(Fraction(x)) for x in cert['weights']])
        m = len(rates0)
        f, unpack = make_obj(ev, m, alpha, 0.0)
        th0 = np.concatenate([np.log(rates0 / (1 - rates0)), np.log(w0)])
        psi0 = f(th0)[0]
        th, val = bfgs(f, th0)
        rates, w, _ = unpack(th)
        warm = dict(start_psi=psi0, psi=val, mean_rate=float(np.dot(rates, w)), max_rate=float(rates.max()))
        summary = {}
        for rfloor in (0.0, 0.05, 0.2):
            vals = [r['psi'] for r in runs if r['rfloor'] == rfloor]
            fin = [v for v in vals if np.isfinite(v)]
            summary[str(rfloor)] = dict(n_runs=len(vals), n_nonfinite=len(vals) - len(fin),
                                        min_psi=min(fin) if fin else None, max_psi=max(fin) if fin else None)
        case = {'k': k, 'alpha': alpha, 'runs': runs, 'warm_start_from_certified_law': warm,
                'summary_by_rate_floor': summary,
                'any_negative_beyond_1e-12': any(r['psi'] < -1e-12 for r in runs) or val < -1e-12}
        report['cases'].append(case)
        print(json.dumps(dict(k=k, alpha=alpha, summary=summary, warm=warm,
                              any_negative=case['any_negative_beyond_1e-12'])), flush=True)
    report['elapsed_seconds'] = round(time.time() - t0, 1)
    Path(a.out).write_text(json.dumps(report, indent=1) + '\n')
    if any(c['any_negative_beyond_1e-12'] for c in report['cases']):
        print('ALARM: a negative Psi_T was found in the satisfiable region', file=sys.stderr)
        sys.exit(1)
    print('NO NEGATIVE Psi_T FOUND in the satisfiable-region search', flush=True)


if __name__ == '__main__':
    main()
