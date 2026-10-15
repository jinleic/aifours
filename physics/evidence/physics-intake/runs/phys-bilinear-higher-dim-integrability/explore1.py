import sys, random
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
from fractions import Fraction as Fr

Dx, Dy, Dt = H.DX, H.DY, H.DT


def rnd(rng, lo=-9, hi=9):
    while True:
        v = Fr(rng.randint(lo, hi), rng.randint(1, 7))
        if v != 0:
            return v


def waves_for(pc, N, rng, with_y=True):
    """Distinct positive k's and l's (avoids k_i + k_j = 0 and k_i = k_j)."""
    ws, ks, ls = [], set(), set()
    while len(ws) < N:
        k = abs(rnd(rng))
        l = abs(rnd(rng)) if with_y else Fr(0)
        if k in ks or (with_y and l in ls):
            continue
        ks.add(k)
        ls.add(l)
        w = H.dispersion_D_t_plus(pc, k)
        ws.append((k, l, w))
    return ws


def single_test(Bexpr, pc, N, seed=1, with_y=True):
    rng = random.Random(seed)
    B = H.bpoly(Bexpr)
    ws = waves_for(pc, N, rng, with_y)
    f, A = H.hirota_product_solution(B, ws)
    return H.residuals([B], ws, f, f)


def system_test(P, M, pc, N, seed=1, with_y=True, amp="free"):
    rng = random.Random(seed)
    Bp = H.bpoly(P)
    Bq = H.bpoly(M * P)
    ws = waves_for(pc, N, rng, with_y)
    a = [rnd(rng) for _ in range(N)]
    if amp == "free":
        b = [rnd(rng) for _ in range(N)]
    elif amp == "equal":
        b = list(a)
    elif amp == "neg":
        b = [-x for x in a]
    F, G = H.two_function_solution([Bp, Bq], ws, a, b)
    return H.residuals([Bp, Bq], ws, F, G)


if __name__ == "__main__":
    print("== single-function Hirota product ansatz ==")
    for name, Bexpr, pc, wy in [("KdV D_x(D_t+D_x^3)", Dx * (Dt + Dx**3), {3: 1}, False),
                                ("SK D_x(D_t+D_x^5)", Dx * (Dt + Dx**5), {5: 1}, False),
                                ("ANNV D_y(D_t+D_x^3)", Dy * (Dt + Dx**3), {3: 1}, True),
                                ("2DSK D_y(D_t+D_x^5)", Dy * (Dt + Dx**5), {5: 1}, True),
                                ("D_x(D_t+D_x^7)", Dx * (Dt + Dx**7), {7: 1}, False),
                                ("D_y(D_t+D_x^7)", Dy * (Dt + Dx**7), {7: 1}, True)]:
        for N in (3, 4):
            res = single_test(Bexpr, pc, N, seed=7, with_y=wy)
            print(f"{name:24s} N={N} nonzero coefficients: {len(res)}")
    print("== two-function systems P F.G = 0, M P F.G = 0 ==")
    for nexp in (3, 5):
        P = Dt + Dx**nexp
        pc = {nexp: 1}
        for label, M, wy in [("(1) M=D_x", Dx, False), ("(2) M=D_y", Dy, True)]:
            for amp in ("free", "equal", "neg"):
                for N in (2, 3):
                    res = system_test(P, M, pc, N, seed=11, with_y=wy, amp=amp)
                    print(f"n={nexp} {label} amp={amp:5s} N={N}: nonzero coefficients {len(res)}"
                          + (f" e.g. {sorted(res)[0]}" if res else ""))
