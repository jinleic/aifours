#!/usr/bin/env python3
"""Independent finite controls for the frozen f212 written argument."""
from itertools import combinations, product
from math import gcd
import json

MOD = 990
ANCHORS = (0, 1, 7, 13, 14)
CLASSES = (3, 25, 45)
FORBIDDEN_GCD = {3, 5, 11, 15, 33, 55, 165}


def allowed(d, use_u=True, use_v=True):
    if d % 2 == 0:
        return True
    trigger_u = use_u and d % 3 == 0
    trigger_v = use_v and (d % 5 == 0 or d % 11 == 0)
    return not (trigger_u or trigger_v) or d % 9 == 0


def domain(c, anchors=ANCHORS, use_u=True, use_v=True):
    return [r for r in range(c, MOD, 55)
            if all(allowed(r - y, use_u, use_v) for y in anchors)]


def witness(anchors=ANCHORS, use_u=True, use_v=True, drop_edge=None):
    domains = [domain(c, anchors, use_u, use_v) for c in CLASSES]
    for triple in product(*domains):
        if all((CLASSES[i], CLASSES[j]) == drop_edge or
               allowed(triple[i] - triple[j], use_u, use_v)
               for i, j in combinations(range(3), 2)):
            return triple
    return None


# Exhaust the ordered pair projection; this checks a finite equivalence only.
pair_count = 0
for r in range(MOD):
    for s in range(MOD):
        d = r - s
        via_gcd = d % 2 == 0 or gcd(d, MOD) not in FORBIDDEN_GCD
        assert allowed(d) == via_gcd
        pair_count += 1
assert pair_count == MOD * MOD

survivors = [r for r in range(MOD) if all(allowed(r - y) for y in ANCHORS)]
assert not [r for r in survivors if r % 2 == 0 and r % 3 == 1]
D = {c: domain(c) for c in CLASSES}
shapes = {c: sorted({(r % 2, r % 9) for r in D[c]}) for c in CLASSES}
assert shapes == {
    3: [(1, 5)],
    25: [(0, 0), (0, 2), (0, 3), (0, 5), (0, 6), (0, 8)],
    45: [(1, 0)],
}
assert witness() is None
all_triples = list(product(*(D[c] for c in CLASSES)))
assert len(all_triples) == 6
edge_data = []
for x3, x25, x45 in all_triples:
    edge_data.append({"x25_mod9": x25 % 9,
                      "edge_3_25_ok": allowed(x3 - x25),
                      "edge_25_45_ok": allowed(x25 - x45)})
assert all(not (x["edge_3_25_ok"] and x["edge_25_45_ok"]) for x in edge_data)

# Negatives must expose exactly the indicated missing constraint, not mere failures.
negative_edges = {}
for edge in ((3, 25), (25, 45)):
    triple = witness(drop_edge=edge)
    assert triple is not None
    violations = [(CLASSES[i], CLASSES[j]) for i, j in combinations(range(3), 2)
                  if not allowed(triple[i] - triple[j])]
    assert violations == [edge]
    negative_edges[str(edge)] = {"triple": triple, "only_failed_edge": violations[0]}

negative_rules = {}
for label, use_u, use_v in (("U removed", False, True), ("V removed", True, False)):
    triple = witness(use_u=use_u, use_v=use_v)
    assert triple is not None
    points = ANCHORS + triple
    assert all(allowed(a-b, use_u, use_v) for a, b in combinations(points, 2))
    assert any(not allowed(a-b) for a, b in combinations(points, 2))
    negative_rules[label] = triple

without_14 = witness(anchors=(0, 1, 7, 13))
assert without_14 is not None
assert any(not allowed(x - 14) for x in without_14)

# Exercise the exact multiplier construction over the explicitly bounded grid.
multiplier_count = 0
for e, K, shift, T in product(range(1, 5), range(1, 5), (1, 2), (55, 275, 605, 715)):
    v = e + shift
    n = (2 ** K) * (3 ** v) * T
    for x in range(1, 990, 2):
        if x % 3 == 0 and x % 9 != 0:
            ell = 3
        elif x % 3 != 0 and (x % 5 == 0 or x % 11 == 0):
            ell = 5 if x % 5 == 0 else 11
        else:
            continue
        g = gcd(x, n)
        assert g % ell == 0 and g < n
        t = g // ell
        # K is the largest possible a, so this implies coprimality for all a <= K.
        assert gcd(t, (3 ** e) * (2 ** K)) == 1
        assert gcd(t * ell, n) == g
        multiplier_count += 1
assert multiplier_count == 25600

# The pure-two case, both parities, finite grid: a is allowed to vary independently.
two_case_count = 0
two_parities = set()
for v, K in product(range(1, 5), repeat=2):
    n = 55 * (3 ** v) * (2 ** K)
    for q in range(6, n, 165):
        ell, anchor = (3, 0) if q % 2 else (5, 1)
        x = q - anchor
        g = gcd(x, n)
        assert x % 2 == 1 and x % ell == 0 and g % ell == 0 and g < n
        t = g // ell
        assert gcd(t * ell, n) == g
        assert all(gcd(t, 2 ** a) == 1 for a in range(K + 1))
        two_parities.add(q % 2)
        two_case_count += 1
assert two_parities == {0, 1}

# Two deliberate domain errors: the constructed t ceases to be admissible.
g1 = gcd(15, 990)
t1 = g1 // 5
assert gcd(t1, 3) != 1  # g/5 incorrectly used when x has a factor 3
assert 15 % 9 != 0

g2 = gcd(10, 990)
t2 = g2 // 5
assert gcd(t2, 6) != 1  # an even difference with a head cardinality divisible by 2

print(json.dumps({
    "ordered_pairs": pair_count,
    "anchor_survivors": len(survivors),
    "forbidden_even_mod3_1_survivors": 0,
    "class_representatives_mod_990": D,
    "class_parity_mod9_shapes": shapes,
    "literal_triples_checked": len(all_triples),
    "edge_results": edge_data,
    "negative_removed_edges": negative_edges,
    "negative_removed_rules": negative_rules,
    "negative_removed_anchor_14": without_14,
    "generic_multiplier_checks": multiplier_count,
    "pure_two_case_checks": two_case_count,
    "pure_two_case_parities": sorted(two_parities),
    "bad_multiplier_negative_3_factor": {"n": 990, "x": 15, "ell": 5, "g": g1, "t": t1, "gcd_t_head": gcd(t1, 3)},
    "bad_multiplier_negative_even_difference": {"n": 990, "x": 10, "ell": 5, "g": g2, "t": t2, "gcd_t_head": gcd(t2, 6)},
}, sort_keys=True, indent=2))
