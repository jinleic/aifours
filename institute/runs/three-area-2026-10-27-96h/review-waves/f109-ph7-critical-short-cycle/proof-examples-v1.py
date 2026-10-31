#!/usr/bin/env python3
"""proof-examples-v1.py -- exact quantitative examples for the f109 proof review.
Standard library only; independent of the author's scripts. Uses the sigma/Pade
form derived in proof-reconstruct-v1.py:  sigma(w) = prod(1+u_i w) * (1+2w+(1+z)w^2)^-2,
den = s2^2 - s1 s3, tn = s1 s4 - s2 s3, rn = s3^2 - s2 s4, t = tn/den, r = rn/den.
"""
from fractions import Fraction as Fr
import itertools, builtins
_LOGBUF=[]
def print(*a, **k):
    s=' '.join(str(x) for x in a); _LOGBUF.append(s+'\n'); builtins.print(s)

def sigmas(u, z):
    g = [Fr(1)]
    for k in range(1, 5): g.append(-2*g[k-1] - (1+z)*(g[k-2] if k >= 2 else 0))
    h = [sum(g[i]*g[k-i] for i in range(k+1)) for k in range(5)]
    e = [Fr(1)] + [Fr(0)]*5
    for x in u:
        for k in range(5, 0, -1): e[k] += Fr(x)*e[k-1]
    return [sum(e[j]*h[k-j] for j in range(k+1)) for k in range(5)]

def solve(u, z=Fr(8, 9)):
    s = sigmas(u, z)
    den = s[2]**2 - s[1]*s[3]; tn = s[1]*s[4] - s[2]*s[3]; rn = s[3]**2 - s[2]*s[4]
    D = 81*den; N = -19683*(tn*tn - 4*rn*den)
    t = tn/den if den else None; r = rn/den if den else None
    disc = (t*t - 4*r) if den else None
    return dict(sigma=s, den=den, D=D, N=N, t=t, r=r, disc=disc)

print('== exact (t,r) solutions of (E) at z=8/9 for sample five-rate choices ==')
for u in ([1]*5, [Fr(4,5)]*5, [Fr(6,5)]*5, [1,2,3,4,5], [Fr(1,10)]*5, [10]*5, [Fr(1,10**6)]*5, [10**6]*5):
    o = solve(u)
    print(' u=%s\n   den=%s D=%s N=%s\n   t=%s r=%s  t^2-4r=%s  (= -N/(3D^2): %s)  -> %s' % (
        [str(Fr(x)) for x in u], o['den'], o['D'], o['N'], o['t'], o['r'], o['disc'],
        -o['N']/(3*o['D']**2) == o['disc'], 'NO real v1,v2' if o['disc'] < 0 else 'REAL v1,v2 EXIST'))
    assert o['D'] > 0 and o['N'] > 0 and o['disc'] < 0

print('\n== exact diagonal polynomials u = x*(1,1,1,1,1) at z=8/9 ==')
# D(x1) and N(x1) as univariate polynomials via exact interpolation on enough points
def interp(f, deg):
    xs = [Fr(k) for k in range(deg+1)]; ys = [f(x) for x in xs]
    # Newton -> monomial, exact
    n = deg+1; coef = list(ys)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i]-coef[i-1])/(xs[i]-xs[i-j])
    # expand Newton form
    poly = [Fr(0)]*n; basis = [Fr(1)]
    for i in range(n):
        for k, b in enumerate(basis): poly[k] += coef[i]*b
        nb = [Fr(0)]*(len(basis)+1)
        for k, b in enumerate(basis): nb[k] -= xs[i]*b; nb[k+1] += b
        basis = nb
    return poly
Dx = interp(lambda x: solve([x]*5)['D'], 10)
Nx = interp(lambda x: solve([x]*5)['N'], 20)
def polystr(p): return ' + '.join('(%s)x^%d' % (c, i) for i, c in enumerate(p) if c)
print(' D(x1) =', polystr(Dx))
# check x=1 is a double root of D(x1)-112 and factor out (x-1)^2 exactly
def divide(p, root):
    q = [Fr(0)]*(len(p)-1); rem = Fr(0)
    for i in range(len(p)-1, -1, -1):
        rem = p[i] + rem*root if i == len(p)-1 else p[i] + rem*root
    # synthetic division properly:
    out = [Fr(0)]*(len(p)-1); carry = Fr(0)
    for i in range(len(p)-1, 0, -1):
        carry = p[i] + carry*root; out[i-1] = carry
    remainder = p[0] + carry*root
    return out, remainder
shift = list(Dx); shift[0] -= 112
q1, r1 = divide(shift, Fr(1)); q2, r2 = divide(q1, Fr(1))
print(' D(x1) - 112 = (x-1)^2 * [', polystr(q2), ']   remainders:', r1, r2)
cd = q2[1]**2 - 4*q2[2]*q2[0]
print(' cofactor quadratic: leading %s > 0, discriminant %s < 0 => positive for ALL real x; hence D(x1) >= 112 with equality only at x=1' % (q2[2], cd))
assert r1 == 0 and r2 == 0 and q2[2] > 0 and cd < 0
# N along the diagonal: locate the minimum by exact sign of derivative on a rational grid
dN = [i*Nx[i] for i in range(1, len(Nx))]
def ev(p, x): return sum(c*x**i for i, c in enumerate(p))
grid = [Fr(k, 10000) for k in range(1, 40001)]
mn = min(grid, key=lambda x: ev(Nx, x))
print(' N(x1) minimum on grid x in (0,4] step 1e-4: x=%s  N=%s (~%.6f);  N(x1) at x=1: %s; N(x1)->%s as x->0' % (mn, ev(Nx, mn), float(ev(Nx, mn)), ev(Nx, Fr(1)), Nx[0]))
print(' sign of dN/dx at x=1.2, 1.2118, 1.23:', [ (float(ev(dN, Fr(x))) > 0) for x in ('1.2', '1.2118', '1.23') ])
degN = max(i for i, c in enumerate(Nx) if c)
print(' N(x1) actual degree %d, leading coefficient %s (positive: %s); N(x1) = %s' % (degN, Nx[degN], Nx[degN] > 0, polystr(Nx)))

print('\n== control: z = 1/2 is degenerate (den vanishes at u = 1) and admits REAL v1,v2 ==')
o = solve([1]*5, Fr(1, 2))
print(' z=1/2, u=(1,1,1,1,1): sigma =', [str(x) for x in o['sigma']], ' den =', o['den'])
assert o['den'] == 0
for u in ([Fr(11,10)]*5, [Fr(9,10)]*5, [1, 1, 1, 1, Fr(3,2)]):
    o = solve(u, Fr(1, 2))
    print(' z=1/2, u=%s: den=%s t=%s r=%s t^2-4r=%s -> %s' % ([str(x) for x in u], o['den'], o['t'], o['r'], o['disc'],
          'REAL v1,v2 exist (spectral obstruction FAILS here)' if o['disc'] is not None and o['disc'] >= 0 else 'no real v'))

print('\n== control: z=8/9 pair-sum/power-sum consistency of the matched spectrum ==')
# For u=(1,1,1,1,1)+(v1,v2) with the (complex) solution, check that the first four power sums of
# (-u_1..-u_7) equal those of (0, -1+-i sqrt(8/9) x2, nu1, nu2) where nu = roots of y^2+py+q.
import cmath
o = solve([1]*5); t, r = o['t'], o['r']
p = Fr(5) + t - 4; q = Fr(10) + t*5 + r - 4*p - Fr(70, 9)
disc = t*t - 4*r
v1 = (-float(t) + cmath.sqrt(float(disc)))/2; v2 = (-float(t) - cmath.sqrt(float(disc)))/2   # roots of y^2+ty+r (these are -v)
nu1 = (-float(p) + cmath.sqrt(float(p*p - 4*q)))/2; nu2 = (-float(p) - cmath.sqrt(float(p*p - 4*q)))/2
lam = complex(-1, (8/9)**0.5)
A = [-1.0]*5 + [v1, v2]; B = [0, lam, lam, lam.conjugate(), lam.conjugate(), nu1, nu2]
for k in range(1, 5):
    pa = sum(x**k for x in A); pb = sum(x**k for x in B)
    print('   k=%d power sums: diag-side %s  spectrum-side %s  |diff|=%.2e' % (k, pa, pb, abs(pa-pb)))
print('   (the two "remaining diagonal rates" would be', -v1, 'and', -v2, ': non-real, impossible for a real matrix)')
print('\nPROOF-EXAMPLES DONE')
import pathlib
pathlib.Path(__file__).with_suffix('.log').write_text(open(__file__).read() and ''.join(_LOGBUF) )
