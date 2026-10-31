#!/usr/bin/env python3
"""Exact bounded assays for ordered EGZ extension; not a conjecture verifier.

Run once with an unused output path.  Uses only Python's standard library.
The independent checker is a separate file and does not import this module.
"""

import argparse
import hashlib
import itertools
import json
import random


def add(u, v, p):
    return tuple((x + y) % p for x, y in zip(u, v))


def multiply(a, b, p, signs):
    v, parity = a
    w, other_parity = b
    acted = tuple((sign * x) % p for sign, x in zip(signs, w)) if parity else w
    return add(v, acted, p), (parity + other_parity) % 2


def reflection_collision_exhaustive(p):
    """Enumerate all ordered, pairwise-distinct reflection triples in F_p^2."""
    vectors = list(itertools.product(range(p), repeat=2))
    collision_count = 0
    total = 0
    witness = None
    for v, w, u in itertools.permutations(vectors, 3):
        total += 1
        pairs = [multiply((v, 1), (w, 1), p, (-1, -1)),
                 multiply((v, 1), (u, 1), p, (-1, -1)),
                 multiply((w, 1), (u, 1), p, (-1, -1))]
        collided = pairs[0] == pairs[2]
        progression = all((x + z - 2 * y) % p == 0 for x, y, z in zip(v, w, u))
        if collided != progression:
            raise RuntimeError('collision/progression equivalence failed')
        if len(set(pairs)) != (2 if collided else 3):
            raise RuntimeError('unexpected distinct-pair-product count')
        if collided:
            collision_count += 1
            if witness is None:
                witness = {'v': v, 'w': w, 'u': u,
                           'pair_products': pairs,
                           'index_pairs': [[0, 1], [0, 2], [1, 2]]}
    expected = (p * p) * (p * p - 1)
    if collision_count != expected:
        raise RuntimeError('progression count mismatch')
    return {'p': p, 'dimension': 2, 'triples_checked': total,
            'collision_triples': collision_count, 'expected_collision_triples': expected,
            'relation_verified_for_every_triple': True, 'first_witness': witness}


def exact_kernel_obstruction():
    """Enumerate all target-sized subsets of the sharp elementary-abelian word."""
    p, dim = 3, 2
    m = p ** dim
    word = [(0, 0)] * (m - 1) + [(1, 0)] * (p - 1) + [(0, 1)] * (p - 1)
    zero_indices = []
    checked = 0
    for indices in itertools.combinations(range(len(word)), m):
        checked += 1
        value = (0, 0)
        for i in indices:
            value = add(value, word[i], p)
        if value == (0, 0):
            zero_indices.append(indices)
    if zero_indices:
        raise RuntimeError('claimed short-threshold obstruction failed')
    extended = word + [(0, 0)]
    positive = list(range(m - 1)) + [len(word)]
    value = (0, 0)
    for i in positive:
        value = add(value, extended[i], p)
    if len(positive) != m or value != (0, 0):
        raise RuntimeError('extended positive control failed')
    return {'p': p, 'dimension': dim, 'kernel_order': m, 'word': word,
            'word_length': len(word), 'selector_size': m,
            'subsets_checked': checked, 'zero_sum_selectors': len(zero_indices),
            'one_extra_zero_control_word': extended,
            'one_extra_zero_control_indices': positive}


def block_choices(word, p, signs):
    """One quotient-identity pair per chronological three-occurrence block."""
    blocks = []
    products = []
    for start in range(0, len(word), 3):
        if start + 3 > len(word):
            raise RuntimeError('incomplete quotient block')
        candidates = [(start, start + 1), (start, start + 2), (start + 1, start + 2)]
        pair = next((ij for ij in candidates if word[ij[0]][1] == word[ij[1]][1]), None)
        if pair is None:
            raise RuntimeError('binary quotient triple has no equal pair')
        product = multiply(word[pair[0]], word[pair[1]], p, signs)
        if product[1] != 0:
            raise RuntimeError('selected block did not land in kernel')
        blocks.append(pair)
        products.append(product[0])
    return blocks, products


def choose_kernel_zero(products, p, target):
    """Exact bounded dynamic program over count and F_p^2; retain original block IDs."""
    states = [dict() for _ in range(target + 1)]
    states[0][(0, 0)] = ()
    for block_id, value in enumerate(products):
        for size in range(min(target, block_id + 1), 0, -1):
            for previous, path in list(states[size - 1].items()):
                total = add(previous, value, p)
                if total not in states[size]:
                    states[size][total] = path + (block_id,)
    return states[target].get((0, 0)), sum(map(len, states))


def make_word(kind, length, rng, p):
    if kind == 'random':
        return [((rng.randrange(p), rng.randrange(p)), rng.randrange(2)) for _ in range(length)]
    if kind == 'alternating':
        return [((i % p, (i * i + 1) % p), i % 2) for i in range(length)]
    if kind == 'all_reflections':
        return [((i % p, (i * i + 1) % p), 1) for i in range(length)]
    if kind == 'all_kernel':
        return [((i % p, (i * i + 1) % p), 0) for i in range(length)]
    if kind == 'constant':
        return [((1, 2), 1) for _ in range(length)]
    raise ValueError(kind)


def full_group_trials():
    """Construct actual 50-position selectors in complete 99-letter words."""
    p, dim, quotient_order = 5, 2, 2
    kernel_order = p ** dim
    group_order = quotient_order * kernel_order
    length = 2 * group_order - 1
    block_count = kernel_order + dim * (p - 1)
    if 3 * block_count != length:
        raise RuntimeError('this configured test does not meet exact chunk budget')
    rng = random.Random(20261028)
    results = []
    for signs in [(-1, -1), (-1, 1), (1, 1)]:
        for case_number, kind in enumerate(['alternating', 'all_reflections', 'all_kernel', 'constant'] + ['random'] * 6):
            word = make_word(kind, length, rng, p)
            blocks, products = block_choices(word, p, signs)
            selected_blocks, state_count = choose_kernel_zero(products, p, kernel_order)
            if selected_blocks is None:
                raise RuntimeError('no exact-size zero sum found in bounded corpus')
            indices = tuple(i for j in selected_blocks for i in blocks[j])
            if len(indices) != group_order or tuple(sorted(set(indices))) != indices:
                raise RuntimeError('selector does not preserve actual occurrence order')
            result = ((0, 0), 0)
            for i in indices:
                result = multiply(result, word[i], p, signs)
            if result != ((0, 0), 0):
                raise RuntimeError('original-order product is not identity')
            digest = hashlib.sha256(json.dumps(word, separators=(',', ':')).encode()).hexdigest()
            results.append({'p': p, 'dimension': dim, 'quotient_order': quotient_order,
                            'action_signs': signs, 'case': kind, 'case_number': case_number,
                            'word_length': length, 'word': word, 'word_sha256': digest,
                            'selected_indices_zero_based': indices, 'direct_original_product': result,
                            'quotient_blocks': blocks, 'selected_block_ids_zero_based': selected_blocks,
                            'dp_states_retained': state_count})
    return {'seed': 20261028, 'cases': results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, help='new JSON output path; existing files are not overwritten')
    args = parser.parse_args()
    results = {'scope': 'bounded exact checks only; not exhaustive group or conjecture verification',
               'reflection_triples': [reflection_collision_exhaustive(3), reflection_collision_exhaustive(5)],
               'kernel_obstruction': exact_kernel_obstruction(),
               'actual_group_trials': full_group_trials()}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(results, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'reflection_triples': [{k: row[k] for k in ('p', 'triples_checked', 'collision_triples')}
                                           for row in results['reflection_triples']],
                      'kernel_subsets_checked': results['kernel_obstruction']['subsets_checked'],
                      'kernel_zero_selectors': results['kernel_obstruction']['zero_sum_selectors'],
                      'actual_group_cases': len(results['actual_group_trials']['cases']),
                      'actual_group_successes': len(results['actual_group_trials']['cases']),
                      'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()
