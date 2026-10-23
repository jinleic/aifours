"""Brute-force check of the GST06 block diagonalization formulas for small n, q=4.
For random symmetric orbit data x (x[i,j,t,p] = x[j,i,t,p]), the spectrum of the
full 4^n x 4^n matrix sum x M must equal the union of the generalized block spectra
(blocks are congruent, not unitarily similar, to the true blocks: B(x) v = mu B(id) v)."""
import itertools
import sys

import numpy as np

from terwilliger import I_set, alpha, blocks_index, gamma


def orbit(u, v):
    i = sum(1 for x in u if x)
    j = sum(1 for x in v if x)
    t = sum(1 for x, y in zip(u, v) if x and y)
    p = sum(1 for x, y in zip(u, v) if x and y and x == y)
    return (i, j, t, p)


def block(n, q, Iset, a, k, xx):
    idx = list(range(k, n + a - k + 1))
    B = np.zeros((len(idx), len(idx)))
    for r, i in enumerate(idx):
        for c, j in enumerate(idx):
            s = 0.0
            for (ii, jj, t, p) in Iset:
                if ii == i and jj == j:
                    s += alpha(i, j, t, p, a, k, n, q)[0] * xx[(i, j, t, p)]
            B[r, c] = s
    return B


def run(n, q=4, seed=0):
    rng = np.random.default_rng(seed)
    Iset = I_set(n)
    x = {}
    for (i, j, t, p) in Iset:
        if (j, i, t, p) in x:
            x[(i, j, t, p)] = x[(j, i, t, p)]
        else:
            x[(i, j, t, p)] = rng.normal()
    words = list(itertools.product(range(q), repeat=n))
    N = len(words)
    M = np.zeros((N, N))
    cnt = {}
    for a, u in enumerate(words):
        for b, v in enumerate(words):
            o = orbit(u, v)
            M[a, b] = x[o]
            cnt[o] = cnt.get(o, 0) + 1
    for o in Iset:
        assert cnt.get(o, 0) == gamma(*o, n, q), (o, cnt.get(o), gamma(*o, n, q))
    ev_full = np.sort(np.linalg.eigvalsh(M))
    xid = {o: (1.0 if (o[0] == o[1] == o[2] == o[3]) else 0.0) for o in Iset}
    ev_blocks = []
    for (a, k) in blocks_index(n):
        B = block(n, q, Iset, a, k, x)
        D = block(n, q, Iset, a, k, xid)
        assert np.allclose(B, B.T), (a, k)
        assert np.allclose(D, np.diag(np.diag(D))) and (np.diag(D) > 0).all(), (a, k, D)
        dinv = 1.0 / np.sqrt(np.diag(D))
        ev_blocks.extend(np.linalg.eigvalsh(dinv[:, None] * B * dinv[None, :]))
    ev_full_set = np.unique(np.round(ev_full, 7))
    ev_blk_set = np.unique(np.round(np.array(ev_blocks), 7))
    ok = len(ev_full_set) == len(ev_blk_set) and np.allclose(ev_full_set, ev_blk_set, atol=1e-6)
    print(f"n={n} seed={seed}: full distinct eigs {len(ev_full_set)}, block distinct {len(ev_blk_set)}, "
          f"match={ok}, min full {ev_full.min():.6f} min block {min(ev_blocks):.6f}")
    return ok


if __name__ == "__main__":
    allok = True
    for n in (1, 2, 3):
        for seed in (0, 1):
            allok &= run(n, seed=seed)
    print("PASS" if allok else "FAIL")
    sys.exit(0 if allok else 1)
