#!/usr/bin/env python3
"""Independently replay bounded actual dihedral words and check original products.

No producer code is imported. Every reflection pair is checked directly for
both the prefix equation and the original 2p-occurrence group product.
"""

import argparse
import copy
import hashlib
import itertools
import json
import random


def direct_product(word, indices, p):
    x, bit = 0, 0
    for i in indices:
        y, next_bit = word[i]
        x = (x + y if bit == 0 else x - y) % p
        bit = (bit + next_bit) % 2
    return x, bit


def inspect_word(word, p):
    rotations = [i for i, entry in enumerate(word) if entry[1] == 0]
    reflections = [i for i, entry in enumerate(word) if entry[1] == 1]
    chosen = rotations[:2*p-2]
    if len(chosen) != 2*p-2 or len(reflections) <= p:
        raise ValueError('invalid declared rotation envelope')
    total = sum(word[i][0] for i in chosen) % p
    z = [(i, (word[i][0] + 2*sum(word[j][0] for j in chosen if j < i)) % p)
         for i in reflections]
    full = len({v for _, v in z}) == p
    promised = total == 0 or full
    good = []
    for (i, zi), (j, zj) in itertools.combinations(z, 2):
        indices = sorted(chosen + [i, j])
        actual = direct_product(word, indices, p)
        expected = (total + zi - zj) % p
        if actual != (expected, 0):
            raise ValueError('prefix equation disagrees with original group product')
        if actual == (0, 0):
            good.append((i, j))
    if promised and not good:
        raise ValueError('sufficient condition did not produce an actual pair')
    return {'sum': total, 'full': full, 'promised': promised, 'good': good,
            'chosen': chosen, 'z': z}


def check_saved(entry, p):
    word = entry['word']
    if len(word) != 4*p-1 or any(bit not in (0, 1) or not 0 <= x < p for x, bit in word):
        raise ValueError('malformed original dihedral word')
    digest = hashlib.sha256(json.dumps(word, separators=(',', ':')).encode()).hexdigest()
    if digest != entry['word_sha256']:
        raise ValueError('word hash mismatch')
    independently = inspect_word(word, p)
    declared = entry['analysis']
    if declared['rotation_sum_mod_p'] != independently['sum'] or declared['full_prefix_coverage'] != independently['full']:
        raise ValueError('saved prefix statistics incorrect')
    if declared['selector_promised_by_theorem'] != independently['promised']:
        raise ValueError('saved promise incorrect')
    if declared['selected_rotations'] != independently['chosen']:
        raise ValueError('saved rotation choices incorrect')
    indices = declared['selected_original_indices']
    pair = declared['selected_reflections']
    if independently['good']:
        if pair is None or tuple(pair) not in independently['good']:
            raise ValueError('saved pair does not work')
        if indices != sorted(independently['chosen'] + pair) or len(indices) != 2*p or len(set(indices)) != len(indices):
            raise ValueError('saved original selector incorrect')
        if direct_product(word, indices, p) != (0, 0) or declared['direct_product'] != [0, 0]:
            raise ValueError('saved direct product incorrect')
    elif pair is not None or indices is not None:
        raise ValueError('saved nonexistent selector')
    return independently


def fail_on_mutation(entry, mutate, p, expected):
    damaged = copy.deepcopy(entry)
    mutate(damaged)
    try:
        check_saved(damaged, p)
    except ValueError as exc:
        if str(exc) == expected:
            return expected
        raise ValueError('mutation produced unintended rejection: ' + str(exc)) from exc
    raise ValueError('damaged record accepted')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results')
    args = parser.parse_args()
    raw = open(args.results, 'rb').read()
    data = json.loads(raw)
    if data['seed'] != 2026102802:
        raise ValueError('unexpected seed')
    rng = random.Random(data['seed'])
    checked = pair_checks = total_promised = extra_found = 0
    representative_count = 0
    for domain in data['domains']:
        p, rotations = domain['prime'], domain['rotation_count']
        n = 4*p-1
        counts = {'total': 0, 'promised': 0, 'sum_zero': 0, 'full_coverage': 0,
                  'additional_pair_found': 0}
        first_promised_word = None
        first_promised_trial = None
        for trial in range(80):
            rotation_positions = set(rng.sample(range(n), rotations))
            word = [[rng.randrange(p), 0 if i in rotation_positions else 1] for i in range(n)]
            info = inspect_word(word, p)
            checked += 1
            pair_checks += len(info['z'])*(len(info['z'])-1)//2
            counts['total'] += 1
            counts['sum_zero'] += int(info['sum'] == 0)
            counts['full_coverage'] += int(info['full'])
            counts['promised'] += int(info['promised'])
            counts['additional_pair_found'] += int(bool(info['good']) and not info['promised'])
            if info['promised'] and first_promised_word is None:
                first_promised_word, first_promised_trial = word, trial
        if counts != domain['counts']:
            raise ValueError('seed replay counts mismatch')
        rep = domain['representative']
        if first_promised_word is None:
            if rep is not None:
                raise ValueError('unexpected representative')
        else:
            if rep is None or rep['trial'] != first_promised_trial or rep['word'] != first_promised_word:
                raise ValueError('representative is not seed replay')
            check_saved(rep, p)
            representative_count += 1
        total_promised += counts['promised']
        extra_found += counts['additional_pair_found']
    for entry in data['explicit_families']:
        p = entry['prime']
        info = check_saved(entry, p)
        if info['sum'] == 0 or not info['full'] or len(info['good']) == 0:
            raise ValueError('explicit alternating family lacks claimed condition')
        bits = [bit for _, bit in entry['word']]
        if any(bits[i] == bits[i+1] for i in range(len(bits)-1)):
            raise ValueError('explicit family quotient pattern is not alternating')
    representative = data['explicit_families'][0]
    mutations = [
        fail_on_mutation(representative, lambda x: x['analysis']['selected_original_indices'].__setitem__(1,
                                                                                      x['analysis']['selected_original_indices'][0]),
                         representative['prime'], 'saved original selector incorrect'),
        fail_on_mutation(representative, lambda x: x['analysis'].__setitem__('direct_product', [1, 0]),
                         representative['prime'], 'saved direct product incorrect'),
        fail_on_mutation(representative, lambda x: x.__setitem__('word_sha256', '0'*64),
                         representative['prime'], 'word hash mismatch'),
    ]
    print(json.dumps({'result': 'PASS_BOUNDED_REPLAY_AND_DIRECT_PRODUCTS',
                      'input_sha256': hashlib.sha256(raw).hexdigest(),
                      'random_words_replayed': checked, 'reflection_pairs_directly_checked': pair_checks,
                      'theorem_promised_words': total_promised,
                      'additional_pairs_outside_sufficient_condition': extra_found,
                      'representative_saved_words_checked': representative_count,
                      'explicit_family_instances_checked': len(data['explicit_families']),
                      'mutations_rejected_for_intended_reason': mutations,
                      'scope': 'finite reproducible checks; no general theorem or novelty attested'}, sort_keys=True))


if __name__ == '__main__':
    main()
