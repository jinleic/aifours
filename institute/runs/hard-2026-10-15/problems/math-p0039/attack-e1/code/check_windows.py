#!/usr/bin/env python3
"""Independent checks of the separated-window records, without producer imports.

By default only windows 0 and 99 are fully reexecuted. Specify --all for every
stored window. Manual binary exponentiation is available as a different control
flow from the producing built-in pow call. Checks are exactly scoped in output.
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


def manual_power(exponent, modulus):
    answer, base = 1, 2
    while exponent:
        if exponent & 1:
            answer = answer * base % modulus
        exponent //= 2
        if exponent:
            base = base * base % modulus
    return answer


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('path', nargs='?', default='logs/python-windows.jsonl')
    p.add_argument('--all', action='store_true')
    p.add_argument('--indices', default='0,99')
    p.add_argument('--backend', choices=('pow', 'manual'), default='manual')
    p.add_argument('--output')
    args = p.parse_args()
    rows = [json.loads(s) for s in Path(args.path).read_text().splitlines()]
    want = set(map(int, args.indices.split(',')))
    if args.all:
        want = {r['window'] for r in rows}
    selected = []
    for r in rows:
        if r['window'] in want:
            selected.append(r)
    require({r['window'] for r in selected} == want, 'requested window not present')
    require(len(selected) == len(want), 'duplicate requested window')
    total = 0
    t0 = time.monotonic()
    for r in selected:
        require(0 <= r['window'] < 100 and r['count'] == 1048576 and r['step'] == 24,
                'wrong fixed control-window grid')
        require(r['start'] == 200000000000+24*8388608*512*r['window'],
                'wrong fixed control-window start')
        require(r['step'] > 0 and r['end'] == r['start']+r['step']*r['count'], 'window arithmetic')
        digest = hashlib.sha256()
        hits = []
        for n in range(r['start'], r['end'], r['step']):
            m = n**2+n+1
            residue = pow(2, n+1, m) if args.backend == 'pow' else manual_power(n+1, m)
            decision = 'base2-fail' if residue != 1 else 'needs-exact-elimination'
            digest.update(('%d\t%s\t%d\n' % (n, decision, residue)).encode())
            if residue == 1:
                hits.append(dict(n=n, p=str(m), residue=str(residue)))
        require(digest.hexdigest() == r['sha256_every_n_decision_full_residue'], 'full-residue hash mismatch in window %d' % r['window'])
        require(hits == r['base_two_hits'], 'window survivor mismatch')
        total += r['count']
    result = dict(verified_windows=sorted(want), total_members=total, backend=args.backend,
                  seconds=time.monotonic()-t0,
                  scope='Only the selected windows were independently recomputed; no full production-range certification.')
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        Path(args.output).write_text(text)
    print(text, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, AssertionError, KeyError, IndexError) as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
