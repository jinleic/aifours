#!/usr/bin/env python3
r"""indep_slice_check.py -- lane random5reg-colour, worker PhysRandomColour.SliceConcavityIndep.

Independent check of the slice-concavity chain (a)-(d) for one (i,j)-block of the dual objective
    psi(m) = sum_rt m_rt (ln(m_rt)/2 - ln mu_rt(m)),   mu_rt dPhi/dmu_rt = m_rt  [paper (5.8)],
from Diaz-Kaporis-Kemkes-Kirousis-Perez-Wormald, "On the chromatic number of a random 5-regular
graph", J. Graph Theory 61 (2009).  Primary text: sources/diaz2009-3col-preprint.layout.txt
(spectra l.653-658 and 1693-1703; Phi (5.7) l.993-1001; Lemma 5.3 l.1013-1118; (5.18)-(5.19)
l.1202-1225; the merely "numerically confirmed" concavity of ln G~ on M0(c): l.1839-1844).

Independence: written from README.md section 1 and the primary text only; code/model.py and
code/slice_poly.py were neither read nor imported.  Exact algebra = sympy Poly over ZZ with
SYMPY_GROUND_TYPES=python forced before import (with python-flint installed, sympy 1.14 'auto'
selects flint ground types; asserted off below).  Floating point (mpmath, numpy) appears ONLY in
the numerical cross-check and is labelled as such in the JSON.

Run from the lane root:
    .venv/bin/python code/indep_slice_check.py                       # full run -> evidence/indep_slice_check.json
    .venv/bin/python code/indep_slice_check.py --n-samples 4 --n-control-samples 2 --out -   # smoke, no file

=====================================================================================================
DERIVATION (re-derived independently; every algebraic identity marked [X] is re-checked EXACTLY
as a polynomial identity over ZZ in exact_identities()).

Notation.  Coordinates k = 0,1,2,3 <-> (r,t) = (-1,-1), (-1,1), (1,-1), (1,1) (row/col -1 first,
l.639-641); (x,y,z,w) = (mu_0,mu_1,mu_2,mu_3) as in (5.7).  S = 2x2 nonneg. integer matrices with
entry sum 5 and all row/col sums >= 1, w_s = 5!/prod s_k!.  For mu in (0,inf)^4:
    d_s = w_s mu^s,  Phi = sum_s d_s,  m = sum_s d_s s,  S2 = sum_s d_s s s^T,  D = diag(m).
 [X] Phi equals the closed form (x+y+z+w)^5-(x+y)^5-(x+z)^5-(y+w)^5-(z+w)^5+x^5+y^5+z^5+w^5
     (inclusion-exclusion over the four empty-margin events; pairwise intersections leave one cell).
 [X] F1: mu_l dm_k/dmu_l = sum_s d_s s_k s_l = S2_kl   (Euler: mu_l d(mu^s)/dmu_l = s_l mu^s).
 [X] F2: sum_k s_k = 5 for every s  =>  S2 1 = 5 m,  sum_k m_k = 5 Phi,  m = mu * grad Phi (=(5.8)).
     F3: D 1 = m (trivial).
 [X] F4: S spans R^4 and d_s > 0  =>  S2 = sum_s d_s s s^T is positive definite (PD).

(a) Let theta = ln mu.  By F1, dm/dtheta = S2 (PD, F4); so theta(m) is smooth on the open cone
    {m(mu): mu > 0} (= interior of M0, Lemma 5.3) with dtheta/dm = S2^{-1} (symmetric).  Then
        grad psi = ln m/2 + 1/2 - theta - (dtheta/dm)^T m = ln m/2 + 1/2 - theta - S2^{-1} m
                 = ln m/2 - theta + 3/10          (S2^{-1} m = 1/5 by F2; this is paper (5.18)-(5.19)),
        Hess psi = D^{-1}/2 - dtheta/dm = D^{-1}/2 - S2^{-1}.
    VERDICT (a): correct.

(b) Slice {sum m = c}: tangent space U = 1^perp.  Scaled coordinates: put S^ = D^{-1/2} S2 D^{-1/2}
    (PD).  By F2, S^ sqrt(m) = D^{-1/2} S2 1 = 5 D^{-1/2} m = 5 sqrt(m): sqrt(m) is an EIGENVECTOR of
    S^, so V := sqrt(m)^perp is S^-invariant and (S^^{-1})|_V = (S^|_V)^{-1} exactly.
    u in U  <=>  u = D^{1/2} a with a in V;   v in m^perp  <=>  v = D^{-1/2} c with c in V.
        u^T Hess psi u = a^T (I/2 - S^^{-1}) a,     v^T S2 v = c^T S^ c,     v^T D v = c^T c.
    Hence, with r_1..r_3 the eigenvalues of S^|_V (= generalised eigenvalues of (S2 | D) on m^perp),
    the slice Hessian, taken w.r.t. the metric u^T D^{-1} u on U, has eigenvalues
        lambda_i = 1/2 - 1/r_i,     i.e.   r_i = 2/(1 - 2 lambda_i),
    and   slice Hessian negative definite (ND)  <=>  all r_i < 2  <=>  u^T S2 u < 2 u^T D u on
    m^perp \ {0}.  (The switch from 1^perp to m^perp is legitimate ONLY because S2 1 and D 1 are both
    parallel to m, i.e. because every spectrum has entry sum 5; for a general PD S^ the compression
    of the inverse dominates the inverse of the compression and only "=>" would survive.)
    VERDICT (b): correct, with a wording caveat: the exact equivalence is "slice Hessian ND at m(mu)
    <=> condition"; ND implies local strict concavity but not conversely, so "strictly concave at
    m(mu) iff" overstates the converse.  ND on the whole open (convex) slice => strictly concave there.

(c) Mpoly = 5 Phi (2D - S2) + 3 m m^T.  Mpoly 1 = 5 Phi (2m - 5m) + 3 m (5 Phi) = 0 [X].  For v in
    m^perp: v^T Mpoly v = 5 Phi v^T (2D - S2) v with Phi > 0.  Since <m,1> = 5 Phi > 0, every x is
    x = v + t 1 with v in m^perp, and x^T Mpoly x = v^T Mpoly v (Mpoly symmetric, Mpoly 1 = 0).  The
    coordinate hyperplane {x_k = 0} is a complement of span(1) for every k (1 has no zero entry), so
        (b)  <=>  Mpoly PD on m^perp  <=>  Mpoly PSD with kernel exactly span(1)
             <=>  the 3x3 principal block with index k deleted is PD   (for any single k).
    Entries are integer homogeneous polynomials of degree 10 in mu [X].
    In scaled form D^{-1/2} Mpoly D^{-1/2} = 5 Phi (2I - S^)|_V (+) 0 on sqrt(m) (|sqrt m|^2 = 5 Phi),
    so for every k the 3x3 principal minor (= (k,k) cofactor) is the SAME polynomial
        P3 = adj(Mpoly)_kk = 25 Phi^2 (m_0 m_1 m_2 m_3) prod_i (2 - r_i)               (*)
    (adj of a rank-3 symmetric matrix with kernel 1 is c 1 1^T).  Since S^ has eigenvalue 5 on
    sqrt(m), prod_i (2 - r_i) = det(2I - S^)/(2 - 5) = -det(2D - S2)/(3 prod m), so (*) is the
    polynomial identity  3 P3 = -25 Phi^2 det(2D - S2)  [X, degree 30].  (*) links the FD eigenvalues
    of the slice Hessian directly to the degree-30 minor (numerical cross-check) and gives
    (2 - max r)^3 <= prod(2 - r_i) = P3 / (25 Phi^2 prod m), used for the boundary-margin addendum.
    VERDICT (c): correct.

(d) Sylvester: the 3x3 block is PD iff its three leading principal minors (degrees 10, 20, 30) are
    > 0; a nonzero polynomial whose coefficients are all positive is > 0 on (0,inf)^4.  Computed
    below for all four dropped indices (plus all 1x1 and 2x2 principal minors).  Every interior m of
    the cone equals m(mu) for some mu > 0 (existence half of Lemma 5.3, l.1013-1107), so positivity
    on (0,inf)^4 gives ND slice Hessian on the whole open cone.  It says nothing about the boundary
    of M0(c) (concavity, not strict concavity, extends to the closure by continuity).
    Addendum (margin): along mu(t) = (t^5, t^4, t^2, 1), all coefficients being positive, for
    0 < t <= 1:  P3(mu(t)) <= P3(1,1,1,1) t^{v3}  and  25 Phi^2 prod m >= 25 lc(Phi)^2 prod lc(m_k)
    t^{v0} (v = valuations, lc = leading coefficients); if v3 > v0 then max r -> 2, i.e. the
    supremum of u^T S2 u / u^T D u over the open cone is exactly 2 (not attained): no uniform margin.

Controls.  Ordinary analogue (all 56 matrices, Phi = (x+y+z+w)^5): d_s/Phi is Multinomial(5, p),
p = mu/sum(mu), so S2 = Phi (5 diag p + 20 p p^T) = D + (4/(5 Phi)) m m^T  [X], hence u^T S2 u =
u^T D u on m^perp: the ratio is identically 1 (all r_i = 1, lambda_i = -1/2), and
Mpoly = 25 sigma^8 (sigma diag(mu) - mu mu^T), sigma = sum mu  [X], whose leading minors are
25 sigma^8 mu_a (sigma - mu_a), (25 sigma^8)^2 sigma mu_a mu_b (sigma - mu_a - mu_b),
(25 sigma^8)^3 sigma^2 mu_0 mu_1 mu_2 mu_3  [X].
Mutation controls: drop s = (1,1,1,2) from S (requested; just reported), and the corrupted
threshold 2 -> 1 (Mpoly_1 = 5 Phi (D - S2) + 4 m m^T; must FAIL because r = 229/225 > 1 at the
centre), which shows the all-positive-coefficient test is not vacuous.
=====================================================================================================
"""

import os

os.environ["SYMPY_GROUND_TYPES"] = "python"
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"

import argparse  # noqa: E402
import hashlib  # noqa: E402
import itertools  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import platform  # noqa: E402
import re  # noqa: E402
import resource  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402
from math import comb, factorial, gcd  # noqa: E402

import mpmath  # noqa: E402
import numpy as np  # noqa: E402
import sympy  # noqa: E402
from sympy import Matrix, Poly, Rational, ZZ, symbols  # noqa: E402
from sympy.external.gmpy import GROUND_TYPES  # noqa: E402

assert GROUND_TYPES == "python", f"sympy ground types {GROUND_TYPES!r}, expected 'python'"
assert "flint" not in sys.modules, "python-flint must not be imported"

X = symbols("x y z w")
COORDS = ["(-1,-1)", "(-1,1)", "(1,-1)", "(1,1)"]
LANE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIBLING_P3 = os.path.join("evidence", "slice_P3_drop3_rainbow.txt")
mp = mpmath.mp


def host_date():
    return subprocess.run(["date"], capture_output=True, text=True, check=True).stdout.strip()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ------------------------------------------------------------------------------------------------
# Exact part (sympy Poly over ZZ, pure-Python integers)
# ------------------------------------------------------------------------------------------------

def spectra(kind):
    out = []
    for s in itertools.product(range(6), repeat=4):
        if sum(s) != 5:
            continue
        if kind == "rainbow" and min(s[0] + s[1], s[2] + s[3], s[0] + s[2], s[1] + s[3]) < 1:
            continue
        out.append(s)
    return out


def weight(s):
    return factorial(5) // (factorial(s[0]) * factorial(s[1]) * factorial(s[2]) * factorial(s[3]))


def zpoly(coeffs):
    return Poly.from_dict(coeffs, *X, domain=ZZ)


def build_model(spec):
    wts = {s: weight(s) for s in spec}
    phi = zpoly({s: wts[s] for s in spec})
    m = [zpoly({s: wts[s] * s[k] for s in spec if s[k]}) for k in range(4)]
    s2 = [[zpoly({s: wts[s] * s[k] * s[l] for s in spec if s[k] and s[l]}) for l in range(4)]
          for k in range(4)]
    return wts, phi, m, s2


def build_mpoly(phi, m, s2, c):
    """5 Phi (c D - S2) + (5 - c) m m^T; c = 2 is the claimed matrix, (5 - c) keeps Mpoly 1 = 0."""
    mat = [[None] * 4 for _ in range(4)]
    for k in range(4):
        for l in range(k, 4):
            e = -s2[k][l]
            if k == l:
                e = e + c * m[k]
            mat[k][l] = 5 * phi * e + (5 - c) * m[k] * m[l]
            mat[l][k] = mat[k][l]
    return mat


def det2(mat, i, j):
    return mat[i][i] * mat[j][j] - mat[i][j] * mat[i][j]


def det3(mat, i, j, k):
    a, b, c = mat[i][i], mat[i][j], mat[i][k]
    e, f, g = mat[j][j], mat[j][k], mat[k][k]
    return a * (e * g - f * f) - b * (b * g - f * c) + c * (b * f - e * c)


def det3g(b):
    return (b[0][0] * (b[1][1] * b[2][2] - b[1][2] * b[2][1])
            - b[0][1] * (b[1][0] * b[2][2] - b[1][2] * b[2][0])
            + b[0][2] * (b[1][0] * b[2][1] - b[1][1] * b[2][0]))


def det4(a):
    out = zpoly({})
    for j in range(4):
        cols = [c for c in range(4) if c != j]
        t = a[0][j] * det3g([[a[r][c] for c in cols] for r in (1, 2, 3)])
        out = out + t if j % 2 == 0 else out - t
    return out


def star_identity(phi, m, s2, p3):
    """Exact polynomial form of (*): 3 P3 = -25 Phi^2 det(2D - S2)."""
    a = [[(2 * m[k] if k == l else zpoly({})) - s2[k][l] for l in range(4)] for k in range(4)]
    return 3 * p3 == -25 * phi ** 2 * det4(a)


def valuation(p, expo):
    """(lowest t-exponent, its coefficient) of p(t^expo); no cancellation when coefficients > 0."""
    vals = {}
    for mn, c in coeff_dict(p).items():
        v = sum(e * a for e, a in zip(expo, mn))
        vals[v] = vals.get(v, 0) + c
    v0 = min(vals)
    return v0, vals[v0]


def coeff_dict(p):
    return {tuple(mn): int(c) for mn, c in p.as_dict(native=True).items()}


def poly_stats(p, deg):
    cd = coeff_dict(p)
    if not cd:
        return {"degree_expected": deg, "zero_polynomial": True, "all_coefficients_positive": False}
    mons = sorted(cd)
    coeffs = [cd[mn] for mn in mons]
    cmin, cmax = min(coeffs), max(coeffs)
    g = 0
    for c in coeffs:
        g = gcd(g, c)
    canon = json.dumps([[list(mn), str(cd[mn])] for mn in mons], separators=(",", ":"))
    n_neg = sum(1 for c in coeffs if c < 0)
    neg_part = sum(c for c in coeffs if c < 0)
    return {
        "degree_expected": deg,
        "degrees_present": sorted({sum(mn) for mn in mons}),
        "n_terms": len(mons),
        "n_monomials_of_degree": comb(deg + 3, 3),
        "n_absent_monomials": comb(deg + 3, 3) - len(mons),
        "min_coeff": str(cmin),
        "min_coeff_monomial": list(mons[coeffs.index(cmin)]),
        "max_coeff": str(cmax),
        "max_coeff_monomial": list(mons[coeffs.index(cmax)]),
        "log10_min_coeff_abs": math.log10(abs(cmin)),
        "log10_max_coeff_abs": math.log10(abs(cmax)),
        "n_negative_coeffs": n_neg,
        "sum_negative_coeffs": str(neg_part),
        "all_coefficients_positive": n_neg == 0,
        "content_gcd": str(g),
        "value_at_ones": str(sum(coeffs)),
        "sha256_canonical_terms": hashlib.sha256(canon.encode()).hexdigest(),
    }


def minors_for(mat):
    cache = {}

    def get(idx):
        idx = tuple(idx)
        if idx not in cache:
            if len(idx) == 1:
                cache[idx] = mat[idx[0]][idx[0]]
            elif len(idx) == 2:
                cache[idx] = det2(mat, *idx)
            else:
                cache[idx] = det3(mat, *idx)
        return cache[idx]

    leading = {}
    for k in range(4):
        idx = [i for i in range(4) if i != k]
        leading[k] = {r: (idx[:r], get(idx[:r])) for r in (1, 2, 3)}
    for i in range(4):
        get((i,))
    for i, j in itertools.combinations(range(4), 2):
        get((i, j))
    return leading, cache


def minors_report(mat, t0):
    leading, cache = minors_for(mat)
    rep = {}
    for k in range(4):
        rep[f"drop_index_{k}_{COORDS[k]}"] = {
            f"P{r}": {"indices": idx, **poly_stats(p, 10 * r)} for r, (idx, p) in leading[k].items()
        }
    p3 = [leading[k][3][1] for k in range(4)]
    all_principal = {}
    for idx, p in sorted(cache.items(), key=lambda kv: (len(kv[0]), kv[0])):
        st = poly_stats(p, 10 * len(idx))
        all_principal["".join(map(str, idx))] = {
            "n_terms": st.get("n_terms"), "n_negative_coeffs": st.get("n_negative_coeffs"),
            "all_coefficients_positive": st["all_coefficients_positive"]}
    summary = {
        "leading_minors_all_coefficients_positive_all_k": all(
            rep[key][f"P{r}"]["all_coefficients_positive"] for key in rep for r in (1, 2, 3)),
        "P3_identical_polynomial_for_all_dropped_indices": all(p == p3[0] for p in p3),
        "all_1x1_2x2_3x3_principal_minors": all_principal,
        "all_principal_minors_all_coefficients_positive": all(
            v["all_coefficients_positive"] for v in all_principal.values()),
        "seconds": round(time.time() - t0, 2),
    }
    return {"leading_principal_minors": rep, "summary": summary}, leading


def exact_identities(spec, wts, phi, m, s2, mat, ordinary=False):
    xp = [zpoly({tuple(int(i == k) for i in range(4)): 1}) for k in range(4)]
    zero = zpoly({})
    x, y, z, w = X
    if ordinary:
        closed = Poly((x + y + z + w) ** 5, *X, domain=ZZ)
    else:
        closed = Poly((x + y + z + w) ** 5 - (x + y) ** 5 - (x + z) ** 5 - (y + w) ** 5 - (z + w) ** 5
                      + x ** 5 + y ** 5 + z ** 5 + w ** 5, *X, domain=ZZ)
    res = {
        "n_spectra": len(spec),
        "sum_weights": sum(wts.values()),
        "spectra_span_R4": Matrix([list(s) for s in spec]).rank() == 4,
        "Phi_equals_closed_form": phi == closed,
        "sum_m_equals_5Phi": (m[0] + m[1] + m[2] + m[3]) == 5 * phi,
        "m_equals_mu_gradPhi": all(xp[k] * phi.diff(X[k]) == m[k] for k in range(4)),
        "euler_mu_l_dm_k_dmu_l_equals_S2_kl": all(
            xp[l] * m[k].diff(X[l]) == s2[k][l] for k in range(4) for l in range(4)),
        "S2_symmetric": all(s2[k][l] == s2[l][k] for k in range(4) for l in range(4)),
        "S2_times_1_equals_5m": all((s2[k][0] + s2[k][1] + s2[k][2] + s2[k][3]) == 5 * m[k]
                                    for k in range(4)),
        "Mpoly_symmetric": all(mat[k][l] == mat[l][k] for k in range(4) for l in range(4)),
        "Mpoly_times_1_equals_0": all((mat[k][0] + mat[k][1] + mat[k][2] + mat[k][3]) == zero
                                      for k in range(4)),
        "Mpoly_entries_homogeneous_degree_10": all(
            {sum(mn) for mn in coeff_dict(mat[k][l])} <= {10} for k in range(4) for l in range(4)),
    }
    return res


def centre_exact(phi, m, s2, p3):
    """Exact data at mu = (1,1,1,1) (same direction as the paper's centre b, m = 5/36 each)."""
    ones = (1, 1, 1, 1)
    s2c = Matrix(4, 4, lambda k, l: s2[k][l].eval(ones))
    mc = [m[k].eval(ones) for k in range(4)]
    dc = Matrix.diag(*mc)
    U = Matrix([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])  # row, col, interaction contrasts
    assert all(sum(mc[k] * U[k, j] for k in range(4)) == 0 for j in range(3))
    gs, gd = U.T * s2c * U, U.T * dc * U
    rmat = gd.inv() * gs
    evs = rmat.eigenvals()
    r_list = sorted([Rational(ev) for ev, mult in evs.items() for _ in range(mult)])
    lam = [Rational(1, 2) - 1 / r for r in r_list]
    mstar = Rational(5, 36)
    phic = phi.eval(ones)
    p3_formula = 25 * phic ** 2 * mc[0] * mc[1] * mc[2] * mc[3]
    for r in r_list:
        p3_formula *= (2 - r)
    p3_val = p3.eval(ones)
    return {
        "Phi(1,1,1,1)": str(phic),
        "m(1,1,1,1)": [str(v) for v in mc],
        "contrast_basis_of_m_perp": "row (1,1,-1,-1), col (1,-1,1,-1), interaction (1,-1,-1,1)",
        "U^T S2 U": [[str(v) for v in gs.row(i)] for i in range(3)],
        "U^T D U": [[str(v) for v in gd.row(i)] for i in range(3)],
        "r_i_generalised_eigenvalues_S2_vs_D_on_m_perp": [str(r) for r in r_list],
        "max_ratio_uS2u_over_uDu_on_m_perp": str(max(r_list)),
        "lambda_i_slice_hessian_wrt_metric_Dinv": [str(v) for v in lam],
        "lambda_i_slice_hessian_euclidean_at_m_star_5/36": [str(v / mstar) for v in lam],
        "P3(1,1,1,1)": str(p3_val),
        "25 Phi^2 prod(m) prod(2 - r_i)": str(p3_formula),
        "identity_(*)_holds_exactly_at_centre": p3_val == p3_formula,
    }


def ordinary_closed_forms(m, s2, phi, mat, leading):
    x, y, z, w = X
    sig = Poly(x + y + z + w, *X, domain=ZZ)
    mu = [zpoly({tuple(int(i == k) for i in range(4)): 1}) for k in range(4)]
    cov_ok = all(5 * phi * (s2[k][l] - (m[k] if k == l else 0)) - 4 * m[k] * m[l] == zpoly({})
                 for k in range(4) for l in range(4))
    a = 25 * sig ** 8
    mat_ok = all(mat[k][l] == a * ((sig * mu[k] if k == l else 0) - mu[k] * mu[l])
                 for k in range(4) for l in range(4))
    lead_ok = True
    for k in range(4):
        idx = [i for i in range(4) if i != k]
        (i0, i1, i2) = idx
        lead_ok &= leading[k][1][1] == a * mu[i0] * (sig - mu[i0])
        lead_ok &= leading[k][2][1] == a ** 2 * sig * mu[i0] * mu[i1] * (sig - mu[i0] - mu[i1])
        lead_ok &= leading[k][3][1] == a ** 3 * sig ** 2 * mu[0] * mu[1] * mu[2] * mu[3]
    return {
        "identity_5Phi(S2-D)=4mm^T_exact": cov_ok,
        "consequence": "u^T S2 u = u^T D u + (4/(5 Phi)) <m,u>^2, so on m^perp the ratio "
                       "u^T S2 u / u^T D u is identically 1 for every mu > 0 and every u != 0",
        "exact_max_ratio_on_m_perp": "1" if cov_ok else "identity failed",
        "Mpoly_equals_25 sigma^8 (sigma diag(mu) - mu mu^T)": mat_ok,
        "leading_minors_equal_closed_forms": bool(lead_ok),
    }


# ------------------------------------------------------------------------------------------------
# Floating-point cross-check (mpmath at high precision; numpy float64 only for polynomial values)
# ------------------------------------------------------------------------------------------------

def eval_d(terms, theta):
    mu = [mp.exp(t) for t in theta]
    pw = []
    for k in range(4):
        row = [mp.one]
        for _ in range(5):
            row.append(row[-1] * mu[k])
        pw.append(row)
    return mu, [wt * pw[0][s[0]] * pw[1][s[1]] * pw[2][s[2]] * pw[3][s[3]] for wt, s in terms]


def m_of(terms, d):
    m = [mp.zero] * 4
    for (_, s), dd in zip(terms, d):
        for k in range(4):
            if s[k]:
                m[k] += dd * s[k]
    return m


def s2_of(terms, d):
    a = [[mp.zero] * 4 for _ in range(4)]
    for (_, s), dd in zip(terms, d):
        for k in range(4):
            if s[k]:
                t = dd * s[k]
                for l in range(k, 4):
                    if s[l]:
                        a[k][l] += t * s[l]
    for k in range(4):
        for l in range(k):
            a[k][l] = a[l][k]
    return a


def solve_lin(a, b):
    n = len(b)
    aug = [list(a[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        p = aug[col][col]
        for r in range(col + 1, n):
            f = aug[r][col] / p
            for c in range(col, n + 1):
                aug[r][c] -= f * aug[col][c]
    xs = [mp.zero] * n
    for r in range(n - 1, -1, -1):
        s = aug[r][n]
        for c in range(r + 1, n):
            s -= aug[r][c] * xs[c]
        xs[r] = s / aug[r][r]
    return xs


def scaled(s2, m):
    rt = [mp.sqrt(v) for v in m]
    return [[s2[k][l] / (rt[k] * rt[l]) for l in range(4)] for k in range(4)], rt


def newton_theta(terms, mt, theta0, tol, maxit=80):
    """Own Newton solve of m(exp(theta)) = mt in theta = ln mu (Jacobian S2, diagonally scaled)."""
    th = list(theta0)
    for it in range(maxit):
        _, d = eval_d(terms, th)
        m = m_of(terms, d)
        res = [mt[k] - m[k] for k in range(4)]
        if max(abs(res[k]) / mt[k] for k in range(4)) < tol:
            return th, it
        sh, rt = scaled(s2_of(terms, d), m)
        yv = solve_lin(sh, [res[k] / rt[k] for k in range(4)])
        th = [th[k] + yv[k] / rt[k] for k in range(4)]
    raise RuntimeError("Newton did not converge")


def psi_of(mt, th):
    return mp.fsum(mt[k] * (mp.log(mt[k]) / 2 - th[k]) for k in range(4))


def householder_basis(a):
    """Orthonormal basis (4x3, columns) of a^perp for a unit vector a with a_0 > 0."""
    v = [a[0] + 1] + list(a[1:])
    vv = mp.fsum(t * t for t in v)
    h = [[(1 if i == j else 0) - 2 * v[i] * v[j] / vv for j in range(4)] for i in range(4)]
    return [[h[i][j] for j in range(1, 4)] for i in range(4)]


def eig_sym(a):
    ev = mp.eigsy(mp.matrix(a), eigvals_only=True)
    return sorted(ev[i] for i in range(len(a)))


def scaled_frame(terms, theta):
    """d, m, S2, S^ = D^{-1/2} S2 D^{-1/2}, sqrt(m), E (orthonormal basis of sqrt(m)^perp)."""
    _, d = eval_d(terms, theta)
    m = m_of(terms, d)
    s2 = s2_of(terms, d)
    sh, rt = scaled(s2, m)
    nrm = mp.sqrt(mp.fsum(m))
    e = householder_basis([v / nrm for v in rt])
    return d, m, s2, sh, rt, e


def r_direct(sh, e):
    """Eigenvalues of E^T S^ E = generalised eigenvalues of (S2 | D) on m^perp."""
    return eig_sym([[mp.fsum(e[k][i] * sh[k][l] * e[l][j] for k in range(4) for l in range(4))
                     for j in range(3)] for i in range(3)])


def numeric_point(terms, theta0, eps, tol, c=2):
    d0, m0, s20, sh, rt, e = scaled_frame(terms, theta0)
    phi0 = mp.fsum(d0)
    # analytic, formula (a): H_an = E^T (I/2 - S^^{-1}) E ; direct r: eig(E^T S^ E)
    sinv_e = [solve_lin(sh, [e[k][j] for k in range(4)]) for j in range(3)]
    h_an = [[(mp.mpf(1) / 2 if i == j else 0) - mp.fsum(e[k][i] * sinv_e[j][k] for k in range(4))
             for j in range(3)] for i in range(3)]
    r_dir = r_direct(sh, e)
    # finite differences of psi along b_i = D^{1/2} E_i (Newton for every evaluation)
    h = eps * mp.sqrt(min(m0))
    b = [[rt[k] * e[k][i] for k in range(4)] for i in range(3)]
    psi0 = psi_of(m0, theta0)
    cache = {}
    max_it = 0

    def psi_at(ci):
        nonlocal max_it
        if ci not in cache:
            mt = [m0[k] + h * mp.fsum(ci[i] * b[i][k] for i in range(3)) for k in range(4)]
            th, it = newton_theta(terms, mt, theta0, tol)
            max_it = max(max_it, it)
            cache[ci] = psi_of(mt, th)
        return cache[ci]

    h_fd = [[None] * 3 for _ in range(3)]
    for i in range(3):
        ei = tuple(int(t == i) for t in range(3))
        mi = tuple(-v for v in ei)
        h_fd[i][i] = (psi_at(ei) - 2 * psi0 + psi_at(mi)) / h ** 2
        for j in range(i + 1, 3):
            pp = tuple(int(t == i) + int(t == j) for t in range(3))
            pm = tuple(int(t == i) - int(t == j) for t in range(3))
            h_fd[i][j] = h_fd[j][i] = (psi_at(pp) - psi_at(pm) - psi_at(tuple(-v for v in pm))
                                       + psi_at(tuple(-v for v in pp))) / (4 * h ** 2)
    lam_fd = eig_sym(h_fd)
    lam_an = eig_sym(h_an)
    r_fd = sorted(2 / (1 - 2 * v) for v in lam_fd)
    diff = mp.sqrt(mp.fsum((h_fd[i][j] - h_an[i][j]) ** 2 for i in range(3) for j in range(3)))
    nrm_an = mp.sqrt(mp.fsum(h_an[i][j] ** 2 for i in range(3) for j in range(3)))
    # numeric Mpoly(mu0) and its leading minors for every dropped index
    mm = [[5 * phi0 * ((c * m0[k] if k == l else 0) - s20[k][l]) + (5 - c) * m0[k] * m0[l]
           for l in range(4)] for k in range(4)]
    mins = {}
    for k in range(4):
        idx = [i for i in range(4) if i != k]
        a_ = mm[idx[0]][idx[0]]
        two = mm[idx[0]][idx[0]] * mm[idx[1]][idx[1]] - mm[idx[0]][idx[1]] ** 2
        three = mp.det(mp.matrix([[mm[i][j] for j in idx] for i in idx]))
        mins[k] = (a_, two, three)
    prod_m = m0[0] * m0[1] * m0[2] * m0[3]
    two_minus_r = [2 - r for r in r_fd]
    p3_from_fd = 25 * phi0 ** 2 * prod_m * two_minus_r[0] * two_minus_r[1] * two_minus_r[2]
    return {
        "lam_fd": lam_fd, "lam_an": lam_an, "r_fd": r_fd, "r_dir": r_dir,
        "h_relerr": diff / nrm_an, "mins": mins, "p3_from_fd": p3_from_fd, "max_newton_it": max_it,
        "m_ratio": max(m0) / min(m0),
    }


def poly_log_values(p, logmu):
    """log of a polynomial with POSITIVE coefficients at many points (float64, log-sum-exp)."""
    cd = coeff_dict(p)
    mons = np.array(list(cd.keys()), dtype=np.float64)
    if not all(v > 0 for v in cd.values()):
        return None
    logc = np.array([math.log(v) for v in cd.values()])
    out = np.empty(logmu.shape[0])
    for start in range(0, logmu.shape[0], 200):
        lt = logc[:, None] + mons @ logmu[start:start + 200].T
        mx = lt.max(axis=0)
        out[start:start + 200] = mx + np.log(np.exp(lt - mx).sum(axis=0))
    return out


def numeric_crosscheck(spec, wts, leading, n, seed, dps, eps, label, expect_r=None):
    t0 = time.time()
    mp.dps = dps
    tol = mp.mpf(10) ** (-(dps - 12))
    terms = [(mp.mpf(wts[s]), s) for s in spec]
    rng = np.random.default_rng(seed)
    logmu = rng.uniform(-4.0, 4.0, size=(n, 4)) * math.log(10.0)
    mu_samples = np.exp(logmu)
    logmu = np.log(mu_samples)  # consistent with the floats actually used
    poly_logs = {}
    for k in range(4):
        for r in (1, 2, 3):
            idx, p = leading[k][r]
            key = tuple(idx)
            if key not in poly_logs:
                poly_logs[key] = poly_log_values(p, logmu)
    rows = []
    for t in range(n):
        theta0 = [mp.log(mp.mpf(float(v))) for v in mu_samples[t]]
        rows.append(numeric_point(terms, theta0, eps, tol))
    # ---- summaries (all floating point) ----
    lam_max = [float(max(rw["lam_fd"])) for rw in rows]
    r_max = [float(max(rw["r_dir"])) for rw in rows]
    all_fd_neg = [max(rw["lam_fd"]) < 0 for rw in rows]
    all_an_neg = [max(rw["lam_an"]) < 0 for rw in rows]
    minors_pos = [all(v > 0 for k in range(4) for v in rw["mins"][k]) for rw in rows]
    r_relerr = [float(max(abs(a - b) / b for a, b in zip(rw["r_fd"], rw["r_dir"]))) for rw in rows]
    h_relerr = [float(rw["h_relerr"]) for rw in rows]
    dlog_num = 0.0
    dlog_p3_fd = 0.0
    p3_identity_defined = 0
    for t, rw in enumerate(rows):
        for k in range(4):
            for r in (1, 2, 3):
                key = tuple(leading[k][r][0])
                pl = poly_logs[key]
                val = rw["mins"][k][r - 1]
                if pl is not None and val > 0:
                    dlog_num = max(dlog_num, abs(float(mp.log(val)) - pl[t]))
        if rw["p3_from_fd"] > 0 and poly_logs[tuple(leading[3][3][0])] is not None:
            p3_identity_defined += 1
            dlog_p3_fd = max(dlog_p3_fd,
                             abs(float(mp.log(rw["p3_from_fd"])) - poly_logs[tuple(leading[3][3][0])][t]))
    i_worst = int(np.argmax(r_max))
    out = {
        "LABEL": "FLOATING POINT cross-check (mpmath dps=%d for FD/Newton/eigen; numpy float64 "
                 "log-sum-exp for polynomial values). Not a proof." % dps,
        "model": label,
        "n_samples": n,
        "seed": seed,
        "sampler": "numpy.random.default_rng(seed).uniform(-4,4,(n,4)); mu = 10**u (log-uniform "
                   "on [1e-4,1e4]^4); theta0 = ln(mu) of the float64 values",
        "fd_scheme": "central 2nd differences of psi along b_i = D^{1/2} E_i (E orthonormal basis of "
                     "sqrt(m)^perp, Householder), step h = eps*sqrt(min m); psi via own Newton in "
                     "theta = ln mu, |residual|/m < 1e-(dps-12)",
        "eps": eps,
        "max_newton_iterations": max(rw["max_newton_it"] for rw in rows),
        "max_m_ratio_max_over_min": float(max(rw["m_ratio"] for rw in rows)),
        "n_fd_slice_hessian_negative_definite": sum(all_fd_neg),
        "n_analytic_slice_hessian_negative_definite": sum(all_an_neg),
        "n_numeric_Mpoly_minors_all_positive_all_k": sum(minors_pos),
        "n_concordant_fd_ND_iff_minors_positive": sum(1 for a, b in zip(all_fd_neg, minors_pos) if a == b),
        "max_relerr_Hfd_vs_Hanalytic_frobenius": max(h_relerr),
        "max_relerr_r_from_fd_vs_r_direct": max(r_relerr),
        "max_abs_dlog_polynomial_minors_vs_numeric_matrix_minors": dlog_num,
        "max_abs_dlog_P3_poly_vs_25Phi^2_prod_m_prod(2-r_fd)": dlog_p3_fd,
        "n_P3_identity_evaluated": p3_identity_defined,
        "max_over_samples_of_max_lambda_fd": max(lam_max),
        "min_over_samples_of_min_lambda_fd": float(min(min(rw["lam_fd"]) for rw in rows)),
        "max_over_samples_of_max_r_direct": max(r_max),
        "min_over_samples_of_min_r_direct": float(min(min(rw["r_dir"]) for rw in rows)),
        "quantiles_max_r_direct_[0,.5,.9,.99,1]": [float(q) for q in
                                                   np.quantile(r_max, [0, .5, .9, .99, 1])],
        "worst_sample": {
            "index": i_worst,
            "mu": [float(v) for v in mu_samples[i_worst]],
            "r_direct": [float(v) for v in rows[i_worst]["r_dir"]],
            "r_from_fd": [float(v) for v in rows[i_worst]["r_fd"]],
            "lambda_fd": [float(v) for v in rows[i_worst]["lam_fd"]],
        },
        "seconds": round(time.time() - t0, 2),
    }
    if expect_r is not None:
        out[f"max_abs_r_direct_minus_{expect_r}"] = float(
            max(abs(v - expect_r) for rw in rows for v in rw["r_dir"]))
        out[f"max_abs_r_fd_minus_{expect_r}"] = float(
            max(abs(v - expect_r) for rw in rows for v in rw["r_fd"]))
        out["max_abs_lambda_fd_plus_1/2"] = float(
            max(abs(v + mp.mpf(1) / 2) for rw in rows for v in rw["lam_fd"]))
    return out


def boundary_margin(spec, wts, phi, m, p3, dps, expo=(5, 4, 2, 0)):
    """Exact: valuations along mu(t) = t^expo; then a labelled floating-point probe of max r."""
    v3, c3 = valuation(p3, expo)
    rest = sum(coeff_dict(p3).values()) - c3
    vphi, cphi = valuation(phi, expo)
    vm = [valuation(mk, expo) for mk in m]
    v0 = 2 * vphi + sum(v for v, _ in vm)
    lc0 = 25 * cphi ** 2
    for _, c in vm:
        lc0 *= c
    e3 = v3 - v0
    lead, tail = Fraction(c3, lc0), Fraction(rest, lc0)
    out = {
        "family": "mu(t) = (t^5, t^4, t^2, 1), 0 < t <= 1 (monomial curve chosen after random sample "
                  "#3 of seed 20261016, mu ~ 10^(-3.88,-2.80,-0.01,3.52), max r 1.9497; regime: "
                  "spectrum (1,0,0,4) dominates and (0,1,1,3) dominates the spectra touching y or z)",
        "valuation_P3": v3, "leading_coeff_P3": str(c3),
        "valuations_Phi_m": [vphi] + [v for v, _ in vm],
        "valuation_25Phi^2_prod_m": v0, "leading_coeff_25Phi^2_prod_m": str(lc0),
        "exact_bound": f"(2 - max r)^3 <= prod_i(2 - r_i) = P3/(25 Phi^2 prod m) <= {lead} t^{e3} + "
                       f"({tail}) t^{e3 + 1}  for 0 < t <= 1 (all coefficients > 0)",
        "exact_asymptotics": f"prod_i(2 - r_i) = {lead} t^{e3} (1 + O(t)) as t -> 0+",
        "conclusion_sup_max_r_equals_2_not_attained": e3 > 0,
    }
    mp.dps = dps
    terms = [(mp.mpf(wts[s]), s) for s in spec]
    probe = []
    for lg in (0.5, 1, 2, 4, 8, 16):
        t = mp.mpf(10) ** (-lg)
        _, _, _, sh, _, e = scaled_frame(terms, [a * mp.log(t) for a in expo])
        rr = r_direct(sh, e)
        prod = (2 - rr[0]) * (2 - rr[1]) * (2 - rr[2])
        bound = ((lead.numerator * t ** e3 / lead.denominator)
                 + (tail.numerator * t ** (e3 + 1) / tail.denominator)) ** (mp.mpf(1) / 3)
        probe.append({"t": f"10^-{lg}", "r_i": [float(v) for v in rr],
                      "2_minus_max_r": float(2 - rr[2]),
                      "prod(2-r_i)/t^%d" % e3: float(prod / t ** e3),
                      "exact_upper_bound_on_2_minus_max_r": float(bound)})
    out["FLOATING_POINT_probe_dps_%d" % dps] = probe
    return out


# ------------------------------------------------------------------------------------------------
# Post-hoc comparison with the sibling artifact (read only AFTER the independent computation)
# ------------------------------------------------------------------------------------------------

TERM_RE = re.compile(r"([+-]?)([^+-]+)")


def parse_sibling_poly(text):
    names = {"x": 0, "y": 1, "z": 2, "w": 3}
    out = {}
    body = text.replace(" ", "").replace("**", "^").strip()
    for sign, term in TERM_RE.findall(body):
        coef = 1
        exps = [0, 0, 0, 0]
        for fac in term.split("*"):
            if fac.isdigit():
                coef *= int(fac)
            elif "^" in fac:
                v, ex = fac.split("^")
                exps[names[v]] += int(ex)
            else:
                exps[names[fac]] += 1
        coef = -coef if sign == "-" else coef
        key = tuple(exps)
        out[key] = out.get(key, 0) + coef
    return {k: v for k, v in out.items() if v}


def compare_sibling(p3):
    path = os.path.join(LANE_ROOT, SIBLING_P3)
    if not os.path.exists(path):
        return {"file": SIBLING_P3, "present": False}
    with open(path) as fh:
        text = fh.read()
    sib = parse_sibling_poly(text)
    mine = coeff_dict(p3)
    res = {"file": SIBLING_P3, "present": True, "sha256": sha256_file(path),
           "n_terms_sibling": len(sib), "n_terms_mine": len(mine),
           "identical": sib == mine}
    if not res["identical"] and sib and set(sib) == set(mine):
        k0 = next(iter(mine))
        num, den = sib[k0], mine[k0]
        res["proportional"] = all(sib[k] * den == mine[k] * num for k in mine)
        res["ratio_sibling_over_mine"] = f"{num}/{den}"
    return res


# ------------------------------------------------------------------------------------------------

def model_block(kind_label, spec, c, t0, ordinary=False):
    wts, phi, m, s2 = build_model(spec)
    mat = build_mpoly(phi, m, s2, c)
    ident = exact_identities(spec, wts, phi, m, s2, mat, ordinary=ordinary)
    rep, leading = minors_report(mat, t0)
    if c == 2:
        ident["identity_(*)_3P3_equals_minus25Phi^2_det(2D-S2)"] = star_identity(
            phi, m, s2, leading[3][3][1])
    return {"model": kind_label, "threshold_c": c, "exact_identities": ident, **rep}, \
        (wts, phi, m, s2, mat, leading)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-samples", type=int, default=2000)
    ap.add_argument("--n-control-samples", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20261016)
    ap.add_argument("--control-seed", type=int, default=20261017)
    ap.add_argument("--dps", type=int, default=120)
    ap.add_argument("--eps", type=float, default=1e-15)
    ap.add_argument("--out", default=os.path.join("evidence", "indep_slice_check.json"))
    args = ap.parse_args()
    os.chdir(LANE_ROOT)

    t_start = time.time()
    date_start = host_date()
    print("start", date_start, flush=True)
    result = {
        "artifact": "evidence/indep_slice_check.json",
        "worker": "PhysRandomColour.SliceConcavityIndep",
        "lane": "physics/evidence/six-lane-20261016/random5reg-colour",
        "script": "code/indep_slice_check.py",
        "script_sha256": sha256_file(os.path.abspath(__file__)),
        "date_start_host": date_start,
        "independence": "code/model.py and code/slice_poly.py neither read nor imported; exact part "
                        "uses sympy Poly over ZZ with SYMPY_GROUND_TYPES=python (python-flint not "
                        "imported: checked at start and end)",
        "argv": sys.argv[1:],
        "versions": {
            "python": sys.version.split()[0], "sympy": sympy.__version__, "mpmath": mpmath.__version__,
            "numpy": np.__version__, "sympy_ground_types": GROUND_TYPES,
            "mpmath_backend": mpmath.libmp.BACKEND, "platform": platform.platform(),
        },
        "primary_text": {
            "file": "sources/diaz2009-3col-preprint.layout.txt",
            "sha256": sha256_file(os.path.join("sources", "diaz2009-3col-preprint.layout.txt")),
            "lines": {"spectra": "653-658, 1693-1703", "Phi_(5.7)": "993-1001",
                      "Lemma_5.3": "1013-1118", "(5.18)-(5.19)": "1202-1225",
                      "numerically_confirmed_concavity_claim": "1839-1844"},
        },
    }
    timings = {}

    # ---- rainbow (the claim) ----
    t0 = time.time()
    rain = spectra("rainbow")
    block, (wts, phi, m, s2, mat, leading) = model_block("rainbow_36_spectra", rain, 2, t0)
    block["centre_exact_mu_ones"] = centre_exact(phi, m, s2, leading[3][3][1])
    block["boundary_margin_addendum"] = boundary_margin(rain, wts, phi, m, leading[3][3][1], args.dps)
    result["rainbow"] = block
    timings["rainbow_exact"] = round(time.time() - t0, 2)
    print("rainbow exact done", timings["rainbow_exact"], flush=True)
    rain_leading = leading
    rain_wts = wts

    # ---- ordinary control ----
    t0 = time.time()
    ordi = spectra("ordinary")
    oblock, (owts, ophi, om, os2, omat, olead) = model_block("ordinary_56_matrices", ordi, 2, t0,
                                                             ordinary=True)
    oblock["closed_forms"] = ordinary_closed_forms(om, os2, ophi, omat, olead)
    oblock["result"] = (
        "minors: all coefficients positive = %s; exact max u^T S2 u / u^T D u on m^perp = %s"
        % (oblock["summary"]["leading_minors_all_coefficients_positive_all_k"],
           oblock["closed_forms"]["exact_max_ratio_on_m_perp"]))
    timings["ordinary_exact"] = round(time.time() - t0, 2)
    print("ordinary exact done", timings["ordinary_exact"], flush=True)

    # ---- mutation: drop (1,1,1,2) ----
    t0 = time.time()
    drop = [s for s in rain if s != (1, 1, 1, 2)]
    assert len(drop) == 35
    dblock, _ = model_block("rainbow_minus_(1,1,1,2)", drop, 2, t0)
    dblock["dropped_spectrum"] = {"s": [1, 1, 1, 2], "w_s": weight((1, 1, 1, 2))}
    dblock["note"] = ("Phi_equals_closed_form = false is expected: (5.7) is the closed form for all 36 "
                      "spectra; the other identities only need entry sum 5 and still hold")
    dblock["result"] = ("all-positive coefficients PERSIST after dropping (1,1,1,2)"
                        if dblock["summary"]["leading_minors_all_coefficients_positive_all_k"]
                        else "all-positive coefficients DO NOT persist after dropping (1,1,1,2)")
    timings["drop_exact"] = round(time.time() - t0, 2)
    print("drop exact done", timings["drop_exact"], flush=True)

    # ---- mutation: corrupted threshold 2 -> 1 ----
    t0 = time.time()
    tblock, _ = model_block("rainbow_36_threshold_1_(corrupted)", rain, 1, t0)
    tblock["note"] = ("Mpoly_1 = 5 Phi (D - S2) + 4 m m^T (threshold 2 -> 1); must be rejected because "
                      "r = 229/225 > 1 at the centre (and the ordinary analogue sits exactly at r = 1)")
    tblock["result"] = ("REJECTED as required: negative coefficients present"
                        if not tblock["summary"]["leading_minors_all_coefficients_positive_all_k"]
                        else "NOT rejected: control failed")
    timings["threshold1_exact"] = round(time.time() - t0, 2)
    print("threshold-1 exact done", timings["threshold1_exact"], flush=True)

    # ---- numerical cross-checks (floating point) ----
    t0 = time.time()
    num_rain = numeric_crosscheck(rain, rain_wts, rain_leading, args.n_samples, args.seed, args.dps,
                                  args.eps, "rainbow_36_spectra")
    timings["numeric_rainbow"] = round(time.time() - t0, 2)
    print("numeric rainbow done", timings["numeric_rainbow"], flush=True)
    t0 = time.time()
    num_ord = numeric_crosscheck(ordi, owts, olead, args.n_control_samples, args.control_seed,
                                 args.dps, args.eps, "ordinary_56_matrices", expect_r=1)
    timings["numeric_ordinary"] = round(time.time() - t0, 2)
    print("numeric ordinary done", timings["numeric_ordinary"], flush=True)

    result["numeric_crosscheck"] = {"rainbow": num_rain, "ordinary_control": num_ord}
    result["controls"] = {
        "ordinary_analogue": oblock,
        "mutation_drop_spectrum_(1,1,1,2)": dblock,
        "mutation_threshold_2_to_1": tblock,
    }

    # ---- post-hoc comparison with sibling artifact ----
    result["posthoc_comparison_sibling_P3"] = compare_sibling(rain_leading[3][3][1])

    # ---- verdicts ----
    rs = block["summary"]
    ids = block["exact_identities"]
    result["derivation_verdict"] = {
        "a": {"verdict": "correct",
              "statement": "Hess psi = D^{-1}/2 - S2^{-1} in m-coordinates",
              "basis": "dm/d(ln mu) = S2 (exact Euler identity), S2 PD (spectra span R^4), "
                       "S2^{-1} m = 1/5 from S2 1 = 5 m (exact); grad psi = ln m/2 - ln mu + 3/10 "
                       "reproduces paper (5.19)",
              "exact_support": {k: ids[k] for k in ("euler_mu_l_dm_k_dmu_l_equals_S2_kl",
                                                    "S2_times_1_equals_5m", "spectra_span_R4",
                                                    "m_equals_mu_gradPhi")}},
        "b": {"verdict": "correct, wording caveat",
              "statement": "slice {sum m = c}: Hessian ND at m(mu) <=> u^T S2 u < 2 u^T D u for all "
                           "u != 0 with <u,m> = 0",
              "basis": "in scaled coordinates S^ = D^{-1/2} S2 D^{-1/2} has eigenvector sqrt(m) "
                       "(eigenvalue 5, from S2 1 = 5 m), so sqrt(m)^perp is S^-invariant and the "
                       "compression of S^^{-1} equals the inverse of the compression; slice Hessian "
                       "eigenvalues (metric D^{-1}) are lambda_i = 1/2 - 1/r_i with r_i the "
                       "generalised eigenvalues of (S2|D) on m^perp",
              "caveat": "'strictly concave at m(mu) iff' should read 'slice Hessian negative definite "
                        "at m(mu) iff' (ND => local strict concavity, converse false in general); "
                        "the switch 1^perp -> m^perp relies on all spectra having entry sum 5"},
        "c": {"verdict": "correct",
              "statement": "condition (b) <=> Mpoly 1 = 0 and leading 3x3 block of Mpoly PD",
              "basis": "Mpoly 1 = 0 (exact); x^T Mpoly x = v^T Mpoly v for x = v + t1, v in m^perp; "
                       "{x_k = 0} complements span(1) for every k; v^T Mpoly v = 5 Phi v^T(2D-S2)v",
              "exact_support": {k: ids[k] for k in ("Mpoly_times_1_equals_0", "Mpoly_symmetric",
                                                    "Mpoly_entries_homogeneous_degree_10",
                                                    "identity_(*)_3P3_equals_minus25Phi^2_det(2D-S2)")}},
        "d": {"verdict": ("confirmed" if rs["leading_minors_all_coefficients_positive_all_k"]
                          else "REFUTED"),
              "statement": "leading principal minors (deg 10, 20, 30) of the 3x3 block, for all 4 "
                           "dropped indices, have only positive coefficients",
              "all_leading_minors_positive_all_k": rs["leading_minors_all_coefficients_positive_all_k"],
              "all_1x1_2x2_3x3_principal_minors_positive": rs["all_principal_minors_all_coefficients_positive"],
              "P3_same_polynomial_for_all_k": rs["P3_identical_polynomial_for_all_dropped_indices"],
              "scope": "strict concavity of psi on the interior of every slice M0(c) (open cone); "
                       "uses existence half of Lemma 5.3; no statement about the boundary of M0(c)",
              "margin": "no uniform margin: sup over the open cone of max u^T S2 u / u^T D u (u in "
                        "m^perp) is exactly 2, approached but not attained (see "
                        "rainbow.boundary_margin_addendum)"
              if block["boundary_margin_addendum"]["conclusion_sup_max_r_equals_2_not_attained"]
              else "boundary valuation test inconclusive for the chosen curve"},
    }

    timings["total"] = round(time.time() - t_start, 2)
    result["runtime_seconds"] = timings
    result["peak_rss_mib"] = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20, 1)
    result["flint_imported_at_end"] = "flint" in sys.modules
    result["date_end_host"] = host_date()
    print("end", result["date_end_host"], flush=True)

    text = json.dumps(result, indent=1, sort_keys=False, default=str)
    if args.out == "-":
        brief = {k: result[k] for k in ("derivation_verdict", "runtime_seconds", "peak_rss_mib",
                                        "posthoc_comparison_sibling_P3")}
        brief["centre"] = result["rainbow"]["centre_exact_mu_ones"]
        brief["boundary"] = result["rainbow"]["boundary_margin_addendum"]
        brief["exact_identities"] = result["rainbow"]["exact_identities"]
        brief["numeric"] = {k: {kk: vv for kk, vv in v.items() if not isinstance(vv, (dict, list))}
                            for k, v in result["numeric_crosscheck"].items()}
        print(json.dumps(brief, indent=1, default=str))
    else:
        with open(args.out, "w") as fh:
            fh.write(text + "\n")
        print("wrote", args.out, hashlib.sha256((text + "\n").encode()).hexdigest())


if __name__ == "__main__":
    main()
