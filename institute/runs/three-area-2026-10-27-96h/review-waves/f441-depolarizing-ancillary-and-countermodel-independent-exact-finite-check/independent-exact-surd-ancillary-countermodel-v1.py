import time
from fractions import Fraction as F

STOP = time.monotonic() + 50

def tick():
    if time.monotonic() > STOP:
        raise RuntimeError('time cap: NOT CERTIFIED')

class ExactFailure(Exception):
    pass

def need(ok, tag):
    if not ok:
        raise ExactFailure(tag)

class E:
    __slots__ = ('a', 'b', 'c', 'd')
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a, self.b, self.c, self.d = map(F, (a, b, c, d))
    def __add__(self, x):
        x = e(x)
        return E(self.a+x.a, self.b+x.b, self.c+x.c, self.d+x.d)
    __radd__ = __add__
    def __neg__(self):
        return E(-self.a, -self.b, -self.c, -self.d)
    def __sub__(self, x):
        return self + (-e(x))
    def __rsub__(self, x):
        return e(x) + (-self)
    def __mul__(self, x):
        x = e(x)
        a,b,c,d = self.a,self.b,self.c,self.d
        u,v,w,z = x.a,x.b,x.c,x.d
        return E(a*u+3*b*v-c*w-3*d*z,
                 a*v+b*u-c*z-d*w,
                 a*w+3*b*z+c*u+3*d*v,
                 a*z+b*w+c*v+d*u)
    __rmul__ = __mul__
    def conj(self):
        return E(self.a, self.b, -self.c, -self.d)
    def __truediv__(self, x):
        x = e(x)
        n = x*x.conj()
        den = n.a*n.a - 3*n.b*n.b
        if not den:
            raise ZeroDivisionError('exact field division by zero')
        return self*x.conj()*E(n.a/den, -n.b/den)
    def __rtruediv__(self, x):
        return e(x)/self
    def __eq__(self, x):
        x = e(x)
        return (self.a,self.b,self.c,self.d) == (x.a,x.b,x.c,x.d)
    def __bool__(self):
        return bool(self.a or self.b or self.c or self.d)

def e(x):
    return x if isinstance(x, E) else E(x)

def sign(x):
    x = e(x)
    need(not x.c and not x.d, 'nonreal comparison')
    a,b = x.a,x.b
    sa = (a > 0) - (a < 0)
    sb = (b > 0) - (b < 0)
    if not b:
        return sa
    if not a:
        return sb
    if sa == sb:
        return sa
    z = a*a - 3*b*b
    return sa*((z > 0) - (z < 0))

def zero(r, c=None):
    c = r if c is None else c
    return [[E() for j in range(c)] for i in range(r)]

def eye(n):
    A = zero(n)
    for i in range(n):
        A[i][i] = E(1)
    return A

def diag(xs):
    A = zero(len(xs))
    for i,x in enumerate(xs):
        A[i][i] = e(x)
    return A

def unit(n, j):
    return [E(int(i == j)) for i in range(n)]

def matrix_unit(n, i, j):
    A = zero(n)
    A[i][j] = E(1)
    return A

def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]

def add(A, B):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(A,B)]

def scale(x, A):
    x = e(x)
    return [[x*y for y in row] for row in A]

def sub(A, B):
    return add(A, scale(-1, B))

def mm(A, B):
    tick()
    C = zero(len(A), len(B[0]))
    for i in range(len(A)):
        for k in range(len(B)):
            if A[i][k]:
                for j in range(len(B[0])):
                    C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C

def tr(A):
    return sum((A[i][i] for i in range(len(A))), E())

def outer(v):
    v = [e(x) for x in v]
    return [[x*y.conj() for y in v] for x in v]

def act(A, v):
    return [sum((A[i][j]*e(v[j]) for j in range(len(v))), E()) for i in range(len(A))]

def inner(v, w):
    return sum((e(x).conj()*e(y) for x,y in zip(v,w)), E())

def value(v, A):
    return inner(v, act(A,v))

def kron(A, B):
    return [[A[i][j]*B[r][s] for j in range(len(A[0])) for s in range(len(B[0]))]
            for i in range(len(A)) for r in range(len(B))]

def sum_mats(items):
    C = zero(len(items[0]), len(items[0][0]))
    for A in items:
        C = add(C,A)
    return C

def conjugate(U, A):
    return mm(mm(U,A),dag(U))

def psd(A):
    tick()
    n = len(A)
    if any(len(row) != n for row in A) or A != dag(A):
        return False
    H = [row[:] for row in A]
    for k in range(n):
        tick()
        q = H[k][k]
        if q.c or q.d or sign(q) < 0:
            return False
        if not q:
            if any(H[k][j] for j in range(k+1,n)):
                return False
            continue
        for i in range(k+1,n):
            for j in range(k+1,n):
                H[i][j] = H[i][j] - H[i][k]*H[k][j]/q
    return True

def state(A, tag):
    need(A == dag(A) and tr(A) == 1 and psd(A), tag)

def projector(A, rank, tag):
    need(A == dag(A) and mm(A,A) == A and tr(A) == rank and psd(A), tag)

def marginal_a(A, a, d):
    return [[sum((A[i*d+r][j*d+r] for r in range(d)), E()) for j in range(a)] for i in range(a)]

def marginal_b(A, a, d):
    return [[sum((A[i*d+r][i*d+s] for i in range(a)), E()) for s in range(d)] for r in range(d)]

def conditional(A, a, d, i):
    return [[A[i*d+r][i*d+s] for s in range(d)] for r in range(d)]

def dep_unit(d, i, j, p):
    p = F(p)
    A = scale(1-p, matrix_unit(d,i,j))
    return add(A, scale(p/d,eye(d))) if i == j else A

def apply_leg(A, a, d, p, leg):
    tick()
    need(leg in (0,1), 'invalid tensor leg')
    n = a*d
    need(len(A) == n and all(len(row) == n for row in A), 'tensor shape')
    dim = a if leg == 0 else d
    maps = {(i,j): dep_unit(dim,i,j,p) for i in range(dim) for j in range(dim)}
    C = zero(n)
    for i in range(a):
        tick()
        for j in range(a):
            for r in range(d):
                for s in range(d):
                    c = A[i*d+r][j*d+s]
                    if not c:
                        continue
                    if leg == 0:
                        B = maps[i,j]
                        for u in range(a):
                            for v in range(a):
                                C[u*d+r][v*d+s] = C[u*d+r][v*d+s] + c*B[u][v]
                    else:
                        B = maps[r,s]
                        for u in range(d):
                            for v in range(d):
                                C[i*d+u][j*d+v] = C[i*d+u][j*d+v] + c*B[u][v]
    return C

def psi(d):
    if d == 2:
        return [E(F(3,5)), E(0,0,F(4,5))]
    need(d == 3, 'unsupported example dimension')
    return [E(F(1,3)), E(0,0,F(2,3)), E(F(2,3))]

def physical_q(d, p):
    p = F(p)
    P = outer(psi(d))
    projector(P,1,'single-input projector')
    B = apply_leg(P,1,d,p,1)
    b = p/d
    alpha = 1-p+b
    expected = add(scale(alpha,P),scale(b,sub(eye(d),P)))
    need(B == expected, 'physical pure-output decomposition')
    state(B,'physical pure-output state')
    return sorted([alpha]+[b]*(d-1), reverse=True)

def majorized(xs, ys):
    xs,ys = sorted(xs,reverse=True),sorted(ys,reverse=True)
    return len(xs) == len(ys) and sum(xs) == sum(ys) and all(sum(xs[:k]) <= sum(ys[:k]) for k in range(1,len(xs)+1))

def check_choi(d, p):
    p = F(p)
    need(0 <= p <= F(d*d,d*d-1), 'CP parameter interval')
    w = [E(int(i == j)) for i in range(d) for j in range(d)]
    J = scale(F(1,d),outer(w))
    projector(J,1,'maximally entangled projector')
    C = apply_leg(J,d,d,p,1)
    need(C == add(scale(1-p,J),scale(p/(d*d),eye(d*d))), 'Choi matrix-unit identity')
    need(p/(d*d) >= 0 and 1-p+p/(d*d) >= 0, 'Choi scalar eigenvalues')
    state(C,'exact Choi positivity')

def prefix_certificates(A, d, p, q):
    p = F(p)
    n = 2*d
    state(A,'ancillary input density')
    MA = marginal_a(A,2,d)
    state(MA,'ancillary marginal density')
    need(psd(sub(eye(2),MA)), 'marginal upper bound')
    R = apply_leg(A,2,d,p,1)
    t,b = 1-p,p/d
    need(R == add(scale(t,A),scale(b,kron(MA,eye(d)))), 'ancillary matrix-unit map')
    state(R,'ancillary output density')
    ref = q+[F(0)]*(n-d)
    small_C = scale(t,A) if t >= 0 else zero(n)
    for k in range(1,n+1):
        tick()
        C,mu = (small_C,b) if k < d else (R,F(0))
        slack = sub(add(scale(mu,eye(n)),C),R)
        need(psd(C) and psd(slack), 'exact Ky Fan PSD certificate')
        need(E(k*mu)+tr(C) == E(sum(ref[:k])), 'sorted reference prefix')

def check_examples():
    count = 0
    for d,params in ((2,(F(0),F(1,2),F(1),F(7,6),F(4,3))),
                     (3,(F(0),F(1,2),F(1),F(17,16),F(9,8)))):
        P = outer(psi(d))
        product = kron(outer(unit(2,0)),P)
        other = kron(outer(unit(2,1)),P)
        v = [E() for i in range(2*d)]
        if d == 2:
            v[0],v[3] = E(F(3,5)),E(0,0,F(4,5))
        else:
            v[0],v[4],v[5] = E(F(1,3)),E(0,0,F(2,3)),E(F(2,3))
        entangled = outer(v)
        projector(entangled,1,'entangled input projector')
        mixed = add(scale(F(2,5),entangled),scale(F(3,5),other))
        state(mixed,'mixed complex input density')
        need(sign(E(1)-tr(mm(mixed,mixed))) > 0, 'genuinely mixed input')
        need(any(x.c or x.d for row in mixed for x in row), 'complex input coverage')
        for p in params:
            check_choi(d,p)
            q = physical_q(d,p)
            for A in (product,entangled,mixed):
                prefix_certificates(A,d,p,q)
                count += 1
    need(count == 30,'finite case count')
    return count

BAD = 0

def rejects(label, reason, f):
    global BAD
    try:
        f()
    except ExactFailure as exc:
        need(str(exc) == reason, 'wrong mutation reason: '+label)
        BAD += 1
    else:
        raise ExactFailure('mutation not rejected: '+label)

s = E(0,1)
ii = E(0,0,1)
need(s*s == 3 and ii*ii == -1, 'field multiplication controls')
z = E(2,1,1,1)
need(z/z == 1 and s.conj() == s and ii.conj() == -ii, 'field inverse/conjugation controls')
need(sign(E(2)-s) > 0 and sign(E(1)-s) < 0 and sign(s-E(2)) < 0 and sign(s-E(1)) > 0, 'exact surd sign controls')
I2 = eye(2)
Z = diag([1,-1])
X = [[E(),E(1)],[E(1),E()]]
US = [I2,Z,X,mm(X,Z)]
for U in US:
    need(mm(U,dag(U)) == I2 and mm(dag(U),U) == I2, 'Pauli unitarity')
weights = [F(5,8),F(1,8),F(1,8),F(1,8)]

def check_weights(w):
    tag = 'Pauli weight/channel identity'
    need(sum(w) == 1 and all(x >= 0 for x in w), tag)
    for i in range(2):
        for j in range(2):
            A = matrix_unit(2,i,j)
            B = sum_mats([scale(w[k],conjugate(US[k],A)) for k in range(4)])
            need(B == dep_unit(2,i,j,F(1,2)), tag)
    need(all(w[j] <= w[i] for i in (0,1) for j in (2,3)), tag)
    need([sum(w[:2]),sum(w[2:])] == [F(3,4),F(1,4)], tag)

check_weights(weights)
e0 = unit(4,0)
v = [E(),s/2,E(1)/2,E()]
P0,V = outer(e0),outer(v)
projector(P0,1,'first spectral projector')
projector(V,1,'second spectral projector')
need(mm(P0,V) == zero(4) and inner(e0,v) == 0, 'orthogonal spectral decomposition')
Q = add(P0,V)
R = add(scale(F(2,3),P0),scale(F(1,3),V))
projector(Q,2,'common rank-two projector')
state(R,'countermodel state')
R_exp = diag([F(2,3),F(1,4),F(1,12),0])
R_exp[1][2] = R_exp[2][1] = s/12
need(R == R_exp,'actual countermodel entries')
q = physical_q(2,F(1,2))
need(q == [F(3,4),F(1,4)], 'physical qubit reference')
need(majorized([F(2,3),F(1,3),F(0),F(0)],q+[F(0),F(0)]), 'global spectral bound')
products = sorted([x*y for x in q for y in q],reverse=True)
need(products == [F(9,16),F(3,16),F(3,16),F(1,16)], 'sorted physical tensor reference')
sigma = diag([F(3,4),F(1,4)])

def check_marginal(S):
    need(marginal_b(R,2,2) == S,'second-system marginal')

check_marginal(sigma)
need(marginal_a(R,2,2) == diag([F(11,12),F(1,12)]), 'first-system marginal')
TABLE = [[F(2,3),F(2,3),F(1,12),F(1,12)],
         [F(1,3),F(1,12),F(1,6),F(1,6)]]

def make_orbit(leg=0, correct_adjoint=True):
    out = []
    for U in US:
        W = kron(U,I2) if leg == 0 else kron(I2,U)
        out.append(mm(mm(W,R),dag(W) if correct_adjoint else W))
    return out

def check_orbit(O):
    for B in O:
        state(B,'orbit density/conjugation')
    S = sum_mats(O)
    need(S == scale(2,kron(I2,sigma)), 'twirl leg/marginal')
    need(psd(sub(scale(F(3,2),eye(4)),S)), 'sharpened row bound')
    for r,h in enumerate((e0,v)):
        for j,B in enumerate(O):
            need(value(h,B) == TABLE[r][j], 'actual orbit table')

def check_consumer(C, O):
    projector(C,2,'consumer projector validity')
    for j,B in enumerate(O):
        need(tr(mm(C,B)) == TABLE[0][j]+TABLE[1][j], 'same-projector consumer')

O = make_orbit()
check_orbit(O)
check_consumer(Q,O)
for U in US:
    W = kron(U,I2)
    need(mm(dag(W),W) == eye(4), 'orbit spectral invariance')
Y = sum_mats([scale(weights[j],O[j]) for j in range(4)])
need(Y == apply_leg(R,2,2,F(1,2),0), 'physical first-leg output map')
Y_exp = diag([25,9,11,3])
Y_exp[1][2] = Y_exp[2][1] = 2*s
Y_exp = scale(F(1,48),Y_exp)
need(Y == Y_exp,'actual Y entries')
state(Y,'actual Y density')
need(tr(mm(Q,Y)) == E(F(25,32)), 'same-Q output witness')
need(F(25,32) > sum(products[:2]) == F(3,4), 'strict product-prefix violation')
B = scale(48,[[Y[1][1],Y[1][2]],[Y[2][1],Y[2][2]]])
need(tr(B) == 20 and B[0][0]*B[1][1]-B[0][1]*B[1][0] == 87, 'exact Y spectral polynomial')
need(mm(B,B) == sub(scale(20,B),scale(87,I2)), 'exact Y block characteristic identity')
need(1 < 13 < 49 and 13 < 225, 'Y root ordering and strict prefix gap')
C1 = conditional(R,2,2,1)
w1 = tr(C1)
need(C1 == diag([F(1,12),0]) and w1 == E(F(1,12)), 'actual conditional block')
need(w1*q[0] == E(F(1,16)), 'conditional pure-output cap')
need(sign(value(unit(2,0),C1)-w1*q[0]) > 0, 'conditional strict violation')

def check_conditional(C, w):
    need(C == conditional(R,2,2,1), 'conditional block normalization')
    need(e(w) == tr(C), 'conditional trace normalization')

def require_admissible():
    C = conditional(R,2,2,1)
    w = tr(C)
    check_conditional(C,w)
    need(psd(sub(scale(w*q[0],I2),C)), 'conditional pure-output admissibility')

check_conditional(C1,w1)
bell_raw = [E(1),E(),E(),E(1)]
bell_vectors = [act(kron(I2,U),bell_raw) for U in US]
for i in range(4):
    for j in range(4):
        need(inner(bell_vectors[i],bell_vectors[j]) == E(2 if i == j else 0), 'Bell orbit orthogonality')
bell_projectors = [scale(F(1,2),outer(h)) for h in bell_vectors]
for P in bell_projectors:
    projector(P,1,'Bell orbit projector')
need(sum_mats(bell_projectors) == eye(4), 'Bell orbit full dimension')
bell_out = sum_mats([scale(weights[j],bell_projectors[j]) for j in range(4)])
need(bell_out == apply_leg(bell_projectors[0],2,2,F(1,2),1), 'Bell physical ancillary map')
need(majorized(weights,q+[F(0),F(0)]), 'Bell non-refutation spectral bound')

def wrong_negative_reference():
    p = F(4,3)
    A = apply_leg(outer(psi(2)),1,2,p,1)
    h = [E(F(4,5)),E(0,0,F(-3,5))]
    need(inner(h,h) == 1 and inner(psi(2),h) == 0, 'negative witness normalization')
    alpha = 1-p+p/2
    need(sign(E(alpha)-value(h,A)) >= 0, 'negative sorted prefix')

rejects('wrong Pauli weight','Pauli weight/channel identity',
        lambda: check_weights([F(1,8),F(5,8),F(1,8),F(1,8)]))
rejects('missing adjoint','orbit density/conjugation',
        lambda: check_orbit(make_orbit(0,False)))
rejects('wrong tensor leg','twirl leg/marginal',
        lambda: check_orbit(make_orbit(1,True)))
rejects('stale projector','same-projector consumer',
        lambda: check_consumer(add(P0,outer(unit(4,1))),O))
rejects('independent projector','same-projector consumer',
        lambda: check_consumer(add(P0,outer(unit(4,3))),O))
rejects('wrong marginal','second-system marginal',
        lambda: check_marginal(diag([F(1,4),F(3,4)])))
rejects('normalized block substituted for raw block','conditional block normalization',
        lambda: check_conditional(scale(12,C1),w1))
rejects('conditional probability discarded','conditional trace normalization',
        lambda: check_conditional(C1,E(1)))
rejects('unsorted negative branch','negative sorted prefix',wrong_negative_reference)
rejects('false acceptance as Omega output','conditional pure-output admissibility',require_admissible)
need(BAD == 10,'mutation count')
CASES = check_examples()
tick()
print('COUNTERMODEL: exact Pauli orbit, common Q, marginal and Y identities certified')
print('CONSUMER: Tr(QY)=25/32 > K2(q tensor q)=3/4')
print('ADMISSIBILITY: C1 trace=1/12; largest eigenvalue=1/12 > 1/16; rejected')
print('ANCILLARY: '+str(CASES)+' finite cases; d=2,3; positive, negative, endpoints; complex mixed inputs')
print('CONTROLS: '+str(BAD)+' intended failures rejected')
print('RESULT: PASS (finite identities and certificates only)')
