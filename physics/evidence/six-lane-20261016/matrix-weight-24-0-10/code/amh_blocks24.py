"""AMH Terwilliger blocks (Eq. (31)) on the exact 8-parameter genus-2 family for n=24, K=1.

Each block B_(a,k)(s) = B0 + sum_f s_f B_f with EXACT rational matrices (alpha is rational on the support because
all weights i, j are even). Floating copies, diagonally rescaled (a congruence, so PSD-ness is unchanged), are used
by the SDP search; exact PSD of any final candidate is checked separately (exact LDL^T over Q).
"""
import json
import pickle
from fractions import Fraction

from g2_polytope import load_space
from genus2 import orbit_to_tau
from g2_system import s3key
from terwilliger import C, blocks_index, gamma, beta

N = 24


def alpha_exact(i, j, t, p, a, k, n=N, q=4):
    """alpha(i,j,t,p,a,k) as an exact Fraction; requires i+j even (true on the Type II support)."""
    assert (i + j) % 2 == 0
    b = beta(n - a, t - a, i - a, j - a, k - a)
    if b == 0:
        return Fraction(0)
    s = 0
    for g in range(0, p + 1):
        s += (-1) ** ((a - g) % 2) * C(a, g) * C(t - a, p - g) * (q - 2) ** (t - a - p + g)
    e = (i + j) // 2 - t
    return Fraction(b * s) * (Fraction(q - 1) ** e)


def family_x(keys, free, c, V):
    """Map AMH orbit (i,j,t,p) -> (const, [coef per free param]) for x = lambda/gamma, exact."""
    col = {json.dumps(k): idx for idx, k in enumerate(keys)}
    out = {}
    n = N
    for i in range(n + 1):
        for j in range(n + 1):
            for t in range(min(i, j) + 1):
                for p in range(t + 1):
                    if i + j > t + n:
                        continue
                    tau = orbit_to_tau((i, j, t, p))
                    kk = s3key(tau)
                    key = json.dumps([list(kk[0]), kk[1]])
                    if key not in col:
                        continue
                    idx = col[key]
                    g = gamma(i, j, t, p, n)
                    out[(i, j, t, p)] = (c[idx] / g, [V[idx][f] / g for f in range(len(free))])
    return out


if __name__ == "__main__":
    keys, piv, free, c, V = load_space()
    fx = family_x(keys, free, c, V)
    print("support orbits (i,j,t,p):", len(fx))
    nf = len(free)
    blocks = []
    for (a, k) in blocks_index(N):
        idx = list(range(k, N + a - k + 1))
        m = len(idx)
        B = [[[Fraction(0)] * m for _ in range(m)] for _ in range(nf + 1)]
        nonzero = False
        for r, i in enumerate(idx):
            for cc, j in enumerate(idx):
                for t in range(min(i, j) + 1):
                    for p in range(t + 1):
                        o = (i, j, t, p)
                        if o not in fx:
                            continue
                        al = alpha_exact(i, j, t, p, a, k)
                        if al == 0:
                            continue
                        const, coefs = fx[o]
                        B[0][r][cc] += al * const
                        for f in range(nf):
                            B[f + 1][r][cc] += al * coefs[f]
                        nonzero = True
        blocks.append({"a": a, "k": k, "idx": idx, "B": B, "nonzero": nonzero})
    pickle.dump({"blocks": blocks, "free": free, "keys": keys}, open("../evidence/amh_blocks24_exact.pkl", "wb"))
    print("blocks:", len(blocks), "nonzero blocks:", sum(b["nonzero"] for b in blocks))
