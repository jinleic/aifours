#!/usr/bin/env python3
"""Reviewer-owned exact examples, not an MOQLS witness or author-code replay."""
from fractions import Fraction


def gf8_mul(a, b):
    result = 0
    for _ in range(3):
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return result


def labels(point):
    x, y = point
    return (x, y, *(y ^ gf8_mul(a, x) for a in (1, 2, 3)))


def rank(rows):
    matrix = [[Fraction(v) for v in row] for row in rows]
    m, n = len(matrix), len(matrix[0])
    pivot_row = 0
    for column in range(n):
        pivot = next((i for i in range(pivot_row, m) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        for i in range(pivot_row + 1, m):
            if matrix[i][column]:
                ratio = matrix[i][column] / matrix[pivot_row][column]
                for j in range(column, n):
                    matrix[i][j] -= ratio * matrix[pivot_row][j]
        pivot_row += 1
        if pivot_row == m:
            break
    return pivot_row


def require_five(row):
    if sum(row) != 5:
        raise ValueError("row-incidence is not five")


def require_gram(y):
    for i in range(8):
        for j in range(8):
            if sum(row[i] * row[j] for row in y) != 120 * (8 * (i == j) - 1):
                raise ValueError("scaled cross-Gram mismatch")


def expected_failure(label, fn, reason):
    try:
        fn()
    except ValueError as exc:
        if str(exc) != reason:
            raise
        print(f"NEGATIVE {label}: rejected: {exc}")
        return
    raise RuntimeError(f"negative {label} unexpectedly passed")


points = [(x, y) for x in range(8) for y in range(8)]
for i, p in enumerate(points):
    for q in points[i + 1:]:
        assert sum(a == b for a, b in zip(labels(p), labels(q))) <= 1
fixed = [(x, gf8_mul(4, x)) for x in range(8)]
assert len(set(fixed)) == 8
assert all(len({labels(p)[j] for p in fixed}) == 8 for j in range(5))
component = [p for p in points if p not in fixed]
incidence = [[int(any(a == b for a, b in zip(labels(x), labels(f))))
              for f in fixed] for x in component]
for row in incidence:
    require_five(row)
assert all(sum(row[j] for row in incidence) == 35 for j in range(8))
assert all(sum(row[i] * row[j] for row in incidence) == 20
           for i in range(8) for j in range(i + 1, 8))
y = [[5 - 8 * v for v in row] for row in incidence]
require_gram(y)
assert rank(y) == 7
assert Fraction(sum(v * v for row in y for v in row), 64 * 64) == Fraction(105, 64)
print("POSITIVE synthetic five-net: row=5 col=35 pair=20; scaled X^T X=120(8I-J); rank(X)=7; ||X||^2=105/64")
wrong_incidence = incidence[0][:]
wrong_incidence[0] ^= 1
expected_failure("flipped incidence", lambda: require_five(wrong_incidence),
                 "row-incidence is not five")
wrong_y = [row[:] for row in y]
wrong_y[0][0] += 1
expected_failure("perturbed cross block", lambda: require_gram(wrong_y),
                 "scaled cross-Gram mismatch")


def basis_sum_rank(blocks):
    n = sum(blocks)
    u = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    start = 0
    for k in blocks:
        for i in range(start, start + k):
            for j in range(start, start + k):
                u[i][j] = Fraction(int(i == j)) - Fraction(2, k)
        start += k
    vectors = [[Fraction(int(i == j)) for i in range(n)] for j in range(n)]
    vectors += [[u[i][j] for i in range(n)] for j in range(n)]
    projectors = [[v[i] * v[j] for i in range(n) for j in range(n)]
                  for v in vectors]
    return rank(projectors)


for blocks, expected in [((6,), 11), ((3, 3), 10), ((7,), 13), ((4, 3), 12)]:
    got = basis_sum_rank(blocks)
    if got != expected:
        raise ValueError(f"block-rank mismatch {blocks}: {got} != {expected}")
    print(f"POSITIVE rational transition blocks {blocks}: projector-sum rank {got}")


def wrong_pivot_expectation():
    if basis_sum_rank((6,)) != 10:
        raise ValueError("connected six-block is not split rank ten")


expected_failure("misclassified connected pivot", wrong_pivot_expectation,
                 "connected six-block is not split rank ten")
print("DONE: examples and intended-reason negatives; not a general proof or existence witness")
