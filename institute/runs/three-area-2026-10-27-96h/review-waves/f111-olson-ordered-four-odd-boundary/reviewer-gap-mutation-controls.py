#!/usr/bin/env python3
"""Independent direct action, mutation and complete p=3 raw-gap controls."""
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json


def action(word, indices, p):
    images = []
    for x in range(p):
        y = x
        for i in reversed(indices):
            typ, value = word[i][0], int(word[i][1:])
            y = (y + value) % p if typ == 'r' else (value - y) % p
        images.append(y)
    return images


def independent_matching_table(n):
    # Enumerate every edge subset rather than using the path formula or DP.
    result = []
    for graph in range(1 << n):
        maximum = 0
        for selected in range(1 << n):
            if selected & ~graph:
                continue
            if all(not ((selected >> j) & 1 and (selected >> ((j + 1) % n)) & 1)
                   for j in range(n)):
                maximum = max(maximum, selected.bit_count())
        result.append(maximum)
    return result


def raw_gap_exhaustion():
    p, n = 3, 7
    matching = independent_matching_table(n)
    counts = {'reflection_words': 0, 'actual_gap_bit_patterns': 0,
              'nonconstant_gap_cases': 0, 'ref_failing_reflection_words': 0,
              'lower_ref_failing_gap_cases': 0}
    for z in product(range(p), repeat=n):
        counts['reflection_words'] += 1
        ref_failing = all(sum((1 if j % 2 == 0 else -1) * z[i]
                              for j, i in enumerate(choice)) % p != 0
                          for choice in combinations(range(n), 2 * p))
        counts['ref_failing_reflection_words'] += int(ref_failing)
        different = sum((z[i] != z[(i + 1) % n]) << i for i in range(n))
        r = different.bit_count()
        if r == 0:
            assert not ref_failing
        for rotations in range(1 << n):
            counts['actual_gap_bit_patterns'] += 1
            graph = different | rotations
            absent = n - graph.bit_count()
            if r:
                counts['nonconstant_gap_cases'] += 1
                assert absent <= n - r
            if ref_failing and matching[graph] <= p - 3:
                counts['lower_ref_failing_gap_cases'] += 1
                assert r and absent >= p + 4 and r <= 2 * p - 6
    return counts


def mutation_checks(data):
    cases = []
    for case in data['actual_examples']:
        p, word = case['p'], case['word'][:]
        selector = case['selected_full_word_indices_zero_based']
        assert len(selector) == 2 * p and len(set(selector)) == 2 * p
        assert all(word[i].startswith('s') for i in selector)
        assert action(word, selector, p) == list(range(p))
        chosen = selector[0]
        word[chosen] = 's' + str((int(word[chosen][1:]) + 1) % p)
        mutated = action(word, selector, p)
        assert mutated != list(range(p))
        displacement = [(mutated[i] - i) % p for i in range(p)]
        assert len(set(displacement)) == 1 and displacement[0] in (1, p - 1)
        cases.append({'p': p, 'variant': case['variant'],
                      'mutated_selected_index': chosen,
                      'mutated_product_action': mutated,
                      'reason': 'same-size reflection selector has nonidentity product'})
    return cases


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    target = Path(args.output)
    if target.exists():
        raise FileExistsError(target)
    raw = Path(args.input).read_bytes()
    data = json.loads(raw)
    result = {'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'own_example_source_sha256': hashlib.sha256(raw).hexdigest(),
              'gap_exhaustion': raw_gap_exhaustion(),
              'selected_label_mutations': mutation_checks(data)}
    with target.open('x', encoding='utf-8') as out:
        json.dump(result, out, indent=2, sort_keys=True)
        out.write('\n')
    print(json.dumps({'gap_exhaustion': result['gap_exhaustion'],
                      'label_mutations_rejected': len(result['selected_label_mutations']),
                      'program_sha256': result['program_sha256']}, sort_keys=True))


if __name__ == '__main__':
    main()
