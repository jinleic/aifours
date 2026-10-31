#!/usr/bin/env python3
"""Independent, bounded GF(2) controls; not a Boolean-target search.

Enumerates small vector spaces and quadratic truth tables from definitions.  It
never imports, reads or runs the author's programs or their output files.
"""
from collections import Counter
from itertools import combinations, product
import json
import random
import sys


def check(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p] = row
                break
    return len(pivots)


def kernel(rows, n):
    pivots = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p] = row
                break
    ans = []
    for j in range(n):
        if j in pivots:
            continue
        v = 1 << j
        for p in sorted(pivots):
            if (pivots[p] & v).bit_count() & 1:
                v ^= 1 << p
        ans.append(v)
    return ans


def span(basis):
    out = [0]
    for v in basis:
        out += [x ^ v for x in out]
    return out


def swap_pairs(x, pairs):
    x &= (1 << (2 * pairs)) - 1
    return ((x & 0x55) << 1) | ((x & 0xaa) >> 1)


def symp(x, y, pairs):
    return (swap_pairs(x, pairs) & y).bit_count() & 1


def form_rank(basis, pairs):
    return rank([sum(symp(x, y, pairs) << j for j, y in enumerate(basis))
                 for x in basis])


def three_spaces(n):
    """Unique three-spaces via their first two nonzero points and first point outside their plane."""
    lim = 1 << n
    for a in range(1, lim):
        for b in range(a + 1, lim):
            c = a ^ b
            if c <= b:
                continue
            for v in range(b + 1, lim):
                if v == c or (v ^ a) < v or (v ^ b) < v or (v ^ c) < v:
                    continue
                yield (a, b, v)


def coset_syndrome(points, equations):
    syndrome = 0
    for point in points:
        label = sum(((point & eq).bit_count() & 1) << i
                    for i, eq in enumerate(equations))
        syndrome ^= 1 << label
    return syndrome


def quadratic_truth_tables():
    # Truth tables as 64-bit integers, Gray traversal of all 22 ANF coefficients.
    masks = []
    for degree in range(3):
        for indices in combinations(range(6), degree):
            mask = 0
            for x in range(64):
                if all((x >> j) & 1 for j in indices):
                    mask |= 1 << x
            masks.append(mask)
    check(len(masks) == 22, 'RM_COEFFICIENT_COUNT')
    hist = [0] * 65
    value = 0
    for i in range(1 << 22):
        if i:
            value ^= masks[(i & -i).bit_length() - 1]
        hist[value.bit_count()] += 1
    check(sum(hist) == 1 << 22 and hist[0] == 1, 'RM_ENUMERATION')
    check(sum(hist[1:16]) == 0 and hist[16] > 0, 'RM_MINIMUM_WEIGHT')
    cubic = sum(1 << x for x in range(64) if (x & 7) == 7)
    check(cubic.bit_count() == 8, 'CUBIC_CONTROL_EXPECTED_WEIGHT')
    return {str(i): v for i, v in enumerate(hist) if v}, cubic.bit_count()


def all_subspaces_and_geometry():
    total = 0
    families8 = []
    admissible6 = 0
    rank8_counts = Counter()
    rank6_counts = Counter()
    radical = [0, 64, 128, 192]
    six_radical_even = 0
    ext = Counter()
    for dual in three_spaces(8):
        total += 1
        L = kernel(dual, 8)
        check(len(L) == 5 and all((u & v).bit_count() % 2 == 0
                                  for u in dual for v in L), 'KERNEL_CONSTRUCTION')
        r8 = form_rank(L, 4)
        r6 = form_rank(L, 3)
        t = 5 - rank([x & 63 for x in L])
        rank8_counts[r8] += 1
        rank6_counts[(t, r6)] += 1
        # In the nondegenerate form, J times the dot-annihilator is the B-annihilator.
        iso_basis = tuple(swap_pairs(x, 4) for x in dual)
        iso = all(symp(x, y, 4) == 0 for x, y in combinations(iso_basis, 2))
        check((r8 == 2) == iso, 'RANK8_ORTHOGONAL_EQUIVALENCE')
        if iso:
            families8.append(iso_basis)
            nonzero = sorted(span(iso_basis)[1:])
            for x, y in combinations(nonzero, 2):
                z = x ^ y
                if y < z:
                    ext[(x, y, z)] += 1
        if r6 <= 2:
            admissible6 += 1
            check(t >= 1, 'RANK6_ADMISSIBLE_MISSES_RADICAL')
            if coset_syndrome(radical, dual) == 0:
                six_radical_even += 1
    check(total == 97155, 'ALL_FIVE_SPACE_COUNT')
    check(len(families8) == 11475, 'RANK8_FAMILY_COUNT')
    check(admissible6 == 16515 and six_radical_even == admissible6,
          'RANK6_FAMILY_OR_RADICAL_POSITIVE')
    check(rank6_counts[(2, 0)] + rank6_counts[(2, 2)] == 1395
          and rank6_counts[(1, 2)] == 15120, 'RANK6_FAMILY_SPLIT')
    check(len(ext) == 5355 and set(ext.values()) == {15}, 'ISOTROPIC_EXTENSION')
    bad_dual = kernel([64, 128, 2, 4, 8], 8)
    check(form_rank([64, 128, 2, 4, 8], 3) <= 2, 'MUTATION_L_ADMISSIBILITY')
    check(coset_syndrome([0, 64, 128, 193], bad_dual) != 0,
          'MUTATED_RADICAL_SHOULD_HAVE_ODD_COSETS')
    return {
        'all_five_spaces': total,
        'rank8_restricted_rank_counts': {str(k): v for k, v in sorted(rank8_counts.items())},
        'rank6_intersection_dimension_and_restricted_rank_counts':
            {f'{t},{r}': v for (t, r), v in sorted(rank6_counts.items())},
        'rank8_admissible': len(families8),
        'rank6_admissible': admissible6,
        'rank6_radical_plane_even_for_all': six_radical_even,
        'rank8_isotropic_two_planes': len(ext),
        'rank8_isotropic_three_extensions_per_two_plane': sorted(set(ext.values())),
        'mutated_radical_negative': 'ODD_COSET',
    }, families8


def bilinear_rigidity():
    # Unknowns are all 64 entries of an arbitrary bilinear form; no symmetry assumed.
    pivots = {}
    conditions = 0
    for x in range(256):
        for y in range(256):
            if symp(x, y, 4):
                continue
            conditions += 1
            row = sum(y << (8 * i) for i in range(8) if (x >> i) & 1)
            while row:
                p = row.bit_length() - 1
                if p in pivots:
                    row ^= pivots[p]
                else:
                    pivots[p] = row
                    break
    check(len(pivots) == 63, 'BILINEAR_RIGIDITY_RANK')
    return {'orthogonal_ordered_pairs': conditions, 'constraint_rank': len(pivots),
            'solution_dimension': 64 - len(pivots), 'known_nonzero_solution': 'B'}


def rank8_six_point_controls(families):
    by_dimension = Counter()
    zerosum = Counter()
    gram_zero = Counter()
    concrete = 0
    for d in range(1, 5):
        for nonzero in combinations(range(1, 1 << d), 5):
            points = (0,) + nonzero
            s = 0
            for x in points:
                s ^= x
            if s:
                continue
            zerosum[d] += 1
            dr = rank(points)
            by_dimension[dr] += 1
            gram = [sum((sum(((x >> i) & 1) * ((x >> j) & 1) for x in points) & 1) << j
                        for j in range(d)) for i in range(d)]
            if not any(gram):
                gram_zero[d] += 1
            if d == 4:
                check(dr == 4, 'RANK8_POINT_SPAN')
                check(any(coset_syndrome(points, tuple(swap_pairs(x, 4) for x in D))
                          for D in families), 'RANK8_SIX_SET_PARITY')
                concrete += 1
    check(zerosum[3] == 0 and zerosum[4] > 0 and sum(gram_zero.values()) == 0,
          'SIX_COLUMN_SELF_ORTHOGONAL_OBSTRUCTION')
    neg = (0, 1, 2, 4, 8, 15)
    check(rank(neg) == 4 and not any([]), 'SIX_COLUMN_NEGATIVE_SETUP')
    check(any(sum(((x >> i) & 1) * ((x >> j) & 1) for x in neg) & 1
              for i in range(4) for j in range(4)), 'NON_SELF_ORTHOGONAL_NEGATIVE')
    return {'zero_sum_six_sets_by_ambient_dimension': dict(zerosum),
            'zero_sum_six_sets_by_actual_span': dict(by_dimension),
            'self_orthogonal_zero_sum_sets': dict(gram_zero),
            'rank8_embedded_six_sets_tested': concrete,
            'negative_reason': 'NON_SELF_ORTHOGONAL_GRAM'}


def rank6_geometry_and_cases():
    iso2 = []
    for x in range(1, 64):
        for y in range(x + 1, 64):
            if y < (x ^ y) and not symp(x, y, 3):
                iso2.append((x, y))
    check(len(iso2) == 315, 'SIX_DIM_ISOTROPIC_PLANES')
    separators = {}
    counts = []
    for v in range(1, 64):
        choices = [U for U in iso2 if any(symp(v, u, 3) for u in U)]
        check(bool(choices), 'NONZERO_SEPARATION')
        separators[v] = choices[0]
        counts.append(len(choices))
    check(not any(any(symp(0, u, 3) for u in U) for U in iso2),
          'ZERO_VECTOR_SEPARATOR_NEGATIVE')
    # If U is not isotropic, U-perp has rank 4, so its lift is inadmissible.
    noniso = (1, 2)
    bad_bar = kernel([swap_pairs(x, 3) for x in noniso], 6)
    check(symp(*noniso, 3) == 1 and len(bad_bar) == 4
          and form_rank([64] + bad_bar, 3) == 4, 'NONISOTROPIC_NEGATIVE')

    def syndrome(points, r, U):
        # Character on R/<r>, plus the two symplectic labels for U-perp.
        dual = {1: 2, 2: 1, 3: 3}[r]
        out = 0
        for point in points:
            rho, s = point >> 6, point & 63
            t = (rho & dual).bit_count() & 1
            label = t | (symp(s, U[0], 3) << 1) | (symp(s, U[1], 3) << 2)
            out ^= 1 << label
        return out

    U0 = iso2[0]
    full = [0, 64, 128, 192]
    full_tests = 0
    for s in range(1, 64):
        for d in (1, 2, 3):
            r = next(x for x in (1, 2, 3) if x != d)
            for points in (full + [s, s ^ (64 * d)],
                           [0, 64 * d] + [s ^ rho for rho in full]):
                check(syndrome(points, r, U0) != 0, 'FULL_FIBRE_SPLIT')
                full_tests += 1
    three_tests = 0
    distinct_tests = 0
    for v in range(1, 64):
        s1 = 1 if v != 1 else 2
        s2 = s1 ^ v
        check(s1 and s2 and s1 != s2, 'THREE_FIBRE_SETUP')
        for d0, d1, d2 in product((1, 2, 3), repeat=3):
            points = [0, 64 * d0, s1, s1 ^ (64 * d1), s2, s2 ^ (64 * d2)]
            if len({d0, d1, d2}) < 3:
                r = next(x for x in (1, 2, 3) if x not in (d0, d1, d2))
                U = U0
            else:
                r, U = d0, separators[v]
                distinct_tests += 1
            check(syndrome(points, r, U) != 0, 'THREE_PAIR_SPLIT')
            three_tests += 1
    return {'isotropic_two_planes': len(iso2),
            'nonzero_vectors_with_separator': len(separators),
            'separator_counts_min_max': [min(counts), max(counts)],
            'zero_vector_negative': 'NO_SEPARATING_PLANE',
            'nonisotropic_plane_negative': 'RESTRICTED_RANK_4_NOT_ADMISSIBLE',
            'full_and_pair_cases_checked': full_tests,
            'three_pair_cases_checked': three_tests,
            'all_distinct_differences_cases_checked': distinct_tests}


def genuine_boolean_parity():
    rng = random.Random(195131)
    results = []
    changed_q_detected = False
    for sample in range(2):
        support = set(rng.sample(range(512), 256))
        T = 0
        for x in support:
            T ^= x
        check(T != 0, 'RANDOM_T_ZERO')
        Kbasis = kernel([T], 9)
        K = span(Kbasis)
        k = {a: (sum((a & x).bit_count() & 1 for x in support) - 128 if a else 0)
             for a in K}
        check(len(K) == 256 and all(k[a] % 2 == 0 for a in K), 'ACTUAL_EVEN_HALF')
        q = {a: (k[a] // 2) & 1 for a in K}
        def polar(x, y):
            return q[x] ^ q[y] ^ q[x ^ y]
        btable = [[polar(x, y) for y in Kbasis] for x in Kbasis]
        check(all(btable[i][i] == 0 and btable[i][j] == btable[j][i]
                  for i in range(8) for j in range(8)), 'POLAR_ALTERNATING')
        def predicted(mask):
            out = 0
            for i in range(8):
                if (mask >> i) & 1:
                    out ^= q[Kbasis[i]]
                    for j in range(i):
                        if (mask >> j) & 1:
                            out ^= btable[i][j]
            return out
        check(all(q[a] == predicted(i) for i, a in enumerate(K)), 'QUADRATIC_RECONSTRUCTION')
        changed = Kbasis[0] ^ Kbasis[1] ^ Kbasis[2]
        edited = dict(q)
        edited[changed] ^= 1
        check(edited[changed] != predicted(7), 'ALTERED_QUADRATIC_NEGATIVE')
        changed_q_detected = True
        Z8 = {a for a in K if k[a] % 8 == 0}
        check(any(k[a] != 0 for a in Z8), 'PEAK_HYPOTHESIS_NEGATIVE_SETUP')
        tested = attempts = 0
        while tested < 32:
            attempts += 1
            check(attempts <= 10000, 'ADMISSIBLE_SAMPLE_CAP_UNKNOWN')
            Lbasis = rng.sample(K[1:], 5)
            if rank(Lbasis) != 5:
                continue
            gram = [sum(polar(x, y) << j for j, y in enumerate(Lbasis)) for x in Lbasis]
            if rank(gram) > 2:
                continue
            L = span(Lbasis)
            unseen = set(K)
            raw = []
            zpar = []
            squares = []
            while unseen:
                a = min(unseen)
                A = {a ^ x for x in L}
                unseen.difference_update(A)
                weight = sum(q[x] for x in A)
                check(weight % 8 == 0, 'RANK_AT_MOST_TWO_WEIGHT')
                zpar.append(sum(x in Z8 for x in A) & 1)
                raw.append((weight // 4 + sum(x in Z8 for x in A)) & 1)
                squares.append(sum(k[x] * k[x] for x in A) % 32)
            check(len(raw) == 8 and len(set(raw)) == 1 and len(set(zpar)) == 1,
                  'COSSET_PARITY')
            check(len(set(squares)) == 1 and all(s == 16 * r for s, r in zip(squares, raw)),
                  'PARSEVAL_RESIDUE')
            tested += 1
        results.append({'support_size': len(support), 'T': T,
                        'five_space_samples': tested, 'attempts': attempts,
                        'max_abs_k_on_even_half': max(map(abs, k.values())),
                        'divisible8_nonzero_coefficients': sum(k[a] != 0 for a in Z8)})
    check(changed_q_detected, 'ALTERED_Q_CONTROL')
    return {'seed': 195131, 'functions': results,
            'altered_q_negative': 'NOT_QUADRATIC',
            'missing_peak_negative': 'Z8_CONTAINS_NONZERO_K'}


def main():
    tables, cubic_weight = quadratic_truth_tables()
    geometry, families = all_subspaces_and_geometry()
    result = {'status': 'PASS',
              'quadratic_rm_2_6': {'truth_tables': 1 << 22, 'weight_histogram': tables,
                                   'cubic_negative_weight': cubic_weight,
                                   'cubic_negative_reason': 'DEGREE_3_NOT_RM_2'},
              'all_subspaces': geometry,
              'bilinear_rigidity': bilinear_rigidity(),
              'rank8': rank8_six_point_controls(families),
              'rank6': rank6_geometry_and_cases(),
              'genuine_balanced_function_parity': genuine_boolean_parity(),
              'limits': ['no Boolean-target existence/exclusion search',
                         'no exhaustive 33,732,216 six-set replay',
                         'all listed checks concern necessary conditions and finite geometry']}
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(json.dumps({'status': 'FAIL', 'type': type(exc).__name__, 'reason': str(exc)}),
              file=sys.stderr)
        raise
