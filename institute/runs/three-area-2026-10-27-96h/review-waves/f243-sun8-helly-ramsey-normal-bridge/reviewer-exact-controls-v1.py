#!/usr/bin/env python3
"""Reviewer-owned bounded finite controls; no author code or data imported."""
from itertools import combinations, combinations_with_replacement, product
from math import gcd
import signal
import sys


class Failure(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Failure(reason)


def expect_failure(name, reason, operation):
    try:
        operation()
    except Failure as exc:
        require(str(exc) == reason, f"{name}: wrong failure {exc}")
        print(f"NEGATIVE {name}: {reason}")
        return
    raise Failure(f"{name}: mutation unexpectedly accepted")


def all_subgroups(elements, identity, multiply):
    def generate(generators):
        seen = {identity}
        pending = [identity]
        while pending:
            x = pending.pop()
            for g in generators:
                y = multiply(x, g)
                if y not in seen:
                    seen.add(y)
                    pending.append(y)
        return frozenset(seen)

    first = frozenset({identity})
    seen = {first}
    pending = [first]
    while pending:
        subgroup = pending.pop()
        for x in elements:
            if x not in subgroup:
                enlarged = generate(tuple(subgroup) + (x,))
                if enlarged not in seen:
                    seen.add(enlarged)
                    pending.append(enlarged)
    return seen


def dihedral_product(p, m):
    elements = list(product(range(p), range(2), range(m)))
    identity = (0, 0, 0)

    def multiply(x, y):
        a, b, c = x
        d, e, f = y
        return ((a + (1 if b == 0 else -1) * d) % p, (b + e) % 2, (c + f) % m)

    def inverse(x):
        a, b, c = x
        return (((-1 if b == 0 else 1) * a) % p, b, (-c) % m)

    return elements, identity, multiply, inverse


def check_fibre_identity():
    elements, identity, multiply, inverse = dihedral_product(3, 2)
    kernel = frozenset(x for x in elements if x[2] == 0)
    subgroups = all_subgroups(elements, identity, multiply)
    trials = 0
    for subgroup in subgroups:
        image = {x[2] for x in subgroup}
        intersection = subgroup & kernel
        a = 2 // len(image)
        b = len(kernel) // len(intersection)
        require(len(elements) // len(subgroup) == a * b, "INDEX_PRODUCT")
        for g in elements:
            original = {multiply(g, u) for u in subgroup}
            for t in elements:
                fibre = {multiply(n, t) for n in kernel}
                intersection_fibre = original & fibre
                if not intersection_fibre:
                    continue
                x = min(intersection_fibre)
                tinv = inverse(t)
                lhs = {multiply(y, tinv) for y in intersection_fibre}
                conjugate = {multiply(multiply(t, k), tinv) for k in intersection}
                rhs = {multiply(multiply(x, tinv), k) for k in conjugate}
                require(lhs == rhs, "FIBRE_IDENTITY")
                require(conjugate <= kernel and len(conjugate) == len(intersection), "CONJUGATE_KERNEL")
                trials += 1
    print(f"FIBRE D6xC2: subgroups={len(subgroups)} nonempty_fibres={trials}")

    # A non-normal reflection subgroup, with a noncentral choice of t.
    s = (0, 1, 0)
    subgroup = frozenset({identity, s})
    t = (1, 0, 0)
    tinv = inverse(t)
    actual = {multiply(u, tinv) for u in subgroup}
    mutant = {multiply(tinv, u) for u in subgroup}
    expect_failure("drop_conjugation", "MISSING_CONJUGATION",
                   lambda: require(actual == mutant, "MISSING_CONJUGATION"))


def has_monochromatic_triangle(n, mask):
    edges = list(combinations(range(n), 2))
    lookup = {edge: i for i, edge in enumerate(edges)}
    for a, b, c in combinations(range(n), 3):
        colors = [(mask >> lookup[e]) & 1 for e in ((a, b), (a, c), (b, c))]
        if colors[0] == colors[1] == colors[2]:
            return True
    return False


def check_ramsey():
    avoiding = {}
    examples = {}
    for n in (5, 6):
        edge_count = n * (n - 1) // 2
        examples[n] = [mask for mask in range(1 << edge_count)
                       if not has_monochromatic_triangle(n, mask)]
        avoiding[n] = len(examples[n])
    require(avoiding[5] == 12, "FIVE_VERTEX_COUNT")
    require(avoiding[6] == 0, "SIX_VERTEX_RAMSEY")
    print(f"RAMSEY labelled_graphs: n5_avoiding={avoiding[5]} n6_avoiding={avoiding[6]}")
    expect_failure("ramsey_five_vertices", "NO_MONOCHROMATIC_TRIANGLE",
                   lambda: require(has_monochromatic_triangle(5, examples[5][0]),
                                   "NO_MONOCHROMATIC_TRIANGLE"))


def check_crt():
    families = 0
    compatible_count = 0
    for modulus in range(1, 13):
        cosets = [(a, c) for a in range(1, modulus + 1) if modulus % a == 0
                  for c in range(a)]
        for family in combinations_with_replacement(cosets, 4):
            compatible = all((c - d) % gcd(a, b) == 0
                             for (a, c), (b, d) in combinations(family, 2))
            witness = any(all((x - c) % a == 0 for a, c in family)
                          for x in range(modulus))
            require(compatible == witness, "CRT_PAIRWISE_VS_GLOBAL")
            families += 1
            compatible_count += compatible
    print(f"CRT finite cyclic: M=1..12 four_label_families={families} compatible={compatible_count}")
    expect_failure("incompatible_crt", "PAIR_CONFLICT",
                   lambda: require((0 - 1) % gcd(2, 2) == 0, "PAIR_CONFLICT"))
    # A class modulo L does not canonically select a residue modulo M when L|M.
    require({x for x in range(6) if x % 2 == 0} == {0, 2, 4}, "CRT_LIFTS")
    expect_failure("reverse_crt_class_map", "NO_UNIQUE_LIFT",
                   lambda: require((0 - 2) % 2 != 0 or (0 - 2) % 6 == 0,
                                   "NO_UNIQUE_LIFT"))


def cosets_for(elements, subgroups, multiply):
    result = []
    for subgroup in subgroups:
        index = len(elements) // len(subgroup)
        seen = set()
        for x in elements:
            coset = frozenset(multiply(x, y) for y in subgroup)
            if coset not in seen:
                seen.add(coset)
                result.append((index, coset))
        require(len(seen) == index, "COSET_PARTITION_COUNT")
    return result


def bad_triple_count(cosets):
    count = 0
    bad_pairs = 0
    for i, (a, x) in enumerate(cosets):
        for j in range(i + 1, len(cosets)):
            b, y = cosets[j]
            if gcd(a, b) > 7 or not x.isdisjoint(y):
                continue
            bad_pairs += 1
            for c, z in cosets[j + 1:]:
                if gcd(a, c) <= 7 and gcd(b, c) <= 7 and x.isdisjoint(z) and y.isdisjoint(z):
                    count += 1
    return bad_pairs, count


def check_factors_and_product():
    elements, identity, multiply, _ = dihedral_product(11, 1)
    dsubgroups = all_subgroups(elements, identity, multiply)
    dcosets = cosets_for(elements, dsubgroups, multiply)
    cyc = list(range(22))
    add = lambda a, b: (a + b) % 22
    csubgroups = all_subgroups(cyc, 0, add)
    ccosets = cosets_for(cyc, csubgroups, add)
    for label, universe, subgroups, cosets in (
            ("D22", elements, dsubgroups, dcosets),
            ("C22", cyc, csubgroups, ccosets)):
        require(sum(len(universe) // len(h) == 2 for h in subgroups) == 1,
                f"{label}_UNIQUE_INDEX_TWO")
        twos = [x for index, x in cosets if index == 2]
        require(len(twos) == 2 and twos[0].isdisjoint(twos[1]) and
                twos[0] | twos[1] == set(universe), f"{label}_INDEX_TWO_PAIR")
        pairs, triples = bad_triple_count(cosets)
        require(triples == 0, f"{label}_BAD_TRIPLE")
        print(f"FACTORS {label}: subgroups={len(subgroups)} cosets={len(cosets)} bad_pairs={pairs} bad_triples={triples}")

    big, _, mul, _ = dihedral_product(11, 22)
    subgroup = {(a, 0, 2 * c) for a in range(11) for c in range(11)}
    representatives = [(0, b, c) for b, c in product(range(2), range(2))]
    cosets = [{mul(g, h) for h in subgroup} for g in representatives]
    require(len(big) == 484 and len(subgroup) == 121, "PRODUCT_ORDER")
    require(all(x.isdisjoint(y) for x, y in combinations(cosets, 2)), "PRODUCT_DISJOINT")
    require(set.union(*cosets) == set(big), "PRODUCT_COVER")
    require(gcd(4, 4) <= 7, "PRODUCT_GCD")
    print("PRODUCT D22xC22: order=484 subgroup=121 four_index_4_cosets=4")


def check_shortcuts():
    seven_cosets = [{(i, y) for y in range(7)} for i in range(7)]
    require(all(x.isdisjoint(y) for x, y in combinations(seven_cosets, 2)), "C7_ORIGINAL_DISJOINT")
    projections = [{y for _, y in coset} for coset in seven_cosets]
    require(all(x == set(range(7)) for x in projections), "C7_PROJECTION")
    expect_failure("originals_project_disjointly", "PROJECTED_OVERLAP",
                   lambda: require(projections[0].isdisjoint(projections[1]), "PROJECTED_OVERLAP"))
    expect_failure("sun8_bounds_fibre_by_two", "FIBRE_EXCEEDS_TWO",
                   lambda: require(len(seven_cosets) <= 2, "FIBRE_EXCEEDS_TWO"))

    points = set(product(range(5), repeat=2))
    lines = [{(x, y) for x, y in points if y == 0},
             {(x, y) for x, y in points if x == 0},
             {(x, y) for x, y in points if (x + y) % 5 == 1}]
    require(all(len(line) == 5 for line in lines), "F5_LINE_SIZE")
    require(all(x & y for x, y in combinations(lines, 2)), "F5_PAIRWISE_INTERSECTION")
    require(not set.intersection(*lines), "F5_EMPTY_TRIPLE")
    originals = [{(i, x, y) for x, y in line} for i, line in enumerate(lines)]
    require(all(x.isdisjoint(y) for x, y in combinations(originals, 2)), "F5_LAYER_DISJOINT")
    require(125 // len(originals[0]) == 25 and gcd(25, 25) == 25, "F5_ORIGINAL_INDEX")
    expect_failure("pairwise_means_global", "NON_HELLY_TRIANGLE",
                   lambda: require(bool(set.intersection(*lines)), "NON_HELLY_TRIANGLE"))
    print("SHORTCUTS C7xC7: seven disjoint originals, identical quotient images")
    print("SHORTCUTS C5xF5^2: non-Helly quotient triple, original indices=25")


def main():
    check_fibre_identity()
    check_ramsey()
    check_crt()
    check_factors_and_product()
    check_shortcuts()
    print("CONTROLS COMPLETE; finite samples do not prove infinite or parametric claims")


def timed_out(_signum, _frame):
    raise TimeoutError


signal.signal(signal.SIGALRM, timed_out)
signal.alarm(110)
try:
    main()
except TimeoutError:
    print("UNKNOWN: control time cap reached", file=sys.stderr)
    sys.exit(124)
except Failure as exc:
    print(f"CONTROL FAILURE: {exc}", file=sys.stderr)
    sys.exit(1)
