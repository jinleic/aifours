#!/usr/bin/env python3
"""Exact necessary-support enumeration; independent of candidate code."""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement


def one_overlap(a, b):
    return (a & b).bit_count() == 1


def column_masks(rows, m):
    return [sum(1 << i for i, row in enumerate(rows) if row >> j & 1)
            for j in range(m)]


def unique_overlap_pair(masks):
    return next(((i, j) for i, j in combinations(range(len(masks)), 2)
                 if one_overlap(masks[i], masks[j])), None)


def connected(rows, m):
    seen_r, seen_c = {0}, set()
    while True:
        old = len(seen_r), len(seen_c)
        seen_c.update(j for i in tuple(seen_r) for j in range(m)
                      if rows[i] >> j & 1)
        seen_r.update(i for j in tuple(seen_c) for i in range(m)
                      if rows[i] >> j & 1)
        if (len(seen_r), len(seen_c)) == old:
            return len(seen_r) == m and len(seen_c) == m


def necessary_conditions(rows, m):
    if len(rows) != m or any(row.bit_count() < 2 or row >> m for row in rows):
        return False
    cols = column_masks(rows, m)
    if any(c.bit_count() < 2 for c in cols):
        return False
    if unique_overlap_pair(rows) is not None or unique_overlap_pair(cols) is not None:
        return False
    if not connected(rows, m):
        return False
    if m > 2:
        pairs = [row for row in rows if row.bit_count() == 2]
        high = [row for row in rows if row.bit_count() >= 3]
        if any(a & b for a, b in combinations(pairs, 2)):
            return False
        if any(sum((h & p) == p for h in high) < 2 for p in pairs):
            return False
    return True


def enumerate_component(m, excess):
    # A connected component with m>2 has disjoint degree-2 row pairs.
    # Relabel columns so those pairs are (0,1),(2,3),... .
    # Other rows are enumerated as nondecreasing multisets of masks, which
    # avoids row-permutation duplicates but preserves every possible support.
    if m == 2:
        return [(3, 3)] if excess == 0 else []
    found = []
    for s in range(m + 1):
        b = m - s
        if 2 * s > m or b > excess:
            continue
        pairs = [3 << (2 * j) for j in range(s)]
        allowed = [mask for mask in range(1 << m)
                   if mask.bit_count() >= 3
                   and mask.bit_count() - 2 <= excess
                   and all((mask & p).bit_count() in (0, 2) for p in pairs)]
        for high in combinations_with_replacement(allowed, b):
            if sum(h.bit_count() - 2 for h in high) != excess:
                continue
            rows = tuple(pairs) + high
            if necessary_conditions(rows, m):
                found.append(rows)
    return found


def exact_orthogonal(matrix):
    n = len(matrix)
    return all(sum(matrix[i][k] * matrix[j][k] for k in range(n)) == int(i == j)
               for i in range(n) for j in range(n))


def matrix_support(matrix):
    return tuple(sum(1 << j for j, value in enumerate(row) if value)
                 for row in matrix)


def check_real_unitary(label, matrix, expected_excess):
    n = len(matrix)
    masks = matrix_support(matrix)
    assert exact_orthogonal(matrix), label
    assert sum(mask.bit_count() for mask in masks) - 2 * n == expected_excess, label
    assert necessary_conditions(masks, n), label
    print('positive_exact_orthogonal', label, 'n', n, 'excess', expected_excess,
          'row_masks', ','.join(map(str, masks)))


def main():
    # Intended-reason negative controls for the separately used predicates.
    assert unique_overlap_pair((0b011, 0b110)) == (0, 1)
    print('negative_row_unique_overlap rejected_pair 0,1')
    cols = column_masks((0b011, 0b110), 3)
    assert one_overlap(cols[0], cols[1])
    print('negative_column_unique_overlap rejected_pair 0,1')
    assert min(c.bit_count() for c in column_masks((0b011, 0b011, 0b111), 3)) == 1
    print('negative_column_degree rejected_degree 1')
    disconnected = (0b0011, 0b0011, 0b1100, 0b1100)
    assert not connected(disconnected, 4)
    print('negative_connectedness rejected_two_2x2_components')
    pair = 0b00011
    high = (0b00111, 0b11100, 0b11100)
    assert sum((h & pair) == pair for h in high) == 1
    print('negative_pair_neighbours rejected_count 1')

    check_real_unitary('two_by_two', [
        [Q(3, 5), Q(4, 5)], [Q(4, 5), Q(-3, 5)]], 0)
    check_real_unitary('three_by_three_one_zero', [
        [Q(3, 5), Q(4, 5), Q(0)],
        [Q(12, 25), Q(-9, 25), Q(4, 5)],
        [Q(16, 25), Q(-12, 25), Q(-3, 5)]], 2)
    check_real_unitary('three_by_three_full', [
        [Q(1, 3), Q(-2, 3), Q(-2, 3)],
        [Q(-2, 3), Q(1, 3), Q(-2, 3)],
        [Q(-2, 3), Q(-2, 3), Q(1, 3)]], 3)
    check_real_unitary('four_by_four_excess_four', [
        [Q(3, 5), Q(4, 5), Q(0), Q(0)],
        [Q(0), Q(0), Q(3, 5), Q(4, 5)],
        [Q(12, 25), Q(-9, 25), Q(16, 25), Q(-12, 25)],
        [Q(16, 25), Q(-12, 25), Q(-12, 25), Q(9, 25)]], 4)

    counts = {}
    for excess in range(5):
        for m in range(2, 8):
            counts[m, excess] = len(enumerate_component(m, excess))
        print('excess', excess, 'm2..m7_counts',
              ','.join(str(counts[m, excess]) for m in range(2, 8)))

    assert [m for m in range(2, 8) if counts[m, 0]] == [2]
    assert all(counts[m, 1] == 0 for m in range(2, 8))
    assert [m for m in range(2, 8) if counts[m, 2]] == [3]
    assert [m for m in range(2, 8) if counts[m, 3]] == [3]
    assert counts[5, 4] == counts[7, 4] == 0
    assert counts[4, 4] > 0
    # Whole seven-row matrix: only excess allocations 4 or 2+2 remain;
    # 4 must occupy an odd component, and 2+2 consumes six rows.
    possible = set()
    def compose(rows_left, excess_left):
        if rows_left == 0:
            if excess_left == 0:
                possible.add(True)
            return
        for m in range(2, min(7, rows_left) + 1):
            for e in range(excess_left + 1):
                if counts[m, e]:
                    compose(rows_left - m, excess_left - e)
    compose(7, 4)
    assert not possible
    print('seven_by_seven_excess_four_compositions', len(possible))
    print('control_complete')


if __name__ == '__main__':
    main()
