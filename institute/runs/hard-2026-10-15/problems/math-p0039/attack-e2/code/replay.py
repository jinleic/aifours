#!/usr/bin/env python3
"""Exact, slow, independent Python reexecution of an explicitly bounded class.

Compute a full pow for EVERY n, including composite moduli, without a sieve.
Only base-two hits require further work: exact trial factors up to B and
divisor congruences. No probable-prime result eliminates a candidate.
This program imports no producing code or evidence-checking code.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time


def resolve(n, p, bound):
    # All trial divisors are sufficient as witnesses; primality of q is unneeded.
    for q in range(2, min(bound, p-1)+1):
        if p % q == 0:
            return dict(kind='proper-factor', divisor=q, cofactor=p//q)
    for d in range(2, min(bound, n)+1):
        if n % d == 0:
            residue = pow(d, n+1, p)
            if residue != 1:
                return dict(kind='divisor-power-failure', divisor=d, residue=str(residue))
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--stop', type=int, required=True)
    parser.add_argument('--step', type=int, default=24)
    parser.add_argument('--factor-bound', type=int, default=1000000)
    parser.add_argument('--output')
    parser.add_argument('--records')
    args = parser.parse_args()
    if args.start < 2 or args.stop <= args.start or args.step <= 0:
        raise ValueError('invalid progression')
    t0 = time.monotonic()
    digest = hashlib.sha256()
    hits = []
    unresolved = []
    record_stream = open(args.records, 'w') if args.records else None
    count = 0
    for n in range(args.start, args.stop, args.step):
        p = n*n+n+1
        residue = pow(2, n+1, p)
        witness = None
        decision = 'base2-fail'
        if residue == 1:
            witness = resolve(n, p, args.factor_bound)
            decision = witness['kind'] if witness else 'unresolved'
            hits.append(dict(n=n, p=str(p), residue=str(residue), witness=witness))
            if witness is None:
                unresolved.append(n)
        line = '%d\t%s\t%d\n' % (n, decision, residue)
        digest.update(line.encode())
        if record_stream:
            record_stream.write(line)
        count += 1
    if record_stream:
        record_stream.close()
    result = dict(start=args.start, stop=args.stop, step=args.step, count=count,
                  base_two_hits=hits, unresolved=unresolved,
                  every_n_decision_full_residue_sha256=digest.hexdigest(),
                  seconds=time.monotonic()-t0,
                  method='Python int pow for EVERY class member; no producing C code imported or executed.')
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        Path(args.output).write_text(text)
    print(text, end='')
    if unresolved:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
