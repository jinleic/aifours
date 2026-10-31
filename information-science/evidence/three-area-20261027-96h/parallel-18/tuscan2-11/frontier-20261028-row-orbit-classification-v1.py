#!/usr/bin/env python3
"""Mechanical case list for the written row-orbit lemma (n = 11).

For every cycle type of a nontrivial symbol permutation g of order k <= 10 and
every b >= 1 with f = 11 - b*k >= 1 free rows, apply the lemma's necessary
conditions in a fixed order and record which part excludes the case:
  part1  : b <= c_k (block rows start on k-cycles; c_k = 0 means no block);
  part3  : f = 1 is impossible;
  part4  : if all pairs of short-cycle symbols have lcm < k, then b <= c_k - 1;
  part5  : (T2) short-cycle symbols sit in positions 1..9 and pairs with lcm < k
           are at distance >= 3; exact backtracking decides placeability.
This enumerates a written argument's case split; it is not a search for arrays.
Usage: SCRIPT OUTPUT.json
"""
import json
import sys
from math import lcm
from pathlib import Path

N = 11


def partitions(n, largest=None):
    largest = n if largest is None else largest
    if n == 0:
        yield ()
        return
    for part in range(min(n, largest), 0, -1):
        for rest in partitions(n - part, part):
            yield (part,) + rest


def placeable(short_lengths, k):
    m = len(short_lengths)
    clash = [[lcm(short_lengths[i], short_lengths[j]) < k for j in range(m)] for i in range(m)]
    pos = [0] * m

    def rec(i, used):
        if i == m:
            return True
        for p in range(1, N - 1):
            if p not in used and all(not clash[i][j] or abs(p - pos[j]) >= 3 for j in range(i)):
                pos[i] = p
                if rec(i + 1, used | {p}):
                    return True
        return False
    return rec(0, frozenset())


def main(argv):
    if len(argv) != 2:
        raise SystemExit('usage: SCRIPT OUTPUT.json')
    cases = []
    for cycles in partitions(N):
        k = lcm(*cycles)
        if k < 2:
            continue
        ck = cycles.count(k)
        short = [length for length in cycles if length < k for _ in range(length)]
        pair_free = all(lcm(x, y) < k for x in set(short) for y in set(short))
        b = 1
        while b * k <= N - 1:
            f = N - b * k
            if b > ck:
                part = 'part1'
            elif f == 1:
                part = 'part3'
            elif short and pair_free and b > ck - 1:
                part = 'part4'
            elif not placeable(short, k):
                part = 'part5'
            else:
                part = None
            cases.append({'cycles': list(cycles), 'order': k, 'k_cycles': ck, 'b': b, 'free_rows': f,
                          'excluded_by': part})
            b += 1
    remaining = [c for c in cases if c['excluded_by'] is None]
    tally = {}
    for c in cases:
        tally[c['excluded_by'] or 'remaining'] = tally.get(c['excluded_by'] or 'remaining', 0) + 1
    result = {'n': N, 'cases': cases, 'tally': tally, 'remaining': remaining,
              'scope': 'Case split of the written lemma only; remaining cases are open structured subclasses.'}
    with Path(argv[1]).open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'total': len(cases), 'tally': tally,
                      'remaining': [(c['cycles'], c['b']) for c in remaining]}))


if __name__ == '__main__':
    main(sys.argv)
