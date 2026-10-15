"""Reduced deg-lex Groebner-Shirshov basis of a finite-type Artin group in the
Artin-Garside generators, computed from the Garside normal-form oracle.

For a deg-lex order the irreducible words of the (unique) reduced GS basis
are the deg-lex-smallest words of their group elements, and the reduced GS
basis is {u -> NF(u) : u reducible, every proper factor of u irreducible}.
This script enumerates that set for leading words of length <= L by a
breadth-first search over irreducible words (independent of any rewriting
or completion procedure).

Usage: python3 work/gs_oracle.py TYPE n [m] L [--positive] [--order 0,1,2]
Output: JSON lines to stdout: {"lhs":..., "rhs":...}, then a summary line
with the irreducible-word counts by length.
"""
from __future__ import annotations

import argparse
import json
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from coxeter import DELTA, DINV, build, letter  # noqa: E402


def series_mul(a, b, L):
    c = [0] * (L + 1)
    for i, x in enumerate(a[: L + 1]):
        if x:
            for j, y in enumerate(b[: L + 1 - i]):
                c[i + j] += x * y
    return c


def series_inv(a, L):
    assert a[0] == 1
    b = [0] * (L + 1)
    b[0] = 1
    for k in range(1, L + 1):
        b[k] = -sum(a[j] * b[k - j] for j in range(1, min(k, len(a) - 1) + 1))
    return b


def growth_counts(W, L, mode="group"):
    """Coefficients of growth series, from M(t) = 1 / sum_{T subset S} (-1)^{|T|} t^{N_T}
    (Deligne/Saito formula for the Artin monoid; N_T = number of positive roots of W_T):
      mode="monoid":   M(t)                         (all positive elements)
      mode="positive": (1 - t^N) M(t)               (Delta-free positive elements)
      mode="group":    (1 - t^N) M(t) (1+t)/(1-t)   (group, generators {s_i, Delta^{+-1}})."""
    from itertools import combinations

    from coxeter import Coxeter

    n = W.n
    den = [0] * (max(L, W.N) + 1)
    for r in range(n + 1):
        for T in combinations(range(n), r):
            if T:
                MT = [[W.M[i][j] for j in T] for i in T]
                NT = Coxeter(MT).N
            else:
                NT = 0
            if NT <= L:
                den[NT] += (-1) ** r
    Mser = series_inv(den, L)
    one_minus = [0] * (L + 1)
    one_minus[0] = 1
    if W.N <= L:
        one_minus[W.N] = -1
    if mode == "monoid":
        return Mser
    F = series_mul(Mser, one_minus, L)
    if mode == "positive":
        return F
    geo = [1] + [2] * L  # (1+t)/(1-t)
    return series_mul(F, geo, L)


def enumerate_basis(G, L, positive=False, monoid=False):
    """Reduced deg-lex GS basis restricted to leading words of length <= L.
    positive: only words over the Artin generators (group normal form);
    monoid: the Artin monoid A^+(W) itself (no Delta letters; NF = lexmin)."""
    W = G.W
    gens = [letter(i) for i in range(W.n)]
    alphabet = gens if (positive or monoid) else [DINV, DELTA] + gens
    if monoid:
        start = []

        def step(st, y):
            return G.times_atom(st, ord(y) - ord("a"))

        def nf(st):
            return G.lexmin(st)
    else:
        start = (0, [])
        step = G.group_mul_letter
        nf = G.nf_state
    level = {"": start}
    irr_counts = [1]
    rules = []
    for length in range(1, L + 1):
        nxt = {}
        for w, st in level.items():
            for y in alphabet:
                u = w + y
                if u[1:] not in level:
                    continue
                st2 = step(st, y)
                v = nf(st2)
                if v == u:
                    nxt[u] = st2
                else:
                    rules.append((u, v))
        level = nxt
        irr_counts.append(len(level))
    return rules, irr_counts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("typ")
    ap.add_argument("n", type=int)
    ap.add_argument("L", type=int)
    ap.add_argument("--m", type=int, default=0)
    ap.add_argument("--positive", action="store_true")
    ap.add_argument("--monoid", action="store_true")
    ap.add_argument("--order", default=None)
    a = ap.parse_args()
    order = [int(x) for x in a.order.split(",")] if a.order else None
    G = build(a.typ, a.n, a.m, order)
    rules, counts = enumerate_basis(G, a.L, a.positive, a.monoid)
    for lhs, rhs in sorted(rules, key=lambda r: (len(r[0]), r[0])):
        print(json.dumps({"lhs": lhs, "rhs": rhs}))
    mode = "monoid" if a.monoid else ("positive" if a.positive else "group")
    expected = growth_counts(G.W, a.L, mode)
    print(json.dumps({"summary": True, "type": a.typ, "n": a.n, "m": a.m, "L": a.L,
                      "mode": mode, "order": order, "delta": G.delta_word(),
                      "phi": G.W.phi, "irreducible_counts": counts,
                      "growth_formula": expected, "match": counts == expected,
                      "nrules": len(rules)}))


if __name__ == "__main__":
    main()
