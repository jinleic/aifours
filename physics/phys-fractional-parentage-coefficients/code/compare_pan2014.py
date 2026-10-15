"""Reproduction check against Pan, Bao, Zhang, Draayer, EPJ Plus 129, 169 (2014), arXiv:1309.2654,
Tables III and IV (elementary O(5) > O(3) Wigner coefficients <(tau 0) L1; (1 0) 2 || (tau+1 0) L>,
L = 2 tau + 2 - k, L1 = 2 tau - k').  Our r(v; v-1) with v = tau + 1 is the same quantity up to
phase conventions, so squares are compared.  Table IV (k = 6, multiplicity 2) is compared in
the principal-parent basis of the k' = 2 daughter (their chi = 2) and its orthogonal
complement (chi = 1), computed from basis-independent data.  Entries transcribed from the
arXiv text (pdftotext of arXiv:1309.2654v1, Tables III-IV).
Run: $PY code/compare_pan2014.py
"""
import sympy as sp

from multiplicity_obstruction import family_gram
from top_family_symbolic import Spin2Families, cg2, reduced_cfp2, v

t = sp.Symbol('tau')
f4 = 32 * t ** 4 - 288 * t ** 3 + 1024 * t ** 2 - 1692 * t + 1065       # Pan's f(tau)
F = f4.subs(t, t + 1)                                                    # f(tau+1)
TABLE3 = {  # (k, k'): squared coefficient
    (3, 0): 2 * (4 * t + 1) * (t - 1) / ((4 * t - 1) * (2 * t - 1) * (t + 1)),
    (2, 0): 2 * (2 * t + 1) / ((4 * t - 1) * (t + 1)),
    (0, 0): sp.Integer(1),
    (3, 2): 3 * (2 * t + 1) / ((4 * t - 1) * (t + 1) * (t - 1)),
    (2, 2): (t - 1) * (4 * t + 3) / ((4 * t - 1) * (t + 1)),
    (3, 3): t * (2 * t + 1) * (t - 2) / ((2 * t - 1) * (t + 1) * (t - 1)),
    (4, 0): 32 * t * (t - 1) * (t - 2) / ((4 * t - 1) * (4 * t - 3) * (2 * t + 3) * (2 * t - 1) * (t + 1)),
    (4, 2): 4 * (2 * t + 1) ** 2 * (4 * t + 1) * (t - 2) / ((4 * t - 1) * (4 * t - 5) * (2 * t + 3) * (t + 1) * (t - 1)),
    (5, 2): 2 * (4 * t - 1) * (t - 2) * (t - 3) / ((4 * t - 5) * (2 * t - 3) * (t + 1) * (t - 1)),
    (4, 3): 4 * (4 * t + 1) * (4 * t - 1) / ((2 * t + 3) * (2 * t - 3) * (2 * t - 1) * (t + 1) * (t - 1)),
    (5, 3): 2 * (2 * t + 1) ** 2 * (t - 3) / ((4 * t - 7) * (2 * t - 3) * (t + 1) * (t - 1)),
    (4, 4): (t - 3) * (2 * t - 1) * (2 * t + 1) * (4 * t + 1) * (4 * t - 1) / (
        (4 * t - 3) * (4 * t - 5) * (2 * t + 3) * (2 * t - 3) * (t + 1)),
    (5, 4): 6 * (2 * t + 1) * (2 * t - 1) / ((4 * t - 5) * (2 * t - 3) * (t + 1) * (t - 2)),
    (5, 5): (t - 1) * (t - 4) * (4 * t - 3) * (2 * t - 1) / ((4 * t - 7) * (2 * t - 3) * (t + 1) * (t - 2)),
}
TABLE4 = {  # (k', chi): squared coefficient, k = 6
    (2, 1): sp.Integer(0),
    (2, 2): 3 * F / ((4 * t - 7) * (4 * t - 5) * (2 * t + 3) * (2 * t - 3) * (t + 1) * (t - 1)),
    (3, 1): 32 * (4 * t - 5) * (2 * t - 1) * (t - 1) ** 2 * (t - 3) * (t - 4) / ((4 * t - 7) * (t + 1) * (t - 2) * F),
    (3, 2): (4 * t - 9) ** 2 * (4 * t - 3) * (4 * t - 1) * (2 * t + 1) ** 2 * (2 * t - 1) / (
        (4 * t - 7) * (2 * t + 3) * (2 * t - 3) * (t + 1) * (t - 1) * F),
    (4, 1): 6 * (4 * t - 5) ** 2 * (4 * t - 3) * (2 * t + 1) * (t - 4) / ((4 * t - 9) * (t + 1) * (t - 2) * F),
    (4, 2): 192 * (4 * t - 1) * (2 * t + 1) * (2 * t - 1) ** 2 * (t - 1) * (t - 3) ** 3 / (
        (4 * t - 9) * (4 * t - 5) * (2 * t + 3) * (2 * t - 3) * (t + 1) * F),
    (5, 1): 12 * (2 * t + 1) ** 2 * (2 * t - 1) ** 2 * (2 * t - 3) ** 2 / ((4 * t - 7) * (2 * t - 5) * (t + 1) * (t - 2) * F),
    (5, 2): 96 * (4 * t - 5) * (4 * t - 3) * (4 * t - 1) * (t - 1) * (t - 3) * (t - 4) / (
        (4 * t - 7) * (2 * t + 3) * (2 * t - 3) * (2 * t - 5) * (t + 1) * F),
}


def main():
    S = Spin2Families()
    D = S.D
    ok3 = 0
    for (k, kp), ref in TABLE3.items():
        (e, psi), = S.basis(k, v)
        (ep, phi), = S.basis(kp, v - 1)
        val, _, _ = reduced_cfp2(D, psi, k, phi, kp, 2)
        assert sp.simplify(val.subs(v, t + 1) - ref) == 0, ((k, kp), sp.factor(val.subs(v, t + 1)), ref)
        ok3 += 1
    # Table IV: principal-parent basis of the k'=2 daughter
    _, phi0, phi1, q00, q01, q11, disc = family_gram(6)
    G = sp.Matrix([[q00, q01], [q01, q11]])
    Ginv = G.inv()
    k = 6
    data = {}
    for kp in (2, 3, 4, 5):
        (e0, y), = S.basis(kp, v - 1)
        j = k - kp
        nd = D.inner(y, y, v - 1, kp)
        shift = kp + 1 - k
        fac = sp.ff(v - k, shift) if shift >= 0 else 1 / sp.ff(v - 1 - kp, -shift)
        Cd = fac / (D.w(j) * nd * v * cg2(2, 2 * v - k, 2 * (v - 1) - kp, j))
        b = sp.Matrix([D.inner(phi0, D.mul_z(y, j), v, k), D.inner(phi1, D.mul_z(y, j), v, k)])
        data[kp] = (Cd, b)
    C2, b2 = data[2]
    Q22 = sp.cancel(C2 * (b2.T * Ginv * b2)[0, 0])
    ok4 = 0
    for kp in (2, 3, 4, 5):
        Cd, b = data[kp]
        Qdd = sp.cancel(Cd * (b.T * Ginv * b)[0, 0])
        Q2d_sq = sp.cancel(C2 * Cd * ((b2.T * Ginv * b)[0, 0]) ** 2)
        chi2 = sp.cancel(Q2d_sq / Q22)                    # principal parent of k'=2
        chi1 = sp.cancel(Qdd - chi2)                      # orthogonal complement
        for chi, val in ((1, chi1), (2, chi2)):
            ref = TABLE4[(kp, chi)]
            diff = sp.simplify(val.subs(v, t + 1) - ref)
            status = "agrees" if diff == 0 else f"DIFFERS: ours = {sp.factor(val.subs(v, t + 1))}"
            print(f"Table IV k'={kp} chi={chi}: {status}")
            ok4 += diff == 0
    print(f"Pan et al. (2014) Table III: {ok3}/14 squared entries reproduced exactly; "
          f"Table IV (multiplicity-free rows): {ok4}/8 reproduced")
    assert ok3 == 14 and ok4 == 8, "disagreement with Pan et al. (2014)"


if __name__ == "__main__":
    main()
