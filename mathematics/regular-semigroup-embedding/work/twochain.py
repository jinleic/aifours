"""Bands whose structure semilattice is a 2-element chain ("2-chain bands"), and tools for them.

Model (proof.md, Section 4): B = T u D with T = I_t x L_t (top rectangular band) and D = I_b x L_b
(bottom rectangular band, an ideal).  For x = (r, l) in T and z = (i, j) in D:
    x z = (phi_x(i), j),     z x = (i, psi_x(j)),
and B is a band iff for all r, l, r', l':
    (F) phi_(r,l') = phi_(r,l) o phi_(r',l')        (G) psi_(r,l') = psi_(r',l') o psi_(r,l).
Every 2-chain band is locally regular (proof.md, Lemma 5); it is regular iff phi_(r,l) does not
depend on l and psi_(r,l) does not depend on r.
"""
from __future__ import annotations

import itertools


def build_table(It, Lt, Ib, Lb, phi, psi):
    """phi[(r,l)] = tuple over Ib, psi[(r,l)] = tuple over Lb.  Elements: top (r,l) then bottom (i,j)."""
    top = [(r, l) for r in range(It) for l in range(Lt)]
    bot = [(i, j) for i in range(Ib) for j in range(Lb)]
    elems = [("t",) + x for x in top] + [("b",) + z for z in bot]
    idx = {e: k for k, e in enumerate(elems)}
    N = len(elems)
    T = [[0] * N for _ in range(N)]
    for a, ea in enumerate(elems):
        for b, eb in enumerate(elems):
            if ea[0] == "t" and eb[0] == "t":
                T[a][b] = idx[("t", ea[1], eb[2])]
            elif ea[0] == "b" and eb[0] == "b":
                T[a][b] = idx[("b", ea[1], eb[2])]
            elif ea[0] == "t":
                T[a][b] = idx[("b", phi[(ea[1], ea[2])][eb[1]], eb[2])]
            else:
                T[a][b] = idx[("b", ea[1], psi[(eb[1], eb[2])][ea[2]])]
    return T, elems


def decompose(T, elems_idx=None):
    """Recover the 2-chain structure of a band table: returns dict or None if not a 2-chain band."""
    N = len(T) if elems_idx is None else None
    E = list(range(len(T))) if elems_idx is None else list(elems_idx)
    Es = set(E)
    # D-classes: e D f iff efe = e and fef = f
    dcl = []
    seen = set()
    for e in E:
        if e in seen:
            continue
        c = [f for f in E if T[T[e][f]][e] == e and T[T[f][e]][f] == f]
        dcl.append(c)
        seen.update(c)
    if len(dcl) != 2:
        return None
    # the bottom class is an ideal
    d0, d1 = dcl
    if all(T[x][y] in set(d0) for x in d1 for y in d0):
        top, bot = d1, d0
    elif all(T[x][y] in set(d1) for x in d0 for y in d1):
        top, bot = d0, d1
    else:
        return None

    def rect(cls):
        # rows = R-classes, cols = L-classes
        rows, cols = [], []
        for e in cls:
            r = frozenset(f for f in cls if T[e][f] == f and T[f][e] == e)
            c = frozenset(f for f in cls if T[e][f] == e and T[f][e] == f)
            if r not in rows:
                rows.append(r)
            if c not in cols:
                cols.append(c)
        coord = {}
        for e in cls:
            ri = next(k for k, r in enumerate(rows) if e in r)
            ci = next(k for k, c in enumerate(cols) if e in c)
            coord[e] = (ri, ci)
        return len(rows), len(cols), coord

    It, Lt, ct = rect(top)
    Ib, Lb, cb = rect(bot)
    inv_b = {v: k for k, v in cb.items()}
    phi, psi = {}, {}
    for x in top:
        r, l = ct[x]
        phi[(r, l)] = tuple(cb[T[x][inv_b[(i, 0)]]][0] for i in range(Ib))
        psi[(r, l)] = tuple(cb[T[inv_b[(0, j)]][x]][1] for j in range(Lb))
    return dict(top=top, bot=bot, It=It, Lt=Lt, Ib=Ib, Lb=Lb, ct=ct, cb=cb, phi=phi, psi=psi)


def check_band_axioms(It, Lt, Ib, Lb, phi, psi) -> bool:
    for r, l, r2, l2 in itertools.product(range(It), range(Lt), range(It), range(Lt)):
        if tuple(phi[(r, l)][phi[(r2, l2)][i]] for i in range(Ib)) != phi[(r, l2)]:
            return False
        if tuple(psi[(r2, l2)][psi[(r, l)][j]] for j in range(Lb)) != psi[(r, l2)]:
            return False
    return True
