"""Broad float (mpmath, 60 digits) exploration of two-function 3SS for general P(D_x, D_t), multipliers M.
Exploratory only; candidates must be re-verified exactly."""
import sys, random, itertools
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
Dx, Dy, Dt = H.DX, H.DY, H.DT


def to_mp_poly(B):
    return {k: mp.mpf(v.numerator) / v.denominator for k, v in B.items()}


def solve_w(Pexpr, kq, branch_rng, sign=1):
    """Roots w of P(sign*k, sign*w) = 0 (F-type sign=1, G-type sign=-1); random real root if any."""
    w = sp.Symbol("w")
    poly = sp.Poly(sp.expand(Pexpr.subs({Dx: sign * kq, Dt: sign * w})), w)
    coeffs = [mp.mpf(sp.Rational(c).p) / sp.Rational(c).q for c in poly.all_coeffs()]
    if len(coeffs) <= 1:
        return None
    roots = mp.polyroots(coeffs, maxsteps=200, extraprec=200)
    real = [r for r in roots if abs(mp.im(r)) < mp.mpf(10) ** -40]
    pool = [mp.re(r) for r in real] if real else list(roots)
    return branch_rng.choice(pool)


def run(Pexpr, Mexpr, N=3, seed=1, types=None, amp="free"):
    rng = random.Random(seed)
    Bp = to_mp_poly(H.bpoly(Pexpr))
    Bq = to_mp_poly(H.bpoly(sp.expand(Mexpr * Pexpr)))
    with_y = Mexpr.has(Dy)
    if types is None:
        types = ["FG"] * N
    ws, a, b = [], [], []
    for i in range(N):
        kq = sp.Rational(rng.randint(1, 29), rng.randint(3, 11)) * rng.choice((1, -1))
        k = mp.mpf(kq.p) / kq.q
        l = (mp.mpf(rng.randint(1, 29)) / rng.randint(3, 11) * rng.choice((1, -1))) if with_y else mp.mpf(0)
        w = solve_w(Pexpr, kq, rng, sign=-1 if types[i] == "G" else 1)
        if w is None:
            return "no-dispersion"
        ws.append((k, l, w))
        ai = mp.mpf(rng.randint(1, 19)) / rng.randint(1, 7) * rng.choice((1, -1))
        bi = mp.mpf(rng.randint(1, 19)) / rng.randint(1, 7) * rng.choice((1, -1))
        if amp == "equal":
            bi = ai
        if types[i] == "F":
            bi = mp.mpf(0)
        if types[i] == "G":
            ai = mp.mpf(0)
        a.append(ai)
        b.append(bi)
    for i in range(N):
        kv, mk = ws[i], tuple(-c for c in ws[i])
        for B in (Bp, Bq):
            r = H.beval(B, kv) * a[i] + H.beval(B, mk) * b[i]
            babs = {m: abs(c) for m, c in B.items()}
            if abs(r) > mp.mpf(10) ** -35 * (1 + H.beval(babs, tuple(abs(x) for x in kv))) * (abs(a[i]) + abs(b[i])):
                return "one-soliton-inconsistent"
    try:
        F, G = H.two_function_solution([Bp, Bq], ws, a, b)
    except Exception:  # singular 2x2 recursion
        return "degenerate"
    kap = H._kappa_table(ws)
    tots, gscale = [], mp.mpf(0)
    for n in itertools.product((0, 1, 2), repeat=N):
        if 2 not in n:
            continue
        S2 = sum(1 << i for i, v in enumerate(n) if v == 2)
        S1 = sum(1 << i for i, v in enumerate(n) if v == 1)
        for B in (Bp, Bq):
            babs = {m: abs(c) for m, c in B.items()}
            tot = mp.mpf(0)
            for A in H._submasks(S1):
                mu, nu = S2 | A, S2 | (S1 ^ A)
                v = H._vec_sub(kap[A], kap[S1 ^ A])
                tot += F[mu] * G[nu] * H.beval(B, v)
                gscale = max(gscale, abs(F[mu] * G[nu]) * H.beval(babs, tuple(abs(x) for x in v)))
            tots.append(abs(tot))
    # relative to the largest single term anywhere (rounding noise in exactly-zero coefficients is harmless)
    worst = max(tots) / gscale if gscale > 0 else mp.mpf(0)
    return "PASS" if worst < mp.mpf(10) ** -30 else f"FAIL(rel={mp.nstr(worst, 3)})"


def classify(Pexpr, Mexpr, N=3, seeds=(1, 2, 3)):
    par = H.parity(H.bpoly(Pexpr))
    pats = [None] if par in ("odd", "even") else [list(t) for t in itertools.product("FG", repeat=N)]
    outs = set()
    for pat in pats:
        for s in seeds:
            outs.add(run(Pexpr, Mexpr, N, s, pat).split("(")[0])
    return par, sorted(outs)


if __name__ == "__main__":
    Ps = {
        "Dt^2-Dx^2-Dx^4 (Bq)": Dt**2 - Dx**2 - Dx**4,
        "Dt^2+Dx^4": Dt**2 + Dx**4,
        "Dt^2+DxDt+Dx^4": Dt**2 + Dx * Dt + Dx**4,
        "Dt^2+Dx^3": Dt**2 + Dx**3,
        "DxDt+Dx^4": Dx * Dt + Dx**4,
        "Dx^3Dt+Dt^2": Dx**3 * Dt + Dt**2,
        "Dx^3Dt+Dx^2": Dx**3 * Dt + Dx**2,
        "Dx^3Dt+DxDt": Dx**3 * Dt + Dx * Dt,
        "Dt+Dx^3": Dt + Dx**3,
        "Dt+Dx^5": Dt + Dx**5,
        "Dt+DxDt+Dx^3": Dt + Dx * Dt + Dx**3,
        "Dt+Dx^2Dt+Dx^3": Dt + Dx**2 * Dt + Dx**3,
        "Dt+Dx^2Dt+Dx^5": Dt + Dx**2 * Dt + Dx**5,
        "Dt+Dt^3+Dx^3": Dt + Dt**3 + Dx**3,
        "Dt+Dx^2Dt": Dt + Dx**2 * Dt,
        "Dt+Dx^2": Dt + Dx**2,
        "Dt+Dx^3+Dt^2": Dt + Dx**3 + Dt**2,
        "Dt^3+Dx^3": Dt**3 + Dx**3,
        "Dx^2Dt+Dx^3": Dx**2 * Dt + Dx**3,
    }
    Ms = {"Dx|Dy": (Dx, Dy), "Dx^3|Dy^3": (Dx**3, Dy**3), "Dx+Dx^3|Dy+Dy^3": (Dx + Dx**3, Dy + Dy**3)}
    for pname, P in Ps.items():
        for mname, (M1, M2) in Ms.items():
            par, o1 = classify(P, M1)
            _, o2 = classify(P, M2)
            print(f"{pname:22s} {mname:16s} parity={par:5s} (1):{o1}  (2):{o2}", flush=True)
