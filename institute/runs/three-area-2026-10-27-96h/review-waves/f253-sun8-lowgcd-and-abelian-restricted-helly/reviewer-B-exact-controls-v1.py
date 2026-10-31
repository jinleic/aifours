#!/usr/bin/env python3
"""Reviewer-owned finite controls, written from definitions; imports no author code."""
from itertools import combinations, permutations, product
from math import gcd


class Rejected(Exception):
    pass


def demand(condition, reason):
    if not condition:
        raise Rejected(reason)


def negative(name, expected, action):
    try:
        action()
    except Rejected as exc:
        if str(exc) != expected:
            raise RuntimeError(f"{name}: wrong rejection: {exc}") from exc
        print(f"NEGATIVE {name}: REJECTED {expected}")
    else:
        raise RuntimeError(f"{name}: expected rejection {expected}")


def pcompose(p, q):
    return tuple(p[q[i]] for i in range(3))


def pinverse(p):
    return tuple(p.index(i) for i in range(3))


def mul(x, y):
    return (pcompose(x[0], y[0]), x[1] ^ y[1])


def inv(x):
    return (pinverse(x[0]), x[1])


def left_cosets(group, subgroup):
    return {frozenset(mul(g, h) for h in subgroup) for g in group}


def gcd_controls():
    count = 0
    overlap_count = 0
    for a, b, c, d in product(range(1, 19), repeat=4):
        divisor = gcd(a, c) * gcd(b, d)
        total = gcd(a * b, c * d)
        demand(total % divisor == 0, "DIVISIBILITY_FAILURE")
        count += 1
        if gcd(b, d) >= 2 and total <= 7:
            demand(gcd(a, c) <= 3, "OVERLAP_GCD_BOUND_FAILURE")
            overlap_count += 1
    print(f"POSITIVE gcd-product: {count} quadruples; overlap bound: {overlap_count} applicable")
    a, b, c, d = 2, 3, 3, 2
    negative("replace divisibility by equality", "PRODUCT_NEED_NOT_EQUAL_GCD",
             lambda: demand(gcd(a, c) * gcd(b, d) == gcd(a * b, c * d),
                            "PRODUCT_NEED_NOT_EQUAL_GCD"))


def nonabelian_controls():
    ident = (0, 1, 2)
    transposition = (1, 0, 2)
    cycle = (1, 2, 0)
    s3 = {(p, 0) for p in permutations(range(3))}
    full = {(p, b) for p in permutations(range(3)) for b in range(2)}
    kernel = s3
    k = {(ident, 0), (transposition, 0)}
    t = (cycle, 1)
    n = (transposition, 0)
    conjugate = {mul(mul(t, h), inv(t)) for h in k}
    c0 = {mul(t, h) for h in k}
    nt = mul(n, t)
    c1 = {mul(nt, h) for h in k}
    demand(not (c0 & c1), "FIBRES_NOT_DISJOINT")
    fibre0 = {mul(x, inv(t)) for x in c0 if x[1] == t[1]}
    fibre1 = {mul(x, inv(t)) for x in c1 if x[1] == t[1]}
    demand(fibre0 == conjugate, "FIRST_FIBRE_ORIENTATION")
    demand(fibre1 == {mul(n, h) for h in conjugate}, "SECOND_FIBRE_ORIENTATION")
    demand(conjugate <= kernel and len(full) // len(k) == 6, "INDEX_ERROR")
    demand((2, len(kernel) // len(k), 2 * len(kernel) // len(k)) == (2, 3, 6),
           "PRODUCT_INDEX_ERROR")
    demand(gcd(6, 6) <= 7, "ORIGINAL_GCD_ERROR")
    print("POSITIVE S3 x C2: two disjoint actual index-6 cosets over one quotient point; a=2 b=3; conjugated fibres")
    negative("omit conjugation", "WRONG_FIBRE_SUBGROUP",
             lambda: demand(fibre0 == k, "WRONG_FIBRE_SUBGROUP"))

    p = {(ident, 0), ((1, 2, 0), 0), ((2, 0, 1), 0)}
    r = k
    ps = left_cosets(s3, p)
    rs = left_cosets(s3, r)
    demand(len(ps) == 2 and len(rs) == 3, "COPRIME_COSSET_COUNT")
    demand(all(len(x & y) == 1 for x in ps for y in rs), "COPRIME_COSSET_INTERSECTION")
    print("POSITIVE S3 coprime index 2 and 3: all 6 prescribed pairs intersect uniquely")
    singleton0, singleton1 = {0}, {1}
    negative("remove coprime hypothesis", "NO_COMMON_POINT",
             lambda: demand(bool(singleton0 & singleton1), "NO_COMMON_POINT"))


def triangle(modulus):
    points = set(product(range(modulus), repeat=2))
    a = {(x, y) for x, y in points if y == 0}
    b = {(x, y) for x, y in points if x == 0}
    c = {(x, y) for x, y in points if (x + y) % modulus == 1}
    return points, (a, b, c)


def helly_controls():
    cosets = ({0}, {1}, {0, 1})
    checked = 0
    for size in range(1, 4):
        for family in combinations(cosets, size):
            if all(x & y for x, y in combinations(family, 2)):
                demand(bool(set.intersection(*family)), "TWO_POINT_HELLY_FAILURE")
                checked += 1
    print(f"POSITIVE two-point Helly: {checked} pairwise-intersecting distinct-coset families")
    for p in (2, 3):
        universe, family = triangle(p)
        demand(all(x & y for x, y in combinations(family, 2)), "NEGATIVE_NOT_PAIRWISE_INTERSECTING")
        demand(all(len(universe) // len(x) == p for x in family), "NEGATIVE_WRONG_INDEX")
        negative(f"omit index-{4 if p == 2 else 3} exclusion (abstract quotient F_{p}^2)",
                 "EMPTY_TRIPLE", lambda: demand(bool(set.intersection(*family)), "EMPTY_TRIPLE"))
    negative("unique lift from mod 2 to mod 6", "MULTIPLE_LIFTS",
             lambda: demand(len({x % 6 for x in (0, 2, 4)}) == 1, "MULTIPLE_LIFTS"))


def binary_subgroups(bits):
    if bits == 1:
        return [{0}, {0, 1}]
    if bits == 2:
        return [{0}, {0, 1}, {0, 2}, {0, 3}, {0, 1, 2, 3}]
    raise ValueError("unsupported binary rank")


def odd_subgroups(p):
    zero = {(0, 0)}
    lines = [{(x, (m * x) % p) for x in range(p)} for m in range(p)]
    lines.append({(0, y) for y in range(p)})
    whole = set(product(range(p), repeat=2))
    spaces = [zero, *lines, whole]
    demand(len({frozenset(s) for s in spaces}) == p + 3, "DUPLICATE_VECTOR_SUBSPACE")
    return spaces


def all_abelian_cosets(bits, p):
    universe = list(product(range(1 << bits), range(p), range(p)))
    position = {x: i for i, x in enumerate(universe)}
    nodes = []
    subgroups = 0
    for binary in binary_subgroups(bits):
        for odd in odd_subgroups(p):
            subgroup = [(b, x, y) for b in binary for x, y in odd]
            subgroups += 1
            unseen = set(universe)
            while unseen:
                b0, x0, y0 = next(iter(unseen))
                coset = {(b0 ^ b, (x0 + x) % p, (y0 + y) % p) for b, x, y in subgroup}
                demand(coset <= unseen, "COSET_PARTITION_FAILURE")
                unseen.difference_update(coset)
                mask = sum(1 << position[x] for x in coset)
                nodes.append((len(universe) // len(subgroup), mask))
    return universe, subgroups, nodes


def maximum_bad_packing(nodes, p):
    pure = [node for node in nodes if node[0] % p]
    high = [node for node in nodes if node[0] % p == 0]
    partials = []
    for size in range(len(pure) + 1):
        for family in combinations(pure, size):
            if all(not (x[1] & y[1]) and gcd(x[0], y[0]) <= 7
                   for x, y in combinations(family, 2)):
                union = 0
                for _, mask in family:
                    union |= mask
                partials.append((union, tuple(index for index, _ in family)))
    best = max((len(indices) for _, indices in partials), default=0)
    for index, mask in high:
        for union, indices in partials:
            if not (mask & union) and all(gcd(index, other) <= 7 for other in indices):
                best = max(best, len(indices) + 1)
    # Two high indices are both divisible by p > 7 and cannot coexist.
    return best, len(pure), len(high), len(partials)


def example_controls():
    p = 11
    q_points, q_subgroups, q_nodes = all_abelian_cosets(1, p)
    g_points, g_subgroups, g_nodes = all_abelian_cosets(2, p)
    demand((q_subgroups, len(q_nodes)) == (28, 762), "Q_ENUMERATION_COUNT")
    demand((g_subgroups, len(g_nodes)) == (70, 2794), "G_ENUMERATION_COUNT")
    demand(not any(index in (3, 4) for index, _ in q_nodes), "Q_EXCLUDED_INDEX")
    qmax, qpure, qhigh, qpartials = maximum_bad_packing(q_nodes, p)
    gmax, gpure, ghigh, gpartials = maximum_bad_packing(g_nodes, p)
    demand(qmax == 2 and gmax == 4, "BAD_PACKING_MAXIMUM")
    print(f"POSITIVE p=11 exhaustive Q: {q_subgroups} subgroups, {len(q_nodes)} cosets, pure/high={qpure}/{qhigh}, pure families={qpartials}, B7=2")
    print(f"POSITIVE p=11 exhaustive G: {g_subgroups} subgroups, {len(g_nodes)} cosets, pure/high={gpure}/{ghigh}, pure families={gpartials}, B7=4")
    demand(len(q_points) == 242 and len(g_points) == 484, "UNIVERSE_SIZE")
    lines = [
        {q for q in q_points if q[2] == 0},
        {q for q in q_points if q[1] == 0},
        {q for q in q_points if (q[1] + q[2]) % p == 1},
    ]
    demand(all(len(x) == 22 for x in lines), "EXAMPLE_LINE_INDEX")
    demand([len(x & y) for x, y in combinations(lines, 2)] == [2, 2, 2], "EXAMPLE_PAIR_OVERLAP")
    demand(not set.intersection(*lines), "EXAMPLE_TRIPLE_NOT_EMPTY")
    negative("non-Helly p-line images satisfy low-gcd overlap constraint", "QUOTIENT_GCD_EXCEEDS_THREE",
             lambda: demand(gcd(11, 11) <= 3, "QUOTIENT_GCD_EXCEEDS_THREE"))
    print("POSITIVE p=11: actual quotient line cosets index 11, pair overlaps 2 points, triple empty")
    repeated = [2] * 100
    demand(all(gcd(x, y) == 2 for x, y in combinations(repeated, 2)), "REPEATED_INDEX_GCD")
    negative("finite bound 99 when repetition is admitted", "REPEATED_LABELS_EXCEED_BOUND",
             lambda: demand(len(repeated) <= 99, "REPEATED_LABELS_EXCEED_BOUND"))
    print("SCOPE repeated labels: arithmetic only; no external J7 definition imported")


def main():
    gcd_controls()
    nonabelian_controls()
    helly_controls()
    example_controls()
    print("ALL REVIEWER-OWNED BOUNDED CONTROLS COMPLETE")


if __name__ == "__main__":
    main()
