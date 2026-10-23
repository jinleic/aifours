#!/usr/bin/env python3
"""Exact constants of the analytic bridge (notes/PROOF.md, Sections 6-7).

Given a trial (k, alpha, epsilon, y, T) whose premises

    (P1) Psi_T <= -epsilon      (certified by certify_a.py / certify_b.py)
    (P2) T exp(-y) <= epsilon/2 (certified by the same programs)

hold, PROOF.md gives, with exact rational arithmetic only:

    E E(F_rep_Poisson(alpha n)) >= c0 n,            c0 = epsilon/(2y), every n >= 1   (B)
    E E(F_dist_M) >= c0 n - sqrt(alpha n) - 1 - alpha binom(k,2),  M = floor(alpha n) (O)
    >= c n,  c = c0/2,  whenever n >= N0 = ceil(max(k, 16 alpha/c0^2, 4(1+alpha binom(k,2))/c0))
    P[F_dist_M satisfiable] <= exp(-2 c^2 n / alpha)   for n >= N0                     (Q)

This script does NOT re-establish P1/P2; it recomputes the constants exactly,
checks the elementary implications used to reach (P) and (Q) at the stated
N0, and prints them. Exit 1 if any implication check fails.
"""
import argparse
import json
import sys
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path


class Fail(Exception):
    pass


def ceil_frac(q):
    return -((-q.numerator) // q.denominator)


def sqrt_upper(q):
    """Smallest integer s with s^2 >= q (q >= 0 rational): ceil(sqrt(q))."""
    n = ceil_frac(q)
    s = isqrt(n)
    return s if s * s >= n else s + 1


def constants(t):
    k = int(t['k'])
    alpha = Fraction(t['alpha'])
    eps = Fraction(t['epsilon'])
    y = Fraction(t['y'])
    c0 = eps / (2 * y)
    c = c0 / 2
    K2 = comb(k, 2)
    a = 16 * alpha / c0 ** 2
    b = 4 * (1 + alpha * K2) / c0
    N0 = max(k, ceil_frac(a), ceil_frac(b))
    # implication checks at n = N0 (both sufficient conditions are monotone in n)
    n = Fraction(N0)
    if not (alpha * n <= (c0 * n / 4) ** 2):
        raise Fail('sqrt(alpha n) <= c0 n/4 fails at N0')
    if not (1 + alpha * K2 <= c0 * n / 4):
        raise Fail('1 + alpha binom(k,2) <= c0 n/4 fails at N0')
    if not (N0 >= k):
        raise Fail('N0 < k')
    rate = 2 * c ** 2 / alpha                    # P[SAT] <= exp(-rate * n)
    inv = 1 / rate
    return dict(name=t.get('name'), k=k, alpha=str(alpha), alpha_decimal=f'{float(alpha):.6f}',
                epsilon=str(eps), y=str(y), T=int(t['T']),
                c0=str(c0), c=str(c), N0=N0, N0_sci=f'{N0:.6e}',
                sat_exponent_rate=str(rate),
                sat_bound=f'P[SAT] <= exp(-n / {inv}) for n >= {N0}' if inv.denominator == 1
                else f'P[SAT] <= exp(-n * {rate}) for n >= {N0}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--trials', default='certificates/trials.json')
    ap.add_argument('--output')
    args = ap.parse_args()
    trials = json.loads(Path(args.trials).read_text())['trials']
    out = [constants(t) for t in trials]
    for r in out:
        print(f"CONSTANTS {r['name']}: k={r['k']} alpha={r['alpha']} ({r['alpha_decimal']}) c0={r['c0']} c={r['c']} "
              f"N0={r['N0']} ; {r['sat_bound']}", flush=True)
    if args.output:
        Path(args.output).write_text(json.dumps({'constants': out}, indent=1) + '\n')


if __name__ == '__main__':
    try:
        main()
    except Fail as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
