#!/usr/bin/env python3
"""Exact bounded checks for one parametric regular-band-by-group monoid family.

Checks definitions directly with integer tuples, not the external embedding theorem.
No file, network, process or randomness access.  A broken band-coordinate map is
an intentional negative control and must fail exactly the homomorphism check.
"""
from itertools import product


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def band_product(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return (a[0], b[1])


def source_product(a, b):
    return (band_product(a[0], b[0]), (a[1] + b[1]) % 2)


def exercise():
    band = [None] + list(product(range(2), repeat=2))
    source = list(product(band, range(2)))
    unit = (None, 0)
    mul = source_product
    E = [a for a in source if mul(a, a) == a]

    require(all(mul(mul(a, b), c) == mul(a, mul(b, c))
                for a, b, c in product(source, repeat=3)), "associativity")
    require(all(mul(unit, a) == a == mul(a, unit) for a in source), "unit")
    require(all(any(mul(mul(a, b), a) == a and mul(mul(b, a), b) == b
                    for b in source) for a in source), "regularity")
    require(all(mul(a, b) in E for a, b in product(E, repeat=2)), "orthodoxy")

    for e in E:
        corner = {mul(mul(e, a), e) for a in source}
        corner_e = [x for x in corner if mul(x, x) == x]
        require(all(mul(x, y) in corner_e for x, y in product(corner_e, repeat=2)),
                "local orthodox")
        for x, y, z in product(corner_e, repeat=3):
            left = mul(mul(mul(mul(x, y), x), z), x)
            right = mul(mul(mul(x, y), z), x)
            require(left == right, "local regular band")

    for e, a in product(E, source):
        below = any(mul(f, a) == e == mul(a, g) for f, g in product(E, repeat=2))
        require(not below or a in E, "weak E-unitarity")

    def q(a):
        return a[1]

    require(all(q(mul(a, b)) == (q(a) + q(b)) % 2
                for a, b in product(source, repeat=2)), "q homomorphism")
    require(all((q(a) == 0) == (a in E) for a in source), "q purity")
    tau = {(a, b) for a, b in product(source, repeat=2)
           if all((mul(mul(x, a), y) in E) == (mul(mul(x, b), y) in E)
                  for x, y in product(source, repeat=2))}
    require(all(((a, b) in tau) == (q(a) == q(b))
                for a, b in product(source, repeat=2)), "syntactic kernel")

    require(all(band_product(x, x) == x for x in band), "target band")
    require(all(band_product(band_product(band_product(band_product(x, y), x), z), x)
                == band_product(band_product(band_product(x, y), z), x)
                for x, y, z in product(band, repeat=3)), "target regular band")

    def verify_host(beta):
        require(all(beta(mul(a, b)) == band_product(beta(a), beta(b))
                    for a, b in product(source, repeat=2)), "band-coordinate homomorphism")
        require(len({(beta(a), q(a)) for a in source}) == len(source), "host injectivity")
        return True

    def beta(a):
        return a[0]

    verify_host(beta)
    same_q = [(e, f) for e, f in product(E, repeat=2) if e != f and q(e) == q(f)]
    r_pairs = [(e, f) for e, f in same_q if mul(e, f) == f and mul(f, e) == e]
    l_pairs = [(e, f) for e, f in same_q if mul(e, f) == e and mul(f, e) == f]
    require(r_pairs and l_pairs, "missing genuine R/L idempotent pairs")
    require(all(beta(e) != beta(f) for e, f in r_pairs + l_pairs), "R/L separation")

    # Deliberate wrong map: merge one rectangular-band coordinate only.
    def broken_beta(a):
        e = a[0]
        return None if e is None else (0, e[1])

    try:
        verify_host(broken_beta)
    except ValueError as error:
        require(str(error) == "host injectivity", "unexpected negative-control reason")
        negative = str(error)
    else:
        raise ValueError("negative control unexpectedly passed")

    print("source_size=", len(source), "idempotents=", len(E), "q_image_size=2", sep="")
    print("same_q_ordered_distinct_idempotent_pairs=", len(same_q), sep="")
    print("ordered_R_pairs=", len(r_pairs), " ordered_L_pairs=", len(l_pairs), sep="")
    print("PASS associativity, unit, regularity, orthodoxy, local_r, WEU, q_pure, tau_kernel")
    print("PASS target_regular_band, host_homomorphism, injectivity, R/L_separation")
    print("CONTROL intentional-coordinate-merge rejected:", negative)
    print("SCOPE: one finite 10-element family instance only; no universal theorem or novelty verified")


if __name__ == "__main__":
    exercise()
