"""Conjectured Pfaffian closed form for the two-amplitude N-soliton of (2), P = D_t + D_x^3:
  F_S = R_S(k) b_S Pf(M^S),  G_S = R_S(k) b_S Pf(N^S),  x_i = a_i/b_i,
  M_ij = (x_i l_i - x_j l_j)/(l_i + l_j),  M_i0 = x_i;   N_ij = (x_j l_i - x_i l_j)/(l_i + l_j),  N_i0 = 1;
  Pfaffian over S (|S| even) or S + {0} (|S| odd)."""
import sys, random, itertools, time
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
from fractions import Fraction as Fr

Dx, Dy, Dt = H.DX, H.DY, H.DT


def pf(idx, A):
    """Pfaffian of antisymmetric A restricted to the ordered index list idx (len even)."""
    if not idx:
        return Fr(1)
    i0, rest = idx[0], idx[1:]
    s = Fr(0)
    for pos, j in enumerate(rest):
        sub = rest[:pos] + rest[pos + 1:]
        s += (-1) ** pos * A(i0, j) * pf(sub, A)
    return s


def check(N, seed, mult="Dy"):
    rng = random.Random(seed)
    ks, ls, a, b = [], [], [], []
    while len(ks) < N:
        k = Fr(rng.randint(1, 40), rng.randint(1, 9)) * rng.choice((1, -1))
        l = Fr(rng.randint(1, 40), rng.randint(1, 9)) * rng.choice((1, -1))
        if any(abs(k) == abs(q) for q in ks) or any(abs(l) == abs(q) for q in ls):
            continue
        ks.append(k); ls.append(l)
        a.append(Fr(rng.randint(1, 30), rng.randint(1, 9)) * rng.choice((1, -1)))
        b.append(Fr(rng.randint(1, 30), rng.randint(1, 9)) * rng.choice((1, -1)))
    if mult == "Dx":
        ls = list(ks)
    P = Dt + 2 * Dx**3 - 5 * Dx  # c1 = -5, c3 = 2
    Bs = [H.bpoly(P), H.bpoly((Dy if mult == "Dy" else Dx) * P)]
    waves = [(k, (l if mult == "Dy" else Fr(0)), -(2 * k**3 - 5 * k)) for k, l in zip(ks, ls)]
    F, G = H.two_function_solution(Bs, waves, a, b)
    x = [ai / bi for ai, bi in zip(a, b)]

    def M(i, j):
        if j == -1:
            return x[i]
        if i == -1:
            return -x[j]
        return (x[i] * ls[i] - x[j] * ls[j]) / (ls[i] + ls[j])

    def Nm(i, j):
        if j == -1:
            return Fr(1)
        if i == -1:
            return Fr(-1)
        return (x[j] * ls[i] - x[i] * ls[j]) / (ls[i] + ls[j])

    ok = True
    for S in range(1 << N):
        idx = [i for i in range(N) if S >> i & 1]
        R = Fr(1)
        for i, j in itertools.combinations(idx, 2):
            R *= (ks[i] - ks[j]) / (ks[i] + ks[j])
        bS = Fr(1)
        for i in idx:
            bS *= b[i]
        order = idx + ([-1] if len(idx) % 2 else [])
        Fc = R * bS * pf(order, M)
        Gc = R * bS * pf(order, Nm)
        if Fc != F[S] or Gc != G[S]:
            ok = False
    res = H.residuals(Bs, waves, F, G)
    return ok, len(res)

def safe(N, seed, mult="Dy"):
    for s in range(seed, seed + 50):
        try:
            return check(N, s, mult)
        except H.DegenerateSystem:
            continue


for N in (3, 4, 5, 6, 7):
    t0 = time.time()
    print(N, [safe(N, s) for s in (1, 100)], [safe(N, s, "Dx") for s in (200,)], f"{time.time()-t0:.1f}s",
          flush=True)
