#!/usr/bin/env python3
"""proof-review-v1-exact-controls.py  (f148 proof review; written from scratch by the reviewer)

Independent exact controls for the candidate
  "PH7 at z=8/9: one directed 3-cycle, no 2-/4-cycle, is impossible".
Standard library only (fractions/itertools/json/hashlib).  No author checker or replay is
imported or executed; the author certificate JSON is opened as DATA only (digests, degrees,
term counts, leaf paths).

Parts
  A  symbolic reconstruction of (EQ) from first principles (ring Q[u0..u4,theta,t,r]):
     affine structure in (t,r), closed forms a00..c1, den/tn/rn/N, theta-degree 3, Cramer
     identities, Bernstein coefficients b0..b3, integrality, (BERN) identity, PD-determinant
     identity, term counts / degrees / canonical digests, digest-sensitivity negative controls
  B  exact rational 7x7 Metzler matrices in the graph class (seeded random, with 5/6/7-cycles):
     Faddeev-LeVerrier charpoly == full cycle-cover expansion == direct determinant;
     y^6..y^3 class formulas; (THETA) on row generators; E4/E3 == actual coefficient defects;
     negative controls adding a 2-cycle / 4-cycle / second triangle (formula must fail by
     exactly the new cycle weight)
  C  exact point controls: den/tn/rn/N, Cramer solution satisfies (EQ), t^2-4r = -N/(19683 den^2),
     theta=0/1 endpoints, Bernstein identity at points, PD criterion, den theta-root search,
     extreme-magnitude sweep, cubic negative control
  D  full structural parse of the author certificate (sha, metadata, every leaf list: binary,
     distinct, prefix-free, Kraft-complete, both children, depth>=5, open-cube corner)
  E  bounded own-implementation spot check of 12 certificate leaves (exact Fractions, own
     de Casteljau) with a negative control -- a SAMPLE, not a universality claim

Run history: run 1 (log ...-run1-reviewer-expectation-bug.txt) failed only B.7/2cycle because the
reviewer's expected delta omitted the added 2-cycle's fixed-point product (it feeds y^4 and y^3
too); the expectation was generalized to -w_C e_{7-L-d}(outside C). No author material changed.
"""
import hashlib, itertools, json, math, platform, random, sys, time
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Fr

CERT_PATH = ('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/'
             'parallel-18/phase-type/frontier-20261028-ph7-one-triangle-full-critical-certificate.json')
CERT_SHA = 'd1195a6f0099d105eb34e5a6acbeb1fec3d81c333658af7a3c8b2ea5ac79f2c9'
LOG = open(sys.argv[1], 'w') if len(sys.argv) > 1 else None
Z = Fr(8, 9)
FAILS = []


def out(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    if LOG:
        LOG.write(s + '\n'); LOG.flush()


def check(cond, msg):
    out('PASS' if cond else 'FAIL', msg)
    if not cond:
        FAILS.append(msg)


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


T0 = time.monotonic()
out('start_utc', utc(), 'python', platform.python_version(), platform.machine())
out('script_sha256', hashlib.sha256(open(__file__, 'rb').read()).hexdigest())

# ----------------------------------------------------------------------------
# sparse multivariate polynomials over Q; ring variables:
#   0..4 = u0..u4  (u0,u1,u2 triangle rates; u3,u4 chosen outside rates)
#   5 = theta, 6 = t (or v1), 7 = r (or v2)
NV = 8
IU, ITH, IT, IR = (0, 1, 2, 3, 4), 5, 6, 7
ZERO = (0,) * NV


def P_const(c):
    c = Fr(c)
    return {ZERO: c} if c else {}


def P_var(i):
    e = [0] * NV; e[i] = 1
    return {tuple(e): Fr(1)}


def P_add(a, b):
    o = dict(a)
    for k, v in b.items():
        s_ = o.get(k, 0) + v
        if s_:
            o[k] = s_
        else:
            o.pop(k, None)
    return o


def P_scale(a, c):
    c = Fr(c)
    return {k: v * c for k, v in a.items()} if c else {}


def P_sub(a, b):
    return P_add(a, P_scale(b, -1))


def P_mul(a, b):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple([x + y for x, y in zip(ka, kb)])
            o[k] = o.get(k, 0) + va * vb
    return {k: v for k, v in o.items() if v}


def P_sum(*ps):
    o = {}
    for p_ in ps:
        o = P_add(o, p_)
    return o


def P_deg(a, i):
    return max((k[i] for k in a), default=-1)


def P_coeff(a, i, m):
    """coefficient polynomial of var_i^m (var_i exponent zeroed)."""
    o = {}
    for k, v in a.items():
        if k[i] == m:
            kk = list(k); kk[i] = 0
            o[tuple(kk)] = v
    return o


def P_uses(a, i):
    return any(k[i] for k in a)


def P_eval(a, vals):
    tot = Fr(0)
    for k, v in a.items():
        term = v
        for i, e_ in enumerate(k):
            if e_:
                term *= Fr(vals[i]) ** e_
        tot += term
    return tot


def esym(polys, k):
    o = {}
    for comb in itertools.combinations(polys, k):
        pr = P_const(1)
        for p_ in comb:
            pr = P_mul(pr, p_)
        o = P_add(o, pr)
    return o


def to5(a):
    """project a polynomial free of theta,t,r to a 5-tuple integer dict (asserts integrality)."""
    o = {}
    for k, v in a.items():
        assert not (k[ITH] or k[IT] or k[IR]), k
        assert v.denominator == 1, (k, v)
        o[k[:5]] = int(v)
    return o


def digest5(p5):
    rows = [[list(k), str(int(c))] for k, c in sorted(p5.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


# ============================================================================
out('\n===== PART A: symbolic reconstruction =====')
U = [P_var(i) for i in IU]
TH, T, R = P_var(ITH), P_var(IT), P_var(IR)
s = [P_const(1)] + [esym(U, k) for k in (1, 2, 3, 4, 5)]          # s[0..5] of u0..u4
W = P_mul(TH, P_mul(U[0], P_mul(U[1], U[2])))                       # triangle product w = theta u0 u1 u2
O = P_add(U[3], U[4])

# A.0 identity e_k(u0..u4, v1, v2) = s_k + (v1+v2) s_{k-1} + v1 v2 s_{k-2}  (v1,v2 = ring vars 6,7)
V1, V2 = P_var(IT), P_var(IR)
ok = True
for k in range(1, 5):
    lhs = esym(U + [V1, V2], k)
    rhs = P_sum(s[k], P_mul(P_add(V1, V2), s[k - 1]), P_mul(P_mul(V1, V2), s[k - 2]) if k >= 2 else {})
    ok &= (lhs == rhs)
check(ok, 'A.0 e_k(u0..u4,v1,v2) = s_k + t s_{k-1} + r s_{k-2} for k=1..4 (symbolic)')


def e7(k):  # elementary symmetric of all seven rates in (s, t, r) form
    return P_sum(s[k], P_mul(T, s[k - 1]), P_mul(R, s[k - 2]) if k >= 2 else {})


# A.1 actual characteristic coefficients in the class (derivation: review section 2)
chi = {7: P_const(1), 6: e7(1), 5: e7(2), 4: P_sub(e7(3), W), 3: P_sub(e7(4), P_mul(W, P_add(O, T)))}
# A.2 D(y) = y[(y+1)^2 + z]^2 from scratch
k17 = 1 + Z
D = [Fr(1), Fr(4), 4 + 2 * k17, 4 * k17, k17 ** 2, Fr(0)]           # y^5 .. y^0
check(D == [1, 4, Fr(70, 9), Fr(68, 9), Fr(289, 81), 0], 'A.2 D(y) coefficients = 1,4,70/9,68/9,289/81,0')
# A.3 D*Q, Q=y^2+py+q: coeff y^(7-j) = D[j] + p D[j-1] + q D[j-2]; solve p,q from y^6,y^5
p = P_sub(chi[6], P_const(D[1]))
q = P_sub(P_sub(chi[5], P_const(D[2])), P_scale(p, D[1]))
E4 = P_sub(chi[4], P_sum(P_const(D[3]), P_scale(p, D[2]), P_scale(q, D[1])))
E3 = P_sub(chi[3], P_sum(P_const(D[4]), P_scale(p, D[3]), P_scale(q, D[2])))
# manuscript display (EQ) built separately for comparison
m_p = P_sum(s[1], T, P_const(-4))
m_q = P_sum(s[2], P_mul(T, s[1]), R, P_scale(m_p, -4), P_const(Fr(-70, 9)))
m_E4 = P_sum(s[3], P_mul(T, s[2]), P_mul(R, s[1]), P_scale(W, -1),
             P_scale(m_q, -4), P_scale(m_p, Fr(-70, 9)), P_const(Fr(-68, 9)))
m_E3 = P_sum(s[4], P_mul(T, s[3]), P_mul(R, s[2]), P_scale(P_mul(W, P_add(O, T)), -1),
             P_scale(m_q, Fr(-70, 9)), P_scale(m_p, Fr(-68, 9)), P_const(Fr(-289, 81)))
check(p == m_p and q == m_q, 'A.3 p,q from first principles equal manuscript p=s1+t-4, q=s2+ts1+r-4p-70/9')
check(E4 == m_E4 and E3 == m_E3, 'A.3 E4,E3 from first principles equal manuscript (EQ)')

# A.4 affine structure in (t,r)
for E, nm in ((E4, 'E4'), (E3, 'E3')):
    aff = P_deg(E, IT) <= 1 and P_deg(E, IR) <= 1 and not any(k[IT] and k[IR] for k in E)
    check(aff, f'A.4 {nm} is affine in (t,r) (no t^2, r^2, t*r)')
a00, a01 = P_coeff(E4, IT, 1), P_coeff(E4, IR, 1)
a10, a11 = P_coeff(E3, IT, 1), P_coeff(E3, IR, 1)
c0 = P_coeff(P_coeff(E4, IT, 0), IR, 0)
c1 = P_coeff(P_coeff(E3, IT, 0), IR, 0)
check(E4 == P_sum(P_mul(a00, T), P_mul(a01, R), c0) and E3 == P_sum(P_mul(a10, T), P_mul(a11, R), c1),
      'A.4 E4 = a00 t + a01 r + c0 ; E3 = a10 t + a11 r + c1 (exact split)')
# A.5 reviewer hand closed forms
h_a00 = P_sum(s[2], P_scale(s[1], -4), P_const(Fr(74, 9)))
h_a01 = P_sub(s[1], P_const(4))
h_a10 = P_sum(s[3], P_scale(W, -1), P_scale(s[1], Fr(-70, 9)), P_const(Fr(212, 9)))
h_a11 = P_sub(s[2], P_const(Fr(70, 9)))
h_c0 = P_sum(s[3], P_scale(s[2], -4), P_scale(s[1], Fr(74, 9)), P_const(Fr(-28, 3)), P_scale(W, -1))
h_c1 = P_sum(s[4], P_scale(P_mul(W, O), -1), P_scale(s[2], Fr(-70, 9)), P_scale(s[1], Fr(212, 9)),
             P_const(Fr(-1007, 27)))
check(a00 == h_a00, 'A.5 a00 = s2 - 4 s1 + 74/9')
check(a01 == h_a01, 'A.5 a01 = s1 - 4')
check(a10 == h_a10, 'A.5 a10 = s3 - w - (70/9) s1 + 212/9')
check(a11 == h_a11, 'A.5 a11 = s2 - 70/9')
check(c0 == h_c0, 'A.5 c0 = s3 - 4 s2 + (74/9) s1 - 28/3 - w')
check(c1 == h_c1, 'A.5 c1 = s4 - w O - (70/9) s2 + (212/9) s1 - 1007/27')

# A.6 den, tn, rn, N; Cramer identities; theta degree
den = P_sub(P_mul(a00, a11), P_mul(a01, a10))
tn = P_add(P_scale(P_mul(c0, a11), -1), P_mul(a01, c1))
rn = P_add(P_scale(P_mul(a00, c1), -1), P_mul(c0, a10))
check(P_add(P_mul(a00, tn), P_mul(a01, rn)) == P_scale(P_mul(c0, den), -1) and
      P_add(P_mul(a10, tn), P_mul(a11, rn)) == P_scale(P_mul(c1, den), -1),
      'A.6 Cramer identities a00 tn + a01 rn = -c0 den, a10 tn + a11 rn = -c1 den (symbolic)')
N = P_scale(P_sub(P_mul(tn, tn), P_scale(P_mul(rn, den), 4)), -19683)
check(19683 == 3 ** 9, 'A.6 19683 = 3^9')
check(P_deg(N, ITH) == 3, f'A.6 N has theta-degree 3 (observed {P_deg(N, ITH)})')
check(not P_uses(N, IT) and not P_uses(N, IR), 'A.6 N is free of t and r')
check(P_deg(den, ITH) == 1 and P_deg(tn, ITH) == 1 and P_deg(rn, ITH) == 2,
      f'A.6 theta-degrees den={P_deg(den, ITH)} tn={P_deg(tn, ITH)} rn={P_deg(rn, ITH)}')
out('info terms: den', len(den), 'tn', len(tn), 'rn', len(rn), 'N', len(N))
check(P_sub(den, P_mul(a11, a11)) == P_mul(P_sub(s[1], P_const(4)), P_sub(P_scale(a11, -4), a10)),
      'A.6 side identity den - a11^2 = (s1-4)(-4 a11 - a10)  (so den = a11^2 on the slice s1=4)')

# A.7 Bernstein coefficients in theta on [0,1]
Ncoef = [P_coeff(N, ITH, j) for j in range(4)]
b = []
for k in range(4):
    bk = {}
    for j in range(k + 1):
        bk = P_add(bk, P_scale(Ncoef[j], Fr(math.comb(k, j), math.comb(3, j))))
    b.append(bk)
one_m = P_sub(P_const(1), TH)
Bern = [P_mul(one_m, P_mul(one_m, one_m)),
        P_scale(P_mul(TH, P_mul(one_m, one_m)), 3),
        P_scale(P_mul(P_mul(TH, TH), one_m), 3),
        P_mul(TH, P_mul(TH, TH))]
check(P_sum(*[P_mul(b[k], Bern[k]) for k in range(4)]) == N,
      'A.7 (BERN) N = b0(1-th)^3 + 3b1 th(1-th)^2 + 3b2 th^2(1-th) + b3 th^3 (symbolic)')
check(b[0] == Ncoef[0] and b[3] == P_sum(*Ncoef), 'A.7 b0 = N(0), b3 = N(1)')
check(all(v.denominator == 1 for bk in b for v in bk.values()), 'A.7 all Bernstein coefficients b0..b3 are integers')
Ntest = P_scale(N, Fr(1, 3))
bt = []
for k in range(4):
    bk = {}
    for j in range(k + 1):
        bk = P_add(bk, P_scale(P_coeff(Ntest, ITH, j), Fr(math.comb(k, j), math.comb(3, j))))
    bt.append(bk)
out('info with scale 3^8 instead of 3^9, all Bernstein coefficients integer?', all(v.denominator == 1 for bk in bt for v in bk.values()))
G = P_sub(P_scale(P_mul(b[1], b[3]), 4), P_scale(P_mul(b[2], b[2]), 3))
check(P_sub(P_scale(P_mul(b[1], b[3]), 3), P_scale(P_mul(b[2], b[2]), Fr(9, 4))) == P_scale(G, Fr(3, 4)),
      'A.7 det[[3b1,3b2/2],[3b2/2,b3]] = (3/4)(4 b1 b3 - 3 b2^2) (symbolic)')
# bracket as quadratic form: [1-th, th] M [1-th, th]^T with M = [[3b1,3b2/2],[3b2/2,b3]]
bracket = P_sum(P_scale(P_mul(b[1], P_mul(one_m, one_m)), 3), P_scale(P_mul(b[2], P_mul(TH, one_m)), 3), P_mul(b[3], P_mul(TH, TH)))
check(P_add(P_mul(b[0], Bern[0]), P_mul(TH, bracket)) == N, 'A.7 N = b0(1-th)^3 + th*bracket (symbolic)')

P5 = {'b0': to5(b[0]), 'b1': to5(b[1]), 'b2': to5(b[2]), 'b3': to5(b[3]), 'quadratic_discriminant': to5(G)}
for nm, p5 in P5.items():
    out('info', nm, 'terms', len(p5), 'individual_degrees', [max(k[j] for k in p5) for j in range(5)],
        'digest', digest5(p5))
check(len(P5['b0']) == 1753 and len(P5['b1']) == 1753 and len(P5['b3']) == 1717 and len(P5['quadratic_discriminant']) == 31422,
      'A.8 term counts 1753,1753,1717,31422 as in manuscript section 4')
sym = all(P_eval(b[0], [Fr(2), Fr(3), Fr(5), Fr(7), Fr(11), Fr(1, 3), 0, 0]) == P_eval(b[0], [Fr(x) for x in perm] + [Fr(1, 3), 0, 0])
          for perm in itertools.permutations([2, 3, 5]) for _ in [0]
          for perm in [list(perm) + [7, 11]])
sym2 = all(P_eval(G, [Fr(2), Fr(3), Fr(5), Fr(7), Fr(11), 0, 0, 0]) == P_eval(G, [Fr(x) for x in perm] + [0, 0, 0])
           for perm in ([2, 3, 5, 11, 7], [5, 2, 3, 7, 11], [3, 5, 2, 11, 7]))
check(sym and sym2, 'A.8 b0 and G are symmetric in (u0,u1,u2) and in (u3,u4) at a test point')


# A.9 digest-sensitivity negative controls (intended failures)
def N_from(E4_, E3_):
    a00_, a01_ = P_coeff(E4_, IT, 1), P_coeff(E4_, IR, 1)
    a10_, a11_ = P_coeff(E3_, IT, 1), P_coeff(E3_, IR, 1)
    c0_ = P_coeff(P_coeff(E4_, IT, 0), IR, 0); c1_ = P_coeff(P_coeff(E3_, IT, 0), IR, 0)
    den_ = P_sub(P_mul(a00_, a11_), P_mul(a01_, a10_))
    tn_ = P_add(P_scale(P_mul(c0_, a11_), -1), P_mul(a01_, c1_))
    rn_ = P_add(P_scale(P_mul(a00_, c1_), -1), P_mul(c0_, a10_))
    return P_scale(P_sub(P_mul(tn_, tn_), P_scale(P_mul(rn_, den_), 4)), -19683)


def bern_of(N_):
    bb = []
    for k in range(4):
        bk = {}
        for j in range(k + 1):
            bk = P_add(bk, P_scale(P_coeff(N_, ITH, j), Fr(math.comb(k, j), math.comb(3, j))))
        bb.append(bk)
    return bb


def safe_digest(poly):
    try:
        return digest5(poly)
    except AssertionError:
        return 'NON-INTEGER'


#  (i) z -> 1 changes D and must change the b0 digest
k17x = 1 + Fr(1)
Dx = [Fr(1), Fr(4), 4 + 2 * k17x, 4 * k17x, k17x ** 2, Fr(0)]
px = P_sub(chi[6], P_const(Dx[1])); qx = P_sub(P_sub(chi[5], P_const(Dx[2])), P_scale(px, Dx[1]))
E4x = P_sub(chi[4], P_sum(P_const(Dx[3]), P_scale(px, Dx[2]), P_scale(qx, Dx[1])))
E3x = P_sub(chi[3], P_sum(P_const(Dx[4]), P_scale(px, Dx[3]), P_scale(qx, Dx[2])))
bx = bern_of(N_from(E4x, E3x))
#  (ii) drop the triangle's -w t contribution to y^3 (wrong no-4-cycle accounting)
E3y = P_add(E3, P_mul(W, T))
by = bern_of(N_from(E4, E3y))
dx0, dy3 = safe_digest(bx[0]), safe_digest(by[3])
check(dx0 != digest5(P5['b0']) and dy3 != digest5(P5['b3']),
      f'A.9 negative controls: z=1 b0 digest {dx0[:16]}.. and dropped -w t b3 digest {dy3[:16]}.. both differ from reviewer digests')

# ============================================================================
out('\n===== PART B: exact rational matrices in the graph class =====')
rng = random.Random(148_2026_1029)
n = 7


def upoly_mul(a, b_):
    o = [Fr(0)] * (len(a) + len(b_) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b_):
            o[i + j] += x * y
    return o


def simple_cycles(arcs):
    cyc = []

    def dfs(start, v, path, vis):
        for w_ in range(n):
            if (v, w_) in arcs:
                if w_ == start:
                    cyc.append(tuple(path))
                elif w_ > start and w_ not in vis:
                    vis.add(w_); path.append(w_)
                    dfs(start, w_, path, vis)
                    path.pop(); vis.remove(w_)

    for st in range(n):
        dfs(st, st, [st], {st})
    return cyc


def strongly_connected(arcs):
    def reach(fwd):
        seen = {0}; stack = [0]
        while stack:
            v = stack.pop()
            for w_ in range(n):
                e_ = (v, w_) if fwd else (w_, v)
                if e_ in arcs and w_ not in seen:
                    seen.add(w_); stack.append(w_)
        return len(seen) == n
    return reach(True) and reach(False)


def charpoly_FL(A):
    """Faddeev-LeVerrier: c[j] = coefficient of y^j of det(yI - A)."""
    c = [Fr(0)] * (n + 1); c[n] = Fr(1)
    M = [[Fr(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        AM = [[sum(A[i][l] * M[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        for i in range(n):
            AM[i][i] += c[n - k + 1]
        M = AM
        tr = sum(sum(A[i][l] * M[l][i] for l in range(n)) for i in range(n))
        c[n - k] = -tr / k
    return c


def det_frac(Mx):
    Mx = [row[:] for row in Mx]; m = len(Mx); d = Fr(1)
    for col in range(m):
        piv = next((r_ for r_ in range(col, m) if Mx[r_][col] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != col:
            Mx[col], Mx[piv] = Mx[piv], Mx[col]; d = -d
        d *= Mx[col][col]
        for r_ in range(col + 1, m):
            f = Mx[r_][col] / Mx[col][col]
            if f:
                for cc in range(col, m):
                    Mx[r_][cc] -= f * Mx[col][cc]
    return d


def cycle_weight(A, cyc):
    w_ = Fr(1)
    for i in range(len(cyc)):
        w_ *= A[cyc[i]][cyc[(i + 1) % len(cyc)]]
    return w_


def cycle_cover_charpoly(A, cycles):
    """det(yI-A) = sum over vertex-disjoint cycle families F of prod_{C in F}(-w_C) prod_{i not in V(F)} (y+u_i)."""
    u = [-A[i][i] for i in range(n)]
    res = [Fr(0)] * (n + 1)

    def rec(idx, used, wgt):
        poly = [Fr(1)]
        for i in range(n):
            if i not in used:
                poly = upoly_mul(poly, [u[i], Fr(1)])
        for j, cf in enumerate(poly):
            res[j] += wgt * cf
        for c_ in range(idx, len(cycles)):
            vs = set(cycles[c_])
            if vs & used:
                continue
            rec(c_ + 1, used | vs, wgt * (-cycle_weight(A, cycles[c_])))

    rec(0, frozenset(), Fr(1))
    return res


def esym_vals(vals, k):
    return sum((math.prod(cb) for cb in itertools.combinations(vals, k)), Fr(0))


TRI = {(0, 1), (1, 2), (2, 0)}
others = [(i, j) for i in range(n) for j in range(n) if i != j and (i, j) not in TRI]


def sample_graph():
    tries = 0
    while True:
        tries += 1
        arcs = set(TRI) | set(rng.sample(others, rng.randint(5, 11)))
        cyc = simple_cycles(arcs)
        h = Counter(len(c_) for c_ in cyc)
        if h[2] == 0 and h[3] == 1 and h[4] == 0 and strongly_connected(arcs):
            return arcs, cyc, h, tries


def random_matrix(arcs, generator=True):
    A = [[Fr(0)] * n for _ in range(n)]
    for (i, j) in arcs:
        A[i][j] = Fr(rng.randint(1, 60), rng.randint(1, 7))
    for i in range(n):
        A[i][i] = -(sum(A[i]) if generator else Fr(rng.randint(1, 60), rng.randint(1, 7)))
    return A


def class_formula(A):
    u = [-A[i][i] for i in range(n)]
    wD = cycle_weight(A, (0, 1, 2))
    return {6: esym_vals(u, 1), 5: esym_vals(u, 2), 4: esym_vals(u, 3) - wD,
            3: esym_vals(u, 4) - wD * esym_vals(u[3:], 1)}, u, wD


graphs = []
want = 6
seen_long = Counter()
while len(graphs) < want:
    arcs, cyc, h, tries = sample_graph()
    graphs.append((arcs, cyc, h))
    seen_long.update({L: 1 for L in h if L >= 5})
    out(f'info graph#{len(graphs)} arcs={len(arcs)} cycle-length histogram={dict(sorted(h.items()))} '
        f'(after {tries} draws) arcs={sorted(arcs)}')
check(seen_long[5] > 0 and seen_long[6] > 0 and seen_long[7] > 0,
      f'B.0 sampled class graphs include 5-, 6- and 7-cycles (graph counts by length: {dict(seen_long)})')

for gi, (arcs, cyc, h) in enumerate(graphs, 1):
    disjoint_pairs = sum(1 for a_, b_ in itertools.combinations(cyc, 2) if not (set(a_) & set(b_)))
    check(disjoint_pairs == 0, f'B.1 graph#{gi}: no two vertex-disjoint cycles exist ({len(cyc)} simple cycles)')
    for gen_flag in (True, False):
        A = random_matrix(arcs, gen_flag)
        c = charpoly_FL(A)
        cc = cycle_cover_charpoly(A, cyc)
        check(c == cc, f'B.2 graph#{gi} generator={gen_flag}: Faddeev-LeVerrier == full cycle-cover expansion')
        y0 = Fr(rng.randint(-9, 9), rng.randint(1, 4))
        direct = det_frac([[(y0 if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)])
        check(sum(c[j] * y0 ** j for j in range(n + 1)) == direct, f'B.2 graph#{gi} generator={gen_flag}: charpoly(y0) == direct det(y0 I - A)')
        cf, u, wD = class_formula(A)
        check(all(c[d_] == cf[d_] for d_ in (6, 5, 4, 3)), f'B.3 graph#{gi} generator={gen_flag}: y^6..y^3 == e1, e2, e3-w, e4-w(O+t)')
        theta = wD / (u[0] * u[1] * u[2])
        if gen_flag:
            check(c[0] == 0, f'B.3 graph#{gi}: generator has chi(0)=0')
            check(0 < theta < 1, f'B.4 graph#{gi}: row generator gives theta = w/(u1u2u3) = {theta} in (0,1)')
            check(all(ui > 0 for ui in u), f'B.4 graph#{gi}: all seven diagonal rates positive')
        pv = c[6] - 4; qv = c[5] - 4 * pv - Fr(70, 9)
        E4_actual = c[4] - (4 * qv + Fr(70, 9) * pv + Fr(68, 9))
        E3_actual = c[3] - (Fr(70, 9) * qv + Fr(68, 9) * pv + Fr(289, 81))
        vals = [u[0], u[1], u[2], u[3], u[4], theta, u[5] + u[6], u[5] * u[6]]
        check(P_eval(E4, vals) == E4_actual and P_eval(E3, vals) == E3_actual,
              f'B.5 graph#{gi} generator={gen_flag}: symbolic E4,E3 at the matrix point == actual y^4,y^3 defects vs D*Q')
        dv = P_eval(den, vals)
        if dv != 0 and gen_flag:
            tv, rv = P_eval(tn, vals) / dv, P_eval(rn, vals) / dv
            Nv = P_eval(N, vals)
            check(tv * tv - 4 * rv == -Nv / (19683 * dv * dv), f'B.5 graph#{gi}: t^2-4r = -N/(19683 den^2) at the matrix point')
            out(f'info graph#{gi}: actual (t,r)=({u[5] + u[6]},{u[5] * u[6]}) vs D-forced ({tv},{rv}); N={float(Nv):.6g} den={float(dv):.6g}')
        rem = c[:]
        for d_ in range(n, 4, -1):
            lead = rem[d_]
            if lead:
                for j, dc in enumerate(D):
                    rem[d_ - j] -= lead * dc
        check(any(rem[j] != 0 for j in range(5)), f'B.6 graph#{gi} generator={gen_flag}: D does not divide chi (nonzero remainder)')

# negative controls: add exactly one arc creating exactly one new short cycle
found = {'2cycle': False, '4cycle': False, 'triangle': False}
for gi, (arcs, cyc, h) in enumerate(graphs, 1):
    for arc in others:
        if arc in arcs:
            continue
        arcs2 = set(arcs) | {arc}
        cyc2 = simple_cycles(arcs2)
        h2 = Counter(len(c_) for c_ in cyc2)
        kind = None
        if h2[2] == 1 and h2[3] == 1 and h2[4] == 0:
            kind = '2cycle'
        elif h2[2] == 0 and h2[3] == 1 and h2[4] == 1:
            kind = '4cycle'
        elif h2[2] == 0 and h2[3] == 2 and h2[4] == 0:
            kind = 'triangle'
        if kind is None or found[kind]:
            continue
        found[kind] = True
        A = random_matrix(arcs2, True)
        c = charpoly_FL(A)
        check(c == cycle_cover_charpoly(A, cyc2), f'B.7 negative control {kind} (graph#{gi} + arc {arc}): FL == cycle-cover expansion')
        cf, u, wD = class_formula(A)
        Lnew = {'2cycle': 2, '4cycle': 4, 'triangle': 3}[kind]
        new = [c_ for c_ in cyc2 if len(c_) == Lnew and set(c_) != {0, 1, 2}]
        assert len(new) == 1, new
        wnew = cycle_weight(A, new[0])
        # the new cycle C adds -w_C * prod_{i not in C}(y+u_i): degree d gets -w_C e_{7-L-d}(rates outside C)
        outside_new = [u[i] for i in range(n) if i not in new[0]]
        expect = {d_: (-wnew * esym_vals(outside_new, 7 - Lnew - d_) if 7 - Lnew - d_ >= 0 else 0) for d_ in (6, 5, 4, 3)}
        diffs = {d_: c[d_] - cf[d_] for d_ in (6, 5, 4, 3)}
        check(diffs == expect and any(expect.values()),
              f'B.7 negative control {kind} new cycle {new[0]}: class formula fails by exactly the new cycle contribution {expect}')
check(all(found.values()), f'B.7 all three negative controls executed: {found}')

# ============================================================================
out('\n===== PART C: exact point controls (samples; NOT a universality proof) =====')
rng2 = random.Random(2026_10_29)


def rand_pos():
    return Fr(rng2.randint(1, 500), rng2.randint(1, 50))


npts = 40
n_den_pos = n_den_neg = n_den_zero = 0
n_N_pos = 0
n_pd = 0
root_in_unit = 0
pt_fail = 0
for trial in range(npts):
    uv = [rand_pos() for _ in range(5)]
    d0 = P_eval(den, uv + [0, 0, 0]); d1 = P_eval(den, uv + [1, 0, 0])
    if d1 != d0:
        th_star = -d0 / (d1 - d0)
        if 0 <= th_star <= 1:
            root_in_unit += 1
    for th in (Fr(0), Fr(1), Fr(rng2.randint(1, 999), 1000), Fr(rng2.randint(1, 31), 32)):
        vals = uv + [th, 0, 0]
        A00, A01, A10, A11 = (P_eval(x, vals) for x in (a00, a01, a10, a11))
        C0, C1 = P_eval(c0, vals), P_eval(c1, vals)
        dv = A00 * A11 - A01 * A10
        tnv = -C0 * A11 + A01 * C1; rnv = -A00 * C1 + C0 * A10
        Nv = P_eval(N, vals)
        if not (dv == P_eval(den, vals) and tnv == P_eval(tn, vals) and rnv == P_eval(rn, vals)
                and Nv == -19683 * (tnv * tnv - 4 * rnv * dv)):
            pt_fail += 1; check(False, f'C.1 trial {trial} th={th}: pointwise den/tn/rn/N mismatch')
        if dv == 0:
            n_den_zero += 1
            check(Nv == -19683 * tnv * tnv and Nv <= 0, f'C.2 trial {trial}: den=0 => N = -19683 tn^2 <= 0')
        else:
            n_den_pos += dv > 0; n_den_neg += dv < 0
            tv, rv = tnv / dv, rnv / dv
            if not (P_eval(E4, uv + [th, tv, rv]) == 0 and P_eval(E3, uv + [th, tv, rv]) == 0):
                pt_fail += 1; check(False, f'C.3 trial {trial} th={th}: Cramer (t,r) does not satisfy (EQ)')
            if not (tv * tv - 4 * rv == -Nv / (19683 * dv * dv)):
                pt_fail += 1; check(False, f'C.3 trial {trial} th={th}: t^2-4r identity fails')
        bv = [P_eval(bk, vals) for bk in b]
        if not (Nv == bv[0] * (1 - th) ** 3 + 3 * bv[1] * th * (1 - th) ** 2 + 3 * bv[2] * th ** 2 * (1 - th) + bv[3] * th ** 3):
            pt_fail += 1; check(False, f'C.4 trial {trial} th={th}: Bernstein identity at point fails')
        if (th == 0 and Nv != bv[0]) or (th == 1 and Nv != bv[3]):
            pt_fail += 1; check(False, f'C.4 trial {trial}: endpoint N(0)=b0 / N(1)=b3 fails')
        n_N_pos += Nv > 0
        Gv = P_eval(G, vals)
        n_pd += (bv[0] > 0 and bv[1] > 0 and bv[3] > 0 and Gv > 0)
check(pt_fail == 0, f'C.1-C.4 {npts} rate points x 4 theta values (incl. theta=0,1): all pointwise identities held')
out(f'info samples: den>0 {n_den_pos}, den<0 {n_den_neg}, den=0 {n_den_zero}; N>0 at {n_N_pos}/{npts * 4}; '
    f'(b0,b1,b3,G)>0 at {n_pd}/{npts * 4}; den theta-root inside [0,1] for {root_in_unit}/{npts} rate points')
out('info sample positivity above is NOT universality evidence; universality is the imported certificate')

ext = [Fr(1, 10 ** 6), Fr(1, 1000), Fr(1, 7), Fr(1), Fr(9), Fr(1000), Fr(10 ** 6)]
bad = []
cnt = 0
for combo in itertools.product(ext, repeat=5):
    if len({*combo}) > 1 and rng2.random() > 0.02:
        continue
    for th in (Fr(0), Fr(1, 2), Fr(1)):
        vals = list(combo) + [th, 0, 0]
        Nv = P_eval(N, vals); dv = P_eval(den, vals)
        cnt += 1
        if Nv <= 0:
            bad.append((combo, th, Nv, dv))
        if dv <= 0:
            out('info den<=0 at extreme point', combo, th, dv)
check(not bad, f'C.5 extreme-magnitude sweep ({cnt} points incl. all 7 equal-rate diagonals x 3 thetas): N>0 at every sampled point (samples only)')
bb = [Fr(1), Fr(1), Fr(-2), Fr(1)]
cub = lambda th: bb[0] * (1 - th) ** 3 + 3 * bb[1] * th * (1 - th) ** 2 + 3 * bb[2] * th ** 2 * (1 - th) + bb[3] * th ** 3
check(4 * bb[1] * bb[3] - 3 * bb[2] ** 2 < 0 and cub(Fr(1, 2)) < 0 and cub(0) > 0 and cub(1) > 0,
      f'C.6 cubic negative control: b=(1,1,-2,1) has b0,b1,b3>0, 4b1b3-3b2^2={4 * bb[1] * bb[3] - 3 * bb[2] ** 2}<0 and N(1/2)={cub(Fr(1, 2))}<0 (criterion not vacuous)')
bb2 = [Fr(1), Fr(1), Fr(-1), Fr(1)]
cub2 = lambda th: bb2[0] * (1 - th) ** 3 + 3 * bb2[1] * th * (1 - th) ** 2 + 3 * bb2[2] * th ** 2 * (1 - th) + bb2[3] * th ** 3
check(4 * bb2[1] * bb2[3] - 3 * bb2[2] ** 2 > 0 and all(cub2(Fr(k, 256)) > 0 for k in range(257)),
      'C.6 cubic positive control: b=(1,1,-1,1) with b2<0 but 4b1b3-3b2^2=1>0 is positive on a 257-point grid (b2 sign not needed)')
bv = [P_eval(bk, [Fr(3, 2), Fr(1, 3), Fr(5), Fr(2, 7), Fr(11)] + [0, 0, 0]) for bk in b]
check(all(3 * bv[1] * (1 - th) ** 2 + 3 * bv[2] * th * (1 - th) + bv[3] * th ** 2 > 0 for th in (Fr(k, 64) for k in range(-32, 97))),
      'C.7 bracket 3b1(1-th)^2+3b2 th(1-th)+b3 th^2 > 0 on a grid over [-1/2, 3/2] for a sampled rate point (PD => all real theta)')

# ============================================================================
out('\n===== PART D: full structural parse of the author certificate (data only) =====')
raw = open(CERT_PATH, 'rb').read()
check(hashlib.sha256(raw).hexdigest() == CERT_SHA and len(raw) == 51575 and raw.count(b'\n') == 2377,
      'D.0 certificate bytes: sha256/bytes/LF match manifest')
C = json.loads(raw)
check(C['z'] == '8/9' and C['theta_domain'] == '[0,1]' and C['rate_compactification'] == 'ui=xi/(1-xi)'
      and C['split_axis'] == 'path depth modulo5', 'D.1 certificate metadata z, theta_domain, compactification, split axis')
check(C['identity'] == 'N=b0(1-theta)^3+theta[3b1(1-theta)^2+3b2 theta(1-theta)+b3 theta^2]', 'D.1 certificate identity string matches (BERN)')
check(sorted(C.keys()) == ['identity', 'rate_compactification', 'records', 'scope', 'split_axis', 'theta_domain', 'z'],
      f'D.1 certificate top-level keys {sorted(C.keys())}')
out('info scope string:', C['scope'])
names = [r_['name'] for r_ in C['records']]
check(names == ['b0', 'b1', 'b3', 'quadratic_discriminant'], f'D.2 record names {names}')


def box_of(path):
    bnd = [[Fr(0), Fr(1)] for _ in range(5)]
    for dpt, bit in enumerate(path):
        ax = dpt % 5; lo, hi = bnd[ax]; mid = (lo + hi) / 2
        bnd[ax] = [lo, mid] if bit == '0' else [mid, hi]
    return bnd


total = 0
for rec in C['records']:
    nm = rec['name']; leaves = rec['positive_leaf_paths']
    mine = P5[nm]
    check(rec['coefficient_sha256'] == digest5(mine), f'D.3 {nm}: certificate coefficient digest == reviewer-derived polynomial digest')
    check(rec['coefficient_terms'] == len(mine), f'D.3 {nm}: coefficient_terms {rec["coefficient_terms"]} == reviewer {len(mine)}')
    check(rec['individual_degrees'] == [max(k[j] for k in mine) for j in range(5)], f'D.3 {nm}: individual_degrees {rec["individual_degrees"]} == reviewer')
    check(sorted(rec.keys()) == ['coefficient_sha256', 'coefficient_terms', 'individual_degrees', 'name', 'positive_leaf_paths'], f'D.3 {nm}: record keys')
    L = len(leaves); total += L
    check(all(isinstance(x, str) and x and set(x) <= {'0', '1'} for x in leaves), f'D.4 {nm}: all {L} leaf paths are nonempty binary strings')
    check(len(set(leaves)) == L, f'D.4 {nm}: leaf paths distinct')
    S = set(leaves)
    prefix_free = not any(x[:j] in S for x in leaves for j in range(1, len(x)))
    check(prefix_free, f'D.4 {nm}: prefix-free')
    kraft = sum(Fr(1, 2 ** len(x)) for x in leaves)
    check(kraft == 1, f'D.4 {nm}: Kraft sum = {kraft} (==1 with prefix-free => complete binary tree => leaf boxes cover [0,1]^5)')
    internal = {x[:j] for x in leaves for j in range(len(x))}
    check(all((q_ + '0' in S or q_ + '0' in internal) and (q_ + '1' in S or q_ + '1' in internal) for q_ in internal),
          f'D.4 {nm}: every internal node has both children ({len(internal)} internal nodes)')
    depths = Counter(len(x) for x in leaves)
    check(min(depths) >= 5, f'D.4 {nm}: min depth {min(depths)} >= 5 (each axis split at least once); max depth {max(depths)}')
    inside_ok = True; len_ok = True
    for x in leaves:
        bnd = box_of(x)
        len_ok &= all(hi - lo <= Fr(1, 2) for lo, hi in bnd)
        inside_ok &= any(all(0 < bnd[j][cb[j]] < 1 for j in range(5)) for cb in itertools.product((0, 1), repeat=5))
    check(inside_ok and len_ok, f'D.4 {nm}: every leaf box has an open-cube corner and all side lengths <= 1/2')
    out(f'info {nm}: leaves {L}, depth histogram {dict(sorted(depths.items()))}')
check([len(r_['positive_leaf_paths']) for r_ in C['records']] == [657, 567, 522, 565] and total == 2311,
      f'D.5 leaf counts {[len(r_["positive_leaf_paths"]) for r_ in C["records"]]} total {total} == manuscript (657,567,522,565; 2311)')
out('info Part D parses the certificate structure only; universal leaf positivity is imported from the separate certificate audit')

# ============================================================================
out('\n===== PART E: bounded own-implementation spot check of 12 leaves (sample only) =====')


def bern_root(p5):
    """Exact Bernstein coefficients on [0,1]^5 of  Ptilde(x) = prod(1-x_i)^{d_i} P(x/(1-x)):
    b_beta = a_beta / prod C(d_i, beta_i)  (the compactification maps monomials to Bernstein basis)."""
    ds = [max(k[j] for k in p5) for j in range(5)]
    shape = tuple(d + 1 for d in ds)
    arr = {}
    for k, v in p5.items():
        arr[k] = Fr(v, math.prod(math.comb(ds[j], k[j]) for j in range(5)))
    return arr, ds


def split_exact(arr, ds, axis, bit):
    """de Casteljau midpoint subdivision along one axis; keeps the chosen half (exact Fractions)."""
    d = ds[axis]
    other = [j for j in range(5) if j != axis]
    out_ = {}
    for coord in itertools.product(*[range(ds[j] + 1) for j in other]):
        line = []
        for k in range(d + 1):
            key = [0] * 5
            for jj, j in enumerate(other):
                key[j] = coord[jj]
            key[axis] = k
            line.append(arr.get(tuple(key), Fr(0)))
        levels = [line]
        while len(levels[-1]) > 1:
            levels.append([(x + y) / 2 for x, y in zip(levels[-1], levels[-1][1:])])
        for k in range(d + 1):
            val = levels[k][0] if bit == '0' else levels[d - k][-1]
            key = [0] * 5
            for jj, j in enumerate(other):
                key[j] = coord[jj]
            key[axis] = k
            out_[tuple(key)] = val
    return out_


def leaf_check(p5, path, verbose_name):
    arr, ds = bern_root(p5)
    for dpt, bit in enumerate(path):
        arr = split_exact(arr, ds, dpt % 5, bit)
    bnd = box_of(path)
    nonneg = all(v >= 0 for v in arr.values())
    corners_ok = True; inside = 0
    for cb in itertools.product((0, 1), repeat=5):
        if all(0 < bnd[j][cb[j]] < 1 for j in range(5)):
            inside += 1
            key = tuple(0 if cb[j] == 0 else ds[j] for j in range(5))
            corners_ok &= arr.get(key, Fr(0)) > 0
    # corner coefficient must equal the compactified polynomial value at the corner (sanity)
    cb = next(cb for cb in itertools.product((0, 1), repeat=5) if all(0 < bnd[j][cb[j]] < 1 for j in range(5)))
    xs = [bnd[j][cb[j]] for j in range(5)]
    us = [x / (1 - x) for x in xs]
    val = math.prod((1 - xs[j]) ** ds[j] for j in range(5)) * sum(Fr(v) * math.prod(us[j] ** k[j] for j in range(5)) for k, v in p5.items())
    key = tuple(0 if cb[j] == 0 else ds[j] for j in range(5))
    corner_eq = (arr.get(key, Fr(0)) == val)
    return nonneg, corners_ok, inside, corner_eq, min(arr.values())


spot_fail = 0
for rec in C['records']:
    nm = rec['name']; leaves = rec['positive_leaf_paths']
    sel = [leaves[0], leaves[len(leaves) // 2], leaves[-1]]
    for path in sel:
        nonneg, corners_ok, inside, corner_eq, mn = leaf_check(P5[nm], path, nm)
        okk = nonneg and corners_ok and inside > 0 and corner_eq
        spot_fail += not okk
        out(f'{"PASS" if okk else "FAIL"} E.1 {nm} leaf {path}: all Bernstein coeffs >= 0 ({nonneg}), open-cube corners > 0 ({corners_ok}, {inside} corners), corner==value ({corner_eq}), min coeff {mn}')
check(spot_fail == 0, 'E.1 all 12 sampled leaves pass with the reviewer own exact de Casteljau (sample only)')
# root arrays contain negative entries (so subdivision is genuinely needed) -- informational
for nm in ('b0', 'b1', 'b3', 'quadratic_discriminant'):
    arr, ds = bern_root(P5[nm])
    neg = sum(1 for v in arr.values() if v < 0)
    out(f'info {nm}: root Bernstein array has {neg} negative of {len(arr)} nonzero entries')
# negative control: flip the sign of the b0 constant term and re-run the first b0 leaf
p5bad = dict(P5['b0'])
kconst = (0, 0, 0, 0, 0)
p5bad[kconst] = -p5bad.get(kconst, 0) - 1
nonneg, corners_ok, inside, corner_eq, mn = leaf_check(p5bad, C['records'][0]['positive_leaf_paths'][0], 'b0-bad')
check(not (nonneg and corners_ok), f'E.2 negative control: perturbed b0 (constant term {P5["b0"].get(kconst)} -> {p5bad[kconst]}) fails the first b0 leaf (nonneg={nonneg}, corners_ok={corners_ok})')

out('\n===== SUMMARY =====')
out('fail_count', len(FAILS))
for f_ in FAILS:
    out('FAILED:', f_)
out('elapsed_seconds', round(time.monotonic() - T0, 2), 'end_utc', utc())
out('VERDICT_LINE', 'ALL CONTROLS PASS' if not FAILS else 'SOME CONTROLS FAILED')
