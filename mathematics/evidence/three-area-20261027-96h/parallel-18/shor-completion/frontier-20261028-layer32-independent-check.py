#!/usr/bin/env python3
"""Verify a full-cardinality 2-boundary relaxation and its raw ambiguity."""
from collections import Counter
import hashlib
import json
import sys

OLD = {(0, j) for j in (0, 1, 7, 13, 14)}
OLD |= {(i, j) for i in (3, 8) for j in (0, 2, 4, 6)}
OLD |= {(11, j) for j in (0, 1, 2)}


def validate(n, pairs):
    pairs = [tuple(p) for p in pairs]
    if len(pairs) != n:
        raise ValueError('WRONG_CARDINALITY')
    if len(set(pairs)) != len(pairs):
        raise ValueError('DUPLICATE_PAIR')
    if any(not (0 <= i < n and 0 <= j < n) for i, j in pairs):
        raise ValueError('PAIR_OUT_OF_RANGE')
    if not OLD <= set(pairs):
        raise ValueError('OLD_PAIR_MISSING')
    seen = set()
    seams = Counter()
    for i, j in pairs:
        for k, l in pairs:
            key = (i, (j+k) % n, l)
            if key in seen:
                raise ValueError('TWO_BOUNDARY_COLLISION')
            seen.add(key)
            seams[key[1]] += 1
    if len(seen) != n*n:
        raise ValueError('PATH_COUNT_WRONG')
    return seams


def atom(i, j):
    return 'a'*i + 'b' + 'a'*j


def verify_ambiguity(pairs):
    pairs = set(pairs)
    left = ((11,0), (3,0), (11,0))
    right = ((11,1), (2,3), (8,0))
    if not set(left+right) <= pairs:
        raise ValueError('AMBIGUITY_ATOM_MISSING')
    L = ''.join(atom(*x) for x in left)
    R = ''.join(atom(*x) for x in right)
    if left == right or L != R:
        raise ValueError('AMBIGUITY_NOT_EQUAL')
    return L


def expect_error(n, pairs, expected):
    try:
        validate(n, pairs)
    except ValueError as e:
        if str(e) == expected:
            return expected
        raise
    raise AssertionError(('mutation accepted', expected))


def main(path):
    raw = open(path, 'rb').read()
    data = json.loads(raw)
    if data['n'] != 32:
        raise ValueError('WRONG_ORDER')
    base = [tuple(p) for p in data['pairs']]
    seams = validate(32, base)
    word = verify_ambiguity(base)
    lifts = []
    for m in (1, 2, 3, 5):
        n = 32*m
        pairs = [(i+32*k, j) for i, j in base for k in range(m)]
        counts = validate(n, pairs)
        verify_ambiguity(pairs)
        lifts.append({'n': n, 'pairs': len(pairs), 'two_atom_keys': n*n,
                      'min_seam_count': min(counts.values()), 'max_seam_count': max(counts.values())})
    duplicate = list(base); duplicate[-1] = duplicate[-2]
    missing = [p for p in base if p != (0, 7)] + [(1, 2)]
    collision = list(base); collision[-1] = (0, 3)
    controls = [expect_error(32, duplicate, 'DUPLICATE_PAIR'),
                expect_error(32, missing, 'OLD_PAIR_MISSING'),
                expect_error(32, collision, 'TWO_BOUNDARY_COLLISION')]
    return {'model_sha256': hashlib.sha256(raw).hexdigest(),
            'base_pairs': len(base), 'base_two_atom_keys': 32**2,
            'base_seam_counts': [seams[j] for j in range(32)],
            'raw_ambiguity': word, 'lifts': lifts, 'controls': controls,
            'scope': 'full-cardinality two-boundary relaxation is not full UD or completeness'}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: layer32-independent-check.py MODEL.json')
    print(json.dumps(main(sys.argv[1]), indent=2))
