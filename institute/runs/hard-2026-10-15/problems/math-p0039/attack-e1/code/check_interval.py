#!/usr/bin/env python3
"""Recompute a full explicitly specified no-sieve interval, no producer imports.

One chunk is ten million consecutive n=8 (mod 24) members. Every n, decision,
and COMPLETE residue contributes to a SHA-256 digest, compared with a stored
producer result. Manual right-to-left exponentiation differs from built-in
pow's implementation. Both use Python arbitrary-precision integers.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time


def require(ok, message):
    if not ok:
        raise ValueError(message)


def manual_modular_power(exponent, modulus):
    answer = 1
    base = 2
    while exponent:
        if exponent % 2:
            answer = answer * base % modulus
        exponent //= 2
        if exponent:
            base = base * base % modulus
    return answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('chunk', type=int, choices=range(10))
    parser.add_argument('--evidence')
    parser.add_argument('--backend', choices=('pow', 'manual'), default='manual')
    parser.add_argument('--output')
    args = parser.parse_args()
    path = args.evidence or 'evidence/prefix-chunks/%02d.json' % args.chunk
    stored = json.loads(Path(path).read_text())
    start = 200000000000 + 240000000*args.chunk
    stop = start + 240000000
    require((stored['start'], stored['stop'], stored['step'], stored['count']) ==
            (start, stop, 24, 10000000), 'wrong chunk endpoints/count')
    require(stored['base_two_hits'] == [] and stored['unresolved'] == [],
            'stored interval has a base-two hit or unresolved case')
    digest = hashlib.sha256()
    t0 = time.monotonic()
    count = 0
    for n in range(start, stop, 24):
        modulus = n*n+n+1
        residue = pow(2, n+1, modulus) if args.backend == 'pow' else manual_modular_power(n+1, modulus)
        require(residue != 1, 'base-two hit at n='+str(n))
        digest.update(('%d\tbase2-fail\t%d\n' % (n, residue)).encode())
        count += 1
    require(count == stored['count'], 'enumerated count mismatch')
    require(digest.hexdigest() == stored['every_n_decision_full_residue_sha256'],
            'full-interval hash mismatch')
    result = dict(chunk=args.chunk, start=start, stop=stop, step=24, count=count,
                  backend=args.backend, seconds=time.monotonic()-t0,
                  every_n_decision_full_residue_sha256=digest.hexdigest(),
                  scope='Every class member of this chunk only; no exhaustive general-range certification.')
    output = json.dumps(result, indent=2)+'\n'
    if args.output:
        Path(args.output).write_text(output)
    print(output, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, AssertionError) as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
