#!/usr/bin/env python3
"""Bounded independent exact controls; these do not prove imported theorems."""
import datetime
import itertools
import json
import math

CAP = 300_000


def stamp():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def is_prime(a):
    return a >= 2 and all(a % d for d in range(2, math.isqrt(a) + 1))


def factors(a):
    result = []
    d = 2
    while d * d <= a:
        if a % d == 0:
            result.append(d)
            while a % d == 0:
                a //= d
        d += 1
    if a > 1:
        result.append(a)
    return result


def primitive(p, d):
    """Return first prime r <= CAP with ord_r(p)=d, else UNKNOWN."""
    for k in range(1, (CAP - 1) // d + 1):
        r = k * d + 1
        if is_prime(r) and pow(p, d, r) == 1 and all(
            pow(p, d // ell, r) != 1 for ell in factors(d)
        ):
            return r
    return None


def order_mod(p, r):
    if math.gcd(p, r) != 1:
        return None
    x = 1
    for d in range(1, r):
        x = x * p % r
        if x == 1:
            return d
    raise AssertionError("Fermat bound failed")


def group_order(n, q):
    numerator = q ** (n * (n - 1) // 2)
    for j in range(2, n + 1):
        numerator *= q**j - (-1)**j
    center = math.gcd(n, q + 1)
    assert numerator % center == 0
    return numerator // center


def beta(p, f, m, r):
    return all(pow(p, m * (f // k), r) != r - 1
               for k in factors(f) if k != 2 and k != r)


def divisors_at_least_eight(number):
    result = set()
    for d in range(1, math.isqrt(number) + 1):
        if number % d == 0:
            if d >= 8:
                result.add(d)
            if number // d >= 8:
                result.add(number // d)
    return sorted(result)


def graph_clique(values):
    """Exact pivoted Bron-Kerbosch over distinct numerical divisors."""
    ns = len(values)
    adj = [0] * ns
    for i in range(ns):
        for j in range(i + 1, ns):
            g = math.gcd(values[i], values[j])
            if 2 <= g <= 7:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    best = []
    nodes = 0

    def visit(chosen, possible, excluded):
        nonlocal best, nodes
        nodes += 1
        if len(chosen) + possible.bit_count() <= len(best):
            return
        if not possible and not excluded:
            if len(chosen) > len(best):
                best = chosen[:]
            return
        universe = possible | excluded
        pivot = max((i for i in range(ns) if universe & (1 << i)),
                    key=lambda i: (possible & adj[i]).bit_count())
        remaining = possible & ~adj[pivot]
        while remaining:
            bit = remaining & -remaining
            v = bit.bit_length() - 1
            visit(chosen + [v], possible & adj[v], excluded & adj[v])
            possible &= ~bit
            excluded |= bit
            remaining &= ~bit
            if len(chosen) + possible.bit_count() <= len(best):
                break

    visit([], (1 << ns) - 1, 0)
    clique = [values[i] for i in best]
    assert all(2 <= math.gcd(a, b) <= 7
               for a, b in itertools.combinations(clique, 2))
    return {"divisors": ns, "max_clique": len(clique), "witness": clique,
            "search_nodes": nodes}


def cosets_s3_control():
    elements = list(itertools.permutations(range(3)))
    identity = (0, 1, 2)
    h = {identity, (1, 2, 0), (2, 0, 1)}
    k = {identity, (1, 0, 2)}

    def mul(a, b):
        return tuple(a[b[i]] for i in range(3))

    hs = {frozenset(mul(g, x) for x in h) for g in elements}
    ks = {frozenset(mul(g, x) for x in k) for g in elements}
    assert len(hs) == 2 and len(ks) == 3
    assert all(a & b for a in hs for b in ks)
    assert any({mul(mul(g, x), tuple(g.index(i) for i in range(3)))
                for x in k} != k for g in elements)
    return {"group": "S3", "indices": [2, 3], "left_coset_pairs": 6,
            "all_pairs_intersect": True, "index_3_subgroup_nonnormal": True}


started = stamp()
endpoints = [(3, 3, 6048), (3, 5, 126000), (4, 2, 25920),
             (4, 3, 3265920), (5, 2, 13685760)]
orders = []
for n, q, expected in endpoints:
    actual = group_order(n, q)
    assert actual == expected
    orders.append({"n": n, "q": q, "order": actual,
                   "factors": factors(actual),
                   "v7": next((v for v in range(1, 20)
                               if actual % (7**v)), 20) - 1,
                   "clique": graph_clique(divisors_at_least_eight(actual))})
    assert orders[-1]["clique"]["max_clique"] < 8

nonprime = []
for n in (3, 4, 5, 6, 7, 8, 9, 10):
    m = n if n % 2 else n - 1
    for p in (2, 3, 5):
        for f in (2, 3):
            exponent = 2 * m * f
            r = primitive(p, exponent)
            if r is None:
                nonprime.append({"n": n, "p": p, "f": f,
                                 "status": "UNKNOWN_AT_CAP"})
                continue
            q = p**f
            assert is_prime(r) and order_mod(p, r) == exponent
            assert order_mod(q, r) == 2 * m and r > 7
            assert beta(p, f, m, r)
            assert (q**m + 1) % r == 0 and group_order(n, q) % r == 0
            assert ((q**m + 1) % (r*r) == 0) == (group_order(n, q) % (r*r) == 0)
            nonprime.append({"n": n, "p": p, "f": f, "r": r,
                             "base_order": exponent, "status": "PASS"})

prime_fields = []
for n in (3, 4, 5, 6, 7, 8, 9, 10):
    m = n if n % 2 else n - 1
    for p in (2, 3, 5, 7, 11, 233):
        d = 2 * m
        r = primitive(p, d)
        if r is None:
            status = "ZS_EXCEPTION" if (p, d) == (2, 6) else "UNKNOWN_AT_CAP"
            prime_fields.append({"n": n, "p": p, "status": status})
            continue
        assert is_prime(r) and order_mod(p, r) == d
        assert beta(p, 1, m, r)
        assert (p**m + 1) % r == 0 and group_order(n, p) % r == 0
        square = (p**m + 1) % (r*r) == 0
        assert square == (group_order(n, p) % (r*r) == 0)
        threshold = 2*n + 1 if n % 2 else 2*n - 1
        if not is_prime(threshold):
            assert r != threshold
        prime_fields.append({"n": n, "p": p, "r": r,
                             "threshold": threshold, "r_squared": square,
                             "small_source_exception": (n, p) in
                                 {(3, 3), (3, 5), (4, 2), (4, 3), (5, 2), (6, 2)},
                             "status": "PASS"})

# Negative controls detect source/order/beta/coset mistakes; they are NOT counterexamples to Sun8.
assert group_order(4, 3) == 3265920
assert math.gcd(4, 3 + 1) * group_order(4, 3) == 13063680
assert order_mod(7**5, 43) == 6 and not beta(7, 5, 3, 43)
assert pow(7, 3, 43) == 42
assert order_mod(2, 11) == 10 and (2**5 + 1) % 11 == 0
assert (2**5 + 1) % 121 != 0
assert order_mod(233, 11) == 10 and (233**5 + 1) % 121 == 0
assert group_order(5, 233) % 121 == 0 and group_order(6, 233) % 121 == 0
assert (-11) % 2 == 1  # 1 is a square modulo 2; source exception matters.
faults = {
    "omit_center": {"n": 4, "q": 3, "correct": 3265920,
                    "incorrect_uncancelled": 13063680, "detected": True},
    "primitive_over_q_does_not_imply_beta": {
        "p": 7, "f": 5, "m": 3, "r": 43,
        "ord_r_q": 6, "k": 5, "p_to_mf_over_k_mod_r": 42,
        "beta": False, "detected": True},
    "r_divides_does_not_imply_r_squared": {
        "p": 2, "m": 5, "r": 11, "p_to_m_plus_1": 33,
        "mod_r_squared": 33, "detected": True},
    "squared_positive": {"p": 233, "m": 5, "r": 11,
                         "p_to_m_plus_1": 233**5 + 1,
                         "divides_both_PSU5_and_PSU6_orders": True},
    "source_small_cases": {
        "U5_2_and_U6_2": "ord_11(2)=10; beta vacuous; -11 is 1 mod 2; f=1",
        "table_square_branch_if_literal": True,
        "proposition_6_4_treats_separately": True},
    "coprime_indices": cosets_s3_control(),
}
print(json.dumps({"clock_start": started, "clock_end": stamp(), "search_cap": CAP,
                  "orders_and_divisor_graphs": orders,
                  "nonprime_fields": nonprime,
                  "prime_fields": prime_fields,
                  "fault_controls": faults}, indent=2, sort_keys=True))
