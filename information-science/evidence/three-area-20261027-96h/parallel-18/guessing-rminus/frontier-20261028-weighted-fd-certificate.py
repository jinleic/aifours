#!/usr/bin/env python3
"""Independent integer verifier for one weighted R-minus binary FD law.

The numerical-search output is only an untrusted candidate. This program uses
no floating-point arithmetic. It also gives an explicit finite block-size
sufficient for the strict 649/100 strategy bound via the standard type bound.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

INPUT = Path(__file__).with_name('frontier-20261028-fd-law-search-precise-result.json')
OUTPUT = Path(__file__).with_name('frontier-20261028-weighted-fd-certificate-result.json')
NEIGHBOURS = {
    1: (2, 3, 4, 5, 6, 7), 2: (1, 3, 7, 9, 10),
    3: (1, 2, 4, 8, 9), 4: (1, 3, 5, 8, 10),
    5: (1, 4, 6, 9, 10), 6: (1, 5, 7, 8, 9),
    7: (1, 2, 6, 8, 10), 8: (3, 4, 6, 7, 9, 10),
    9: (2, 3, 5, 6, 8), 10: (2, 4, 5, 7, 8),
}
NUMERATOR = 649
DENOMINATOR = 100


def binhash(value):
    return sha256(value.to_bytes((value.bit_length() + 7) // 8, 'big')).hexdigest()


def main():
    raw = INPUT.read_bytes()
    candidate = json.loads(raw)
    words = candidate['support_words_one_based_bitsets']
    weights = candidate['rounded_probability_numerators']
    assert len(words) == len(set(words)) == len(weights) == 88
    assert all(type(w) is int and 0 <= w < 1024 for w in words)
    assert all(type(w) is int and w > 0 for w in weights)
    total = sum(weights)
    assert total == candidate['rounded_probability_denominator'] == 6000
    assert all(v in NEIGHBOURS[u] for u, ns in NEIGHBOURS.items() for v in ns)
    assert sum(map(len, NEIGHBOURS.values())) == 52

    # Independent lookup-table FD verification and complete binary decoder.
    tables = {v: {} for v in range(1, 11)}
    def observation(w, v):
        return tuple((w >> (u - 1)) & 1 for u in NEIGHBOURS[v])
    for word in words:
        for vertex in range(1, 11):
            key, value = observation(word, vertex), (word >> (vertex - 1)) & 1
            old = tables[vertex].setdefault(key, value)
            assert old == value, (word, vertex)
    winners = []
    for bits in product((0, 1), repeat=10):
        word = sum(bit << i for i, bit in enumerate(bits))
        if all(tables[v].get(observation(word, v), 0) == bits[v - 1]
               for v in range(1, 11)):
            winners.append(word)
    assert set(words) <= set(winners)

    one = [sum(weight * ((word >> i) & 1) for word, weight in zip(words, weights))
           for i in range(10)]
    unweighted = [sum((word >> i) & 1 for word in words) for i in range(10)]
    worst = min(range(10), key=lambda i: abs(2 * one[i] - total))
    a = one[worst]
    b = total - a
    # Exactly certifies 100 H(X_V) > 649 H(X_worst).
    left = pow(a, NUMERATOR * a) * pow(b, NUMERATOR * b)
    right = pow(total, (NUMERATOR - DENOMINATOR) * total)
    for value, count in Counter(weights).items():
        right *= pow(value, DENOMINATOR * value * count)
    strict = left > right
    assert strict
    # Largest integer k such that left >= 2^k right, giving a quantified gap.
    gap_bits = left.bit_length() - right.bit_length()
    if left < (right << gap_bits):
        gap_bits -= 1
    assert gap_bits > 0 and left >= (right << gap_bits)
    # n=6000t, standard type lower bound M >= exp(nH)/(n+1)^88.
    # Thus 2^(gap_bits*t) > (6000t+1)^8800 suffices for M^100>Q^649.
    selected_t = None
    for t in (1, 10, 100, 1000, 10000):
        if (1 << (gap_bits * t)) > pow(total * t + 1, 88 * DENOMINATOR):
            selected_t = t
            break
    assert selected_t is not None
    baseline_inequality = pow(2, NUMERATOR) > pow(88, DENOMINATOR)
    assert baseline_inequality

    result = {
        'candidate_file': str(INPUT), 'candidate_sha256': sha256(raw).hexdigest(),
        'graph_edge_count': 26, 'word_count': len(words), 'positive_weight_count': len(weights),
        'weight_total': total, 'weight_frequency': sorted(Counter(weights).items()),
        'weighted_marginal_one_counts': one, 'unweighted_marginal_one_counts': unweighted,
        'lookup_fd_check': True, 'full_binary_domain_cases': 1024,
        'full_binary_default_zero_winner_count': len(winners),
        'default_zero_winners_exactly_candidate': set(words) == set(winners),
        'worst_marginal_vertex_one_based': worst + 1,
        'worst_marginal_one_count': a, 'worst_marginal_zero_count': b,
        'target_ratio': '649/100',
        'integer_inequality': 'a^(649a)(N-a)^(649(N-a)) > N^(549N) product_i w_i^(100 w_i)',
        'exact_integer_strict_comparison': strict,
        'left_bit_length': left.bit_length(), 'right_bit_length': right.bit_length(),
        'left_big_endian_sha256': binhash(left), 'right_big_endian_sha256': binhash(right),
        'certified_gap_at_least_power_of_two': gap_bits,
        'finite_type_class': {
            't': selected_t, 'n': total * selected_t,
            'row_count_rule': 'weight_i*t for each of the 88 listed candidate words',
            'M': '(6000t)! / product_i (weight_i*t)!',
            'Q': 'max_v binom(6000t, marginal_one_count_v*t)',
            'verified_integer_type_bound': '2^(gap_bits*t) > (6000t+1)^8800',
            'deduced': 'M^100 > Q^649; original q=Q full-domain decoders have at least M winners',
        },
        'exact_uniform_baseline_comparison': '2^649 > 88^100',
        'uniform_baseline_strictly_below_649_over_100': baseline_inequality,
        'limits': 'One exact FD law and an explicit finite type-class existence construction; below the known 20/3 lower bound and not a universal upper bound.',
    }
    with OUTPUT.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
