#!/usr/bin/env python3
"""Exact, reduction-based exhaustive Sun8 check for A7 and GL3(2).

Requires the already available NumPy. All group/proof arithmetic is integral.
Builds each group from its definition, enumerates ALL subgroups up to conjugacy
by cyclic extension, expands the classes, enumerates every feasible eight-index
multiset, and checks every six-family of disjoint index-seven cosets. It uses
two elementary written lemmas, not Sun7/R8: coprime-index cosets intersect; a
coset inside a coset of L translates to a coset of a subgroup of L. Thus this is
a reduced exhaustive check, NOT a direct scan of all eight-coset subsets.
No input certificate, old checker, network, subprocess, or filesystem output.
"""
from collections import Counter
from itertools import permutations, product
from math import gcd
import hashlib
import json
import numpy as np


class CheckError(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise CheckError(reason)


def even(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 == 0


def linear_group():
    vectors = [v for v in product((0, 1), repeat=3) if any(v)]
    labels = {v: i for i, v in enumerate(vectors)}
    result = []
    for entries in product((0, 1), repeat=9):
        images = [tuple(sum(entries[3 * r + c] * v[c] for c in range(3)) % 2
                        for r in range(3)) for v in vectors]
        if len(set(images)) == 7 and all(any(v) for v in images):
            result.append(tuple(labels[v] for v in images))
    return result


def group_table(elements):
    elements = sorted(set(elements))
    degree, size = len(elements[0]), len(elements)
    points = np.array(elements, dtype=np.int64)
    weights = degree ** np.arange(degree, dtype=np.int64)
    lookup = np.full(degree ** degree, -1, dtype=np.int32)
    lookup[points @ weights] = np.arange(size, dtype=np.int32)
    multiplication = np.empty((size, size), dtype=np.int32)
    for i in range(size):
        multiplication[i] = lookup[points[i][points] @ weights]
    require(bool((multiplication >= 0).all()), "GROUP_NOT_CLOSED")
    identity = int(lookup[np.arange(degree, dtype=np.int64) @ weights])
    require(identity >= 0, "GROUP_IDENTITY_MISSING")
    rows, columns = np.nonzero(multiplication == identity)
    require(len(rows) == size and len(set(rows.tolist())) == size, "GROUP_INVERSE_FAILURE")
    inverses = np.empty(size, dtype=np.int32)
    inverses[rows] = columns
    return points, multiplication, identity, inverses


def subgroup_key(subgroup):
    return np.packbits(subgroup, bitorder="little").tobytes()


def generate(multiplication, identity, generators):
    size = len(multiplication)
    seen = np.zeros(size, dtype=bool)
    seen[identity] = True
    frontier = np.array([identity], dtype=np.int32)
    generators = np.array(sorted(set(generators)), dtype=np.int32)
    while frontier.size and generators.size:
        following = multiplication[np.ix_(frontier, generators)].ravel()
        following = np.unique(following[~seen[following]])
        seen[following] = True
        frontier = following
    return seen


def subgroup_lattice(multiplication, identity, inverses):
    size = len(multiplication)
    cyclic = {}
    for g in range(size):
        subgroup = generate(multiplication, identity, [g])
        cyclic.setdefault(subgroup_key(subgroup), g)
    known, representatives = {}, []

    def add_class(generators, subgroup):
        class_id = len(representatives)
        representatives.append((generators, subgroup))
        members = np.flatnonzero(subgroup)
        for g in range(size):
            conjugate = np.zeros(size, dtype=bool)
            conjugate[multiplication[multiplication[g, members], inverses[g]]] = True
            key = subgroup_key(conjugate)
            require(key not in known or known[key] == class_id, "CONJUGACY_CLASS_COLLISION")
            known[key] = class_id

    trivial = np.zeros(size, dtype=bool)
    trivial[identity] = True
    add_class([], trivial)
    cursor = 0
    while cursor < len(representatives):
        generators, subgroup = representatives[cursor]
        cursor += 1
        for g in cyclic.values():
            if subgroup[g]:
                continue
            extension = generate(multiplication, identity, generators + [g])
            if subgroup_key(extension) not in known:
                add_class(generators + [g], extension)
    subgroups = []
    for key in known:
        subgroup = np.unpackbits(np.frombuffer(key, dtype=np.uint8), bitorder="little")[:size].astype(bool)
        members = np.flatnonzero(subgroup)
        require(bool(subgroup[identity]), "SUBGROUP_IDENTITY_FAILURE")
        require(bool(subgroup[inverses[members]].all()), "SUBGROUP_INVERSE_FAILURE")
        require(bool(subgroup[multiplication[np.ix_(members, members)]].all()), "SUBGROUP_CLOSURE_FAILURE")
        subgroups.append(subgroup)
    return representatives, subgroups


def mask(subset):
    return int.from_bytes(subgroup_key(subset), "little")


def cosets(multiplication, subgroup):
    size = len(multiplication)
    members = np.flatnonzero(subgroup)
    covered = np.zeros(size, dtype=bool)
    result = []
    for g in range(size):
        if covered[g]:
            continue
        subset = np.zeros(size, dtype=bool)
        subset[multiplication[g, members]] = True
        require(int(subset.sum()) == len(members), "COSET_SIZE_FAILURE")
        covered |= subset
        result.append(mask(subset))
    require(len(result) * len(members) == size, "COSET_PARTITION_FAILURE")
    return result


def family_check(coset_masks, indices, size, cap):
    require(len(coset_masks) == len(indices), "FAMILY_LENGTH_MISMATCH")
    covered, previous = 0, []
    for item, index in zip(coset_masks, indices):
        require(0 < item < (1 << size), "COSET_OUT_OF_RANGE")
        require(size % index == 0 and item.bit_count() == size // index, "SIZE_INDEX_MISMATCH")
        require(not (covered & item), "COSET_OVERLAP")
        require(all(gcd(index, old) <= cap for old in previous), "INDEX_GCD_EXCEEDS_CAP")
        covered |= item
        previous.append(index)
    return covered


def eight_index_patterns(order_histogram, size):
    indices = sorted({size // order for order in order_histogram if order < size})
    output = []

    def visit(chosen, allowed, occupied):
        need = 8 - len(chosen)
        if not need:
            output.append(tuple(chosen))
            return
        if not allowed or (min(allowed) > 7 and len(allowed) < need):
            return
        for position, index in enumerate(allowed):
            new_occupied = occupied + size // index
            if new_occupied > size:
                continue
            following = allowed[position if index <= 7 else position + 1:]
            following = [j for j in following if 2 <= gcd(index, j) <= 7]
            visit(chosen + [index], following, new_occupied)

    visit([], indices, 0)
    return indices, output


def six_coset_check(index_seven_cosets, size):
    full = (1 << size) - 1
    coset_set = set(index_seven_cosets)
    counts = Counter()
    family_count = 0

    def visit(chosen, candidates, covered):
        nonlocal family_count
        if len(chosen) == 6:
            require((full ^ covered) in coset_set, "SIX_COMPLEMENT_NOT_COSET")
            family_count += 1
            counts[full ^ covered] += 1
            return
        need = 6 - len(chosen)
        for position, item in enumerate(candidates):
            if len(candidates) - position < need:
                break
            following = [other for other in candidates[position + 1:] if not (item & other)]
            visit(chosen + [item], following, covered | item)

    visit([], index_seven_cosets, 0)
    return family_count, counts


def verify_group(label, elements, expected_size):
    points, multiplication, identity, inverses = group_table(elements)
    size = len(points)
    require(size == expected_size, "WRONG_GROUP_ORDER")
    representatives, subgroups = subgroup_lattice(multiplication, identity, inverses)
    histogram = Counter(int(subgroup.sum()) for subgroup in subgroups)
    indices, patterns = eight_index_patterns(histogram, size)
    require(min(indices) == 7, "UNHANDLED_SMALL_INDEX")
    require(bool(patterns), "NO_REDUCED_PATTERNS_CONTROL")
    require(all(p[:6] == (7,) * 6 and p[6] > 7 and p[7] > 7 and gcd(p[6] // 7, p[7] // 7) == 1
                for p in patterns), "UNHANDLED_INDEX_PATTERN")
    index_seven_cosets = sorted({c for subgroup in subgroups if int(subgroup.sum()) == size // 7
                                 for c in cosets(multiplication, subgroup)})
    six_count, complement_counts = six_coset_check(index_seven_cosets, size)
    stabilizer_checks = []
    for _, stabilizer in representatives:
        stabilizer_size = int(stabilizer.sum())
        if stabilizer_size != size // 7:
            continue
        internal = [subgroup for subgroup in subgroups if not bool((subgroup & ~stabilizer).any())]
        full_stabilizer = set(np.flatnonzero(stabilizer).tolist())
        coprime_pairs = 0
        for position, first in enumerate(internal):
            first_index = stabilizer_size // int(first.sum())
            if first_index == 1:
                continue
            for second in internal[position + 1:]:
                second_index = stabilizer_size // int(second.sum())
                if second_index == 1 or gcd(first_index, second_index) != 1:
                    continue
                actual_product = set(multiplication[np.ix_(np.flatnonzero(first), np.flatnonzero(second))].ravel().tolist())
                require(actual_product == full_stabilizer, "COPRIME_STABILIZER_PRODUCT_FAILURE")
                coprime_pairs += 1
        stabilizer_checks.append({"order": stabilizer_size, "internal_subgroups": len(internal),
                                  "coprime_proper_index_pairs": coprime_pairs})
    require(bool(stabilizer_checks), "NO_INDEX_SEVEN_STABILIZER")
    seven_subgroup = next(subgroup for subgroup in subgroups if int(subgroup.sum()) == size // 7)
    positive_seven = cosets(multiplication, seven_subgroup)
    require(len(positive_seven) == 7, "SEVEN_PARTITION_CONTROL_FAILURE")
    require(family_check(positive_seven, [7] * 7, size, 7) == (1 << size) - 1,
            "SEVEN_PARTITION_CONTROL_FAILURE")
    larger_index = min(index for index in indices if index >= 8)
    larger_subgroup = next(subgroup for subgroup in subgroups if int(subgroup.sum()) == size // larger_index)
    positive_eight = cosets(multiplication, larger_subgroup)[:8]
    family_check(positive_eight, [larger_index] * 8, size, larger_index)
    controls = []
    for name, test, intended in [
        ("duplicate_coset", lambda: family_check(positive_seven + [positive_seven[0]], [7] * 8, size, 7), "COSET_OVERLAP"),
        ("wrong_index", lambda: family_check([positive_seven[0]], [8], size, 8), "SIZE_INDEX_MISMATCH"),
        ("forbidden_index_gcd", lambda: family_check(positive_eight, [larger_index] * 8, size, 7), "INDEX_GCD_EXCEEDS_CAP"),
    ]:
        try:
            test()
        except CheckError as error:
            require(str(error) == intended, "WRONG_MUTATION_REASON")
            controls.append({"mutation": name, "rejected_for": str(error)})
        else:
            raise CheckError("MUTATION_ACCEPTED")
    subgroup_digest = hashlib.sha256(b"".join(sorted(subgroup_key(s) for s in subgroups))).hexdigest()
    return {"group": label, "order": size, "subgroup_conjugacy_classes": len(representatives),
            "subgroups": len(subgroups), "subgroup_set_sha256": subgroup_digest,
            "order_histogram": sorted(histogram.items()), "proper_indices": indices,
            "eight_index_patterns": patterns, "index_seven_cosets": len(index_seven_cosets),
            "six_disjoint_index_seven_families": six_count,
            "complements_all_index_seven_cosets": True,
            "distinct_complements": len(complement_counts), "stabilizer_checks": stabilizer_checks,
            "seven_coset_partition_positive": True, "eight_coset_relaxed_cap_positive": larger_index,
            "targeted_negative_controls": controls,
            "conclusion": "NO_EIGHT_DISJOINT_COSETS_WITH_ALL_INDEX_GCDS_AT_MOST_SEVEN",
            "scope": "Author-run exact reduced exhaustive check; elementary written reduction lemmas required; not independent-model, formal, novelty or adoption verification."}


def main():
    results = [verify_group("GL3(2)", linear_group(), 168),
               verify_group("A7", [p for p in permutations(range(7)) if even(p)], 2520)]
    print(json.dumps({"status": "PASS", "groups": results}, indent=2))


if __name__ == "__main__":
    main()
