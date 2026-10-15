"""Square-class analysis of the two-dimensional spin-2 multiplicity families L = 2v - k
(k = 6, 8, 9, 10, 11; default k = 6, the first multiplicity family).

For v > k the space V of seniority-v, spin-(2v-k) highest-weight states is 2-dimensional
over K = Q(v), spanned by phi0 = proj(covariant with e = 0) and phi1 = proj(covariant with
e = 1) (for k = 6: f^(v-6) H^3 and f^(v-3) j).  q is the Fock form divided by (v-k)!.
The script prints (exact, symbolic in v):
  * the Gram matrix G, disc(q) = det G and q(phi0), q(phi1), factored over Q;
  * for each multiplicity-free daughter d: the pairing b_d(x) = <x, z_mu y_d> and the factor
    C_d with  cfp(x/|x|; d)^2 = b_d(x)^2 * C_d / q(x);
  * the residue test: for every irreducible non-linear factor pi of q(phi1) (and q(phi0))
    with odd multiplicity, whether -disc is a square in Q[v]/(pi).
Run: $PY code/multiplicity_obstruction.py [k]
"""
import sys

import sympy as sp

from top_family_symbolic import Spin2Families, cg2, f2_labels, v


def square_free_part(expr):
    """(constant, [(irreducible poly, exponent mod 2)]) of a rational function of v."""
    num, den = sp.fraction(sp.factor(sp.together(expr)))
    out = []
    c = sp.Integer(1)
    for poly, sgn in ((num, 1), (den, -1)):
        cf, facs = sp.factor_list(sp.Poly(poly, v))
        c *= sp.Rational(cf) ** sgn
        for fac, m in facs:
            if m % 2:
                out.append(fac.as_expr())
    return c, out


def is_square_mod(expr, pi):
    """Is the rational function expr (a unit at pi) a square in the field F = Q[v]/(pi)?

    Returns (answer, certificate); answer None if undecided.  With d = deg pi and
    alpha = expr(theta), the norm polynomial R(t) = Res_v(t^2 - alpha(v), pi(v)) has degree 2d
    and roots +-sqrt(alpha(theta_i)).
      * R irreducible over Q: sqrt(alpha) has degree 2d > d = [F:Q], so NOT a square;
      * d = 2: decided exactly: alpha = A + B sqrt(Delta) is a square in Q(sqrt(Delta)) iff
        (B = 0 and A or A*Delta is a rational square) or (B != 0, A^2 - Delta B^2 = n^2 and
        S = (A +- n)/2 = s^2 for a sign; then alpha = (s + (B/2s) sqrt(Delta))^2);
      * d an odd prime, alpha not in Q, R = g(t) g(-t) with g irreducible of degree d:
        a root beta of g has degree d and Q(beta) contains Q(alpha) = F (F has no proper
        subfield other than Q), so Q(beta) = F and alpha = beta^2 IS a square.
    """
    P = sp.Poly(pi, v)
    num, den = sp.fraction(sp.together(expr))
    alpha = sp.rem(sp.Poly(num, v) * sp.invert(sp.Poly(den, v), P), P)   # alpha in Q[v]/(pi)
    d = P.degree()
    t = sp.Symbol('t')
    R = sp.Poly(sp.resultant(t ** 2 - alpha.as_expr(), P.as_expr(), v), t)
    facs = sp.factor_list(R)[1]
    if len(facs) == 1 and facs[0][1] == 1 and sp.Poly(facs[0][0], t).degree() == 2 * d:
        return False, f"Res_v(t^2 - alpha, pi) irreducible over Q of degree {2 * d}"
    if d == 2:
        a2, a1, a0 = [sp.Rational(c) for c in P.all_coeffs()]
        Delta = a1 ** 2 - 4 * a2 * a0
        c1, c0 = ([sp.Rational(c) for c in alpha.all_coeffs()] + [0, 0])[:2] if alpha.degree() == 1 \
            else (sp.Integer(0), sp.Rational(alpha.as_expr()))
        A = c0 - c1 * a1 / (2 * a2)
        Bc = c1 / (2 * a2)

        def ratsq(x):
            return x >= 0 and sp.sqrt(x).is_rational

        if Bc == 0:
            ok = ratsq(A) or ratsq(A * Delta)
            return ok, f"alpha = {A} in Q; Delta = {Delta}"
        Nrm = A ** 2 - Delta * Bc ** 2
        if not ratsq(Nrm):
            return False, f"norm A^2 - Delta B^2 = {Nrm} is not a rational square (Delta = {Delta})"
        n = sp.sqrt(Nrm)
        for S in ((A + n) / 2, (A - n) / 2):
            if S != 0 and ratsq(S):
                s = sp.sqrt(S)
                tt = Bc / (2 * s)
                assert sp.expand((s + tt * sp.sqrt(Delta)) ** 2 - (A + Bc * sp.sqrt(Delta))) == 0
                return True, f"alpha = ({s} + {tt} sqrt({Delta}))^2"
        return False, f"norm is a square but neither (A +- n)/2 is a rational square (Delta = {Delta})"
    if sp.isprime(d) and d > 2 and alpha.degree() >= 1 and len(facs) == 2 and all(
            m == 1 and sp.Poly(g, t).degree() == d for g, m in facs):
        g = sp.Poly(facs[0][0], t)
        h = sp.Poly(facs[1][0], t)
        if sp.Poly(g.as_expr().subs(t, -t), t).monic() == h.monic():
            return True, f"R = g(t) g(-t), g irreducible of prime degree {d}: {g.as_expr()}"
    return None, f"inconclusive: Res factors as {facs}"


def family_gram(k=6):
    """Symbolic Gram data of family k: (S, phi0, phi1, q00, q01, q11, disc)."""
    assert f2_labels(k) == [0, 1], k
    S = Spin2Families()
    D = S.D
    phi0 = S.harm_proj(S.covariant(k, 0), v, k)
    phi1 = S.harm_proj(S.covariant(k, 1), v, k)
    q00 = D.inner(phi0, phi0, v, k)
    q01 = D.inner(phi0, phi1, v, k)
    q11 = D.inner(phi1, phi1, v, k)
    disc = sp.factor(q00 * q11 - q01 ** 2)
    return S, phi0, phi1, q00, q01, q11, disc


def numeric_crosscheck(k, q00, q01, q11, nvals=10):
    """Scale-invariant check against the independent polynomial engine (spin2_basis):
    cos^2 = q01^2/(q00 q11) of the two projected covariants at L = 2v - k."""
    from spin2_basis import Spin2
    S2 = Spin2()
    B = S2.B
    for vv in range(k + 1, k + 1 + nvals):
        (e0, a), (e1, b) = S2.raw_basis(vv, 2 * vv - k)
        assert (e0, e1) == (0, 1)
        num = B.inner(a, b) ** 2 / (B.norm2(a) * B.norm2(b))
        sym = sp.Rational((q01 ** 2 / (q00 * q11)).subs(v, vv))
        assert sym == sp.Rational(int(num.p), int(num.q)), vv
    return nvals


def main(k=6):
    S, phi0, phi1, q00, q01, q11, disc = family_gram(k)
    D = S.D
    print(f"family k = {k} (L = 2v - {k})")
    print("q(phi0) =", sp.factor(q00))
    print("q(phi1) =", sp.factor(q11))
    print("<phi0,phi1> =", sp.factor(q01))
    print("disc = det G =", disc)
    print("square-free part of disc:", square_free_part(disc))
    n = numeric_crosscheck(k, q00, q01, q11)
    print(f"independent numeric engine agrees on q01^2/(q00 q11) for {n} values v = {k + 1}..{k + n}")
    free = [kp for kp in range(max(0, k - 4), k + 1) if len(f2_labels(kp)) == 1]
    rows = []
    Cd_list = []
    for kp in free:
        (e0, y), = S.basis(kp, v - 1)
        j = k - kp
        nd = D.inner(y, y, v - 1, kp)
        shift = kp + 1 - k
        fac = sp.ff(v - k, shift) if shift >= 0 else 1 / sp.ff(v - 1 - kp, -shift)
        Cd = sp.factor(fac / (D.w(j) * nd * v * cg2(2, 2 * v - k, 2 * (v - 1) - kp, j)))
        b0 = D.inner(phi0, D.mul_z(y, j), v, k)
        b1 = D.inner(phi1, D.mul_z(y, j), v, k)
        rows.append((b0, b1))
        Cd_list.append(Cd)
        print(f"daughter k'={kp}: C_d = {Cd};  square-free part {square_free_part(Cd)}")
        print(f"   b_d(phi0) = {sp.factor(b0)},  b_d(phi1) = {sp.factor(b1)}")
    M = sp.Matrix(rows)
    print(f"rank of the {len(rows)}x2 pairing matrix over Q(v):", M.rank(simplify=True))
    G = sp.Matrix([[q00, q01], [q01, q11]])
    Ginv = G.inv()
    # basis-invariant total parentage weight Q_dd = C_d * b_d^T G^{-1} b_d (sum over any
    # orthonormal parent basis of cfp^2 into daughter d); principal parent of d has
    # q(x_d) = b_d^T G^{-1} b_d.
    for kp, (b0, b1), Cd in zip(free, rows, Cd_list):
        bvec = sp.Matrix([b0, b1])
        beta = sp.factor(sp.cancel((bvec.T * Ginv * bvec)[0, 0]))
        Qdd = sp.factor(sp.cancel(beta * Cd))
        print(f"daughter k'={kp}: Q_dd = {Qdd}")
        print(f"   square-free part of Q_dd: {square_free_part(Qdd)}")
    for name, a in (("q(phi1)", q11), ("q(phi0)", q00)):
        _, facs = square_free_part(a)
        for pi in facs:
            if sp.Poly(pi, v).degree() >= 2:
                sq, cert = is_square_mod(-disc, pi)
                print(f"residue test at pi = {pi} (odd in {name}): -disc is "
                      f"{'a square' if sq else ('NOT a square' if sq is False else 'undecided')}"
                      f" in Q[v]/(pi)   [{cert}]")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
