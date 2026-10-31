#!/usr/bin/env python3
"""Bounded exact check of Bicyclic x finite Rees actual quotient and host.

Infinite bicyclic labels are not truncated after multiplication; finite ranges
are only a check domain. Full proof of the arbitrary-actor claim is separate.
"""
from itertools import product


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def main():
    P = ((0, 0, 0), (0, 0, 0), (0, 0, 1))
    C = list(product(range(3), range(2), range(3)))
    B = list(product(range(2), repeat=2))
    S = list(product(B, C))

    def bm(a, b):
        i, j = a
        k, ell = b
        return (i + max(k-j, 0), ell + max(j-k, 0))

    def cm(a, b):
        i, g, lam = a
        j, h, mu = b
        return (i, (g + P[lam][j] + h) % 2, mu)

    def sm(a, b):
        return (bm(a[0], b[0]), cm(a[1], b[1]))

    def idem(a):
        return sm(a, a) == a

    def actor(a):
        (i, j), (row, g, col) = a
        return (i-j, int(row == 2), g, int(col == 2))

    # Direct finite-source contextual τ computation, including absent factors.
    ccontexts = [None] + C
    def cctx(x, c, y):
        z = c if x is None else cm(x, c)
        return z if y is None else cm(z, y)
    def cidem(c):
        return cm(c, c) == c
    sig_c = {a: bytes(cidem(cctx(x, a, y)) for x, y in product(ccontexts, repeat=2)) for a in C}
    def cq(c):
        return (int(c[0] == 2), c[1], int(c[2] == 2))
    require(all((sig_c[a] == sig_c[b]) == (cq(a) == cq(b)) for a, b in product(C, repeat=2)),
            "actual Rees tau")

    contexts = [None] + S
    def sctx(x, a, y):
        z = a if x is None else sm(x, a)
        return z if y is None else sm(z, y)
    sig = {a: bytes(idem(sctx(x, a, y)) for x, y in product(contexts, repeat=2)) for a in S}
    require(all((sig[a] == sig[b]) == (actor(a) == actor(b)) for a, b in product(S, repeat=2)),
            "bounded product tau")
    require(all((actor(a)[0] == 0 and cidem(a[1])) == idem(a) for a in S), "actor purity")

    # Tail A_k, source C rectangle (row,column); shift only the tail index.
    def beta(a):
        return (a[0][0], a[1][0], a[1][2])
    def bm_band(x, y):
        return (max(x[0], y[0]), x[1], y[2])
    def shifted(x, n):
        return (x[0] + n, x[1], x[2])
    for a, b in product(S, repeat=2):
        direct = beta(sm(a, b))
        expected = bm_band(beta(a), shifted(beta(b), actor(a)[0]))
        require(direct == expected, "physical band multiplication")
    require(len({(beta(a), actor(a)) for a in S}) == len(S), "host injectivity")

    E = [a for a in S if idem(a)]
    same_q = [(e, f) for e, f in product(E, repeat=2) if e != f and actor(e) == actor(f)]
    rp = [(e, f) for e, f in same_q if sm(e, f) == f and sm(f, e) == e]
    lp = [(e, f) for e, f in same_q if sm(e, f) == e and sm(f, e) == f]
    require(rp and lp, "missing R/L examples")
    require(all(beta(e) != beta(f) for e, f in rp+lp), "R/L separation")
    require(any(not idem(sm(e, f)) for e, f in product(E, repeat=2)), "E should not be closed")
    wrong = sum(beta(sm(a, b)) != bm_band(beta(a), shifted(beta(b), -actor(a)[0]))
                for a, b in product(S, repeat=2))
    require(wrong > 0, "wrong-action control")

    print("input_labels=", len(S), " bounded_contexts=", len(contexts)**2, sep="")
    print("finite_Rees_elements=", len(C), " Rees_tau_classes=", len(set(map(cq, C))), sep="")
    print("sample_idempotents=", len(E), " same_q_pairs=", len(same_q),
          " R_pairs=", len(rp), " L_pairs=", len(lp), sep="")
    print("PASS Rees_tau, bounded_product_tau, actor_purity, host_multiplication, injectivity, E_nonclosure")
    print("CONTROL wrong-shift mismatches=", wrong, sep="")
    print("SCOPE: finite label/context sample only; infinite tau and universal embedding require the written proof")


if __name__ == "__main__":
    main()
