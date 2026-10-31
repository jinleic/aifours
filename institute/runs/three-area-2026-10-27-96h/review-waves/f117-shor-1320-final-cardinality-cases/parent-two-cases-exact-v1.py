#!/usr/bin/env python3
"""Parent exact check of the remaining order-1320 border cases.

Necessary arithmetic only; the code-to-border theorem is a written premise.
No author/reviewer checker is imported or executed.
"""
import hashlib
import itertools as it
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'parent-two-cases-result-v1.json'
SOURCE = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261028-1320-border-no-go-candidate-v1.md')
PIN = '52aeaff132fb0e59f9c735054b017df9471e543035ba0bfea1d3dcd04385869e'
from math import gcd
N = 1320
A = {0, 3, 8, 11}
Y = {0, 1, 7, 13, 14}


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, text=True, capture_output=True).stdout.strip()


def differences(values):
    return {gcd(abs(a-b), N) for a, b in it.combinations(values, 2)}


def independent(values, forbidden):
    return not (differences(values) & forbidden)


def screen(anchors, forbidden):
    return [x for x in range(N)
            if all(x == y or gcd(abs(x-y), N) not in forbidden for y in anchors)]


def main():
    if OUT.exists():
        raise FileExistsError(OUT)
    start = clock()
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != PIN:
        raise ValueError('SOURCE_HASH_MISMATCH')
    ga, gy = differences(A), differences(Y)
    cp = screen(A, gy)
    if len(cp) != 112:
        raise AssertionError('HEAD_UNIVERSE')

    # P24: every class 1,2,5,6 mod8 has exactly three candidate heads.
    forced = A.copy()
    for c in (1, 2, 5, 6):
        members = [x for x in cp if x % 8 == c]
        if len(members) != 3:
            raise AssertionError('FORCED_HEAD_CLASS')
        forced.update(members)
    full_g = differences(forced)
    q24 = screen(Y, full_g)
    q24_counts = [sum(x % 11 == c for x in q24) for c in range(11)]
    deficient = [c for c, count in enumerate(q24_counts) if count < 5]
    if not deficient:
        raise AssertionError('P24_EXPECTED_COUNTING_CONTRADICTION')
    # Omitting the six extra forced-old-head classes loses this root test.
    smaller_g = ga | {55, 165, 220, 440, 660}
    relaxed = screen(Y, smaller_g)
    relaxed_counts = [sum(x % 11 == c for x in relaxed) for c in range(11)]
    if any(c < 5 for c in relaxed_counts):
        raise AssertionError('P24_CONTROL_EXPECTED_NO_ROOT_DEFICIENCY')

    # P44: a 4+4 choice in the two mod11 classes cannot avoid gcd55.
    c1 = [x for x in cp if x % 11 == 1]
    c2 = [x for x in cp if x % 11 == 2]
    heads = []
    no55 = []
    for u in it.combinations(c1, 4):
        for v in it.combinations(c2, 4):
            choice = u+v
            if independent(choice, gy):
                heads.append(choice)
                if 55 not in differences(choice):
                    no55.append(choice)
    if not heads or no55:
        raise AssertionError('P44_FORCED_GCD55')

    forbidden = ga | {55}
    cq = screen(Y, forbidden)
    classes = {c: [x for x in cq if x % 5 == c] for c in (0, 4)}
    if any(x % 3 == 1 for values in classes.values() for x in values):
        raise AssertionError('P44_OUTSIDE_CLASS_FACT')
    extras = [x for x in cq if x % 5 not in (0, 4) and x % 3 != 1]
    if len(extras) != 12:
        raise AssertionError('P44_SEED_UNIVERSE')
    statistics = {'seeds': 0, 'compatible_seeds': 0, 'class_choice_pairs': 0,
                  'balanced_pairs': 0, 'cross_compatible_pairs': 0, 'solutions': 0}
    retained = []
    for seed in it.combinations(extras, 8):
        statistics['seeds'] += 1
        if not independent(seed, forbidden):
            continue
        statistics['compatible_seeds'] += 1
        choices = {}
        for c, required_anchor in ((0, 0), (4, 14)):
            pool = [x for x in classes[c]
                    if independent(seed+(x,), forbidden)]
            options = []
            for group in it.combinations(pool, 6):
                if required_anchor in group and independent(group, forbidden):
                    options.append(group)
            choices[c] = options
        retained.append({'seed': list(seed),
                         'class0_choices': len(choices[0]),
                         'class4_choices': len(choices[4])})
        for left in choices[0]:
            for right in choices[4]:
                statistics['class_choice_pairs'] += 1
                union = seed+left+right
                balanced = (sum(x % 3 == 0 for x in union) == 10 and
                            sum(x % 3 == 2 for x in union) == 10)
                statistics['balanced_pairs'] += balanced
                cross_ok = all(gcd(abs(x-y), N) not in forbidden
                               for x in left for y in right)
                statistics['cross_compatible_pairs'] += cross_ok
                statistics['solutions'] += balanced and cross_ok
    if statistics['solutions'] or not statistics['balanced_pairs']:
        raise AssertionError('P44_EXCLUSION_OR_SKIP_CROSS_POSITIVE_CONTROL')
    receipt = {
        'kind': 'PARENT_EXACT_ORDER1320_FINAL_CASE_CHECK',
        'started_native_clock': start, 'finished_native_clock': clock(),
        'source_sha256': PIN,
        'P24': {'forced_heads': sorted(forced), 'forbidden_gcds': sorted(full_g),
                'Q_candidate_count': len(q24), 'Q_mod11_counts': q24_counts,
                'required_per_mod11_class': 5, 'deficient_classes': deficient,
                'relaxed_no_root_deficiency_counts': relaxed_counts},
        'P44': {'head_admissible_pairs': len(heads), 'head_no55_pairs': len(no55),
                'tail_extras': extras, 'statistics': statistics,
                'compatible_seed_choices': retained,
                'skip_cross_positive_control': statistics['balanced_pairs']},
        'limits': 'Only exact necessary conditions for the final two border '
                  'cardinalities. Code-to-border, prime uniformity, Sands, and '
                  'f114 cardinality reduction remain written/reviewed premises; '
                  'no all-order completion theorem, novelty or formal proof.'}
    with OUT.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps({'result': 'PASS_FINAL_CASES',
                      'P24_counts': q24_counts, 'P24_deficient': deficient,
                      'P44_statistics': statistics,
                      'receipt': str(OUT),
                      'receipt_sha256': hashlib.sha256(OUT.read_bytes()).hexdigest(),
                      'clock_started': start,
                      'clock_finished': receipt['finished_native_clock']}, sort_keys=True))


if __name__ == '__main__':
    main()
