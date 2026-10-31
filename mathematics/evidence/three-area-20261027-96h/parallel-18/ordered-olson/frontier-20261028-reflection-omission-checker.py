#!/usr/bin/env python3
"""Independently recount saved reflection-omission assay using a prefix recurrence."""

import argparse
import hashlib
import itertools
import json
import random


def omission_values(seq, p):
    signed = [((1 if i % 2 == 0 else -1) * x) % p for i, x in enumerate(seq)]
    value = (-sum(signed[1:])) % p
    result = [value]
    for j in range(len(seq) - 1):
        value = (value + signed[j] + signed[j + 1]) % p
        result.append(value)
    return result


def direct(seq, omitted, p):
    accumulator = 0
    sign = 1
    for i, value in enumerate(seq):
        if i != omitted:
            accumulator = (accumulator + sign * value) % p
            sign = -sign
    if sign != 1:
        raise ValueError('wrong selected reflection parity')
    return accumulator


def verify(seq, p):
    if len(seq) != 2*p+1 or any(x < 0 or x >= p for x in seq):
        raise ValueError('invalid reflection sequence')
    values = omission_values(seq, p)
    if values != [direct(seq, i, p) for i in range(len(seq))]:
        raise ValueError('recurrence disagrees with direct original-order product')
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results')
    args = parser.parse_args()
    raw = open(args.results, 'rb').read()
    data = json.loads(raw)
    if data['seed'] != 2026102803:
        raise ValueError('unexpected seed')
    rng = random.Random(data['seed'])
    checked = 0
    for row in data['domains']:
        p = row['p']
        if row['mode'] == 'complete':
            sequences = itertools.product(range(p), repeat=2*p+1)
        elif row['mode'] == 'seeded_sample':
            sequences = ([rng.randrange(p) for _ in range(2*p+1)] for _ in range(5000))
        else:
            raise ValueError('unknown assay mode')
        total = impossible = 0
        first = None
        for seq in sequences:
            values = verify(seq, p)
            total += 1
            if 0 not in values:
                impossible += 1
                if first is None:
                    first = {'p': p, 'reflection_exponents': list(seq),
                             'omission_products': values, 'identity_omissions': []}
        if total != row['tested'] or impossible != row['no_identity_omission'] or first != row['first_failure']:
            raise ValueError('independent assay count/witness mismatch')
        checked += total
    print(json.dumps({'result': 'PASS_BOUNDED_OMISSION_RECOUNT',
                      'input_sha256': hashlib.sha256(raw).hexdigest(),
                      'actual_sequences_rechecked': checked,
                      'scope': 'finite reflection-only primitive, not original full-word counterexample'}, sort_keys=True))


if __name__ == '__main__':
    main()
