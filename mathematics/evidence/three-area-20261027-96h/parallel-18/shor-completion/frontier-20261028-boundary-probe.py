#!/usr/bin/env python3
"""Bounded exact UD and two-boundary probes for the literal Shor code.

No negative result decides finite completion.  The Sardinas-Patterson search
stores actual word lists witnessing every residual, and emits equal raw words
only after checking the two concatenations.  No third-party packages required.
"""
from collections import deque
import json
import sys

OLD_PAIRS = ((0, 0), (0, 1), (0, 7), (0, 13), (0, 14),
             (3, 0), (3, 2), (3, 4), (3, 6),
             (8, 0), (8, 2), (8, 4), (8, 6),
             (11, 0), (11, 1), (11, 2))


def atom(i, j):
    return b'a' * i + b'b' + b'a' * j


def short_name(word):
    if b'b' not in word:
        return 'a^' + str(len(word))
    i = word.index(b'b')
    if word.count(b'b') == 1:
        return 'a^%db a^%d' % (i, len(word) - i - 1)
    return word.decode('ascii')


def sp_certificate(code):
    """Return None iff UD; else two distinct lists whose concatenations agree."""
    words = tuple(sorted(set(code)))
    if b'' in words:
        return ((), (b'',))
    seen = set()
    queue = deque()

    def add(residual, longer, shorter):
        if residual not in seen:
            seen.add(residual)
            queue.append((residual, longer, shorter))

    for x in words:
        for y in words:
            if len(x) > len(y) and x.startswith(y):
                add(x[len(y):], (x,), (y,))
    while queue:
        suffix, longer, shorter = queue.popleft()
        for word in words:
            if suffix == word:
                result = (longer, shorter + (word,))
                if result[0] == result[1] or b''.join(result[0]) != b''.join(result[1]):
                    raise AssertionError('invalid SP witness')
                return result
            if suffix.startswith(word):
                add(suffix[len(word):], longer, shorter + (word,))
            elif word.startswith(suffix):
                add(word[len(suffix):], shorter + (word,), longer)
    return None


def two_boundary_collision(pairs, n):
    """A collision is two different 2-atom lists with equal residues."""
    seen = {}
    for e1 in pairs:
        for e2 in pairs:
            key = (e1[0] % n, (e1[1] + e2[0]) % n, e2[1] % n)
            if key in seen and seen[key] != (e1, e2):
                return (seen[key], (e1, e2), key)
            seen[key] = (e1, e2)
    return None


def ambiguity_json(certificate):
    if certificate is None:
        return None
    left, right = certificate
    return {'left': [short_name(w) for w in left],
            'right': [short_name(w) for w in right],
            'raw_word': b''.join(left).decode('ascii'),
            'atom_count': [len(left), len(right)]}


def scan(n, cap, max_examples=8):
    base = tuple(atom(i, j) for i, j in OLD_PAIRS) + (b'a' * n,)
    if len(set(base)) != len(OLD_PAIRS) + 1:
        raise AssertionError('unexpected duplicate base word')
    base_sp = sp_certificate(base)
    base_two = two_boundary_collision(OLD_PAIRS, n)
    result = {'n': n, 'grid': {'i': [0, cap], 'j': [0, cap]},
              'old_pairs_count': len(OLD_PAIRS),
              'base_ud': base_sp is None,
              'base_ambiguity': ambiguity_json(base_sp),
              'base_two_boundary_collision': base_two,
              'tried': 0, 'two_collision': 0, 'two_clear_sp_reject': 0,
              'sp_ud': 0, 'examples_two_clear_sp_reject': []}
    if base_sp is not None or base_two is not None:
        return result
    for i in range(cap + 1):
        for j in range(cap + 1):
            if (i, j) in OLD_PAIRS:
                continue
            result['tried'] += 1
            pairs = OLD_PAIRS + ((i, j),)
            if two_boundary_collision(pairs, n) is not None:
                result['two_collision'] += 1
                continue
            cert = sp_certificate(base + (atom(i, j),))
            if cert is None:
                result['sp_ud'] += 1
            else:
                result['two_clear_sp_reject'] += 1
                if len(result['examples_two_clear_sp_reject']) < max_examples:
                    result['examples_two_clear_sp_reject'].append({
                        'candidate_pair': [i, j], 'ambiguity': ambiguity_json(cert)})
    return result


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: boundary-probe.py PURE_A_EXPONENT GRID_MAX')
    n, cap = map(int, sys.argv[1:])
    if n <= 0 or not 0 <= cap <= 40:
        raise SystemExit('require n>0 and 0<=GRID_MAX<=40')
    print(json.dumps(scan(n, cap), sort_keys=True, indent=2))
