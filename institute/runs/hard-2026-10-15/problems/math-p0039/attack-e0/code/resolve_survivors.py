#!/usr/bin/env python3
"""Resolve every logged unsieved base-two survivor with exact witnesses only.

Trial proper divisors of p, then test prime divisors of n using Feit's valid
condition. Factorization of n uses exact trial division. No primality or
probable-primality result can eliminate a survivor. Unknown cases remain open.
"""
import argparse
import json
from pathlib import Path


def factor_n(n):
    factors = []
    q = 2
    while q*q <= n:
        if n % q == 0:
            factors.append(q)
            while n % q == 0:
                n //= q
        q = 3 if q == 2 else q+2
    if n > 1:
        factors.append(n)
    return factors


def resolve(n, bound):
    p = n*n+n+1
    assert pow(2, n+1, p) == 1
    for q in range(2, min(bound, p-1)+1):
        if p % q == 0:
            return dict(kind='proper-factor', factor=q, cofactor=str(p//q))
    divisors = factor_n(n)
    for d in divisors:
        residue = pow(d, n+1, p)
        if residue != 1:
            return dict(kind='divisor-power-failure', divisor=d, residue=str(residue))
    return dict(kind='unresolved', note='All prime divisors of n passed the valid necessary condition; no proper factor of p found within the stated trial bound.', prime_divisors_of_n=divisors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('prefix', nargs='?', default='logs/main')
    parser.add_argument('--output', default='evidence/survivors.json')
    parser.add_argument('--factor-bound', type=int, default=1000000)
    args = parser.parse_args()
    rows = [json.loads(s) for s in Path(args.prefix+'.blocks.jsonl').read_text().splitlines()]
    assert rows[0]['kind'] == 'header' and rows[-1]['kind'] == 'footer'
    blocks = sorted((r for r in rows if r['kind'] == 'block'), key=lambda r: r['id'])
    assert [b['id'] for b in blocks] == list(range(len(blocks)))
    survivors = sorted(n for b in blocks for n in b['survivors'])
    assert len(survivors) == len(set(survivors))
    resolved_rows = []
    unresolved = []
    for n in survivors:
        witness = resolve(n, args.factor_bound)
        resolved_rows.append(dict(n=n, p=str(n*n+n+1), witness=witness))
        if witness['kind'] == 'unresolved':
            unresolved.append(n)
    result = dict(start=rows[0]['start'], end=blocks[-1]['end'] if blocks else rows[0]['start'],
                  step=rows[0]['step'], logged_survivor_count=len(survivors),
                  eliminations=resolved_rows, unresolved=unresolved,
                  trial_factor_bound=args.factor_bound,
                  rule='Only explicit proper factors or failures of a proved necessary divisor condition eliminate a survivor. No probable-prime elimination is allowed.')
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if unresolved:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
