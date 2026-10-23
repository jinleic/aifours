"""INDEPENDENT exact verifier of a matrix-weight table against Angles Munne-Huber arXiv:2603.19901v1
Eq. (31) + (32) pure + (33) self-dual + (34) additive + (35) Type II, for n=24, K=1, delta=10, A_j of Eq. (38).

Written separately from the search code: its own gamma, beta, alpha (GST06 / AMH Eqs. (41)-(42)),
its own constraint list transcribed from AMH Eq. (31)-(35), Fractions throughout, exact LDL^T PSD test.
Input: JSON with "counts": {"[[a,b,c],d]": value} giving lambda for every pair type with sorted
(n0x,nx0,nxx) = [a,b,c] and n_xy = d (S3-symmetric table); absent types have lambda = 0.

Usage: verify_amh.py candidate.json [--n N --delta D --A json]  (defaults: the [[24,0,10]] problem)
"""
import argparse
import json
from fractions import Fraction
from math import comb, factorial

A38 = {0: 1, 10: 18216, 12: 156492, 14: 1147608, 16: 3736557, 18: 6248088, 20: 4399164, 22: 1038312, 24: 32778}


def binom(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def gam(i, j, t, p, n, q=4):
    # number of ordered pairs (u,v) in F_q^n with |S(u)|=i,|S(v)|=j,|S(u)&S(v)|=t, #{u_l=v_l!=0}=p
    return ((q - 1) ** (i + j - t) * (q - 2) ** (t - p) * factorial(n)
            // (factorial(p) * factorial(t - p) * factorial(i - t) * factorial(j - t) * factorial(n - i - j + t)))


_beta_cache = {}


def bet(m, t, i, j, k):
    key = (m, t, i, j, k)
    if key not in _beta_cache:
        tot = 0
        for u in range(m + 1):
            tot += (-1) ** abs(t - u) * binom(u, t) * binom(m - 2 * k, m - k - u) * binom(m - k - u, i - u) \
                   * binom(m - k - u, j - u)
        _beta_cache[key] = tot
    return _beta_cache[key]


def alp(i, j, t, p, a, k, n, q=4):
    # AMH Eq. (42) with (q-1)^((i+j)/2 - t); requires i+j even (all weights even on a Type II support)
    assert (i + j) % 2 == 0
    s = sum((-1) ** abs(a - g) * binom(a, g) * binom(t - a, p - g) * (q - 2) ** (t - a - p + g) for g in range(p + 1))
    return Fraction(bet(n - a, t - a, i - a, j - a, k - a) * s) * Fraction(q - 1) ** ((i + j) // 2 - t)


def krawtchouk(j, i, n):
    return sum((-1) ** a * 3 ** (j - a) * binom(i, a) * binom(n - i, j - a) for a in range(j + 1))


def lam_table(counts, n):
    lam = {}
    for i in range(n + 1):
        for j in range(n + 1):
            for t in range(min(i, j) + 1):
                for p in range(t + 1):
                    if i + j > t + n:
                        continue
                    n0x, nx0, nxx, nxy = j - t, i - t, p, t - p
                    key = json.dumps([sorted([n0x, nx0, nxx]), nxy])
                    lam[(i, j, t, p)] = Fraction(counts.get(key, 0))
    return lam


def psd(M):
    A = [row[:] for row in M]
    alive = list(range(len(A)))
    while alive:
        pv = max(alive, key=lambda r: A[r][r])
        d = A[pv][pv]
        if d < 0:
            return False
        if d == 0:
            return all(A[r][c] == 0 for r in alive for c in alive)
        alive.remove(pv)
        for r in alive:
            if A[r][pv]:
                f = A[r][pv] / d
                for c in alive:
                    A[r][c] -= f * A[pv][c]
    return True


def lam_from_entries(entries, n):
    """Full AMH-indexed table: entries = [[i,j,t,p,lambda], ...]; every other (i,j,t,p) in I(n) has lambda = 0."""
    lam = {}
    for i in range(n + 1):
        for j in range(n + 1):
            for t in range(min(i, j) + 1):
                for p in range(t + 1):
                    if i + j <= t + n:
                        lam[(i, j, t, p)] = Fraction(0)
    for i, j, t, p, v in entries:
        assert (i, j, t, p) in lam, ("index outside I(n)", i, j, t, p)
        assert lam[(i, j, t, p)] == 0, "duplicate entry"
        lam[(i, j, t, p)] = Fraction(v)
    return lam


def verify(counts=None, n=24, delta=10, K=1, A=A38, k_logical=0, entries=None):
    lam = lam_from_entries(entries, n) if entries is not None else lam_table(counts, n)
    x = {o: v / gam(*o, n) for o, v in lam.items()}
    rep = {}
    # (34) integrality and nonnegativity
    rep["34_integral"] = all(v.denominator == 1 for v in lam.values())
    rep["34_nonnegative"] = all(v >= 0 for v in x.values())
    # (31) normalization
    rep["31_x0000_is_1"] = x[(0, 0, 0, 0)] == 1
    # (31) anticommuting pairs vanish
    rep["31_odd_t_minus_p_zero"] = all(v == 0 for (i, j, t, p), v in x.items() if (t - p) % 2)
    # (31) triple permutation symmetry
    groups = {}
    for (i, j, t, p), v in x.items():
        if (t - p) % 2:
            continue
        kk = i + j - t - p
        groups.setdefault((tuple(sorted((i, j, kk))), t - p), set()).add(v)
    rep["31_triple_symmetry"] = all(len(s) == 1 for s in groups.values())
    # (31) projector row sums: sum_{k=i+j-t-p} gamma x = (2^n/K) gamma_{k,0}^{0,0} x_{k,0}^{0,0}
    rs = {}
    for (i, j, t, p), v in lam.items():
        rs[i + j - t - p] = rs.get(i + j - t - p, 0) + v
    rep["31_row_sums"] = all(rs.get(kk, 0) == Fraction(2 ** n, K) * lam[(kk, 0, 0, 0)] for kk in range(n + 1))
    # (31) Knill-Laflamme, 0 < j < delta
    rep["31_KL"] = all(Fraction(K, 2 ** n) * sum(krawtchouk(j, i, n) * lam[(i, 0, 0, 0)] for i in range(n + 1))
                       == lam[(j, 0, 0, 0)] for j in range(1, delta))
    # (32) pure
    rep["32_pure"] = all(v == 0 for (i, j, t, p), v in x.items()
                         if {i, j, i + j - t - p} & set(range(1, delta)))
    # (33) self-dual
    diag = {i: lam[(i, i, i, i)] for i in range(n + 1)}
    rep["33_shadow_odd"] = all(sum((-1) ** i * krawtchouk(j, i, n) * diag[i] for i in range(n + 1)) == 0
                               for j in range(n + 1) if (n - j) % 2)
    rep["33_B_equals_A"] = all(Fraction(K, 2 ** n) * sum(krawtchouk(j, i, n) * diag[i] for i in range(n + 1))
                               == diag[j] for j in range(n + 1))
    # (35) Type II
    rep["35_typeII"] = sum(diag[j] for j in range(0, n + 1, 2)) == 2 ** (n - k_logical)
    # Eq. (38) weight distribution
    rep["38_weights"] = all(lam[(i, 0, 0, 0)] == A.get(i, 0) for i in range(n + 1))
    # (31) PSD of every Terwilliger block
    bad = []
    nblocks = 0
    for a in range(n + 1):
        for k in range(a, n + 1):
            if k > n + a - k:
                continue
            idx = list(range(k, n + a - k + 1))
            M = [[Fraction(0)] * len(idx) for _ in idx]
            nonzero = False
            for r, i in enumerate(idx):
                for c, j in enumerate(idx):
                    for t in range(min(i, j) + 1):
                        for p in range(t + 1):
                            v = x.get((i, j, t, p), 0)
                            if v:
                                M[r][c] += alp(i, j, t, p, a, k, n) * v
                                nonzero = True
            nblocks += 1
            if nonzero and not psd(M):
                bad.append((a, k))
    rep["31_blocks_psd"] = not bad
    rep["31_blocks_failing"] = bad
    rep["n_blocks"] = nblocks
    rep["ALL_PASS"] = all(v for kk, v in rep.items() if kk not in ("31_blocks_failing", "n_blocks"))
    return rep


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    a = ap.parse_args()
    cand = json.load(open(a.candidate))
    if "entries" in cand:
        rep = verify(entries=[[int(v) for v in e] for e in cand["entries"]])
    else:
        rep = verify({k: int(v) for k, v in cand["counts"].items()})
    rep["input"] = a.candidate
    print(json.dumps(rep, indent=1))
    raise SystemExit(0 if rep["ALL_PASS"] else 1)
