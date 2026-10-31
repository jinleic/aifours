#!/usr/bin/env python3
"""Local part of a prospective consolidated PH7 local-to-global argument.

Refines the adopted algebraic endpoint in a nested rational box, proves an
exact local dual bound with rho=delta_z=1/500 by centered polynomial arithmetic,
and writes one exclusive local-stage certificate. NO global complement or
supremum equality is claimed by this program.
"""
import ast
import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'frontier-20261029-ph7-local-global-local-certificate-v1.json'
assert not OUT.exists(), 'refusing to overwrite local certificate'
sys.path.insert(0, str(ROOT / 'frontier-20261028-localdeps'))
import sympy as S

# Reuse only named interval/AD declarations of the pinned owner checker; do NOT
# run its top-level certificate writer. This reuse is not an independent replay.
ENGINE = ROOT / 'frontier-20261029-ph7-v4-local-spectral-optimality-check.py'
ENGINE_SHA = '6eed9b486726dcb79a8ad8d57c4106aa312c354df7cc7989c5887dd7a121813b'
raw = ENGINE.read_bytes(); assert hashlib.sha256(raw).hexdigest() == ENGINE_SHA
names = {'I', 'AD', 'elementary', 'quantities', 'dual_box', 'evaluate'}
nodes = [n for n in ast.parse(raw).body if isinstance(n, (ast.ClassDef, ast.FunctionDef)) and n.name in names]
assert {n.name for n in nodes} == names
engine = {'Q': Q}
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(ENGINE)+' [declarations only]', 'exec'), engine)
I, AD = engine['I'], engine['AD']
quantities, dual_box = engine['quantities'], engine['dual_box']

OLD_CENTER = [Q(1338787907, 10**9), Q(1042029691, 10**9), Q(820420441, 10**9)]
OLD_RADIUS = Q(1, 10**7)
CENTER = [Q(334696976789746519, 250000000000000000), Q(208405938226799943, 200000000000000000), Q(410210220392063003, 500000000000000000)]
RADIUS = Q(1, 10**16)
RHO = DELTA_Z = Q(1, 500)
assert all(abs(a-b)+RADIUS < OLD_RADIUS for a, b in zip(CENTER, OLD_CENTER))

def root_jet(box):
    u, v, z = [AD.variable(t, 3, i) for i, t in enumerate(box)]
    W, E3, _, _, Z = quantities([v, v, u, u, u, u, u], z)
    return [W, E3, Z]

point = root_jet([I(t) for t in CENTER])
assert all(t.v.lo == t.v.hi and all(g.lo == g.hi for g in t.g) for t in point)
J0 = S.Matrix([[S.Rational(g.lo) for g in t.g] for t in point])
P = J0.inv(); assert P*J0 == S.eye(3)
Pq = [[Q(int(t.p), int(t.q)) for t in row] for row in P.tolist()]
root_box = [I(t-RADIUS, t+RADIUS) for t in CENTER]
jets = root_jet(root_box)
contraction = max(sum((I(int(i == j))-sum((jets[k].g[j]*Pq[i][k] for k in range(3)), I(0))).absmax() for j in range(3)) for i in range(3))
center_error = max(abs(sum(Pq[i][k]*point[k].v.lo for k in range(3))) for i in range(3))
assert contraction < Q(1, 10**8)
assert center_error+contraction*RADIUS < RADIUS
# A contraction on the new closed box has a unique zero there. Since the box
# lies in the adopted old uniqueness box, it is the same endpoint triple.
a, b, det = dual_box(root_box)
ap, bp, _ = dual_box([I(t) for t in CENTER])
assert ap.lo == ap.hi and bp.lo == bp.hi
ar = Q(round(ap.lo*10**15), 10**15); br = Q(round(bp.lo*10**15), 10**15)
a_error = max(abs(a.lo-ar), abs(a.hi-ar)); b_error = max(abs(b.lo-br), abs(b.hi-br))

v = S.symbols('v1:8'); z, aa, bb = S.symbols('z aa bb')
def esym(vs, k): return sum(S.prod(c) for c in itertools.combinations(vs, k)) if k else S.Integer(1)
e = [esym(v, k) for k in range(7)]
p = e[1]-4; q = e[2]-4*e[1]+10-2*z
W = e[3]-4*e[2]+(10-2*z)*e[1]+12*z-20
E3 = e[4]-(6+2*z)*e[2]+(20+4*z)*e[1]+3*z*z+6*z-45
E2 = e[5]-(1+z)**2*p-(4+4*z)*q; E1 = e[6]-(1+z)**2*q
s = v[0]+v[1]; S4 = sum(v[:4]); K = E3-W*S4; Z = E1-s*E2
alpha = esym(v[:4], 3)-s*esym(v[3:], 2); B = v[0]*v[1]-s*s
Y = Z-W*alpha-K*B+W*W/2
F = Z+aa*W+bb*E3-E3*E3
lam = aa+alpha+bb*S4-W/2-S4*E3; mu = bb+B-E3
assert S.expand(F-Y-lam*W-mu*K) == 0

# Exact symbolic derivative polynomials shifted about a rational center.
# The coefficient triangle bounds keep cancellations at the center; this is
# much sharper than substituting intervals into the unexpanded Hessian.
gens = (*v, z)
centers = (CENTER[1], CENTER[1], *([CENTER[0]]*5), CENTER[2])
def shift(expr):
    poly = S.Poly(expr, *gens)
    terms = {k: Q(int(c.p), int(c.q)) for k, c in poly.terms()}
    for ax, c0 in enumerate(centers):
        out = {}
        for powers, val in terms.items():
            k = powers[ax]
            for j in range(k+1):
                kk = powers[:ax]+(j,)+powers[ax+1:]
                out[kk] = out.get(kk, Q(0))+val*math.comb(k, j)*c0**(k-j)
        terms = {k: val for k, val in out.items() if val}
    return terms

def bound(terms, radius):
    c0 = terms.get((0,)*8, Q(0))
    error = sum(abs(val)*radius**sum(k) for k, val in terms.items() if sum(k))
    return I(c0-error, c0+error)

def digest(terms):
    rows = [[list(k), str(v)] for k, v in sorted(terms.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()

pc = {aa: S.Rational(ar), bb: S.Rational(br)}
H = S.hessian(F, v).subs(pc)
HC = {(i, j): shift(H[i, j]) for i in range(7) for j in range(i, 7)}
HW = {(i, j): shift(S.diff(W, v[i], v[j])) for i in range(7) for j in range(i, 7)}
HE = {(i, j): shift(S.diff(E3, v[i], v[j])) for i in range(7) for j in range(i, 7)}
EX = {'lambda': shift(lam.subs(pc)), 'mu': shift(mu.subs(pc)), 'Fz': shift(S.diff(F, z).subs(pc)),
      'Wz': shift(S.diff(W, z)), 'E3z': shift(S.diff(E3, z))}
# Arbitrary rational upper-unit-triangular preconditioner (determinant 1).
# Its choice is diagnostic-guided, its invertibility and every sign are exact.
RN = [[1000000, -890365, -255692, -211537, -180386, -157232, -139346],
      [0, 1000000, -255692, -211537, -180386, -157232, -139346],
      [0, 0, 1000000, -172689, -147259, -128357, -113756],
      [0, 0, 0, 1000000, -147259, -128357, -113756],
      [0, 0, 0, 0, 1000000, -128357, -113756],
      [0, 0, 0, 0, 0, 1000000, -113756],
      [0, 0, 0, 0, 0, 0, 1000000]]
R = [[Q(t, 10**6) for t in row] for row in RN]
assert all(R[i][i] == 1 and all(R[i][j] == 0 for j in range(i)) for i in range(7))

def congruence(polys):
    out = {}
    for i in range(7):
        for j in range(i, 7):
            acc = {}
            for (k, l), poly in polys.items():
                c = -R[k][i]*R[l][j]
                if k != l: c -= R[l][i]*R[k][j]
                if c:
                    for key, val in poly.items(): acc[key] = acc.get(key, Q(0))+c*val
            out[i, j] = {k: v for k, v in acc.items() if v}
    return out
TC, TW, TE = congruence(HC), congruence(HW), congruence(HE)
r = RHO+RADIUS  # also encloses the z displacement since DELTA_Z=RHO
T = {}
for (i, j), poly in TC.items():
    enclosure = bound(poly, r)
    error = a_error*bound(TW[i, j], r).absmax()+b_error*bound(TE[i, j], r).absmax()
    enclosure = enclosure+I(-error, error)
    T[i, j] = T[j, i] = enclosure
margins = [T[i, i].lo-sum(T[i, j].absmax() for j in range(7) if j != i) for i in range(7)]
assert min(margins) > 0
s4hi = 2*(CENTER[1]+r)+2*(CENTER[0]+r)
lambda_error = a_error+b_error*s4hi
LB = bound(EX['lambda'], r)+I(-lambda_error, lambda_error)
MB = bound(EX['mu'], r)+I(-b_error, b_error)
z_error = a_error*bound(EX['Wz'], r).absmax()+b_error*bound(EX['E3z'], r).absmax()
FZ = bound(EX['Fz'], r)+I(-z_error, z_error)
assert LB.lo > 0 and MB.lo > 0 and FZ.hi < 0

result = {
    'scope': 'LOCAL stage only; no global complement or supremum equality',
    'engine_path': ENGINE.name, 'engine_sha256': ENGINE_SHA,
    'old_root_center': [str(t) for t in OLD_CENTER], 'old_root_radius': str(OLD_RADIUS),
    'refined_root_center': [str(t) for t in CENTER], 'refined_root_radius': str(RADIUS),
    'root_contraction_matrix': [[str(t) for t in row] for row in Pq],
    'root_contraction_norm_upper': str(contraction), 'root_center_error_upper': str(center_error),
    'root_refinement_predicates': ['new closed box inside old uniqueness box', 'norm<1/10^8', 'center_error+norm*radius<radius'],
    'rho': str(RHO), 'delta_z': str(DELTA_Z),
    'dual_a_interval': a.pair(), 'dual_b_interval': b.pair(), 'dual_determinant_interval': det.pair(),
    'rational_a_center': str(ar), 'rational_b_center': str(br), 'a_error_bound': str(a_error), 'b_error_bound': str(b_error),
    'R_numerators_denominator_1000000': RN,
    'lambda_interval': LB.pair(), 'mu_interval': MB.pair(), 'F_z_interval': FZ.pair(),
    'diagonal_dominance_margins': [str(t) for t in margins],
    'centered_congruence_polynomial_sha256': {f'{i},{j}': digest(poly) for (i, j), poly in TC.items()},
    'centered_scalar_polynomial_sha256': {k: digest(poly) for k, poly in EX.items()},
    'proof_predicates': ['lambda>0', 'mu>0', 'F_z<0', 'R^T(-H_v F)R strictly positive diagonally dominant'],
}
OUT.write_text(json.dumps(result, indent=1)+'\n')
print('PASS: nested endpoint root box, exact contraction and dual constants')
print('PASS: rho=delta_z=1/500; positive multipliers, negative F_z, uniform negative v-Hessian')
print('LOCAL ONLY; no global supremum equality')
print('saved', OUT)
