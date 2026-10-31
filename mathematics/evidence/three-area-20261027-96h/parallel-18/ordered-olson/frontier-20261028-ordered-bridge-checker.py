#!/usr/bin/env python3
"""Independently check stored finite word witnesses and bounded assay counts.

This checker imports no experimental producer. It checks each selected
original-index product directly, then checks two intentionally damaged cases.
"""

import argparse
import copy
import hashlib
import itertools
import json


def fail(message):
    raise ValueError(message)


def check_actual_case(case):
    p = case['p']
    signs = case['action_signs']
    word = case['word']
    ids = case['selected_indices_zero_based']
    if p != 5 or case['dimension'] != 2 or case['quotient_order'] != 2:
        fail('unexpected group declaration')
    if len(signs) != 2 or any(s not in (-1, 1) for s in signs):
        fail('invalid involution action')
    if len(word) != 99 or case['word_length'] != len(word):
        fail('wrong original word length')
    encoded = json.dumps(word, separators=(',', ':')).encode()
    if hashlib.sha256(encoded).hexdigest() != case['word_sha256']:
        fail('word hash mismatch')
    if len(ids) != 50 or any(not isinstance(i, int) or i < 0 or i >= len(word) for i in ids):
        fail('wrong selection size or index range')
    if any(ids[j] >= ids[j + 1] for j in range(len(ids) - 1)):
        fail('indices not strictly increasing')
    x = y = parity = 0
    for i in ids:
        vec, bit = word[i]
        if len(vec) != 2 or bit not in (0, 1) or any(not isinstance(a, int) or a < 0 or a >= p for a in vec):
            fail('invalid source element')
        sx = signs[0] if parity else 1
        sy = signs[1] if parity else 1
        x = (x + sx * vec[0]) % p
        y = (y + sy * vec[1]) % p
        parity = (parity + bit) % 2
    if (x, y, parity) != (0, 0, 0):
        fail('original-order product not identity')
    if case['direct_original_product'] != [[0, 0], 0]:
        fail('incorrect stored original product')
    blocks = case['quotient_blocks']
    chosen = case['selected_block_ids_zero_based']
    if len(blocks) != 33 or len(chosen) != 25 or any(chosen[j] >= chosen[j + 1] for j in range(24)):
        fail('bad quotient block selection')
    expected = []
    for j, block in enumerate(blocks):
        if len(block) != 2 or not (3*j <= block[0] < block[1] < 3*j+3):
            fail('quotient pair outside its original chronological block')
        if word[block[0]][1] != word[block[1]][1]:
            fail('quotient pair product is not identity')
    for j in chosen:
        if not isinstance(j, int) or j < 0 or j >= len(blocks):
            fail('block ID out of range')
        expected.extend(blocks[j])
    if expected != ids:
        fail('selected occurrences do not match selected original block pairs')


def check_reflection_counts(row):
    p = row['p']
    if p not in (3, 5) or row['dimension'] != 2:
        fail('unexpected reflection assay domain')
    vectors = [(a, b) for a in range(p) for b in range(p)]
    total = collisions = 0
    for a in vectors:
        for b in vectors:
            for c in vectors:
                if a == b or b == c or a == c:
                    continue
                total += 1
                p_ab = tuple((a[j] - b[j]) % p for j in (0, 1))
                p_ac = tuple((a[j] - c[j]) % p for j in (0, 1))
                p_bc = tuple((b[j] - c[j]) % p for j in (0, 1))
                collision = p_ab == p_bc
                if collision != all((a[j] + c[j]) % p == (2 * b[j]) % p for j in (0, 1)):
                    fail('reflection collision equivalence failed')
                if len({p_ab, p_ac, p_bc}) != (2 if collision else 3):
                    fail('reflection products have wrong distinct count')
                collisions += int(collision)
    if (total, collisions) != (row['triples_checked'], row['collision_triples']):
        fail('reflection exhaustive counts disagree')
    if collisions != p*p*(p*p-1):
        fail('reflection formula disagree')
    witness = row['first_witness']
    a, b, c = witness['v'], witness['w'], witness['u']
    products = [[[ (a[j]-b[j]) % p for j in (0, 1) ], 0],
                [[ (a[j]-c[j]) % p for j in (0, 1) ], 0],
                [[ (b[j]-c[j]) % p for j in (0, 1) ], 0]]
    if products != witness['pair_products'] or products[0] != products[2] or products[0] == products[1]:
        fail('stored reflection witness is invalid')


def check_kernel(row):
    p, m, word = row['p'], row['kernel_order'], row['word']
    if p != 3 or row['dimension'] != 2 or m != 9 or len(word) != 12:
        fail('unexpected kernel obstruction domain')
    checked = solutions = 0
    for indices in itertools.combinations(range(len(word)), m):
        checked += 1
        x = sum(word[i][0] for i in indices) % p
        y = sum(word[i][1] for i in indices) % p
        solutions += int(x == y == 0)
    if checked != row['subsets_checked'] or solutions != row['zero_sum_selectors'] or solutions:
        fail('kernel obstruction mismatch')
    extra, indices = row['one_extra_zero_control_word'], row['one_extra_zero_control_indices']
    if len(indices) != m or len(set(indices)) != m or any(i < 0 or i >= len(extra) for i in indices):
        fail('invalid positive control indices')
    if any(sum(extra[i][j] for i in indices) % p for j in (0, 1)):
        fail('positive control not zero sum')


def intended_failure(case, mutation, expected):
    changed = copy.deepcopy(case)
    mutation(changed)
    try:
        check_actual_case(changed)
    except ValueError as error:
        if str(error) == expected:
            return expected
        fail('mutation rejected for unintended reason: ' + str(error))
    fail('mutation was not rejected')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results', help='producer JSON, read once')
    args = parser.parse_args()
    raw = open(args.results, 'rb').read()
    data = json.loads(raw)
    rows = data['reflection_triples']
    if len(rows) != 2:
        fail('wrong number of reflection assay domains')
    for row in rows:
        check_reflection_counts(row)
    check_kernel(data['kernel_obstruction'])
    cases = data['actual_group_trials']['cases']
    if len(cases) != 30:
        fail('wrong number of actual-word trials')
    for case in cases:
        check_actual_case(case)
    mutations = [
        intended_failure(cases[0], lambda c: c['selected_indices_zero_based'].__setitem__(1, c['selected_indices_zero_based'][0]),
                         'indices not strictly increasing'),
        intended_failure(cases[0], lambda c: c['selected_indices_zero_based'].__setitem__(-1, len(c['word'])),
                         'wrong selection size or index range'),
        intended_failure(cases[0], lambda c: c.__setitem__('direct_original_product', [[1, 0], 0]),
                         'incorrect stored original product'),
        intended_failure(cases[0], lambda c: c['quotient_blocks'][0].__setitem__(0, 3),
                         'quotient pair outside its original chronological block'),
    ]
    print(json.dumps({'result': 'PASS_BOUNDED_CHECKS', 'input_sha256': hashlib.sha256(raw).hexdigest(),
                      'actual_group_cases_checked': len(cases),
                      'reflection_triple_domains_checked': len(rows),
                      'kernel_subsets_checked': data['kernel_obstruction']['subsets_checked'],
                      'mutation_controls_rejected_for_intended_reasons': mutations,
                      'scope': 'exact finite checks only; no general proof or novelty attested'}, sort_keys=True))


if __name__ == '__main__':
    main()
