"""Exhaustive finite sanity checks of the insertion/comparison identities.

This is a finite check, not the universal proof in notes/PROOF.md.
It enumerates all H:{0,1}^n->{0,1,2} for n=1,2 and four specified
old-site configurations. New clause tuples include repeated indices.
Assertions use exact Fraction arithmetic. Deliberate broken-domain modes
must fail, documenting why integer costs and nonnegative overlaps matter.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
import sys
import time


def log_interval(r):
    assert 0 < r <= 1
    u = (1 - r) / (1 + r)
    t = u
    s = F(0)
    for j in range(32):
        s += 2 * t / (2 * j + 1)
        t *= u * u
    return -s - 2 * t / (65 * (1 - u * u)), -s


def rate_products(arity):
    # Equal-mass rates 1/4 and 3/4, aggregated by the count of 3/4.
    return [(F(3 ** c, 4 ** arity), F(comb(arity, c), 2 ** arity))
            for c in range(arity + 1)]


def check_system(n, base, oldsites, k, stats):
    t = F(1, 2)  # exp(-y) specified exactly
    assignments = list(product((0, 1), repeat=n))
    literals = list(product(range(n), (0, 1)))
    energy_laws = []
    for active in product((0, 1), repeat=len(oldsites)):
        mass = F(1)
        table = list(base)
        for bit, (i, J, p) in zip(active, oldsites):
            mass *= p if bit else 1-p
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
            newmin = min(e+c for e, c in zip(table, costs))
            expected_delta = int(all(frozen[lit] for lit in clause))
            assert newmin - emin == expected_delta
            after += p * t ** newmin
            stats['insertion_checks'] += 1
        terms[after/Z] += clause_weight
    for lit in literals:
        costs = [int(s[lit[0]] == lit[1]) for s in assignments]
        activated = sum((p * t ** min(e+c for e, c in zip(table, costs))
                         for p, table, _, _ in energy_laws), F(0))
        for q, mass in rate_products(k-1):
            after = (1-q)*Z+q*activated
            terms[after/Z] -= k * mass / len(literals)
    for p, mass in rate_products(k):
        terms[1-(1-t)*p] += (k-1)*mass
    upper = F(0)
    for ratio, coefficient in terms.items():
        lo, hi = log_interval(ratio)
        upper += coefficient * (hi if coefficient >= 0 else lo)
    assert upper <= 0, f'comparison fails n={n},k={k},H={base},sites={oldsites}'
    stats['local_comparisons'] += 1


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--break-integer', action='store_true')
    p.add_argument('--break-odd-domain', action='store_true')
    args = p.parse_args()
    if args.break_integer:
        H, penalty = [F(0), F(1,2)], [1, 0]
        delta = min(e+c for e,c in zip(H,penalty))-min(H)
        # This is deliberately false; the checker must reject it.
        assert delta == 1, 'EXPECTED REJECTION: noninteger H gives insertion increment 1/2'
    if args.break_odd_domain:
        B, C, k = -3, 1, 5
        assert B**k-k*B*C**(k-1)+(k-1)*C**k >= 0, 'EXPECTED REJECTION: negative B is outside the odd-k proof domain'
    begin = time.monotonic()
    stats = {'local_comparisons': 0, 'insertion_checks': 0}
    for n in (1, 2):
        systems = [[], [(0,0,F(1,3))],
                   [(0,0,F(1,3)),(0,1,F(2,3))],
                   [(0,0,F(2,5)),(n-1,1,F(3,5))]]
        for base in product((0,1,2), repeat=2**n):
            for oldsites in systems:
                for k in (3,4,5):
                    check_system(n, base, oldsites, k, stats)
    print(f'PASS finite exhaustive check: {stats}; {time.monotonic()-begin:.2f} seconds')
    print('Scope: n=1,2; all integer cost tables in {0,1,2}; four listed old-site configurations; k=3,4,5. No larger range is claimed.')


if __name__ == '__main__':
    try:
        main()
    except AssertionError as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
