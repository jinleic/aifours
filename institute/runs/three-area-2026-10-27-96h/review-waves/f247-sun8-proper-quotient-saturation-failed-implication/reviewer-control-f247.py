#!/usr/bin/env python3
"""Reviewer-owned finite arithmetic controls, not a proof of the general case."""
import itertools
import json
import math

PRIMES = (11, 13, 17, 19, 23, 29, 31, 37, 41)


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def divisor_products(primes):
    products = [1]
    for prime in primes:
        products += [prime * x for x in products]
    return products


def crt_original(q, layer):
    # Unique residue modulo 7*q with the specified 7-layer and q-residue 0.
    return (q * ((layer * pow(q, -1, 7)) % 7)) % (7 * q)


def meet(d, a, e, b):
    # Two cyclic residue classes meet exactly when residues agree mod gcd.
    return (a - b) % math.gcd(d, e) == 0


def bad_indices(indices):
    return all(math.gcd(a, b) <= 7 for a, b in itertools.combinations(indices, 2))


def largest_disjoint_support_family(m):
    # Complete exact DP over partitions of prime-support masks; only nonempty
    # supports represent proper subgroups. Repetition can never be bad.
    best = [0] * (1 << m)
    for mask in range(1, 1 << m):
        sub = mask
        while sub:
            best[mask] = max(best[mask], 1 + best[mask ^ sub])
            sub = (sub - 1) & mask
    return best[-1]


def first_bad_quotient_pair(primes):
    divisors = divisor_products(primes)
    for a in divisors:
        for b in divisors:
            gcd = math.gcd(a, b)
            if 1 < gcd <= 7:
                # 0 mod a and 1 mod b are disjoint and have bad gcd.
                assert not meet(a, 0, b, 1)
                return {"indices": [a, b], "residues": [0, 1], "gcd": gcd}
    return None


def run_case(m):
    primes = PRIMES[:m]
    assert len(set(primes)) == m and all(is_prime(q) and q > 7 for q in primes)
    q_order = math.prod(primes)
    group_order = 7 * q_order
    originals = [(7 * primes[i], crt_original(primes[i], i)) for i in range(7)]
    for i, (d, a) in enumerate(originals):
        assert d == 7 * primes[i] and a % 7 == i and a % primes[i] == 0
    for (d, a), (e, b) in itertools.combinations(originals, 2):
        assert math.gcd(d, e) == 7 and not meet(d, a, e, b)
    assert all(math.gcd(a, b) == 1 for a, b in itertools.combinations(primes[:7], 2))

    # In the fibre over Q=0, check all seven elements and their unique cosets.
    for layer in range(7):
        fibre_point = (q_order * ((layer * pow(q_order, -1, 7)) % 7)) % group_order
        assert fibre_point % q_order == 0 and fibre_point % 7 == layer
        members = [i for i, (d, a) in enumerate(originals) if fibre_point % d == a]
        assert members == [layer]

    q_divisors = divisor_products(primes)
    for i, a in enumerate(q_divisors):
        for j, b in enumerate(q_divisors):
            gcd = math.gcd(a, b)
            assert gcd == 1 or gcd > 7
            assert (gcd == 1) == ((i & j) == 0)
    assert first_bad_quotient_pair(primes) is None
    assert largest_disjoint_support_family(m) == m
    assert bad_indices(primes)

    # Whole-group indices: every nontrivial gcd at most 7 is exactly 7.
    g_divisors = divisor_products((7,) + primes)
    for a in g_divisors:
        for b in g_divisors:
            gcd = math.gcd(a, b)
            assert gcd == 1 or gcd == 7 or gcd > 7
    # Under gcd 7, residue-class intersection depends only on the layer.
    for a, b in itertools.product(range(7), repeat=2):
        assert ((a - b) % 7 == 0) == (a == b)
    layer_classes = [(7, a) for a in range(7)]
    assert all(math.gcd(d, e) == 7 and not meet(d, a, e, b)
               for (d, a), (e, b) in itertools.combinations(layer_classes, 2))

    # Exhaust all actual cyclic cosets of every index that passes the seven
    # gcd upper bounds. This is finite even with the extra quotient primes.
    allowed_indices = [d for d in g_divisors
                       if all(math.gcd(d, e) <= 7 for e, _ in originals)]
    checked_cosets = 0
    for d in allowed_indices:
        for a in range(d):
            checked_cosets += 1
            assert any(meet(d, a, e, b) for e, b in originals), (d, a)

    # Negative 1: repeat the first layer for the second original coset.
    mutated_second = (7 * primes[1], crt_original(primes[1], 0))
    assert meet(*originals[0], *mutated_second)
    assert math.gcd(originals[0][0], mutated_second[0]) == 7

    # Negative 2: a real eighth disjoint coset exists if the gcd cap is dropped.
    d = 7 * primes[0]
    a = (7 * pow(7, -1, primes[0])) % d  # 0 mod 7, 1 mod q_1
    assert all(not meet(d, a, e, b) for e, b in originals)
    eighth_gcds = [math.gcd(d, e) for e, _ in originals]
    assert eighth_gcds[0] == d and eighth_gcds[0] > 7

    # Negative 3: a proper subgroup repeated in J gives a forbidden large gcd.
    assert not bad_indices([primes[0], primes[0]])
    assert math.gcd(primes[0], primes[0]) > 7

    return {
        "m": m,
        "primes": primes,
        "original_indices": [d for d, _ in originals],
        "quotient_max_bad_index_family": m,
        "fibre_points_checked": 7,
        "gcd_admissible_eighth_indices": sorted(allowed_indices),
        "gcd_admissible_eighth_cosets_exhausted": checked_cosets,
        "negative_repeated_layer": {"detected": "intersection", "gcd": 7},
        "negative_no_gcd_cap": {"disjoint_eighth_index": d, "residue": a,
                                "first_original_gcd": eighth_gcds[0]},
        "negative_repeated_proper_J_index": {"index": primes[0], "gcd": primes[0]},
    }


def main():
    cases = [run_case(m) for m in (7, 8, 9)]
    # Negative 4: allowing q=7 destroys B_7(Q)<=1. Q remains cyclic here.
    mutated = (7, 11, 13, 17, 19, 23, 29)
    witness = first_bad_quotient_pair(mutated)
    assert witness == {"indices": [7, 7], "residues": [0, 1], "gcd": 7}
    print(json.dumps({"status": "PASS", "cases": cases,
                      "negative_small_quotient_prime": witness,
                      "limits": "finite samples only; general proof is separate"},
                     indent=2))


if __name__ == "__main__":
    main()
