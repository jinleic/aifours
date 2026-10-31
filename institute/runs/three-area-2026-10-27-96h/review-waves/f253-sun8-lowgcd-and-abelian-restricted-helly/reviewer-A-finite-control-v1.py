#!/usr/bin/env python3
"""Exact finite F_2 controls for the f253-A review; no source imports."""
from itertools import combinations
from math import gcd


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def span1(generator):
    require(generator != 0, "ZERO_GENERATOR")
    return frozenset((0, generator))


def translate(v, subgroup):
    return frozenset(v ^ h for h in subgroup)


def project(points):
    return frozenset(v & 3 for v in points)


def partition_guard(cosets):
    for i, j in combinations(range(len(cosets)), 2):
        if cosets[i] & cosets[j]:
            raise ValueError(f"OVERLAP_C{i + 1}_C{j + 1}")
    require(frozenset().union(*cosets) == frozenset(range(8)), "NOT_ALL_V")


def nonhelly_guard(images):
    for i, j in combinations(range(3), 2):
        require(bool(images[i] & images[j]), f"PAIR_{i + 1}_{j + 1}_DISJOINT")
    require(not (images[0] & images[1] & images[2]), "TRIPLE_NONEMPTY")


def expect_rejection(reason, fn):
    try:
        fn()
    except ValueError as exc:
        require(str(exc) == reason, f"WRONG_NEGATIVE_REASON:{exc}")
        print("NEGATIVE_REJECT", reason)
        return
    raise ValueError(f"NEGATIVE_ACCEPTED:{reason}")


def all_subspaces(dimension):
    size = 1 << dimension
    result = []
    for membership in range(1 << (size - 1)):
        subset = frozenset([0] + [v for v in range(1, size) if membership & (1 << (v - 1))])
        if all((a ^ b) in subset for a in subset for b in subset):
            result.append(subset)
    return result


def packing_counts(dimension):
    size = 1 << dimension
    subspaces = all_subspaces(dimension)
    cosets = set()
    for subgroup in subspaces:
        index = size // len(subgroup)
        for v in range(size):
            coset = translate(v, subgroup)
            mask = sum(1 << point for point in coset)
            cosets.add((mask, index))
    cosets = sorted(cosets)
    counts = [0] * (size + 1)

    def visit(start, occupied, indices):
        counts[len(indices)] += 1
        for i in range(start, len(cosets)):
            mask, index = cosets[i]
            if occupied & mask or any(gcd(index, previous) > 7 for previous in indices):
                continue
            visit(i + 1, occupied | mask, indices + (index,))

    visit(0, 0, ())
    maximum = max(i for i, count in enumerate(counts) if count)
    print(f"DIM={dimension} SUBGROUPS={len(subspaces)} DISTINCT_COSETS={len(cosets)} COUNTS_BY_SIZE={counts} MAX={maximum}")
    return maximum


def main():
    subgroups = [span1(g) for g in (2, 5, 3, 4)]
    representatives = (0, 4, 6, 3)
    cosets = [translate(v, h) for v, h in zip(representatives, subgroups)]
    expected_cosets = [frozenset((0, 2)), frozenset((4, 1)), frozenset((6, 5)), frozenset((3, 7))]
    require(cosets == expected_cosets, "WRONG_DISPLAYED_COSET")
    partition_guard(cosets)
    images = list(map(project, cosets))
    expected_images = [frozenset((0, 2)), frozenset((0, 1)), frozenset((2, 1)), frozenset((3,))]
    require(images == expected_images, "WRONG_QUOTIENT_IMAGE")
    nonhelly_guard(images)
    require([images[0] & images[1], images[0] & images[2], images[1] & images[2]] == [frozenset((0,)), frozenset((2,)), frozenset((1,))], "WRONG_PAIR_INTERSECTION")
    require(all(not (images[3] & image) for image in images[:3]), "FOURTH_IMAGE_OVERLAP")
    line = frozenset((0, 4))
    pairs = [(4 // len(project(h)), 2 // len(h & line)) for h in subgroups]
    require(pairs == [(2, 2), (2, 2), (2, 2), (4, 1)], "WRONG_IMAGE_FIBER_INDICES")
    require(all(a * b == 4 for a, b in pairs), "WRONG_PRODUCT_INDEX")
    expected_fibers = {
        0: {1: (0,), 2: (1,)},
        1: {2: (0,), 3: (1,)},
        2: {1: (0,), 3: (1,)},
        3: {4: (0, 1)},
    }
    actual_fibers = {}
    for q in range(4):
        actual_fibers[q] = {i + 1: tuple(sorted(v >> 2 for v in c if (v & 3) == q)) for i, c in enumerate(cosets) if q in project(c)}
    require(actual_fibers == expected_fibers, "WRONG_QUOTIENT_FIBER_TABLE")
    print("COSETS", [sorted(c) for c in cosets])
    print("QUOTIENT_IMAGES", [sorted(a) for a in images])
    print("QUOTIENT_FIBER_INDICES", pairs)
    print("FIBERS", actual_fibers)
    for dimension, expected in ((1, 2), (2, 4), (3, 4)):
        require(packing_counts(dimension) == expected, f"WRONG_B7_DIM_{dimension}")
    mutated_cosets = list(cosets)
    mutated_cosets[1] = translate(representatives[1], span1(1))
    expect_rejection("OVERLAP_C2_C3", lambda: partition_guard(mutated_cosets))
    mutated_images = list(images)
    mutated_images[2] = project(translate(0, subgroups[2]))
    expect_rejection("TRIPLE_NONEMPTY", lambda: nonhelly_guard(mutated_images))
    print("ALL_CONTROL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
