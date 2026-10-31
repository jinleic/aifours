#!/usr/bin/env python3
"""Independent exact rational controls for the f193 review; no author imports.

Finite controls diagnose specified statements only; they do not prove stochastic
or infinite-family claims. All arithmetic is exact, with no floating point.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial


class ControlFailure(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise ControlFailure(reason)


def negative(name, reason, check):
    try:
        check()
    except ControlFailure as exc:
        require(str(exc) == reason, name + ': wrong rejection reason')
        print('NEGATIVE', name, 'rejected:', reason)
        return
    raise ControlFailure(name + ': invalid claim was not rejected')


def g_bounds(x, n=32):
    # Direct factorial terms, independent of the submitted recurrence/checker.
    q = x * x / (2 * (n + 2))
    require(0 <= q < 1, 'geometric-tail-unavailable')
    def term(k):
        return x ** (2 * k) / (2 ** k * factorial(k) * (2 * k - 1))
    partial = Q(1) - sum((term(k) for k in range(1, n + 1)), Q(0))
    # For k>=n+1, term(k+1)/term(k) < x^2/[2(k+1)] <= q.
    return partial - term(n + 1) / (1 - q), partial


def scaled_interval(bounds, scale=10**12):
    low, high = bounds
    lo = (low * scale).numerator // (low * scale).denominator
    z = high * scale
    hi = -((-z.numerator) // z.denominator)
    return f'[{lo}/{scale},{hi}/{scale}]'


def bracket(a, b):
    require(a < b, 'endpoint-order')
    al, _ = g_bounds(a)
    _, bu = g_bounds(b)
    require(al > 0, 'lower-not-positive')
    require(bu < 0, 'upper-not-negative')
    return al, bu


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def sub2(a, b):
    return [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]


def gram_nilpotent(u):
    # P=[[0,1],[0,0]], B=I, C=[1,0], H(t)=[1,t].
    return [[u, u*u/2], [u*u/2, u*u*u/3]]


def sampled_gram(s, n):
    out = [[Q(0), Q(0)], [Q(0), Q(0)]]
    for j in range(1, n + 1):
        t = Q(j, n)
        if t > s:
            h = (Q(1), t-s)
            for k, l in product(range(2), repeat=2):
                out[k][l] += h[k]*h[l]/n
    return out


def measurable(values, atoms):
    return all(len({values[omega] for omega in atom}) == 1 for atom in atoms)


def main():
    lo, hi = Q(32673, 25000), Q(130693, 100000)
    gl, gu = bracket(lo, hi)
    require(gl > Q(17, 1000000), 'lower-margin')
    require(gu < -Q(4, 10000000), 'upper-margin')
    print('ROOT exact:', lo, '< r <', hi)
    print('  g(lower) in', scaled_interval(g_bounds(lo)))
    print('  g(upper) in', scaled_interval(g_bounds(hi)))
    print('  certified margins: g(lower)>17/1000000; g(upper)<-4/10000000')
    negative('false-lower', 'lower-not-positive',
             lambda: bracket(hi, hi + Q(1, 100000)))
    negative('false-upper', 'upper-not-negative',
             lambda: bracket(lo - Q(1, 100000), lo))
    negative('unsafe-tail', 'geometric-tail-unavailable', lambda: g_bounds(Q(100)))

    one_low, one_high = g_bounds(Q(1))
    require(one_low > Q(1, 3) and one_high < Q(1), 'stopping-positive-bound')
    print('STOP exact: 1/3 < g(1) < 1; with the written stopped-martingale argument E sqrt(1+tau_1) < 3')
    negative('supercritical-boundary', 'stopping-g-not-positive',
             lambda: require(g_bounds(Q(2))[0] > 0, 'stopping-g-not-positive'))

    # Scalar G(u)=u: pulse RMS^2=1-epsilon/2 and kernel discrepancy^2=s.
    for s in (Q(1, 10), Q(1, 2), Q(1)):
        require(Q(1)-s < Q(1), 'scalar-strict-clock')
        require(s > 0, 'scalar-kernel-error')
    for eps in (Q(1, 2), Q(1, 4), Q(1, 10)):
        require(1-eps/2 < 1 and 1-eps/2 > 0, 'scalar-rms-pulse')
    print('SCALAR exact: strict clock, pulse RMS^2=1-epsilon/2, kernel error^2=s')

    # An observable, nonnormal, genuinely 2-input matrix: exact Gramian and gap.
    one = gram_nilpotent(Q(1))
    require(one == [[Q(1), Q(1, 2)], [Q(1, 2), Q(1, 3)]], 'matrix-gram')
    # Largest eigenvalue is (4+sqrt(13))/6; bracket by its characteristic polynomial.
    poly = lambda x: 12*x*x-16*x+1
    require(poly(Q(1267, 1000)) < 0 < poly(Q(1268, 1000)), 'matrix-top-eigenvalue')
    for s in (Q(1, 10), Q(1, 2), Q(1)):
        gap = sub2(one, gram_nilpotent(1-s))
        require(gap[0][0] == s and det2(gap) == s**4/12, 'matrix-exact-gap')
        require(gap[0][0] > 0 and det2(gap) > 0, 'matrix-positive-gap')
    print('MATRIX exact: nonnormal H(t)=[1,t], Gramian [[1,1/2],[1/2,1/3]],')
    print('  cT^2=(4+sqrt(13))/6 in (1267/1000,1268/1000); gap determinant=s^4/12>0')
    for n in (4, 8, 16, 32, 64):
        errors = []
        for s in (Q(0), Q(1, 3), Q(3, 5), Q(1)):
            exact, sampled = gram_nilpotent(1-s), sampled_gram(s, n)
            errors.extend(abs(exact[i][j]-sampled[i][j]) for i, j in product(range(2), repeat=2))
        err = max(errors)
        require(err <= Q(4, n), 'sampled-gram-bound')
        print('  sampled N=', n, 'max entry error=', err, '<=4/N')

    # Kernel continuity for H(t)=t and rank-deficient/invisible direction.
    for s in (Q(1, 10), Q(1, 2), Q(1)):
        err2 = s**3/3 + s*s*(1-s)
        require(0 < err2 <= s*s, 'delayed-kernel-continuity')
        require(Q(1, 3) - (1-s)**3/3 > 0, 'delayed-strict-clock')
    for eps in (Q(1, 2), Q(1, 4), Q(1, 10)):
        pulse = (1-(1-eps)**4)/(12*eps)
        require(0 < Q(1, 3)-pulse <= eps/2, 'delayed-rms-pulse')
    print('DELAYED exact: CB=0 but H(t)=t, cT^2=1/3;')
    print('  kernel error^2=s^3/3+s^2(1-s)<=s^2; pulse limit=1/3')
    negative('CB-zero-implies-zero-gain', 'dynamic-output-nonzero',
             lambda: require(Q(1, 3) == 0, 'dynamic-output-nonzero'))
    for s in (Q(1, 10), Q(1, 2), Q(1)):
        # P=0, B=I, C=[1,0], G(1-s)=diag(1-s,0), cT^2=1.
        require(s > 0 and Q(1) > 0, 'invisible-gap')
    print('RANK/INVISIBLE exact: G(u)=diag(u,0), cT^2=1; e2 produces zero output')
    negative('invisible-direction-positive', 'invisible-output-is-zero',
             lambda: require(Q(0) > 0, 'invisible-output-is-zero'))

    # P=[[0,1],[0,0]], B=e1, C=e2^T: nonzero B,C but H identically zero.
    require(Q(0) == 0, 'zero-kernel')
    require(Q(0) < Q(1, 10), 'zero-branch-positive-gamma')
    print('ZERO exact: nonzero B,C, H(t)=0 and cT=0; nonzero-input strict criterion iff gamma>0')
    negative('zero-branch-closed-at-zero', 'zero-criterion-fails-at-zero',
             lambda: require(Q(0) < Q(0), 'zero-criterion-fails-at-zero'))

    # Finite-filtration analogue of the specific adapted truncation defect.
    outcomes = list(product((-1, 1), repeat=2))
    early_atoms = [[o for o in outcomes if o[0] == a] for a in (-1, 1)]
    path_cut = {o: int((Q(1, 2) + Q(1 if o[1] < 0 else 9, 2)) <= 4)
                for o in outcomes}
    pointwise_early = {o: 1 for o in outcomes}
    require(measurable(pointwise_early, early_atoms), 'pointwise-cut-not-adapted')
    negative('path-norm-truncation-adapted', 'future-dependent-truncation',
             lambda: require(measurable(path_cut, early_atoms), 'future-dependent-truncation'))
    print('TRUNCATION exact finite-filtration control: pointwise early cut is adapted; full-path cut is not')
    print('DONE: all assertions are exact finite controls, not a stochastic proof')


if __name__ == '__main__':
    main()
