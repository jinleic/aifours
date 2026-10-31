#!/usr/bin/env python3
"""Independent finite exact controls; no author code or external libraries."""
from fractions import Fraction as F


class G:
    def __init__(self, r=0, i=0):
        if isinstance(r, G):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = F(r), F(i)

    def __add__(self, o):
        o = G(o)
        return G(self.r + o.r, self.i + o.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, o):
        return self + (-G(o))

    def __rsub__(self, o):
        return G(o) - self

    def __mul__(self, o):
        o = G(o)
        return G(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = G(o)
        den = o.r * o.r + o.i * o.i
        assert den
        return G((self.r * o.r + self.i * o.i) / den,
                 (self.i * o.r - self.r * o.i) / den)

    def __eq__(self, o):
        o = G(o)
        return self.r == o.r and self.i == o.i

    def __repr__(self):
        return f"({self.r}+{self.i}i)"

    def conj(self):
        return G(self.r, -self.i)

    def real(self):
        assert self.i == 0, self
        return self.r

    def abs2(self):
        return self.r * self.r + self.i * self.i


def zmat(m, n):
    return [[G() for _ in range(n)] for _ in range(m)]


def eye(n):
    a = zmat(n, n)
    for j in range(n):
        a[j][j] = G(1)
    return a


def adj(a):
    return [[a[i][j].conj() for i in range(len(a))] for j in range(len(a[0]))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[G(c) * x for x in row] for row in a]


def mul(a, b):
    assert len(a[0]) == len(b)
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), G())
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, v):
    return [sum((a[i][j] * v[j] for j in range(len(v))), G()) for i in range(len(a))]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), G())


def dot(u, v):
    return sum((x.conj() * y for x, y in zip(u, v)), G())


def n2(v):
    return dot(v, v).real()


def fro2(a):
    return sum((x.abs2() for row in a for x in row), F(0))


def outer(u, v):
    return [[x * y.conj() for y in v] for x in u]


def basis(n, j):
    v = [G() for _ in range(n)]
    v[j] = G(1)
    return v


def vec(n, entries):
    v = [G() for _ in range(n)]
    for j, x in entries.items():
        v[j] = G(x)
    return v


def kron(a, b):
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])]
             for j in range(len(a[0]) * len(b[0]))] for i in range(len(a) * len(b))]


def inv(a):
    n = len(a)
    rows = [list(a[i]) + eye(n)[i] for i in range(n)]
    for k in range(n):
        pivot = next(j for j in range(k, n) if rows[j][k] != 0)
        rows[k], rows[pivot] = rows[pivot], rows[k]
        p = rows[k][k]
        rows[k] = [x / p for x in rows[k]]
        for j in range(n):
            if j != k:
                p = rows[j][k]
                rows[j] = [x - p * y for x, y in zip(rows[j], rows[k])]
    return [row[n:] for row in rows]


def rank(a):
    a = [list(row) for row in a]
    m, n = len(a), len(a[0])
    k = 0
    for j in range(n):
        pivot = next((i for i in range(k, m) if a[i][j] != 0), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        p = a[k][j]
        a[k] = [x / p for x in a[k]]
        for i in range(k + 1, m):
            p = a[i][j]
            a[i] = [x - p * y for x, y in zip(a[i], a[k])]
        k += 1
        if k == m:
            break
    return k


def unit_col_sigma2(a):
    aa = mul(adj(a), a)
    assert all(aa[i][j] == 0 for i in range(len(aa)) for j in range(len(aa)) if i != j)
    return max(aa[i][i].real() for i in range(len(aa)))


def comm(a):
    return sub(mul(a, adj(a)), mul(adj(a), a))


def iszero(a):
    return all(x == 0 for row in a for x in row)


def diagonal(xs):
    a = zmat(len(xs), len(xs))
    for j, x in enumerate(xs):
        a[j][j] = G(x)
    return a


# Direct rational sampling of the cleared Gram identity, not a proof of it.
gram_count = 0
for k in range(1, 10):
    t, q = F(k, 10), F(10-k, 10)
    for j in range(10):
        r = t*q*F(j, 10)
        dlt = t*q-r
        nn = q*(t*t+r)/dlt-r/(dlt*(1+2*dlt))
        assert (1+t-nn)*(1+2*dlt) == 1+2*t*q-4*r
        assert nn <= t*(1+2*q)
        gram_count += 1
assert 1+2*F(1, 4)-4*F(1, 8) != 1+2*F(1, 4)-3*F(1, 8)
print('gram rational points:', gram_count, '; altered -3r identity rejected')

# Compute a complex weighted Riesz maximizer independently by matrix inversion.
u = vec(4, {0: F(3, 5)})
v = vec(4, {0: F(396, 505), 1: G(0, F(80, 505))})
t, q = n2(u), n2(v)
r = dot(u, v).abs2()
dlt = t*q-r
assert t+q == 1 and dlt > 0
D = sub(sub(eye(4), outer(u, u)), outer(v, v))
H = inv(D)
assert mul(D, H) == eye(4)
N = q*dot(u, mv(H, u)).real() - dot(v, mv(H, u)).abs2()/trace(H).real()
assert dot(u, mv(H, u)).real() == (t*t+r)/dlt
assert dot(v, mv(H, u)).abs2() == r/(dlt*dlt)
assert trace(H).real() == 2+1/dlt
assert N == q*(t*t+r)/dlt-r/(dlt*(1+2*dlt))
Z = outer(v, mv(H, u))
Aproj = sub(Z, scale(trace(Z)/trace(H), H))
assert trace(Aproj) == 0
wd = trace(mul(mul(adj(Aproj), Aproj), D)).real()
ll = dot(v, mv(Aproj, u)).abs2()
assert wd > 0 and ll == N*wd
assert N > t*(1+q)
print('complex Gram/Riesz saturation: exact; negative coefficient t(1+q) rejected')

# Explicit trace-zero and endpoints, including rank-one equality of dagger.
A1 = zmat(4, 4)
A1[0][1] = G(1)
A2 = zmat(4, 4)
A2[0][1], A2[1][2] = G(2), G(0, 1)
A3 = diagonal([3, -1, -1, -1])
A4 = diagonal([1, G(0, 1), -1, G(0, -1)])
A0 = zmat(4, 4)
a_list = [A0, A1, A2, A3, A4]
uv = [
    (u, v),
    (vec(4, {0:F(1,2), 1:G(0,F(1,2))}), vec(4, {2:F(1,2), 3:G(0,F(1,2))})),
    (vec(4, {0:F(1,2), 1:F(1,2)}), vec(4, {0:F(1,2), 1:F(1,2)})),
    (vec(4, {1:F(3,5)}), vec(4, {1:G(0,F(4,5))})),
    (basis(4, 0), vec(4, {})),
    (vec(4, {}), basis(4, 3)),
]
lemma_count = 0
for a in a_list:
    assert trace(a) == 0
    f, sig = fro2(a), unit_col_sigma2(a)
    for x, y in uv:
        t, q = n2(x), n2(y)
        assert t+q == 1
        dx = f-n2(mv(a, x))-n2(mv(a, y))
        L = dot(y, mv(a, x))
        assert dx >= 0 and L.abs2() <= t*(1+2*q)*dx <= (t+F(1,2))*dx
        gap = 2*f-(n2(mv(a, x))+n2(mv(a, y))+L.abs2()/(1+t)+sig)
        margin = f-sig+(1-2*t*q)*dx/(1+t)
        assert gap >= margin >= f-sig+dx/(2*(1+t)) >= 0
        b = F(3, 2)
        gu = [p+b*z for p,z in zip(mv(a,x),y)]
        cross_gap = 2*(f+b*b)-(n2(gu)+n2(mv(a,y))+sig)
        square = (1+t)*(G(b)-L/(1+t)).abs2()
        assert cross_gap >= margin+square and cross_gap > 0
        lemma_count += 1
xe, ye = uv[3]
equality = 2*fro2(A1)-(n2(mv(A1,xe))+n2(mv(A1,ye))+dot(ye,mv(A1,xe)).abs2()/(1+n2(xe))+unit_col_sigma2(A1))
assert equality == 0
print('lemma/dagger/cross exact cases:', lemma_count, '; rank-one dagger equality, all b=3/2 cross gaps strict')

# Intended negative: omitting trace-zero makes the lemma false.
w = vec(4, {0:F(1,2), 1:F(1,2)})
P = zmat(4, 4)
for i in (0,1):
    for j in (0,1):
        P[i][j] = G(F(1,2))
dp = fro2(P)-2*n2(mv(P,w))
lp = dot(w,mv(P,w)).abs2()
assert trace(P) == 1 and dp == 0 and lp == F(1,4) and lp > n2(w)*(1+2*n2(w))*dp
print('negative missing trace-zero: d=0, |L|^2=1/4 > 0')

# Exact partial traces and swap/HS identities on complex unit vectors.
psi = [basis(8,0), basis(8,3), vec(8,{0:F(3,5),3:G(0,F(4,5))}),
       vec(8,{0:F(4,5),3:G(0,-F(3,5))}), vec(8,{4:F(3,5),7:G(0,F(4,5))})]
T = [[G(1),G(0,1)],[G(-2),G(0,2)]]
Gamma = add(kron(A2,eye(2)),kron(eye(4),T))
swap_count = 0
for x in psi:
    for y in psi:
        assert n2(x)==n2(y)==1
        c = dot(y,x)
        M = [[sum((x[2*i+k]*y[2*j+k].conj() for k in range(2)),G()) for j in range(4)] for i in range(4)]
        N2 = [[sum((x[2*i+k]*y[2*i+l].conj() for i in range(4)),G()) for l in range(2)] for k in range(2)]
        assert trace(M)==trace(N2)==c
        m0, n0 = sub(M,scale(c/4,eye(4))), sub(N2,scale(c/2,eye(2)))
        s1,s2 = fro2(N2),fro2(M)
        assert 0<=s1<=1 and 0<=s2<=1 and 1-s1-s2+c.abs2()>=0
        weight = fro2(m0)+fro2(n0)/2
        assert weight == s2+s1/2-c.abs2()/2 and weight<=1
        amp = dot(y,mv(Gamma,x))
        assert amp == trace(mul(A2,m0))+trace(mul(T,n0))
        assert amp.abs2() <= (fro2(A2)+2*fro2(T))*weight
        swap_count += 1
# At an equal product state, missing both trace-centering corrections produces 3/2 > 1.
assert F(1)+F(1,2)>1
print('complex swap/HS vector pairs:', swap_count, '; negative no-centering factor 3/2 > 1')

# Supported-site pair norm and saturation; this does not test unrestricted planes.
def tensor_vec(x,y):
    return [a*b for a in x for b in y]

X = kron(A1,eye(4))
f1 = tensor_vec(basis(4,1),basis(4,0))
f2 = tensor_vec(basis(4,1),basis(4,1))
assert dot(f1,f2)==0 and n2(f1)==n2(f2)==1
projected = n2(mv(X,f1))+n2(mv(X,f2))
assert projected == 2 and fro2(X)==4 and projected==fro2(X)/2
assert projected>fro2(X)/4
print('supported-site saturation: 2=4/2; negative stronger 1/4 bound rejected')

# Explicit square-normal but nonnormal and both-squares-nonnormal matrices.
B = zmat(4,4)
B[0][0],B[1][1],B[0][1] = G(1),G(-1),G(0,2)
B[2][2],B[3][3],B[2][3] = G(2),G(-2),G(3)
B2 = mul(B,B)
assert trace(B)==0 and rank(B)==4 and not iszero(comm(B)) and iszero(comm(B2))
assert B2==diagonal([1,1,4,4])
Z2 = zmat(4,4)
Z2[0][1],Z2[2][3] = G(1),G(2)
assert trace(Z2)==0 and rank(Z2)==2 and iszero(mul(Z2,Z2))
C = adj(A2)
assert trace(A2)==trace(C)==0 and not iszero(comm(mul(A2,A2))) and not iszero(comm(mul(C,C)))
print('square-normal nonnormal full-rank example and rank-two square-zero: exact')
print('negative square-normal implies normal rejected; both-squares-nonnormal domain nonempty')
print('ALL FINITE EXACT CONTROLS PASSED; examples do not prove universal assertions')
