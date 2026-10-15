"""Beyond three solitons for the passing class deg p <= 3 (claim C6).

  exact    : N = 4, 5 at fixed-seed random rational points for several cubic/quadratic P, (1) and (2),
             two-amplitude (odd p) or random F/G type patterns (mixed p).  Exact rational arithmetic, but a
             finite set of points: Empirical evidence, not a proof.
  pfaffian : conjectured closed form for odd cubic p = c1 k + c3 k^3, two amplitudes, x_i = a_i/b_i:
               F_S = R_S(k) b_S Pf(M on S'),  G_S = R_S(k) b_S Pf(N on S'),  R_S(k) = prod_{i<j in S} (k_i-k_j)/(k_i+k_j),
               M_ij = (x_i l_i - x_j l_j)/(l_i + l_j), M_i0 = x_i;  N_ij = (x_j l_i - x_i l_j)/(l_i + l_j), N_i0 = 1,
             S' = S (|S| even) or S + {0} (|S| odd); system (1) uses l_i = k_i.  Compared with the recursion
             and with the residuals for N = 3..7 at fixed-seed rational points (Empirical evidence).
  symbolic : (--symbolic N) every residual coefficient of the closed form for system (2), P = D_t + D_x^3,
             computed in the field Q(k_i, l_i, x_i) with b_i = 1 (no loss: the equations are homogeneous in each
             soliton's amplitude pair).  All zero = the closed form is an exact N-soliton solution.
Run: python n_soliton_checks.py [--symbolic N]
"""
from __future__ import annotations

import json
import random
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

from sympy import QQ
from sympy.polys.fields import field

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hirota_ns as H  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "results"
Dx, Dy, Dt = H.DX, H.DY, H.DT


def _pf(idx, A, one):
    """Pfaffian of the antisymmetric function A restricted to the ordered index list idx (even length)."""
    if not idx:
        return one
    i0, rest = idx[0], idx[1:]
    total = one * 0
    for pos, j in enumerate(rest):
        total += (-1) ** pos * A(i0, j) * _pf(rest[:pos] + rest[pos + 1:], A, one)
    return total


def closed_form(ks, ls, x, b, one):
    """Conjectured two-amplitude coefficients (F_S, G_S) for odd cubic p; index 0 of the formula is -1, placed last."""
    N = len(ks)

    def M(i, j):
        if j == -1:
            return x[i]
        return (x[i] * ls[i] - x[j] * ls[j]) / (ls[i] + ls[j])

    def Nm(i, j):
        if j == -1:
            return one
        return (x[j] * ls[i] - x[i] * ls[j]) / (ls[i] + ls[j])

    F, G = [None] * (1 << N), [None] * (1 << N)
    for S in range(1 << N):
        idx = [i for i in range(N) if S >> i & 1]
        R, bS = one, one
        for p_, i in enumerate(idx):
            bS = bS * b[i]
            for j in idx[p_ + 1:]:
                R = R * (ks[i] - ks[j]) / (ks[i] + ks[j])
        order = idx + ([-1] if len(idx) % 2 else [])
        F[S] = R * bS * _pf(order, M, one)
        G[S] = R * bS * _pf(order, Nm, one)
    return F, G


def symbolic_closed_form(N):
    """Number of nonzero residual coefficients of the closed form for (2), P = D_t + D_x^3, in Q(k, l, x)."""
    names = []
    for i in range(1, N + 1):
        names += [f"k{i}", f"l{i}", f"x{i}"]
    K, *gens = field(",".join(names), QQ)
    g = dict(zip(names, gens))
    ks = [g[f"k{i}"] for i in range(1, N + 1)]
    ls = [g[f"l{i}"] for i in range(1, N + 1)]
    x = [g[f"x{i}"] for i in range(1, N + 1)]
    F, G = closed_form(ks, ls, x, [K.one] * N, K.one)
    P = {(0, 0, 1): K.one, (3, 0, 0): K.one}
    Bs = [P, H.bmul({(0, 1, 0): K.one}, P)]
    waves = [(k, l, -k**3) for k, l in zip(ks, ls)]
    return len(H.residuals(Bs, waves, F, G))


def exact_random(Pexpr, pc, mult, N, seed):
    rng = random.Random(seed)
    Bs = [H.bpoly(Pexpr), H.bpoly(mult * Pexpr)]
    odd = all(j % 2 == 1 for j in pc)
    ks, ls = set(), set()
    waves, a, b = [], [], []
    while len(waves) < N:
        k = Fr(rng.randint(1, 40), rng.randint(1, 9)) * rng.choice((1, -1))
        l = Fr(rng.randint(1, 40), rng.randint(1, 9)) * rng.choice((1, -1)) if mult == Dy else Fr(0)
        if abs(k) in ks or (mult == Dy and abs(l) in ls):
            continue
        ks.add(abs(k))
        ls.add(abs(l))
        typ = "FG" if odd else rng.choice("FG")
        pk = sum(Fr(c) * k**j for j, c in pc.items())
        pmk = sum(Fr(c) * (-k) ** j for j, c in pc.items())
        waves.append((k, l, -pk if typ in ("FG", "F") else pmk))
        a.append(Fr(rng.randint(1, 30), rng.randint(1, 9)) if typ in ("FG", "F") else Fr(0))
        b.append(Fr(rng.randint(1, 30), rng.randint(1, 9)) * rng.choice((1, -1)) if typ in ("FG", "G") else Fr(0))
    F, G = H.two_function_solution(Bs, waves, a, b)
    return len(H.residuals(Bs, waves, F, G))


def single_random(Bexpr, pc, with_y, N, seed):
    rng = random.Random(seed)
    B = H.bpoly(Bexpr)
    waves, ks, ls = [], set(), set()
    while len(waves) < N:
        k = Fr(rng.randint(1, 40), rng.randint(1, 9))
        l = Fr(rng.randint(1, 40), rng.randint(1, 9)) if with_y else Fr(0)
        if k in ks or (with_y and l in ls):
            continue
        ks.add(k)
        ls.add(l)
        waves.append((k, l, -sum(Fr(c) * k**j for j, c in pc.items())))
    f, _ = H.hirota_product_solution(B, waves)
    return len(H.residuals([B], waves, f, f))


def pfaffian_closed_form(N, seed, mult):
    """Return (closed form == recursion for all S, number of nonzero residual coefficients); None if degenerate."""
    rng = random.Random(seed)
    ks, ls, a, b = [], [], [], []
    while len(ks) < N:
        k = Fr(rng.randint(1, 40), rng.randint(1, 9)) * rng.choice((1, -1))
        l = Fr(rng.randint(1, 40), rng.randint(1, 9)) * rng.choice((1, -1))
        if any(abs(k) == abs(q) for q in ks) or any(abs(l) == abs(q) for q in ls):
            continue
        ks.append(k)
        ls.append(l)
        a.append(Fr(rng.randint(1, 30), rng.randint(1, 9)) * rng.choice((1, -1)))
        b.append(Fr(rng.randint(1, 30), rng.randint(1, 9)) * rng.choice((1, -1)))
    if mult == "Dx":
        ls = list(ks)
    P = Dt + 2 * Dx**3 - 5 * Dx
    Bs = [H.bpoly(P), H.bpoly((Dy if mult == "Dy" else Dx) * P)]
    waves = [(k, (l if mult == "Dy" else Fr(0)), -(2 * k**3 - 5 * k)) for k, l in zip(ks, ls)]
    try:
        F, G = H.two_function_solution(Bs, waves, a, b)
    except H.DegenerateSystem:
        return None
    Fc, Gc = closed_form(ks, ls, [ai / bi for ai, bi in zip(a, b)], b, Fr(1))
    return (Fc == F and Gc == G), len(H.residuals(Bs, waves, F, G))


def main():
    OUT.mkdir(exist_ok=True)
    report = {}
    if "--symbolic" in sys.argv:
        Nsym = int(sys.argv[sys.argv.index("--symbolic") + 1])
        t0 = time.time()
        n = symbolic_closed_form(Nsym)
        print(f"symbolic closed form N={Nsym}, (2), P=D_t+D_x^3: nonzero residual coefficients = {n}"
              f"  [{time.time() - t0:.0f}s]")
        (OUT / f"n_soliton_symbolic_closed_form_N{Nsym}.json").write_text(json.dumps(
            {"N": Nsym, "system": "(2), P = D_t + D_x^3, two amplitudes, b_i = 1",
             "nonzero_residual_coefficients": n, "seconds": round(time.time() - t0)}, indent=2))
        return
    rows = {}
    for label, Pexpr, pc in (("Dt+Dx^3", Dt + Dx**3, {3: 1}),
                             ("Dt+2Dx^3-3Dx", Dt + 2 * Dx**3 - 3 * Dx, {3: 2, 1: -3}),
                             ("Dt+Dx^2", Dt + Dx**2, {2: 1}),
                             ("Dt+Dx^3+Dx^2-Dx", Dt + Dx**3 + Dx**2 - Dx, {3: 1, 2: 1, 1: -1})):
        for mname, mult in (("(1)", Dx), ("(2)", Dy)):
            for N in (4, 5):
                outs = [exact_random(Pexpr, pc, mult, N, seed) for seed in (101, 202, 303)]
                rows[f"{label} {mname} N={N}"] = outs
    print("exact random points (nonzero residual counts per seed):", rows)
    report["exact_random_two_function"] = rows
    single = {}
    for label, Bexpr, pc, wy in (("ANNV Dy(Dt+Dx^3)", Dy * (Dt + Dx**3), {3: 1}, True),
                                 ("SK Dx(Dt+Dx^5)", Dx * (Dt + Dx**5), {5: 1}, False),
                                 ("2DSK Dy(Dt+Dx^5)", Dy * (Dt + Dx**5), {5: 1}, True)):
        for N in (4, 5):
            single[f"{label} N={N}"] = [single_random(Bexpr, pc, wy, N, s) for s in (101, 202, 303)]
    print("single-function controls (nonzero residual counts per seed):", single)
    report["single_function_controls"] = single
    pf_rows = {}
    for mult in ("Dy", "Dx"):
        for N in range(3, 8):
            outs, seed = [], 1000 * N
            while len(outs) < 2:
                r = pfaffian_closed_form(N, seed, mult)
                seed += 1
                if r is not None:
                    outs.append(r)
            pf_rows[f"{'(2)' if mult == 'Dy' else '(1)'} N={N}"] = outs
    print("Pfaffian closed form, p = 2k^3 - 5k: (closed form == recursion, nonzero residuals):", pf_rows)
    report["pfaffian_closed_form"] = {k: [list(v) for v in vs] for k, vs in pf_rows.items()}
    (OUT / "n_soliton_checks.json").write_text(json.dumps(report, indent=2))
    print("wrote", OUT / "n_soliton_checks.json")


if __name__ == "__main__":
    main()
