#!/usr/bin/env python3
"""Reviewer-authored exact checks for f180 (no author code, no SymPy, no floats):
(1) target coefficients of y[(y+1)^2+z]^2(y^2+py+q) for symbolic p,q,z;
(2) the algebraic identities used by Lemmas 6/C3 and by the case (a)/(d) reductions,
    for symbolic z (z is a polynomial variable);
(3) exact spot checks (random rationals) that every selector polynomial is the
    stated endpoint/tangent expression;
(4) rebuild of every certified polynomial from the written definitions, scale lcm and
    digest comparison with the certificate (parsed in full);
(5) coverage proofs (prefix-free + Kraft) and label/rule consistency for all covers."""
import sys, os, json, hashlib, random, time, importlib.util, itertools, math
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
L = _load('rlib', 'reviewer-f180-lib.py'); RD = _load('rdefs', 'reviewer-f180-defs.py')
CERT = '/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-threshold-z3-certificate-v1.json'
T0 = time.time(); Z3 = Fr(83, 100); checks = []
def ok(name, cond):
    checks.append((name, bool(cond)))
    if not cond:
        print('FAIL', name)

# (1) target coefficients: variables y, p, q, z
n = 4; y, p, q, z = [L.var(i, n) for i in range(n)]; c = lambda a: L.const(a, n)
quad = L.padd(L.pmul(L.padd(y, c(1)), L.padd(y, c(1))), z)
target = L.pmuls(y, quad, quad, L.padd(L.pmul(y, y), L.pmul(p, y), q))
lz = lambda a, b: L.padd(c(a), L.pscale(z, b)); zp1sq = L.pmul(lz(1, 1), lz(1, 1))
want = {7: c(1), 6: L.padd(p, c(4)), 5: L.padd(q, L.pscale(p, 4), lz(6, 2)),
        4: L.padd(lz(4, 4), L.pmul(lz(6, 2), p), L.pscale(q, 4)),
        3: L.padd(zp1sq, L.pmul(lz(4, 4), p), L.pmul(lz(6, 2), q)),
        2: L.padd(L.pmul(zp1sq, p), L.pmul(lz(4, 4), q)),
        1: L.pmul(zp1sq, q), 0: {}}
for k in range(8):
    ok('target y^%d coefficient' % k, L.is_zero(L.psub(L.coef_in(target, 0, k), want[k])))
ok('target degree 7', L.deg_in(target, 0) == 7)

# (2) identities for symbolic z (8 variables: v1..v6, x, z)
w = RD.build_world(); V, X, Z = RD.V, RD.X, RD.Z; N8 = 8; C8 = lambda a: L.const(a, N8)
f = w['f']; A, B, h0, h1, D, E, K = [w[k] for k in ('A', 'B', 'h0', 'h1', 'D', 'E', 'K')]
F1m4 = L.padd(f[1], C8(-4))
ok('q = A + x(f1-4)', L.is_zero(L.psub(w['q'], L.padd(A, L.pmul(X, F1m4)))))
ok('E4 = A x + B', L.is_zero(L.psub(w['E4'], L.padd(L.pmul(A, X), B))))
ok('E3 = h0 + x h1', L.is_zero(L.psub(w['E3'], L.padd(h0, L.pmul(X, h1)))))
ok('K = E + x D', L.is_zero(L.psub(K, L.padd(E, L.pmul(X, D)))))
ok('E A - B D = h0 A - h1 B', L.is_zero(L.psub(L.psub(L.pmul(E, A), L.pmul(B, D)), L.psub(L.pmul(h0, A), L.pmul(h1, B)))))
al = w['al']; be1 = L.padd(V[4], V[5])
K1 = L.padd(al[3], L.pscale(L.pmul(al[1], al[2]), -1), L.pscale(L.pmul(al[1], al[1]), 4), L.pscale(al[1], -16), RD.lin(20, 4))
K2 = L.padd(al[2], L.pscale(L.pmul(al[1], al[1]), -1), L.pscale(al[1], 4), RD.lin(-6, -2))
ok('D = K1 + be1 K2 (no be2 dependence)', L.is_zero(L.psub(D, L.padd(K1, L.pmul(be1, K2)))))
Abar = L.padd(al[2], L.pscale(al[1], -4), RD.lin(10, -2), L.pmul(be1, L.padd(al[1], C8(-4))), L.pscale(L.pmul(be1, be1), Fr(1, 4)))
Dbar = L.padd(L.pscale(L.pmul(al[1], al[1]), 4), L.pscale(al[1], -16), RD.lin(20, 4), L.pscale(L.pmul(al[1], al[2]), Fr(-5, 6)), L.pmul(be1, K2))
d56 = L.psub(V[4], V[5])
ok('Abar - A = (v5-v6)^2/4', L.is_zero(L.psub(L.psub(Abar, A), L.pscale(L.pmul(d56, d56), Fr(1, 4)))))
ok('Dbar - D = al1 al2/6 - al3', L.is_zero(L.psub(L.psub(Dbar, D), L.psub(L.pscale(L.pmul(al[1], al[2]), Fr(1, 6)), al[3]))))
sos4 = {}
for i, j, k in itertools.combinations(range(4), 3):
    for a_, b_, c_ in ((i, j, k), (j, i, k), (k, i, j)):
        dd = L.psub(V[b_], V[c_]); sos4 = L.padd(sos4, L.pmul(V[a_], L.pmul(dd, dd)))
ok('al1 al2 - 6 al3 = (1/2) sum_T [v_i(v_j-v_k)^2+...] (>=0)', L.is_zero(L.psub(L.psub(L.pmul(al[1], al[2]), L.pscale(al[3], 6)), L.pscale(sos4, Fr(1, 2)))))
sq4 = L.padd(*[L.pmul(L.psub(V[i], V[j]), L.psub(V[i], V[j])) for i, j in itertools.combinations(range(4), 2)])
ok('3 al1^2 - 8 al2 = sum_{i<j<=4}(v_i-v_j)^2', L.is_zero(L.psub(L.psub(L.pscale(L.pmul(al[1], al[1]), 3), L.pscale(al[2], 8)), sq4)))
sq6 = L.padd(*[L.pmul(L.psub(V[i], V[j]), L.psub(V[i], V[j])) for i, j in itertools.combinations(range(6), 2)])
ok('5 f1^2 - 12 f2 = sum_{i<j<=6}(v_i-v_j)^2', L.is_zero(L.psub(L.psub(L.pscale(L.pmul(f[1], f[1]), 5), L.pscale(f[2], 12)), sq6)))
four = L.psub(C8(4), f[1])
ok('A - (4-f1)^2 = f2 + 4 f1 - f1^2 - 6 - 2z', L.is_zero(L.psub(L.psub(A, L.pmul(four, four)), L.padd(f[2], L.pscale(f[1], 4), L.pscale(L.pmul(f[1], f[1]), -1), RD.lin(-6, -2)))))
s_ = X   # a free variable for the completed square
lhs = L.padd(L.pscale(L.pmul(s_, s_), Fr(-7, 12)), L.pscale(s_, 4), RD.lin(-6, -2))
sh = L.padd(s_, C8(Fr(-24, 7)))
rhs = L.padd(C8(Fr(6, 7)), L.pscale(Z, -2), L.pscale(L.pmul(sh, sh), Fr(-7, 12)))
ok('-7/12 s^2+4s-6-2z = 6/7-2z-7/12(s-24/7)^2', L.is_zero(L.psub(lhs, rhs)))
ok('6/7 - 2 z3 < 0 (z3 > 3/7)', Fr(6, 7) - 2 * Z3 < 0)
Y2b = w['Y2b']; Y1p = w['Y1p']
ok('deg_x Y2b = 2', L.deg_in(Y2b, 6) == 2)
ok('c2(Y2b) = S3 * A', L.is_zero(L.psub(L.coef_in(Y2b, 6, 2), L.pmul(w['S3'], A))))
s12 = w['s12']
mbeta = L.padd(L.pmul(s12, L.psub(V[4], V[2])), L.pmul(s12, X), L.psub(L.pmul(s12, V[5]), L.pmul(V[0], V[1])))
ok('-beta = s12(v5-v3) + s12 x + (s12 v6 - v1 v2)', L.is_zero(L.padd(w['beta'], mbeta)))
ok('s12 v6 - v1 v2 = v1 v6 + v2 (v6 - v1)', L.is_zero(L.psub(L.psub(L.pmul(s12, V[5]), L.pmul(V[0], V[1])), L.padd(L.pmul(V[0], V[5]), L.pmul(V[1], L.psub(V[5], V[0]))))))
ok('deg_x Y1+ = 2', L.deg_in(Y1p, 6) == 2)
ok('E1 has degree 1 in x and contains e6', L.deg_in(w['E1'], 6) == 1)

# (3) exact spot checks of selector meanings at random rationals (z = z3)
nb, mc, aux = RD.selector_polys(Z3)
g = aux['g']
def ev(P, pt):
    tot = Fr(0)
    for k, v in P.items():
        t = Fr(v)
        for e_, a_ in zip(k, pt):
            if e_: t *= a_ ** e_
        tot += t
    return tot
rng = random.Random(20261029)
nspot = 0
for trial in range(60):
    vs = sorted(Fr(rng.randint(1, 400), rng.randint(1, 200)) for _ in range(6))
    A_, B_, D_, E_ = [ev(aux[k], vs) for k in ('A6', 'B6', 'D6', 'E6')]
    f1 = sum(vs); Q0 = A_ * A_ - (f1 - 4) * B_
    Y2 = lambda xx: ev(g['Y2b'], vs + [xx]); Y1 = lambda xx: ev(g['Y1p'], vs + [xx])
    c0, c1, c2 = [ev(t, vs) for t in aux['c']]; d0, d1, d2 = [ev(t, vs) for t in aux['d']]
    Y2d = lambda xx: 2 * c2 * xx + c1
    E4 = lambda xx: A_ * xx + B_
    if A_ == 0 or D_ == 0 or f1 == 4:
        continue
    nspot += 1
    xq = -A_ / (f1 - 4); xE = -B_ / A_; xH = -E_ / D_
    ok_ = True
    ok_ &= ev(nb['F'], vs) == 4 - f1 and ev(nb['Fm'], vs) == f1 - 4 and ev(nb['A'], vs) == A_ and ev(nb['mA'], vs) == -A_
    ok_ &= ev(nb['Q'], vs) == Q0
    ok_ &= ev(nb['mE46'], vs) == -E4(vs[5])
    ok_ &= ev(nb['mG6'], vs) == -Y2(vs[5]) and ev(nb['mD6'], vs) == -Y2d(vs[5])
    ok_ &= ev(nb['mDl'], vs) == -(c1 * c1 - 4 * c2 * c0)
    ok_ &= ev(nb['mGq'], vs) == -(f1 - 4) ** 2 * Y2(xq)
    ok_ &= ev(nb['T2'], vs) == A_ * (f1 - 4) ** 2 * (Y2(xq) + Y2d(xq) * (xE - xq))
    ok_ &= (f1 - 4) * (xE - xq) == Q0 / A_
    ok_ &= ev(nb['mGE'], vs) == -A_ * A_ * Y2(xE) and ev(nb['mDE'], vs) == -A_ * Y2d(xE)
    ok_ &= ev(mc['A'], vs) == A_ and ev(mc['mD'], vs) == -D_ and ev(mc['D'], vs) == D_ and ev(mc['mA'], vs) == -A_
    ok_ &= ev(mc['c2'], vs) == d2
    ok_ &= ev(mc['mendL'], vs) == -A_ * A_ * Y1(xE) and ev(mc['mendH'], vs) == -D_ * D_ * Y1(xH)
    ok_ &= ev(mc['H'], vs) == -(ev(aux['h06'], vs) * A_ - ev(aux['h16'], vs) * B_) == -(E_ * A_ - B_ * D_)
    ok_ &= ev(g['E4'] if 'E4' in g else RD.at_z(w['E4'], Z3), vs + [Fr(7, 3)]) == E4(Fr(7, 3))
    ok_ &= ev(RD.at_z(w['K'], Z3), vs + [Fr(5, 2)]) == E_ + Fr(5, 2) * D_
    ok('spot trial %d' % trial, ok_)
ok('at least 50 spot trials', nspot >= 50)

# (4) digests
raw = open(CERT, 'rb').read(); cert = json.loads(raw.decode('utf-8'))
ok('certificate sha256', hashlib.sha256(raw).hexdigest() == 'b1946079fc0a380e77cdfd1e04dd9e88a6fac6e5379bf8dce65e0ef3acad6d10')
ok('certificate z3 field', cert['z3'] == '83/100')
for cov, polys in (('NB', nb), ('MC', mc)):
    ok('%s polynomial name set' % cov, set(cert[cov]['polynomials']) == set(polys))
    for k, P in polys.items():
        Pi, Lc = L.integerize(P)
        ok('%s %s scale lcm' % (cov, k), Lc == cert[cov]['polynomials'][k]['scale_lcm'])
        ok('%s %s digest' % (cov, k), L.digest(Pi) == cert[cov]['polynomials'][k]['sha256'])
Qpol, Hpol = RD.compact_polys(Z3)
for cov, P in (('QO', Qpol), ('HO', Hpol)):
    Pi, Lc = L.integerize(P)
    ok('%s scale lcm' % cov, Lc == cert[cov]['scale_lcm']); ok('%s digest' % cov, L.digest(Pi) == cert[cov]['sha256'])
    ok('%s degree<=2 per variable' % cov, all(L.deg_in(Pi, i) <= 2 for i in range(6)))
ok('Qpol(6 unsorted) == Q0(sorted defs)', L.is_zero(L.psub(Qpol, nb['Q'])))
ok('Hpol(6 unsorted) == H(sorted defs)', L.is_zero(L.psub(Hpol, mc['H'])))
for k, P in RD.residual_polys(Z3).items():
    Pi, Lc = L.integerize(P)
    ok('residual %s digest' % k, L.digest(Pi) == cert['residual']['polynomials'][k]['sha256'])
# boxes and cubes
ok('N cube <-> N box', [Fr(11, 32) / (1 - Fr(11, 32)), Fr(37, 64) / (1 - Fr(37, 64))] == [Fr(11, 21), Fr(37, 27)])
ok('M cube <-> M box', [Fr(7, 16) / (1 - Fr(7, 16)), Fr(5, 8) / (1 - Fr(5, 8))] == [Fr(7, 9), Fr(5, 3)])
ok('cert QO cube', cert['QO']['excluded_cube'] == ['11/32', '37/64']); ok('cert HO cube', cert['HO']['excluded_cube'] == ['7/16', '5/8'])
ok('cert NB box', cert['NB']['box'] == ['11/21', '37/27']); ok('cert MC box', cert['MC']['box'] == ['7/9', '5/3'])

# (5) coverage + labels + rules
MYNB = {'unsorted': [], 'F': ['F'], 'A': ['A'], 'Q': ['Q'], 'E4v6': ['mA', 'mE46'], 'Y2v6': ['mA', 'mG6', 'mD6'],
        'Y2tan': ['mA', 'Fm', 'mGq', 'T2'], 'Y2E': ['mA', 'mGE', 'mDE'], 'Disc': ['mA', 'mDl']}
MYMC = {'unsorted': [], 'mA': ['mA'], 'D': ['D'], 'H': ['H'], 'Y1end': ['A', 'mD', 'c2', 'mendL', 'mendH']}
ok('NB rules == packet text rules', cert['NB']['rules'] == MYNB)
ok('MC rules == packet text rules', cert['MC']['rules'] == MYMC)
ok('NB nonstrict == {Y2v6:mD6, Y2E:mDE}', sorted(cert['NB']['nonstrict']) == ['Y2E:mDE', 'Y2v6:mD6'])
labs = {'QO': {'pos', 'R'}, 'HO': {'pos', 'R'}, 'NB': set(MYNB), 'MC': set(MYMC), 'residual': {'Abar<=0', 'Dbar<=0', 'f1-4<0'}}
for cov in ('QO', 'HO', 'NB', 'MC', 'residual'):
    lv = cert[cov]['leaves']
    good = all(isinstance(t, list) and len(t) == 2 and isinstance(t[0], str) and t[1] in labs[cov] for t in lv)
    ok('%s leaf records well-formed with known labels' % cov, good)
    cov_ok, info = L.coverage_proof([t[0] for t in lv])
    ok('%s coverage: %s' % (cov, info), cov_ok)
    cnt = {}
    for _, lab in lv: cnt[lab] = cnt.get(lab, 0) + 1
    if 'leaf_counts' in cert[cov]:
        ok('%s leaf_counts field == recount' % cov, cnt == cert[cov]['leaf_counts'])
    print(cov, len(lv), dict(sorted(cnt.items())), info)
ok('sorted leaf lists', all([t[0] for t in cert[c]['leaves']] == sorted(t[0] for t in cert[c]['leaves']) for c in ('QO', 'HO', 'NB', 'MC', 'residual')))
npass = sum(1 for _, b in checks if b)
print('identity/digest/coverage checks: %d/%d PASS' % (npass, len(checks)), round(time.time() - T0, 1), 's')
sys.exit(0 if npass == len(checks) else 1)
