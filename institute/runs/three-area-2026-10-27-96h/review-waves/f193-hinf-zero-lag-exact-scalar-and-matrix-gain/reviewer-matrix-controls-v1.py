#!/usr/bin/env python3
"""Exact rational checks generated from explicit P,B,C, not author code."""
from fractions import Fraction as F
from itertools import product


class Rejected(Exception):
    pass


def check(ok, why):
    if not ok:
        raise Rejected(why)


def negative(name, why, fn):
    try:
        fn()
    except Rejected as e:
        check(str(e) == why, 'wrong-negative-reason')
        print('NEGATIVE', name, 'rejected:', why)
        return
    raise Rejected(name + '-incorrectly-accepted')


def mat(a):
    return [[F(x) for x in row] for row in a]


def tr(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def plus(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, c):
    return [[c*x for x in row] for row in a]


def minus(a, b):
    return plus(a, scale(b, -1))


def coeffs(p, b, c):
    p, b, c = map(mat, (p, b, c))
    check(all(x == 0 for row in mm(p, p) for x in row), 'P-not-square-zero')
    return mm(c, b), mm(mm(c, p), b)


def gram(a, d, u):
    aa = mm(tr(a), a)
    ad = plus(mm(tr(a), d), mm(tr(d), a))
    dd = mm(tr(d), d)
    return plus(plus(scale(aa, u), scale(ad, u*u/2)), scale(dd, u**3/3))


def sample_gram(a, d, s, n):
    m = len(a[0])
    out = [[F(0) for _ in range(m)] for _ in range(m)]
    for j in range(1, n+1):
        t = F(j, n)
        if t > s:
            h = plus(a, scale(d, t-s))
            out = plus(out, scale(mm(tr(h), h), F(1, n)))
    return out


def pulse_gram(a, d, e):
    aa = mm(tr(a), a)
    ad = plus(mm(tr(a), d), mm(tr(d), a))
    dd = mm(tr(d), d)
    t1 = (1-(1-e)**2)/(2*e)
    t2 = (1-(1-e)**3)/(6*e)
    t3 = (1-(1-e)**4)/(12*e)
    return plus(plus(scale(aa, t1), scale(ad, t2)), scale(dd, t3))


def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def kernel_error2(a, d, vec, s):
    h0 = [row[0] for row in mm(a, [[F(x)] for x in vec])]
    h1 = [row[0] for row in mm(d, [[F(x)] for x in vec])]
    norm0 = sum((x*x for x in h0), F(0))
    cross = sum((x*y for x, y in zip(h0, h1)), F(0))
    norm1 = sum((x*x for x in h1), F(0))
    exact = norm0*s + cross*s*s + norm1*s**3/3 + norm1*s*s*(1-s)
    bound = 2*(norm0+norm1)*s + norm1*s*s
    return exact, bound


def main():
    nil = [[0,1],[0,0]]
    a, d = coeffs(nil, [[1,0],[0,1]], [[1,0]])
    check(a == mat([[1,0]]) and d == mat([[0,1]]), 'nonnormal-kernel')
    check(gram(a,d,F(1)) == mat([[1,F(1,2)],[F(1,2),F(1,3)]]), 'nonnormal-gram')
    for s in (F(1,7), F(1,2), F(1)):
        gap = minus(gram(a,d,F(1)), gram(a,d,1-s))
        check(gap[0][0] == s and det2(gap) == s**4/12, 'nonnormal-gap')
    print('EXPLICIT nonnormal P,B,C: H(t)=[1,t]; exact Gram and positive gap verified')

    ar, dr = coeffs([[0,0],[0,0]], [[1,0],[0,1]], [[1,0]])
    check(gram(ar,dr,F(3,4)) == mat([[F(3,4),0],[0,0]]), 'invisible-gram')
    check(mm(ar,mat([[0],[1]])) == mat([[0]]) and mm(dr,mat([[0],[1]])) == mat([[0]]), 'invisible-kernel')
    ab, db = coeffs(nil, [[1,0],[0,0]], [[1,0]])
    check(gram(ab,db,F(3,4)) == gram(ar,dr,F(3,4)), 'rank-deficient-B-gram')
    print('EXPLICIT invisible direction and singular B: G(u)=diag(u,0), cT^2=1')
    negative('invisible-output-positive', 'invisible-kernel-zero',
             lambda: check(mm(ar,mat([[0],[1]])) != mat([[0]]), 'invisible-kernel-zero'))

    az, dz = coeffs(nil, [[1],[0]], [[0,1]])
    check(az == mat([[0]]) and dz == mat([[0]]) and gram(az,dz,F(1)) == mat([[0]]), 'zero-kernel')
    print('EXPLICIT zero mode: B=e1 and C=e2^T are nonzero but H(t)=0 and cT=0')
    negative('zero-threshold-included', 'strict-zero-threshold-false',
             lambda: check(F(0) < F(0), 'strict-zero-threshold-false'))

    al, dl = coeffs(nil, [[0],[1]], [[1,0]])
    check(al == mat([[0]]) and dl == mat([[1]]) and gram(al,dl,F(1)) == mat([[F(1,3)]]), 'delayed-observability')
    print('EXPLICIT delayed mode: CB=0, CPB=1, H(t)=t, cT^2=1/3')
    negative('CB-zero-implies-zero-output', 'CPB-makes-output-nonzero',
             lambda: check(gram(al,dl,F(1)) == mat([[0]]), 'CPB-makes-output-nonzero'))

    am, dm = coeffs(nil, [[1,1],[0,1]], [[1,0],[0,2]])
    gm = gram(am,dm,F(1))
    check(gm == mat([[1,F(3,2)],[F(3,2),F(19,3)]]), 'two-output-gram')
    char = lambda x: 12*x*x-88*x+49
    check(char(F(168,25)) < 0 < char(F(673,100)), 'two-output-spectral-bracket')
    for s in (F(1,7), F(1,2), F(1)):
        gap = minus(gm,gram(am,dm,1-s))
        check(gap[0][0] > 0 and det2(gap) > 0, 'two-output-strict-gap')
    print('EXPLICIT 2-input/2-output: G(1)=[[1,3/2],[3/2,19/3]],')
    print('  cT^2=(22+sqrt(337))/6 in (168/25,673/100); sampled gaps positive')
    for n in (4,8,16,32,64):
        errors=[]
        for s in (F(0),F(1,3),F(3,5),F(1)):
            diff=minus(sample_gram(am,dm,s,n),gram(am,dm,1-s))
            errors.extend(abs(x) for row in diff for x in row)
        check(max(errors) <= F(20,n), 'sampled-matrix-convergence')
        print('  N=',n,'max exact entry error=',max(errors),'<=20/N')
    for e in (F(1,2), F(1,4), F(1,8), F(1,16)):
        diff=minus(gm,pulse_gram(am,dm,e))
        check(max(abs(x) for row in diff for x in row) <= 20*e, 'matrix-pulse-limit')
        for s in (F(0), e/2, e):
            exact,bound=kernel_error2(am,dm,[1,1],s)
            check(0 <= exact <= bound and bound <= 100*e, 'matrix-burst-kernel-limit')
        print('  epsilon=',e,'pulse and burst-kernel rational bounds verified')
    negative('Gramian-is-identity', 'matrix-gram-not-identity',
             lambda: check(gm == mat([[1,0],[0,1]]), 'matrix-gram-not-identity'))
    print('DONE: exact finite matrix controls; universal and stochastic steps remain written arguments')


if __name__ == '__main__':
    main()
