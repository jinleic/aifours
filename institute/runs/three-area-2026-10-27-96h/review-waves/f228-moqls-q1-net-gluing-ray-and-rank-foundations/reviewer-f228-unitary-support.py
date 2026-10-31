#!/usr/bin/env python3
"""Enumerate necessary support conditions for 3x3 unitary matrices."""
from itertools import combinations


def supports(mask):
    return [[bool(mask & (1 << (3 * r + c))) for c in range(3)] for r in range(3)]


def reason(mask):
    rows = supports(mask)
    cols = [list(col) for col in zip(*rows)]
    if any(sum(line) < 2 for line in rows + cols):
        return "singleton-or-empty-row-or-column"
    for lines in (rows, cols):
        for a, b in combinations(lines, 2):
            if sum(x and y for x, y in zip(a, b)) == 1:
                return "single-common-nonzero-for-orthogonal-pair"
    return "necessary-conditions-pass"


full = (1 << 9) - 1
assert reason(full) == "necessary-conditions-pass"
assert reason(full ^ (1 << 0)) == "necessary-conditions-pass"
assert reason(full ^ (1 << 0) ^ (1 << 1)) == "singleton-or-empty-row-or-column"
assert reason(full ^ (1 << 0) ^ (1 << 4)) == "single-common-nonzero-for-orthogonal-pair"
hist = {}
for mask in range(1 << 9):
    if reason(mask) == "necessary-conditions-pass":
        zeros = 9 - bin(mask).count("1")
        hist[zeros] = hist.get(zeros, 0) + 1
assert hist == {1: 9, 0: 1}
print("necessary support conditions: zero-count histogram", sorted(hist.items()))
print("negatives rejected: singleton-or-empty-row-or-column; single-common-nonzero-for-orthogonal-pair")
print("No existence conclusion follows from support conditions alone.")
