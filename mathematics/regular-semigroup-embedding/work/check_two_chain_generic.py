"""Check Theorem 4 on Z2-graded semigroups produced by the GENERIC SAT enumerator (enum_extensions.py),
i.e. without assuming the structural normal form used to generate instances in
check_two_chain_theorem.py.  For each input table S (E = {0..n-1} even part, A = rest odd part):
  1. verify S is associative, regular, orthodox, E-unitary with sigma = parity, E a band with two
     D-classes (Step 1 of the proof);
  2. extract the rectangular-group coordinates of the two J-classes and the maps Phi, Psi,
     and verify the normal form Phi_(r,h,l) = pi_r o sigma_h o p_l, Psi_(r,h,l) = pi'_l o sigma'_h o p'_r
     (Steps 2-3 of the proof);
  3. run the construction of Step 4-5 (B0, F) and verify that it yields an embedding into B0^G x| G.

Usage: python3 work/check_two_chain_generic.py file1.json [file2.json ...]
       (each file holds one table or a list of tables)
"""
from __future__ import annotations

import json
import sys

from check_two_chain_theorem import (band_locally_regular, band_regular, check_semigroup_properties,
                                     construct_and_check, cyclic, d_classes)


def extract(T):
    N = len(T)
    E = [x for x in range(N) if T[x][x] == x]
    n = len(E)
    assert E == list(range(n))
    sigma = [0] * n + [1] * (N - n)
    Gt = cyclic(2)
    check_semigroup_properties(T, sigma, Gt, 0)
    dcl = d_classes(T, E)
    assert len(dcl) == 2, f"band has {len(dcl)} D-classes"
    c0, c1 = dcl
    if all(T[x][y] in set(c0) for x in c1 for y in c0):
        top, bot = c1, c0
    else:
        top, bot = c0, c1
    tops, bots = set(top), set(bot)

    def inv(x):
        return next(y for y in range(N) if T[T[x][y]][x] == x and T[T[y][x]][y] == y)

    def rows_cols(cls):
        rows, cols = [], []
        for e in cls:
            r = frozenset(f for f in cls if T[e][f] == f and T[f][e] == e)
            c = frozenset(f for f in cls if T[e][f] == e and T[f][e] == f)
            if r not in rows:
                rows.append(r)
            if c not in cols:
                cols.append(c)
        return rows, cols

    trows, tcols = rows_cols(top)
    brows, bcols = rows_cols(bot)

    def coords(x):
        xp = inv(x)
        a, b = T[x][xp], T[xp][x]
        if a in tops:
            return ("t", next(k for k, r in enumerate(trows) if a in r), sigma[x], next(k for k, c in enumerate(tcols) if b in c))
        return ("b", next(k for k, r in enumerate(brows) if a in r), sigma[x], next(k for k, c in enumerate(bcols) if b in c))

    elems = [coords(x) for x in range(N)]
    assert len(set(elems)) == N, "coordinates not injective (H-classes of S must meet sigma-classes once)"
    H1 = sorted({x[2] for x in elems if x[0] == "t"})
    I1, L1, I2, L2 = len(trows), len(tcols), len(brows), len(bcols)
    find = {c: k for k, c in enumerate(elems)}
    # sanity: every coordinate tuple with group part in H1 (top) / G (bottom) occurs
    for r in range(I1):
        for h in H1:
            for l in range(L1):
                assert ("t", r, h, l) in find
    for i in range(I2):
        for g in (0, 1):
            for j in range(L2):
                assert ("b", i, g, j) in find

    def Phi(r, h, l):
        x = find[("t", r, h, l)]
        out = []
        for i in range(I2):
            z = find[("b", i, 0, 0)]
            c = elems[T[x][z]]
            assert c[0] == "b" and c[3] == 0 and c[2] == h
            # independence of the column/parity of z
            for g in (0, 1):
                for j in range(L2):
                    c2 = elems[T[x][find[("b", i, g, j)]]]
                    assert c2 == ("b", c[1], (h + g) % 2, j), "x z not of the form (Phi_x(i), hk, j)"
            out.append(c[1])
        return out

    def Psi(r, h, l):
        x = find[("t", r, h, l)]
        out = []
        for j in range(L2):
            z = find[("b", 0, 0, j)]
            c = elems[T[z][x]]
            for g in (0, 1):
                for i in range(I2):
                    c2 = elems[T[find[("b", i, g, j)]][x]]
                    assert c2 == ("b", i, (g + h) % 2, c[3]), "z x not of the form (i, kh, Psi_x(j))"
            out.append(c[3])
        return out

    # normal form, reference row/column 0 and identity element 0 of the group
    p = [dict(enumerate(Phi(0, 0, l))) for l in range(L1)]
    J = sorted(set(p[0].values()))
    pi = [dict((j, Phi(r, 0, 0)[j]) for j in J) for r in range(I1)]
    sig = {h: tuple(J.index(Phi(0, h, 0)[j]) for j in J) for h in H1}
    for r in range(I1):
        for h in H1:
            for l in range(L1):
                ph = Phi(r, h, l)
                pred = [pi[r][J[sig[h][J.index(p[l][i])]]] for i in range(I2)]
                assert ph == pred, "normal form Phi = pi sigma p fails"
    pc = [dict(enumerate(Psi(r, 0, 0))) for r in range(I1)]
    Jc = sorted(set(pc[0].values()))
    pic = [dict((j, Psi(0, 0, l)[j]) for j in Jc) for l in range(L1)]
    sigc = {h: tuple(Jc.index(Psi(0, h, 0)[j]) for j in Jc) for h in H1}
    for r in range(I1):
        for h in H1:
            for l in range(L1):
                ps = Psi(r, h, l)
                pred = [pic[l][Jc[sigc[h][Jc.index(pc[r][j])]]] for j in range(L2)]
                assert ps == pred, "normal form Psi = pi' sigma' p' fails"
    d = dict(Gt=Gt, e=0, ginv=[0, 1], H1=H1, I1=I1, L1=L1, I2=I2, L2=L2, J=J, pi=pi, p=p, Jc=Jc,
             pic=pic, pc=pc, sig=sig, sigc=sigc, elems=elems)
    return sigma, d, E


def main() -> None:
    total = 0
    nonreg = 0
    for fn in sys.argv[1:]:
        data = json.load(open(fn))
        tables = data if isinstance(data[0][0], list) else [data]
        for T in tables:
            sigma, d, E = extract(T)
            assert band_locally_regular(T, E)
            nr = not band_regular(T, E)
            M = construct_and_check(T, sigma, d)
            total += 1
            nonreg += nr
            print(f"{fn}: |S|={len(T)} |E|={len(E)} |H1|={len(d['H1'])} E regular={not nr} |B0|={M}: embedding verified")
    print(f"GENERIC ALL OK: {total} semigroups ({nonreg} with non-regular band)")


if __name__ == "__main__":
    main()
