#!/usr/bin/env python3
"""Unrun prospective exact PSL(2,7) actual-subgroup/coset assay.

No input, network, child processes, or filesystem writes.  Parent must fully
read this source, separately authorize one run, and impose a 55-second outer
limit.  The internal monotonic deadline is 52 seconds.  A traceback, timeout,
or absent run is not a pass.  This checker addresses q=7 only.
"""
import itertools
import json
import math
import time
from collections import Counter

START = time.monotonic()
DEADLINE = START + 52.0


def guard():
    if time.monotonic() >= DEADLINE:
        raise TimeoutError("cooperative 52-second deadline reached; no verdict")


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def checked_matrix(a):
    if (not isinstance(a, tuple) or len(a) != 4 or
            any(type(x) is not int or not 0 <= x < 7 for x in a)):
        raise ValueError("matrix must be a 4-tuple of residues 0..6")
    if (a[0] * a[3] - a[1] * a[2]) % 7 != 1:
        raise ValueError("matrix determinant is not 1")
    return a


def canonical(a):
    a = checked_matrix(a)
    return min(a, tuple((-x) % 7 for x in a))


def matrix_product(a, b):
    return ((a[0]*b[0] + a[1]*b[2]) % 7,
            (a[0]*b[1] + a[1]*b[3]) % 7,
            (a[2]*b[0] + a[3]*b[2]) % 7,
            (a[2]*b[1] + a[3]*b[3]) % 7)


def rejects_matrix(a):
    try:
        canonical(a)
        return False
    except ValueError:
        return True


def indices(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


# Enumerate determinant-one matrices directly, then quotient by the actual
# center {I,-I}; integer ids refer to the sorted canonical representatives.
elements = sorted({canonical((a, b, c, d))
                   for a in range(7) for b in range(7)
                   for c in range(7) for d in range(7)
                   if (a*d - b*c) % 7 == 1})
need(len(elements) == 168, "projective group order")
N = len(elements)
BIT = [1 << i for i in range(N)]
FULL = (1 << N) - 1
id_of = {a: i for i, a in enumerate(elements)}
unit = id_of[canonical((1, 0, 0, 1))]
minus_unit = (6, 0, 0, 6)
need(canonical(minus_unit) == elements[unit], "projective center")
need(rejects_matrix((1, 0, 0, 2)) and rejects_matrix((1, 0, 0))
     and rejects_matrix((8, 0, 0, 1)), "malformed matrix refusal")
guard()

product = []
for a in elements:
    product.append([id_of[canonical(matrix_product(a, b))] for b in elements])
    guard()
inverse = [id_of[canonical((a[3], (-a[1]) % 7,
                              (-a[2]) % 7, a[0]))] for a in elements]
for a in range(N):
    need(len(set(product[a])) == N, "product row permutation")
    need(product[a][unit] == a and product[unit][a] == a, "unit")
    need(product[a][inverse[a]] == unit and
         product[inverse[a]][a] == unit, "inverse")

# This is an independent reachability check against the determinant enumeration.
upper = id_of[canonical((1, 1, 0, 1))]
lower = id_of[canonical((1, 0, 1, 1))]
generated = {unit}
frontier = [unit]
while frontier:
    x = frontier.pop()
    for s in (upper, lower):
        y = product[x][s]
        if y not in generated:
            generated.add(y)
            frontier.append(y)
    guard()
need(len(generated) == N, "unipotents do not generate the group")


def left_coset(g, subgroup_members):
    return sum(BIT[product[g][h]] for h in subgroup_members)


def right_coset(g, subgroup_members):
    return sum(BIT[product[h][g]] for h in subgroup_members)


def is_left_coset(coset, subgroup):
    if not coset:
        return False
    g = next(indices(coset))
    return coset == left_coset(g, list(indices(subgroup)))


def adjoin(subgroup, members, generator):
    # Explore right multiplication by h*generator from every left H-coset.
    # Each new point brings in its entire left H-coset.  Since all elements
    # have finite order, the resulting finite monoid is <H,g>.
    seen = subgroup
    representatives = [unit]
    pos = 0
    while pos < len(representatives):
        x = representatives[pos]
        pos += 1
        for h in members:
            y = product[product[x][h]][generator]
            if not (seen & BIT[y]):
                new_coset = left_coset(y, members)
                need(not (seen & new_coset), "adjoin coset overlap")
                seen |= new_coset
                representatives.append(y)
        guard()
    return seen


# For fixed H, one representative g of each left H-coset gH suffices:
# <H,gh>=<H,g> for every h in H.  Every subgroup is reachable by repeatedly
# adjoining elements of it, so the queue covers the complete subgroup lattice.
known = {BIT[unit]}
queue = [BIT[unit]]
position = 0
while position < len(queue):
    H = queue[position]
    position += 1
    members = list(indices(H))
    covered = 0
    for g in range(N):
        if covered & BIT[g]:
            continue
        block = left_coset(g, members)
        need(not (covered & block), "left cosets must partition")
        covered |= block
        if H & BIT[g]:
            continue
        K = adjoin(H, members, g)
        if K not in known:
            known.add(K)
            queue.append(K)
    need(covered == FULL, "subgroup coset enumeration incomplete")
    guard()

subgroups = sorted(known, key=lambda H: (H.bit_count(), H))
subgroup_id = {H: i for i, H in enumerate(subgroups)}
need(FULL in known, "entire group missing")
for H in subgroups:
    members = list(indices(H))
    need(H & BIT[unit] and N % len(members) == 0, "subgroup unit/order")
    for a in members:
        need(H & BIT[inverse[a]], "subgroup inverse closure")
        for b in members:
            need(H & BIT[product[a][b]], "subgroup product closure")
    guard()

proper = [H for H in subgroups if H != FULL]
maximal = [H for H in proper
           if not any(H != K and (H & K) == H for K in proper)]
maximal_indices = Counter(N // H.bit_count() for H in maximal)
need(maximal_indices == Counter({7: 14, 8: 8}), "maximal index/count")

# Materialize every proper actual left coset, not just subgroup labels.
# A coset determines its subgroup, since x^{-1}C is independent of x in C.
cosets_by_subgroup = {}
all_cosets = []
by_mask = {}
for H in proper:
    members = list(indices(H))
    covered = 0
    blocks = []
    for g in range(N):
        if covered & BIT[g]:
            continue
        C = left_coset(g, members)
        need(not (covered & C), "coset partition overlap")
        need(C not in by_mask, "distinct subgroup/coset sets duplicated")
        covered |= C
        blocks.append((g, C))
        record = (H, g, C)
        by_mask[C] = record
        all_cosets.append(record)
    need(covered == FULL and len(blocks) == N // len(members),
         "actual coset enumeration incomplete")
    cosets_by_subgroup[H] = blocks
    guard()


def conjugate(g, H):
    return sum(BIT[product[product[g][h]][inverse[g]]] for h in indices(H))


index7 = sorted(H for H in maximal if N // H.bit_count() == 7)
for H in maximal:
    normalizer = [g for g in range(N) if conjugate(g, H) == H]
    need(set(normalizer) == set(indices(H)), "maximal self-normalizer")
    guard()
remaining = set(index7)
classes = []
while remaining:
    H = min(remaining)
    orbit = {conjugate(g, H) for g in range(N)}
    need(orbit <= remaining and len(orbit) == 7, "index-7 conjugacy class")
    classes.append(sorted(orbit))
    remaining -= orbit
need(len(classes) == 2, "two index-7 classes")
classes.sort(key=lambda row: tuple(row))
points, lines = classes


def class_action(cls):
    lookup = {H: j for j, H in enumerate(cls)}
    action = []
    for g in range(N):
        image = [lookup[conjugate(g, H)] for H in cls]
        need(sorted(image) == list(range(7)), "class action permutation")
        action.append(image)
        guard()
    for a in range(N):
        for b in range(N):
            ab = product[a][b]
            for x in range(7):
                need(action[ab][x] == action[a][action[b][x]],
                     "conjugation action orientation")
        guard()
    for x, H in enumerate(cls):
        stabilizer = sum(BIT[g] for g in range(N) if action[g][x] == x)
        need(stabilizer == H, "actual point stabilizer")
    orbit = {(action[g][0], action[g][1]) for g in range(N)}
    need(len(orbit) == 42 and all(x != y for x, y in orbit),
         "degree-seven action not 2-transitive")
    return action


point_action = class_action(points)
line_action = class_action(lines)

# Incidence is reconstructed from actual K-orbits on the point class: the
# 3-orbit of each line stabilizer K is its line; no Fano table is imported.
incidence = [[False] * 7 for _ in range(7)]  # [point][line]
for a, K in enumerate(lines):
    unseen = set(range(7))
    orbits = []
    while unseen:
        x = min(unseen)
        orbit = {point_action[k][x] for k in indices(K)}
        need(orbit <= unseen, "point orbits overlap")
        unseen -= orbit
        orbits.append(orbit)
    need(sorted(map(len, orbits)) == [3, 4], "line 3+4 orbit")
    for x in next(o for o in orbits if len(o) == 3):
        incidence[x][a] = True
need(all(sum(incidence[x][a] for x in range(7)) == 3 for a in range(7)),
     "three points per line")
need(all(sum(incidence[x]) == 3 for x in range(7)), "three lines per point")
for x, y in itertools.combinations(range(7), 2):
    need(sum(incidence[x][a] and incidence[y][a] for a in range(7)) == 1,
         "point pair incidence")
for a, b in itertools.combinations(range(7), 2):
    need(sum(incidence[x][a] and incidence[x][b] for x in range(7)) == 1,
         "line pair incidence")
for expected in (False, True):
    all_flags = {(x, a) for x in range(7) for a in range(7)
                 if incidence[x][a] == expected}
    x, a = min(all_flags)
    flag_orbit = {(point_action[g][x], line_action[g][a]) for g in range(N)}
    need(flag_orbit == all_flags, "flag or antiflag action")
guard()

# Each cell is the full set of group elements mapping its source to target.
# Compare this actual bitset against the independently materialized cosets.
cells = []
cell_at = {}
for kind, cls, action in (("P", points, point_action),
                           ("L", lines, line_action)):
    for x, H in enumerate(cls):
        for y in range(7):
            C = sum(BIT[g] for g in range(N) if action[g][x] == y)
            need(C.bit_count() == 24 and C in by_mask and by_mask[C][0] == H,
                 "transporter is not its claimed actual left coset")
            cell_at[(kind, x, y)] = len(cells)
            cells.append((kind, x, y, H, C))
actual_index7 = {C for H, _, C in all_cosets if N // H.bit_count() == 7}
need(len(cells) == 98 and len(actual_index7) == 98 and
     {cell[4] for cell in cells} == actual_index7, "98 actual index-7 cosets")
cell_by_mask = {cell[4]: i for i, cell in enumerate(cells)}

same_hist = Counter()
cross_hist = Counter()
adjacency = [0] * len(cells)  # only larger-numbered neighbours
for i, first in enumerate(cells):
    kind, x, y, _, C = first
    for j in range(i + 1, len(cells)):
        kind2, a, b, _, D = cells[j]
        overlap = (C & D).bit_count()
        if kind == kind2:
            same_hist[overlap] += 1
            need((overlap == 0) == (x == a or y == b),
                 "same-class disjointness")
            need(overlap in (0, 4), "same-class intersection size")
        else:
            # All P cells were appended before all L cells.
            cross_hist[overlap] += 1
            left_flag = incidence[x][a]
            right_flag = incidence[y][b]
            need((overlap == 0) == (left_flag != right_flag),
                 "cross-class incidence criterion")
            if overlap:
                need(overlap == (8 if left_flag else 6),
                     "cross-class intersection size")
        if not overlap:
            adjacency[i] |= 1 << j
    guard()
need(same_hist == Counter({0: 588, 4: 1764}), "same-class pair counts")
need(cross_hist == Counter({0: 1176, 6: 784, 8: 441}),
     "cross-class pair counts")


def completion(six, proposed=None):
    if len(six) != 6 or len(set(six)) != 6:
        return None
    union = 0
    for i in six:
        if not 0 <= i < len(cells) or union & cells[i][4]:
            return None
        union |= cells[i][4]
    rest = FULL ^ union
    if proposed is not None and rest != proposed:
        return None
    return cell_by_mask.get(rest)


clique_counts = Counter()
partitions = set()
first_six = None
nodes = 0


def visit(chosen, candidates):
    global nodes, first_six
    nodes += 1
    if nodes % 1024 == 0:
        guard()
    if len(chosen) == 6:
        complement = completion(chosen)
        need(complement is not None, "six-clique has no actual coset complement")
        p = sum(cells[i][0] == "P" for i in chosen)
        clique_counts[f"{p},{6-p}"] += 1
        partitions.add(tuple(sorted((*chosen, complement))))
        if first_six is None:
            first_six = tuple(chosen)
        return
    needed = 6 - len(chosen)
    while candidates.bit_count() >= needed:
        low = candidates & -candidates
        i = low.bit_length() - 1
        candidates ^= low
        visit((*chosen, i), candidates & adjacency[i])


visit((), (1 << len(cells)) - 1)
need(clique_counts == Counter({"6,0": 98, "0,6": 98,
                               "4,2": 294, "2,4": 294, "3,3": 784}),
     "six-clique composition counts")
need(len(partitions) == 224, "seven-coset partition count")
guard()

# Check every actual proper coset whose index is not divisible by 7 against
# every actual index-7 coset; classify real intersection sizes by index.
other_cosets = [(H, g, C) for H, g, C in all_cosets
                if (N // H.bit_count()) % 7]
intersection_hist = Counter()
for cell in cells:
    C = cell[4]
    for H, _, D in other_cosets:
        index = N // H.bit_count()
        amount = (C & D).bit_count()
        need(amount > 0 and math.gcd(7, index) == 1,
             "non-7 index actual coset failed to intersect")
        need(amount == N // (7 * index), "coprime intersection cardinality")
        intersection_hist[f"{index}:{amount}"] += 1
    guard()

# Only the high relative indices derived from 7m | 168 are used here.
high = [(H, (N // H.bit_count()) // 7) for H in proper
        if (N // H.bit_count()) % 7 == 0 and N // H.bit_count() > 7]
high_values = sorted({m for _, m in high})
need(all(m > 1 and 24 % m == 0 for m in high_values), "relative divisors")
for a, b, c in itertools.combinations_with_replacement(high_values, 3):
    need(not (math.gcd(a, b) == math.gcd(a, c) == math.gcd(b, c) == 1),
         "three pairwise coprime high relative indices")
high_coprime = sorted({tuple(sorted((a, b))) for a in high_values
                       for b in high_values if math.gcd(a, b) == 1})
need(set(high_coprime) <= {(2, 3), (3, 4), (3, 8)},
     "unexpected relative coprime indices")

# Independently inspect actual relative cosets inside every order-24 index-7
# subgroup.  No isomorphism label or all-group Sun8 claim is used.
internal = []
for K in points + lines:
    local = [H for H in proper if H != K and (H & K) == H]
    local_cosets = {}
    for H in local:
        local_cosets[H] = [C for _, C in cosets_by_subgroup[H] if (C & K) == C]
        need(len(local_cosets[H]) == K.bit_count() // H.bit_count(),
             "internal actual left cosets")
    labels = 0
    pairs = 0
    pair_types = Counter()
    for A, B in itertools.combinations_with_replacement(local, 2):
        m, n = K.bit_count() // A.bit_count(), K.bit_count() // B.bit_count()
        if math.gcd(m, n) != 1:
            continue
        need(tuple(sorted((m, n))) in {(2, 3), (3, 4), (3, 8)},
             "internal relative index outside derived pairs")
        labels += 1
        pair_types[str(tuple(sorted((m, n))))] += 1
        for C in local_cosets[A]:
            for D in local_cosets[B]:
                need(C & D, "disjoint coprime-index internal cosets")
                pairs += 1
    internal.append({"ambient_subgroup_id": subgroup_id[K],
                     "proper_internal_subgroups": len(local),
                     "coprime_label_pairs": labels,
                     "actual_coset_pairs": pairs,
                     "relative_index_pair_counts": dict(pair_types)})
    guard()

# Named negative controls use deliberately malformed inputs/consumers.  They
# are assertions about refusal, not additional scientific executions.
H = points[0]
Hm = list(indices(H))
g = next(g for g in range(N) if left_coset(g, Hm) != right_coset(g, Hm))
need(not is_left_coset(right_coset(g, Hm), H), "left/right mix accepted")
need(is_left_coset(left_coset(g, Hm), H), "valid left coset rejected")

bad_incidence = [row[:] for row in incidence]
bad_incidence[0][0] = not bad_incidence[0][0]
wrong_incidence_mismatches = 0
for x, y, a, b in itertools.product(range(7), repeat=4):
    C = cells[cell_at[("P", x, y)]][4]
    D = cells[cell_at[("L", a, b)]][4]
    wrong = bad_incidence[x][a] != bad_incidence[y][b]
    wrong_incidence_mismatches += (wrong != (not (C & D)))
need(wrong_incidence_mismatches > 0, "wrong incidence not rejected")

valid_six = [cell_at[("P", 0, y)] for y in range(6)]
wrong_completion = cells[cell_at[("P", 1, 6)]][4]
need(completion(valid_six) is not None and
     completion(valid_six, wrong_completion) is None,
     "false complement accepted")
nonclique = [cell_at[("P", 0, y)] for y in range(5)] + [cell_at[("P", 1, 1)]]
need(completion(nonclique) is None, "overlapping six falsely completed")

for kind, x, y, _, C in cells:
    inverted = sum(BIT[inverse[z]] for z in indices(C))
    need(inverted == cells[cell_at[(kind, y, x)]][4], "inverse transporter")
transposed = cells[cell_at[("P", 1, 0)]][4]
need(not is_left_coset(transposed, points[0]), "transposed source accepted")
need(not is_left_coset(points[0], lines[0]), "source class mix accepted")

packing = [cells[cell_at[("P", 0, y)]][4] for y in range(7)]
union = 0
for C in packing:
    need(not (union & C), "positive packing is not disjoint")
    union |= C
need(union == FULL and len(packing) == 7, "seven-coset packing")
need(math.gcd(7, 7) == 7 and len(cosets_by_subgroup[points[0]]) == 7,
     "label repetition versus seven actual cosets")
need(len({packing[0] for _ in range(8)}) == 1,
     "repeated labels incorrectly treated as eight disjoint cosets")


def model_for_q(q):
    if q != 7:
        raise ValueError("this finite model covers q=7 only")
    return N


try:
    model_for_q(8)
    raise AssertionError("out-of-scope field accepted")
except ValueError:
    pass
need(model_for_q(7) == N, "q=7 scope guard")
guard()

counts_by_order = Counter(H.bit_count() for H in subgroups)
cosets_by_index = Counter(N // H.bit_count() for H, _, _ in all_cosets)
maximal_set = set(maximal)
result = {
    "status": "PASS_BOUNDED_Q7_ASSAY_ONLY",
    "elapsed_before_encoding_seconds": round(time.monotonic() - START, 6),
    "scope": {"field": 7, "objects": "actual left cosets of actual subgroups",
              "all_fields": False, "all_group_sun8": False,
              "classification_source_authenticated": False},
    "group": {"order": N, "identity_id": unit,
              "upper_generator_id": upper, "lower_generator_id": lower,
              "canonical_matrix_representatives_by_id": elements},
    "subgroup_enumeration": {
        "method": "complete adjoin-closure, one representative per gH",
        "total": len(subgroups), "counts_by_order": dict(counts_by_order),
        "proper_cosets_total": len(all_cosets),
        "proper_cosets_by_index": dict(cosets_by_index),
        "maximal_counts_by_index": dict(maximal_indices),
        "inventory": [{"id": subgroup_id[H], "order": H.bit_count(),
                       "members": list(indices(H)), "maximal": H in maximal_set}
                      for H in subgroups]},
    "geometry": {
        "point_stabilizer_ids": [subgroup_id[H] for H in points],
        "line_stabilizer_ids": [subgroup_id[H] for H in lines],
        "lines_as_point_numbers": [[x for x in range(7) if incidence[x][a]]
                                    for a in range(7)],
        "actual_index7_cosets": len(cells),
        "same_class_intersections": dict(same_hist),
        "cross_class_intersections": dict(cross_hist),
        "six_cliques_by_point_line_count": dict(clique_counts),
        "seven_coset_partitions": len(partitions),
        "first_six_cells": [list(cells[i][:3]) for i in first_six],
        "first_six_complement": list(cells[completion(first_six)][:3])},
    "nondivisible_by_7": {"cosets": len(other_cosets),
                          "index_and_intersection_size_counts": dict(intersection_hist)},
    "high_relative_indices": {"values": high_values,
                              "coprime_pairs": high_coprime,
                              "subgroup_label_count": len(high)},
    "internal_actual_coprime_checks": internal,
    "positive_seven_packing": {"subgroup_id": subgroup_id[points[0]],
                               "coset_members": [list(indices(C)) for C in packing]},
    "named_controls": {"malformed_matrix": "REJECTED",
                       "unquotiented_projective_center": "REJECTED",
                       "left_right_mix": "REJECTED",
                       "wrong_incidence": "REJECTED",
                       "false_completion_and_nonclique": "REJECTED",
                       "transposed_source_map": "REJECTED",
                       "source_class_mix": "REJECTED",
                       "logical_scope_label_vs_coset_and_other_q": "GUARDED"},
}
payload = json.dumps(result, sort_keys=True, separators=(",", ":"))
need(len(payload.encode("utf-8")) <= 200000, "bounded output size")
guard()
print(payload)
