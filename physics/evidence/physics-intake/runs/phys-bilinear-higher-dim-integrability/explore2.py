"""Scan: two-function 3-soliton test for (1) P F.G = 0, D_x P F.G = 0 and (2) P F.G = 0, D_y P F.G = 0,
P = s(D_x) D_t + p(D_x).  Exact rational arithmetic at random points (exploratory)."""
import sys, random, itertools, json
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
from fractions import Fraction as Fr
import sympy as sp

Dx, Dy, Dt = H.DX, H.DY, H.DT
kk = sp.Symbol("k")


def rnd(rng, lo=1, hi=13):
    return Fr(rng.randint(lo, hi), rng.randint(1, 7))


def make_waves(Pexpr, N, rng, with_y, types):
    """types[i] in {'FG','F','G'}; returns waves, a, b."""
    s_expr = sp.expand(Pexpr).coeff(Dt, 1)
    p_expr = sp.expand(Pexpr - s_expr * Dt)
    assert sp.expand(Pexpr).coeff(Dt, 2) == 0
    s_f = sp.lambdify(Dx, s_expr, modules=[{"Rational": Fr}])
    ws, a, b, used_k, used_l = [], [], [], set(), set()
    while len(ws) < N:
        k = rnd(rng) * rng.choice((1, -1))
        l = rnd(rng) * rng.choice((1, -1)) if with_y else Fr(0)
        if abs(k) in used_k or (with_y and abs(l) in used_l):
            continue
        typ = types[len(ws)]
        # F-type / both: P(k,w)=0 -> w = -p(k)/s(k); G-type: P(-k,-w)=0 -> w = p(-k)/s(-k)
        sk = Fr(str(sp.Rational(s_expr.subs(Dx, sp.Rational(k.numerator, k.denominator)))))
        pk = Fr(str(sp.Rational(p_expr.subs(Dx, sp.Rational(k.numerator, k.denominator)))))
        smk = Fr(str(sp.Rational(s_expr.subs(Dx, -sp.Rational(k.numerator, k.denominator)))))
        pmk = Fr(str(sp.Rational(p_expr.subs(Dx, -sp.Rational(k.numerator, k.denominator)))))
        if typ in ("FG", "F"):
            if sk == 0:
                continue
            w = -pk / sk
        else:
            if smk == 0:
                continue
            w = pmk / smk
        used_k.add(abs(k)); used_l.add(abs(l))
        ws.append((k, l, w))
        ai = rnd(rng) * rng.choice((1, -1))
        bi = rnd(rng) * rng.choice((1, -1))
        if typ == "F":
            bi = Fr(0)
        if typ == "G":
            ai = Fr(0)
        a.append(ai); b.append(bi)
    return ws, a, b


def test_system(Pexpr, M, N, seed, types):
    rng = random.Random(seed)
    with_y = (M == Dy)
    Bp, Bq = H.bpoly(Pexpr), H.bpoly(sp.expand(M * Pexpr))
    for attempt in range(20):
        ws, a, b = make_waves(Pexpr, N, rng, with_y, types)
        # one-soliton consistency
        bad = False
        for i in range(N):
            kv, mk = ws[i], tuple(-c for c in ws[i])
            for B in (Bp, Bq):
                if H.beval(B, kv) * a[i] + H.beval(B, mk) * b[i] != 0:
                    bad = True
        if bad:
            return "one-soliton-inconsistent"
        try:
            F, G = H.two_function_solution([Bp, Bq], ws, a, b)
        except H.DegenerateSystem:
            continue
        res = H.residuals([Bp, Bq], ws, F, G)
        return "PASS" if not res else f"FAIL({len(res)})"
    return "DEGENERATE"


def parity_of(Pexpr):
    return H.parity(H.bpoly(Pexpr))


if __name__ == "__main__":
    cases = {
        "Dt+Dx^3": Dt + Dx**3,
        "Dt+Dx^3+Dx": Dt + Dx**3 + 2 * Dx,
        "Dt+Dx^5": Dt + Dx**5,
        "Dt+Dx^5+Dx^3": Dt + Dx**5 + Dx**3,
        "Dt+Dx^7": Dt + Dx**7,
        "Dt+Dx^2": Dt + Dx**2,
        "Dt+Dx^2+Dx^3": Dt + Dx**2 + Dx**3,
        "Dt+Dx^4": Dt + Dx**4,
        "Dt+Dx^3+Dx^4": Dt + Dx**3 + Dx**4,
        "DxDt+Dx^4": Dx * Dt + Dx**4,
        "DxDt+Dx^6": Dx * Dt + Dx**6,
        "DxDt+Dx^4+Dx^2": Dx * Dt + Dx**4 + Dx**2,
        "DxDt+Dx^3": Dx * Dt + Dx**3,
        "Dx^2Dt+Dx^5": Dx**2 * Dt + Dx**5,
        "Dx^3Dt+Dx^6": Dx**3 * Dt + Dx**6,
        "DxDt+Dx^2": Dx * Dt + Dx**2,
        "Dt+Dx": Dt + Dx,
    }
    out = {}
    for name, P in cases.items():
        par = parity_of(P)
        typesets = [("FG",) * 3] if par in ("odd", "even") else list(itertools.product(("F", "G"), repeat=3))
        row = {}
        for Mname, M in (("(1)Dx", Dx), ("(2)Dy", Dy)):
            results = []
            for types in typesets:
                for seed in (1, 2):
                    results.append((("".join(t[0] for t in types)), seed, test_system(P, M, 3, seed, types)))
            row[Mname] = results
        out[name] = (par, row)
        summ = {m: sorted(set(r[2] for r in v)) for m, v in row.items()}
        print(f"{name:18s} parity={par:5s} (1):{summ['(1)Dx']}  (2):{summ['(2)Dy']}")
        if par == "mixed":
            for m, v in row.items():
                fails = sorted(set(t for t, s, r in v if r != "PASS"))
                print(f"    {m} failing type patterns: {fails}")
