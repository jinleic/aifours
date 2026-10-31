#!/usr/bin/env python3
"""Overapproximate all 8-label Sun7-to-P7 necessary prime-support patterns."""
from itertools import combinations_with_replacement
from math import gcd, prod

P = (2, 3, 5, 7)
S = sorted(prod(p for j, p in enumerate(P) if mask & (1 << j))
           for mask in range(1, 16))
count = [0] * 9
seven_patterns = 0
bad = 0
example = None


def walk(vals, start):
    global seven_patterns, bad, example
    count[len(vals)] += 1
    if len(vals) == 8:
        num7 = sum(x % 7 == 0 for x in vals)
        if num7 < 3:
            return
        seven_patterns += 1
        if num7 != 8:
            bad += 1
            example = vals
        return
    for j in range(start, len(S)):
        x = S[j]
        if all(2 <= gcd(x, y) <= 7 for y in vals):
            walk(vals + (x,), j)


walk((), 0)
print("partial_multiset_counts:", count)
print("eight_label_patterns_with_at_least_three_sevens:", seven_patterns)
print("patterns_with_at_least_one_nonseven:", bad)
if bad:
    print("first_counterpattern:", example)
    raise SystemExit("FAIL: support counterpattern exists")
print("PASS: every eligible eight-label support multiset is seven-divisible")
