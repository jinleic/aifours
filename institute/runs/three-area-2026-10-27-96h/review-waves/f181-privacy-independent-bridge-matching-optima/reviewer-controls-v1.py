#!/usr/bin/env python3
"""ReviewF181PrivacyBridge -- independent controls for wave f181-privacy-independent-bridge-matching-optima.

Reviewer-authored. Imports and executes NO author code; the candidate's displayed certificate blocks are
not run. Exact items use fractions.Fraction only (own multivariate polynomial class, own Sturm sequences,
own polygon + circular-segment geometry in Q(sqrt A)+Q(sqrt A)*theta, own Euler/Taylor arctangent
enclosures). Items in the DIAGNOSTIC list use floats (numpy) and are labelled; they are never acceptance.
Reads only the wave manifest and the three manifest-listed inputs (for hashing).
Writes exactly one file: reviewer-controls-v1-result.json (exclusive create).
"""
import datetime
import hashlib
import json
import math
import os
import random
import signal
import sys
import time
from fractions import Fraction as Fr
from math import comb, factorial, isqrt

signal.alarm(110)
T_START = time.time()
CLOCK_START = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
    'local': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
}
HERE = os.path.dirname(os.path.abspath(__file__))
RESULT = os.path.join(HERE, 'reviewer-controls-v1-result.json')
MANIFEST = os.path.join(HERE, 'manifest-v1.json')
MANIFEST_SHA = 'c37601cd5423af6cc20a53ee02dd7228d6b39cd94006d930f88f5696f68ecd49'

POS, NEG, DIAG, VALUES = [], [], [], {}


def pos(cid, ok, detail=None):
    POS.append({'id': cid, 'pass': bool(ok), 'detail': detail})
    return bool(ok)


def neg(cid, fn, expect):
    try:
        accepted, reason = fn()
    except Exception as e:  # a crash is recorded, and it is NOT the intended reason
        accepted, reason = False, 'exception ' + type(e).__name__ + ': ' + str(e)
    ok = (not accepted) and (expect in reason)
    NEG.append({'id': cid, 'mutant_accepted': bool(accepted), 'observed_reason': reason,
                'expected_reason': expect, 'pass': ok})
    return ok


def dg(cid, ok, detail=None):
    DIAG.append({'id': cid, 'pass': bool(ok), 'detail': detail})
    return bool(ok)


def dec(q, d=45):
    sgn = '-' if q < 0 else ''
    q = abs(q)
    n = q.numerator * 10**d // q.denominator
    ip, fp = divmod(n, 10**d)
    return f"{sgn}{ip}.{fp:0{d}d}"


def encdec(lo, hi, d=45):
    """Outward decimal rounding of positive rational enclosures."""
    assert lo > 0 and hi >= lo
    return [dec(lo, d), dec(hi + Fr(1, 10**d), d)]


# ---------------------------------------------------------------- S0 inputs
def facts(p):
    b = open(p, 'rb').read()
    return {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b), 'LF': b.count(b'\n'),
            'CR': b.count(b'\r'), 'final_LF': b.endswith(b'\n')}


SELF = facts(os.path.abspath(__file__))
mf = facts(MANIFEST)
pos('S0.manifest_sha256', mf['sha256'] == MANIFEST_SHA, mf)
man = json.loads(open(MANIFEST, 'rb').read().decode('utf-8'))


def walk(o, path='$'):
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            out += walk(v, path + '.' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            out += walk(v, f'{path}[{i}]')
    else:
        out.append(path)
    return out


leaves = walk(man)
pos('S0.manifest_full_parse',
    man.get('id') == 'f181-privacy-independent-bridge-matching-optima' and man.get('schema_version') == 1
    and len(man['inputs_in_read_order']) == 3 and len(man['outputs']) == 1,
    {'leaf_count': len(leaves), 'top_keys': sorted(man.keys())})
for i, inp in enumerate(man['inputs_in_read_order']):
    f = facts(inp['path'])
    pos(f'S0.input{i}_sha_bytes_LF', f['sha256'] == inp['sha256'] and f['bytes'] == inp['bytes']
        and f['LF'] == inp['LF'] and f['CR'] == 0 and f['final_LF'], {'path': inp['path'], **f})


# ---------------------------------------------------------------- S1 polynomial class
class Poly:
    __slots__ = ('t',)

    def __init__(self, t=None):
        self.t = {}
        if t:
            for k, v in t.items():
                v = Fr(v)
                if v != 0:
                    self.t[k] = v

    @staticmethod
    def c(x):
        return x if isinstance(x, Poly) else Poly({(): Fr(x)})

    @staticmethod
    def var(n):
        return Poly({((n, 1),): 1})

    def __add__(self, o):
        o = Poly.c(o)
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, 0) + v
        return Poly(r)
    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()})

    def __sub__(self, o):
        return self + (-Poly.c(o))

    def __rsub__(self, o):
        return Poly.c(o) + (-self)

    def __mul__(self, o):
        o = Poly.c(o)
        r = {}
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                d = dict(k1)
                for n, e in k2:
                    d[n] = d.get(n, 0) + e
                k = tuple(sorted(d.items()))
                r[k] = r.get(k, 0) + v1 * v2
        return Poly(r)
    __rmul__ = __mul__

    def __pow__(self, n):
        r = Poly.c(1)
        for _ in range(n):
            r = r * self
        return r

    def __truediv__(self, q):
        q = Fr(q)
        return Poly({k: v / q for k, v in self.t.items()})

    def iszero(self):
        return len(self.t) == 0

    def same(self, o):
        return (self - o).iszero()

    def diff(self, n):
        r = {}
        for k, v in self.t.items():
            d = dict(k)
            e = d.get(n, 0)
            if e == 0:
                continue
            if e == 1:
                del d[n]
            else:
                d[n] = e - 1
            kk = tuple(sorted(d.items()))
            r[kk] = r.get(kk, 0) + v * e
        return Poly(r)

    def anti(self, n):
        r = {}
        for k, v in self.t.items():
            d = dict(k)
            e = d.get(n, 0)
            d[n] = e + 1
            kk = tuple(sorted(d.items()))
            r[kk] = r.get(kk, 0) + v / (e + 1)
        return Poly(r)

    def subs(self, n, val):
        val = Poly.c(val)
        r = Poly()
        cache = {}
        for k, v in self.t.items():
            d = dict(k)
            e = d.pop(n, 0)
            if e not in cache:
                cache[e] = val ** e
            r = r + Poly({tuple(sorted(d.items())): v}) * cache[e]
        return r

    def integ(self, n, lo, hi):
        F = self.anti(n)
        return F.subs(n, hi) - F.subs(n, lo)

    def ev(self, env):
        s = Fr(0)
        for k, v in self.t.items():
            p = v
            for n, e in k:
                p *= Fr(env[n]) ** e
            s += p
        return s

    def const_value(self):
        assert all(k == () for k in self.t), 'not constant'
        return self.t.get((), Fr(0))

    def ucoeffs(self, n, env=None):
        env = env or {}
        deg = max((dict(k).get(n, 0) for k in self.t), default=0)
        out = [Fr(0)] * (deg + 1)
        for k, v in self.t.items():
            d = dict(k)
            e = d.pop(n, 0)
            p = v
            for nn, ee in d.items():
                p *= Fr(env[nn]) ** ee
            out[e] += p
        return out


m = Poly.var('m')
g = Poly.var('g')
x = Poly.var('x')
yv = Poly.var('y')

# ---------------------------------------------------------------- S2 geometric moments (independent derivation)


def stirling2(n, k):
    return sum((-1)**i * comb(k, i) * (k - i)**n for i in range(k + 1)) // factorial(k)


# factorial moments of Pr(N=k)=(1-b)b^k are r! m^r; N^j = sum_r S(j,r) N^(r)
T = {0: Poly.c(1)}
for j in range(1, 5):
    T[j] = Poly()
    for r_ in range(1, j + 1):
        T[j] = T[j] + Poly.c(stirling2(j, r_) * factorial(r_)) * m ** r_
pos('S2.T1_eq_m', T[1].same(m))
pos('S2.T2_eq_candidate', T[2].same(m + 2 * m**2))
pos('S2.T3_eq_candidate', T[3].same(m + 6 * m**2 + 6 * m**3))
pos('S2.T4_eq_candidate', T[4].same(m + 14 * m**2 + 36 * m**3 + 24 * m**4))
for bq, K in ((Fr(1, 64), 160), (Fr(1, 32), 160), (Fr(1, 2), 700)):
    mq = bq / (1 - bq)
    okall = True
    for j in range(1, 5):
        Sj = sum((1 - bq) * bq**k * k**j for k in range(K + 1))
        okall &= (0 < T[j].ev({'m': mq}) - Sj < Fr(1, 10**100))
    for j in range(0, 5):
        Bj = sum((1 - bq) * bq**k * comb(k, j) for k in range(K + 1))
        okall &= (0 < mq**j - Bj < Fr(1, 10**100))
    pos(f'S2.exact_partial_sums_and_binomial_moments_b={bq}', okall, {'terms': K + 1})

# ---------------------------------------------------------------- S3 identities of section 2.6 / section 4
M = {}
for j in range(5):
    M[j] = Poly()
    for i in range(j + 1):
        M[j] = M[j] + Poly.c(comb(j, i)) * g**(j - i) * T[i]
Q = g**4 + 4*m*g**3 + 6*m**2*g**2 - 2*m*(1 + 3*m)*g + m**2
P = (g**5 + 5*m*g**4 + (2*m + 12*m**2)*g**3 + (12*m**3 - 2*m)*g**2
     - m*(1 + 2*m)*(1 + 6*m)*g + m**2*(1 + 2*m))
pos('S3.identity2_M3pM2-M3M2p_eq_Q', (M[3].diff('g')*M[2] - M[3]*M[2].diff('g')).same(Q))
pos('S3.identity2_M4pM2-M4M2p_eq_2P', (M[4].diff('g')*M[2] - M[4]*M[2].diff('g')).same(2*P))
v = m*(m + 1)
tau = 1 + 2*m
Qx = Q.subs('g', x - m)
Px = P.subs('g', x - m)
pos('S3.xform_Q', Qx.same(x**4 - 2*v*tau*x + 3*v**2))
pos('S3.xform_P', Px.same(x**5 + 2*v*x**3 - 2*v*tau*x**2 - v*(1 + 3*v)*x + 2*v**2*tau))
pos('S3.tau_sq_eq_1+4v', (tau**2).same(1 + 4*v))
Rx = 2*x**3 - (1 + 6*v)*x + 2*v*tau
pos('S3.P_eq_xQ_plus_vR', Px.same(x*Qx + v*Rx))
pos('S3.xR_plus_Q_eq_3(x2-v)2-x2', (x*Rx + Qx).same(3*(x**2 - v)**2 - x**2))
pos('S3.squared_root_relation', ((x**4 + 3*v**2)**2 - 4*v**2*tau**2*x**2).same(Qx*(x**4 + 3*v**2 + 2*v*tau*x)))
V = Poly.var('v')
Z = Poly.var('z')
XX = Poly.var('X')
pos('S3.z_identity', ((Z**2 + 3)**2 - 16*Z - 12*(Z - 1)**2).same((Z - 1)**3*(Z + 3)))
E1 = (XX**2 + 3*V**2)**2 - 4*V**2*(1 + 4*V)*XX
pos('S3.E1_at_X=vz', E1.subs('X', V*Z).same(V**3*(V*(Z**2 + 3)**2 - 4*(1 + 4*V)*Z)))
pos('S3.z_chain', (4*Z - 12*V*(Z - 1)**2 - V*(Z - 1)**3*(Z + 3) + (V*(Z**2 + 3)**2 - 4*(1 + 4*V)*Z)).iszero())
s_ = Poly.var('s')
TA = Poly.var('tau')
Qg = x**4 - 2*V*TA*x + 3*V**2
Pg = x**5 + 2*V*x**3 - 2*V*TA*x**2 - V*(1 + 3*V)*x + 2*V**2*TA
pos('S3.Q_at_x=sqrt(v)', Qg.subs('x', s_).subs('v', s_**2).same(2*s_**3*(2*s_ - TA)))
pos('S3.P_at_x=sqrt(v)', Pg.subs('x', s_).subs('v', s_**2).same(-(s_**3)))
pos('S3.endpoint_values', Q.subs('g', 0).same(m**2) and Q.subs('g', 1).same((1 + m)**2)
    and P.subs('g', 0).same(m**2*(1 + 2*m)) and P.subs('g', 1).same((1 + m)**2*(1 + 2*m)))
pos('S3.P0_eq_P1_moments', all(((1 + m)*M[j].subs('g', 0)).same(m*M[j].subs('g', 1)) for j in (1, 2, 3, 4)))


def Mev(j, mq, gq):
    return M[j].ev({'m': mq, 'g': gq})


# ---------------------------------------------------------------- S4 staircase costs by direct layer sums
ok4 = []
for bq, K in ((Fr(1, 64), 160), (Fr(1, 2), 700)):
    mq = bq / (1 - bq)
    for gq in (Fr(3, 10), Fr(1, 2), Fr(7, 5)):
        def lay(fun):
            return sum(bq**k * (fun(gq + k) - (fun(gq + k - 1) if k else 0)) for k in range(K + 1))
        pairs = ((2*Mev(2, mq, gq), lay(lambda R: 2*R**2)),
                 (Fr(4, 3)*Mev(3, mq, gq), lay(lambda R: Fr(4, 3)*R**3)),
                 (Mev(4, mq, gq), lay(lambda R: R**4)),
                 (Fr(2, 3)*Mev(4, mq, gq), lay(lambda R: Fr(2, 3)*R**4)))
        ok4.append(all(0 < c_ - s2 < Fr(1, 10**90) for c_, s2 in pairs))
pos('S4.staircase_Z_L_W_J_closed_forms_vs_layer_sums', all(ok4), {'cases': len(ok4)})

# ---------------------------------------------------------------- S5 diamond integrals, radial factor 2/3
Rv = Poly.var('R')


def oct_int(integrand):
    return 8*integrand.integ('x', yv, Rv - yv).integ('y', 0, Rv/2)


pos('S5.diamond_area_2R2', oct_int(Poly.c(1)).same(2*Rv**2))
pos('S5.diamond_int_l1_eq_4R3/3', oct_int(x + yv).same(Fr(4, 3)*Rv**3))
pos('S5.diamond_int_l1sq_eq_R4', oct_int((x + yv)**2).same(Rv**4))
pos('S5.diamond_int_l2sq_eq_2R4/3', oct_int(x**2 + yv**2).same(Fr(2, 3)*Rv**4))
u = Poly.var('u')
rr = Poly.var('r')
pos('S5.uniform_u_factor_2/3', (u**2 + (1 - u)**2).integ('u', 0, 1).same(Poly.c(Fr(2, 3))))
pos('S5.jacobian_(ru,r(1-u))_abs_r', (u*(-rr) - rr*(1 - u)).same(-rr))

# ---------------------------------------------------------------- S6 gap-lemma derivative
rho = Poly.var('rho')
Phi1 = (4*rho**2).integ('rho', 0, Rv)
Phi2 = (4*rho**3).integ('rho', 0, Rv)
pos('S6.Phi1_Phi2', Phi1.same(Fr(4, 3)*Rv**3) and Phi2.same(Rv**4))
pos('S6.Hprime_eq_4R(phi-v)', (Phi1 - 2*V*Rv**2).diff('R').same(4*Rv*(Rv - V))
    and (Phi2 - 2*V*Rv**2).diff('R').same(4*Rv*(Rv**2 - V)))


# ---------------------------------------------------------------- S7 Sturm / Descartes across m
def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def uev(p, xq):
    s = Fr(0)
    for c_ in reversed(p):
        s = s*xq + c_
    return s


def uder(p):
    return trim([i*p[i] for i in range(1, len(p))])


def urem(a, b_):
    a = trim(a)
    b_ = trim(b_)
    while a and len(a) >= len(b_):
        q_ = a[-1]/b_[-1]
        sh = len(a) - len(b_)
        for i, bc in enumerate(b_):
            a[i + sh] -= q_*bc
        a = trim(a)
    return a


def sturm(p):
    seq = [trim(p), uder(p)]
    while True:
        r = urem(seq[-2], seq[-1])
        if not r:
            break
        seq.append([-c_ for c_ in r])
    return seq


def nsc(vals):
    vals = [w for w in vals if w != 0]
    return sum(1 for i in range(len(vals) - 1) if (vals[i] > 0) != (vals[i + 1] > 0))


def V_at(seq, xq):
    if xq == 'inf':
        return nsc([s[-1] for s in seq])
    return nsc([uev(s, xq) for s in seq])


def nroots(seq, a, b_):
    return V_at(seq, a) - V_at(seq, b_)


def bisect(p, lo, hi, width):
    flo = uev(p, lo)
    fhi = uev(p, hi)
    assert flo*fhi < 0
    while hi - lo > width:
        mid = (lo + hi)/2
        fm = uev(p, mid)
        if fm == 0:
            return mid, mid
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi, fhi = mid, fm
    return lo, hi


def sqrt_bracket(q, digits=40):
    n = q.numerator * 10**(2*digits) // q.denominator
    s0 = isqrt(n)
    lo = Fr(s0, 10**digits)
    hi = Fr(s0 + 1, 10**digits)
    assert lo*lo <= q < hi*hi
    return lo, hi


MLIST = [Fr(1, 1000), Fr(1, 255), Fr(1, 63), Fr(1, 31), Fr(1, 7), Fr(1, 3), Fr(2, 5), Fr(51, 125),
         Fr(4083, 10000), Fr(41, 100), Fr(1, 2), Fr(1), Fr(2), Fr(5), Fr(10), Fr(100)]
rows7 = []
for mq in MLIST:
    s_lo, s_hi = sqrt_bracket(mq*mq + mq)
    g0lo, g0hi = s_lo - mq, s_hi - mq
    row = {'m': str(mq)}
    good = True
    larger = {}
    for name, poly in (('Q', Q), ('P', P)):
        pc = poly.ucoeffs('g', {'m': mq})
        sq = sturm(pc)
        good &= (nsc(pc) == 2 and nroots(sq, 0, 'inf') == 2 and nroots(sq, 0, 1) == 2
                 and nroots(sq, 0, g0lo) == 1 and nroots(sq, g0lo, g0hi) == 0 and nroots(sq, g0hi, 1) == 1
                 and len(sq[-1]) == 1 and uev(pc, g0lo) < 0 and uev(pc, g0hi) < 0 and uev(pc, Fr(1)) > 0)
        larger[name] = bisect(pc, g0hi, Fr(1), Fr(1, 10**30))
        row[name + '_larger_root'] = dec(larger[name][0], 20)
    pc = P.ucoeffs('g', {'m': mq})
    sp = sturm(pc)
    lo, hi = larger['Q']
    gLgJ = uev(pc, lo) < 0 and uev(pc, hi) < 0 and nroots(sp, lo, hi) == 0
    row['gL<gJ_via_P<0_on_Q_root_bracket'] = gLgJ
    row['ok'] = bool(good and gLgJ)
    rows7.append(row)
pos('S7.two_simple_positive_roots_split_by_g0_and_gL<gJ_for_16_m', all(r['ok'] for r in rows7), rows7)

# ---------------------------------------------------------------- S8 PASS A recomputation (own code)
CASES = [
    ('ln64', Fr(1, 64), Fr(2975366184837612, 10**16), Fr(2975366184837613, 10**16),
     Fr(3761763123, 10**10), Fr(3761763124, 10**10), Fr(37, 5000)),
    ('ln32', Fr(1, 32), Fr(3646185443795757, 10**16), Fr(3646185443795759, 10**16),
     Fr(441266095196338192, 10**18), Fr(441266095196338193, 10**18), Fr(3, 500)),
    ('ln2', Fr(1, 2), Fr(7061732346792597254817, 10**22), Fr(7061732346792597254818, 10**22),
     Fr(7271025149432606453616, 10**22), Fr(7271025149432606453617, 10**22), Fr(1, 10000)),
]
A_TRUE = {}
for name, bq, aL, zL, aJ, zJ, marg in CASES:
    mq = bq/(1 - bq)
    qc = Q.ucoeffs('g', {'m': mq})
    pc = P.ucoeffs('g', {'m': mq})
    sq, sp = sturm(qc), sturm(pc)
    ok_signs = uev(qc, aL) < 0 < uev(qc, zL) and uev(pc, aJ) < 0 < uev(pc, zJ)
    ok_order = 0 < aL < zL < aJ < zJ < 1
    ok_larger = (nroots(sq, 0, 'inf') == 2 and nroots(sq, aL, zL) == 1 and nroots(sq, zL, 'inf') == 0
                 and nroots(sp, 0, 'inf') == 2 and nroots(sp, aJ, zJ) == 1 and nroots(sp, zJ, 'inf') == 0)
    LB = Mev(4, mq, aL)/(3*Mev(2, mq, zL)) - Mev(4, mq, zJ)/(3*Mev(2, mq, aJ))
    gl = bisect(qc, aL, zL, Fr(1, 10**45))
    gj = bisect(pc, aJ, zJ, Fr(1, 10**45))
    JgL = (Mev(4, mq, gl[0])/(3*Mev(2, mq, gl[1])), Mev(4, mq, gl[1])/(3*Mev(2, mq, gl[0])))
    JgJ = (Mev(4, mq, gj[0])/(3*Mev(2, mq, gj[1])), Mev(4, mq, gj[1])/(3*Mev(2, mq, gj[0])))
    VL = (Fr(2, 3)*Mev(3, mq, gl[0])/Mev(2, mq, gl[1]), Fr(2, 3)*Mev(3, mq, gl[1])/Mev(2, mq, gl[0]))
    VW = (Mev(4, mq, gj[0])/(2*Mev(2, mq, gj[1])), Mev(4, mq, gj[1])/(2*Mev(2, mq, gj[0])))
    ok_PL = uev(pc, aL) < 0 and uev(pc, zL) < 0 and nroots(sp, aL, zL) == 0
    A_TRUE[name] = {'mq': mq, 'qc': qc, 'pc': pc, 'sq': sq, 'gl': gl, 'gj': gj, 'JgL': JgL, 'JgJ': JgJ,
                    'VL': VL, 'VW': VW, 'LB': LB, 'brackets': (aL, zL, aJ, zJ), 'marg': marg}
    pos(f'S8.PASS_A_{name}', ok_signs and ok_order and ok_larger and LB > marg and ok_PL,
        {'signs': ok_signs, 'order': ok_order, 'brackets_hold_LARGER_roots_sturm': ok_larger,
         'g_L<g_J_P<0_on_bracket': ok_PL, 'certified_lower_bound': dec(LB, 30), 'claimed_margin': str(marg),
         'certified_lower_bound_exact': str(LB), 'surplus_over_claimed_margin_exact': str(LB - marg)})
    VALUES[f'PASS_A_{name}'] = {
        'm': str(mq), 'g_L': dec(gl[0], 40), 'g_J': dec(gj[0], 40),
        'true_margin_J(P_gL)-J(P_gJ)_in': encdec(JgL[0] - JgJ[1], JgL[1] - JgJ[0], 30),
        'V_L_in': encdec(VL[0], VL[1], 30), 'V_W_in': encdec(VW[0], VW[1], 30),
        'J(P_gJ)_in': encdec(JgJ[0], JgJ[1], 30), 'J(P_gL)_in': encdec(JgL[0], JgL[1], 30)}

# ---------------------------------------------------------------- S9 d67 displayed constants (context for Cor 4)
b64 = Fr(1, 64)
m64 = b64/(1 - b64)
a67 = Fr(3761763123, 10**10)
z67 = Fr(3761763124, 10**10)
eta = Fr(1, 100)


def JPS_of(aq):
    ZS = 2*Mev(2, m64, aq) - 4*eta**2
    NS = (Fr(2, 3)*Mev(4, m64, aq) - 4*Mev(2, m64, aq)*eta**2 + Fr(16, 3)*Mev(1, m64, aq)*eta**3
          - Fr(8, 3)*eta**4)
    return NS/ZS, ZS


JPS, ZS67 = JPS_of(a67)
JPS_DISP = Fr(4355768046089487574226880288026708390699272667, 26721376640271909097532496900000000000000000000)
LB67 = Mev(4, m64, a67)/(3*Mev(2, m64, z67)) - JPS
LB67_DISP = Fr(55892104628095766169604064637687395172793197064705238995982813,
               28589579218686463271455054512504719394059809867200000000000000000000)
pos('S9.J(P_S)_formula_value_eq_displayed', JPS == JPS_DISP, dec(JPS))
pos('S9.d67_lower_bound_eq_displayed_and_>1e-6', LB67 == LB67_DISP and LB67 > Fr(1, 10**6), dec(LB67, 25))
pos('S9.d67_brackets_equal_PASS_A_ln64_J_brackets', (a67, z67) == CASES[0][4:6])
sv = Poly.var('s')
ETA = Poly.var('eta')
pos('S9.cap_area_and_second_moment', (2*sv).integ('s', 0, ETA).same(ETA**2) and
    (2*sv*(Rv - sv)**2 + Fr(2, 3)*sv**3).integ('s', 0, ETA).same(Rv**2*ETA**2 - Fr(4, 3)*Rv*ETA**3 + Fr(2, 3)*ETA**4))


# ---------------------------------------------------------------- S10 PASS B: independent geometry
class QT:
    """a0 + a1*r + (b0 + b1*r)*theta with r^2 = QT.A; theta^2 forbidden."""
    __slots__ = ('a0', 'a1', 'b0', 'b1')
    A = None

    def __init__(s, a0=0, a1=0, b0=0, b1=0):
        s.a0, s.a1, s.b0, s.b1 = Fr(a0), Fr(a1), Fr(b0), Fr(b1)

    @staticmethod
    def c(o):
        return o if isinstance(o, QT) else QT(o)

    def __add__(s, o):
        o = QT.c(o)
        return QT(s.a0 + o.a0, s.a1 + o.a1, s.b0 + o.b0, s.b1 + o.b1)
    __radd__ = __add__

    def __neg__(s):
        return QT(-s.a0, -s.a1, -s.b0, -s.b1)

    def __sub__(s, o):
        return s + (-QT.c(o))

    def __rsub__(s, o):
        return QT.c(o) + (-s)

    def __mul__(s, o):
        o = QT.c(o)
        A = QT.A

        def m2(u0, u1, w0, w1):
            return (u0*w0 + A*u1*w1, u0*w1 + u1*w0)
        p0, p1 = m2(s.a0, s.a1, o.a0, o.a1)
        q0, q1 = m2(s.a0, s.a1, o.b0, o.b1)
        r0, r1 = m2(s.b0, s.b1, o.a0, o.a1)
        t0_, t1_ = m2(s.b0, s.b1, o.b0, o.b1)
        if t0_ != 0 or t1_ != 0:
            raise ValueError('theta^2 term')
        return QT(p0, p1, q0 + r0, q1 + r1)
    __rmul__ = __mul__

    def isz(s):
        return s.a0 == 0 and s.a1 == 0 and s.b0 == 0 and s.b1 == 0


def poly_AI(vs):
    """area and polar second moment about the origin of a CCW polygon (shoelace-type formulas)"""
    A2 = QT(0)
    I12 = QT(0)
    n = len(vs)
    for i in range(n):
        x0, y0 = vs[i]
        x1, y1 = vs[(i + 1) % n]
        cr = x0*y1 - x1*y0
        A2 = A2 + cr
        I12 = I12 + cr*(x0*x0 + x0*x1 + x1*x1 + y0*y0 + y0*y1 + y1*y1)
    return A2*Fr(1, 2), I12*Fr(1, 12)


def rounded_core(mq, tq, cq, include_segment=True):
    """Octant-1 piece of K_k=K+kD = polygon(O,P0k,P1k,P2k) + circular segment of the circle centred (k-m,0),
    radius r=sqrt(A), angles 0..theta. Boundary from the support-function description of the convex body K."""
    Yq = 2*tq - cq + mq
    Aq = Yq*Yq + cq*cq
    QT.A = Aq
    RR = QT(0, 1)
    TH = QT(0, 0, 1, 0)
    Z0 = QT(0)

    def octant(k):
        k = Fr(k)
        P0 = (RR + (k - mq), Z0)
        P1 = (QT(2*tq - cq + k), QT(cq))
        P2 = (QT(tq + k/2), QT(tq + k/2))
        Ap, Ip = poly_AI([(Z0, Z0), P0, P1, P2])
        if not include_segment:
            return Ap, Ip
        At, It = poly_AI([(Z0, Z0), (RR, Z0), (QT(Yq), QT(cq))])      # triangle (C,P0,P1) relative to C
        M1t0 = At*(RR + Yq)*Fr(1, 3)                                    # x-first moment (area*centroid)
        As = TH*(Aq/2)                                                  # sector area r^2 theta/2
        Is = TH*(Aq*Aq/4)                                               # sector polar moment r^4 theta/4
        M1s0 = QT(Aq*cq/3)                                              # (r^3/3) sin(theta), sin=c/r
        Aseg = As - At
        IsegC = Is - It
        M1seg0 = M1s0 - M1t0
        Cx = k - mq                                                     # centre (k-m, 0)
        Iseg = IsegC + M1seg0*(2*Cx) + Aseg*(Cx*Cx)
        return Ap + Aseg, Ip + Iseg
    vals = [octant(k) for k in range(7)]
    FZ = [a*8 for a, _ in vals]
    FN = [i*8 for _, i in vals]
    sqrtA_free = all(q.a1 == 0 and q.b1 == 0 for q in FZ + FN)

    def newtonE(vs_, deg):
        table = [vs_]
        while len(table[-1]) > 1:
            prev = table[-1]
            table.append([prev[i + 1] - prev[i] for i in range(len(prev) - 1)])
        zero_ok = all(all(w.isz() for w in table[j]) for j in range(deg + 1, len(table)))
        E = QT(0)
        for j in range(deg + 1):
            E = E + table[j][0]*mq**j                                   # E C(N,j) = m^j
        return E, zero_ok
    ZK, zokZ = newtonE(FZ, 2)
    NK, zokN = newtonE(FN, 4)
    return {'Y': Yq, 'A': Aq, 'z': cq/Yq, 'ZK': ZK, 'NK': NK, 'sqrtA_free': sqrtA_free,
            'poly_ok': zokZ and zokN, 'FZ': FZ, 'FN': FN}


def atan_euler(zq, N=40):
    """Euler series, positive terms; tail bounded by geometric ratio w=z^2/(1+z^2)."""
    w = zq*zq/(1 + zq*zq)
    s = Fr(0)
    term = zq/(1 + zq*zq)
    for n in range(N):
        s += term
        term = term*Fr(2*(n + 1), 2*n + 3)*w
    return s, s + term/(1 - w)


def atan_alt(zq, n=40):
    assert n % 2 == 0
    s = sum((-1)**k * zq**(2*k + 1)/(2*k + 1) for k in range(n))
    return s, s + zq**(2*n + 1)/(2*n + 1)


dg('S10.atan_enclosures_contain_float_atan(1/2)',
    float(atan_euler(Fr(1, 2))[0]) <= math.atan(0.5) + 1e-15 and math.atan(0.5) - 1e-15 <= float(atan_euler(Fr(1, 2))[1])
    and float(atan_alt(Fr(1, 2))[0]) <= math.atan(0.5) + 1e-15)

tq = Fr(1882704899884406, 10**16)
cq = Fr(92748081344954, 10**16)
pos('S10.parameters_0<c<t', 0 < cq < tq)


def certify(mq, tq_, cq_, theta_mode='atan'):
    rc_ = rounded_core(mq, tq_, cq_)
    if theta_mode == 'atan':
        e1 = atan_euler(rc_['z'])
        e2 = atan_alt(rc_['z'])
        th = (max(e1[0], e2[0]), min(e1[1], e2[1]))
    else:  # mutation: theta := z
        th = (rc_['z'], rc_['z'])
    ZK_, NK_ = rc_['ZK'], rc_['NK']
    Js = [(NK_.a0 + NK_.b0*t_)/(ZK_.a0 + ZK_.b0*t_) for t_ in th]
    Zs = [ZK_.a0 + ZK_.b0*t_ for t_ in th]
    return rc_, th, min(Js), max(Js), min(Zs), max(Zs)


rc, TH_ENC, Jmin, Jmax, Zmin, Zmax = certify(m64, tq, cq)
JLO_W = Fr(163006627735070347894185905345798, 10**33)
JHI_W = Fr(163006627735070347894185905345799, 10**33)
ZLO_W = Fr(339888889366, 10**12)
ZHI_W = Fr(339888889367, 10**12)
VJUP = Fr(1630066277350704, 10**16)
pos('S10.sqrtA_parts_cancel_exactly', rc['sqrtA_free'])
pos('S10.layer_quantities_polynomial_deg<=2_and_<=4_in_k', rc['poly_ok'])
pos('S10.theta_enclosure_nonempty', TH_ENC[0] < TH_ENC[1], dec(TH_ENC[1] - TH_ENC[0], 5))
pos('S10.Z_K>0_both_ends', Zmin > 0)
pos('S10.J_window_1e-33', JLO_W < Jmin <= Jmax < JHI_W, {'J_lo': dec(Jmin, 50), 'J_hi': dec(Jmax, 50)})
pos('S10.Z_window_1e-12', ZLO_W < Zmin and Zmax < ZHI_W, dec(Zmin, 25))
pos('S10.V_J_upper_half_of_claim_A', Jmax < VJUP)
pos('S10.improves_d67_by_>2.4e-7', JPS - Jmax > Fr(24, 10**8), dec(JPS - Jmax, 25))
K0 = rc['FZ'][0]
pos('S10.|K_k|=|K|+8tk+2k^2_(mixed-area_check)',
    all((rc['FZ'][k] - K0 - (8*tq*k + 2*k*k)).isz() for k in range(7)))
LBK = Mev(4, m64, a67)/(3*Mev(2, m64, z67)) - Jmax
VALUES['PASS_B'] = {'J(P_K)_enclosure': encdec(Jmin, Jmax, 50), 'Z_K': dec(Zmin, 30),
                    'J(P_K)-window_lo': dec(Jmin - JLO_W, 45), 'window_hi-J(P_K)': dec(JHI_W - Jmax, 45),
                    'J(P_S)-J(P_K)': dec(JPS - Jmax, 30), 'J(P_S)': dec(JPS, 45),
                    'certified J(P_gJ)-J(P_K) lower bound (d67-free alternative)': dec(LBK, 30),
                    'theta_enclosure_width': dec(TH_ENC[1] - TH_ENC[0], 5)[:12],
                    'z=c/Y': dec(rc['z'], 30), 'Y': dec(rc['Y'], 30)}
pos('S10.alt_cor4_without_d67_J(P_gJ)-J(P_K)>1e-6', LBK > Fr(1, 10**6), dec(LBK, 25))


def author_formula(mq, tq_, cq_, tail_area_coef=Fr(2), I1_sign=-1):
    """the candidate's WRITTEN section 6.3 formulas, implemented here by the reviewer (not author code)"""
    Yq = 2*tq_ - cq_ + mq
    Aq = Yq*Yq + cq_*cq_
    QT.A = Aq
    lin = Poly.c(2*tq_) - yv

    def defint(pp):
        return pp.integ('y', cq_, tq_).const_value()
    I0 = QT(cq_*Yq/2, 0, Aq/2, 0)
    I1 = QT(cq_*(2*cq_*cq_ + I1_sign*Aq)*Yq/8, 0, Aq*Aq/8, 0)
    intF = I0 - mq*cq_ + defint(lin)
    intF2 = QT(Aq*cq_ - cq_**3/3) - I0*(2*mq) + mq*mq*cq_ + defint(lin**2)
    intF3 = I0*Aq - I1 - 3*mq*(Aq*cq_ - cq_**3/3) + I0*(3*mq*mq) - mq**3*cq_ + defint(lin**3)
    inty2F = I1 - mq*cq_**3/3 + defint(yv**2*lin)
    T2q, T3q, T4q = [T[j].ev({'m': mq}) for j in (2, 3, 4)]
    Zf = (intF - tq_*tq_/2)*8 + 8*tq_*mq + tail_area_coef*T2q
    Nf = (QT(Fr(2, 3)*T4q + Fr(16, 3)*tq_*T3q + 4*tq_*tq_*T2q)
          + (intF*T2q + (intF2 + tq_**3/3)*mq + intF3*Fr(1, 3) + inty2F - tq_**4/3)*8)
    return Zf, Nf


Zf, Nf = author_formula(m64, tq, cq)
pos('S10.written_6.3_Z_K_equals_independent_geometry', (Zf - rc['ZK']).isz())
pos('S10.written_6.3_N_K_equals_independent_geometry', (Nf - rc['NK']).isz())
tv = Poly.var('t')
kv = Poly.var('k')
pos('S10.tail_area_k^2/4', (2*tv + kv - 2*yv).integ('y', tv, tv + kv/2).same(kv**2/4))
slice2 = (x**2 + yv**2).integ('x', yv, 2*tv + kv - yv)
pos('S10.tail_second_moment_k^4/12+tk^3/3+t^2k^2/2',
    slice2.integ('y', tv, tv + kv/2).same(kv**4/12 + tv*kv**3/3 + tv**2*kv**2/2))
Av = Poly.var('A')
pos('S10.arc_antiderivative_I0_by_differentiation', ((Av - yv**2) - yv**2 + Av).same(2*(Av - yv**2)))
pos('S10.arc_antiderivative_I1_by_differentiation',
    ((6*yv**2 - Av)*(Av - yv**2) - yv**2*(2*yv**2 - Av) + Av**2).same(8*yv**2*(Av - yv**2)))
Yq, Aq = rc['Y'], rc['A']
pos('S10.sqrt(A-c^2)=Y>0', Aq - cq*cq == Yq*Yq and Yq > 0)


def hbind(yq):
    return (2*tq - yq + m64)**2 + yq**2 - Aq


cprime = 2*tq + m64 - cq
pos('S10.arc_binding_on_[0,c]_line_on_[c,t]', hbind(cq) == 0 and hbind(cprime) == 0 and cprime >= tq
    and hbind(Fr(0)) > 0 and hbind(tq) < 0 and cq/Yq < 1)
# BM radius increments for level sets of P_K (theta interval) and P_S (exact squares)


def bm_ok(R2k, R2k1):
    lhs = R2k1 - R2k - 1
    return lhs >= 0 and lhs*lhs >= 4*R2k


okS = all(bm_ok((a67 + k)**2 - 2*eta**2, (a67 + k + 1)**2 - 2*eta**2) for k in range(40))
okK = all(bm_ok((K0.a0 + K0.b0*th + 8*tq*k + 2*k*k)/2, (K0.a0 + K0.b0*th + 8*tq*(k + 1) + 2*(k + 1)**2)/2)
          for k in range(40) for th in TH_ENC)
pos('S10.BM_R(bs)>=R(s)+1_level_sets_P_S_and_P_K', okS and okK)

# ---------------------------------------------------------------- S11 exact sanity: radial phases (Thm 1 consequences)
rnd = random.Random(181)
aL, zL, aJ, zJ = CASES[0][2:6]
VL_LOW = Fr(2, 3)*Mev(3, m64, aL)/Mev(2, m64, zL)
VW_LOW = Mev(4, m64, aJ)/(2*Mev(2, m64, zJ))


def phase_cost(Rs, Rtail, bq, phi):
    mq = bq/(1 - bq)
    I = len(Rs)
    Zs = sum(bq**i * 2*R**2 for i, R in enumerate(Rs)) + bq**I * 2*Mev(2, mq, Rtail)/(1 - bq)
    if phi == 1:
        Ns = sum(bq**i * Fr(4, 3)*R**3 for i, R in enumerate(Rs)) + bq**I * Fr(4, 3)*Mev(3, mq, Rtail)/(1 - bq)
    else:
        Ns = sum(bq**i * R**4 for i, R in enumerate(Rs)) + bq**I * Mev(4, mq, Rtail)/(1 - bq)
    return Ns/Zs


def admissible(seq):
    if seq[0] <= 0:
        return False, 'R0<=0'
    for i in range(len(seq) - 1):
        if seq[i + 1] - seq[i] < 1:
            return False, 'gap<1'
    return True, 'ok'


pos('S11.unit_spaced_phase_equals_staircase_formula',
    phase_cost([Fr(3, 10), Fr(13, 10)], Fr(23, 10), b64, 1) == Fr(2, 3)*Mev(3, m64, Fr(3, 10))/Mev(2, m64, Fr(3, 10)))
viol = 0
mingap = {1: None, 2: None}
for trial in range(600):
    I = rnd.randint(1, 5)
    Rs = [Fr(rnd.randint(1, 3000), 1000)]
    for _ in range(I - 1):
        Rs.append(Rs[-1] + 1 + Fr(rnd.randint(0, 1500), 1000))
    Rtail = Rs[-1] + 1 + Fr(rnd.randint(0, 1500), 1000)
    assert admissible(Rs + [Rtail])[0]
    for phi, low in ((1, VL_LOW), (2, VW_LOW)):
        gap_ = phase_cost(Rs, Rtail, b64, phi) - low
        viol += gap_ < 0
        mingap[phi] = gap_ if mingap[phi] is None or gap_ < mingap[phi] else mingap[phi]
pos('S11.random_admissible_radial_phases_never_beat_V_lower_bounds', viol == 0,
    {'phases': 600, 'costs': 1200, 'min_gap_L': dec(mingap[1], 8), 'min_gap_W': dec(mingap[2], 8)})
pos('S11.unit_spaced_t_scan_never_beats_V', all(
    Fr(2, 3)*Mev(3, m64, Fr(i, 100))/Mev(2, m64, Fr(i, 100)) >= VL_LOW and
    Mev(4, m64, Fr(i, 100))/(2*Mev(2, m64, Fr(i, 100))) >= VW_LOW for i in range(1, 400)))

# ---------------------------------------------------------------- S12 negative controls (intended reasons)
TA64 = A_TRUE['ln64']


def na1():
    mut = Fr(math.ceil((TA64['JgL'][1] - TA64['JgJ'][0]) * 10**9), 10**9)
    LB = TA64['LB']
    return (LB > mut), ('LB<=margin' if LB <= mut else 'LB>margin') + f' (mutated margin {mut})'


def na2():
    qc = TA64['qc']
    sq_ = TA64['sq']
    mq = TA64['mq']
    s_lo, _ = sqrt_bracket(mq*mq + mq)
    lo, hi = bisect(qc, Fr(1, 10**6), s_lo - mq, Fr(1, 10**16))
    pattern_ok = uev(qc, lo) < 0 < uev(qc, hi)
    larger_ok = nroots(sq_, hi, 'inf') == 0
    if pattern_ok and larger_ok:
        return True, 'accepted'
    return False, ('sign pattern + to - (smaller root)' if not pattern_ok else 'not the larger root')


def na3():
    qc = TA64['qc']
    aL_, zL_ = TA64['brackets'][0], TA64['brackets'][1]
    a2, z2 = zL_, zL_ + Fr(1, 10**16)
    if uev(qc, a2) < 0 < uev(qc, z2):
        return True, 'accepted'
    return False, 'Q(a)>=0'


def na4():
    Tm = dict(T)
    Tm[2] = m + m**2
    Mm = {}
    for j in range(5):
        Mm[j] = Poly()
        for i in range(j + 1):
            Mm[j] = Mm[j] + Poly.c(comb(j, i)) * g**(j - i) * Tm[i]
    same = (Mm[3].diff('g')*Mm[2] - Mm[3]*Mm[2].diff('g')).same(Q)
    return same, ('identity holds' if same else 'identity mismatch')


def window_reason(jlo, jhi, lo_w, hi_w):
    if lo_w < jlo and jhi < hi_w:
        return True, 'inside window'
    if jlo <= lo_w:
        return False, 'J below window' if jhi <= lo_w else 'J outside window'
    return False, 'J above window' if jlo >= hi_w else 'J outside window'


def nb1():
    return window_reason(Jmin, Jmax, JLO_W + Fr(1, 10**33), JHI_W + Fr(1, 10**33))


def nb2():
    _, _, jl, jh, _, _ = certify(m64, tq, cq, theta_mode='z')
    acc, rsn = window_reason(jl, jh, JLO_W, JHI_W)
    return acc, rsn


def nb3():
    Zm, _ = author_formula(m64, tq, cq, tail_area_coef=Fr(4))
    QT.A = rc['A']
    eq = (Zm - rc['ZK']).isz()
    return eq, ('formula match' if eq else 'formula mismatch (Z)')


def nb4():
    _, Nm = author_formula(m64, tq, cq, I1_sign=+1)
    QT.A = rc['A']
    eq = (Nm - rc['NK']).isz()
    return eq, ('formula match' if eq else 'formula mismatch (N)')


def nb5():
    _, _, jl, jh, _, _ = certify(b64, tq, cq)
    QT.A = rc['A']
    acc, rsn = window_reason(jl, jh, JLO_W, JHI_W)
    return acc, rsn


def nb6():
    rcn = rounded_core(m64, tq, cq, include_segment=False)
    QT.A = rc['A']
    return rcn['sqrtA_free'], ('sqrt(A) parts cancel' if rcn['sqrtA_free'] else 'sqrt(A) part nonzero')


def nb7():
    thr = Fr(math.ceil((JPS - Jmin) * 10**10), 10**10)
    return (JPS - Jmax > thr), ('improvement<=threshold' if JPS - Jmax <= thr else 'improvement>threshold') + f' ({thr})'


def nc1():
    jm, _ = JPS_of(z67)
    return jm == JPS_DISP, ('JPS equal' if jm == JPS_DISP else 'JPS mismatch')


def nt1():
    Rs_half = [Fr(1, 5) + Fr(i, 2) for i in range(400)]
    Zh = sum(b64**i * 2*R**2 for i, R in enumerate(Rs_half))
    Nh = sum(b64**i * Fr(4, 3)*R**3 for i, R in enumerate(Rs_half))
    beats = Nh/Zh < VL_LOW
    VALUES['half_spacing_phase_L_cost'] = dec(Nh/Zh, 20)
    VALUES['half_spacing_phase_beats_V_L_lower_bound'] = beats
    adm, why = admissible(Rs_half)
    return (adm and beats), why


neg('NA1.PASS_A_margin_mutated_above_truth_ln64', na1, 'LB<=margin')
neg('NA2.bracket_around_SMALLER_Q_root_ln64', na2, 'sign pattern + to - (smaller root)')
neg('NA3.g_L_bracket_shifted_past_root', na3, 'Q(a)>=0')
neg('NA4.moment_mutation_T2=m+m^2_breaks_identity2', na4, 'identity mismatch')
neg('NB1.J_window_shifted_up_1e-33', nb1, 'J below window')
neg('NB2.theta_replaced_by_z', nb2, 'J below window')
neg('NB3.tail_area_k^2/2_in_written_Z', nb3, 'formula mismatch (Z)')
neg('NB4.I1_antiderivative_sign_mutation', nb4, 'formula mismatch (N)')
neg('NB5.m_replaced_by_b', nb5, 'J below window')
neg('NB6.polygon_without_circular_segment', nb6, 'sqrt(A) part nonzero')
neg('NB7.improvement_threshold_above_truth', nb7, 'improvement<=threshold')
neg('NC1.d67_core_radius_mutated_a=z', nc1, 'JPS mismatch')
neg('NT1.half_spacing_radial_phase_beats_V_L_but_is_inadmissible', nt1, 'gap<1')

# ---------------------------------------------------------------- S13 float diagnostics (labelled, not acceptance)
try:
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    mf_, tf, cf = float(m64), float(tq), float(cq)
    Yf = 2*tf - cf + mf_
    Af = Yf*Yf + cf*cf

    def Fprof(yarr, drop_m=False):
        yarr = np.asarray(yarr, dtype=float)
        arc = np.sqrt(Af - yarr*yarr) - (0.0 if drop_m else mf_)
        return np.where(yarr <= cf, arc, 2*tf - yarr)

    def d_formula(Pp, drop_m=False):
        a1 = np.abs(Pp[:, 0])
        a2 = np.abs(Pp[:, 1])
        X = np.maximum(a1, a2)
        Yy = np.minimum(a1, a2)
        return np.where(Yy <= tf, np.maximum(0.0, X - Fprof(np.minimum(Yy, tf), drop_m)), X + Yy - 2*tf)

    def inK(Pp):
        a1 = np.abs(Pp[:, 0])
        a2 = np.abs(Pp[:, 1])
        return (a1 + a2 <= 2*tf + 1e-15) & ((a1 + mf_)**2 + a2**2 <= Af + 1e-15) & (a1**2 + (a2 + mf_)**2 <= Af + 1e-15)
    ya = np.linspace(0, cf, 1500)
    yb = np.linspace(cf, tf, 3000)
    oct1 = np.concatenate([np.stack([Fprof(ya), ya], 1), np.stack([2*tf - yb, yb], 1)])
    parts = []
    for sx in (1, -1):
        for sy in (1, -1):
            parts.append(np.stack([sx*oct1[:, 0], sy*oct1[:, 1]], 1))
            parts.append(np.stack([sx*oct1[:, 1], sy*oct1[:, 0]], 1))
    Bd = np.concatenate(parts)
    rng = np.random.default_rng(20261029)
    TP = np.concatenate([rng.uniform(-1.2, 1.2, size=(400, 2)), rng.uniform(-0.45, 0.45, size=(200, 2))])
    inside = inK(TP)
    brute = np.array([0.0 if inside[i] else np.min(np.abs(Bd[:, 0] - TP[i, 0]) + np.abs(Bd[:, 1] - TP[i, 1]))
                      for i in range(len(TP))])
    err = float(np.max(np.abs(d_formula(TP) - brute)))
    errm = float(np.max(np.abs(d_formula(TP, drop_m=True) - brute)))
    dg('D1.octant_distance_formula_vs_bruteforce_boundary_min', err < 1.2e-4,
       {'max_abs_err': err, 'points': len(TP), 'inside': int(inside.sum())})
    dg('D1n.mutated_distance_formula_(no_m)_rejected', errm > 1e-3, {'max_abs_err': errm})
    Hs = rng.uniform(-1, 1, size=(20000, 2))
    Hs = Hs / np.maximum(1.0, np.abs(Hs).sum(1, keepdims=True))
    Xp = rng.uniform(-3, 3, size=(20000, 2))
    dd = np.abs(d_formula(Xp + Hs) - d_formula(Xp))
    dg('D2.distance_1-Lipschitz_and_shell_index_change<=1', bool(np.all(dd <= np.abs(Hs).sum(1) + 1e-12)) and
       bool(np.all(np.abs(np.ceil(d_formula(Xp + Hs)) - np.ceil(d_formula(Xp))) <= 1)), {'pairs': 20000})
    GX, GW = leggauss(48)

    def gl_int(fun, a, b):
        if b <= a:
            return 0.0
        xs = 0.5*(b - a)*GX + 0.5*(b + a)
        return 0.5*(b - a)*float(np.sum(GW*fun(xs)))

    def law_moments(pieces_of_k, bf, K=90):
        acc = {'Z': 0.0, 'J': 0.0, 'L': 0.0, 'W': 0.0}
        for k in range(K + 1):
            wk = (1 - bf)*bf**k
            for (a_, b_, G) in pieces_of_k(k):
                acc['Z'] += wk*8*gl_int(lambda y: G(y) - y, a_, b_)
                acc['J'] += wk*8*gl_int(lambda y: (G(y)**3 - y**3)/3 + y*y*(G(y) - y), a_, b_)
                acc['L'] += wk*8*gl_int(lambda y: ((G(y) + y)**2 - (2*y)**2)/2, a_, b_)
                acc['W'] += wk*8*gl_int(lambda y: ((G(y) + y)**3 - (2*y)**3)/3, a_, b_)
        return {'Z': acc['Z'], 'J': acc['J']/acc['Z'], 'L': acc['L']/acc['Z'], 'W': acc['W']/acc['Z']}

    def K_pieces(k):
        return [(0.0, cf, lambda y, k=k: np.sqrt(Af - y*y) - mf_ + k), (cf, tf + k/2, lambda y, k=k: 2*tf + k - y)]
    af, ef = float(a67), float(eta)

    def S_pieces(k):
        R = af + k
        return [(0.0, ef, lambda y, R=R: R - ef + 0*y), (ef, R/2, lambda y, R=R: R - y)]
    mK = law_moments(K_pieces, 1/64)
    mS = law_moments(S_pieces, 1/64)
    VLf = float(VL_LOW)
    VWf = float(VW_LOW)
    dg('D3.float_layer_quadrature_P_K_matches_exact', abs(mK['J'] - float(Jmin)) < 1e-13 and abs(mK['Z'] - float(Zmin)) < 1e-13,
       {'Z': mK['Z'], 'J': mK['J']})
    dg('D4.float_P_S_matches_d67_exact_J', abs(mS['J'] - float(JPS)) < 1e-13, {'J': mS['J']})
    eps = math.log(64)
    dg('D5.nonradial_competitors_do_not_beat_Theorem1_optima_(L,W)',
       mK['L'] > VLf and mK['W'] > VWf and mS['L'] > VLf and mS['W'] > VWf and 2/eps > VLf and 6/eps**2 > VWf,
       {'L(P_K)-V_L': mK['L'] - VLf, 'W(P_K)-V_W': mK['W'] - VWf, 'L(P_S)-V_L': mS['L'] - VLf,
        'W(P_S)-V_W': mS['W'] - VWf, 'Laplace L-V_L': 2/eps - VLf, 'Laplace W-V_W': 6/eps**2 - VWf})

    def phase_identity(bq, kappa, n=200000):
        sig = (np.arange(n) + 0.5)/n
        nn = np.maximum(0.0, np.floor(kappa - sig) + 1)
        return float(np.mean(bq**(sig + nn)*abs(math.log(bq)))), (1 - bq)*bq**kappa
    pid = [phase_identity(1/3, kap) for kap in (0.0, 0.37, 1.0, 2.37, 5.5)]
    dg('D6.phase_identity_int_u_a_da=(1-b)p', all(abs(l_ - r_) < 1e-9 for l_, r_ in pid), pid)
except Exception as e:  # diagnostics never gate acceptance
    dg('D.exception', False, type(e).__name__ + ': ' + str(e))

# ---------------------------------------------------------------- write result
CLOCK_END = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
    'local': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
}
ALLPOS = all(c['pass'] for c in POS)
ALLNEG = all(c['pass'] for c in NEG)
ALLDIAG = all(c['pass'] for c in DIAG)
result = {
    'schema': 'reviewer-controls-v1-result', 'reviewer': 'ReviewF181PrivacyBridge',
    'wave': 'f181-privacy-independent-bridge-matching-optima',
    'script': {'path': os.path.abspath(__file__), **SELF},
    'python': sys.version, 'clock_start': CLOCK_START, 'clock_end': CLOCK_END,
    'elapsed_seconds': round(time.time() - T_START, 3),
    'author_code_executed_or_imported': False,
    'counts': {'positive': len(POS), 'positive_failed': sum(not c['pass'] for c in POS),
               'negative': len(NEG), 'negative_failed': sum(not c['pass'] for c in NEG),
               'diagnostic': len(DIAG), 'diagnostic_failed': sum(not c['pass'] for c in DIAG)},
    'verdict': 'PASS' if (ALLPOS and ALLNEG) else 'FAIL',
    'diagnostics_all_pass': ALLDIAG,
    'positive': POS, 'negative': NEG, 'diagnostic': DIAG, 'values': VALUES,
}
with open(RESULT, 'x', encoding='utf-8') as fh:
    json.dump(result, fh, indent=1, sort_keys=False, default=str)
    fh.write('\n')
print(json.dumps({'verdict': result['verdict'], 'counts': result['counts'],
                  'elapsed_seconds': result['elapsed_seconds']}))
sys.exit(0 if result['verdict'] == 'PASS' else 1)
