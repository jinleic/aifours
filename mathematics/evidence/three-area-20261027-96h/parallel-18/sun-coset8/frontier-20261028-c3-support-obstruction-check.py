#!/usr/bin/env python3
"""Exhaustively overapproximate the C3 fibre/index obstructions.

Signatures retain only 2, 3, 5, 7 with exponent caps 3, 2, 1, 1.
Every signature divides the original integer; actual counterconfigurations
map into these finite possibilities.  Thus zero abstract models is a sound
finite check of the stated necessary constraints, not a coset construction.
"""
from itertools import product
from math import gcd

SIGNATURES = tuple(
    2**e2 * 3**e3 * 5**e5 * 7**e7
    for e2, e3, e5, e7 in product(range(4), range(3), range(2), range(2))
)


def search(label, roles):
    # Each role is (proper_image, seven_divisible); None means unconstrained.
    candidates = tuple(
        tuple(v for v in SIGNATURES if seven is None or (v % 7 == 0) == seven)
        for _, seven in roles
    )
    counts = [0] * (len(roles) + 1)
    counts[0] = 1
    witness = None

    def visit(chosen):
        nonlocal witness
        k = len(chosen)
        if k == len(roles):
            if witness is None:
                witness = tuple(chosen)
            return
        proper, _ = roles[k]
        for b in candidates[k]:
            n = 3 * b if proper else b
            ok = True
            for j, earlier_b in enumerate(chosen):
                prior_proper, _ = roles[j]
                earlier_n = 3 * earlier_b if prior_proper else earlier_b
                if gcd(n, earlier_n) > 7:
                    ok = False
                    break
                # Full images overlap every proper-image fibre. Two full-image
                # cosets also share fibres. Actual disjoint cosets force gcd>=2.
                if not proper or not prior_proper:
                    if gcd(b, earlier_b) == 1:
                        ok = False
                        break
            if ok:
                counts[k + 1] += 1
                visit(chosen + [b])

    visit([])
    print(f"{label}: partial_counts={counts}; terminal_models={counts[-1]}")
    if witness is not None:
        print(f"{label}: first abstract signature model={witness}")
    return counts[-1]


def main():
    assert len(SIGNATURES) == len(set(SIGNATURES)) == 48
    # At least two proper labels, no proper 7-label; Sun7 forces three full
    # 7-labels.  Actual fibre disjointness supplies all cross/full gcd checks.
    no_proper_seven = search(
        "no_proper_seven",
        ((True, False), (True, False), (False, True), (False, True), (False, True)),
    )
    # One proper 7-label and another proper; two full 7-labels follow from
    # Sun7.  In the putative counterconfiguration there is one further full
    # label, either 7-divisible or not (indeed there are four).
    one_proper_seven = search(
        "one_proper_seven",
        ((True, True), (True, False), (False, True), (False, True), (False, None)),
    )
    if no_proper_seven or one_proper_seven:
        raise SystemExit("FAIL: abstract model remains; do not claim exclusion")
    print("PASS: no abstract model for either C3 obstruction scenario")


if __name__ == "__main__":
    main()
