#!/usr/bin/env python3
"""Reviewer-authored rational/gaussian controls; finite examples, not a proof."""
from fractions import Fraction as F

class G:
    __slots__ = ('r', 'i')
    def __init__(self, r=0, i=0): self.r, self.i = F(r), F(i)
    @staticmethod
    def of(x): return x if isinstance(x, G) else G(x)
    def __add__(self, x):
        x = G.of(x); return G(self.r+x.r, self.i+x.i)
    __radd__ = __add__
    def __neg__(self): return G(-self.r, -self.i)
    def __sub__(self, x): return self + (-G.of(x))
    def __rsub__(self, x): return G.of(x) - self
    def __mul__(self, x):
        x = G.of(x); return G(self.r*x.r-self.i*x.i, self.r*x.i+self.i*x.r)
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = G.of(x); d = x.r*x.r+x.i*x.i
        return G((self.r*x.r+self.i*x.i)/d, (self.i*x.r-self.r*x.i)/d)
    def __eq__(self, x):
        x = G.of(x); return self.r == x.r and self.i == x.i
    def __bool__(self): return bool(self.r or self.i)
    def conj(self): return G(self.r, -self.i)
    def norm2(self): return self.r*self.r+self.i*self.i
    def __repr__(self): return f'G({self.r},{self.i})'

Z = G()
def zero_matrix(): return [[Z for _ in range(16)] for _ in range(16)]
def add_at(d, key, val): d[key] = d.get(key, Z) + val

def channel(x, t):
    a, b = (1+t)/2, (1-t)/2
    out = zero_matrix()
    for (u, v), coeff in x.items():
        pairs = {(0, 0): F(1)}
        for bit in range(4):
            i, j = (u >> bit) & 1, (v >> bit) & 1
            if i == j:
                options = [(0, 0, a if i == 0 else b), (1, 1, b if i == 0 else a)]
            else:
                options = [(i, j, t)]
            nxt = {}
            for (row, col), factor in pairs.items():
                for rb, cb, f in options:
                    nxt[(row | (rb << bit), col | (cb << bit))] = factor*f
            pairs = nxt
        for (row, col), factor in pairs.items(): out[row][col] = out[row][col] + coeff*factor
    return out

def matmul(a, b):
    out = zero_matrix()
    for i in range(16):
        for k in range(16):
            if a[i][k]:
                for j in range(16):
                    if b[k][j]: out[i][j] = out[i][j] + a[i][k]*b[k][j]
    return out

def comm(a, b):
    ab, ba = matmul(a, b), matmul(b, a)
    return [[ab[i][j]-ba[i][j] for j in range(16)] for i in range(16)]

def block(k): return 0 if k == 0 else (1 if k.bit_count() == 1 else 2)
def wt(k): return k.bit_count()

def experiment(t, amplitudes, tag):
    a, b = (1+t)/2, (1-t)/2
    d3, d4 = 1-a*b, a*a+b*b
    assert sum((z.norm2() for z in amplitudes.values()), F(0)) == 1
    v_input, w_input = {}, {(0, 0): G(-1)}
    for x, cx in amplitudes.items():
        add_at(v_input, (x, 0), cx)
        add_at(v_input, (0, x), cx.conj())
        for y, cy in amplitudes.items(): add_at(w_input, (x, y), cx*cy.conj())
    V, W = channel(v_input, t), channel(w_input, t)
    lam = [a**(4-h)*b**h for h in range(5)]
    ee = [1 << i for i in range(4)]
    rest = [k for k in range(16) if wt(k) >= 2]
    A = W[0][0] + sum((V[k][0].conj()*V[k][0]/(lam[0]-lam[wt(k)]) for k in rest), Z)
    M = [[W[ee[i]][ee[j]] + sum((V[ee[i]][k]*V[k][ee[j]]/(lam[1]-lam[wt(k)]) for k in rest), Z)
          for j in range(4)] for i in range(4)]

    c = [[Z for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(i+1, 4): c[i][j] = c[j][i] = amplitudes.get(ee[i] | ee[j], Z)
    gamma = [[sum((c[i][k]*c[j][k].conj() for k in range(4)), Z) for j in range(4)] for i in range(4)]
    n = [gamma[i][i].r for i in range(4)]
    g = [amplitudes.get(15 ^ ee[i], Z) for i in range(4)]
    w2 = sum((amplitudes.get(k, Z).norm2() for k in range(16) if wt(k) == 2), F(0))
    w3 = sum((z.norm2() for z in g), F(0))
    w4 = amplitudes.get(15, Z).norm2()
    EA = -a*a*t*(1-t*t)*w2 + (-a*t*d3+a*t**5/d3)*w3 + (-t*d4+t**7/d4)*w4
    assert A == EA, (tag, 'A', A, EA)
    expected = [[Z for _ in range(4)] for _ in range(4)]
    wrong_g = [[Z for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            h2 = G(-a*b*t*(1-t*t)*(w2-n[i])) if i == j else a*b*t*t*(1+t)*gamma[i][j]
            diag3 = -a*a*b*t*w3-b*b*t*(1+t)*g[i].norm2() if i == j else 0
            coeff3 = t*t*b*b+t**5*b/d3
            h3 = diag3+coeff3*g[i].conj()*g[j]
            h4 = -a*b*t*w4 if i == j else 0
            expected[i][j] = h2+h3+h4
            wrong_g[i][j] = h2+diag3+coeff3*g[i]*g[j].conj()+h4
            assert M[i][j] == expected[i][j], (tag, i, j, M[i][j], expected[i][j])
    if tag == 'complex_weight3':
        assert V[ee[1]][15] == b*t**3*g[1].conj() and V[ee[1]][15] != b*t**3*g[1]
        assert any(M[i][j] != wrong_g[i][j] for i in range(4) for j in range(4)), 'wrong conjugation not detected'

    scale = F(16, 1)/t
    VH = [[V[i][j]*scale for j in range(16)] for i in range(16)]
    dd = [(16*lam[wt(i)]-1)/t for i in range(16)]
    S = zero_matrix(); DS = zero_matrix()
    for i in range(16):
        for j in range(16):
            if block(i) != block(j):
                S[i][j] = -VH[i][j]/(dd[i]-dd[j])
                DS[i][j] = (dd[i]-dd[j])*S[i][j]
    first, second = comm(VH, S), comm(DS, S)
    Q = [[scale*W[i][j] + first[i][j]+second[i][j]/2 for j in range(16)] for i in range(16)]
    assert Q[0][0] == scale*A, (tag, 'bridge A')
    for i in range(4):
        for j in range(4): assert Q[ee[i]][ee[j]] == scale*M[i][j], (tag, 'bridge M', i, j)
    if tag == 'complex_weight2':
        Qbad = scale*W[0][0]+first[0][0]
        assert Qbad != scale*A, 'omitting half-double-commutator not detected'
    bound3 = (-a*t*d3+a*t**5/d3)-2*a*a*b*t+b*b*t*t+b*t**5/d3
    polynomial = -t*(1-t)*(15+24*t+38*t*t+32*t**3+3*t**4)/(32*d3)
    assert bound3 == polynomial, (tag, 'weight3 identity')

c = F(1,142); r = F(19,80); delta = 2*r*r
v, s, w, bs, q, o, g, e = F(4,25), F(2,25), F(204,25), F(1,25), F(41,5), F(21,5), F(199,200), F(137,100)
assert v*v-512*c*c == F(656,3150625) > 0
assert F(81,20)-(4+6*c+4*c*c+c**3) == F(108057,14316440) > 0
assert bs-3*v*s == F(1,625) and q-(w+3*v*s) == F(1,625)
assert o-(4+v+3*v*s) == F(1,625)
assert F(26,25)-1/(1-2*r*s) == F(6,12025) > 0
cubic = F(26,25)*(F(81,20)*(2*s)**3/6+v*(2*s)**2/2+w*(2*s))
assert cubic == F(2661776,1953125) and e-cubic == F(56021,7812500) > 0
assert 2-2*(r*v+r*r*q)-g == F(63,16000) > 0
budget = 3*e*r+3*bs*r*r+3*o*o*r*r/g
assert budget == F(126815937,31840000)
assert 4-budget == F(544063,31840000) > F(16,2000)
assert delta-16*c == F(31,227200) > 0
assert 441-(429+78*delta) == F(5121,1600) > 0
assert 1-39*c/20 == F(2801,2840) > 0
assert F(15,32)*(1-c)-F(1,4) == F(979,4544) > 0
assert 1-2*c**6-F(1,4) == F(3074406814103,4099209085472) > 0
assert (5+142*delta)**2 > 429+78*delta, 'far lower-bound at c failed'
# Intended-reason negatives: using 1/141 fails the same far-region certificate;
# using tube radius 1/4 breaks both stated separation and remainder budgets.
assert (5+141*delta)**2 < 429+78*delta
r_bad = F(1,4)
assert 2-2*(r_bad*v+r_bad*r_bad*q)-g < 0
assert 3*e*r_bad+3*bs*r_bad*r_bad+3*o*o*r_bad*r_bad/g > 4

examples = [
    ('complex_weight2', {3:G(F(3,5)), 5:G(0,F(4,5))}),
    ('complex_weight3', {14:G(F(3,5)), 13:G(0,F(4,5))}),
    ('weight4', {15:G(1)}),
    ('mixed_weight', {3:G(F(1,3)), 14:G(0,F(2,3)), 15:G(F(2,3))}),
]
for t in (c, F(1,2)):
    for tag, amplitudes in examples: experiment(t, amplitudes, tag)

# Actual complex density and rank-three projector; check reflection with the
# transformed, not the unchanged, projector at the new endpoint.
psi = {0:G(F(3,5)), 14:G(0,F(4,5))}
rho = {(i,j): x*y.conj() for i,x in psi.items() for j,y in psi.items()}
Q = zero_matrix()
for (i,j), value in rho.items(): Q[i][j] = value
Q[1][1], Q[2][2] = G(1), G(1)
assert matmul(Q,Q) == Q and sum((Q[i][i] for i in range(16)), Z) == 3
assert all(Q[i][j] == Q[j][i].conj() for i in range(16) for j in range(16))
Qtilde = [[((-1)**(wt(i)+wt(j)))*Q[15 ^ j][15 ^ i] for j in range(16)] for i in range(16)]
def pairing(A, B):
    return sum((A[j][i]*B[i][j] for i in range(16) for j in range(16)), Z)
pos, neg = channel(rho, c), channel(rho, -c)
positive, negative, reflected = pairing(Q,pos), pairing(Q,neg), pairing(Qtilde,pos)
a, b = (1+c)/2, (1-c)/2
reference = a**4+2*a**3*b
assert 16*reference == 3+8*c+6*c*c-c**4
assert not positive.i and not negative.i and positive.r <= reference and negative.r <= reference
assert negative == reflected and negative != positive
print('PASS exact complex state/projector reference bounds and t-sign reflection with transformed Q')
print('PASS intended negative: leaving Q unchanged under reflection gives a different trace')
print('PASS exact scalar endpoint slacks and 1/142 far/tube budgets')
print('PASS eight exact complex/mixed matrix-unit Hessian and commutator-bridge instances (t=1/142,1/2)')
print('PASS intended negatives: wrong complex conjugation, missing half-double-commutator, 1/141 far certificate, radius 1/4 gap and remainder')
print('LIMIT finite controls do not establish universal theorem')
