#!/usr/bin/env python3
"""Independent bounded sequence check; not a premise of the written ZS proof."""
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path


def zero_sum_sizes(sequence, modulus):
    states = [1] + [0] * len(sequence)
    mask = (1 << modulus) - 1
    for used, value in enumerate(sequence, 1):
        for size in range(used, 0, -1):
            previous = states[size - 1]
            states[size] |= ((previous << value) | (previous >> (modulus - value))) & mask
    return {size for size, residues in enumerate(states) if size and residues & 1}


def minimum_cost(sequence, p):
    costs = []
    for generator in range(1, 2 * p, 2):
        if math.gcd(generator, 2 * p) != 1:
            continue
        inverse = pow(generator, -1, 2 * p)
        total = 0
        for value in sequence:
            coefficient = value * inverse % (2 * p)
            if coefficient > p:
                coefficient -= 2 * p
            total += coefficient - 1 if coefficient > 0 else -coefficient
        costs.append(total)
    return min(costs)


def satisfies_zp(sequence, p, kappa):
    return not any(2 * kappa + 2 <= size <= 2 * p
                   for size in zero_sum_sizes(sequence, 2 * p))


def main(output):
    rows = []
    p = 5
    for k in range(1, (p + 1) // 2 + 1):
        for kappa in range(k):
            length = 2 * p + 2 * kappa - k
            examined = accepted = 0
            maximum_cost = None
            for sequence in itertools.combinations_with_replacement(range(1, 2 * p, 2), length):
                examined += 1
                if not satisfies_zp(sequence, p, kappa):
                    continue
                cost = minimum_cost(sequence, p)
                if cost > k - 1:
                    raise ValueError(('ZS counterexample', p, k, kappa, sequence, cost))
                accepted += 1
                maximum_cost = cost if maximum_cost is None else max(maximum_cost, cost)
            expected = math.comb(length + p - 1, p - 1)
            if examined != expected:
                raise ValueError(('incomplete multiset universe', examined, expected))
            rows.append({'p': p, 'k': k, 'kappa': kappa, 'length': length,
                         'multisets': examined, 'ZP_multisets': accepted, 'maximum_minimum_cost': maximum_cost})
    tight = []
    obstructions = []
    for p in (5, 7, 11, 13):
        for k in (2, (p + 1) // 2):
            kappa = k - 1
            sequence = (1,) * (2 * p - 1) + (2 * p - 1,) * kappa
            cost = minimum_cost(sequence, p)
            if not satisfies_zp(sequence, p, kappa) or cost != k - 1:
                raise ValueError(('tight control mismatch', p, k, cost))
            tight.append({'p': p, 'k': k, 'kappa': kappa, 'cost': cost,
                          'stronger_cost_bound_k_minus_2_rejected': cost > k - 2})
        sequence = (1,) * (2 * p - 1) + (3,) * (p - 1)
        cost = minimum_cost(sequence, p)
        if not satisfies_zp(sequence, p, p - 1) or cost <= p - 1:
            raise ValueError(('ZP-only obstruction mismatch', p, cost))
        obstructions.append({'p': p, 'k': p, 'kappa': p - 1, 'minimum_cost': cost,
                             'bound_p_minus_1': p - 1, 'ZP_satisfied': True})
    result = {'status': 'PASS', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python': sys.version, 'scope': 'Complete p=5 sequence-multiset smoke plus stated tight and obstruction controls; not a universal proof or a word counterexample.',
              'all_p5_multisets': sum(row['multisets'] for row in rows),
              'p5': rows, 'tight_controls': tight, 'ZP_only_obstructions': obstructions}
    with Path(output).open('x') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')
    print(json.dumps({'status': result['status'], 'all_p5_multisets': result['all_p5_multisets'],
                      'p5_ZP_multisets': sum(row['ZP_multisets'] for row in rows),
                      'tight_controls': len(tight), 'obstructions': len(obstructions)}))


if __name__ == '__main__':
    main(sys.argv[1])
