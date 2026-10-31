#!/usr/bin/env python3
"""Exact certifications for the N=1 diamond-trial extension and the L(m) lower bound.
All arithmetic in fractions.Fraction. No floats enter any certification; float() is
used only to print human-readable root locations."""
from fractions import Fraction as F
import hashlib, subprocess, datetime

def now():
    return subprocess.run(['/bin/date'], capture_output=True, text=True).stdout.strip()

def P_at(g, m):
    return (g**5 + 5*m*g**4 + (2*m+12*m*m)*g**3 + (12*m**3-2*m)*g*g
            - m*(1+2*m)*(1+6*m)*g + m*m*(1+2*m))

def Ts(m):
    return (m+2*m*m, m+6*m*m+6*m**3, m+14*m*m+36*m**3+24*m**4)

def M2(g,m):
    T2,_,_ = Ts(m); return g*g+2*m*g+T2

def M4(g,m):
    T2,T3,T4 = Ts(m)
    return g**4+4*m*g**3+6*T2*g*g+4*T3*g+T4

def S(g,m):
    """S = M4 - (3/2)M2 ; sign(S(g*)) = sign(lambda_g - 1/2)."""
    return M4(g,m) - F(3,2)*M2(g,m)

def certify(m, grid=400, iters=120):
    """Isolate the larger root g* of P_m in (0,1) by exact bisection and certify
    the strict sign of S at g* by evaluating at both enclosure endpoints."""
    prev_g, prev_v, lo = F(0), P_at(F(0), m), None
    assert prev_v > 0
    for k in range(1, grid+1):
        g = F(k, grid); v = P_at(g, m)
        if prev_v < 0 < v:
            lo = prev_g
        prev_v = v; prev_g = g
    assert lo is not None
    hi = F(1); assert P_at(F(1), m) > 0
    for _ in range(iters):
        mid = (lo+hi)/2
        if P_at(mid, m) < 0: lo = mid
        else: hi = mid
    s_lo, s_hi = S(lo,m), S(hi,m)
    assert (s_lo < 0 and s_hi < 0) or (s_lo > 0 and s_hi > 0)
    return ('below' if s_lo < 0 else 'above'), lo, hi

def exp_below(x, bound, terms=14):
    """Certify exp(x) < bound for rational x>0 by a truncated series plus geometric remainder."""
    s = F(0); fact = 1; pw = F(1)
    for k in range(terms):
        s += pw/fact; pw *= x; fact *= (k+1)
    # remainder <= pw/fact * 1/(1-x/(terms+1)) when x < terms+1
    assert x < terms
    s += pw/fact/(1 - x/F(terms))
    return s < bound

def main():
    print('native date before run:', now())
    out = []
    # (A) L(m) root bracket
    p = lambda m: 16*m**3+16*m**2-1
    assert p(F(11,50)) < 0 < p(F(23,100))
    out.append('PASS A: unique positive root m_L of 16m^3+16m^2-1 lies in (11/50, 23/100); '
               'values %s , %s' % (p(F(11,50)), p(F(23,100))))
    # (B) m0 brackets: coarse and refined; 743/10000 > m0
    delta = lambda m: 24*m**4+48*m**3+26*m*m+2*m-F(5,16)
    assert delta(F(1,14)) < 0 < delta(F(1,13))
    assert delta(F(742,10000)) < 0 < delta(F(743,10000))
    out.append('PASS B: m0 in (742/10000, 743/10000) [also in (1/14,1/13)]; '
               'Delta strictly increasing, so 743/10000 > m0')
    # (C) lambda_g signs: m1=743/10000 (above m0, below the crossing), m2=3/40 and 1/13 above
    s1,lo1,hi1 = certify(F(743,10000))
    s2,lo2,hi2 = certify(F(3,40))
    s3,lo3,hi3 = certify(F(1,13))
    assert s1=='below' and s2=='above' and s3=='above'
    out.append('PASS C: lambda_g(743/10000)<1/2<lambda_g(3/40); lambda_g(1/13)>1/2; '
               'hence m_cprime in (743/10000, 3/40) and m_cprime < 1/13')
    out.append('       g* enclosures (float display only): %.12f %.12f | %.12f %.12f | %.12f %.12f'
               % (lo1,hi1,lo2,hi2,lo3,hi3))
    assert 14*12 < 169
    out.append('PASS D: 14*12=168 < 169, so m<1/13 implies v=m(1+m)<14/169<1/12')
    # (E) cutoff-exactly-2 interval nonempty: sqrt(2) < 1415/1000 and exp(1415/1000) < 123/23
    assert F(1415*1415, 1000000) > 2
    assert exp_below(F(1415,1000), F(123,23))
    out.append('PASS E: sqrt(2) < 1415/1000 and exp(1415/1000) < 123/23 = %s' % F(123,23))
    for line in out:
        print(line)
    print('ALL PASS')
    print('native date after run:', now())
    with open(__file__,'rb') as f:
        print('script sha256:', hashlib.sha256(f.read()).hexdigest())

if __name__ == '__main__':
    main()
