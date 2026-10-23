#!/usr/bin/env python3
"""Twisted actions for an S_3 symmetry group <sigma, tau> (sigma of order 3, tau of order 2, tau sigma tau = sigma^-1)
of (Z_n, k; 1) difference matrices (lane cfr33/cfr27, worker InfoCFR27Lift; notes/facts-v8.md).

tau has order 2 and n is odd, so its twist is removable: WLOG t_tau = 0. sigma_t = (mu_s, pi_s, t). Conditions modulo
the diagonal: (A) N(t) = t + L_s t + L_s^2 t in diag; (B) L_tau t + L_s^-1 t in diag (from tau sigma_t tau = sigma_t^-1).
Classes modulo B' = {(L_s - 1) u : (L_tau - 1) u in diag} (conjugations keeping tau untwisted).
Usage: twist_classes_s3_v1.py N K MU_S PI_S MU_T PI_T      (PI as comma lists, pi[i] = image of row i)
"""
import json, sys
import numpy as np


def main():
    n, k = int(sys.argv[1]), int(sys.argv[2])
    mus, pis = int(sys.argv[3]), [int(x) for x in sys.argv[4].split(",")]
    mut, pit = int(sys.argv[5]), [int(x) for x in sys.argv[6].split(",")]
    def inv(p):
        q = [0] * k
        for i, x in enumerate(p):
            q[x] = i
        return q
    pis_inv, pit_inv = inv(pis), inv(pit)
    total = n ** (k - 1)
    c = np.arange(total, dtype=np.int64)
    T = np.zeros((total, k), dtype=np.int32)
    for x in range(1, k):
        T[:, x] = c % n
        c //= n
    def Ls(V):      # (L_s V)_i = mu_s V_{pi_s^-1(i)}
        return (mus * V[:, pis_inv]) % n
    def Ls_inv(V):  # inverse: (L_s^-1 V)_i = mu_s^-1 V_{pi_s(i)}
        mi = pow(mus, -1, n)
        return (mi * V[:, pis]) % n
    def Lt(V):
        return (mut * V[:, pit_inv]) % n
    def isdiag(V):
        return np.all(((V - V[:, :1]) % n) == 0, axis=1)
    def enc(V):
        V = (V - V[:, :1]) % n
        out = np.zeros(V.shape[0], dtype=np.int64)
        for x in range(k - 1, 0, -1):
            out = out * n + V[:, x]
        return out
    A = isdiag((T + Ls(T) + Ls(Ls(T))) % n)
    Bc = isdiag((Lt(T) + Ls_inv(T)) % n)
    coc = np.nonzero(A & Bc)[0]
    keep_u = isdiag((Lt(T) - T) % n)
    U = T[keep_u]
    Bset = np.unique(enc((Ls(U) - U) % n))
    inB = np.zeros(total, dtype=bool)
    inB[Bset] = True
    seen = np.zeros(total, dtype=bool)
    Bvecs = T[Bset]
    classes = []
    for code in coc:
        if seen[code]:
            continue
        members = enc((Bvecs + T[code]) % n)
        seen[members] = True
        classes.append({"rep_t_sigma": [int(x) for x in T[code]], "class_size": int(len(members)), "trivial": bool(inB[code])})
    print(json.dumps({"n": n, "k": k, "sigma": [mus, pis], "tau": [mut, pit], "cocycles": int(len(coc)),
                      "coboundaries": int(len(Bset)), "classes": classes}))


if __name__ == "__main__":
    main()
