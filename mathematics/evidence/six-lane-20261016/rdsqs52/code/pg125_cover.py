"""Transitive degree-52 action of SL(2,25) (through PSL(2,25)) on (F25^2 \\ {0}) / squares.
Point (p, c): p in PG(1,25) (0..24 = F25 elements, 25 = ∞), c = square class of the
representative scalar t in v = t*(x,1) or t*(1,0); id = p + 26*c."""
import pg125 as F
Q, INF = 25, 25
SQUARES = {F.mul(x, x) for x in range(1, Q)}

def point_of(v1, v2):
    if v2 != 0:
        p = F.mul(v1, F.INV[v2]) if v1 != 0 else 0
        t = v2
    else:
        p = INF
        t = v1
    return p + 26 * (0 if t in SQUARES else 1)

def vec_of(pid):
    p, c = pid % 26, pid // 26
    t = 1 if c == 0 else F.GEN
    return (t, 0) if p == INF else (F.mul(p, t), t)

def matrix_perm(a, b, c, d):
    out = []
    for pid in range(52):
        v1, v2 = vec_of(pid)
        w1 = F.add(F.mul(a, v1), F.mul(b, v2))
        w2 = F.add(F.mul(c, v1), F.mul(d, v2))
        out.append(point_of(w1, w2))
    return tuple(out)

def scalar_perm(n):
    return matrix_perm(n, 0, 0, n)

def frob_perm():
    fr = lambda x: (x % 5) + 5 * ((4 * (x // 5)) % 5)
    out = []
    for pid in range(52):
        v1, v2 = vec_of(pid)
        out.append(point_of(fr(v1), fr(v2)))
    return tuple(out)

g = F.GEN
ginv = F.INV[g]
SL = [matrix_perm(1, 1, 0, 1), matrix_perm(1, 5, 0, 1), matrix_perm(g, 0, 0, ginv), matrix_perm(0, F.neg(1), 1, 0)]
NSQ = scalar_perm(g)                 # swaps the two classes over every projective point
DIAG_NS = matrix_perm(g, 0, 0, 1)    # determinant g: an element of GL(2,25) outside SL·scalars? (PGL part)
FROB = frob_perm()
