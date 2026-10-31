#!/usr/bin/env python3
"""Independent finite synthetic controls; no candidate code or archived data."""
from itertools import permutations, combinations
from math import gcd
import json


def require(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    z = [0] * len(p)
    for i, value in enumerate(p):
        z[value] = i
    return tuple(z)


def subgroup(generators, identity):
    reached = {identity}
    queue = [identity]
    for x in queue:
        for g in generators:
            y = mul(x, g)
            if y not in reached:
                reached.add(y)
                queue.append(y)
    return frozenset(reached)


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def small_s4_fibres():
    elems = tuple(permutations(range(4)))
    identity = tuple(range(4))
    n = frozenset(x for x in elems if parity(x) == 0)
    require(len(n) == 12, 'A4_ORDER')
    subs = {frozenset({identity})}
    queue = [frozenset({identity})]
    for h in queue:
        for g in elems:
            if g not in h:
                new = subgroup(tuple(h) + (g,), identity)
                if new not in subs:
                    subs.add(new)
                    queue.append(new)
    require(len(subs) == 30, 'S4_SUBGROUP_CENSUS')
    reps = (identity, (1, 0, 2, 3))
    fibres = [frozenset(mul(x, t) for x in n) for t in reps]
    entries = []
    formula_checks = 0
    missing_conjugation = None
    for h in sorted(subs, key=lambda x: (len(x), sorted(x))):
        k = h & n
        image_size = len({parity(x) for x in h})
        a, b, original = 2 // image_size, len(n) // len(k), len(elems) // len(h)
        require(original == a * b, 'INDEX_PRODUCT')
        cosets = {frozenset(mul(g, x) for x in h) for g in elems}
        for c in cosets:
            entries.append((a, b, original, c, frozenset(parity(x) for x in c)))
            for t, fibre in zip(reps, fibres):
                inter = c & fibre
                for x in inter:
                    ti = inverse(t)
                    lhs = {mul(z, ti) for z in inter}
                    right = {mul(mul(x, ti), mul(mul(t, v), ti)) for v in k}
                    require(lhs == right and lhs <= n, 'FIBRE_TRANSLATION')
                    formula_checks += 1
                    wrong = {mul(mul(x, ti), v) for v in k}
                    if wrong != lhs and missing_conjugation is None:
                        missing_conjugation = {'subgroup_order': len(h), 'kernel_order': len(k),
                                               'fibre_representative': list(t), 'left_size': len(lhs)}
    require(missing_conjugation is not None, 'MISSING_CONJUGATION_NEGATIVE_NOT_DETECTED')
    divisibility_checks = overlapping_bad_pairs = 0
    for e1, e2 in combinations(entries, 2):
        a1, b1, n1, c1, q1 = e1
        a2, b2, n2, c2, q2 = e2
        d = gcd(a1, a2) * gcd(b1, b2)
        require(gcd(n1, n2) % d == 0, 'GCD_PRODUCT_DIVISIBILITY')
        divisibility_checks += 1
        if not c1.intersection(c2) and q1.intersection(q2):
            require(gcd(b1, b2) >= 2, 'FIBRE_COPRIME_DISJOINT')
            if gcd(n1, n2) <= 7:
                require(gcd(a1, a2) <= 3, 'OVERLAP_LOW_GCD')
                overlapping_bad_pairs += 1
    require(overlapping_bad_pairs > 0, 'NO_OVERLAPPING_BAD_SYNTHETICS')
    return {'subgroups': len(subs), 'left_cosets': len(entries),
            'fibre_formula_checks': formula_checks, 'index_divisibility_pairs': divisibility_checks,
            'actual_overlapping_low_gcd_pairs': overlapping_bad_pairs,
            'negative': {'intended_reason': 'MISSING_CONJUGATION', 'witness': missing_conjugation}}


def vector_cosets(p):
    all_points = frozenset((x, y) for x in range(p) for y in range(p))
    lines = {frozenset(((k*x) % p, (k*y) % p) for k in range(p))
             for x, y in all_points if (x, y) != (0, 0)}
    require(len(lines) == p + 1, 'PLANE_LINE_COUNT')
    subspaces = [frozenset({(0, 0)}), *lines, all_points]
    result = []
    for h in subspaces:
        cosets = {frozenset(((x + dx) % p, (y + dy) % p) for x, y in h)
                  for dx, dy in all_points}
        result.extend((c, p*p // len(h)) for c in cosets)
    return all_points, result


def abelian_helly_synthetic():
    odd, cs = vector_cosets(5)
    cases = []
    for c, odd_index in cs:
        for part in (frozenset({0}), frozenset({1}), frozenset({0, 1})):
            mask = sum(1 << (25 * bit + 5*x + y) for bit in part for x, y in c)
            cases.append((mask, (2 // len(part)) * odd_index))
    require(len(odd) == 25 and len(cases) == 168, 'ABELIAN_CASE_COUNT')
    edges = [set() for _ in cases]
    for i, (m1, a1) in enumerate(cases):
        for j in range(i + 1, len(cases)):
            m2, a2 = cases[j]
            if m1 & m2 and gcd(a1, a2) <= 3:
                edges[i].add(j)
    edge_count = sum(map(len, edges))
    triangles = 0
    for i in range(len(cases)):
        for j in edges[i]:
            for k in edges[i] & edges[j]:
                triangles += 1
                require(cases[i][0] & cases[j][0] & cases[k][0], 'RESTRICTED_TRIPLE_HELLY')
    require(edge_count > 0 and triangles > 0, 'EMPTY_HELLY_CONTROL')
    return {'group': 'C2 x F5^2', 'actual_cosets': len(cases),
            'pairwise_meeting_low_gcd_edges': edge_count, 'checked_clique_triples': triangles}


def missing_restrictions():
    # Three actual disjoint cosets in C2^3; coordinates are (kernel, quotient x, quotient y).
    c = [{(0, 0, 0), (0, 0, 1)}, {(1, 0, 0), (0, 1, 0)}, {(1, 0, 1), (1, 1, 0)}]
    q = [{(x, y) for _, x, y in z} for z in c]
    require(all(not a.intersection(b) for a, b in combinations(c, 2)), 'INDEX4_ACTUAL_NOT_DISJOINT')
    require(all(a.intersection(b) for a, b in combinations(q, 2)), 'INDEX4_PROJECTED_NOT_PAIRWISE')
    require(not set.intersection(*q), 'INDEX4_PROJECTED_HAS_COMMON_POINT')
    require(all(gcd(4, 4) <= 7 for _ in combinations(c, 2)), 'INDEX4_BAD_GCD')
    # Every two-point set in the elementary abelian group is a coset of a subgroup of size two.
    require(all(len(z) == 2 for z in c), 'INDEX4_NOT_AFFINE_LINES')
    f3 = {(x, y) for x in range(3) for y in range(3)}
    lines = [{(x, y) for x, y in f3 if y == 0},
             {(x, y) for x, y in f3 if x == 0},
             {(x, y) for x, y in f3 if (x + y) % 3 == 1}]
    require(all(a.intersection(b) for a, b in combinations(lines, 2)), 'INDEX3_NOT_PAIRWISE')
    require(not set.intersection(*lines), 'INDEX3_HAS_COMMON_POINT')
    require(all(len(z) == 3 for z in lines), 'INDEX3_NOT_AFFINE_LINES')
    return {'negative_index4': {'intended_reason': 'ACTUAL_RESTRICTED_HELLY_FAILS_WITH_INDEX_4',
                                'G': 'C2^3', 'original_indices': [4, 4, 4],
                                'quotient_indices': [2, 2, 2]},
            'negative_index3': {'intended_reason': 'QUOTIENT_HELLY_FAILS_WITH_INDEX_3',
                                'Q': 'C3^2', 'quotient_indices': [3, 3, 3],
                                'scope': 'quotient cosets only; no original-family lift claimed'}}


def ramsey_and_wording():
    def triangle_free_both(n, colouring):
        edges = list(combinations(range(n), 2))
        colour = {e: (colouring >> j) & 1 for j, e in enumerate(edges)}
        for triple in combinations(range(n), 3):
            v = [colour[e] for e in combinations(triple, 2)]
            if v[0] == v[1] == v[2]:
                return False
        return True
    k5 = sum(triangle_free_both(5, b) for b in range(1 << 10))
    k6 = sum(triangle_free_both(6, b) for b in range(1 << 15))
    require(k5 == 12 and k6 == 0, 'RAMSEY_3_3')
    require(8 >= 8 and 9 >= 8 and gcd(8, 9) == 1, 'GCD_WORDING_NEGATIVE')
    require(gcd(2, 3) * gcd(3, 2) == 1 and gcd(6, 6) == 6, 'DIVISIBILITY_NOT_EQUALITY_NEGATIVE')
    return {'K5_two_colourings_without_monochromatic_triangle': k5,
            'K6_two_colourings_without_monochromatic_triangle': k6,
            'negative_gcd_wording': {'intended_reason': 'INDICES_AT_LEAST_8_DO_NOT_FORCE_GCD_AT_LEAST_8',
                                      'indices': [8, 9], 'gcd': 1},
            'negative_gcd_equality': {'intended_reason': 'GCD_PRODUCT_IS_A_DIVISOR_NOT_ALWAYS_EQUAL',
                                       'a': [2, 3], 'b': [3, 2]}}


def example_control():
    p = 11
    odd, cosets = vector_cosets(p)
    full_odd = [z for z, index in cosets if index == 1]
    require(len(full_odd) == 1, 'UNIQUE_FULL_ODD_COSET')
    q2 = [frozenset((bit, xy) for xy in odd) for bit in (0, 1)]
    require(not q2[0].intersection(q2[1]), 'Q_INDEX2_NOT_DISJOINT')
    checked = 0
    for odd_coset, index in cosets:
        if index == 1:
            continue
        for bit in (0, 1):
            c = {(bit, xy) for xy in odd_coset}
            require(sum(bool(c & q) for q in q2) == 1, 'Q_P_COSET_INDEX2_INTERSECTION')
            checked += 1
    lines = [{(x, y) for x, y in odd if y == 0},
             {(x, y) for x, y in odd if x == 0},
             {(x, y) for x, y in odd if (x + y) % p == 1}]
    pair_sizes = [len(a & b) for a, b in combinations(lines, 2)]
    require(pair_sizes == [1, 1, 1] and not set.intersection(*lines), 'Q_NOT_3_HELLY')
    bits = frozenset((x, y) for x in range(2) for y in range(2))
    z2 = frozenset({(0, 0)})
    two_lines = [frozenset({(0, 0), (1, 0)}), frozenset({(0, 0), (0, 1)}),
                 frozenset({(0, 0), (1, 1)})]
    bit_cosets = set()
    for h in (z2, *two_lines, bits):
        for x, y in bits:
            bit_cosets.add(frozenset(((a + x) % 2, (b + y) % 2) for a, b in h))
    require(len(bit_cosets) == 11, 'F2_SQUARED_AFFINE_COSET_COUNT')
    max_packing = 0
    for k in range(1, len(bit_cosets) + 1):
        for family in combinations(bit_cosets, k):
            if all(not a.intersection(b) for a, b in combinations(family, 2)):
                max_packing = max(max_packing, k)
    require(max_packing == 4, 'F2_SQUARED_AFFINE_PACKING')
    return {'p': p, 'Q_even_p_divisible_cosets_checked_against_index2_partition': checked,
            'quotient_affine_line_pair_intersections': pair_sizes, 'triple_intersection': 0,
            'G_two_primary_affine_cosets': len(bit_cosets), 'G_two_primary_max_packing': max_packing,
            'scope': 'finite instance; symbolic all-prime argument is written in review'}


out = {'s4': small_s4_fibres(), 'restricted_abelian': abelian_helly_synthetic(),
       'missing_restrictions': missing_restrictions(), 'ramsey': ramsey_and_wording(),
       'example': example_control()}
print(json.dumps(out, sort_keys=True, indent=2))
