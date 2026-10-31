"""Reviewer-authored definitions for the f180 review, written from the
packet text (target y^k coefficients, Lemma 5, Lemma 6, Lemma C3 selectors).

Variables of the 8-variable world: 0..5 = v1..v6 (sorted, six non-largest),
6 = x = v7, 7 = z.  Everything exact (int/Fraction).
"""
import importlib.util, sys, os
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('rlib', os.path.join(_here, 'reviewer-f180-lib.py'))
L = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(L)

N8 = 8
V = [L.var(i, N8) for i in range(6)]
X = L.var(6, N8)
Z = L.var(7, N8)
def C(c): return L.const(c, N8)
def lin(a, b):            # a + b z
    return L.padd(C(a), L.pscale(Z, b))

def build_world():
    w = {}
    e = L.esyms(V + [X], N8, 7)          # e_k of v1..v7
    f = L.esyms(V, N8, 6)                # f_k of v1..v6
    w['e'], w['f'] = e, f
    p = L.padd(e[1], C(-4))
    q = L.padd(e[2], L.pscale(e[1], -4), lin(10, -2))
    zp1sq = L.pmul(lin(1, 1), lin(1, 1))
    # target coefficients of y[(y+1)^2+z]^2 (y^2+p y+q), derived by hand:
    #  y^4: (4+4z)+(6+2z)p+4q ; y^3: (1+z)^2+(4+4z)p+(6+2z)q ; y^2: (1+z)^2 p+(4+4z)q ; y^1: (1+z)^2 q
    E4 = L.psub(e[3], L.padd(lin(4, 4), L.pmul(lin(6, 2), p), L.pscale(q, 4)))
    E3 = L.psub(e[4], L.padd(zp1sq, L.pmul(lin(4, 4), p), L.pmul(lin(6, 2), q)))
    E2 = L.psub(e[5], L.padd(L.pmul(zp1sq, p), L.pmul(lin(4, 4), q)))
    E1 = L.psub(e[6], L.pmul(zp1sq, q))
    A = L.padd(f[2], L.pscale(f[1], -4), lin(10, -2))
    B = L.padd(f[3], L.pscale(f[2], -4), L.pmul(lin(10, -2), f[1]), lin(-20, 12))
    h1 = L.padd(f[3], L.pmul(lin(-6, -2), f[1]), lin(20, 4))
    h0 = L.padd(f[4], L.pmul(lin(-6, -2), f[2]), L.pmul(lin(20, 4), f[1]), L.pscale(L.pmul(Z, Z), 3), lin(-45, 6))
    S4 = L.padd(*V[:4]); S3 = L.padd(*V[:3]); s12 = L.padd(V[0], V[1])
    D = L.psub(h1, L.pmul(A, S4)); E = L.psub(h0, L.pmul(B, S4))
    K = L.psub(E3, L.pmul(E4, S4))
    al = L.esyms(V[:4], N8, 4)
    m2 = al[2]
    L4 = L.padd(V[3], V[4], V[5], X)
    Y2b = L.psub(L.psub(E2, L.pmul(E4, m2)), L.pmul(S3, L.psub(E3, L.pmul(E4, L4))))
    e2_4567 = L.esyms([V[3], V[4], V[5], X], N8, 2)[2]
    alpha = L.psub(al[3], L.pmul(s12, e2_4567))
    beta = L.psub(L.esyms(V[:3], N8, 2)[2], L.pmul(s12, L.padd(V[4], V[5], X)))
    Y1p = L.padd(L.psub(E1, L.pmul(s12, E2)), L.pscale(L.pmul(E4, alpha), -1),
                 L.pscale(L.pmul(K, beta), -1), L.pscale(L.pmul(E4, E4), Fr(1, 2)))
    w.update(dict(p=p, q=q, E4=E4, E3=E3, E2=E2, E1=E1, A=A, B=B, h0=h0, h1=h1, S4=S4, S3=S3, s12=s12,
                  D=D, E=E, K=K, al=al, m2=m2, L4=L4, Y2b=Y2b, alpha=alpha, beta=beta, Y1p=Y1p))
    return w

def at_z(P, zval):
    """substitute z := zval and drop the z variable"""
    return L.drop_var(L.subst_const(P, 7, zval), 7)

def six(P):
    """drop the (absent) x variable from an at_z 7-variable polynomial"""
    return L.drop_var(P, 6)

def selector_polys(zval):
    w = build_world()
    g = {k: at_z(w[k], zval) for k in ('A', 'B', 'h0', 'h1', 'D', 'E', 'Y2b', 'Y1p')}
    A6, B6, D6, E6, h06, h16 = [six(g[k]) for k in ('A', 'B', 'D', 'E', 'h0', 'h1')]
    f1 = six(at_z(w['f'][1], zval))
    F1m4 = L.padd(f1, L.const(-4, 7 - 1))
    c = [six(L.coef_in(g['Y2b'], 6, k)) for k in range(3)]     # c0, c1, c2 of Y2b in x
    d = [six(L.coef_in(g['Y1p'], 6, k)) for k in range(3)]     # d0, d1, d2 of Y1+ in x
    assert L.deg_in(g['Y2b'], 6) == 2 and L.deg_in(g['Y1p'], 6) == 2
    v6 = L.var(5, 6)
    Q0 = L.psub(L.pmul(A6, A6), L.pmul(F1m4, B6))
    GQ = L.padd(L.pmul(c[2], L.pmul(A6, A6)), L.pscale(L.pmul(c[1], L.pmul(A6, F1m4)), -1),
                L.pmul(c[0], L.pmul(F1m4, F1m4)))                  # (f1-4)^2 Y2b(x_q)
    GPQ = L.padd(L.pscale(L.pmul(c[2], A6), -2), L.pmul(c[1], F1m4))   # (f1-4) Y2b'(x_q)
    GE = L.padd(L.pmul(c[2], L.pmul(B6, B6)), L.pscale(L.pmul(c[1], L.pmul(A6, B6)), -1),
                L.pmul(c[0], L.pmul(A6, A6)))                      # A^2 Y2b(x_E)
    nb = {
        'F': L.pscale(F1m4, -1),
        'A': A6,
        'Q': Q0,
        'mA': L.pscale(A6, -1),
        'Fm': F1m4,
        'mE46': L.pscale(L.padd(L.pmul(A6, v6), B6), -1),                         # -E4(v6)
        'mG6': L.pscale(L.padd(L.pmul(c[2], L.pmul(v6, v6)), L.pmul(c[1], v6), c[0]), -1),   # -Y2b(v6)
        'mD6': L.pscale(L.padd(L.pscale(L.pmul(c[2], v6), 2), c[1]), -1),            # -Y2b'(v6)
        'mDl': L.pscale(L.psub(L.pmul(c[1], c[1]), L.pscale(L.pmul(c[2], c[0]), 4)), -1),  # -disc
        'mGq': L.pscale(GQ, -1),
        'T2': L.padd(L.pmul(A6, GQ), L.pmul(GPQ, Q0)),
        'mGE': L.pscale(GE, -1),
        'mDE': L.psub(L.pscale(L.pmul(c[2], B6), 2), L.pmul(c[1], A6)),             # = -A Y2b'(x_E)
    }
    endL = L.padd(L.pmul(d[2], L.pmul(B6, B6)), L.pscale(L.pmul(d[1], L.pmul(A6, B6)), -1), L.pmul(d[0], L.pmul(A6, A6)))
    endH = L.padd(L.pmul(d[2], L.pmul(E6, E6)), L.pscale(L.pmul(d[1], L.pmul(D6, E6)), -1), L.pmul(d[0], L.pmul(D6, D6)))
    mc = {
        'mA': L.pscale(A6, -1),
        'D': D6,
        'H': L.pscale(L.psub(L.pmul(h06, A6), L.pmul(h16, B6)), -1),
        'A': A6,
        'mD': L.pscale(D6, -1),
        'c2': d[2],
        'mendL': L.pscale(endL, -1),
        'mendH': L.pscale(endH, -1),
    }
    return nb, mc, dict(c=c, d=d, A6=A6, B6=B6, D6=D6, E6=E6, h06=h06, h16=h16, F1m4=F1m4, Q0=Q0, w=w, g=g)

def compact_polys(zval):
    """Qpol, Hpol (unscaled) in six unsorted rates u0..u5"""
    n = 6; U = [L.var(i, n) for i in range(n)]
    G = L.esyms(U, n, 4)
    c = lambda a: L.const(a, n)
    A = L.padd(G[2], L.pscale(G[1], -4), c(10 - 2 * zval))
    B = L.padd(G[3], L.pscale(G[2], -4), L.pscale(G[1], 10 - 2 * zval), c(12 * zval - 20))
    h1 = L.padd(G[3], L.pscale(G[1], -(6 + 2 * zval)), c(20 + 4 * zval))
    h0 = L.padd(G[4], L.pscale(G[2], -(6 + 2 * zval)), L.pscale(G[1], 20 + 4 * zval), c(3 * zval * zval + 6 * zval - 45))
    Qpol = L.psub(L.pmul(A, A), L.pmul(L.padd(G[1], c(-4)), B))
    Hpol = L.pscale(L.psub(L.pmul(h0, A), L.pmul(h1, B)), -1)
    return Qpol, Hpol

def residual_polys(zval):
    """(y, tau, gam): al1=y, al2=(3/8) tau y^2, be1=y/2+gam; Abar, Dbar, 2(f1-4), times 144 / 144 / 2"""
    n = 3; Y = L.var(0, n); T = L.var(1, n); G = L.var(2, n); c = lambda a: L.const(a, n)
    b1 = L.padd(L.pscale(Y, Fr(1, 2)), G); a2 = L.pscale(L.pmul(T, L.pmul(Y, Y)), Fr(3, 8))
    K2 = L.padd(a2, L.pscale(L.pmul(Y, Y), -1), L.pscale(Y, 4), c(-6 - 2 * zval))
    Abar = L.padd(a2, L.pscale(Y, -4), c(10 - 2 * zval), L.pmul(b1, L.padd(Y, c(-4))), L.pscale(L.pmul(b1, b1), Fr(1, 4)))
    Dbar = L.padd(L.pscale(L.pmul(Y, Y), 4), L.pscale(Y, -16), c(20 + 4 * zval), L.pscale(L.pmul(Y, a2), Fr(-5, 6)),
                  L.pmul(b1, K2))
    F = L.padd(Y, b1, c(-4))
    return {'Abar': L.pscale(Abar, 144), 'Dbar': L.pscale(Dbar, 144), 'f1minus4': L.pscale(F, 2)}
