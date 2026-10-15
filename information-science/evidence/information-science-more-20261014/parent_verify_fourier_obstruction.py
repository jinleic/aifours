#!/usr/bin/env python3
"""Parent's independent reproduction of Theorem 10 in ai4s/positive-tfd-marginals.

Independent of the worker's FLINT/Arb checker: exact Fractions for the corner
check, the certificate constants and Sturm counts; mpmath at 60 digits for the
Gaussian integrals (closed-form moment recursion, cross-checked by quadrature).
The mpmath evaluations are high-precision reproductions, not interval
certificates. Standard library plus mpmath only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60


# ---------- exact polynomial arithmetic (coefficient index = degree) ----------
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def pscale(a, c):
    return trim([c * x for x in a])


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pderiv(a):
    return trim([i * a[i] for i in range(1, len(a))] or [F(0)])


def peval(a, x):
    value = 0
    for c in reversed(a):
        value = value * x + c
    return value


def prem(a, b):
    a = trim(a)
    while len(a) >= len(b) and any(a):
        factor = a[-1] / b[-1]
        shift = len(a) - len(b)
        a = trim([a[i] - (factor * b[i - shift] if i >= shift else 0) for i in range(len(a))])
        if len(a) < len(b) or (len(a) == 1 and a[0] == 0):
            break
    return a


def real_root_count(poly):
    """Number of distinct real roots by an exact Sturm sequence."""
    seq = [trim(poly), pderiv(poly)]
    while len(seq[-1]) > 1 or seq[-1][0] != 0:
        r = prem(seq[-2], seq[-1])
        if len(r) == 1 and r[0] == 0:
            break
        seq.append(pscale(r, F(-1)))
    def variations(signs):
        signs = [s for s in signs if s != 0]
        return sum(1 for x, y in zip(signs, signs[1:]) if x != y)
    plus = [(1 if p[-1] > 0 else -1) for p in seq]
    minus = [(1 if p[-1] > 0 else -1) * (-1) ** (len(p) - 1) for p in seq]
    return variations(minus) - variations(plus)


P = [F(3), F(0), F(-12), F(0), F(4)]          # p = 4t^4 - 12t^2 + 3
DP = pderiv(P)                                 # p' = 16t^3 - 24t
BASE = padd([F(196)], pmul(P, P))              # 196 + p^2
FLUX = pscale(DP, F(14))                       # 14 p'


# ---------- Gaussian moment integrals in mpmath ----------
def moments(alpha, beta, mmax):
    """I[m] = int_alpha^beta t^m exp(-t^2) dt (alpha, beta may be +-inf)."""
    def edge(x, n):
        if mp.isinf(x):
            return mp.mpf(0)
        return (x ** n) * mp.e ** (-x * x)
    def erf(x):
        if x == mp.inf:
            return mp.mpf(1)
        if x == -mp.inf:
            return mp.mpf(-1)
        return mp.erf(x)
    out = [mp.sqrt(mp.pi) / 2 * (erf(beta) - erf(alpha)), (edge(alpha, 0) - edge(beta, 0)) / 2]
    for m in range(2, mmax + 1):
        out.append((edge(alpha, m - 1) - edge(beta, m - 1)) / 2 + (m - 1) * out[m - 2] / 2)
    return out


def poly_gauss(poly, alpha, beta):
    I = moments(alpha, beta, len(poly) - 1)
    return mp.fsum(mp.mpf(c.numerator) / c.denominator * I[m] for m, c in enumerate(poly))


NORM = 220 * mp.sqrt(mp.pi)


def mu(alpha, beta):
    return poly_gauss(BASE, alpha, beta) / NORM


def flux(alpha, beta):
    return poly_gauss(FLUX, alpha, beta) / NORM


def mpf(x):
    return mp.mpf(x.numerator) / x.denominator


# ---------- convex-order call functions ----------
def call_T(k):
    """E(|T|-k)_+ for k >= 0."""
    k = mp.mpf(k)
    tb = poly_gauss(pmul([F(0), F(1)], BASE), k, mp.inf)
    b = poly_gauss(BASE, k, mp.inf)
    return 2 * (tb - k * b) / NORM


def positive_pieces(poly_mp_coeffs, lo, hi):
    """Real roots of an mpmath polynomial inside (lo, hi), sorted."""
    coeffs = list(poly_mp_coeffs)
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    coeffs = list(reversed(coeffs))           # mp.polyroots wants highest degree first
    roots = mp.polyroots(coeffs, maxsteps=400, extraprec=400)
    real = sorted(mp.re(r) for r in roots if abs(mp.im(r)) < mp.mpf(10) ** -40 and lo < mp.re(r) < hi)
    return [lo] + real + [hi]


def call_f(k):
    """E(|f(T)|-k)_+ = 2/NORM * int_0^inf (14|p'| - k(196+p^2))_+ e^{-t^2} dt.

    Returns the value and its breakpoints; the quadrature cross-check integrates
    the same kinked integrand by an unrelated numerical method."""
    k = mp.mpf(k)
    total = mp.mpf(0)
    breaks = []
    knot = mp.sqrt(mp.mpf(3) / 2)                # p' < 0 on (0, knot), > 0 after
    for sign, lo, hi in ((-1, mp.mpf(0), knot), (1, knot, mp.inf)):
        coeffs = [sign * mpf(c) for c in FLUX]
        coeffs += [mp.mpf(0)] * (len(BASE) - len(coeffs))
        coeffs = [c - k * mpf(b) for c, b in zip(coeffs, BASE)]
        points = positive_pieces(coeffs, lo, hi if hi != mp.inf else mp.mpf(50))
        if hi == mp.inf:
            points[-1] = mp.inf
        breaks.extend(points)
        for left, right in zip(points, points[1:]):
            middle = (left + right) / 2 if right != mp.inf else left + 1
            if mp.polyval(list(reversed(coeffs)), middle) > 0:
                I = moments(left, right, len(coeffs) - 1)
                total += mp.fsum(c * I[m] for m, c in enumerate(coeffs))
    return 2 * total / NORM, sorted(set(breaks))


def call_f_quad(k, breaks):
    k = mp.mpf(k)
    def integrand(t):
        q = 14 * abs(peval([mpf(c) for c in DP], t)) - k * peval([mpf(c) for c in BASE], t)
        return max(q, 0) * mp.e ** (-t * t)
    finite = sorted(set([b for b in breaks if b != mp.inf] + [mp.mpf(6)]))
    return 2 * mp.quad(integrand, finite + [mp.inf]) / NORM


# ---------- certificate ----------
def load_certificate(path):
    data = json.loads(Path(path).read_text())["results"][0]
    edges = [F(x) for x in data["edges"]]
    a, b, h, k = ([F(x) for x in data[name]] for name in ("a", "b", "h", "k"))
    return edges, a, b, h, k


def corner_min(edges, a, b, h, k):
    worst = None
    for i in range(len(a)):
        for j in range(len(b)):
            for t in (edges[i], edges[i + 1]):
                for w in (edges[j], edges[j + 1]):
                    value = a[i] + b[j] + h[i] * w + k[j] * t
                    worst = value if worst is None or value < worst else worst
    return worst


def lambda_signal(edges, a, b, h, k, Am, Bm, H, K):
    total = mp.mpf(0)
    for i in range(len(a)):
        lo, hi = mpf(edges[i]), mpf(edges[i + 1])
        total += mpf(a[i] + b[i]) * mu(lo, hi) + mpf(h[i] - k[i]) * flux(lo, hi)
    L = mpf(edges[-1])
    tail_mass = 2 * mu(L, mp.inf)
    tail_abs = 2 * poly_gauss(pmul([F(0), F(1)], BASE), L, mp.inf) / NORM
    return total + mpf(Am + Bm) * tail_mass + mpf(H + K) * tail_abs


def lambda_chirp(edges, a, b, h, k, Am, Bm, H, K, beta):
    """Weak-duality control: the nonnegative Wigner Gaussian is a true coupling."""
    beta = mp.mpf(beta)
    sig_t = mp.sqrt(mp.mpf(1) / 2)
    sig_w = mp.sqrt((1 + beta * beta) / 2)
    gd = beta / (1 + beta * beta)
    def mass(sig, lo, hi):
        s = sig * mp.sqrt(2)
        return moments(lo / s, hi / s, 0)[0] / mp.sqrt(mp.pi)
    def first(sig, lo, hi):
        s = sig * mp.sqrt(2)
        return s * moments(lo / s, hi / s, 1)[1] / mp.sqrt(mp.pi)
    total = mp.mpf(0)
    for i in range(len(a)):
        lo, hi = mpf(edges[i]), mpf(edges[i + 1])
        total += mpf(a[i]) * mass(sig_t, lo, hi) + mpf(h[i]) * beta * first(sig_t, lo, hi)
        total += mpf(b[i]) * mass(sig_w, lo, hi) + mpf(k[i]) * gd * first(sig_w, lo, hi)
    L = mpf(edges[-1])
    total += mpf(Bm) * 2 * mass(sig_t, L, mp.inf) + mpf(K) * 2 * first(sig_t, L, mp.inf)
    total += mpf(Am) * 2 * mass(sig_w, L, mp.inf) + mpf(H) * 2 * first(sig_w, L, mp.inf)
    return total


def signal(t):
    p = peval([mpf(c) for c in P], t)
    return mp.pi ** mp.mpf(-0.25) * mp.e ** (-t * t / 2) * (1 + 1j * p / 14)


def fourier(fun, omega):
    real = mp.quad(lambda t: mp.re(fun(t) * mp.e ** (-1j * omega * t)), [-mp.inf, -4, 0, 4, mp.inf])
    imag = mp.quad(lambda t: mp.im(fun(t) * mp.e ** (-1j * omega * t)), [-mp.inf, -4, 0, 4, mp.inf])
    return (real + 1j * imag) / mp.sqrt(2 * mp.pi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = {"scope": "Independent parent reproduction; exact corner/Sturm/identity checks, 60-digit mpmath integrals (not interval-certified)"}

    # Exact identities.
    he2, he4 = [F(-1), F(0), F(1)], [F(3), F(0), F(-6), F(0), F(1)]
    assert padd(padd(pscale(he4, F(4)), pscale(he2, F(12))), [F(3)]) == P
    gauss_moment = lambda m: F(0) if m % 2 else F(1) * __import__("math").prod(range(1, m, 2)) / 2 ** (m // 2)
    energy_ratio = sum(c * gauss_moment(m) for m, c in enumerate(BASE)) / 196
    assert energy_ratio == F(220, 196)     # E = 55/49
    cov = sum(c * gauss_moment(m) for m, c in enumerate(pmul([F(0), F(1)], DP)))
    assert cov == 0
    f95 = F(14) * peval(DP, F(9, 5)) / peval(BASE, F(9, 5))
    assert f95 == F(9450000, 3143009) and f95 > 3
    cap = F(301, 100)
    sup_roots = [real_root_count(padd(pscale(BASE, cap), pscale(FLUX, F(s)))) for s in (-1, 1)]
    assert sup_roots == [0, 0]
    cap_three_roots = [real_root_count(padd(pscale(BASE, F(3)), pscale(FLUX, F(s)))) for s in (-1, 1)]
    assert sum(cap_three_roots) > 0
    out["exact"] = {"energy": "55/49", "covariance_moment": "0", "f(9/5)": str(f95),
                    "sturm_roots_cap_301/100": sup_roots, "sturm_roots_cap_3_control": cap_three_roots}

    # Fourier self-duality, numerically, plus a non-invariant control.
    errors = []
    for omega in (mp.mpf(0), mp.mpf("0.7"), mp.mpf("1.9"), mp.mpf("-2.3")):
        errors.append(float(abs(fourier(signal, omega) - signal(omega))))
    control = lambda t: t * t * mp.e ** (-t * t / 2)
    control_error = float(abs(fourier(control, mp.mpf("1.3")) - control(mp.mpf("1.3"))))
    assert max(errors) < 1e-30 and control_error > 1e-2
    out["fourier_self_dual_max_error"] = max(errors)
    out["fourier_non_invariant_control_error"] = control_error

    # Convex order: certified-style bracketing on k_j = j/100.
    margins = []
    for j in range(301):
        kj, kn = mp.mpf(j) / 100, mp.mpf(j + 1) / 100
        margins.append(call_T(kn) - call_f(kj)[0])
    worst = min(range(301), key=lambda j: margins[j])
    quad_gaps = []
    for j in (0, 50, 150, 299, 300):
        kk = mp.mpf(j) / 100
        value, breaks = call_f(kk)
        quad_gaps.append(abs(value - call_f_quad(kk, breaks)))
    assert max(quad_gaps) < mp.mpf(10) ** -20
    assert min(margins) > 0
    out["convex_order"] = {"intervals": 301, "min_margin": mp.nstr(margins[worst], 15),
                           "min_interval": [worst / 100, (worst + 1) / 100],
                           "quadrature_crosscheck_max_gap": mp.nstr(max(quad_gaps), 5),
                           "E|f(T)|": mp.nstr(call_f(0)[0], 20),
                           "closed_form_E|f(T)|": mp.nstr(7 * (16 * mp.e ** mp.mpf(-1.5) + 4) / (55 * mp.sqrt(mp.pi)), 20)}
    assert abs(call_f(0)[0] - 7 * (16 * mp.e ** mp.mpf(-1.5) + 4) / (55 * mp.sqrt(mp.pi))) < mp.mpf(10) ** -40

    # Dual certificate.
    edges, a, b, h, k = load_certificate(args.certificate)
    Am = max(F(0), max(-x for x in a))
    Bm = max(F(0), max(-x for x in b))
    H = max(abs(x) for x in h)
    K = max(abs(x) for x in k)
    assert (Am, Bm, H, K) == (F(0), F(84071, 250000), F(34463, 62500), F(524791, 1000000))
    cmin = corner_min(edges, a, b, h, k)
    assert cmin >= 0
    lam = lambda_signal(edges, a, b, h, k, Am, Bm, H, K)
    assert lam < 0
    chirps = {}
    for beta in ("0", "1", "-41/25", "3"):
        value = lambda_chirp(edges, a, b, h, k, Am, Bm, H, K, mpf(F(beta)))
        assert value > 0
        chirps[beta] = mp.nstr(value, 12)
    mutated = {
        "negated_h_k": corner_min(edges, a, b, [-x for x in h], [-x for x in k]),
        "a_lowered_1/50": corner_min(edges, [x - F(1, 50) for x in a], b, h, k),
    }
    assert all(v < 0 for v in mutated.values())
    out["dual_certificate"] = {"corner_min": str(cmin), "A-": str(Am), "B-": str(Bm), "H": str(H), "K": str(K),
                               "Lambda": mp.nstr(lam, 30), "chirp_controls_positive": chirps,
                               "mutation_corner_mins": {kk: str(v) for kk, v in mutated.items()}}
    out["certificate_sha256"] = hashlib.sha256(args.certificate.read_bytes()).hexdigest()
    out["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out["status"] = "PASS"
    args.output.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "corner_min": str(cmin), "Lambda": mp.nstr(lam, 20),
                      "convex_min_margin": out["convex_order"]["min_margin"],
                      "convex_min_interval": out["convex_order"]["min_interval"]}))


if __name__ == "__main__":
    main()
