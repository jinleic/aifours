from fractions import Fraction as F
from itertools import combinations, product
from time import monotonic

START = monotonic()

def budget():
    if monotonic() - START >= 55:
        raise SystemExit("NOT_COMPLETED_TIME_LIMIT")

class E:
    def __init__(self, value=0):
        if isinstance(value, E):
            self.c = value.c
        elif isinstance(value, (tuple, list)):
            if len(value) != 16:
                raise ValueError("Expected 16 field coefficients")
            self.c = tuple(F(x) for x in value)
        else:
            self.c = (F(value),) + (F(0),) * 15

    def __add__(self, other):
        other = E(other)
        return E(tuple(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return E(tuple(-a for a in self.c))

    def __sub__(self, other):
        return self + (-E(other))

    def __rsub__(self, other):
        return E(other) + (-self)

    def __mul__(self, other):
        budget()
        other = E(other)
        out = [F(0)] * 16
        for j, a in enumerate(self.c):
            if not a:
                continue
            for k, b in enumerate(other.c):
                if not b:
                    continue
                degree = j + k
                if degree < 16:
                    out[degree] += a * b
                else:
                    out[degree - 16] -= a * b
        return E(out)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.c == E(other).c

    def bar(self):
        out = [F(0)] * 16
        out[0] = self.c[0]
        for j in range(1, 16):
            out[16 - j] -= self.c[j]
        return E(out)

def zp(k):
    k %= 32
    out = [F(0)] * 16
    out[k % 16] = F(1 if k < 16 else -1)
    return E(out)

ZERO = E(0)
ONE = E(1)
IM = zp(8)

def cs(k):
    return F(1, 2) * (zp(k) + zp(-k))

def sn(k):
    return F(1, 2) * (-IM) * (zp(k) - zp(-k))

H = cs(4)

def eye(n):
    return tuple(tuple(E(int(i == j)) for j in range(n))
                 for i in range(n))

def sm(s, A):
    return tuple(tuple(s * x for x in row) for row in A)

def mm(A, B):
    budget()
    return tuple(tuple(sum((A[i][k] * B[k][j]
                            for k in range(len(B))), ZERO)
                       for j in range(len(B[0])))
                 for i in range(len(A)))

def adj(A):
    return tuple(tuple(A[j][i].bar() for j in range(len(A)))
                 for i in range(len(A[0])))

def mv(A, v):
    return tuple(sum((x * y for x, y in zip(row, v)), ZERO)
                 for row in A)

def vs(s, v):
    return tuple(s * x for x in v)

def inner(v, w):
    return sum((x.bar() * y for x, y in zip(v, w)), ZERO)

def diag(A, B):
    return tuple(tuple(
        A[i][j] if i < 2 and j < 2 else
        B[i - 2][j - 2] if i >= 2 and j >= 2 else ZERO
        for j in range(4)) for i in range(4))

def T(U):
    V = adj(U)
    return tuple(tuple(
        U[i][j - 2] if i < 2 <= j else
        V[i - 2][j] if j < 2 <= i else ZERO
        for j in range(4)) for i in range(4))

def N(k):
    return ((cs(k), sn(k)), (sn(k), -cs(k)))

I2 = eye(2)
I4 = eye(4)
Y = ((ZERO, -IM), (IM, ZERO))
NN = (Y, N(0), N(4), N(2), N(6))
UU = [I2]
for j in range(1, 5):
    UU.append(sm((-1) ** j, mm(NN[j], UU[-1])))
assert UU[4] == sm(-IM, Y)

gg = [diag(Y, Y)]
for j in range(1, 5):
    lower = mm(mm(adj(UU[j - 1]), NN[j]), UU[j - 1])
    gg.append(diag(NN[j], lower))
tt = [T(U) for U in UU]
bb = [sm((-1) ** j, T(sm(IM, U))) for j, U in enumerate(UU)]

for M in gg + tt + bb:
    assert adj(M) == M
    assert mm(M, M) == I4
    assert sum((M[j][j] for j in range(4)), ZERO) == ZERO

def w(j, eps):
    if j == 0:
        return (H, H * eps * IM)
    k = {1: 0, 2: 2, 3: 1, 4: 3}[j]
    if eps == 1:
        return (cs(k), sn(k))
    return (-sn(k), cs(k))

def Q(j, side, eps, eta):
    top = w(j, eps)
    low = mv(adj(UU[j]), top)
    gamma = E(eta) if side == 0 else -IM * ((-1) ** j) * eta
    return vs(H, top) + vs(H * gamma, low)

R = (bb[4], bb[2], bb[0], tt[3], tt[1])
C = (tt[0], bb[3], bb[1], tt[4], tt[2])
D = (gg[0], gg[3], gg[1], gg[4], gg[2])
AMAP = ((0, 0), (3, 1), (1, 1), (4, 0), (2, 0))
BMAP = ((4, 1), (2, 1), (0, 1), (3, 0), (1, 0))

def crt(a, bit):
    a %= 5
    return a + 5 * ((bit - a) % 2)

rays = {}
for typ, mapping in enumerate((AMAP, BMAP)):
    sign = 1 if typ == 0 else -1
    for a, (j, side) in enumerate(mapping):
        ER = R[a]
        EC = C[a if typ == 0 else (a + 1) % 5]
        ED = D[a if typ == 0 else (a - 2) % 5]
        assert mm(ER, EC) == mm(EC, ER)
        assert mm(ER, ED) == mm(ED, ER)
        assert mm(EC, ED) == mm(ED, EC)
        assert mm(mm(ER, EC), ED) == sm(sign, I4)
        for ub, vb in product(range(2), repeat=2):
            eps = sign * ((-1) ** (ub + vb))
            eta = (-1) ** vb if typ == 0 else -((-1) ** ub)
            q = Q(j, side, eps, eta)
            cell = (crt(a, ub), crt(a + typ, vb))
            assert cell not in rays
            rays[cell] = q
            assert mv(ER, q) == vs(sign * ((-1) ** ub), q)
            assert mv(EC, q) == vs(sign * ((-1) ** vb), q)
            assert mv(ED, q) == vs(sign * ((-1) ** (ub + vb)), q)

S = frozenset((0, 1, 5, 6))
expected = {(r, c) for r in range(10) for c in range(10)
            if (c - r) % 10 in S}
assert set(rays) == expected
assert len(rays) == 40

contexts = []
for r in range(10):
    contexts.append(("R" + str(r),
                     tuple(sorted(x for x in rays if x[0] == r))))
for c in range(10):
    contexts.append(("C" + str(c),
                     tuple(sorted(x for x in rays if x[1] == c))))
for s in range(10):
    contexts.append(("L" + str(s),
                     tuple(sorted(x for x in rays
                                  if sum(x) % 10 == s))))
assert len(contexts) == 30

for cell, q in rays.items():
    assert inner(q, q) == ONE, cell
for name, cells in contexts:
    budget()
    assert len(cells) == 4, name
    for x, y in combinations(cells, 2):
        assert inner(rays[x], rays[y]) == ZERO, (name, x, y)

for x, y in combinations(sorted(rays), 2):
    budget()
    z = inner(rays[x], rays[y])
    assert z * z.bar() != ONE, ("PARALLEL", x, y)

orbit = {frozenset((h * s + t) % 10 for s in S)
         for h in (1, 3, 7, 9) for t in range(10)}
assert len(orbit) == 10
for mask in orbit:
    assert all((s + 5) % 10 in mask for s in mask)

budget()
print("FIELD: Q(zeta_32), zeta_32^16 = -1")
print("COEFFICIENT ORDER: 1,zeta_32,...,zeta_32^15")
for cell in sorted(rays):
    coefficients = tuple(tuple(str(a) for a in x.c) for x in rays[cell])
    print("CELL", cell, "COEFFICIENTS", coefficients)
for name, cells in contexts:
    print("CONTEXT", name, cells)
print("AFFINE_SUPPORT_ORBIT", tuple(sorted(tuple(sorted(m)) for m in orbit)))
print("RESULT: PASS_40_RAY_PARTIAL_ARRAY_ONLY")
print("NO_C6_EXTENSION_SUPPLIED; NO_100_RAY_WITNESS; NO_GLOBAL_CLOSURE")
print("ELAPSED_MONOTONIC_SECONDS", monotonic() - START)
