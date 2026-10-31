#!/usr/bin/env python3
"""Direct exact check of one non-simple, nonorthodox original-class cryptogroup.

S = M[C2;3,3;P] x a two-point meet-semilattice.  No external libraries,
randomness, file writes, network, solver, or inferred validity from a table hash.
"""
from itertools import product


def require(condition, label):
    if not condition:
        raise ValueError(label)


def main():
    P = ((0, 0, 0), (0, 0, 0), (0, 0, 1))
    S = list(product(range(3), range(2), range(3), range(2)))

    def mul(a, b):
        i, g, lam, level = a
        j, k, mu, other = b
        return (i, (g + P[lam][j] + k) % 2, mu, min(level, other))

    def beta(a):
        return (a[0], a[2], a[3])

    def bm(a, b):
        return (a[0], b[1], min(a[2], b[2]))

    require(all(mul(mul(a, b), c) == mul(a, mul(b, c))
                for a, b, c in product(S, repeat=3)), "associativity")
    E = [a for a in S if mul(a, a) == a]
    require(all(any(mul(mul(a, b), a) == a and mul(mul(b, a), b) == b
                    for b in S) for a in S), "regularity")
    failure = next(((a, b, mul(a, b)) for a, b in product(E, repeat=2)
                    if mul(a, b) not in E), None)
    require(failure is not None, "expected idempotent nonclosure")

    for e in E:
        corner = {mul(mul(e, a), e) for a in S}
        corner_e = [x for x in corner if mul(x, x) == x]
        require(all(mul(x, y) in corner_e for x, y in product(corner_e, repeat=2)),
                "local orthodox")
        require(all(mul(mul(mul(mul(x, y), x), z), x) == mul(mul(mul(x, y), z), x)
                    for x, y, z in product(corner_e, repeat=3)), "local regular band")
    for e, a in product(E, S):
        below = any(mul(f, a) == e == mul(a, g) for f, g in product(E, repeat=2))
        require(not below or a in E, "weak E-unitary")

    right = {a: frozenset([a] + [mul(a, x) for x in S]) for a in S}
    left = {a: frozenset([a] + [mul(x, a) for x in S]) for a in S}
    H = {(a, b) for a, b in product(S, repeat=2)
         if right[a] == right[b] and left[a] == left[b]}
    require(all(((a, b) in H) == (beta(a) == beta(b)) for a, b in product(S, repeat=2)),
            "H via principal ideals")
    require(all((mul(a, x), mul(b, x)) in H and (mul(x, a), mul(x, b)) in H
                for a, b, x in product(S, repeat=3) if (a, b) in H), "H congruence")
    require(all(any(mul(mul(a, b), a) == a and mul(mul(b, a), b) == b and (a, b) in H
                    for b in S) for a in S), "completely regular")
    require(all(beta(e) != beta(f) for e, f in product(E, repeat=2) if e != f),
            "idempotent separation by beta")
    band = set(map(beta, S))
    require(all(bm(x, x) == x for x in band), "band")
    require(all(bm(bm(bm(bm(x, y), x), z), x) == bm(bm(bm(x, y), z), x)
                for x, y, z in product(band, repeat=3)), "regular band")
    require(all(beta(mul(a, b)) == bm(beta(a), beta(b)) for a, b in product(S, repeat=2)),
            "beta homomorphism")

    def ctx(x, a, y):
        z = a if x is None else mul(x, a)
        return z if y is None else mul(z, y)

    C = [None] + S
    tau = {(a, b) for a, b in product(S, repeat=2)
           if all((ctx(x, a, y) in E) == (ctx(x, b, y) in E) for x, y in product(C, repeat=2))}
    require(all((a, c) in tau for a, b, c in product(S, repeat=3)
                if (a, b) in tau and (b, c) in tau), "tau transitivity")
    require(all((mul(a, x), mul(b, x)) in tau and (mul(x, a), mul(x, b)) in tau
                for a, b, x in product(S, repeat=3) if (a, b) in tau), "tau congruence")
    classes = []
    class_of = {}
    for a in S:
        if a not in class_of:
            index = len(classes)
            members = [b for b in S if (a, b) in tau]
            classes.append(members)
            for b in members:
                class_of[b] = index
    require(all((class_of[mul(a, a)] == class_of[a]) == (a in E) for a in S), "q purity")
    require(len({(beta(a), class_of[a]) for a in S}) == len(S), "host injectivity")
    require(all((class_of[mul(a, b)], beta(mul(a, b)))
                == (class_of[mul(a, b)], bm(beta(a), beta(b)))
                for a, b in product(S, repeat=2)), "host homomorphism")
    same_q = [(e, f) for e, f in product(E, repeat=2)
              if e != f and class_of[e] == class_of[f]]
    rp = [(e, f) for e, f in same_q if mul(e, f) == f and mul(f, e) == e]
    lp = [(e, f) for e, f in same_q if mul(e, f) == e and mul(f, e) == f]
    require(rp and lp, "nontrivial same-q R/L pairs")
    require(all(beta(e) != beta(f) for e, f in rp + lp), "R/L separation")
    ideal = {a for a in S if a[3] == 0}
    require(0 < len(ideal) < len(S), "proper ideal nonempty")
    require(all(mul(x, a) in ideal and mul(a, x) in ideal for x in S for a in ideal),
            "proper ideal")
    broken = lambda a: (0, a[2], a[3])
    require(all(broken(mul(a, b)) == bm(broken(a), broken(b))
                for a, b in product(S, repeat=2)), "negative control not homomorphic")
    require(len({(broken(a), class_of[a]) for a in S}) < len(S),
            "negative control unexpectedly injective")

    print("source_size=", len(S), " idempotents=", len(E), " H_classes=", len(band),
          " tau_quotient_size=", len(classes), sep="")
    print("proper_ideal_size=", len(ideal), " idempotent_nonclosure=", failure, sep="")
    print("same_q_idempotent_pairs=", len(same_q), " R_pairs=", len(rp), " L_pairs=", len(lp), sep="")
    print("PASS associativity, regularity, local_r, WEU, completely_regular, non-simple, E_nonclosed")
    print("PASS H_via_ideals, H_congruence, V_band_quotient, idempotent_separation, q_purity, host")
    print("CONTROL row-collapse remains homomorphic but fails host injectivity")
    print("SCOPE: one finite 36-element cryptogroup; no universal theorem or novelty verified")


if __name__ == "__main__":
    main()
