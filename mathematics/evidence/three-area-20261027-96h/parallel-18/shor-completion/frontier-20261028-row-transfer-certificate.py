#!/usr/bin/env python3
"""Verify an all-order max-plus period for Shor one-b row packings.

Independent age-tuple implementation; does not import the earlier bitmask DP.
Only fixed finite vector comparisons and cyclic representative DPs are run.
"""
import json

GAPS = frozenset((3, 5, 8, 11))
WIDTH = 11
ROWS = {'0': frozenset((0, 1, 7, 13, 14)),
        '3/8': frozenset((0, 2, 4, 6)),
        '11': frozenset((0, 1, 2))}
PERIOD_BASE = {'0': 129, '3/8': 29, '11': 69}


def start(required):
    seeds = {x for x in required if x < WIDTH}
    if any(abs(x-y) in GAPS for x in seeds for y in seeds if x != y):
        raise AssertionError('first forced tails collide')
    for pos in set(range(WIDTH)) - seeds:
        if not any(abs(pos-x) in GAPS for x in seeds):
            raise AssertionError(('unaccounted initial tail', pos))
    state = tuple(sorted(WIDTH-x for x in seeds))
    return {state: len(seeds)}, seeds


def advance(vector, allow_zero, allow_one):
    out = {}
    for ages, count in vector.items():
        aged = tuple(x+1 for x in ages if x < WIDTH)
        if allow_zero:
            out[aged] = max(out.get(aged, -1), count)
        if allow_one and not (set(ages) & GAPS):
            with_new = (1,) + aged
            out[with_new] = max(out.get(with_new, -1), count+1)
    if not out:
        raise AssertionError('empty legal state vector')
    return out


def vector_at(required, length):
    vec, seeds = start(required)
    for t in range(WIDTH, length):
        vec = advance(vec, t not in required, True)
    return vec, seeds


def period_check(name, required):
    base = PERIOD_BASE[name]
    left, _ = vector_at(required, base)
    right, _ = vector_at(required, base + 16)
    if left.keys() != right.keys():
        raise AssertionError(('different states', name))
    if any(right[state] != value + 4 for state, value in left.items()):
        raise AssertionError(('non-periodic score', name))
    return {'row': name, 'prefix_length': base, 'states': len(left),
            'length_increment': 16, 'score_increment': 4}


def optimum(n, required):
    # Interior state at prefix length n-11.  Remaining positions are the
    # only ones that can collide cyclically with the forced first 11 bits.
    vec, seeds = vector_at(required, n-WIDTH)
    for i in range(n-WIDTH, n):
        wrap_blocked = any((n - (i-a)) in GAPS for a in seeds)
        vec = advance(vec, i not in required, not wrap_blocked)
    return max(vec.values())


def all_rows(n):
    vals = {name: optimum(n, req) for name, req in ROWS.items()}
    return {'n': n, 'row0': vals['0'], 'rows3_and8': vals['3/8'], 'row11': vals['11'],
            'outside_min': n-vals['0']-2*vals['3/8']-vals['11']}


def main():
    periods = [period_check(name, req) for name, req in ROWS.items()]
    representatives = [all_rows(n) for n in range(140, 156)]
    expected = [6,8,5,8,2,6,5,5,6,8,7,8,10,10,7,11]
    if [x['outside_min'] for x in representatives] != expected:
        raise AssertionError('representative bounds changed')
    directly_checked = [all_rows(n) for n in (660, 1320, 2640)]
    for result in directly_checked:
        n = result['n']
        rep = next(x for x in representatives if x['n'] % 16 == n % 16)
        increments = (n - rep['n']) // 16
        for key in ('row0', 'rows3_and8', 'row11'):
            if result[key] != rep[key] + 4*increments:
                raise AssertionError(('period extrapolation mismatch', n, key))
        if result['outside_min'] != rep['outside_min']:
            raise AssertionError(('outside bound mismatch', n))
    return {'period_certificates': periods, 'representatives': representatives,
            'direct_checks': directly_checked,
            'scope': 'exact finite-state parity/period checks, not a complete-code witness'}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
