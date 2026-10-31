from fractions import Fraction as F


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def zero(m, n):
    return [[F(0) for _ in range(n)] for _ in range(m)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def diag(xs):
    m = zero(len(xs), len(xs))
    for i, x in enumerate(xs):
        m[i][i] = F(x)
    return m


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def trans(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def direct(a, b):
    n, m = len(a), len(b)
    out = zero(n + m, n + m)
    for i in range(n):
        for j in range(n):
            out[i][j] = a[i][j]
    for i in range(m):
        for j in range(m):
            out[n + i][n + j] = b[i][j]
    return out


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def norm2(v):
    return sum((x * x for x in v), F(0))


def f2(a):
    return sum((x * x for row in a for x in row), F(0))


def mv(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def dot(u, v):
    return sum((x * y for x, y in zip(u, v)), F(0))


def xsum(a, b):
    return add(kron(a, eye(len(b))), kron(eye(len(a)), b))


def rank(a):
    a = [row[:] for row in a]
    r = 0
    for c in range(len(a[0])):
        piv = next((i for i in range(r, len(a)) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def psd(a):
    assert a == trans(a)
    a = [row[:] for row in a]
    n = len(a)
    for k in range(n):
        p = a[k][k]
        if p < 0:
            return False
        if p == 0:
            if any(a[k][j] for j in range(k + 1, n)):
                return False
            continue
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] -= a[i][k] * a[k][j] / p
    return True


def permutation(weights, perm):
    n = len(weights)
    a = zero(n, n)
    for p in range(n):
        a[perm[p]][p] = F(weights[p])
    return a


def shift(weights):
    d = len(weights)
    return permutation(weights, [(i - 1) % d for i in range(d)])


def grade(a, b, k):
    d = len(a)
    out = zero(d, d)
    for i in range(d):
        out[(i - 1) % d][i] += a[i]
        out[i][i] += b[(k - i) % d]
    return out


def check(name, ok, detail=''):
    if not ok:
        raise AssertionError(name + ' ' + str(detail))
    print('PASS', name, detail)


# The row Cauchy--Schwarz coefficient sum, using unequal dimensions and cycles.
a, b = list(map(F, [1, 2, 0])), list(map(F, [2, 0, -1, 1]))
sigma, tau = [2, 0, 1], [1, 0, 3, 2]
si = [sigma.index(i) for i in range(3)]
ti = [tau.index(i) for i in range(4)]
ma = max(a[i] ** 2 + a[si[i]] ** 2 for i in range(3))
mb = max(b[i] ** 2 + b[ti[i]] ** 2 for i in range(4))
w = [F((7 * i) % 11 - 5, 3) for i in range(12)]
x = xsum(permutation(a, sigma), permutation(b, tau))
out = norm2(mv(x, w))
mid = sum(((a[p] ** 2 + a[si[p]] ** 2 + b[q] ** 2 + b[ti[q]] ** 2) * w[4*p+q] ** 2
           for p in range(3) for q in range(4)), F(0))
check('unequal-permutation-CS', out <= mid <= (ma + mb) * norm2(w), (out, mid, ma, mb))
check('strict-support-margin', ma <= sum(z*z for z in a) and mb < sum(z*z for z in b), (ma, mb))

# If predecessor coefficients are omitted, constructive interference breaks the alleged bound.
a, b = [F(1), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)]
w = [F(0)] * 16
w[0], w[4*3+1] = F(1), F(1)
out = norm2(mv(xsum(shift(a), shift(b)), w))
wrong = sum(((a[p]**2 + b[q]**2) * w[4*p+q]**2 for p in range(4) for q in range(4)), F(0))
check('negative-omit-incoming-weights', out > wrong, (out, wrong))

# Grade supports and exact ranks; two special grades have full squared Frobenius norm.
for d in (3, 4, 5):
    a, b = [F(0)] * d, [F(0)] * d
    a[0], b[1] = F(1), F(2)
    blocks = [grade(a, b, k) for k in range(d)]
    check('cyclic-grade-frob-d' + str(d), all(f2(g) == 5 for g in blocks))
    check('cyclic-two-equality-grades-d' + str(d), rank(blocks[0]) == rank(blocks[1]) == 1,
          [rank(g) for g in blocks])
    a = [F(1), F(2)] + [F(0)] * (d - 2)
    b = [F(0)] * d
    check('cyclic-two-same-shift-rank-d' + str(d), all(rank(grade(a, b, k)) == 2 for k in range(d)))
    a, b = [F(0)] * d, [F(0)] * d
    a[0], b[1], b[2] = F(1), F(2), F(3)
    check('cyclic-three-weights-rank-d' + str(d), all(rank(grade(a, b, k)) >= 2 for k in range(d)))
    b = [F(0)] * d
    check('cyclic-single-weight-rank-d' + str(d), all(rank(grade(a, b, k)) == 1 for k in range(d)))
    a = [F(0)] * d
    check('cyclic-zero-rank-d' + str(d), all(rank(grade(a, b, k)) == 0 for k in range(d)))
a = b = [F(1), F(1)]
blocks = [grade(a, b, k) for k in range(2)]
check('negative-d2-equality-extension', all(rank(g) == 1 and f2(g) == 4 for g in blocks),
      'each rank-one block has squared singular value 4; both shifts have two weights')

# Independent trace-zero lemma and its weighted-HS scalar identity.
u = [F(0), F(3,5), F(0), F(0)]
v = [F(16,25), F(12,25), F(0), F(0)]
t, q, r = norm2(u), norm2(v), dot(u, v)**2
delta = t*q-r
n1 = q*(t*t+r)/delta-r/(delta*(1+2*delta))
n2 = 1+t-(1+2*t*q-4*r)/(1+2*delta)
check('weighted-HS-projection-formula', t+q == 1 and delta > 0 and n1 == n2 and n1 <= t*(1+2*q), (n1, n2))
traceless_rank1 = zero(4, 4)
traceless_rank1[0][1] = F(1)
diag_a = diag([3, -1, -1, -1])
for name, A, sigma2, U, V in [
    ('independent-rank1', traceless_rank1, F(1), u, v),
    ('collinear-diagonal', diag_a, F(9), [F(3,5), F(0), F(0), F(0)], [F(4,5), F(0), F(0), F(0)]),
]:
    t, q = norm2(U), norm2(V)
    d = f2(A) - norm2(mv(A, U)) - norm2(mv(A, V))
    k = dot(V, mv(A, U))
    check('tracezero-lemma-' + name, tr(A) == 0 and t+q == 1 and d >= 0 and k*k <= t*(1+2*q)*d,
          (k*k, t*(1+2*q)*d))
    gap = 2*f2(A) - (norm2(mv(A,U)) + norm2(mv(A,V)) + k*k/(1+t) + sigma2)
    lower = f2(A)-sigma2+(1-2*t*q)*d/(1+t)
    check('dagger-remainder-' + name, gap >= lower >= 0, (gap, lower))
    beta = F(3,4)
    au, av = mv(A,U), mv(A,V)
    mixed = 2*(f2(A)+beta*beta) - (norm2([x+beta*y for x,y in zip(au,V)]) + norm2(av) + sigma2)
    lower_mixed = lower+(1+t)*(beta-k/(1+t))**2
    check('mixed-block-remainder-' + name, mixed >= lower_mixed >= 0, (mixed, lower_mixed))
A = diag([1, 0, 0, 0])
u, v = [F(3,5), F(0), F(0), F(0)], [F(4,5), F(0), F(0), F(0)]
t, q = norm2(u), norm2(v)
d = f2(A)-norm2(mv(A,u))-norm2(mv(A,v))
k = dot(v,mv(A,u))
check('negative-drop-tracezero-lemma', tr(A) != 0 and k*k > t*(1+2*q)*d, (k*k, d))

# Cross partial traces for two normalized pure vectors, including a product equality case.
for name, psi, phi in [
    ('product', [F(1)]+[F(0)]*7, [F(1)]+[F(0)]*7),
    ('entangled', [F(1,3),F(2,3),F(2,3),F(0),F(0),F(0),F(0),F(0)],
     [F(2,3),F(0),F(1,3),F(0),F(2,3),F(0),F(0),F(0)]),
]:
    P = [psi[2*i:2*i+2] for i in range(4)]
    Q = [phi[2*i:2*i+2] for i in range(4)]
    M, N = mul(P,trans(Q)), mul(trans(P),Q)
    c = dot(phi, psi)
    s1, s2 = f2(N), f2(M)
    M0, N0 = add(M,scale(-c/4,eye(4))), add(N,scale(-c/2,eye(2)))
    coefficient = f2(M0)+f2(N0)/2
    check('trace-removal-' + name,
          norm2(psi) == norm2(phi) == 1 and 1-s1-s2+c*c >= 0 and s1 <= 1 and s2 <= 1
          and coefficient == s2/2+(s1+s2-c*c)/2 and coefficient <= 1,
          (s1, s2, c, coefficient))

# Intended-reason counterexamples to either missing trace hypothesis.
A = diag([F(3,4),F(-1,4),F(-1,4),F(-1,4)])
T = diag([F(1,2),F(0)])
X = xsum(A,T)
rhs = f2(A)+2*f2(T)
lhs = norm2(mv(X,[F(1)]+[F(0)]*7))
check('negative-arbitrary-T', tr(A) == 0 and tr(T) != 0 and lhs == F(25,16) and rhs == F(5,4) and lhs > rhs, (lhs,rhs))
T0 = diag([F(1,4),F(-1,4)])
X0 = xsum(A,T0)
check('restricted-T-product-saturation', tr(A) == tr(T0) == 0 and norm2(mv(X0,[F(1)]+[F(0)]*7)) == f2(A)+2*f2(T0) == 1)
A1 = diag([1,0,0,0])
X1 = xsum(A1,T0)
check('negative-arbitrary-A', tr(A1) != 0 and tr(T0) == 0 and norm2(mv(X1,[F(1)]+[F(0)]*7)) > f2(A1)+2*f2(T0))

# A nonnormal square-normal 4x4 matrix, and exact PSD block certificates.
B1, B2 = mat([[0,1],[2,0]]), mat([[0,3],[0,0]])
B = direct(B1,B2)
Bsq = mul(B,B)
check('square-normal-nonnormal-example', tr(B1) == tr(B2) == 0 and mul(Bsq,trans(Bsq)) == mul(trans(Bsq),Bsq)
      and mul(B,trans(B)) != mul(trans(B),B))
for j, T in enumerate((B1,B2), 1):
    G = xsum(traceless_rank1,T)
    bound = f2(traceless_rank1)+2*f2(T)
    slack = add(scale(bound,eye(8)),scale(-1,mul(trans(G),G)))
    check('restricted-block-exact-psd-' + str(j), psd(slack), bound)
G = xsum(A,diag([F(1,2),0]))
wrong_slack = add(scale(f2(A)+2*F(1,4),eye(8)),scale(-1,mul(trans(G),G)))
check('negative-unrestricted-block-psd', not psd(wrong_slack))

# Exact moment expansion and mean-zero bound for diagonal fixtures.
A = diag([1,1,-1,-1])
B = diag([1,1,-1,-1])
X = xsum(A,B)
H = mul(trans(X),X)
a,b = f2(A),f2(B)
p,q = tr(mul(mul(trans(A),A),mul(trans(A),A))),tr(mul(mul(trans(B),B),mul(trans(B),B)))
z = tr(mul(A,A))*tr(mul(B,B))
actual = tr(mul(H,H))
check('fourth-moment-expansion', tr(H) == 4*(a+b) and actual == 4*(p+q)+4*a*b+2*z,
      (tr(H),actual,a,b,p,q,z))
check('negative-omit-z', actual != 4*(p+q)+4*a*b, (actual,4*(p+q)+4*a*b))
lambda_values = sorted([H[i][i] for i in range(16)],reverse=True)
top = lambda_values[0]+lambda_values[1]
variance = sum(((v-(a+b)/4)**2 for v in lambda_values),F(0))
check('variance-CS-and-strict-test', (top-(a+b)/2)**2 <= F(7,4)*variance
      and 14*(p+q)+7*z < 8*(a*a+b*b)+2*a*b and top < 2*(a+b),
      (top,variance,14*(p+q)+7*z,8*(a*a+b*b)+2*a*b))
check('tail-test-strict', (a-1)+(b-1) > 2, (a-1+b-1,F(2)))

# Both-squares-nonnormal weighted shifts near rank one, at ranks 2, 3, 4.
for n in (2,3,4):
    weights = [F(1,4)**i if i < n else F(0) for i in range(4)]
    A = shift(weights)
    Asq = mul(A,A)
    a = f2(A)
    p = sum((x**4 for x in weights),F(0))
    check('rank'+str(n)+'-nonnormal-squares-and-failed-spectral-tests',
          rank(A) == n and mul(Asq,trans(Asq)) != mul(trans(Asq),Asq)
          and 2*(a-1) < 2 and 28*p > 18*a*a and tr(Asq) == 0,
          (a,p,2*(a-1),28*p-18*a*a))

print('ALL EXACT CONTROLS COMPLETED')
