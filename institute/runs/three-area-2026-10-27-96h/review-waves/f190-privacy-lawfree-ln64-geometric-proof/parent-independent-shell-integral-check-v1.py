#!/usr/bin/env python3
"""Independent exact strip/triangle calculation, not author certificate execution."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'parent-independent-shell-integral-result-v1.json'
if OUT.exists():
    raise RuntimeError('Refusing to overwrite receipt')
START = time.monotonic()
CLOCK = subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()
M = Q(1, 63)
T2 = M + 2*M**2
T3 = M + 6*M**2 + 6*M**3
T4 = M + 14*M**2 + 36*M**3 + 24*M**4
LOW = Q(163006627735070347894185905345794, 10**33)
HIGH = LOW + Q(1, 10**33)

def add(*ps):
    result = [Q(0)] * max(map(len, ps))
    for p in ps:
        for i, x in enumerate(p):
            result[i] += x
    return result

def scale(p, x):
    return [v*x for v in p]

def mul(p, q):
    result = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i+j] += a*b
    return result

def integral(p, lo, hi):
    return sum((a*(hi**(i+1)-lo**(i+1))/Q(i+1) for i,a in enumerate(p)), Q(0))

def angle_bounds(z):
    if z == 0:
        return Q(0), Q(0)
    if not 0 < z < 1:
        raise ValueError('angle-domain')
    n = 30
    a = sum(((-1)**k*z**(2*k+1)/Q(2*k+1) for k in range(n)), Q(0))
    b = a + z**(2*n+1)/Q(2*n+1)
    grid = 10**75
    lo = Q((a*grid).numerator // (a*grid).denominator, grid)
    hi = Q(-((-b*grid).numerator // (-b*grid).denominator), grid)
    if not lo <= a < b <= hi:
        raise ValueError('angle-rounding')
    return lo, hi

def shell(t, c, triangle_moment=True, triangle_area_scale=1):
    if not 0 <= c < t:
        raise ValueError('core-domain')
    y = 2*t-c+M
    a = y*y+c*c
    bounds = angle_bounds(c/y)
    # On the arc write s=sqrt(a-u^2), F=s-M. Expanding the
    # integrated horizontal cost gives (a/3+T2-M^2)s+2u^2s/3
    # plus the polynomial below. No copied moments routine.
    i0 = (c*y/2, a/2)
    i1 = (c*(2*c*c-a)*y/8, a*a/8)
    k = 2*M**3/3-M*T2+T3/3
    n_arc = ((a/3+T2-M*M)*i0[0]+Q(2,3)*i1[0]+k*c-c**4/3,
             (a/3+T2-M*M)*i0[1]+Q(2,3)*i1[1])
    z_arc = (i0[0]-c*c/2, i0[1])
    # Facet F=2t-u: integrate the horizontal line formulas
    # E(F+G)^3/3 + u^2(F+M) - 4u^3/3 directly as polynomials.
    f = [2*t, Q(-1)]
    f2 = mul(f,f)
    f3 = mul(f2,f)
    line_n = add(scale(f3,Q(1,3)), scale(f2,M), scale(f,T2),
                 [T3/3, Q(0), M, Q(-4,3)], mul([Q(0),Q(0),Q(1)],f))
    line_z = [2*t+M, Q(-2)]
    n_facet = integral(line_n,c,t)
    z_facet = integral(line_z,c,t)
    # The region above the diagonal endpoint is a SEPARATE triangle.
    n_triangle = 4*t*t*T2+Q(8,3)*t*T3+Q(2,3)*T4 if triangle_moment else Q(0)
    z_triangle = 2*T2*triangle_area_scale
    n = (8*(n_arc[0]+n_facet)+n_triangle, 8*n_arc[1])
    z = (8*(z_arc[0]+z_facet)+z_triangle, 8*z_arc[1])
    values = [(n[0]+n[1]*th, z[0]+z[1]*th) for th in bounds]
    if any(zz <= 0 for nn,zz in values):
        raise ValueError('normalizer-positive')
    return values

def brackets(values):
    return all(nn-LOW*zz > 0 and HIGH*zz-nn > 0 for nn,zz in values)

T = Q(1882704899884405717532381874371113060926, 10**40)
C = Q(92748081344953973231659959220098184342, 10**40)
V = shell(T,C)
if not brackets(V):
    raise RuntimeError('actual-upper-shell-outside-target-window')
# Independent coarse positive control: diamond radius one half.
coarse = shell(Q(1,4),Q(0))
g = Q(1,2)
m2 = g*g+2*M*g+T2
m4 = g**4+4*M*g**3+6*T2*g*g+4*T3*g+T4
if not all(nn/zz == m4/(3*m2) == Q(12549035,71140356) for nn,zz in coarse):
    raise RuntimeError('diamond-control')
if not m4/(3*m2) < Q(1,2):
    raise RuntimeError('minimal-shell-prerequisite')
negatives = {
    'omit-tail-triangle': not brackets(shell(T,C,triangle_moment=False)),
    'double-tail-area': not brackets(shell(T,C,triangle_area_scale=2)),
    'rounded-core-constants': not brackets(shell(Q(1883,10000),Q(93,10000))),
}
if not all(negatives.values()):
    raise RuntimeError('negative-control-not-detected')
grid = 10**75
rational_floor = lambda x: str((x*grid).numerator // (x*grid).denominator) + '/10^75'
record = {
    'kind': 'PARENT_INDEPENDENT_EXACT_SHELL_INTEGRAL_CONTROL',
    'clock_before': CLOCK,
    'clock_after': subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip(),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'all_checks_passed': True,
    'lower_crossproduct_positive': all(nn-LOW*zz>0 for nn,zz in V),
    'upper_crossproduct_positive': all(HIGH*zz-nn>0 for nn,zz in V),
    'coarse_law_J': str(m4/(3*m2)),
    'lower_crossproduct_floor': rational_floor(min(nn-LOW*zz for nn,zz in V)),
    'upper_crossproduct_floor': rational_floor(min(HIGH*zz-nn for nn,zz in V)),
    'negative_controls': negatives,
    'elapsed_seconds': time.monotonic()-START,
    'limits': 'Exact feasible-law cost window, separate triangle and V<1/2 prerequisite only. Does not replay the complete R-regime lower certificate or establish all-law geometry by finite sampling.'
}
with OUT.open('x') as fp:
    json.dump(record,fp,indent=2)
    fp.write('\n')
print(json.dumps({'result':'PASS','receipt':str(OUT),'script_sha256':record['script_sha256'],'elapsed_seconds':record['elapsed_seconds']}))
