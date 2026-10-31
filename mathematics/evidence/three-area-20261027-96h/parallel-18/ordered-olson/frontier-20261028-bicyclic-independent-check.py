#!/usr/bin/env python3
"""Bounded exact check of the infinite bicyclic-to-shift host formulas.

This independent implementation does not truncate products and does not
import the author's program. Finite checks do not prove the infinite theorem.
"""

import argparse
import itertools
import json


def multiply(a, b):
    i, j = a
    k, ell = b
    return i + max(0, k-j), ell + max(0, j-k)


def host_multiply(a, b):
    tail_a, grade_a = a
    tail_b, grade_b = b
    return max(tail_a, grade_a + tail_b), grade_a + grade_b


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    labels = list(itertools.product(range(5), repeat=2))
    shifts = list(range(-3, 4))
    identity = (0, 0)
    for a in labels:
        if multiply(identity, a) != a or multiply(a, identity) != a:
            raise ValueError('unit violation')
        inv = (a[1], a[0])
        if multiply(multiply(a, inv), a) != a or multiply(multiply(inv, a), inv) != inv:
            raise ValueError('mutual inverse violation')
        if (a[0] == a[1]) != (multiply(a, a) == a):
            raise ValueError('idempotent characterization mismatch')
    for a, b, c in itertools.product(labels, repeat=3):
        if multiply(multiply(a, b), c) != multiply(a, multiply(b, c)):
            raise ValueError('associativity violation')
    wrong_direction = 0
    for a, b in itertools.product(labels, repeat=2):
        q_a = a[0] - a[1]
        q_b = b[0] - b[1]
        ab = multiply(a, b)
        if ab[0] - ab[1] != q_a + q_b:
            raise ValueError('grade homomorphism violation')
        if host_multiply((a[0], q_a), (b[0], q_b)) != (ab[0], ab[0]-ab[1]):
            raise ValueError('host multiplicativity violation')
        for shift in shifts:
            lhs = max(shift+a[0], shift+q_a+b[0])
            rhs = shift+ab[0]
            if lhs != rhs:
                raise ValueError('canonical relation violation')
            wrong = max(shift+a[0], shift-q_a+b[0])
            wrong_direction += int(wrong != rhs)
    if not wrong_direction:
        raise ValueError('wrong shift-direction control not detected')
    host_images = [(i, i-j) for i, j in labels]
    if len(set(host_images)) != len(labels):
        raise ValueError('host injection violation')
    p, q = (0, 1), (1, 0)
    if multiply(p, q) != identity or multiply(q, p) != (1, 1):
        raise ValueError('bicyclic distinguished products mismatch')
    result = {'result': 'PASS_BOUNDED_INDEPENDENT_BICYCLIC_CHECK',
              'source_input_labels': len(labels), 'shifts': len(shifts),
              'associativity_triples': len(labels)**3,
              'canonical_relation_cases': len(labels)**2*len(shifts),
              'wrong_shift_direction_mismatches': wrong_direction,
              'unit_inverse_grade_purity_canonical_host_injection': True,
              'bicyclic_distinguished_products': {'p_times_q': multiply(p, q), 'q_times_p': multiply(q, p)},
              'scope': 'bounded exact checks; products are not truncated; not a proof of infinite claims'}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
