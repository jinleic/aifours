#!/usr/bin/env python3
"""Reviewer-owned exact finite controls; Gaussian integers and rational scalars only."""
from fractions import Fraction as Q
from itertools import combinations

Z = (0, 0)
ONE = (1, 0)
IUNIT = (0, 1)

def addz(a, b):
    return (a[0] + b[0], a[1] + b[1])

def negz(a):
    return (-a[0], -a[1])

def mulz(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def conjz(a):
    return (a[0], -a[1])

def put(m, key, val):
    v = addz(m.get(key, Z), val)
    if v == Z:
        m.pop(key, None)
    else:
        m[key] = v

def summ(*ms):
    r = {}
    for m in ms:
        for k, v in m.items():
            put(r, k, v)
    return r

def scale(m, n):
    return {k: (v[0]*n, v[1]*n) for k, v in m.items() if n and v != Z}

def dagger(m):
    return {(j, i): conjz(v) for (i, j), v in m.items()}

def conjugate(m):
    return {k: conjz(v) for k, v in m.items()}

def eye(n):
    return {(i, i): ONE for i in range(n)}

def mm(a, b):
    byrow = {}
    for (j, k), v in b.items():
        byrow.setdefault(j, []).append((k, v))
    r = {}
    for (i, j), v in a.items():
        for k, w in byrow.get(j, ()):
            put(r, (i, k), mulz(v, w))
    return r

def kron(a, b, nb):
    r = {}
    for (i, j), v in a.items():
        for (p, q), w in b.items():
            put(r, (i*nb+p, j*nb+q), mulz(v, w))
    return r

def outer(v, w=None):
    if w is None:
        w = v
    return {(i, j): mulz(a, conjz(b)) for i, a in v.items() for j, b in w.items() if mulz(a, conjz(b)) != Z}

def matvec(a, v):
    r = {}
    for (i, j), x in a.items():
        if j in v:
            put(r, i, mulz(x, v[j]))
    return r

def inner(v, w):
    s = Z
    for i, x in v.items():
        s = addz(s, mulz(conjz(x), w.get(i, Z)))
    return s

def traceprod(a, b):
    s = Z
    for (i, j), x in a.items():
        s = addz(s, mulz(x, b.get((j, i), Z)))
    return s

def pt_a(a, d):
    return {(k*d+j, i*d+q): v for (row, col), v in a.items() for i, j in [divmod(row, d)] for k, q in [divmod(col, d)]}

def pt_b(a, d):
    return {(i*d+q, k*d+j): v for (row, col), v in a.items() for i, j in [divmod(row, d)] for k, q in [divmod(col, d)]}

def swap(d):
    return {(i*d+j, j*d+i): ONE for i in range(d) for j in range(d)}

def om(d):
    return {i*d+i: ONE for i in range(d)}

def vec(m, d):
    return {i*d+j: v for (i, j), v in m.items()}

def skew(d, phases=None):
    phases = phases or [ONE]*(d//2)
    m = {}
    for i, z in enumerate(phases):
        m[(2*i, 2*i+1)] = z
        m[(2*i+1, 2*i)] = negz(z)
    return m

def sandwich(a, x):
    return mm(mm(a, x), dagger(a))

def val(v, a):
    return inner(v, matvec(a, v))

def orientation_and_source():
    d = 4
    J = skew(d, [ONE, IUNIT])
    K = conjugate(J)
    assert mm(J, dagger(J)) == eye(d)
    assert J != K
    F, O, Id = swap(d), om(d), eye(d*d)
    j, j_wrong = vec(K, d), vec(J, d)
    rot = kron(eye(d), dagger(J), d)
    twist_j = kron(eye(d), J, d)
    assert matvec(rot, O) == j
    assert sandwich(rot, outer(O)) == outer(j)
    assert outer(j) != outer(j_wrong), 'wrong orientation must be detected at projector level'
    assert sandwich(rot, sandwich(twist_j, F)) == F
    assert matvec(F, j) == scale(j, -1)
    tw = kron(eye(d), conjugate(K), d)
    T = sandwich(tw, F)
    R = summ(Id, F, outer(j))
    assert pt_b(R, d) == summ(Id, outer(O), T)
    assert dagger(T) == T and mm(T, T) == Id
    assert mm(summ(Id, T), summ(Id, T)) == scale(summ(Id, T), 2)
    wrong_twist = sandwich(kron(eye(d), K, d), F)
    assert wrong_twist != T, 'wrong source twist must differ'
    bad = summ(Id, scale(F, -1), outer(j))
    bad_expect = val(O, pt_b(bad, d))
    assert bad_expect == (-d*d, 0), 'non-PPT negative must be witnessed by Omega'
    print('ORIENTATION/SOURCE: complex J!=conj(J), both Choi terms, PPT square factor; wrong projector and twist rejected; non-PPT Omega expectation', bad_expect[0])
    return d, F, j, R

def four_tests(d, l):
    K = skew(d)
    j, F = vec(K, d), swap(d)
    e1, e2 = 0, 2
    a = {e1*d+e1: ONE}
    b = {e1*d+e2: ONE, e2*d+e1: (-1, 0)}
    r = 2*(l//2)
    c = {}
    for i in range(r//2):
        c[(2*i)*d+2*i+1] = ONE
        c[(2*i+1)*d+2*i] = (-1, 0)
    v = {(2*i)*d+2*i+1: ONE for i in range(l)}
    for x, expected in zip([a,b,c,v], [(1,0),(-1,0),(-1,r),(0,l)]):
        n = inner(x, x)
        f = val(x, F)
        h = inner(j, x)
        assert n[1] == f[1] == 0
        actual = (Q(f[0], n[0]), Q(h[0]*h[0]+h[1]*h[1], n[0]))
        assert actual == expected, (d,l,actual,expected)
    # The matrix ranks are visible directly: 1, 2, r, l nonzero disjoint rows/columns.

def polygon(d, l):
    r = 2*(l//2)
    # Coefficients of d*u,d*v,d*w,d*x = constant + P*p + Q*q.
    z = [(1,-1,d-1),(1,-1,-d-1),(1,-1+d*r,-d-1),(1,-1+d*l,-1)]
    verts = set()
    excluded = 0
    for i,j in combinations(range(4), 2):
        c1,a1,b1 = z[i]
        c2,a2,b2 = z[j]
        det = a1*b2-a2*b1
        assert det
        p = Q(-c1*b2+c2*b1, det)
        q = Q(-a1*c2+a2*c1, det)
        if all(c+a*p+b*q >= 0 for c,a,b in z):
            verts.add((p,q))
        else:
            excluded += 1
    D, E = l*d+l-r-1, l*d-l-1
    expected = {(Q(1),Q(0)), (Q(0),Q(1,d+1)), (Q(-1,D),Q(l-r,D)), (Q(-1,E),Q(-l,E))}
    assert verts == expected and excluded == 2
    # For odd l, an explicit rank-l Y violates the C vertex, proving strict enclosure.
    if l % 2:
        j, F, Id = vec(skew(d), d), swap(d), eye(d*d)
        Cnum = summ(scale(Id,l), scale(outer(j),-1), scale(F,l-r))
        Y = {}
        for i in range((l-1)//2):
            Y[(2*i)*d+2*i+1] = ONE
            Y[(2*i+1)*d+2*i] = (-1,0)
        i = (l-1)//2
        Y[(2*i)*d+2*i+1] = ONE
        assert val(Y,Cnum) == (-(l-1),0)
        # All l rows and l columns are distinct, so the coefficient rank is exactly l.
    else:
        j = vec(skew(d),d)
        Y = {(2*i)*d+2*i+1:ONE for i in range(l)}
        assert val(Y,summ(scale(eye(d*d),l),scale(outer(j),-1))) == Z


def compression(d, l, lam, sig):
    n = 2*l
    assert len(lam) == len(sig) == l and all(a*a+b*b == 25 for a,b in zip(lam,sig))
    assert sum(s != 0 for s in sig)*2 <= d-n
    Id = eye(n*d)
    F_E = {(i*d+j,j*d+i): ONE for i in range(n) for j in range(n)}
    u, w, j5, hs, blocked = [], [], {}, [], set()
    for i in range(l):
        a = {(2*i)*d+2*i+1: ONE, (2*i+1)*d+2*i: (-1,0)}
        u.append(a); w.append(lam[i]); j5 = summ(j5,scale(a,lam[i]))
    ci = 0
    for i in range(l):
        if sig[i] == 0:
            continue
        p, q = n+2*ci, n+2*ci+1
        ci += 1
        c = {(2*i)*d+p: ONE, (2*i+1)*d+q: (-1,0)}
        h = {(2*i)*d+q: ONE, (2*i+1)*d+p: ONE}
        u.append(c); w.append(sig[i]); j5 = summ(j5,scale(c,sig[i])); hs.append(h)
        blocked.update((row,col) for row in (2*i,2*i+1) for col in (p,q))
        assert matvec(pt_a(outer(h),d),c) == scale(c,-1)
    assert sum(t*t for t in w) == 25*l
    lhs = summ(scale(Id,25*l),scale(F_E,-25*l),scale(outer(j5),-1))
    P = {}
    first_nonzero = None
    for a,b in combinations(range(len(u)),2):
        v = summ(scale(u[b],w[a]),scale(u[a],-w[b]))
        t = outer(v)
        P = summ(P,t)
        if t and first_nonzero is None:
            first_nonzero = t
    assert first_nonzero is not None
    for a,b in combinations(range(n),2):
        if a//2 == b//2 and a%2 == 0 and b == a+1:
            continue
        v = {a*d+b:ONE,b*d+a:(-1,0)}
        P = summ(P,scale(outer(v),25*l))
    for row in range(n):
        for col in range(n,d):
            if (row,col) not in blocked:
                P = summ(P,{(row*d+col,row*d+col):(25*l,0)})
    Qmat = {}
    for h in hs:
        Qmat = summ(Qmat,scale(outer(h),25*l))
    rhs = summ(P,pt_a(Qmat,d))
    assert lhs == rhs, (d,l,lam,sig)
    # Intended reasons: exact missing Lagrange summand, and co-positive term without PT.
    assert summ(lhs,scale(summ(P,scale(first_nonzero,-1),pt_a(Qmat,d)),-1)) == first_nonzero
    if hs:
        assert summ(P,Qmat) != lhs, 'omitting partial transpose must fail'
    return len(lhs),len(hs)


def cp_closure(d, F, j, R):
    # Two CP Kraus operators per side, no trace-preserving assumption.
    unit = eye(d)
    M1 = summ(unit,{(0,1):(2,0),(2,0):IUNIT})
    M2 = {(0,1):ONE,(2,3):ONE,(3,0):IUNIT}
    N1 = summ(unit,{(1,0):ONE,(2,3):IUNIT})
    N2 = {(0,2):ONE,(3,1):(-1,0),(1,0):IUNIT}
    a = {0:ONE,1:IUNIT,3:ONE}
    b = {1:ONE,2:ONE,3:IUNIT}
    rankone = outer(a,b)
    general = summ(unit,{(0,1):ONE,(3,2):IUNIT})
    C = summ(scale(eye(d*d),2),scale(F,-2),scale(outer(j),-1))
    CPimage = {}
    for m in (M1,M2):
        for n in (N1,N2):
            CPimage = summ(CPimage,sandwich(kron(m,n,d),C))
    for side,(A,B) in enumerate([(rankone,general),(general,rankone)]):
        X = sandwich(kron(A,B,d),R)
        left = traceprod(CPimage,X)
        right = Z
        wrong = Z
        for m in (M1,M2):
            for n in (N1,N2):
                ma, nb = mm(dagger(m),A), mm(dagger(n),B)
                if side == 0:
                    assert ma == outer(matvec(dagger(m),a),b)
                else:
                    assert nb == outer(matvec(dagger(n),a),b)
                right = addz(right,traceprod(C,sandwich(kron(ma,nb,d),R)))
                wrong = addz(wrong,traceprod(C,sandwich(kron(mm(m,A),mm(n,B),d),R)))
        assert left == right and left[1] == 0 and left[0] >= 0
        assert wrong != right, 'using Kraus rather than adjoint must change this pairing'
        print('CP closure rank-one side',side,'pairing',left[0],'wrong-adjoint pairing',wrong[0])


def pairing_and_endpoints(d,F,j,R):
    W = summ(scale(eye(d*d),2),scale(F,-2),scale(outer(j),-1))
    assert traceprod(W,R) == (d*(4-d),0)
    # Use canonical d=6 for the strict mixture endpoint 1/28.
    d=6; F=swap(d); j=vec(skew(d),d); R=summ(eye(d*d),F,outer(j))
    W=summ(scale(eye(d*d),2),scale(F,-2),scale(outer(j),-1))
    E=2*d-2-1
    bh=Q(traceprod(W,R)[0],E)
    ident=Q(traceprod(outer(j),R)[0])
    assert bh == Q(-4,3) and ident == 36
    for x,sgn in [(Q(0),-1),(Q(1,56),-1),(Q(1,28),0),(Q(1,14),1)]:
        z=(1-x)*bh+x*ident
        assert (z>0)-(z<0) == sgn
    print('MIXTURE: d=6,k=2 strict cutoff 1/28; endpoint zero, above positive')


d,F,j,R = orientation_and_source()
for d0,l0 in [(4,2),(6,2),(6,3),(8,3),(8,4),(10,3),(12,5)]:
    four_tests(d0,l0)
    polygon(d0,l0)
print('FOUR TESTS/POLYGON: 7 exact cases, 2 excluded intersections each; odd C has explicit rank-l negative')
for args in [(4,2,[5,5],[0,0]),(6,2,[3,5],[4,0]),(8,2,[3,0],[4,5]),(6,3,[5,5,5],[0,0,0]),(8,3,[3,5,5],[4,0,0]),(10,3,[0,3,5],[5,4,0]),(8,4,[5,5,5,5],[0,0,0,0]),(10,4,[0,5,5,5],[5,0,0,0])]:
    nn, defects = compression(*args)
    print('COMPRESSION d,l=',args[:2],'lhs nonzero entries=',nn,'defects=',defects,'exact')
cp_closure(d,F,j,R)
pairing_and_endpoints(d,F,j,R)
print('ALL CONTROLS PASS')
