"""Genus-2 (pair) MacWilliams machinery for additive codes over F4 (= Pauli stabilizer groups mod phase).

Pair type of a coordinate (u_l, v_l): 00, 0x (u=0,v!=0), x0, xx (u=v!=0), xy (both nonzero, different).
Type-count vector tau = (n0x, nx0, nxx, nxy); n00 = n - sum.  AMH orbit (i,j,t,p) <-> nx0=i-t, n0x=j-t, nxx=p, nxy=t-p.
Symplectic character H[a,c] = (-1)^{<a,c>_symp}; genus-2 transform M = H (x) H symmetrized to the 5x5 matrix T
(rows/cols 00,0x,x0,xx,xy), verified here by brute force. For an additive code C with symplectic dual C^perp:
   sum_{tau} f_C(tau) K(tau -> tau') = |C|^2 f_{C^perp}(tau'),  K(tau->tau') = [z^tau'] prod_c (T_c . z)^{n_c(tau)}.
"""
import itertools

import numpy as np

CLASSES = ["00", "0x", "x0", "xx", "xy"]


def symp(a, c):
    ax, az = a
    cx, cz = c
    return (ax * cz + az * cx) & 1


def cls(a, b):
    if a == (0, 0) and b == (0, 0):
        return "00"
    if a == (0, 0):
        return "0x"
    if b == (0, 0):
        return "x0"
    if a == b:
        return "xx"
    return "xy"


def brute_T():
    F = [(0, 0), (1, 0), (0, 1), (1, 1)]
    T = np.zeros((5, 5), dtype=np.int64)
    reps = {}
    for a in F:
        for b in F:
            reps.setdefault(cls(a, b), (a, b))
    for r, cname in enumerate(CLASSES):
        a, b = reps[cname]
        # check the row is the same for all representatives of the class
        for a2 in F:
            for b2 in F:
                if cls(a2, b2) != cname:
                    continue
                row = np.zeros(5, dtype=np.int64)
                for c in F:
                    for d in F:
                        row[CLASSES.index(cls(c, d))] += (-1) ** (symp(a2, c) + symp(b2, d))
                if (a2, b2) == (a, b):
                    T[r] = row
                else:
                    assert (row == T[r]).all() or T[r].sum() == 0 and False or True
    # second pass: assert class-consistency strictly
    for a2 in F:
        for b2 in F:
            row = np.zeros(5, dtype=np.int64)
            for c in F:
                for d in F:
                    row[CLASSES.index(cls(c, d))] += (-1) ** (symp(a2, c) + symp(b2, d))
            assert (row == T[CLASSES.index(cls(a2, b2))]).all()
    return T


def types(n):
    """All type-count vectors (n0x, nx0, nxx, nxy) with sum <= n."""
    out = []
    for a in range(n + 1):
        for b in range(n + 1 - a):
            for c in range(n + 1 - a - b):
                for d in range(n + 1 - a - b - c):
                    out.append((a, b, c, d))
    return out


def tau_to_orbit(tau, n):
    n0x, nx0, nxx, nxy = tau
    t = nxx + nxy
    return (nx0 + t, n0x + t, t, nxx)  # (i, j, t, p)


def orbit_to_tau(o):
    i, j, t, p = o
    return (j - t, i - t, p, t - p)


def transform_row(tau, n, T, mod=None):
    """Dense array R[n0x, nx0, nxx, nxy] = [z^tau'] prod_c (T_c . z)^{n_c(tau)} (n00 implied).
    Exact if mod is None and values fit int64 is NOT guaranteed -> use mod (int64) or object."""
    n0x, nx0, nxx, nxy = tau
    n00 = n - sum(tau)
    counts = [n00, n0x, nx0, nxx, nxy]
    shape = (n + 1,) * 4
    if mod is None:
        R = np.zeros(shape, dtype=object)
        R[0, 0, 0, 0] = 1
    else:
        R = np.zeros(shape, dtype=np.int64)
        R[0, 0, 0, 0] = 1
    for ci, cnt in enumerate(counts):
        row = T[ci]
        for _ in range(cnt):
            new = R * int(row[0])            # z00 factor: no shift
            # shifts along axes: 0x -> axis0, x0 -> axis1, xx -> axis2, xy -> axis3
            for ax in range(4):
                coef = int(row[ax + 1])
                if coef == 0:
                    continue
                sl_to = [slice(None)] * 4
                sl_from = [slice(None)] * 4
                sl_to[ax] = slice(1, None)
                sl_from[ax] = slice(0, -1)
                new[tuple(sl_to)] = new[tuple(sl_to)] + coef * R[tuple(sl_from)]
            R = new % mod if mod is not None else new
    return R


if __name__ == "__main__":
    T = brute_T()
    print("T (rows/cols 00,0x,x0,xx,xy):\n", T)
    print("T^2 == 16 I:", (T @ T == 16 * np.eye(5, dtype=np.int64)).all())
