"""Independent brute-force checks of the band facts used in proof.md (no SAT, no shared code).

1. E5 (5-element band below) is a band, NOT regular, locally regular, left semiregular
   (L is a congruence, identity xyz = xyzxzyz), not right semiregular.
2. E5 with an identity adjoined is left semiregular but NOT locally regular
   (so LSRB is not contained in L(ReB)).
3. Every band of order <= 4 that is locally regular is regular (exhaustive backtracking
   enumeration of all labelled bands of order <= 4).  So 5 is the minimum order of a locally
   regular non-regular band.
4. The free band FB(3) (159 elements, Green-Rees normal form re-implemented here) is locally
   regular and not regular.

Usage: python3 work/check_band_facts.py
"""
from __future__ import annotations

import itertools
import sys

E5 = [[0, 1, 4, 3, 4],
      [0, 1, 3, 3, 4],
      [2, 2, 2, 2, 2],
      [3, 3, 3, 3, 3],
      [4, 4, 4, 4, 4]]


def p(T, *xs):
    v = xs[0]
    for x in xs[1:]:
        v = T[v][x]
    return v


def is_band(T):
    n = len(T)
    return all(T[x][x] == x for x in range(n)) and all(
        T[T[x][y]][z] == T[x][T[y][z]] for x in range(n) for y in range(n) for z in range(n))


def regular_witness(T, elems):
    for a, x, y in itertools.product(elems, repeat=3):
        if p(T, a, x, y, a) != p(T, a, x, a, y, a):
            return (a, x, y)
    return None


def locally_regular_witness(T):
    n = len(T)
    for e in range(n):
        loc = sorted({p(T, e, x, e) for x in range(n)})
        w = regular_witness(T, loc)
        if w is not None:
            return (e, loc, w)
    return None


def L_congruence(T):
    n = len(T)
    L = [[T[x][y] == x and T[y][x] == y for y in range(n)] for x in range(n)]
    return all(L[T[z][x]][T[z][y]] and L[T[x][z]][T[y][z]] for x in range(n) for y in range(n) if L[x][y] for z in range(n))


def R_congruence(T):
    n = len(T)
    R = [[T[x][y] == y and T[y][x] == x for y in range(n)] for x in range(n)]
    return all(R[T[z][x]][T[z][y]] and R[T[x][z]][T[y][z]] for x in range(n) for y in range(n) if R[x][y] for z in range(n))


def lsrb_identity(T):
    n = len(T)
    return all(p(T, x, y, z) == p(T, x, y, z, x, z, y, z) for x in range(n) for y in range(n) for z in range(n))


def adjoin_identity(T):
    n = len(T)
    U = [[0] * (n + 1) for _ in range(n + 1)]
    for x in range(n + 1):
        for y in range(n + 1):
            if x == n:
                U[x][y] = y
            elif y == n:
                U[x][y] = x
            else:
                U[x][y] = T[x][y]
    return U


def enumerate_bands(n):
    """all labelled bands on {0..n-1} by backtracking over the table with associativity pruning."""
    cells = [(x, y) for x in range(n) for y in range(n) if x != y]
    T = [[None] * n for _ in range(n)]
    for x in range(n):
        T[x][x] = x

    def consistent():
        for x in range(n):
            for y in range(n):
                xy = T[x][y]
                if xy is None:
                    continue
                for z in range(n):
                    yz = T[y][z]
                    if yz is None:
                        continue
                    l = T[xy][z]
                    r = T[x][yz]
                    if l is not None and r is not None and l != r:
                        return False
        return True

    def rec(k):
        if k == len(cells):
            yield [row[:] for row in T]
            return
        x, y = cells[k]
        for v in range(n):
            T[x][y] = v
            if consistent():
                yield from rec(k + 1)
        T[x][y] = None

    yield from rec(0)


def free_band_3():
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def nf(w):
        c = set(w)
        if len(c) <= 1:
            return w[:1]
        seen, pidx = set(), None
        for i, ch in enumerate(w):
            if ch not in seen:
                seen.add(ch)
                if len(seen) == len(c):
                    pidx = i
                    break
        seen, qidx = set(), None
        for i in range(len(w) - 1, -1, -1):
            if w[i] not in seen:
                seen.add(w[i])
                if len(seen) == len(c):
                    qidx = i
                    break
        return nf(w[:pidx]) + (w[pidx], w[qidx]) + nf(w[qidx + 1:])

    elems = [(0,), (1,), (2,)]
    idx = {w: k for k, w in enumerate(elems)}
    k = 0
    while k < len(elems):
        for g in range(3):
            v = nf(elems[k] + (g,))
            if v not in idx:
                idx[v] = len(elems)
                elems.append(v)
        k += 1
    T = [[idx[nf(u + v)] for v in elems] for u in elems]
    return T


def main() -> None:
    ok = True
    # 1
    assert is_band(E5), "E5 not a band"
    w = regular_witness(E5, range(5))
    print("E5 band: True; regular-identity witness (a,x,y) with axya != axaya:", w,
          "values", p(E5, *[w[0], w[1], w[2], w[0]]), p(E5, w[0], w[1], w[0], w[2], w[0]))
    lw = locally_regular_witness(E5)
    print("E5 locally regular:", lw is None)
    print("E5 L congruence (left semiregular):", L_congruence(E5), " identity xyz=xyzxzyz:", lsrb_identity(E5))
    print("E5 R congruence:", R_congruence(E5))
    ok &= w is not None and lw is None and L_congruence(E5) and lsrb_identity(E5) and not R_congruence(E5)
    # 2
    E51 = adjoin_identity(E5)
    assert is_band(E51)
    lw1 = locally_regular_witness(E51)
    print("E5^1 band:", True, " left semiregular:", lsrb_identity(E51), " locally regular:", lw1 is None, " witness:", lw1)
    ok &= lsrb_identity(E51) and lw1 is not None
    # 3
    for n in range(1, 5):
        cnt = 0
        bad = 0
        for T in enumerate_bands(n):
            cnt += 1
            if locally_regular_witness(T) is None and regular_witness(T, range(n)) is not None:
                bad += 1
        print(f"order {n}: {cnt} labelled bands, locally-regular-but-not-regular: {bad}")
        ok &= bad == 0
    # 4
    FB3 = free_band_3()
    print("|FB(3)| =", len(FB3), " band:", is_band(FB3))
    w3 = regular_witness(FB3, range(len(FB3)))
    lw3 = locally_regular_witness(FB3)
    print("FB(3) regular:", w3 is None, " locally regular:", lw3 is None,
          " left semiregular (L congruence):", L_congruence(FB3), " right semiregular (R congruence):", R_congruence(FB3))
    ok &= is_band(FB3) and len(FB3) == 159 and w3 is not None and lw3 is None and not L_congruence(FB3) and not R_congruence(FB3)
    print("ALL BAND FACTS OK" if ok else "SOME CHECK FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
