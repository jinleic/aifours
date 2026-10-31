#!/usr/bin/env python3
"""Bounded overapproximation of index-two fibre/gcd obstructions.

The signatures divide original kernel indices; their retained prime support
preserves every nontrivial actual intersection gcd that is at most seven.
No model means no actual configuration satisfying these necessary conditions.
"""
from itertools import product
from math import gcd

SIG = tuple(
    2**e2 * 3**e3 * 5**e5 * 7**e7
    for e2, e3, e5, e7 in product(range(4), range(3), range(2), range(2))
)


def run(label, roles):
    choices = [
        [b for b in SIG if seven is None or (b % 7 == 0) == seven]
        for _, seven in roles
    ]
    counts = [0] * (len(roles) + 1)
    counts[0] = 1
    witness = None

    def visit(vals):
        nonlocal witness
        k = len(vals)
        if k == len(roles):
            if witness is None:
                witness = tuple(vals)
            return
        proper, _ = roles[k]
        for b in choices[k]:
            n = 2 * b if proper else b
            for j, prev_b in enumerate(vals):
                prev_proper, _ = roles[j]
                prev_n = 2 * prev_b if prev_proper else prev_b
                if gcd(n, prev_n) > 7:
                    break
                if (not proper or not prev_proper) and gcd(b, prev_b) == 1:
                    break
            else:
                counts[k + 1] += 1
                visit(vals + [b])

    visit([])
    print(f"{label}: partial_counts={counts}; terminal_models={counts[-1]}")
    if witness is not None:
        print(f"{label}: first abstract signature model={witness}")
    return counts[-1]


def main():
    assert len(SIG) == len(set(SIG)) == 48
    # Sun7 forces three seven indices. Proper pairs cannot both carry seven.
    a = run("no_proper_seven", ((True, False), (True, False),
                                (False, True), (False, True), (False, True)))
    b = run("one_proper_seven", ((True, True), (True, False),
                                 (False, True), (False, True), (False, None)))
    if a or b:
        raise SystemExit("FAIL: abstract model remains; no exclusion established")
    print("PASS: no abstract model for either C2 obstruction scenario")


if __name__ == "__main__":
    main()
