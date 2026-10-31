#!/usr/bin/env python3
"""Independent direct-product replay of the bounded cross-cut support assay."""

import argparse
import copy
import hashlib
import json
import random


def direct(word, indices, p):
    x = parity = 0
    for i in indices:
        value, bit = word[i]
        x = (x + value if parity == 0 else x - value) % p
        parity ^= bit
    return x, parity


def calculate(word, p):
    rot = [i for i, (_, e) in enumerate(word) if not e][:2*p-2]
    refs = [i for i, (_, e) in enumerate(word) if e]
    if len(rot) != 2*p-2 or len(word) != 4*p-1:
        raise ValueError('wrong actual word or rotation count')
    total = sum(word[i][0] for i in rot) % p
    z = [(i, (word[i][0] + 2*sum(word[j][0] for j in rot if j < i)) % p) for i in refs]
    old = total == 0 or len({v for _, v in z}) == p
    cuts = []
    direct_checks = 0
    for k in range(1, len(z)):
        aa, bb = z[:k], z[k:]
        A, B = {x for _, x in aa}, {y for _, y in bb}
        intersection = A.intersection({(y-total) % p for y in B})
        lower = max(0, len(A)+len(B)-p)
        if len(intersection) < lower:
            raise ValueError('intersection lower bound failed')
        pairs = [(i, j) for i, x in aa for j, y in bb if (y-x) % p == total]
        if len(pairs) < len(intersection):
            raise ValueError('actual pairs do not realize support intersection')
        for i, j in pairs:
            direct_checks += 1
            if direct(word, sorted(rot+[i, j]), p) != (0, 0):
                raise ValueError('actual ordered product not identity')
        if lower:
            cuts.append({'cut_after_reflection_count': k, 'left_support': sorted(A),
                         'right_support': sorted(B), 'lower_bound': lower,
                         'actual_cross_cut_pairs': len(pairs), 'first_pair': list(pairs[0])})
    return {'rotation_sum': total, 'old_condition': old,
            'full_potential_support': len({v for _, v in z}) == p,
            'good_cuts': cuts, 'potentials': [list(pair) for pair in z],
            'selected_rotations': rot}, direct_checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results')
    args = parser.parse_args()
    raw = open(args.results, 'rb').read()
    data = json.loads(raw)
    rng = random.Random(data['seed'])
    checked = direct_checks = improved_total = 0
    for row in data['domains']:
        p, r = row['p'], row['rotation_count']
        improved = any_cut = 0
        first = None
        for trial in range(80):
            positions = set(rng.sample(range(4*p-1), r))
            word = [[rng.randrange(p), 0 if i in positions else 1] for i in range(4*p-1)]
            observed, checks = calculate(word, p)
            checked += 1
            direct_checks += checks
            any_cut += int(bool(observed['good_cuts']))
            if observed['good_cuts'] and not observed['old_condition']:
                improved += 1
                if first is None:
                    first = {'trial': trial, 'word': word, 'analysis': observed}
        if (improved != row['strict_fixed_I_improvements'] or
                any_cut != row['at_least_one_cut_certificate'] or first != row['first_improvement']):
            raise ValueError('seed replay or saved cut mismatch')
        improved_total += improved
    for entry in data['proper_support_family_checks']:
        p = entry['p']
        expected, checks = calculate(entry['word'], p)
        direct_checks += checks
        if expected != entry['analysis'] or expected['old_condition']:
            raise ValueError('proper-support family mismatch')
        cut = entry['specified_middle_cut']
        if cut not in expected['good_cuts']:
            raise ValueError('specified family cut missing')
    damaged = copy.deepcopy(data['proper_support_family_checks'][0]['analysis'])
    damaged['selected_rotations'][0] = damaged['selected_rotations'][1]
    expected, _ = calculate(data['proper_support_family_checks'][0]['word'], data['proper_support_family_checks'][0]['p'])
    if damaged == expected:
        raise ValueError('duplicate selected-rotation control was not detected')
    print(json.dumps({'result': 'PASS_INDEPENDENT_CROSSCUT_REPLAY',
                      'input_sha256': hashlib.sha256(raw).hexdigest(),
                      'sampled_words_replayed': checked,
                      'direct_crosscut_products_checked': direct_checks,
                      'strict_fixed_I_improvements': improved_total,
                      'proper_support_family_instances_checked': len(data['proper_support_family_checks']),
                      'duplicate_rotation_control_rejected': True,
                      'scope': 'bounded seed replay, not proof or novelty certification'}, sort_keys=True))


if __name__ == '__main__':
    main()
