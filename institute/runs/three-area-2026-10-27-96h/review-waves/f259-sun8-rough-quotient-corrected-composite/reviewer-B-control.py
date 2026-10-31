#!/usr/bin/env python3
"""Independent, finite controls only; the universal claims require the written proof."""
import itertools
import json
import math

checks = {}
negatives = {}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def expected_failure(label, condition, reason):
    try:
        require(condition, reason)
    except AssertionError as exc:
        require(str(exc) == reason, f"{label}: wrong rejection reason: {exc}")
        negatives[label] = reason
    else:
        raise AssertionError(f"{label}: intended negative unexpectedly passed")


def power(element, exponent, multiply, identity):
    result = identity
    for _ in range(exponent):
        result = multiply(result, element)
    return result


def prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))


# C7 is a finite control for the rational/C7 example, not an enumeration of Q.
cosets7 = [(frozenset({x}), 7) for x in range(7)]
cosets7.append((frozenset(range(7)), 1))
disjoint_families = [family for size in range(9)
                     for family in itertools.combinations(cosets7, size)
                     if all(a[0].isdisjoint(b[0])
                            for a, b in itertools.combinations(family, 2))]
maximum = max(map(len, disjoint_families))
witness7 = cosets7[:7]
require(maximum == 7, "C7 disjoint maximum")
require(all(math.gcd(a[1], b[1]) == 7
            for a, b in itertools.combinations(witness7, 2)), "C7 low-gcd witness")
expected_failure("B7_C7_le_6", maximum <= 6, "SEVEN_DISJOINT_INDEX_7_COSETS")
checks["C7"] = {"maximum_disjoint_cosets": maximum, "witness_indices": [7] * 7}

# Two complete finite affine-plane instances. A general proof is separate.
planes = {}
for p in (11, 23):
    points = {(x, y) for x in range(p) for y in range(p)}
    lines = [{(x, y) for x, y in points if x == 0},
             {(x, y) for x, y in points if y == 0},
             {(x, y) for x, y in points if (x + y) % p == 1}]
    intersections = [len(lines[i] & lines[j]) for i, j in ((0, 1), (0, 2), (1, 2))]
    triple = len(set.intersection(*lines))
    require(intersections == [1, 1, 1] and triple == 0, f"p={p} affine triangle")
    concurrent_line = {(x, y) for x, y in points if (x + y) % p == 0}
    require(lines[0] & lines[1] & concurrent_line == {(0, 0)}, f"p={p} concurrency")
    proper_subgroups = [frozenset({(0, 0)})]
    proper_subgroups += [frozenset((t, m * t % p) for t in range(p))
                         for m in range(p)]
    proper_subgroups.append(frozenset((0, t) for t in range(p)))
    require(len(set(proper_subgroups)) == p + 2, f"p={p} distinct subgroups")
    indices = [p * p // len(h) for h in proper_subgroups]
    require(set(indices) == {p, p * p}, f"p={p} subgroup indices")
    min_pair_gcd = min(math.gcd(a, b) for a in indices for b in indices)
    require(min_pair_gcd == p > 7, f"p={p} J7<=1 including repetition")
    planes[str(p)] = {"points": len(points), "proper_subgroups": len(indices),
                      "indices": sorted(set(indices)), "min_label_pair_gcd": min_pair_gcd,
                      "triangle_pair_intersections": intersections,
                      "triangle_total_intersection": triple,
                      "concurrent_control_intersection": 1}
    if p == 23:
        expected_failure("global_3_Helly", triple > 0, "PAIRWISE_BUT_EMPTY_TRIPLE")
        expected_failure("J7_le_0", len(proper_subgroups) == 0, "PROPER_SUBGROUP_EXISTS")
        finite_order = 7 * p * p
        divisors = [d for d in range(2, finite_order + 1) if finite_order % d == 0]
        require(min(divisors) == 7, "finite product minimum index lower bound")
        require(finite_order // (p * p) == 7, "index-7 projection witness")
        expected_failure("f151_mu_threshold", min(divisors) >= 8, "MU_IS_7")
        checks["finite_product"] = {"order": finite_order,
                                    "minimum_index_from_Lagrange_and_projection": 7}
checks["affine_planes"] = planes

# A twisted-coordinate presentation of the split central C7 by F_23^2 extension.
# This checks the adjustment calculation in one finite model only.
p = 23
modulus = 7

def f(v):
    a, b = v
    return (3 * a + b * b + a * b) % modulus


def twisted_mul(g, h):
    n, a, b = g
    m, c, d = h
    v, w = (a, b), (c, d)
    vw = ((a + c) % p, (b + d) % p)
    return ((n + m + f(v) + f(w) - f(vw)) % modulus, *vw)


identity = (0, 0, 0)
x, y = (0, 1, 0), (0, 0, 1)
xp = power(x, p, twisted_mul, identity)
yp = power(y, p, twisted_mul, identity)
require(xp == (6, 0, 0) and yp == (2, 0, 0), "unadjusted lift powers")
invp = pow(p, -1, modulus)
xadj = twisted_mul(((-xp[0] * invp) % modulus, 0, 0), x)
yadj = twisted_mul(((-yp[0] * invp) % modulus, 0, 0), y)
require(power(xadj, p, twisted_mul, identity) == identity, "x adjustment")
require(power(yadj, p, twisted_mul, identity) == identity, "y adjustment")
require(twisted_mul(xadj, yadj) == twisted_mul(yadj, xadj), "adjusted commutator")
section = {twisted_mul(power(xadj, i, twisted_mul, identity),
                       power(yadj, j, twisted_mul, identity))
           for i in range(p) for j in range(p)}
require(len(section) == p * p, "section cardinality")
require(len({(a, b) for _, a, b in section}) == p * p, "section projection")
require(section & {(a, 0, 0) for a in range(7)} == {identity}, "section kernel")
checks["central_finite_model"] = {"p": p, "kernel_order": modulus,
                                  "initial_lift_powers": [xp, yp],
                                  "adjusted_section_order": len(section)}

# A p=7 boundary mutation: C49 -> C7 with kernel 7*C49 is nonsplit.
seventh_powers = sorted({(7 * (1 + 7 * k)) % 49 for k in range(7)})
require(seventh_powers == [7], "C49 lift powers")
expected_failure("drop_p_invertibility", 0 in seventh_powers, "PTH_ROOT_OBSTRUCTED")

# A different kernel can have p-torsion in its automorphism group, even p>7.
# C23 semidirect (C11 x C11), first coordinate acting by multiplication by 2.
def action_mul(g, h):
    a, u, v = g
    b, s, t = h
    return ((a + pow(2, u, 23) * b) % 23, (u + s) % 11, (v + t) % 11)

conjugated = action_mul(action_mul((0, 1, 0), (1, 0, 0)), (0, 10, 0))
require(conjugated == (2, 0, 0), "nontrivial action control")
expected_failure("drop_aut_condition", conjugated == (1, 0, 0), "NONTRIVIAL_QUOTIENT_ACTION")

# Exact p=23, q=11 semidirect extension and actual lift powers.
p, q = 23, 11
require(prime(p) and prime(q), "prime pair")
require((p - 1) % q == 0 and 2 ** q == 2048 == 23 * 89 + 1, "prime-pair arithmetic")
require(pow(2, q, p) == 1 and all(pow(2, k, p) != 1 for k in range(1, q)), "action order")
require(math.gcd(p * q, 210) == 1, "rough quotient order")

def gm(g, h):
    return ((g[0] + pow(2, g[1], p) * h[0]) % p, (g[1] + h[1]) % (q * q))


def qm(g, h):
    return ((g[0] + pow(2, g[1], p) * h[0]) % p, (g[1] + h[1]) % q)


def proj(g):
    return (g[0], g[1] % q)


group = [(a, b) for a in range(p) for b in range(q * q)]
quotient = {(a, b) for a in range(p) for b in range(q)}
require({proj(g) for g in group} == quotient, "quotient surjectivity")
require(all(pow(2, b, p) == pow(2, b % q, p) for b in range(q * q)), "action descends")
gens = [(1, 0), (0, 1), (0, q)]
require(all(proj(gm(g, h)) == qm(proj(g), proj(h)) for g in group for h in gens),
        "quotient map on generators")
kernel = [g for g in group if proj(g) == (0, 0)]
require(kernel == [(0, q * k) for k in range(q)], "kernel")
require(all(gm(g, (0, q)) == gm((0, q), g) for g in group), "central kernel generator")
require(gm((0, 1), (1, 0)) != gm((1, 0), (0, 1)), "nonabelian quotient action")
lifts = [g for g in group if proj(g) == (0, 1)]
require(lifts == [(0, 1 + q * k) for k in range(q)], "all prescribed lifts")
lift_powers = [power(g, q, gm, (0, 0)) for g in lifts]
require(lift_powers == [(0, q)] * q, "eleventh powers of all lifts")
expected_failure("splitting_section", (0, 0) in lift_powers, "NONIDENTITY_11TH_POWER")

cosets11 = [(frozenset({x}), 11) for x in range(11)]
cosets11.append((frozenset(range(11)), 1))
require(all(math.gcd(a[1], b[1]) > 7
            for a, b in itertools.combinations(cosets11, 2)
            if a[0].isdisjoint(b[0])), "B7(C11)<=1")
expected_failure("strict_gcd_threshold_mutation", math.gcd(11, 11) > 11,
                 "GCD_EQUALS_THRESHOLD")
checks["nonsplit_semidirect"] = {"group_order": len(group), "quotient_order": len(quotient),
                                 "kernel_order": len(kernel), "lifts_of_0_1": len(lifts),
                                 "each_lift_eleventh_power": [0, q],
                                 "B7_C11_le_1": True}

print(json.dumps({"status": "PASS", "checks": checks, "intended_reason_negatives": negatives},
                 sort_keys=True, indent=2))
