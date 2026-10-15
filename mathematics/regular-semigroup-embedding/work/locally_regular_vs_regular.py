"""Is the variety L(ReB) of bands all of whose local submonoids eBe are regular equal to ReB?

L(ReB) is defined by  e z e x e y e z e = e z e x e z e y e z e  (regular identity a x y a = a x a y a
inside eBe, with a = eze, x -> exe, y -> eye).  ReB is defined by  a x y a = a x a y a.
We compute the verbal congruences of both identities on the free band FB(n) and compare.

Usage: uv run --with numpy python work/locally_regular_vs_regular.py [n]
"""
from __future__ import annotations

import sys

import numpy as np

from freeband import can, congruence_closure, free_band


def regular_pairs(mult):
    m = mult.shape[0]
    A = np.arange(m)
    pairs = []
    for a in range(m):
        # a x y a  vs  a x a y a, vectorised over x, y
        ax = mult[a, A]  # a x
        axy = mult[ax[:, None], A[None, :]]  # a x y
        lhs = mult[axy, a]
        axa = mult[ax, a]
        axay = mult[axa[:, None], A[None, :]]
        rhs = mult[axay, a]
        d = lhs != rhs
        if d.any():
            pairs.append(np.stack([lhs[d], rhs[d]], axis=1))
    return np.unique(np.sort(np.concatenate(pairs), axis=1), axis=0) if pairs else np.zeros((0, 2), int)


def locally_regular_pairs(mult):
    m = mult.shape[0]
    A = np.arange(m)
    ea = set()
    for e in range(m):
        for z in range(m):
            ea.add((e, int(mult[mult[e, z], e])))
    pairs = []
    for e, a in sorted(ea):
        # a x e y a  vs  a x a y a  (a <= e)
        ax = mult[a, A]
        axe = mult[ax, e]
        axey = mult[axe[:, None], A[None, :]]
        lhs = mult[axey, a]
        axa = mult[ax, a]
        axay = mult[axa[:, None], A[None, :]]
        rhs = mult[axay, a]
        d = lhs != rhs
        if d.any():
            pairs.append(np.stack([lhs[d], rhs[d]], axis=1))
    return np.unique(np.sort(np.concatenate(pairs), axis=1), axis=0) if pairs else np.zeros((0, 2), int)


def main(n: int) -> None:
    elems, index, mult = free_band(n)
    gens = [index[(i,)] for i in range(n)]
    print(f"|FB({n})| = {len(elems)}")
    lab_reg = congruence_closure(mult, gens, regular_pairs(mult))
    lab_loc = congruence_closure(mult, gens, locally_regular_pairs(mult))
    print(f"|F_ReB({n})|    = {len(set(lab_reg))}")
    print(f"|F_L(ReB)({n})| = {len(set(lab_loc))}")
    if n >= 3:
        x, y, z = 0, 1, 2
        u = index[can((x, y, z, x))]
        v = index[can((x, y, x, z, x))]
        print("xyzx = xyxzx holds in L(ReB)?", lab_loc[u] == lab_loc[v])
    # every regular-identity consequence must hold in ReB-quotient; check inclusion of congruences
    incl = all(lab_reg[i] == lab_reg[j] for i in range(len(elems)) for j in range(len(elems))
               if lab_loc[i] == lab_loc[j]) if len(elems) < 400 else None
    print("ker(L(ReB)) subset of ker(ReB):", incl)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
