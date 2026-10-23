#!/usr/bin/env python3
"""Exhaustive finite sanity audit of the insertion identity (C) and comparison (G).

Ported from the epoch-2 snapshot's code/small_models.py (same checks), with
explicit exceptions instead of assert statements and one added rate law.
This is a FINITE check, not the universal proof in notes/PROOF.md.

For n=1,2 it enumerates every integer table H:{0,1}^n->{0,1,2}, four listed
old-site systems, k=3,4,5 and every ordered clause of k literals (repeated
indices included). For each old activation pattern it recomputes the new
minimum by brute force and checks min(H+V)-min H = 1{all old minimisers
violate the clause} (identity (C)). It then forms

    E_new Delta_C Phi - k E_new Delta_S Phi + (k-1) d_y

with exact Fractions for every ratio and rigorous atanh enclosures of each
log, and checks that its rigorous upper bound is <= 0 (inequality before (G)).

Configurations: (rho, t=exp(-y)) in
    {((delta_1/4 + delta_3/4)/2, 1/2),  ((delta_1/5 + delta_1/2 + delta_4/5)/3, 1/3)}.

--break-comparison: first passes a valid witness, then reverses ONLY the
sign of the (k-1) d_y correction inside check_system; the shared
comparison gate must fire (exit 1 with 'comparison fails').
"""
import argparse
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import factorial


class AuditFailure(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise AuditFailure(msg)


def log_interval(r):
    """Rigorous (lo, hi) for log r, 0 < r <= 1, via atanh series + tail."""
    need(0 < r <= 1, f'log argument {r} outside (0,1]')
    u = (1 - r) / (1 + r)
    t = u
    s = F(0)
    for j in range(32):
        s += 2 * t / (2 * j + 1)
        t *= u * u
    return -s - 2 * t / (65 * (1 - u * u)), -s


def product_law(law, arity):
    out = defaultdict(F)
    for combo in combinations_with_replacement(range(len(law)), arity):
        mass = F(factorial(arity))
        val = F(1)
        for idx, c in Counter(combo).items():
            mass = mass * law[idx][1] ** c / factorial(c)
            val *= law[idx][0] ** c
        out[val] += mass
    need(sum(out.values()) == 1, 'product law mass != 1')
    return sorted(out.items())


def check_system(n, base, oldsites, k, law, t, stats, *, break_comparison=False):
    assignments = list(product((0, 1), repeat=n))
    literals = list(product(range(n), (0, 1)))
    energy_laws = []
    for active in product((0, 1), repeat=len(oldsites)):
        mass = F(1)
        table = list(base)
        for bit, (i, J, p) in zip(active, oldsites):
            mass *= p if bit else 1 - p
            if bit:
                table = [e + int(s[i] == J) for e, s in zip(table, assignments)]
        emin = min(table)
        mins = [s for e, s in zip(table, assignments) if e == emin]
        frozen = {(i, J): int(all(s[i] == J for s in mins)) for i, J in literals}
        energy_laws.append((mass, table, emin, frozen))
    Z = sum((p * t ** emin for p, _, emin, _ in energy_laws), F(0))
    terms = defaultdict(F)
    clause_weight = F(1, len(literals) ** k)
    for clause in product(literals, repeat=k):
        costs = [int(all(s[i] == J for i, J in clause)) for s in assignments]
        after = F(0)
        for p, table, emin, frozen in energy_laws:
            newmin = min(e + c for e, c in zip(table, costs))
            expected = int(all(frozen[lit] for lit in clause))
            need(newmin - emin == expected,
                 f'insertion identity fails n={n} H={base} sites={oldsites} clause={clause}')
            after += p * t ** newmin
            stats['insertion_checks'] += 1
        terms[after / Z] += clause_weight
    for lit in literals:
        costs = [int(s[lit[0]] == lit[1]) for s in assignments]
        activated = sum((p * t ** min(e + c for e, c in zip(table, costs))
                         for p, table, _, _ in energy_laws), F(0))
        for q, mass in product_law(law, k - 1):
            after = (1 - q) * Z + q * activated
            terms[after / Z] -= k * mass / len(literals)
    sign = -1 if break_comparison else 1
    for p, mass in product_law(law, k):
        terms[1 - (1 - t) * p] += sign * (k - 1) * mass
    lower = upper = F(0)
    for ratio, coef in terms.items():
        lo, hi = log_interval(ratio)
        upper += coef * (hi if coef >= 0 else lo)
        lower += coef * (lo if coef >= 0 else hi)
    if break_comparison:
        need(lower > 0, 'mutation did not produce a rigorously positive expression')
        print('CONTROL: mutated comparison has a rigorously positive lower bound.', flush=True)
    need(upper <= 0, f'comparison fails n={n},k={k},H={base},sites={oldsites}')
    stats['local_comparisons'] += 1


CONFIGS = [
    ('rho=(d_1/4+d_3/4)/2, t=1/2', [(F(1, 4), F(1, 2)), (F(3, 4), F(1, 2))], F(1, 2)),
    ('rho=(d_1/5+d_1/2+d_4/5)/3, t=1/3', [(F(1, 5), F(1, 3)), (F(1, 2), F(1, 3)), (F(4, 5), F(1, 3))], F(1, 3)),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--break-comparison', action='store_true')
    args = ap.parse_args()
    begin = time.monotonic()
    if args.break_comparison:
        label, law, t = CONFIGS[0]
        witness = (1, (0, 1), [(0, 0, F(1, 3)), (0, 1, F(2, 3))], 5)
        st = defaultdict(int)
        check_system(*witness, law, t, st)
        print('CONTROL: valid witness passed check_system; reversing the d_y correction sign.', flush=True)
        check_system(*witness, law, t, st, break_comparison=True)
        print('CONTROL MISSED: broken comparison was accepted.', flush=True)
        return
    for label, law, t in CONFIGS:
        stats = defaultdict(int)
        for n in (1, 2):
            systems = [[], [(0, 0, F(1, 3))],
                       [(0, 0, F(1, 3)), (0, 1, F(2, 3))],
                       [(0, 0, F(2, 5)), (n - 1, 1, F(3, 5))]]
            for base in product((0, 1, 2), repeat=2 ** n):
                for oldsites in systems:
                    for k in (3, 4, 5):
                        check_system(n, base, oldsites, k, law, t, stats)
        print(f'PASS finite exhaustive check [{label}]: {dict(stats)}', flush=True)
    print(f'Scope: n=1,2; all integer cost tables in {{0,1,2}}; four listed old-site configurations; '
          f'k=3,4,5; the two (rho, t) configurations above. No larger range is claimed. '
          f'{time.monotonic() - begin:.2f} seconds.')


if __name__ == '__main__':
    try:
        main()
    except AuditFailure as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
