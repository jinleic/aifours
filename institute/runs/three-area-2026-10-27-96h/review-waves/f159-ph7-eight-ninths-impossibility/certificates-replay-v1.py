#!/usr/bin/env python3
"""certificates-replay-v1.py -- ReviewF159Certificates independent exact replay.

Wave f159-ph7-eight-ninths-impossibility (manifest SHA-256 0302af70...63a).
Standard library only.  No author code is imported or executed: the author
scripts were only read and hashed.  Every polynomial is re-derived here from the
written definitions (characteristic matching with D(y)=y[(y+1)^2+8/9]^2 and the
displayed formulas); JSON-embedded expressions and digests are only COMPARED
against, never used as inputs.

Certificates replayed (both parsed completely, duplicate JSON keys rejected):
  G4 = frontier-20261028-ph7-girth4-critical-bernstein-certificate.json  (b2674b82...)
  RS = frontier-20261029-ph7-no-two-cycle-residual-certificate-v1.json   (45256245...)

Methods (independent of each other):
  * G4: per-leaf tensor-product blossom (polar form) change of basis computed
    directly from the dyadic box, cross-checked on EVERY leaf against a separate
    integer midpoint de Casteljau tree walk, plus direct evaluation of the
    compactified polynomial at every vertex of a leaf sample.
  * RS: per-leaf explicit affine substitution + power->Bernstein conversion,
    cross-checked on every leaf and for all three polynomials against an exact
    Fraction de Casteljau subdivision from the root, plus direct vertex
    evaluation of both the compactified and the original polynomial.
Controls: positive (actual certificates) and intended-reason negative controls.
Outputs (exclusive create, never overwrite; '--dry-run' writes nothing):
  certificates-replay-v1-result.json, certificates-replay-v1-stdout.txt
"""
import hashlib, itertools, json, math, random, re, subprocess, sys, time
from fractions import Fraction as Fr

WAVE = '/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f159-ph7-eight-ninths-impossibility/'
P18 = '/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/'
RUNDIR = '/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/'
INPUTS = {
    'manifest': (WAVE + 'manifest-v1.json', '0302af70a2f3186aec20309e0e8f8ba10aad21ef478d81203ec9c1bc55bbc63a'),
    'girth4_disposition': (RUNDIR + 'dispositions/math-1-ph7-girth-four-two-or-three-cycle-parent-v1.md', '789b687ad2aab722b405cfb0b2d2a7bdd29aca44bdf29ed6650747367886253f'),
    'G4': (P18 + 'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json', 'b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8'),
    'no2cycle_md': (P18 + 'frontier-20261029-ph7-critical-no-two-cycle-exclusion-v1.md', '46659f60be21537f02d6ea76ceac3be2b89a7a55c3d2b1e8f249c7c315383745'),
    'RS': (P18 + 'frontier-20261029-ph7-no-two-cycle-residual-certificate-v1.json', '45256245ecda8aed8ec18150c642fd70c3665cd9af31c49dc59fb25e367ed6be'),
    'main_md': (P18 + 'frontier-20261029-ph7-eight-ninths-impossibility-v1.md', '599feaa589a6281316786cdd4d19050a88ba2945a12ce253d5f04678e862b2d4'),
}
OUT_JSON = WAVE + 'certificates-replay-v1-result.json'
OUT_LOG = WAVE + 'certificates-replay-v1-stdout.txt'

LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)
def clock():
    return subprocess.run(['/bin/date'], capture_output=True, text=True).stdout.strip()
REC = {'checks': {}, 'controls': {}}
FAILED = []
SCOPE = 'both'          # 'G4', 'RS', 'both' (affect certificate verdicts) or 'supp' (supplementary only)
def check(name, cond, detail=None, scope=None):
    sc = scope or SCOPE
    REC['checks'][name] = {'ok': bool(cond), 'scope': sc} if detail is None else {'ok': bool(cond), 'scope': sc, 'detail': detail}
    log(('PASS ' if cond else 'FAIL ') + '[' + sc + '] ' + name + ('' if detail is None else ' :: ' + json.dumps(detail, default=str)))
    if not cond:
        FAILED.append((sc, name))

T0 = time.time()
REC['clock_start'] = clock()
REC['script_sha256'] = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
REC['python'] = sys.version
log('clock_start', REC['clock_start'])
log('script_sha256', REC['script_sha256'])

# ------------------------------------------------------------------ inputs
RAW = {}
for key, (path, sha) in INPUTS.items():
    b = open(path, 'rb').read()
    RAW[key] = b
    check('input sha256 ' + key, hashlib.sha256(b).hexdigest() == sha, {'bytes': len(b), 'LF': b.count(b'\n')}, scope={'G4': 'G4', 'RS': 'RS'}.get(key, 'both'))
def strict_json(b):
    def hook(pairs):
        d = {}
        for k, v in pairs:
            if k in d:
                raise ValueError('duplicate JSON key ' + k)
            d[k] = v
        return d
    return json.loads(b.decode('utf-8'), object_pairs_hook=hook)
G4 = strict_json(RAW['G4'])
RS = strict_json(RAW['RS'])
check('G4 top-level keys', sorted(G4) == sorted(['z', 'Q_coefficients_sha256', 'H_coefficients_sha256', 'Q_variable_degrees', 'H_variable_degrees', 'Q_terms', 'H_terms', 'Q_positive_compactified_binary_leaf_paths', 'H_positive_compactified_binary_leaf_paths', 'split_axis', 'compactification', 'identity', 'scope']), sorted(G4), scope='G4')
check('RS top-level keys', sorted(RS) == sorted(['z', 'variables', 'compactification', 'polynomials', 'split_axis', 'selectors', 'leaf_counts', 'leaves', 'imported']), sorted(RS), scope='RS')
REC['G4_metadata'] = {k: G4[k] for k in ('z', 'Q_variable_degrees', 'H_variable_degrees', 'Q_terms', 'H_terms', 'split_axis', 'compactification', 'identity', 'scope')}
REC['RS_metadata'] = {k: RS[k] for k in ('z', 'variables', 'compactification', 'split_axis', 'selectors', 'leaf_counts', 'imported')}
check('both certificates declare z=8/9', G4['z'] == '8/9' and RS['z'] == '8/9')

# ------------------------------------------------------------------ sparse polynomials
def padd(*ps):
    o = {}
    for p in ps:
        for k, v in p.items():
            o[k] = o.get(k, 0) + v
    return {k: v for k, v in o.items() if v}
def pscale(p, c):
    c = Fr(c)
    return {k: v * c for k, v in p.items() if v * c}
def pmul(p, q):
    o = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            o[k] = o.get(k, 0) + v1 * v2
    return {k: v for k, v in o.items() if v}
def psub(p, q):
    return padd(p, pscale(q, -1))
def const(c, n):
    c = Fr(c)
    return {(0,) * n: c} if c else {}
def var(i, n):
    return {tuple(1 if j == i else 0 for j in range(n)): Fr(1)}
def elem_sym_all(vs, n, kmax):
    """e_0..e_kmax of the polynomials vs via the generating function prod(1+v t)."""
    e = [const(1, n)] + [{} for _ in range(kmax)]
    for v in vs:
        for k in range(kmax, 0, -1):
            e[k] = padd(e[k], pmul(v, e[k - 1]))
    return e
def compose(p, subs, n):
    o = {}
    cache = {}
    def power(i, m):
        if (i, m) not in cache:
            r = const(1, n)
            for _ in range(m):
                r = pmul(r, subs[i])
            cache[(i, m)] = r
        return cache[(i, m)]
    for k, v in p.items():
        t = const(v, n)
        for i, m in enumerate(k):
            if m:
                t = pmul(t, power(i, m))
        o = padd(o, t)
    return o
def upmul(a, b):
    o = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return o
def digest(P):
    assert all(Fr(v).denominator == 1 for v in P.values())
    rows = [[list(k), str(int(v))] for k, v in sorted(P.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
def evalP(P, pt):
    return sum((v * math.prod(Fr(pt[i]) ** e[i] for i in range(len(pt))) for e, v in P.items()), Fr(0))

# ------------------------------------------------------------------ A. characteristic matching
log('--- A. characteristic matching with D(y)=y[(y+1)^2+8/9]^2 (y^2+p y+q)')
SCOPE = 'both'
z = Fr(8, 9)
quad = [1 + z, Fr(2), Fr(1)]
Dy = upmul([Fr(0), Fr(1)], upmul(quad, quad))      # ascending coefficients, degree 5
check('D(y) coefficients', Dy == [0, Fr(289, 81), Fr(68, 9), Fr(70, 9), 4, 1], [str(c) for c in Dy])
def ladd(*ls):
    o = {}
    for l in ls:
        for k, v in l.items():
            o[k] = o.get(k, 0) + v
    return {k: v for k, v in o.items() if v}
def lsc(l, c):
    return {k: v * c for k, v in l.items()}
ONE = {'1': Fr(1)}
# [y^6]: e1 = Dy4 + p ; [y^5]: e2 = Dy3 + p Dy4 + q ; [y^4]: e3 - W = Dy2 + p Dy3 + q Dy4 ; [y^3]: e4 - CW - C4 = Dy1 + p Dy2 + q Dy3
LF_p = ladd({'e1': Fr(1)}, lsc(ONE, -Dy[4]))
LF_q = ladd({'e2': Fr(1)}, lsc(ONE, -Dy[3]), lsc(LF_p, -Dy[4]))
LF_E4 = ladd({'e3': Fr(1)}, lsc(ONE, -Dy[2]), lsc(LF_p, -Dy[3]), lsc(LF_q, -Dy[4]))
LF_E3 = ladd({'e4': Fr(1)}, lsc(ONE, -Dy[1]), lsc(LF_p, -Dy[2]), lsc(LF_q, -Dy[3]))
check('p = e1-4', LF_p == {'e1': 1, '1': -4})
check('q = e2-4e1+74/9', LF_q == {'e2': 1, 'e1': -4, '1': Fr(74, 9)})
check('E4 = e3-4e2+(74/9)e1-28/3', LF_E4 == {'e3': 1, 'e2': -4, 'e1': Fr(74, 9), '1': Fr(-28, 3)})
check('E3 = e4-(70/9)e2+(212/9)e1-1007/27', LF_E3 == {'e4': 1, 'e2': Fr(-70, 9), 'e1': Fr(212, 9), '1': Fr(-1007, 27)})
txt4 = RAW['no2cycle_md'].decode('utf-8')
txt8 = RAW['main_md'].decode('utf-8')
for s in ['E4:=e3-4e2+(74/9)e1-28/3 = W >= 0,', 'E3:=e4-(70/9)e2+(212/9)e1-1007/27 = CW+C4.',
          'A=f2-4f1+74/9,  B=f3-4f2+(74/9)f1-28/3,', 'h0=f4-(70/9)f2+(212/9)f1-1007/27,  h1=f3-(70/9)f1+212/9,',
          'Qpol=81[A^2-(f1-4)B]>0,   Hpol=-243[h0 A-h1 B]>0,', 'q=A+x(f1-4),  E4=A x+B,  E3=h0+x h1,',
          'K=E+x D,  D:=h1-A*S4,  E:=h0-B*S4,  E*A-B*D=h0*A-h1*B.', 'D = K1 + beta1*K2   (beta2 cancels),',
          'K1 = alpha3-alpha1*alpha2+4alpha1^2-16alpha1+212/9,', 'K2 = alpha2-alpha1^2+4alpha1-70/9,',
          'A  = (alpha2-4alpha1+74/9) + beta1(alpha1-4) + beta2.',
          'A <= Abar := (alpha2-4alpha1+74/9)+beta1(alpha1-4)+beta1^2/4,      Abar-A=(r5-r6)^2/4,',
          'D <= Dbar := 4alpha1^2-16alpha1+212/9-(5/6)alpha1*alpha2+beta1*K2,  Dbar-D=alpha1*alpha2/6-alpha3.',
          'Put `y=alpha1>0`, `alpha2=(3/8)tau*y^2` with `tau in (0,1]`, and `gam=beta1-y/2>=0`.']:
    check('no-2-cycle text contains: ' + s, s in txt4)
check('main text Lemma C constants', '`p=e1-4`, `q=e2-4e1+74/9`, `E4=e3-4e2+(74/9)e1-28/3`, `E3=e4-(70/9)e2+(212/9)e1-1007/27`' in txt8)
check('main text Lemma C conditions', 'p>0,   q>0,   E4>=0,   E3-E4*S4>=0' in txt8)

# ------------------------------------------------------------------ B. six-rate Qpol/Hpol
log('--- B. seventh-rate splitting, written A,B,h0,h1, Qpol/Hpol, elimination identities, digests')
SCOPE = 'G4'
r7 = [var(i, 7) for i in range(6)]
x7 = var(6, 7)
e7 = elem_sym_all(r7 + [x7], 7, 4)
def lf_poly(l, e, n):
    o = {}
    for k, v in l.items():
        o = padd(o, const(v, n) if k == '1' else pscale(e[int(k[1])], v))
    return o
q7, E4_7, E3_7, p7 = (lf_poly(L, e7, 7) for L in (LF_q, LF_E4, LF_E3, LF_p))
def split_x(p):
    a0, a1 = {}, {}
    for k, v in p.items():
        assert k[6] <= 1
        (a1 if k[6] else a0)[k[:6] + (0,)] = v
    return a0, a1
f7 = elem_sym_all(r7, 7, 4)
c7 = lambda a: const(a, 7)
A_w = padd(f7[2], pscale(f7[1], -4), c7(Fr(74, 9)))
B_w = padd(f7[3], pscale(f7[2], -4), pscale(f7[1], Fr(74, 9)), c7(Fr(-28, 3)))
h0_w = padd(f7[4], pscale(f7[2], Fr(-70, 9)), pscale(f7[1], Fr(212, 9)), c7(Fr(-1007, 27)))
h1_w = padd(f7[3], pscale(f7[1], Fr(-70, 9)), c7(Fr(212, 9)))
q0, q1 = split_x(q7); E40, E41 = split_x(E4_7); E30, E31 = split_x(E3_7)
check('q = A + x(f1-4) with written A', not psub(q0, A_w) and not psub(q1, padd(f7[1], c7(-4))))
check('E4 = A x + B with written A,B', not psub(E41, A_w) and not psub(E40, B_w))
check('E3 = h0 + x h1 with written h0,h1', not psub(E30, h0_w) and not psub(E31, h1_w))
check('p = f1 + x - 4', not psub(p7, padd(f7[1], x7, c7(-4))))
Q7 = pscale(psub(pmul(A_w, A_w), pmul(padd(f7[1], c7(-4)), B_w)), 81)
H7 = pscale(psub(pmul(h0_w, A_w), pmul(h1_w, B_w)), -243)
check('A*q = Qpol/81 + (f1-4)*E4 (so q=Qpol/(81A) when E4=0)', not psub(pmul(A_w, q7), padd(pscale(Q7, Fr(1, 81)), pmul(padd(f7[1], c7(-4)), E4_7))))
check('A*E3 = -Hpol/243 + h1*E4 (so E3=-Hpol/(243A) when E4=0)', not psub(pmul(A_w, E3_7), padd(pscale(H7, Fr(-1, 243)), pmul(h1_w, E4_7))))
def drop_last(p):
    o = {}
    for k, v in p.items():
        assert k[-1] == 0
        o[k[:-1]] = v
    return o
Qpol = drop_last(Q7)
Hpol = drop_last(H7)
check('Qpol integer coefficients', all(v.denominator == 1 for v in Qpol.values()))
check('Hpol integer coefficients', all(v.denominator == 1 for v in Hpol.values()))
check('Qpol term count == G4 Q_terms (168)', len(Qpol) == G4['Q_terms'] == 168, len(Qpol))
check('Hpol term count == G4 H_terms (435)', len(Hpol) == G4['H_terms'] == 435, len(Hpol))
qd = [max(k[i] for k in Qpol) for i in range(6)]
hd = [max(k[i] for k in Hpol) for i in range(6)]
check('Qpol per-variable degrees == G4 (2,...,2)', qd == G4['Q_variable_degrees'] == [2] * 6, qd)
check('Hpol per-variable degrees == G4 (2,...,2)', hd == G4['H_variable_degrees'] == [2] * 6, hd)
perm_sym = all(Qpol.get(tuple(k[i] for i in pm), None) == v for pm in [(1, 0, 2, 3, 4, 5), (1, 2, 3, 4, 5, 0)] for k, v in Qpol.items()) and \
    all(Hpol.get(tuple(k[i] for i in pm), None) == v for pm in [(1, 0, 2, 3, 4, 5), (1, 2, 3, 4, 5, 0)] for k, v in Hpol.items())
check('Qpol/Hpol symmetric under S6 generators', perm_sym)
dQ, dH = digest(Qpol), digest(Hpol)
REC['Qpol_digest'], REC['Hpol_digest'] = dQ, dH
check('Qpol canonical digest == G4 Q_coefficients_sha256', dQ == G4['Q_coefficients_sha256'], dQ)
check('Hpol canonical digest == G4 H_coefficients_sha256', dH == G4['H_coefficients_sha256'], dH)
check('RS imported digests == G4 digests == re-derived', RS['imported'] == {'girth4_certificate_sha256_Q': dQ, 'girth4_certificate_sha256_H': dH}, scope='both')
REC['Qpol_constant'], REC['Hpol_constant'] = str(Qpol[(0,) * 6]), str(Hpol[(0,) * 6])

# ------------------------------------------------------------------ C. residual chain and 3-variable polynomials
log('--- C. residual reduction identities and three-parameter polynomials')
SCOPE = 'RS'
r6 = [var(i, 6) for i in range(6)]          # r1..r4 = four smallest a_i, r5,r6 = two largest
f6 = elem_sym_all(r6, 6, 4)
c6 = lambda a: const(a, 6)
A6 = padd(f6[2], pscale(f6[1], -4), c6(Fr(74, 9)))
B6 = padd(f6[3], pscale(f6[2], -4), pscale(f6[1], Fr(74, 9)), c6(Fr(-28, 3)))
h06 = padd(f6[4], pscale(f6[2], Fr(-70, 9)), pscale(f6[1], Fr(212, 9)), c6(Fr(-1007, 27)))
h16 = padd(f6[3], pscale(f6[1], Fr(-70, 9)), c6(Fr(212, 9)))
al = elem_sym_all(r6[:4], 6, 4)
be1 = padd(r6[4], r6[5])
be2 = pmul(r6[4], r6[5])
S4 = al[1]
D6 = psub(h16, pmul(A6, S4))
E6 = psub(h06, pmul(B6, S4))
lift = lambda p: {k + (0,): v for k, v in p.items()}
check('K := E3 - E4*S4 = E + x*D (7 variables)', not psub(psub(E3_7, pmul(E4_7, lift(S4))), padd(lift(E6), pmul(x7, lift(D6)))))
check('E*A - B*D = h0*A - h1*B', not psub(psub(pmul(E6, A6), pmul(B6, D6)), psub(pmul(h06, A6), pmul(h16, B6))))
K1 = padd(al[3], pscale(pmul(al[1], al[2]), -1), pscale(pmul(al[1], al[1]), 4), pscale(al[1], -16), c6(Fr(212, 9)))
K2 = padd(al[2], pscale(pmul(al[1], al[1]), -1), pscale(al[1], 4), c6(Fr(-70, 9)))
check('D = K1 + beta1*K2 (beta2 cancels)', not psub(D6, padd(K1, pmul(be1, K2))))
check('A = (alpha2-4alpha1+74/9) + beta1(alpha1-4) + beta2', not psub(A6, padd(al[2], pscale(al[1], -4), c6(Fr(74, 9)), pmul(be1, padd(al[1], c6(-4))), be2)))
s3 = [var(i, 3) for i in range(3)]
c3 = lambda a: const(a, 3)
AL1, AL2, BE1 = s3
AbarS = padd(AL2, pscale(AL1, -4), c3(Fr(74, 9)), pmul(BE1, padd(AL1, c3(-4))), pscale(pmul(BE1, BE1), Fr(1, 4)))
K2S = padd(AL2, pscale(pmul(AL1, AL1), -1), pscale(AL1, 4), c3(Fr(-70, 9)))
DbarS = padd(pscale(pmul(AL1, AL1), 4), pscale(AL1, -16), c3(Fr(212, 9)), pscale(pmul(AL1, AL2), Fr(-5, 6)), pmul(BE1, K2S))
FS = padd(AL1, BE1, c3(-4))
Abar6 = compose(AbarS, [al[1], al[2], be1], 6)
Dbar6 = compose(DbarS, [al[1], al[2], be1], 6)
d56 = psub(r6[4], r6[5])
check('Abar - A = (r5-r6)^2/4', not psub(psub(Abar6, A6), pscale(pmul(d56, d56), Fr(1, 4))))
check('Dbar - D = alpha1*alpha2/6 - alpha3', not psub(psub(Dbar6, D6), psub(pscale(pmul(al[1], al[2]), Fr(1, 6)), al[3])))
check('f1 - 4 = alpha1 + beta1 - 4', not psub(padd(f6[1], c6(-4)), compose(FS, [al[1], al[2], be1], 6)))
a4 = r6[:4]
sos3 = {}
for i in range(4):
    for j in range(4):
        for k in range(j + 1, 4):
            if i not in (j, k):
                dd = psub(a4[j], a4[k])
                sos3 = padd(sos3, pscale(pmul(a4[i], pmul(dd, dd)), Fr(1, 2)))
check('alpha1*alpha2 - 6 alpha3 = (1/2) sum a_i (a_j-a_k)^2', not psub(psub(pmul(al[1], al[2]), pscale(al[3], 6)), sos3))
sos2 = {}
for i in range(4):
    for j in range(i + 1, 4):
        dd = psub(a4[i], a4[j])
        sos2 = padd(sos2, pmul(dd, dd))
check('3 alpha1^2 - 8 alpha2 = sum_{i<j}(a_i-a_j)^2  (tau<=1)', not psub(psub(pscale(pmul(al[1], al[1]), 3), pscale(al[2], 8)), sos2))
gamid = {}
for i in range(4):
    gamid = padd(gamid, pscale(padd(psub(r6[4], a4[i]), psub(r6[5], a4[i])), Fr(1, 4)))
check('beta1 - alpha1/2 = (1/4) sum_i [(r5-a_i)+(r6-a_i)]  (gam>=0 under the ordering)', not psub(psub(be1, pscale(al[1], Fr(1, 2))), gamid))
sos6 = {}
for i in range(6):
    for j in range(i + 1, 6):
        dd = psub(r6[i], r6[j])
        sos6 = padd(sos6, pmul(dd, dd))
check('5 f1^2 - 12 f2 = sum_{i<j}(r_i-r_j)^2  (case a)', not psub(psub(pscale(pmul(f6[1], f6[1]), 5), pscale(f6[2], 12)), sos6))
four = psub(c6(4), f6[1])
check('case a: A-(4-f1)^2 = f2+4f1-f1^2-70/9', not psub(psub(A6, pmul(four, four)), padd(f6[2], pscale(f6[1], 4), pscale(pmul(f6[1], f6[1]), -1), c6(Fr(-70, 9)))))
s1 = var(0, 1)
lhs = padd(pscale(pmul(s1, s1), Fr(-7, 12)), pscale(s1, 4), const(Fr(-70, 9), 1))
shv = padd(s1, const(Fr(-24, 7), 1))
check('case a: -(7/12)f1^2+4f1-70/9 = -58/63-(7/12)(f1-24/7)^2', not psub(lhs, padd(const(Fr(-58, 63), 1), pscale(pmul(shv, shv), Fr(-7, 12)))))
Y, TAU, GAM = (var(i, 3) for i in range(3))
SUBS = [Y, pscale(pmul(TAU, pmul(Y, Y)), Fr(3, 8)), padd(GAM, pscale(Y, Fr(1, 2)))]
PA = pscale(compose(AbarS, SUBS, 3), 144)
PD = pscale(compose(DbarS, SUBS, 3), 144)
PF = pscale(compose(FS, SUBS, 3), 2)
POLYS3 = {'Abar': PA, 'Dbar': PD, 'f1minus4': PF}
NAMES = ('y', 'tau', 'gam')
def parse_terms(rhs):
    rhs = rhs.replace('**', '^').replace(' ', '')
    out = {}
    for t in re.findall(r'[+-]?[^+-]+', rhs):
        m = re.fullmatch(r'([+-]?)(\d*)\*?([a-z][a-z0-9*^]*)?', t)
        assert m, t
        sign = -1 if m.group(1) == '-' else 1
        coef = int(m.group(2)) if m.group(2) else 1
        ex = [0, 0, 0]
        if m.group(3):
            for fac in m.group(3).split('*'):
                if '^' in fac:
                    nm, pw = fac.split('^')
                    ex[NAMES.index(nm)] += int(pw)
                else:
                    ex[NAMES.index(fac)] += 1
        out[tuple(ex)] = out.get(tuple(ex), 0) + sign * coef
    return {k: Fr(v) for k, v in out.items() if v}
md_lines = {}
for line in txt4.split('\n'):
    for nm, pre in (('Abar', '    144 Abar = '), ('Dbar', '    144 Dbar = '), ('f1minus4', '    2(f1-4)  = ')):
        if line.startswith(pre):
            md_lines[nm] = line[len(pre):].rstrip(',.')
check('three scaled residual polynomial lines found in no-2-cycle text', sorted(md_lines) == ['Abar', 'Dbar', 'f1minus4'], md_lines)
for nm, P in POLYS3.items():
    check('re-derived %s == written candidate line' % nm, parse_terms(md_lines[nm]) == P, md_lines[nm])
    check('re-derived %s == JSON expr (own parser)' % nm, parse_terms(RS['polynomials'][nm]['expr']) == P)
    dg = [max(k[i] for k in P) for i in range(3)]
    check('re-derived %s degrees == JSON degrees' % nm, dg == RS['polynomials'][nm]['degrees'], dg)
    check('re-derived %s canonical digest == JSON sha256' % nm, digest(P) == RS['polynomials'][nm]['sha256'])
REC['residual_polynomials'] = {nm: {str(k): str(v) for k, v in sorted(P.items())} for nm, P in POLYS3.items()}

# ------------------------------------------------------------------ D. leaf-set structure
log('--- D. leaf-set structure (binary, unique, prefix-free, Kraft=1, explicit walk)')
def structure(paths):
    probs = []
    if any(set(p) - {'0', '1'} for p in paths) or any(p == '' for p in paths):
        probs.append('non-binary or empty path')
    if len(set(paths)) != len(paths):
        probs.append('duplicate path')
    S = set(paths)
    coll = [p for p in S if any(p[:i] in S for i in range(len(p)))]
    if coll:
        probs.append('prefix collision x%d' % len(coll))
    kraft = sum((Fr(1, 2 ** len(p)) for p in S), Fr(0))
    if kraft != 1:
        probs.append('Kraft sum %s != 1' % kraft)
    pref = set(p[:i] for p in S for i in range(len(p)))
    gaps = []
    stack = ['']
    while stack:
        nd = stack.pop()
        if nd in S:
            continue
        if nd in pref:
            stack += [nd + '0', nd + '1']
        else:
            gaps.append(nd)
    if gaps:
        probs.append('uncovered node(s) x%d e.g. %s' % (len(gaps), gaps[:3]))
    return probs, str(kraft), [min(map(len, S)), max(map(len, S))] if S else None
QL = G4['Q_positive_compactified_binary_leaf_paths']
HL = G4['H_positive_compactified_binary_leaf_paths']
RL = RS['leaves']
check('G4 Q leaf list is a list of 5332 strings', isinstance(QL, list) and len(QL) == 5332 and all(isinstance(p, str) for p in QL), scope='G4')
check('G4 H leaf list is a list of 5334 strings', isinstance(HL, list) and len(HL) == 5334 and all(isinstance(p, str) for p in HL), scope='G4')
check('RS leaves: 1653 [path,label] pairs', isinstance(RL, list) and len(RL) == 1653 and all(isinstance(e, list) and len(e) == 2 and all(isinstance(t, str) for t in e) for e in RL), scope='RS')
for nm, ps in (('G4-Q', QL), ('G4-H', HL), ('RS', [p for p, _ in RL])):
    probs, kraft, lens = structure(ps)
    check('%s complete prefix-free dyadic cover' % nm, not probs, {'problems': probs, 'kraft': kraft, 'len_min_max': lens}, scope=nm[:2])
labels = {}
for _, lab in RL:
    labels[lab] = labels.get(lab, 0) + 1
check('RS labels within the 3 declared selectors and counts == JSON leaf_counts', set(labels) <= {'Abar<=0', 'Dbar<=0', 'f1-4<0'} and labels == RS['leaf_counts'] == {'Abar<=0': 800, 'Dbar<=0': 789, 'f1-4<0': 64}, labels, scope='RS')

def box_from_path(path, naxes, reverse=False):
    ks = [0] * naxes
    ns = [0] * naxes
    for pos, ch in enumerate(path):
        a = pos % naxes
        b = 1 if ch == '1' else 0
        if reverse:
            b ^= 1
        ks[a] = 2 * ks[a] + b
        ns[a] += 1
    return ks, ns

# ------------------------------------------------------------------ E. residual certificate replay
log('--- E. residual certificate replay (closed cube [0,1]^3 in (s,tau,g); bit 0 = lower half; axis = depth mod 3)')
SCOPE = 'RS'
def binom_affine(c0, c1, m):
    return [Fr(math.comb(m, l)) * c0 ** (m - l) * c1 ** l for l in range(m + 1)]
def power_to_bern(a, d):
    a = list(a) + [Fr(0)] * (d + 1 - len(a))
    assert len(a) == d + 1
    return [sum((Fr(math.comb(m, l), math.comb(d, l)) * a[l] for l in range(m + 1)), Fr(0)) for m in range(d + 1)]
def basis_compact(d, lo, hi):
    h = hi - lo
    return [power_to_bern(upmul(binom_affine(lo, h, i), binom_affine(1 - lo, -h, d - i)), d) for i in range(d + 1)]
def basis_plain(d, lo, hi):
    h = hi - lo
    return [power_to_bern(binom_affine(lo, h, j), d) for j in range(d + 1)]
def degs3(P):
    return tuple(max(k[i] for k in P) for i in range(3))
def r1_local(P, box):
    dy, dt, dg = degs3(P)
    (s0, s1_), (t0, t1), (g0, g1) = box
    Phi, Psi, Chi = basis_compact(dy, s0, s1_), basis_plain(dt, t0, t1), basis_compact(dg, g0, g1)
    return {(m1, m2, m3): sum((v * Phi[i][m1] * Psi[j][m2] * Chi[k][m3] for (i, j, k), v in P.items()), Fr(0))
            for m1 in range(dy + 1) for m2 in range(dt + 1) for m3 in range(dg + 1)}
def r2_global(P):
    dy, dt, dg = degs3(P)
    G = {(m1, m2, m3): Fr(0) for m1 in range(dy + 1) for m2 in range(dt + 1) for m3 in range(dg + 1)}
    for (i, j, k), v in P.items():
        for m2 in range(j, dt + 1):
            G[(i, m2, k)] += v / math.comb(dy, i) / math.comb(dg, k) * Fr(math.comb(m2, j), math.comb(dt, j))
    return G
def dc_split(row):
    d = len(row) - 1
    tri = [list(row)]
    for _ in range(d):
        prev = tri[-1]
        tri.append([(prev[i] + prev[i + 1]) / 2 for i in range(len(prev) - 1)])
    return [tri[k][0] for k in range(d + 1)], [tri[d - k][k] for k in range(d + 1)]
def r2_split(T, shape, axis, upper):
    out = {}
    d = shape[axis]
    others = [range(shape[i] + 1) for i in range(3) if i != axis]
    for rest in itertools.product(*others):
        def key(m):
            kk = list(rest)
            kk.insert(axis, m)
            return tuple(kk)
        lft, rgt = dc_split([T[key(m)] for m in range(d + 1)])
        new = rgt if upper else lft
        for m in range(d + 1):
            out[key(m)] = new[m]
    return out
def compact_value(P, s, t, g):
    dy, dt, dg = degs3(P)
    return sum((v * s ** i * (1 - s) ** (dy - i) * t ** j * g ** k * (1 - g) ** (dg - k) for (i, j, k), v in P.items()), Fr(0))
SEL = {'Abar<=0': ('Abar', 'le'), 'Dbar<=0': ('Dbar', 'le'), 'f1-4<0': ('f1minus4', 'lt')}
def rs_replay(polys, leaves, reverse=False, full=True):
    G2 = {nm: r2_global(P) for nm, P in polys.items()}
    st = {'leaves': 0, 'label_fail': [], 'r1_r2_mismatch': 0, 'vertex_mismatch': 0, 'vertex_checks': 0,
          'labelled_coeffs': 0, 'all_coeffs': 0, 'tight_label_leaves': 0, 'tight_list': [], 'alt_selectors': {}, 'per_label': {}, 'per_leaf': []}
    for path, lab in leaves:
        ks, ns = box_from_path(path, 3, reverse)
        box = tuple((Fr(ks[a], 2 ** ns[a]), Fr(ks[a] + 1, 2 ** ns[a])) for a in range(3))
        holds = {}
        for nm, P in (polys.items() if full else [(SEL[lab][0], polys[SEL[lab][0]])]):
            L1 = r1_local(P, box)
            st['all_coeffs'] += len(L1)
            if full and not reverse:
                T = G2[nm]
                shape = degs3(P)
                for pos, ch in enumerate(path):
                    ax = pos % 3
                    if shape[ax] > 0:
                        T = r2_split(T, shape, ax, ch == '1')
                if T != L1:
                    st['r1_r2_mismatch'] += 1
                dy, dt, dg = shape
                for cs in (0, 1):
                    for ct in (0, 1):
                        for cg in (0, 1):
                            sv, tv, gv = box[0][cs], box[1][ct], box[2][cg]
                            coeff = L1[(dy * cs, dt * ct, dg * cg)]
                            ok = compact_value(P, sv, tv, gv) == coeff
                            if sv < 1 and gv < 1:
                                yv, gmv = sv / (1 - sv), gv / (1 - gv)
                                ok = ok and (1 - sv) ** dy * (1 - gv) ** dg * evalP(P, (yv, tv, gmv)) == coeff
                            st['vertex_checks'] += 1
                            st['vertex_mismatch'] += (not ok)
            mx = max(L1.values())
            holds[nm] = mx
        nm, rule = SEL[lab]
        mx = holds[nm]
        ok = (mx <= 0) if rule == 'le' else (mx < 0)
        st['labelled_coeffs'] += math.prod(d + 1 for d in degs3(polys[nm]))
        if not ok:
            st['label_fail'].append([path, lab, str(mx)])
        if mx == 0:
            st['tight_label_leaves'] += 1
            st['tight_list'].append([path, lab])
        st['per_leaf'].append([path, lab, str(mx)])
        st['per_label'][lab] = st['per_label'].get(lab, 0) + 1
        if full:
            alt = tuple(sorted(s for s, (pn, rr) in SEL.items() if ((holds[pn] <= 0) if rr == 'le' else (holds[pn] < 0))))
            st['alt_selectors'][' & '.join(alt)] = st['alt_selectors'].get(' & '.join(alt), 0) + 1
        st['leaves'] += 1
    return st
t = time.time()
stR = rs_replay(POLYS3, RL)
REC['RS_replay'] = {k: v for k, v in stR.items()}
REC['RS_replay']['seconds'] = round(time.time() - t, 2)
check('RS: every one of 1653 leaves satisfies its labelled selector', stR['leaves'] == 1653 and not stR['label_fail'], {'fails': stR['label_fail'][:5], 'per_label': stR['per_label']})
check('RS: method R1 (affine substitution) == R2 (de Casteljau) for all 3 polynomials on all leaves', stR['r1_r2_mismatch'] == 0, {'tensors_compared': 3 * 1653})
check('RS: all vertex coefficients == direct compactified/original evaluation', stR['vertex_mismatch'] == 0, {'vertex_checks': stR['vertex_checks']})
log('RS labelled coefficients checked', stR['labelled_coeffs'], '; all coefficients computed', stR['all_coeffs'], '; tight leaves (max coeff = 0)', stR['tight_label_leaves'], stR['tight_list'])
log('RS selectors holding per leaf (all three evaluated):', json.dumps(stR['alt_selectors']))
check('RS: tight (max labelled coefficient = 0) leaves are only non-strict Abar/Dbar selectors', all(l in ('Abar<=0', 'Dbar<=0') for _, l in stR['tight_list']), stR['tight_list'])
# Domain needed by f159 case (d): y>0, tau in (0,1], gam>=0  <->  s in (0,1), tau in (0,1], g in [0,1).
# Its boundary faces tau=1 (all four smallest rates equal) and g=0 (all six rates equal) ARE needed; they are checked
# separately here: the closed leaf boxes touching each face must tile that face exactly (area 1) -- the selector
# bounds were verified on the closed boxes above, so they hold on these faces.  Faces s=0, tau=0, s=1, g=1 are
# not needed (y>0, tau>0, finite y/gam) and no claim is made from them.
def face_area(leaves, axis, upper):
    tot = Fr(0)
    cnt = 0
    for path, _ in leaves:
        ks, ns = box_from_path(path, 3)
        on = (ks[axis] + 1 == 2 ** ns[axis]) if upper else (ks[axis] == 0)
        if on:
            cnt += 1
            tot += math.prod(Fr(1, 2 ** ns[a]) for a in range(3) if a != axis)
    return tot, cnt
for fname, axis, upper in (('tau=1', 1, True), ('g=0', 2, False)):
    area, cnt = face_area(RL, axis, upper)
    check('RS needed boundary face %s: touching closed leaves tile the face (area 1)' % fname, area == 1, {'leaves_on_face': cnt, 'area': str(area)})
REC['domains'] = {
    'f159_needed_G4': 'Qpol>0 and Hpol>0 on the OPEN positive orthant (0,inf)^6 only (Lemma C rates are positive: escape rates in the no-2-cycle text, eigenvalues of -S in the main text); compactified: x in (0,1)^6',
    'f129_asserted_G4': 'girth-4 disposition: strictly positive compactified polynomial on the open cube, i.e. all six POSITIVE rates (nonnegative Bernstein coefficients + strictly positive leaf vertices inside the open cube)',
    'G4_zero_faces': 'u_i=0 faces are NOT needed by f159 and NOT part of the f129 assertion; any statement about them below is a separately labelled reviewer computation (supp scope), not inferred from metadata',
    'f159_needed_RS': 'no point with y>0, tau in (0,1], gam>=0 has Abar>0, Dbar>0, f1-4>=0; compactified s in (0,1), tau in (0,1], g in [0,1); needed faces tau=1, g=0 checked separately; certificate covers the closed cube [0,1]^3',
}

# ------------------------------------------------------------------ F. girth-4 certificate replay
log('--- F. girth-4 certificate replay ([0,1]^6, u_i=x_i/(1-x_i), degree 2 per variable, axis = depth mod 6, bit 0 = lower half)')
SCOPE = 'G4'
STR = [3 ** (5 - i) for i in range(6)]
BASES = [[idx for idx in range(729) if (idx // STR[a]) % 3 == 0] for a in range(6)]
VERTS = [(alpha, sum(e * STR[i] for i, e in enumerate(alpha))) for alpha in itertools.product((0, 2), repeat=6)]
def g4_global(P):
    T = [0] * 729
    for k, v in P.items():
        assert v.denominator == 1 and max(k) <= 2
        b = Fr(int(v))
        for e in k:
            b /= math.comb(2, e)
        b *= 64
        assert b.denominator == 1
        T[sum(e * STR[i] for i, e in enumerate(k))] = int(b)
    return T
def blossom(k, n):
    N = 1 << n
    a0, a1, b0, b1 = N - k, k, N - k - 1, k + 1
    return ((a0 * a0, 2 * a1 * a0, a1 * a1), (a0 * b0, a1 * b0 + a0 * b1, a1 * b1), (b0 * b0, 2 * b1 * b0, b1 * b1))
def transform(T, a, M):
    st_ = STR[a]
    (m00, m01, m02), (m10, m11, m12), (m20, m21, m22) = M
    out = [0] * 729
    for i0 in BASES[a]:
        i1 = i0 + st_
        i2 = i1 + st_
        v0, v1, v2 = T[i0], T[i1], T[i2]
        out[i0] = m00 * v0 + m01 * v1 + m02 * v2
        out[i1] = m10 * v0 + m11 * v1 + m12 * v2
        out[i2] = m20 * v0 + m21 * v1 + m22 * v2
    return out
def dcsplit6(T, a):
    st_ = STR[a]
    L = [0] * 729
    Rr = [0] * 729
    for i0 in BASES[a]:
        i1 = i0 + st_
        i2 = i1 + st_
        v0, v1, v2 = T[i0], T[i1], T[i2]
        mid = v0 + 2 * v1 + v2
        L[i0], L[i1], L[i2] = 4 * v0, 2 * (v0 + v1), mid
        Rr[i0], Rr[i1], Rr[i2] = mid, 2 * (v1 + v2), 4 * v2
    return L, Rr
def g4_leaf(T0, ks, ns):
    TB = T0
    for a in range(6):
        TB = transform(TB, a, blossom(ks[a], ns[a]))
    return TB
def g4_replay(P, leaf_list, reverse=False, crosscheck=True):
    leaves = set(leaf_list)
    prefixes = set(p[:i] for p in leaves for i in range(len(p)))
    T0 = g4_global(P)
    st = {'leaves': 0, 'coeffs': 0, 'zero_coeffs': 0, 'neg_leaves': [], 'interior_vertices': 0, 'nonpos_interior_vertex_leaves': [],
          'halfopen_vertices': 0, 'halfopen_nonpos': 0, 'dc_mismatch': [], 'gaps': [], 'min_axis_bits': 10 ** 9,
          'min_interior_vertex_value': None}
    stack = [('', T0)]
    while stack:
        path, T = stack.pop()
        if path in leaves:
            ks, ns = box_from_path(path, 6, reverse)
            st['min_axis_bits'] = min(st['min_axis_bits'], min(ns))
            TB = g4_leaf(T0, ks, ns)
            if crosscheck and TB != T:
                st['dc_mismatch'].append(path)
            st['leaves'] += 1
            st['coeffs'] += len(TB)
            st['zero_coeffs'] += TB.count(0)
            if min(TB) < 0:
                st['neg_leaves'].append(path)
            bad = False
            for alpha, idx in VERTS:
                interior = halfopen = True
                for i, e in enumerate(alpha):
                    if e == 0 and ks[i] == 0:
                        interior = False
                    if e == 2 and ks[i] + 1 == (1 << ns[i]):
                        interior = halfopen = False
                if interior:
                    st['interior_vertices'] += 1
                    val = Fr(TB[idx], 64 * 4 ** len(path))
                    if st['min_interior_vertex_value'] is None or val < st['min_interior_vertex_value']:
                        st['min_interior_vertex_value'] = val
                    if TB[idx] <= 0:
                        bad = True
                if halfopen:
                    st['halfopen_vertices'] += 1
                    if TB[idx] <= 0:
                        st['halfopen_nonpos'] += 1
            if bad:
                st['nonpos_interior_vertex_leaves'].append(path)
        elif path in prefixes:
            L, Rr = dcsplit6(T, len(path) % 6)
            stack.append((path + '1', Rr))
            stack.append((path + '0', L))
        else:
            st['gaps'].append(path)
    return st
def summar(st):
    o = {k: (len(v) if isinstance(v, list) else v) for k, v in st.items()}
    o['min_interior_vertex_value'] = str(st['min_interior_vertex_value']) if st['min_interior_vertex_value'] is not None else None
    o['min_interior_vertex_value_float'] = float(st['min_interior_vertex_value']) if st['min_interior_vertex_value'] is not None else None
    o['examples_neg'] = st['neg_leaves'][:3]
    o['examples_nonpos_vertex'] = st['nonpos_interior_vertex_leaves'][:3]
    return o
G4RES = {}
for nm, P, L in (('Q', Qpol, QL), ('H', Hpol, HL)):
    t = time.time()
    st = g4_replay(P, L)
    G4RES[nm] = summar(st)
    G4RES[nm]['seconds'] = round(time.time() - t, 2)
    check('G4-%s: all %d leaves visited, no gaps' % (nm, len(L)), st['leaves'] == len(L) and not st['gaps'])
    check('G4-%s: every leaf splits every coordinate at least once' % nm, st['min_axis_bits'] >= 1, st['min_axis_bits'])
    check('G4-%s: all Bernstein coefficients >= 0' % nm, not st['neg_leaves'], {'coeffs': st['coeffs'], 'zero_coeffs': st['zero_coeffs']})
    check('G4-%s: all leaf vertices inside open cube have coefficient > 0' % nm, not st['nonpos_interior_vertex_leaves'], {'interior_vertices': st['interior_vertices']})
    check('G4-%s: blossom tensor == de Casteljau tensor on every leaf' % nm, not st['dc_mismatch'])
    check('G4-%s zero-face diagnostic (reviewer computation, NOT an f129 assertion, NOT needed by f159): all leaf vertices with coordinates in [0,1)^6 have coefficient > 0' % nm,
          st['halfopen_nonpos'] == 0, {'halfopen_vertices': st['halfopen_vertices'], 'nonpositive': st['halfopen_nonpos'], 'min_interior_vertex_value': G4RES[nm]['min_interior_vertex_value_float']}, scope='supp')
REC['G4_replay'] = G4RES
check('G4 totals: 7,775,514 coefficients and 421,110 interior vertices', G4RES['Q']['coeffs'] + G4RES['H']['coeffs'] == 7775514 and G4RES['Q']['interior_vertices'] + G4RES['H']['interior_vertices'] == 421110,
      [G4RES['Q']['coeffs'] + G4RES['H']['coeffs'], G4RES['Q']['interior_vertices'] + G4RES['H']['interior_vertices']])
def g4_direct_scaled(P, kv, ns):
    pw = []
    for i in range(6):
        N = 1 << ns[i]
        k = kv[i]
        pw.append(((N - k) ** 2, k * (N - k), k * k))
    tot = 0
    for e, v in P.items():
        tt = int(v)
        for i in range(6):
            tt *= pw[i][e[i]]
        tot += tt
    return 64 * tot
for nm, P, L in (('Q', Qpol, QL), ('H', Hpol, HL)):
    T0g = g4_global(P)
    ps = sorted(L)
    sample = ps[::97] + [ps[-1]]
    nv = bad = 0
    for path in sample:
        ks, ns = box_from_path(path, 6)
        TB = g4_leaf(T0g, ks, ns)
        for alpha, idx in VERTS:
            kv = [ks[i] + (1 if alpha[i] == 2 else 0) for i in range(6)]
            nv += 1
            bad += g4_direct_scaled(P, kv, ns) != TB[idx]
    check('G4-%s: direct compactified evaluation == vertex coefficient (sample of %d leaves, all 64 vertices)' % (nm, len(sample)), bad == 0, {'vertices': nv})
    nv = bad = 0
    for path in ps[1000:1004]:
        ks, ns = box_from_path(path, 6)
        TB = g4_leaf(T0g, ks, ns)
        for alpha, idx in VERTS:
            xs = [Fr(ks[i] + (1 if alpha[i] == 2 else 0), 2 ** ns[i]) for i in range(6)]
            if all(0 < xx < 1 for xx in xs):
                val = evalP(P, [xx / (1 - xx) for xx in xs]) * math.prod((1 - xx) ** 2 for xx in xs)
                nv += 1
                bad += val * 64 * 4 ** len(path) != TB[idx]
    check('G4-%s: original polynomial at u=x/(1-x) times prod(1-x)^2 == vertex coefficient (4 leaves)' % nm, bad == 0 and nv > 0, {'vertices': nv})

# ------------------------------------------------------------------ G. supplementary exact controls
log('--- G. supplementary: (CHAR) on exact random no-2-cycle matrices; Lemma C falsification sweep (diagnostic)')
SCOPE = 'supp'
def det_frac(M):
    n = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        for r in range(c + 1, n):
            fct = A[r][c] / A[c][c]
            if fct:
                for k in range(c, n):
                    A[r][k] -= fct * A[c][k]
    return det
def charpoly(G):
    n = len(G)
    ys = list(range(n + 1))
    vals = [det_frac([[(Fr(yv) if i == j else Fr(0)) - G[i][j] for j in range(n)] for i in range(n)]) for yv in ys]
    co = [Fr(0)] * (n + 1)
    for idx, yi in enumerate(ys):
        num = [Fr(1)]
        den = Fr(1)
        for jdx, yj in enumerate(ys):
            if jdx != idx:
                num = upmul(num, [Fr(-yj), Fr(1)])
                den *= (yi - yj)
        for k in range(n + 1):
            co[k] += vals[idx] * num[k] / den
    return co
def char_pred(G):
    n = 7
    u = [-G[i][i] for i in range(n)]
    e = [Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]
    for t_ in u:
        for k in range(4, 0, -1):
            e[k] += t_ * e[k - 1]
    W = CW = C4 = Fr(0)
    for tri in itertools.combinations(range(n), 3):
        a, b, c = tri
        for (i, j, k) in ((a, b, c), (a, c, b)):
            w = G[i][j] * G[j][k] * G[k][i]
            W += w
            CW += w * sum(u[v] for v in range(n) if v not in tri)
    for quad_ in itertools.combinations(range(n), 4):
        a = quad_[0]
        for rest in itertools.permutations(quad_[1:]):
            cyc = (a,) + rest
            C4 += math.prod(G[cyc[i]][cyc[(i + 1) % 4]] for i in range(4))
    return e, W, CW, C4
rng = random.Random(159159)
char_ok = []
for trial in range(3):
    # directed 7-cycle backbone 0->1->...->6->0, forced chords 2->0 (3-cycle 0,1,2) and 6->3 (4-cycle 3,4,5,6),
    # random one-way chords on unused pairs only: no 2-cycle, W>0 and C4>0 by construction.
    G = [[Fr(0)] * 7 for _ in range(7)]
    for i in range(7):
        G[i][(i + 1) % 7] = Fr(rng.randint(1, 9), rng.randint(1, 4))
    G[2][0] = Fr(rng.randint(1, 9), rng.randint(1, 4))
    G[6][3] = Fr(rng.randint(1, 9), rng.randint(1, 4))
    for i in range(7):
        for j in range(i + 1, 7):
            if G[i][j] == 0 and G[j][i] == 0 and rng.random() < 0.4:
                w = Fr(rng.randint(1, 9), rng.randint(1, 4))
                if rng.random() < 0.5:
                    G[i][j] = w
                else:
                    G[j][i] = w
    for i in range(7):
        G[i][i] = -Fr(rng.randint(1, 30), rng.randint(1, 5))
    assert all(G[i][j] == 0 or G[j][i] == 0 for i in range(7) for j in range(7) if i != j)
    co = charpoly(G)
    e, W, CW, C4 = char_pred(G)
    char_ok.append(co[7] == 1 and co[6] == e[1] and co[5] == e[2] and co[4] == e[3] - W and co[3] == e[4] - CW - C4 and W > 0 and C4 > 0)
check('CHAR positive control: [y^6]=e1,[y^5]=e2,[y^4]=e3-W,[y^3]=e4-CW-C4 on 3 exact no-2-cycle matrices with W>0, C4>0', all(char_ok), char_ok)
i2, j2 = next((i, j) for i in range(7) for j in range(7) if i != j and G[i][j] != 0 and G[j][i] == 0)
G[j2][i2] = Fr(3, 2)
co = charpoly(G)
e, W, CW, C4 = char_pred(G)
neg_char = (co[5] != e[2]) and (co[5] == e[2] - G[i2][j2] * G[j2][i2])
check('CHAR negative control: adding one 2-cycle breaks [y^5]=e2 by exactly -G_ij G_ji (intended reason)', neg_char)
REC['controls']['CHAR_negative'] = {'added_2cycle': [i2, j2], 'ok': neg_char}
def lemmaC(v):
    v = sorted(v)
    e = [Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]
    for t_ in v:
        for k in range(4, 0, -1):
            e[k] += t_ * e[k - 1]
    p = e[1] - 4
    q = e[2] - 4 * e[1] + Fr(74, 9)
    E4 = e[3] - 4 * e[2] + Fr(74, 9) * e[1] - Fr(28, 3)
    E3 = e[4] - Fr(70, 9) * e[2] + Fr(212, 9) * e[1] - Fr(1007, 27)
    K = E3 - E4 * sum(v[:4])
    return (p > 0, q > 0, E4 >= 0, K >= 0)
rng = random.Random(8 * 9 * 159)
sweep = {'samples': 0, 'all_four': 0, 'three_of_four': 0}
for mode in ('uniform', 'near_equal', 'one_large', 'log_spread'):
    for _ in range(5000):
        if mode == 'uniform':
            v = [Fr(rng.randint(1, 4000), 1000) for _ in range(7)]
        elif mode == 'near_equal':
            b = Fr(rng.randint(300, 1500), 1000)
            v = [b * (1 + Fr(rng.randint(-50, 50), 1000)) for _ in range(7)]
        elif mode == 'one_large':
            v = [Fr(rng.randint(1, 1500), 1000) for _ in range(6)] + [Fr(rng.randint(1000, 20000), 1000)]
        else:
            v = [Fr(2) ** rng.randint(-6, 3) * Fr(rng.randint(500, 1000), 1000) for _ in range(7)]
        c = lemmaC(v)
        sweep['samples'] += 1
        sweep['all_four'] += all(c)
        sweep['three_of_four'] += (sum(c) == 3)
REC['lemmaC_sweep'] = sweep
check('Lemma C falsification sweep (diagnostic only): no sampled 7-tuple satisfies all four conditions', sweep['all_four'] == 0, sweep)

# ------------------------------------------------------------------ H. negative controls (expected to be REJECTED for the stated reason)
log('--- H. intended-reason negative controls')
ctrl = REC['controls']
ustar = [Fr(1)] * 6
for nm, P, L in (('Q', Qpol, QL), ('H', Hpol, HL)):
    v = evalP(P, ustar)
    Pm = padd(P, const(-(v + 1), 6))
    st = g4_replay(Pm, L, crosscheck=False)
    cont = [p for p in L if all(Fr(box_from_path(p, 6)[0][i], 2 ** box_from_path(p, 6)[1][i]) <= Fr(1, 2) <= Fr(box_from_path(p, 6)[0][i] + 1, 2 ** box_from_path(p, 6)[1][i]) for i in range(6))]
    neg = set(st['neg_leaves'])
    ok = evalP(Pm, ustar) == -1 and len(neg) > 0 and len(cont) > 0 and all(p in neg for p in cont)
    ctrl['G4_%s_mutated_minus_value_at_ones' % nm] = {'P(1^6)': str(v), 'mutant_value_at_ones': str(evalP(Pm, ustar)), 'leaves_with_negative_coeff': len(neg),
                                                       'leaves_with_nonpositive_interior_vertex': len(st['nonpos_interior_vertex_leaves']),
                                                       'leaves_containing_x*=(1/2)^6': len(cont), 'all_containing_leaves_rejected': all(p in neg for p in cont)}
    check('NEG G4-%s: P-(P(1^6)+1) rejected; every leaf containing x*=(1/2)^6 has a negative coefficient' % nm, ok, ctrl['G4_%s_mutated_minus_value_at_ones' % nm], scope='G4')
for nm, P, L in (('Q', Qpol, QL), ('H', Hpol, HL)):
    st = g4_replay(P, L, reverse=True, crosscheck=False)
    ctrl['G4_%s_reversed_bit_convention' % nm] = {'leaves_with_negative_coeff': len(st['neg_leaves']), 'leaves_with_nonpositive_interior_vertex': len(st['nonpos_interior_vertex_leaves'])}
    check('NEG G4-%s: reversed bit convention (0=upper) rejected' % nm, len(st['neg_leaves']) + len(st['nonpos_interior_vertex_leaves']) > 0, ctrl['G4_%s_reversed_bit_convention' % nm], scope='G4')
stRr = rs_replay(POLYS3, RL, reverse=True, full=False)
ctrl['RS_reversed_bit_convention'] = {'label_failures': len(stRr['label_fail'])}
check('NEG RS: reversed bit convention (0=upper) rejected', len(stRr['label_fail']) > 0, ctrl['RS_reversed_bit_convention'], scope='RS')
for nm, ps in (('G4-Q', list(QL)), ('RS', [p for p, _ in RL])):
    dropped = ps[:-1]
    dup = ps + [ps[0]]
    ext = ps + [ps[0] + '0']
    res = {'drop_last': structure(dropped)[0], 'duplicate_first': structure(dup)[0], 'child_of_first': structure(ext)[0]}
    ok = any('Kraft' in s or 'uncovered' in s for s in res['drop_last']) and any('duplicate' in s for s in res['duplicate_first']) and any('prefix collision' in s for s in res['child_of_first'])
    ctrl['%s_structural' % nm] = res
    check('NEG %s: missing leaf -> gap; duplicate -> duplicate; child of leaf -> prefix collision' % nm, ok, res, scope=nm[:2])
relab = None
for path, lab in RL:
    if lab == 'Abar<=0':
        ks, ns = box_from_path(path, 3)
        box = tuple((Fr(ks[a], 2 ** ns[a]), Fr(ks[a] + 1, 2 ** ns[a])) for a in range(3))
        if max(r1_local(PD, box).values()) > 0:
            relab = path
            break
RLm = [[p, ('Dbar<=0' if p == relab else l)] for p, l in RL]
stm = rs_replay(POLYS3, RLm, full=False)
ctrl['RS_relabel'] = {'leaf': relab, 'from': 'Abar<=0', 'to': 'Dbar<=0', 'failures': stm['label_fail']}
check('NEG RS: relabelling one Abar leaf as Dbar<=0 rejected (positive Dbar coefficient)', relab is not None and len(stm['label_fail']) == 1 and stm['label_fail'][0][0] == relab, ctrl['RS_relabel'], scope='RS')
PAm = padd(PA, const(144, 3))     # 74/9 -> 83/9 in Abar
stm = rs_replay({'Abar': PAm, 'Dbar': PD, 'f1minus4': PF}, RL, full=False)
ctrl['RS_Abar_constant_74/9_to_83/9'] = {'label_failures': len(stm['label_fail']), 'examples': stm['label_fail'][:3]}
check('NEG RS: Abar with 74/9 replaced by 83/9 rejected (positive Abar coefficient on some Abar leaf)', len(stm['label_fail']) > 0 and all(l == 'Abar<=0' for _, l, _ in stm['label_fail']), ctrl['RS_Abar_constant_74/9_to_83/9'], scope='RS')
PFm = padd(PF, const(1, 3))       # f1-4 -> f1-7/2
stm = rs_replay({'Abar': PA, 'Dbar': PD, 'f1minus4': PFm}, RL, full=False)
ctrl['RS_f1_threshold_4_to_7/2'] = {'label_failures': len(stm['label_fail']), 'examples': stm['label_fail'][:3]}
check('NEG RS: f1-4 replaced by f1-7/2 rejected (nonnegative coefficient on some f1 leaf)', len(stm['label_fail']) > 0 and all(l == 'f1-4<0' for _, l, _ in stm['label_fail']), ctrl['RS_f1_threshold_4_to_7/2'], scope='RS')

# ------------------------------------------------------------------ verdict + outputs
REC['verdict_G4'] = 'COMPLETE_VALID' if not [n for sc, n in FAILED if sc in ('G4', 'both')] else 'INVALID_OR_FAILED_CHECK'
REC['verdict_RS'] = 'COMPLETE_VALID' if not [n for sc, n in FAILED if sc in ('RS', 'both')] else 'INVALID_OR_FAILED_CHECK'
REC['supplementary_ok'] = not [n for sc, n in FAILED if sc == 'supp']
REC['failed_checks'] = FAILED
REC['n_checks'] = len(REC['checks'])
REC['seconds'] = round(time.time() - T0, 2)
REC['clock_end'] = clock()
log('failed checks:', FAILED)
log('verdict_G4', REC['verdict_G4'], 'verdict_RS', REC['verdict_RS'], 'checks', REC['n_checks'], 'seconds', REC['seconds'])
log('clock_end', REC['clock_end'])
if '--dry-run' in sys.argv:
    print('dry run: no output files written')
else:
    with open(OUT_JSON, 'x') as fh:
        fh.write(json.dumps(REC, indent=1, default=str, sort_keys=True) + '\n')
    with open(OUT_LOG, 'x') as fh:
        fh.write('\n'.join(LOG) + '\n')
    print('wrote', OUT_JSON, OUT_LOG)
sys.exit(1 if FAILED else 0)
