"""Cross-checks against the independent polynomial engine fpc_core:
  * Theorem B (general spin f, near-stretched families k = 2, 3), f = 2..6, v <= 10.  The
    formulas come symbolically (in v and f) from top_family_symbolic.run_general and are
    compared exactly, with signs, to the CFP of the unique highest-weight state of
    S_z = f v - k in Sym^v (phase: coefficient of the lexicographically largest exponent
    tuple positive, the rule used in the derivation);
  * Theorem E1 (weight of the scalar parent), f = 1..4, v <= 9;
  * Theorem B' (k = 4, first multiplicity family, pair-first basis), f = 3, 4, 5, v <= 9.
Run: $PY code/check_general_f.py
"""
import sympy as sp
from flint import fmpq

from fpc_core import SpinBosons
from top_family_symbolic import fs, run_general, run_general_k4, v


def unique_state(B, n, L):
    basis = B.hw_harmonic_basis(n, L)
    assert len(basis) == 1, (B.f, n, L, len(basis))
    p = basis[0]
    lead = max(p)
    return p if p[lead] > 0 else {a: -c for a, c in p.items()}



def pair_first_numeric(B, n):
    """Numeric pair-first basis of the deficit-4 space at degree n (same rule as
    top_family_symbolic.pair_first_k4): GS of z_f^(n-2) Q4, z_f^(n-4) H2^2."""
    f = B.f
    Q4 = unique_state(B, 2, 2 * f - 4)
    H2 = unique_state(B, 2, 2 * f - 2)
    zf = lambda m: {tuple([0] * (2 * f) + [m]): fmpq(1)}  # noqa: E731
    A = B.mul(zf(n - 2), Q4)
    Bv = B.mul(zf(n - 4), B.mul(H2, H2))
    c = B.inner(A, Bv) / B.norm2(A)
    B2 = dict(Bv)
    for a, x in A.items():
        B2[a] = B2.get(a, fmpq(0)) - c * x
    return [A, {a: x for a, x in B2.items() if x != 0}]


def check_k4(fvals=(3, 4, 5), nmax=9):
    res = run_general_k4()
    checks = 0
    for f in fvals:
        B = SpinBosons(f)
        for n in range(5, nmax + 1):
            parents = pair_first_numeric(B, n)
            daughters = {0: [{tuple([0] * (2 * f) + [n - 1]): fmpq(1)}],
                         2: [unique_state(B, n - 1, f * (n - 1) - 2)],
                         3: [unique_state(B, n - 1, f * (n - 1) - 3)],
                         4: pair_first_numeric(B, n - 1)}
            for i, psi in enumerate(parents, start=1):
                tot = fmpq(0)
                for kp, ds in daughters.items():
                    for jd, phi in enumerate(ds, start=1):
                        sq, s = B.cfp_sq_sign(psi, n, f * n - 4, phi, f * (n - 1) - kp)
                        val, sg = res[(i, kp, jd if kp == 4 else 0)]
                        ref = sp.Rational(val.subs({fs: f, v: n}))
                        assert sp.Rational(int(sq.p), int(sq.q)) == ref, (f, n, i, kp, jd, sq, ref)
                        if ref != 0:
                            assert s == sg, (f, n, i, kp, jd)
                        tot += sq
                        checks += 1
                assert tot == 1, (f, n, i, tot)
    return checks

def scalar_parent_weight(fmax=4, nmax=9):
    """Theorem E1: for every normalised seniority-(v-1) state phi with L' = 0, the total weight
    sum_alpha cfp(v alpha L=f; phi)^2 = (2v+D-2)(v+D-3) / (D v (2v+D-4)),  D = 2f+1."""
    from check_seniority_factorization import harmonic_states
    checks = 0
    for f in range(1, fmax + 1):
        B = SpinBosons(f)
        D = B.D
        H = harmonic_states(B, nmax)
        for (vm1, Lp), daughters in H.items():
            v_ = vm1 + 1
            if Lp != 0 or v_ > nmax or (v_, f) not in H:
                continue
            for phi in daughters:
                W = sum((B.cfp_sq_sign(psi, v_, f, phi, 0)[0] for psi in H[(v_, f)]), fmpq(0))
                assert W == fmpq((2 * v_ + D - 2) * (v_ + D - 3), D * v_ * (2 * v_ + D - 4)), (f, v_)
                checks += 1
    return checks


def main():
    _, res = run_general(3)
    checks = 0
    for f in range(2, 7):
        B = SpinBosons(f)
        for (k, kp), (val, sg) in res.items():
            if not (k < 2 * f):
                continue
            for n in range(max(k, kp + 1, 2), 11):
                L, Lp = f * n - k, f * (n - 1) - kp
                psi = unique_state(B, n, L)
                phi = unique_state(B, n - 1, Lp)
                sq, s = B.cfp_sq_sign(psi, n, L, phi, Lp)
                ref = sp.Rational(val.subs({fs: f, v: n}))
                assert sp.Rational(int(sq.p), int(sq.q)) == ref, (f, n, k, kp, sq, ref)
                if ref != 0:
                    assert s == sg, (f, n, k, kp, s, sg)
                checks += 1
    print(f"Theorem B formulas agree exactly (with signs) with the polynomial engine: {checks} checks,"
          f" f = 2..6, v <= 10")
    print(f"Theorem E1 (scalar-parent weight) agrees exactly: {scalar_parent_weight()} daughters,"
          f" f = 1..4, v <= 9")
    print(f"Theorem B' (k = 4, pair-first basis) agrees exactly (with signs; completeness = 1): "
          f"{check_k4()} CFPs, f = 3, 4, 5, v = 5..9")


if __name__ == "__main__":
    main()
