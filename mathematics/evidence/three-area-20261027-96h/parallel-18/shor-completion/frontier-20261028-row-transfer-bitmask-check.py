#!/usr/bin/env python3
"""Independent bitmask verification of Shor-row max-plus periodicity."""
import json

D = (3, 5, 8, 11)
W = 11
LIMIT = (1 << W) - 1
DATA = {'0': ({0, 1, 7, 13, 14}, 129),
        '3/8': ({0, 2, 4, 6}, 29),
        '11': ({0, 1, 2}, 69)}


def initial(required):
    forced = {i for i in required if i < W}
    vec = {}
    for mask in range(1 << W):
        positions = {i for i in range(W) if mask & (1 << (W-1-i))}
        if not forced <= positions:
            continue
        if any(j-i in D for i in positions for j in positions if j > i):
            continue
        vec[mask] = len(positions)
    if len(vec) != 1:
        raise AssertionError(('unexpected initial states', required, len(vec)))
    return vec, forced


def advance(vec, must_select=False, cannot_select=False):
    out = {}
    for mask, value in vec.items():
        if not must_select:
            new = (mask << 1) & LIMIT
            if value > out.get(new, -1):
                out[new] = value
        if not cannot_select and not any(mask & (1 << (d-1)) for d in D):
            new = ((mask << 1) | 1) & LIMIT
            if value+1 > out.get(new, -1):
                out[new] = value+1
    if not out:
        raise AssertionError('no state')
    return out


def vector(required, length):
    vec, forced = initial(required)
    for pos in range(W, length):
        vec = advance(vec, must_select=pos in required)
    return vec, forced


def confirm_period(left, right):
    if set(left) != set(right):
        raise ValueError('STATE_SET_MISMATCH')
    if any(right[s] != v+4 for s, v in left.items()):
        raise ValueError('SCORE_SHIFT_MISMATCH')


def optimum(n, required):
    vec, forced = vector(required, n-W)
    for pos in range(n-W, n):
        wrap = any(n-(pos-a) in D for a in forced)
        vec = advance(vec, must_select=pos in required, cannot_select=wrap)
    return max(vec.values())


def row_summary(n):
    values = {name: optimum(n, req) for name, (req, _) in DATA.items()}
    return [values['0'], values['3/8'], values['11'],
            n-values['0']-2*values['3/8']-values['11']]


def main():
    certificates = {}
    for name, (required, base) in DATA.items():
        left, _ = vector(required, base)
        right, _ = vector(required, base+16)
        confirm_period(left, right)
        altered = dict(right)
        s = next(iter(altered))
        altered[s] += 1
        try:
            confirm_period(left, altered)
        except ValueError as e:
            if str(e) != 'SCORE_SHIFT_MISMATCH':
                raise
        else:
            raise AssertionError('score mutation not rejected')
        altered = dict(right)
        del altered[s]
        try:
            confirm_period(left, altered)
        except ValueError as e:
            if str(e) != 'STATE_SET_MISMATCH':
                raise
        else:
            raise AssertionError('state mutation not rejected')
        certificates[name] = {'prefix': base, 'states': len(left),
                              'score_and_state_mutations_rejected': True}
    reps = {n: row_summary(n) for n in range(140, 156)}
    direct = {n: row_summary(n) for n in (660, 1320, 2640)}
    for n, actual in direct.items():
        r = next(t for t in reps if t % 16 == n % 16)
        t = (n-r)//16
        if actual[:3] != [v+4*t for v in reps[r][:3]] or actual[3] != reps[r][3]:
            raise AssertionError(('incorrect extrapolation', n))
    return {'certificates': certificates, 'representatives': reps, 'direct': direct,
            'scope': 'finite-state proof checks; row relaxation only'}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
