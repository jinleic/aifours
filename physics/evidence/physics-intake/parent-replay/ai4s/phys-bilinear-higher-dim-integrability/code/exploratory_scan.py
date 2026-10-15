"""Claim C8. Exploratory scan outside the proved class (Empirical evidence only; finite samples, fixed seeds).

Part 1  P(D_x, D_t) of several shapes (D_t^2, D_x^j D_t terms, even/odd/mixed parity) and multipliers
        Q in {D_x, D_x^3, D_x + D_x^3} with R = Q(D_y).  For each (P, Q) we run the generic three-soliton test
        of (1) and of (2) at 3 random points per soliton-type pattern, in 60-digit mpmath arithmetic (the
        dispersion relation is solved numerically, so this part is floating point).  Outcome labels:
        PASS (max relative residual < 1e-30), FAIL, degenerate (singular recursion).
Part 2  discrete extra dimension: R(S) = sinh(D_n), i.e. the multiplier sinh(nu_A - nu_C) on exp(nu n),
        for P = D_t + D_x^3 (two amplitudes) and P = D_t + D_x^2 (F/G patterns); exact rational arithmetic
        with z_i = exp(nu_i) rational.
Run: python exploratory_scan.py
"""
from __future__ import annotations

import itertools
import json
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hirota_ns as H  # noqa: E402

mp.mp.dps = 60
OUT = Path(__file__).resolve().parent.parent / "results"
Dx, Dy, Dt = H.DX, H.DY, H.DT
W = sp.Symbol("w")


def _mp(B):
    return {k: mp.mpf(v.numerator) / v.denominator for k, v in B.items()}


def _root(Pexpr, kq, rng, sign):
    poly = sp.Poly(sp.expand(Pexpr.subs({Dx: sign * kq, Dt: sign * W})), W)
    coeffs = [mp.mpf(sp.Rational(c).p) / sp.Rational(c).q for c in poly.all_coeffs()]
    if len(coeffs) <= 1:
        return None
    roots = mp.polyroots(coeffs, maxsteps=200, extraprec=200)
    real = [mp.re(r) for r in roots if abs(mp.im(r)) < mp.mpf(10) ** -40]
    return rng.choice(real if real else list(roots))


def float_test(Pexpr, Mexpr, seed, types):
    rng = random.Random(seed)
    Bs = [_mp(H.bpoly(Pexpr)), _mp(H.bpoly(sp.expand(Mexpr * Pexpr)))]
    with_y = Mexpr.has(Dy)
    waves, a, b = [], [], []
    for typ in types:
        kq = sp.Rational(rng.randint(1, 29), rng.randint(3, 11)) * rng.choice((1, -1))
        l = mp.mpf(rng.randint(1, 29)) / rng.randint(3, 11) * rng.choice((1, -1)) if with_y else mp.mpf(0)
        w = _root(Pexpr, kq, rng, -1 if typ == "G" else 1)
        if w is None:
            return "no-dispersion"
        waves.append((mp.mpf(kq.p) / kq.q, l, w))
        ai = mp.mpf(rng.randint(1, 19)) / rng.randint(1, 7) * rng.choice((1, -1))
        bi = mp.mpf(rng.randint(1, 19)) / rng.randint(1, 7) * rng.choice((1, -1))
        a.append(mp.mpf(0) if typ == "G" else ai)
        b.append(mp.mpf(0) if typ == "F" else bi)
    try:
        F, G = H.two_function_solution(Bs, waves, a, b)
    except Exception:  # singular recursion (exact zero det) or division by zero
        return "degenerate"
    kap = H._kappa_table(waves)
    worst, scale = mp.mpf(0), mp.mpf(0)
    for n in itertools.product((0, 1, 2), repeat=3):
        S2 = sum(1 << i for i, v in enumerate(n) if v == 2)
        S1 = sum(1 << i for i, v in enumerate(n) if v == 1)
        for B in Bs:
            babs = {m: abs(c) for m, c in B.items()}
            tot = mp.mpf(0)
            for A in H._submasks(S1):
                mu, nu = S2 | A, S2 | (S1 ^ A)
                v = H._vec_sub(kap[A], kap[S1 ^ A])
                tot += F[mu] * G[nu] * H.beval(B, v)
                scale = max(scale, abs(F[mu] * G[nu]) * H.beval(babs, tuple(abs(x) for x in v)))
            if 2 in n:
                worst = max(worst, abs(tot))
    rel = worst / scale if scale > 0 else mp.mpf(0)
    return "PASS" if rel < mp.mpf(10) ** -30 else "FAIL"


def part1():
    Ps = {
        "Dt^2-Dx^2-Dx^4": Dt**2 - Dx**2 - Dx**4, "Dt^2+Dx^4": Dt**2 + Dx**4, "Dt^2+DxDt+Dx^4": Dt**2 + Dx * Dt + Dx**4,
        "Dt^2+Dx^3": Dt**2 + Dx**3, "DxDt+Dx^4": Dx * Dt + Dx**4, "DxDt+Dx^6": Dx * Dt + Dx**6,
        "Dx^3Dt+Dx^2": Dx**3 * Dt + Dx**2, "Dt+DxDt+Dx^3": Dt + Dx * Dt + Dx**3,
        "Dt+Dx^2Dt+Dx^3": Dt + Dx**2 * Dt + Dx**3, "Dt+Dx^2Dt+Dx^5": Dt + Dx**2 * Dt + Dx**5,
        "Dt+Dt^3+Dx^3": Dt + Dt**3 + Dx**3, "Dt+Dx^3+Dt^2": Dt + Dx**3 + Dt**2,
        "Dt+Dx^3": Dt + Dx**3, "Dt+Dx^2": Dt + Dx**2, "Dt+Dx^5": Dt + Dx**5,
    }
    Ms = {"Dx|Dy": (Dx, Dy), "Dx^3|Dy^3": (Dx**3, Dy**3), "Dx+Dx^3|Dy+Dy^3": (Dx + Dx**3, Dy + Dy**3)}
    rows, mismatches = {}, []
    for pname, P in Ps.items():
        par = H.parity(H.bpoly(P))
        pats = [("FG",) * 3] if par in ("odd", "even") else list(itertools.product("FG", repeat=3))
        for mname, (M1, M2) in Ms.items():
            per = {}
            for pat in pats:
                r1 = sorted({float_test(P, M1, s, pat) for s in (1, 2, 3)})
                r2 = sorted({float_test(P, M2, s, pat) for s in (1, 2, 3)})
                per["".join(x[0] for x in pat)] = (r1, r2)
                if r1 == ["PASS"] and r2 != ["PASS"]:
                    mismatches.append((pname, mname, "".join(x[0] for x in pat), r1, r2))
            rows[f"{pname} | {mname}"] = {"parity": par, "patterns": per}
            summ1 = sorted({x for v in per.values() for x in v[0]})
            summ2 = sorted({x for v in per.values() for x in v[1]})
            print(f"{pname:18s} {mname:16s} {par:5s} (1): {summ1}  (2): {summ2}", flush=True)
    print("patterns where (1) passes but (2) does not:", mismatches if mismatches else "none")
    return rows, mismatches


def part2():
    """R(S) = sinh(D_n): multiplier sinh(nu_A - nu_C) = (Z_A/Z_C - Z_C/Z_A)/2 with Z_A = prod_{i in A} z_i."""
    out = {}
    for label, Pexpr, pc in (("Dt+Dx^3", Dt + Dx**3, {3: 1}), ("Dt+Dx^2", Dt + Dx**2, {2: 1})):
        Pd = H.bpoly(Pexpr)
        odd = all(j % 2 for j in pc)
        pats = [("FG",) * 3] if odd else list(itertools.product("FG", repeat=3))
        for pat in pats:
            res_counts = []
            for seed in (11, 12, 13):
                rng = random.Random(seed)
                waves, a, b, z = [], [], [], []
                for typ in pat:
                    k = Fr(rng.randint(1, 25), rng.randint(1, 7)) * rng.choice((1, -1))
                    pk = sum(Fr(c) * k**j for j, c in pc.items())
                    pmk = sum(Fr(c) * (-k) ** j for j, c in pc.items())
                    waves.append((k, Fr(0), -pk if typ in ("FG", "F") else pmk))
                    z.append(Fr(rng.randint(2, 30), rng.randint(1, 9)))
                    a.append(Fr(rng.randint(1, 9)) if typ in ("FG", "F") else Fr(0))
                    b.append(Fr(rng.randint(1, 9)) * rng.choice((1, -1)) if typ in ("FG", "G") else Fr(0))
                kap = H._kappa_table(waves)
                Z = [Fr(1)] * 8
                for S in range(1, 8):
                    Z[S] = Fr(1)
                    for i in range(3):
                        if S >> i & 1:
                            Z[S] *= z[i]

                def B1(A, C, kap=kap):
                    return H.beval(Pd, H._vec_sub(kap[A], kap[C]))

                def B2(A, C, kap=kap, Z=Z):
                    return B1(A, C) * (Z[A] / Z[C] - Z[C] / Z[A]) / 2

                F, G = H.two_function_solution([B1, B2], waves, a, b)
                res_counts.append(len(H.residuals([B1, B2], waves, F, G)))
            out[f"{label} pattern {'two-amplitude' if odd else ''.join(pat)}"] = res_counts
    print("Part 2 (R(S) = sinh(D_n)), nonzero residual counts per seed:", out)
    return out


def main():
    OUT.mkdir(exist_ok=True)
    rows, mism = part1()
    disc = part2()
    (OUT / "exploratory_scan.json").write_text(json.dumps(
        {"part1": rows, "part1_mismatches_1pass_2fail": mism, "part2_discrete_sinh": disc}, indent=2, default=str))
    print("wrote", OUT / "exploratory_scan.json")


if __name__ == "__main__":
    main()
