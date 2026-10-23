#!/usr/bin/env python3
"""Independently check that every logged survivor has an exact elimination."""
import argparse
import json
from pathlib import Path
import sys


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('path', nargs='?', default='evidence/survivors.json')
    p.add_argument('--prefix', default='logs/main')
    args = p.parse_args()
    result = json.loads(Path(args.path).read_text())
    log = [json.loads(s) for s in Path(args.prefix+'.blocks.jsonl').read_text().splitlines()]
    need(log[0]['kind'] == 'header' and log[-1]['kind'] == 'footer', 'incomplete log')
    blocks = sorted((b for b in log if b['kind'] == 'block'), key=lambda b: b['id'])
    need([b['id'] for b in blocks] == list(range(len(blocks))), 'block gap')
    expected = sorted(n for b in blocks for n in b['survivors'])
    need(result['start'] == log[0]['start'] and result['end'] == blocks[-1]['end'], 'table interval')
    need(result['step'] == log[0]['step'], 'table class')
    need(result['logged_survivor_count'] == len(expected), 'table survivor count')
    need([r['n'] for r in result['eliminations']] == expected, 'missing or extra survivor')
    unresolved = []
    for r in result['eliminations']:
        n = r['n']; m = n*n+n+1; w = r['witness']
        need(int(r['p']) == m and pow(2, n+1, m) == 1, 'not a genuine base-two survivor')
        if w['kind'] == 'proper-factor':
            q = w['factor']
            need(1 < q < m and q*int(w['cofactor']) == m, 'invalid proper factor')
        elif w['kind'] == 'divisor-power-failure':
            d = w['divisor']
            need(d > 0 and n % d == 0, 'witness is not a divisor')
            need(int(w['residue']) == pow(d, n+1, m) != 1, 'invalid congruence failure')
        elif w['kind'] == 'unresolved':
            unresolved.append(n)
        else:
            raise ValueError('unsupported or probabilistic elimination reason')
    need(unresolved == result['unresolved'], 'unresolved list mismatch')
    need(not unresolved, 'unresolved survivors prevent exclusion')
    print('PASS: %d logged survivors, all exactly eliminated; no unresolved cases.' % len(expected))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, AssertionError, KeyError, IndexError) as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
