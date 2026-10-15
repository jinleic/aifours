"""Replay the all-N proof reduction and independent finite controls for RESULTS.md C9.

The universal statement is proved in RESULTS.md, not by a finite N cutoff here.
This script mechanically reduces the cubic bilinear expression to -3 times the
four-border Pfaffian Pluecker identity, WITHOUT selecting a matrix dimension.
Supplemental controls independently compare:
  * an elimination Pfaffian vs a perfect-matching Pfaffian;
  * block Pfaffians vs the amplitude-polynomial subset formula (including b_i=0);
  * the G_y border identity vs differentiating exponential coefficients;
  * every coefficient of both Hirota equations via ordered-pair enumeration.
It imports neither hirota_ns.py nor n_soliton_checks.py and uses no floats.
Run: python all_n_pfaffian.py
"""
from __future__ import annotations

import itertools
import json
import platform
import random
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent.parent


def pf_match(matrix):
    """Definition of the Pfaffian by signed perfect matchings (small controls)."""
    n = len(matrix)
    if n % 2:
        raise ValueError("Pfaffian needs even size")

    @lru_cache(None)
    def rec(ids):
        if not ids:
            return Q(1)
        i, rest = ids[0], ids[1:]
        return sum(((-1) ** pos * matrix[i][j]
                    * rec(rest[:pos] + rest[pos + 1:])
                    for pos, j in enumerate(rest)), Q(0))
    return rec(tuple(range(n)))


def pf_eliminate(matrix):
    """Independent exact skew elimination; zero pivots are handled by permutations."""
    n = len(matrix)
    if n % 2:
        raise ValueError("Pfaffian needs even size")
    a = [[Q(value) for value in row] for row in matrix]
    out = Q(1)
    for k in range(0, n, 2):
        j = next((j for j in range(k + 1, n) if a[k][j]), None)
        if j is None:
            return Q(0)
        if j != k + 1:
            a[k + 1], a[j] = a[j], a[k + 1]
            for row in a:
                row[k + 1], row[j] = row[j], row[k + 1]
            out = -out
        pivot = a[k][k + 1]
        out *= pivot
        for i in range(k + 2, n):
            for j in range(i + 1, n):
                a[i][j] -= (a[k][i] * a[k + 1][j] - a[k][j] * a[k + 1][i]) / pivot
                a[j][i] = -a[i][j]
    return out


def border(matrix, *vectors):
    n, m = len(matrix), len(vectors)
    out = [[Q(0) for _ in range(n + m)] for _ in range(n + m)]
    for i in range(n):
        for j in range(n):
            out[i][j] = matrix[i][j]
    for j, v in enumerate(vectors):
        if len(v) != n:
            raise ValueError("Incorrect border dimension")
        for i in range(n):
            out[i][n + j] = v[i]
            out[n + j][i] = -v[i]
    return out


def rank_update(matrix, u, v):
    return [[matrix[i][j] + u[i] * v[j] - v[i] * u[j]
             for j in range(len(matrix))] for i in range(len(matrix))]


def formal_cubic_reduction():
    """Formal differentiation of Pfaffian brackets, independent of their dimension."""
    brackets = {}

    def bracket(*labels):
        if len(set(labels)) != len(labels):
            return sp.Integer(0)
        sign = (-1) ** sum(labels[i] > labels[j] for i in range(len(labels))
                           for j in range(i + 1, len(labels)))
        key = tuple(sorted(labels))
        sym = sp.Symbol("tau" if not key else "pf_" + "_".join(map(str, key)))
        brackets[sym] = key
        return sign * sym

    # label 100 denotes the X,s-constant border v; all others denote r_j.
    def derivative(expr, shift):
        out = 0
        for sym in expr.free_symbols:
            labels = brackets[sym]
            if shift == 1:
                dsym = bracket(0, 1, *labels)
            else:
                dsym = bracket(0, 3, *labels) - 2 * bracket(1, 2, *labels)
            for pos, lab in enumerate(labels):
                if lab != 100:
                    new = list(labels)
                    new[pos] += shift
                    dsym += bracket(*new)
            out += sp.diff(expr, sym) * dsym
        return sp.expand(out)

    tau, psi = bracket(), bracket(0, 100)
    tx, px = [tau], [psi]
    for _ in range(3):
        tx.append(derivative(tx[-1], 1))
        px.append(derivative(px[-1], 1))
    ts, ps = derivative(tau, 3), derivative(psi, 3)
    bilinear = sp.expand(tx[3] * psi - 3 * tx[2] * px[1] + 3 * tx[1] * px[2]
                         - tau * px[3] - ts * psi + tau * ps)
    pluecker = (tau * bracket(0, 1, 2, 100)
                - bracket(0, 1) * bracket(2, 100)
                + bracket(0, 2) * bracket(1, 100)
                - bracket(0, 100) * bracket(1, 2))
    residual = sp.expand(bilinear + 3 * pluecker)
    assert residual == 0
    return {"dimension_selected": False, "bilinear_plus_3_Pluecker": str(residual),
            "tau_xxx_minus_tau_s": str(sp.expand(tx[3] - ts)),
            "psi_xxx_minus_psi_s": str(sp.expand(px[3] - ps))}


def matrix_identity_controls():
    rng = random.Random(20261014)
    count = 0
    for n in (0, 2, 4, 6, 8):
        for singular in (False, True):
            a = [[Q(0) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    a[i][j] = Q(rng.randrange(-6, 7), rng.randrange(1, 5))
                    a[j][i] = -a[i][j]
            if singular and n:
                for j in range(n):
                    a[0][j] = a[j][0] = Q(0)
            vectors = [[Q(rng.randrange(-5, 6)) for _ in range(n)] for _ in range(4)]
            u, v, w, z = vectors
            tau = pf_eliminate(a)
            assert tau == pf_match(a)
            br = lambda *vs: pf_eliminate(border(a, *vs))
            assert pf_eliminate(rank_update(a, u, v)) == tau - br(u, v)
            assert pf_eliminate(border(rank_update(a, u, v), w, z)) == br(w, z) - br(u, v, w, z)
            assert tau * br(u, v, w, z) == br(u, v) * br(w, z) - br(u, w) * br(v, z) + br(u, z) * br(v, w)
            count += 1
    return count


def subset_coefficients(k, ell, a, b):
    """Theorem 9.1 with amplitude-polynomial B0,C0; no a_i/b_i."""
    n = len(k)
    f, g = [], []
    for mask in range(1 << n):
        ids = [i for i in range(n) if mask & (1 << i)]
        rho = Q(1)
        for i, j in itertools.combinations(ids, 2):
            rho *= (k[i] - k[j]) / (k[i] + k[j])
        m = len(ids) + len(ids) % 2
        bm = [[Q(0) for _ in range(m)] for _ in range(m)]
        cm = [[Q(0) for _ in range(m)] for _ in range(m)]
        for p, i in enumerate(ids):
            for q in range(p + 1, len(ids)):
                j = ids[q]
                bm[p][q] = (ell[i] * a[i] * b[j] - ell[j] * a[j] * b[i]) / (ell[i] + ell[j])
                cm[p][q] = (ell[i] * b[i] * a[j] - ell[j] * b[j] * a[i]) / (ell[i] + ell[j])
                bm[q][p], cm[q][p] = -bm[p][q], -cm[p][q]
            if len(ids) % 2:
                bm[p][-1], cm[p][-1] = a[i], b[i]
                bm[-1][p], cm[-1][p] = -a[i], -b[i]
        f.append(rho * pf_match(bm))
        g.append(rho * pf_match(cm))
    return f, g


def block_and_residual_controls(n, mode):
    k = [Q(i + 1) for i in range(n)]
    ell = [Q(2 * i + 1) for i in range(n)]
    if mode == "diagonal":
        ell = k.copy()
    if mode == "zero_wavenumbers" and n >= 2:
        k[0], ell[1] = Q(0), Q(0)
    a = [Q((-1) ** i * (i + 2), i + 1) for i in range(n)]
    b = [Q(2 * i + 3, i + 2) for i in range(n)]
    if mode == "zero_amplitudes":
        for i in range(n):
            if i % 2:
                a[i] = Q(0)
            else:
                b[i] = Q(0)
    fs, gs = subset_coefficients(k, ell, a, b)
    c1, c3 = Q(-5, 2), Q(7, 3)
    freq = [-(c1 * ki + c3 * ki ** 3) for ki in k]
    kap, lam, omg, monomial = [], [], [], []
    fval = [Q(i + 2, i + 1) for i in range(n)]
    hval = [Q(2 * i + 1, i + 1) for i in range(n)]
    for mask in range(1 << n):
        ids = [i for i in range(n) if mask & (1 << i)]
        kap.append(sum((k[i] for i in ids), Q(0)))
        lam.append(sum((ell[i] for i in ids), Q(0)))
        omg.append(sum((freq[i] for i in ids), Q(0)))
        product = Q(1)
        for i in ids:
            product *= fval[i] * hval[i]
        monomial.append(product)
    res = {}
    for mu in range(1 << n):
        for nu in range(1 << n):
            powers = tuple(((mu >> i) & 1) + ((nu >> i) & 1) for i in range(n))
            dk, dl, dw = kap[mu] - kap[nu], lam[mu] - lam[nu], omg[mu] - omg[nu]
            term = fs[mu] * gs[nu] * (dw + c1 * dk + c3 * dk ** 3)
            pair = res.setdefault(powers, [Q(0), Q(0)])
            pair[0] += term
            pair[1] += dl * term
    assert all(pair == [0, 0] for pair in res.values())
    alpha = [Q(0)] * n + [a[i] * hval[i] for i in range(n)]
    beta = [Q(0)] * n + [b[i] * hval[i] for i in range(n)]
    beta_y = [Q(0)] * n + [ell[i] * b[i] * hval[i] for i in range(n)]
    q = fval + [Q(0)] * n
    r = [qi + ai for qi, ai in zip(q, alpha)]
    kmat = [[Q(0) for _ in range(2 * n)] for _ in range(2 * n)]
    for i in range(n):
        kmat[i][n + i], kmat[n + i][i] = Q(1), Q(-1)
        for j in range(i + 1, n):
            av = (k[i] - k[j]) / (k[i] + k[j]) * fval[i] * fval[j]
            bv = (ell[i] * alpha[n + i] * beta[n + j] - ell[j] * alpha[n + j] * beta[n + i]) / (ell[i] + ell[j])
            kmat[i][j], kmat[j][i] = av, -av
            kmat[n + i][n + j], kmat[n + j][n + i] = -bv, bv
    lmat = rank_update(kmat, q, alpha)
    sigma = (-1) ** (n * (n - 1) // 2)
    fsum = sum((v * e for v, e in zip(fs, monomial)), Q(0))
    gsum = sum((v * e for v, e in zip(gs, monomial)), Q(0))
    gysum = sum((v * e * l for v, e, l in zip(gs, monomial, lam)), Q(0))
    fblock = sigma * pf_eliminate(lmat)
    gblock = fblock + sigma * pf_eliminate(border(lmat, r, [u - v for u, v in zip(alpha, beta)]))
    gyblock = -sigma * pf_eliminate(border(lmat, r, beta_y))
    assert (fsum, gsum, gysum) == (fblock, gblock, gyblock)
    return {"N": n, "mode": mode, "coefficients_checked_per_equation": len(res),
            "nonzero_residuals": 0, "block_F_G_Gy_match": True}


def main():
    report = {"python": platform.python_version(), "sympy": sp.__version__,
              "universal_reduction": formal_cubic_reduction(),
              "matrix_identity_controls": matrix_identity_controls()}
    report["finite_controls"] = [block_and_residual_controls(n, mode)
                                 for n in range(7)
                                 for mode in ("generic", "zero_amplitudes", "zero_wavenumbers", "diagonal")]
    report["interpretation"] = "All-N proof is RESULTS.md C9; finite controls supplement rather than establish its universal quantifier."
    destination = ROOT / "results/all_n_pfaffian.json"
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print("universal cubic expression + 3*Pluecker = 0 (no matrix dimension selected)")
    print(f"matrix identity controls: {report['matrix_identity_controls']} passed (including singular matrices)")
    print(f"finite controls: {len(report['finite_controls'])} passed; N=0..6, zero amplitudes, zero individual wave numbers, diagonal reduction")
    print("both Hirota residuals: all exact coefficients zero; block F,G,G_y agree")
    print(f"wrote {destination}")


if __name__ == "__main__":
    main()
