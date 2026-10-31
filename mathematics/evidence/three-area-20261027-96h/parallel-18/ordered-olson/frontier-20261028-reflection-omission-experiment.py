#!/usr/bin/env python3
"""Exact finite probe of 2p-of-(2p+1) ordered reflection-only selectors."""

import argparse
import itertools
import json
import random


def direct_product_exponent(values, omitted, p):
    x = parity = 0
    for i, y in enumerate(values):
        if i == omitted:
            continue
        x = (x + y if parity == 0 else x - y) % p
        parity ^= 1
    if parity != 0:
        raise ValueError('selected odd reflection count')
    return x


def moment_vector(values, p):
    return [direct_product_exponent(values, i, p) for i in range(len(values))]


def build_case(values, p):
    moments = moment_vector(values, p)
    return {'p': p, 'reflection_exponents': values, 'omission_products': moments,
            'identity_omissions': [i for i, x in enumerate(moments) if x == 0]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rows = []
    for p in (3,):
        total = impossible = 0
        first = None
        for values in itertools.product(range(p), repeat=2*p+1):
            total += 1
            moments = moment_vector(values, p)
            if 0 not in moments:
                impossible += 1
                if first is None:
                    first = build_case(values, p)
        rows.append({'p': p, 'mode': 'complete', 'tested': total,
                     'no_identity_omission': impossible, 'first_failure': first})
    rng = random.Random(2026102803)
    for p in (5, 7):
        total = impossible = 0
        first = None
        for _ in range(5000):
            values = [rng.randrange(p) for _ in range(2*p+1)]
            total += 1
            moments = moment_vector(values, p)
            if 0 not in moments:
                impossible += 1
                if first is None:
                    first = build_case(values, p)
        rows.append({'p': p, 'mode': 'seeded_sample', 'tested': total,
                     'no_identity_omission': impossible, 'first_failure': first})
    data = {'scope': 'reflection-only selector primitive; NOT a full original-word counterexample',
            'seed': 2026102803, 'domains': rows}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'result': 'COMPLETED_EXACT_FINITE_ASSAYS',
                      'domains': [{key: row[key] for key in ('p', 'mode', 'tested', 'no_identity_omission')}
                                  for row in rows], 'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()
