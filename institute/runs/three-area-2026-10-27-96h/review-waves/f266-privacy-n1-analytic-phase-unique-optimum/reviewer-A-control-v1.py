#!/usr/bin/env python3
"""Reviewer A's independent finite exact checks. No source/author code is run."""
from fractions import Fraction as Q
from math import comb, isqrt
from pathlib import Path
import hashlib
import json
import signal
import subprocess
import sys
import time
import traceback

RECEIPT = Path(__file__).with_name('reviewer-A-control-receipt-v1.json')
if RECEIPT.exists():
    raise FileExistsError(RECEIPT)

def alarm_handler(signum, frame):
    raise TimeoutError('120-second reviewer control ceiling')
signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(120)
start = time.monotonic_ns()
clock = subprocess.check_output(['/bin/date'], text=True).strip()
checks = []

def trim(p):
    p = list(map(Q, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [Q(0)]

def plus(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])

def times(a, b):
    p = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            p[i+j] += x*y
    return trim(p)

def scale(p, k):
    return trim([k*x for x in p])

def power(p, n):
    r = [Q(1)]
    for _ in range(n):
        r = times(r, p)
    return r

def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))])

def value(p, x):
    r = Q(0)
    for a in reversed(p):
        r = r*x+a
    return r

def division(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    out = [Q(0)] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        shift, k = len(a)-len(b), a[-1]/b[-1]
        out[shift] += k
        a = plus(a, [Q(0)]*shift+scale(b, -k))
    return trim(out), trim(a)

def shifted(p, k):
    out = [Q(0)]
    for a in reversed(p):
        out = plus(times(out, [k, Q(1)]), [a])
    return out

def sturm(p):
    s = [trim(p), derivative(p)]
    while s[-1] != [0]:
        r = division(s[-2], s[-1])[1]
        if r == [0]:
            break
        s.append(scale(r, -1))
    return s

def variations(s, x):
    vals = [p[-1] if x is None else value(p, x) for p in s]
    signs = [1 if a > 0 else -1 for a in vals if a]
    return sum(a != b for a, b in zip(signs, signs[1:]))

def roots(p, a, b):
    s = sturm(p)
    assert value(p, a) != 0
    if b is not None:
        assert value(p, b) != 0
    return variations(s, a)-variations(s, b)

def note(name, **data):
    checks.append(dict(name=name, passed=True, **data))

ok = False
error = None
try:
    delta = [Q(-5,16), Q(2), Q(26), Q(48), Q(24)]
    da, db = value(delta, Q(1,14)), value(delta, Q(1,13))
    assert da == Q(-725,38416) and db == Q(8171,456976)
    assert roots(delta, Q(0), None) == roots(delta, Q(1,14), Q(1,13)) == 1
    note('quartic exact signs and Sturm counts', left=str(da), right=str(db))

    cubic = [Q(-1), Q(18), Q(864), Q(2592)]
    ca, cb = value(cubic, Q(1,50)), value(cubic, Q(1,40))
    assert ca == Q(-4276,15625) and cb == Q(61,2000)
    assert roots(cubic, Q(0), None) == roots(cubic, Q(1,50), Q(1,40)) == 1
    assert Q(64,3969) < Q(1,50) < Q(1,40) < Q(15,196)
    assert Q(14,169) < Q(1,12)
    scubic = [Q(-81), Q(-108), Q(-9), Q(2)]
    assert roots(scubic, Q(0), None) == 1
    transformed = [Q(0)]*4
    for k, a in enumerate(cubic):
        transformed[3-k] = 2*a/Q(4**k)
    assert transformed == scale(scubic, -1)
    note('transition cubic exact brackets and reciprocal-root count', left=str(ca), right=str(cb))

    vv = [Q(0), Q(1)]
    av = scale(times([Q(1), Q(-12)], [Q(1), Q(6)]), Q(1,18))
    lhs = plus(power(av,2), scale(times(times(power(vv,2), [Q(1),Q(4)]), [Q(1,6),Q(1)]), -16))
    rhs = scale(times([Q(1),Q(6)], scale(cubic,-1)), Q(1,324))
    assert lhs == rhs
    note('screen squared-comparison polynomial identity')

    instances = []
    for m in (Q(1,14), Q(1,13), Q(1,100), Q(1,1000)):
        # Memoryless recursion, not copied factorial-moment code.
        T = [Q(1)]
        for n in range(1,5):
            T.append(m*sum(comb(n,k)*T[k] for k in range(n)))
        v, tau = m+m*m, 1+2*m
        T2, T3, T4 = T[2:5]
        assert T2 == m+2*m*m
        assert T3 == m+6*m*m+6*m**3
        assert T4 == m+14*m*m+36*m**3+24*m**4
        moment = lambda n: [Q(comb(n,n-j))*T[n-j] for j in range(n+1)]
        M2, M4 = moment(2), moment(4)
        assert value(M2,Q(1,2)) == Q(1,4)+2*m+2*m*m
        assert value(M4,Q(1,2)) == Q(1,16)+5*m+29*m*m+48*m**3+24*m**4
        assert value(M4,Q(1,2))-Q(3,2)*value(M2,Q(1,2)) == value(delta,m)
        P = scale(plus(times(derivative(M4),M2), scale(times(M4,derivative(M2)),-1)), Q(1,2))
        assert P == [m*m*(1+2*m), -m*(1+2*m)*(1+6*m), 12*m**3-2*m, 2*m+12*m*m, 5*m, Q(1)]
        assert value(P,Q(0)) == m*m*(1+2*m)
        assert value(P,Q(1)) == (1+m)**2*(1+2*m)
        Px = shifted(P,-m)
        assert Px == [2*v*v*tau, -v*(1+3*v), -2*v*tau, 2*v, Q(0), Q(1)]
        assert shifted(M2,-m) == [v,Q(0),Q(1)]
        M4x = shifted(M4,-m)
        assert M4x == [v+9*v*v,4*v*tau,6*v,Q(0),Q(1)]
        assert division(Px,[-v,Q(0),Q(1)])[1] == [Q(0),-v]
        GX = [-v-6*v*v, -4*v*tau, Q(0), Q(0), Q(2)]
        id_lhs = plus(times([Q(0),Q(2)],Px),times([v,Q(0),Q(-1)],GX))
        id_rhs = scale(times([v,Q(0),Q(1)],[-v-Q(1,6),Q(0),Q(1)]),6*v)
        assert id_lhs == id_rhs
        assert plus(M4x,scale(power([v,Q(0),Q(1)],2),-3)) == scale(GX,-1)
        lp = Q(1,3)+4*m+4*m*m
        assert value(M4,Q(0)) == 3*lp*value(M2,Q(0))
        assert value(M4,Q(1)) == 3*lp*value(M2,Q(1))
        assert roots(P,Q(0),Q(1)) == roots(P,Q(0),None) == 2
        D = 10**12
        r = Q(isqrt(v.numerator*D*D//v.denominator),D)-m
        assert 0 < r < 1 and value(P,r) < 0
        assert roots(P,Q(0),r) == roots(P,r,Q(1)) == 1
        lo, hi = r, Q(1)
        for _ in range(60):
            mid = (lo+hi)/2
            z = value(P,mid)
            if z == 0:
                lo = hi = mid
                break
            if z < 0:
                lo = mid
            else:
                hi = mid
        sign = 1 if value(cubic,v) > 0 else -1
        qlo, qhi = (lo+m)**2-v-Q(1,6), (hi+m)**2-v-Q(1,6)
        assert (qlo > 0 and sign > 0) or (qhi < 0 and sign < 0)
        square_h = [Q(2,3)*T4-2*T2*T2, Q(16,3)*T3-8*m*T2, 8*T2, Q(32,3)*m, Q(8,3)]
        assert square_h[0] == Q(2,3)*m+Q(22,3)*m*m+16*m**3+8*m**4
        assert square_h[1] == Q(16,3)*m+24*m*m+16*m**3
        assert all(a > 0 for a in square_h)
        P3 = [Q(0),m*m,2*m,Q(4,3)]
        assert derivative(P3) == power([m,Q(2)],2)
        C0 = T3/3-m*T2/2
        for t in (Q(1,10),Q(1,4),Q(2,3)):
            lam = [2*t*t+2*m*t+T2, 2*m, Q(2)]
            base = plus([Q(16,3)*T3+16*t*T2+16*m*t*t],scale(lam,-8*m))
            rounded_hprime = plus(base,[Q(0),Q(0),-16*m,Q(-64,3)])
            assert rounded_hprime == scale(plus([C0+t*v],scale(P3,-1)),16)
            assert plus(lam,[-v]) == plus(power([t+m,Q(1)],2),power([t,Q(-1)],2))
        instances.append(dict(m=str(m), sturm_positive_roots=2, sturm_roots_0_1=2,
                              larger_root_bracket=[str(lo),str(hi)], screen_sign=sign))
    note('moment/quintic/screen/envelope finite identities and isolated-root instances', instances=instances)

    for A in (Q(1,3),Q(2),Q(7,5)):
        c2 = [Q(0),Q(0),Q(1)]
        Y2 = plus([A],scale(c2,-1))
        assert plus(plus(Y2,scale(c2,-1)),[A]) == scale(Y2,2)
        deriv_num = plus(plus(times(plus(scale(c2,6),[-A]),Y2),
                              scale(times(c2,plus(scale(c2,2),[-A])),-1)),[A*A])
        assert deriv_num == scale(times(c2,Y2),8)
    note('arc-primitive differentiated numerators at rational A instances')
    ok = True
except BaseException:
    error = traceback.format_exc()
finally:
    elapsed = time.monotonic_ns()-start
    signal.alarm(0)
    body = Path(__file__).read_bytes()
    receipt = dict(kind='reviewer-owned-bounded-exact-finite-control', reviewer='A',
                   native_clock_before_execution=clock,
                   native_clock_after_execution=subprocess.check_output(['/bin/date'],text=True).strip(),
                   script_path=str(Path(__file__)), script_sha256=hashlib.sha256(body).hexdigest(),
                   script_bytes=len(body), script_LF=body.count(b'\n'),
                   arithmetic='Fraction/integer only; no floating-point mathematical computation',
                   timeout_seconds=120, elapsed_ns=elapsed, exit_code=0 if ok else 1,
                   passed=ok, checks=checks, error=error,
                   limits='Finite identities, rational signs and instance root counts only. No author code, no network, no universal optimization verification.')
    with RECEIPT.open('x',encoding='utf-8') as f:
        f.write(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
sys.exit(0 if ok else 1)
