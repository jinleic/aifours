#!/usr/bin/env python3
"""Twisted actions for a CYCLIC symmetry group <s>, s = (mu, pi), of (Z_n, k; 1) difference matrices
(lane cfr33/cfr27, worker InfoCFR27Lift; notes/facts-v8.md).

A twisted element is s_t: (s_t c)_i = mu c_{pi^-1(i)} + t_i, with t in Z_n^k modulo the diagonal (normalised t_0 = 0).
<s_t> has the same order m as <s> iff N(t) = sum_{j<m} L^j t lies in the diagonal, L(t)_i = mu t_{pi^-1(i)}.
Conjugating by a row translation u changes t by (L - 1)u (mod diagonal). This script enumerates all t (brute force
over Z_n^(k-1)), keeps the cocycles, and partitions them into classes modulo B = {(L - 1)u mod diag}. Output: one JSON
line per class: representative t (lexicographically smallest member), class size, and whether it is the trivial class.
Usage: twist_classes_v1.py N K MU PI(comma list)
"""
import json, sys
import numpy as np


def main():
    n, k, mu = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    pi = [int(x) for x in sys.argv[4].split(",")]
    pinv = [0] * k
    for i, x in enumerate(pi):
        pinv[x] = i
    # order m of (mu, pi)
    m = 1
    p = list(range(k))
    mm = 1
    while True:
        p = [pi[p[i]] for i in range(k)]
        mm = (mm * mu) % n
        if p == list(range(k)) and mm == 1:
            break
        m += 1
    total = n ** (k - 1)
    codes = np.arange(total, dtype=np.int64)
    T = np.zeros((total, k), dtype=np.int32)
    c = codes.copy()
    for x in range(1, k):
        T[:, x] = c % n
        c //= n

    def L(V):
        return (mu * V[:, pinv]) % n

    def norm(V):
        return (V - V[:, :1]) % n

    def enc(V):
        V = norm(V)
        out = np.zeros(V.shape[0], dtype=np.int64)
        for x in range(k - 1, 0, -1):
            out = out * n + V[:, x]
        return out

    # cocycle test: N(t) in diag
    acc = T.copy()
    cur = T.copy()
    for _ in range(m - 1):
        cur = L(cur)
        acc = (acc + cur) % n
    accn = norm(acc)
    is_cocycle = np.all(accn == 0, axis=1)
    # coboundaries
    B = np.unique(enc((L(T) - T) % n))
    inB = np.zeros(total, dtype=bool)
    inB[B] = True
    coc = np.nonzero(is_cocycle)[0]
    seen = np.zeros(total, dtype=bool)
    classes = []
    Bvecs = T[B]
    for code in coc:
        if seen[code]:
            continue
        t = T[code]
        members = enc((Bvecs + t) % n)
        seen[members] = True
        classes.append({"rep_t": [int(x) for x in t], "class_size": int(len(members)), "trivial": bool(inB[code])})
    print(json.dumps({"n": n, "k": k, "mu": mu, "pi": pi, "order": m, "cocycles": int(len(coc)),
                      "coboundaries": int(len(B)), "classes": classes}))


if __name__ == "__main__":
    main()
