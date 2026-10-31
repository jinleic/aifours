#!/usr/bin/env python3
"""Compare exact separated-pair DP and binary-run classification on finite domains.

This checks binary occurrence orders, not the ordered Olson conjecture.
No result file is overwritten and no third-party package is used.
"""

import argparse
import itertools
import json


def maximum_separated_pairs(word):
    """Direct interval DP, allowing any two equal endpoints and skipping interiors."""
    n = len(word)
    value = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        best = value[i + 1]
        for j in range(i + 1, n):
            if word[i] == word[j]:
                best = max(best, 1 + value[j + 1])
        value[i] = best
    return value[0]


def classify_runs(word):
    runs = []
    for bit in word:
        if not runs or runs[-1][0] != bit:
            runs.append([bit, 1])
        else:
            runs[-1][1] += 1
    odd = [i for i, (_, length) in enumerate(runs) if length % 2]
    if len(odd) == 1:
        return 'one_odd_run'
    if (len(odd) == 3 and odd[1] == odd[0] + 1 and odd[2] == odd[1] + 1
            and runs[odd[1]][1] == 1):
        return 'three_adjacent_odd_middle_singleton'
    return 'not_certificate_complete'


def assay(kernel_order):
    length = 4 * kernel_order - 1
    target = 2 * kernel_order - 1
    counts = {'one_odd_run': 0, 'three_adjacent_odd_middle_singleton': 0,
              'not_certificate_complete': 0}
    checked = 0
    examples = {}
    for word in itertools.product((0, 1), repeat=length):
        checked += 1
        label = classify_runs(word)
        max_pairs = maximum_separated_pairs(word)
        if (max_pairs >= target) != (label != 'not_certificate_complete'):
            raise RuntimeError('run characterization disagrees with exact interval DP')
        if max_pairs > target:
            raise RuntimeError('more pairs than occurrence count allows')
        counts[label] += 1
        if label not in examples:
            examples[label] = {'word': word, 'max_pairs': max_pairs}
    m = target
    expected_one = (m + 2) * (2 ** m)
    expected_three = m * (2 ** m)
    expected_total = (length + 1) * (2 ** m)
    if (counts['one_odd_run'] != expected_one or
            counts['three_adjacent_odd_middle_singleton'] != expected_three or
            counts['one_odd_run'] + counts['three_adjacent_odd_middle_singleton'] != expected_total):
        raise RuntimeError('exact combinatorial count disagrees with run classification')
    return {'kernel_order': kernel_order, 'word_length': length, 'target_pairs': target,
            'binary_words_checked': checked, 'counts': counts,
            'expected_counts': {'one_odd_run': expected_one,
                                'three_adjacent_odd_middle_singleton': expected_three,
                                'certificate_complete': expected_total},
            'examples': examples}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    data = {'scope': 'exact finite binary occurrence-order check; not a group-theorem or novelty verification',
            'assays': [assay(k) for k in (1, 2, 3, 4)]}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'result': 'PASS_FINITE_EXHAUSTION',
                      'domains': [{'kernel_order': x['kernel_order'], 'binary_words_checked': x['binary_words_checked'],
                                   'certificate_complete': x['expected_counts']['certificate_complete']}
                                  for x in data['assays']],
                      'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()
