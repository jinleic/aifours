"""Which multipliers M(mu, nu) = phi(mu) - phi(nu) work for P = D_t + D_x^3 (two amplitudes)?"""
import sys, random, itertools
sys.path.insert(0, "/Users/jinleic/jinleic-workspace/ai4s/phys-bilinear-higher-dim-integrability/code")
import hirota_ns as H
from fractions import Fraction as Fr

Dx, Dy, Dt = H.DX, H.DY, H.DT


def run(phi_kind, N=3, seed=1, pexp=3):
    rng = random.Random(seed)
    Pd = H.bpoly(Dt + Dx**pexp)
    waves, a, b = [], [], []
    for i in range(N):
        k = Fr(rng.randint(1, 25), rng.randint(1, 7)) * rng.choice((1, -1))
        waves.append((k, Fr(0), -k**pexp))
        a.append(Fr(rng.randint(1, 9), rng.randint(1, 5)))
        b.append(Fr(rng.randint(1, 9), rng.randint(1, 5)) * rng.choice((1, -1)))
    lam = [Fr(rng.randint(1, 30), rng.randint(1, 7)) for _ in range(N)]
    phi = {}
    for S in range(1 << N):
        idx = [i for i in range(N) if S >> i & 1]
        if phi_kind == "additive":
            phi[S] = sum((lam[i] for i in idx), Fr(0))
        elif phi_kind == "multiplicative":
            v = Fr(1)
            for i in idx:
                v *= lam[i]
            phi[S] = v
        elif phi_kind == "quadratic":
            phi[S] = sum((lam[i] for i in idx), Fr(0)) ** 2
        elif phi_kind == "random":
            phi[S] = Fr(rng.randint(-50, 50), rng.randint(1, 9))
        elif phi_kind == "affine-mult":  # phi = c1*additive + c2*multiplicative
            v = Fr(1)
            for i in idx:
                v *= lam[i]
            phi[S] = 3 * sum((lam[i] for i in idx), Fr(0)) + 2 * v
    kap = H._kappa_table(waves)

    def B1(A, C):
        return H.beval(Pd, H._vec_sub(kap[A], kap[C]))

    # coefficient sums run over mu = S2|A, nu = S2|C; phi must be evaluated on mu, nu (not A, C)
    # -> implement via a closure that receives A, C only: for additive phi, phi(mu)-phi(nu) = phi(A)-phi(C);
    # for general phi we need S2; emulate by full residual computation below instead.
    return waves, a, b, phi, B1, Pd


def full_test(phi_kind, N=3, seed=1, pexp=3):
    waves, a, b, phi, B1, Pd = run(phi_kind, N, seed, pexp)
    kap = H._kappa_table(waves)
    one = Fr(1)
    F = [None] * (1 << N); G = [None] * (1 << N)
    F[0] = G[0] = one
    for i in range(N):
        F[1 << i] = a[i]; G[1 << i] = b[i]
    for S in sorted(range(1, 1 << N), key=lambda m: bin(m).count("1")):
        if bin(S).count("1") < 2:
            continue
        r1 = r2 = Fr(0)
        for T in H._submasks(S):
            if T in (0, S):
                continue
            U = S ^ T
            pv = B1(T, U)
            r1 += F[T] * G[U] * pv
            r2 += F[T] * G[U] * pv * (phi[T] - phi[U])
        m11, m12 = B1(S, 0), B1(0, S)
        m21, m22 = m11 * (phi[S] - phi[0]), m12 * (phi[0] - phi[S])
        det = m11 * m22 - m12 * m21
        F[S] = (-r1 * m22 + r2 * m12) / det
        G[S] = (-r2 * m11 + r1 * m21) / det
    bad = 0
    for n in itertools.product((0, 1, 2), repeat=N):
        S2 = sum(1 << i for i, v in enumerate(n) if v == 2)
        S1 = sum(1 << i for i, v in enumerate(n) if v == 1)
        t1 = t2 = Fr(0)
        for A in H._submasks(S1):
            mu, nu = S2 | A, S2 | (S1 ^ A)
            pv = B1(A, S1 ^ A)
            t1 += F[mu] * G[nu] * pv
            t2 += F[mu] * G[nu] * pv * (phi[mu] - phi[nu])
        if t1 != 0 or t2 != 0:
            bad += 1
    return bad


for kind in ("additive", "multiplicative", "affine-mult", "quadratic", "random"):
    for pexp in (3, 5):
        print(kind, "p=k^%d" % pexp, [full_test(kind, 3, s, pexp) for s in (1, 2, 3)],
              "N=4:", [full_test(kind, 4, s, pexp) for s in (1, 2)])
