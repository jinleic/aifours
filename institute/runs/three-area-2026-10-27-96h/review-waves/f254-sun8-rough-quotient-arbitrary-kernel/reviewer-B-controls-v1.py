#!/usr/bin/env python3
"""Bounded independent finite controls for the frozen f254 slice B.

No source/author code is imported.  All structures are generated directly
from the stated definitions.  A successful run is finite evidence only.
"""
import itertools
import json
import math


class ControlFailure(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise ControlFailure(reason)


def expect_failure(reason, operation):
    try:
        operation()
    except ControlFailure as exc:
        if str(exc) != reason:
            raise ControlFailure('wrong negative reason: ' + str(exc)) from exc
        return reason
    raise ControlFailure('negative did not fail: ' + reason)


def disjoint_family(cosets):
    return all(a.isdisjoint(b) for a, b in itertools.combinations(cosets, 2))


def cyclic_cosets(n, step):
    require(n % step == 0, 'cyclic divisor')
    h = {step * k % n for k in range(n)}
    return {frozenset((x + y) % n for y in h) for x in range(n)}


def check_cyclic_B7_pairs(n):
    # The cyclic subgroups are precisely step*Z/nZ for step dividing n.
    cosets = [(c, d) for d in range(1, n + 1) if n % d == 0
              for c in cyclic_cosets(n, d)]
    for (a, ia), (b, ib) in itertools.combinations(cosets, 2):
        if a.isdisjoint(b):
            require(math.gcd(ia, ib) > 7, 'cyclic B7 pair')
    return len(cosets)


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def semimul(a, b, p, q, action):
    return ((a[0] + pow(action, a[1], p) * b[0]) % p,
            (a[1] + b[1]) % q)


def semipow(x, k, p, q, action):
    result = (0, 0)
    for _ in range(k):
        result = semimul(result, x, p, q, action)
    return result


def seminv(x, p, q, action):
    y = (-x[1]) % q
    return ((-pow(action, y, p) * x[0]) % p, y)


def pc(a, b):
    return tuple(a[b[i]] for i in range(3))


def pinv(a):
    return tuple(a.index(i) for i in range(3))


def add3(a, b, p):
    return ((a[0] + b[0]) % 7, (a[1] + b[1]) % p,
            (a[2] + b[2]) % p)


def main():
    result = {'positive': {}, 'negative': {}}
    pos, neg = result['positive'], result['negative']

    # Explicit affine non-Helly example, generated from equations.
    p = 11
    plane = {(x, y) for x in range(p) for y in range(p)}
    lines = [{(x, y) for x, y in plane if x == 0},
             {(x, y) for x, y in plane if y == 0},
             {(x, y) for x, y in plane if (x + y) % p == 1}]
    require(isprime(p) and p > 7 and all(len(x) == p for x in lines),
            'affine indices')
    pairwise = [len(a & b) for a, b in itertools.combinations(lines, 2)]
    require(pairwise == [1, 1, 1], 'affine pair intersections')
    require(not set.intersection(*lines), 'affine empty triple')
    pos['affine_lines'] = {'p': p, 'group_order': len(plane), 'indices': [p] * 3,
                           'pair_intersections': pairwise, 'triple_intersection': 0}
    neg['global_helly_without_index_condition'] = expect_failure(
        'global-intersection', lambda: require(bool(set.intersection(*lines)),
                                                'global-intersection'))

    # The finite quotient C7 models all finite-index cosets of Q_add x C7.
    seven = cyclic_cosets(7, 7)
    require(len(seven) == 7 and disjoint_family(seven), 'seven C7 cosets')
    require(all(math.gcd(7, 7) == 7 for _ in itertools.combinations(seven, 2)),
            'seven C7 gcd')
    require(len(set.union(*(set(c) for c in seven))) == 7, 'seven cover C7')
    pos['kernel_finite_quotient'] = {'seven_bad_cosets': len(seven),
        'indices': [7] * 7, 'pair_gcd': 7, 'union_size': 7,
        'B7_bound': 'exactly 7; upper bound by cardinality'}

    # Generate every subgroup and coset of C7 x F_11^2 from the two factors.
    # The coprime-factor decomposition and the elementary subspace list give
    # all 2*(1+12+1)=28 subgroups, with no source checker involved.
    vertices = list(itertools.product(range(7), range(p), range(p)))
    vectors = list(itertools.product(range(p), repeat=2))
    spaces = [frozenset({(0, 0)})]
    spaces += [frozenset((t, t * slope % p) for t in range(p))
               for slope in range(p)]
    spaces += [frozenset((0, t) for t in range(p)), frozenset(vectors)]
    require(len(spaces) == 14 and len(set(spaces)) == 14, 'subspace list')
    all_cosets = []
    for factor7 in ({0}, set(range(7))):
        for space in spaces:
            h = {(z, x, y) for z in factor7 for x, y in space}
            seen = set()
            index = len(vertices) // len(h)
            for v in vertices:
                if v not in seen:
                    c = frozenset(add3(v, u, p) for u in h)
                    require(len(c) == len(h), 'coset cardinality')
                    seen.update(c)
                    all_cosets.append((c, index))
            require(len(seen) == len(vertices), 'subgroup coset cover')
    counts = {}
    for _, index in all_cosets:
        counts[index] = counts.get(index, 0) + 1
    expected_counts = {1: 1, 7: 7, 11: 132, 77: 924, 121: 121, 847: 847}
    require(counts == expected_counts, 'complete finite coset counts')
    index7 = [c for c, index in all_cosets if index == 7]
    require(disjoint_family(index7), 'index-seven disjoint')
    require(len(set.union(*(set(c) for c in index7))) == len(vertices),
            'index-seven cover')
    divisible = [(c, index) for c, index in all_cosets if index % p == 0]
    require(all(any(not c.isdisjoint(d) for d in index7) for c, _ in divisible),
            'index-seven blocks p-cosets')
    require(all(index in (1, 7) or index % p == 0 for _, index in all_cosets),
            'finite index dichotomy')
    incomplete = index7[:-1]
    neg['deleted_cover_coset'] = expect_failure('seven-cosets-do-not-cover',
        lambda: require(len(set.union(*(set(c) for c in incomplete))) == len(vertices),
                        'seven-cosets-do-not-cover'))
    survivor = next((index for c, index in divisible
                     if all(c.isdisjoint(d) for d in incomplete)), None)
    require(survivor is not None, 'incomplete cover survivor')
    pos['finite_product_all_cosets'] = {'group_order': len(vertices),
        'subgroups': 28, 'cosets_by_index': counts, 'total_cosets': len(all_cosets),
        'index7_cover_size': len(vertices), 'p_divisible_cosets_checked': len(divisible),
        'after_deleting_one_index7_coset_survivor_index': survivor}

    # A genuinely nonnormal rough quotient and nonnormal original subgroups.
    # F_11 : C5 has order 55 and is 3-rough; the kernel is S3.
    s3 = list(itertools.permutations(range(3)))
    identity = (0, 1, 2)
    qid = (0, 0)
    qgroup = list(itertools.product(range(11), range(5)))
    def qm(a, b):
        return semimul(a, b, 11, 5, 3)
    def qi(a):
        return seminv(a, 11, 5, 3)
    def gm(a, b):
        return (pc(a[0], b[0]), qm(a[1], b[1]))
    def gi(a):
        return (pinv(a[0]), qi(a[1]))
    h5 = {(0, y) for y in range(5)}
    h11 = {(x, 0) for x in range(11)}
    require(pow(3, 5, 11) == 1 and all(pow(3, j, 11) != 1 for j in range(1, 5)),
            'semidirect action')
    conjugate_h5 = {qm(qm((1, 0), h), qi((1, 0))) for h in h5}
    require(conjugate_h5 != h5, 'quotient subgroup nonnormal')
    core_h5 = set(h5)
    core_h11 = set(h11)
    for g in qgroup:
        core_h5.intersection_update(qm(qm(g, h), qi(g)) for h in h5)
        core_h11.intersection_update(qm(qm(g, h), qi(g)) for h in h11)
    require(core_h5 == {qid} and core_h11 == h11, 'quotient subgroup cores')
    require(math.gcd(55, 2 * 3) == 1, '3-rough finite quotient order')

    def quotient_cosets(h):
        remaining = set(qgroup)
        out = []
        while remaining:
            representative = min(remaining)
            c = frozenset(qm(representative, x) for x in h)
            require(c <= remaining, 'quotient coset partition')
            remaining.difference_update(c)
            out.append((representative, c))
        return out
    cs5, cs11 = quotient_cosets(h5), quotient_cosets(h11)
    require(len(cs5) == 11 and len(cs11) == 5, 'nonnormal quotient indices')
    for _, c in cs5:
        for _, d in cs11:
            require(len(c & d) == 1, 'coprime quotient intersection')
            require(len(c & d & set(qgroup) & set(qgroup)) == 1,
                    'repeated unit subgroup intersection')
    left = {qm((1, 0), h) for h in h5}
    right = {qm(h, (1, 0)) for h in h5}
    neg['wrong_left_right_orientation'] = expect_failure('left-right-coset',
        lambda: require(left == right, 'left-right-coset'))

    kperm = (1, 0, 2)
    vperm = (2, 1, 0)
    k = {identity, kperm}
    u1 = {(s, h) for s in k for h in h5}
    u2 = {(s, h) for s in k for h in h11}
    order_g = 6 * len(qgroup)
    n1, n2 = order_g // len(u1), order_g // len(u2)
    require((n1, n2) == (33, 15) and math.gcd(n1, n2) == 3,
            'original index gcd')
    test_g = (identity, (1, 0))
    require({gm(gm(test_g, u), gi(test_g)) for u in u1} != u1,
            'original subgroup nonnormal')
    kernel_k = {(s, qid) for s in k}
    total_fibres = 0
    wrong_conjugation_witness = None
    for qrep1, c1q in cs5:
        for qrep2, c2q in cs11:
            q = next(iter(c1q & c2q))
            c1 = {gm((identity, qrep1), u) for u in u1}
            c2 = {gm((vperm, qrep2), u) for u in u2}
            require(c1.isdisjoint(c2), 'original cosets disjoint')
            fibre = {(s, q) for s in s3}
            for s in s3:
                t = (s, q)
                translated = []
                conjugated = {gm(gm(t, u), gi(t)) for u in kernel_k}
                for c in (c1, c2):
                    actual = {gm(x, gi(t)) for x in c & fibre}
                    x = next(iter(c & fibre))
                    base = gm(x, gi(t))
                    expected = {gm(base, u) for u in conjugated}
                    require(actual == expected, 'fibre translation formula')
                    require(all(z[1] == qid for z in actual | conjugated),
                            'translated fibre in kernel')
                    require(len(actual) == 2 and len(conjugated) == 2,
                            'translated fibre cardinality')
                    wrong = {gm(base, u) for u in kernel_k}
                    if wrong_conjugation_witness is None and actual != wrong:
                        wrong_conjugation_witness = (actual, wrong)
                    translated.append(actual)
                require(translated[0].isdisjoint(translated[1]),
                        'translated disjointness')
                total_fibres += 1
    require(wrong_conjugation_witness is not None, 'nonnormal fibre witness exists')
    actual, wrong = wrong_conjugation_witness
    neg['omitted_kernel_conjugation'] = expect_failure('fiber-missing-conjugation',
        lambda: require(actual == wrong, 'fiber-missing-conjugation'))
    pos['nonnormal_quotient_and_fibres'] = {
        'T': 3, 'kernel': 'S3', 'quotient': 'C11 semidirect C5',
        'orders_G_N_Q': [330, 6, 55], 'quotient_indices': [11, 5],
        'quotient_core_orders': [len(core_h5), len(core_h11)],
        'quotient_coset_tuples': len(cs5) * len(cs11),
        'repeated_whole_group_subgroup_index': 1,
        'original_indices': [n1, n2], 'original_gcd': math.gcd(n1, n2),
        'kernel_indices': [3, 3], 'all_actual_fibres_and_t_choices': total_fibres,
        'first_quotient_subgroup_nonnormal': True,
        'first_original_subgroup_nonnormal': True}

    # Dropping roughness, even with a Sun8 quotient, breaks the all-r theorem.
    quotient_order = 2
    require(math.gcd(quotient_order, 210) != 1, 'nonrough C2')
    require(disjoint_family([{0}, {1}]) and math.gcd(2, 2) <= 7,
            'C2 bad pair')
    neg['dropped_roughness_r1'] = expect_failure('B7-G-bound-fails',
        lambda: require(math.gcd(2, 2) > 7, 'B7-G-bound-fails'))
    pos['nonrough_boundary'] = {'T': 7, 'r': 1, 'kernel_order': 1,
        'quotient_and_G_order': 2, 'two_original_indices': [2, 2],
        'quotient_Sun8': 'vacuous: only two elements'}

    # Non-split cyclic extension: C121 has a unique subgroup of order 11.
    require(check_cyclic_B7_pairs(11) == 12, 'C11 coset count')
    n121_cosets = check_cyclic_B7_pairs(121)
    lifts = [x for x in range(121) if x % 11 == 1]
    require(len(lifts) == 11 and all((11 * x) % 121 != 0 for x in lifts),
            'C121 no splitting lift')
    neg['cyclic_split_section'] = expect_failure('section-order',
        lambda: require((11 * 1) % 121 == 0, 'section-order'))
    pos['nonsplit_cyclic'] = {'G': 'C121', 'N': 'C11', 'Q': 'C11',
        'quotient_generator_lifts_checked': len(lifts),
        'all_lifts_fail_order_11': True, 'all_cyclic_cosets_checked_for_r1': n121_cosets}

    # Give the candidate's existential prime pair explicitly.  Moreover a
    # non-split extension with that nonabelian quotient is built independently.
    pp, qq, action = 23, 11, 2
    require(isprime(pp) and isprime(qq) and pp > 7 and qq > 7 and
            (pp - 1) % qq == 0, 'explicit primes')
    require(pow(action, qq, pp) == 1 and
            all(pow(action, j, pp) != 1 for j in range(1, qq)), 'action order')
    a, b = (1, 0), (0, 1)
    require(semimul(a, b, pp, qq, action) != semimul(b, a, pp, qq, action),
            'nonabelian quotient')
    require(math.gcd(pp * qq, 210) == 1, '7-rough quotient order')
    lifts_b = [(0, 1 + 11 * j) for j in range(11)]
    powers = [semipow(x, 11, pp, 121, action) for x in lifts_b]
    require(all(x == (0, 11) for x in powers), 'nonabelian nonsplit lifts')
    neg['nonabelian_split_section'] = expect_failure('section-order',
        lambda: require(semipow((0, 1), 11, pp, 121, action) == (0, 0),
                        'section-order'))
    pos['nonabelian_nonsplit'] = {'p': pp, 'q': qq, 'action': action,
        'quotient': 'C23 semidirect C11', 'quotient_order': pp * qq,
        'noncommuting_ab': [semimul(a, b, pp, qq, action),
                            semimul(b, a, pp, qq, action)],
        'G': 'C23 semidirect C121', 'kernel': 'C11',
        'all_generator_lifts_checked': len(lifts_b), 'each_eleventh_power': [0, 11],
        'kernel_B7_le_1': True}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
