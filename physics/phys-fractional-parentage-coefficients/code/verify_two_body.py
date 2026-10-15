"""Two-body CFPs from one-body CFPs: exact check of the standard chain (recoupling) formula

  C2(N Gamma L; pair s, N-2 Gamma'' L'') = sum_{Gamma' L'} c(N Gamma L; N-1 Gamma' L') c(N-1 Gamma' L'; N-2 Gamma'' L'')
        * (-1)^(L+L'') sqrt((2s+1)(2L'+1)) {f f s; L'' L L'}          (s even; 0 for s odd)

where C2 is defined by  |N; Gamma L M> = sum C2 [phi_s(N-1,N) (x) |N-2; Gamma'' L''>]_{LM}
with phi_s(N-1,N)_mu = sum <f m1 f m2|s mu> e_m1(N-1) e_m2(N).  The left side is computed in
first quantization from explicit symmetric tensors (verify_first_quantized.to_tensor); the
right side uses the engine's one-body CFPs with signs.  With Theorem A and the closed forms of
RESULTS.md this gives two-body CFPs in closed form wherever the one-body ones are known.
Run: $PY code/verify_two_body.py
"""
import sympy as sp
from sympy.physics.wigner import clebsch_gordan, wigner_6j

from check_seniority_factorization import harmonic_states
from fpc_core import SpinBosons
from verify_first_quantized import lowered, to_tensor


def c1(B, parent, N, L, daughter, Lp):
    sq, sg = B.cfp_sq_sign(parent, N, L, daughter, Lp)
    return sg * sp.sqrt(sp.Rational(int(sq.p), int(sq.q)))


def c2_first_quantized(B, parent, N, L, gdaughter, Lpp, s):
    f = B.f
    Psi = to_tensor(B, parent, N)
    acc = 0
    for Mpp, gpoly in lowered(B, gdaughter, Lpp):
        mu = L - Mpp
        if abs(mu) > s:
            continue
        cg_outer = clebsch_gordan(s, Lpp, L, mu, Mpp, L)
        if cg_outer == 0:
            continue
        G = to_tensor(B, gpoly, N - 2)
        for m1 in range(-f, f + 1):
            m2 = mu - m1
            if abs(m2) > f:
                continue
            cg_pair = clebsch_gordan(f, f, s, m1, m2, mu)
            if cg_pair == 0:
                continue
            for key, x in G.items():
                y = Psi.get(key + (m1, m2))
                if y is not None:
                    acc += cg_outer * cg_pair * x * y
    return sp.nsimplify(sp.radsimp(acc))


def main():
    checks = 0
    for f, Nmax in ((1, 5), (2, 4)):
        B = SpinBosons(f)
        H = harmonic_states(B, Nmax)
        states = {}
        for (v, L), hs in H.items():
            for al, h in enumerate(hs):
                p, N = h, v
                while N <= Nmax:
                    states[(N, v, L, al)] = p
                    p = B.pair_cre(p)
                    N += 2
        for (N, v, L, al), p in states.items():
            if N < 3:
                continue
            for (N2, v2, L2, al2), g in states.items():
                if N2 != N - 2:
                    continue
                for s in range(0, 2 * f + 1):
                    if not (abs(L - L2) <= s <= L + L2):
                        continue
                    lhs = c2_first_quantized(B, p, N, L, g, L2, s)
                    rhs = 0
                    if s % 2 == 0:
                        for (N1, v1, L1, al1), q in states.items():
                            if N1 != N - 1:
                                continue
                            a = c1(B, p, N, L, q, L1)
                            b = c1(B, q, N - 1, L1, g, L2)
                            if a == 0 or b == 0:
                                continue
                            rhs += a * b * (-1) ** (L + L2) * sp.sqrt((2 * s + 1) * (2 * L1 + 1)) * \
                                wigner_6j(f, f, s, L2, L, L1)
                    assert sp.simplify(lhs - rhs) == 0, (f, N, v, L, al, v2, L2, al2, s, lhs, rhs)
                    checks += 1
    print(f"two-body chain formula verified exactly: {checks} two-body CFPs (f=1 N<=5, f=2 N<=4), "
          f"including signs and the vanishing of odd-s pairs")


if __name__ == "__main__":
    main()
