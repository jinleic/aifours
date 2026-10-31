#!/usr/bin/env python3
"""Bounded exact check: one Rees source with nonclosed idempotents and q fibres.

Uses original multiplication and natural-order definition, plus the complete
syntactic congruence, not any theorem about Rees matrices.  A coordinate-collapse
negative control must fail the named injectivity predicate. No I/O or network.
"""
from itertools import product


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def main():
    I = range(3)
    L = range(3)
    G = range(2)
    S = list(product(I, G, L))
    sandwich = ((0, 0, 0), (0, 0, 0), (0, 0, 1))

    def mul(s, t):
        i, g, lam = s
        j, h, mu = t
        return (i, (g + sandwich[lam][j] + h) % 2, mu)

    def ctx(x, s, y):
        value = s if x is None else mul(x, s)
        return value if y is None else mul(value, y)

    require(all(mul(mul(a, b), c) == mul(a, mul(b, c))
                for a, b, c in product(S, repeat=3)), "associativity")
    E = [s for s in S if mul(s, s) == s]
    require(all(any(mul(mul(a, b), a) == a and mul(mul(b, a), b) == b
                    for b in S) for a in S), "regularity")
    failure = next(((e, f, mul(e, f)) for e, f in product(E, repeat=2)
                    if mul(e, f) not in E), None)
    require(failure is not None, "expected E nonclosure")
    for e in E:
        corner = {mul(mul(e, s), e) for s in S}
        require(all(mul(e, x) == x == mul(x, e) for x in corner), "corner identity")
        require(all(any(mul(x, y) == e == mul(y, x) for y in corner)
                    for x in corner), "corner group")

    for e, a in product(E, S):
        below = any(mul(f, a) == e == mul(a, g) for f, g in product(E, repeat=2))
        require(not below or a in E, "weak E-unitarity")

    contexts = [None] + S
    tau = {(a, b) for a, b in product(S, repeat=2)
           if all((ctx(x, a, y) in E) == (ctx(x, b, y) in E)
                  for x, y in product(contexts, repeat=2))}
    require(all((a, a) in tau for a in S), "tau reflexive")
    require(all(((a, b) in tau) == ((b, a) in tau) for a, b in product(S, repeat=2)),
            "tau symmetric")
    require(all((a, c) in tau for a, b, c in product(S, repeat=3)
                if (a, b) in tau and (b, c) in tau), "tau transitive")
    require(all((mul(a, x), mul(b, x)) in tau and (mul(x, a), mul(x, b)) in tau
                for a, b, x in product(S, repeat=3) if (a, b) in tau), "tau congruence")
    classes = []
    class_of = {}
    for a in S:
        if a not in class_of:
            members = [b for b in S if (a, b) in tau]
            index = len(classes)
            classes.append(members)
            for b in members:
                class_of[b] = index

    require(all((class_of[mul(a, a)] == class_of[a]) == (a in E) for a in S),
            "q idempotent purity")
    require(all(any(mul(mul(x, a), y) == b for x, y in product(S, repeat=2))
                for a, b in product(S, repeat=2)), "source simplicity")
    has_identity = any(all(mul(e, a) == a == mul(a, e) for a in S) for e in E)
    require(not has_identity, "expected nonmonoid")

    same_q = [(e, f) for e, f in product(E, repeat=2)
              if e != f and class_of[e] == class_of[f]]
    rp = [(e, f) for e, f in same_q if mul(e, f) == f and mul(f, e) == e]
    lp = [(e, f) for e, f in same_q if mul(e, f) == e and mul(f, e) == f]
    require(rp and lp, "expected nontrivial same-q R/L pairs")

    def rect(a, b):
        return (a[0], b[1])

    def check(beta):
        require(all(beta(mul(a, b)) == rect(beta(a), beta(b))
                    for a, b in product(S, repeat=2)), "rectangular homomorphism")
        require(len({(beta(a), class_of[a]) for a in S}) == len(S), "host injectivity")
        require(all(beta(e) != beta(f) for e, f in rp + lp), "R/L separation")

    def beta(a):
        return (a[0], a[2])

    check(beta)
    try:
        check(lambda a: (0, a[2]))
    except ValueError as error:
        require(str(error) == "host injectivity", "unexpected negative-control reason")
        negative = str(error)
    else:
        raise ValueError("negative control unexpectedly passed")

    print("source_size=", len(S), " idempotents=", len(E), " tau_quotient_size=", len(classes), sep="")
    print("nonidempotent_product_of_idempotents=", failure, sep="")
    print("same_q_ordered_distinct_idempotent_pairs=", len(same_q), sep="")
    print("ordered_R_pairs=", len(rp), " ordered_L_pairs=", len(lp), sep="")
    print("PASS associativity, regularity, nonmonoid, local_group, WEU, source_simple")
    print("PASS tau_equivalence_congruence, pure_actual_q, explicit_rectangular_host, R/L_separation")
    print("CONTROL intentional-row-collapse rejected:", negative)
    print("SCOPE: one finite 18-element Rees source; no universal theorem or novelty verified")


if __name__ == "__main__":
    main()
