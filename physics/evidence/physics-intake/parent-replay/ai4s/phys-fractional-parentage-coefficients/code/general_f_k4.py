"""The first multiplicity family for spin f >= 3: L = f v - 4 (two states of seniority v).

For f >= 3 the deficit-4 highest-weight space is two-dimensional and automatically harmonic
(P lowers the deficit by 2f > 4).  This script (exact, symbolic in v, for f = 3, 4, 5):
  * builds a Q(v)-rational basis (sympy null space of S+ in deficit coordinates) and the Gram
    matrix of the Fock form / (v-4)!;
  * checks that the factors C_d of the multiplicity-free daughters (k' = 0, 2, 3) are products of
    linear polynomials and that the pairing matrix has rank 2;
  * cross-checks the basis-independent weight Q_dd into the stretched daughter (k' = 0) against
    the independent polynomial engine fpc_core at v = 5..9;
  * runs the residue (Brauer) analysis of brauer_residues.analyze on <q11, q11*disc>.
Run: $PY general_f_k4.py [f ...]   (default 3 4 5)
"""
import sys

import sympy as sp
from flint import fmpq

from brauer_residues import analyze
from fpc_core import SpinBosons
from multiplicity_obstruction import square_free_part
from top_family_symbolic import Deficit, cg2, v


def family(f):
    D = Deficit(f, 2 * f)
    k = 4
    phi0, phi1 = D.hw_kernel(v, k, harmonic=False)
    q00 = D.inner(phi0, phi0, v, k)
    q01 = D.inner(phi0, phi1, v, k)
    q11 = D.inner(phi1, phi1, v, k)
    disc = sp.factor(q00 * q11 - q01 ** 2)
    rows, Cds = [], []
    for kp in (0, 2, 3):
        (y,) = D.hw_kernel(v - 1, kp, harmonic=False)
        j = k - kp
        nd = D.inner(y, y, v - 1, kp)
        shift = kp + 1 - k
        fac = sp.ff(v - k, shift) if shift >= 0 else 1 / sp.ff(v - 1 - kp, -shift)
        Cd = sp.factor(fac / (D.w(j) * nd * v * cg2(f, f * v - k, f * (v - 1) - kp, j)))
        rows.append((D.inner(phi0, D.mul_z(y, j), v, k), D.inner(phi1, D.mul_z(y, j), v, k)))
        Cds.append(Cd)
    return D, q00, q01, q11, disc, rows, Cds


def numeric_Q00(f, n):
    """sum over an orthonormal basis of the (n, L = f n - 4) block of cfp^2 into the stretched
    daughter, from the polynomial engine."""
    B = SpinBosons(f)
    basis = B.hw_harmonic_basis(n, f * n - 4)
    assert len(basis) == 2
    ortho = []
    for w in basis:
        w = dict(w)
        for u in ortho:
            c = B.inner(u, w) / B.norm2(u)
            for a, x in u.items():
                w[a] = w.get(a, fmpq(0)) - c * x
            w = {a: x for a, x in w.items() if x != 0}
        ortho.append(w)
    daughter = {tuple([0] * (2 * f) + [n - 1]): fmpq(1)}
    return sum((B.cfp_sq_sign(psi, n, f * n - 4, daughter, f * (n - 1))[0] for psi in ortho), fmpq(0))


def main(fs_):
    for f in fs_:
        D, q00, q01, q11, disc, rows, Cds = family(f)
        print(f"=== spin f = {f}, family L = {f}v - 4 ===")
        print("q(phi0) =", sp.factor(q00))
        print("q(phi1) =", sp.factor(q11))
        print("disc =", disc)
        for kp, Cd in zip((0, 2, 3), Cds):
            nonlin = [p for p in square_free_part(Cd)[1] if sp.Poly(p, v).degree() > 1]
            assert not nonlin, (f, kp, Cd)
        M = sp.Matrix(rows)
        print("C_d linear-type for k' = 0, 2, 3; pairing rank:", M.rank(simplify=True))
        G = sp.Matrix([[q00, q01], [q01, q11]])
        b = sp.Matrix(rows[0])
        Q00 = sp.factor(sp.cancel(Cds[0] * (b.T * G.inv() * b)[0, 0]))
        print("basis-independent weight into the stretched daughter Q_00 =", Q00)
        for n in range(5, 10):
            num = numeric_Q00(f, n)
            assert sp.Rational(Q00.subs(v, n)) == sp.Rational(int(num.p), int(num.q)), (f, n)
        print("Q_00 agrees with the polynomial engine at v = 5..9")
        analyze(q11, disc, height=30)


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or [3, 4, 5])
