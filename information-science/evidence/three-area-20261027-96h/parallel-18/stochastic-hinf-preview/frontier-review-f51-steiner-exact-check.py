#!/usr/bin/env python3
"""Exact symbolic strip/sector and geometric-moment checks for f51."""
from fractions import Fraction as F
import json


def add(*ps):
    z={}
    for p in ps:
        for k,v in p.items(): z[k]=z.get(k,F(0))+v
    return {k:v for k,v in z.items() if v}


def scale(p,c):
    return {k:v*F(c) for k,v in p.items() if v*c}


def mul(a,b):
    out={}
    for (am,at,ar,ap),av in a.items():
        for (bm,bt,br,bp),bv in b.items():
            raw=ar+br
            key=(am+bm,at+bt,raw%2,ap+bp)
            out[key]=out.get(key,F(0))+av*bv*(2**(raw//2))
    return {k:v for k,v in out.items() if v}


def power(a,n):
    out={(0,0,0,0):F(1)}
    for _ in range(n): out=mul(out,a)
    return out


def deriv_m(p):
    out={}
    for (m,t,r,powpi),v in p.items():
        if m: out[(m-1,t,r,powpi)]=m*v
    return out


def main():
    one={(0,0,0,0):F(1)}; m={(1,0,0,0):F(1)}; t={(0,1,0,0):F(1)}
    root2={(0,0,1,0):F(1)}; pi={(0,0,0,1):F(1)}
    M=[one]
    for _ in range(4):
        M.append(add(mul(mul(m,add(one,m)),deriv_m(M[-1])),mul(m,M[-1])))
    T2=add(m,scale(power(m,2),2))
    T3=add(m,scale(power(m,2),6),scale(power(m,3),6))
    T4=add(m,scale(power(m,2),14),scale(power(m,3),36),scale(power(m,4),24))
    if M[2:]!=[T2,T3,T4]: raise RuntimeError('geometric moments differ')

    # Independent strip/vertex contributions, kD + tB, before taking E_k:
    # base=2/3*k^4; four edge strips = 4[(2sqrt2/3)k^3 t
    # + k^2 t^2 +(sqrt2/3) k t^3]; four sectors =
    # 4[(pi/4)k^2 t^2+(2sqrt2/3)k t^3+(pi/8)t^4].
    base=scale(M[4],F(2,3))
    strips=add(scale(mul(root2,mul(M[3],t)),F(8,3)),
               scale(mul(M[2],power(t,2)),4),
               scale(mul(root2,mul(M[1],power(t,3))),F(4,3)))
    sectors=add(mul(pi,mul(M[2],power(t,2))),
                scale(mul(root2,mul(M[1],power(t,3))),F(8,3)),
                scale(mul(pi,power(t,4)),F(1,2)))
    independently_summed=add(base,strips,sectors)
    expected=add(scale(M[4],F(2,3)),
                 scale(mul(root2,mul(M[3],t)),F(8,3)),
                 mul(add(scale(one,4),pi),mul(M[2],power(t,2))),
                 scale(mul(root2,mul(M[1],power(t,3))),4),
                 scale(mul(pi,power(t,4)),F(1,2)))
    if independently_summed!=expected: raise RuntimeError('moment normalizer differs')
    # Area starts at 2k^2; four strips give 4sqrt2*k*t, sectors pi*t^2.
    area=add(scale(M[2],2),scale(mul(root2,mul(M[1],t)),4),mul(pi,power(t,2)))
    expected_area=add(scale(T2,2),scale(mul(root2,mul(m,t)),4),mul(pi,power(t,2)))
    if area!=expected_area: raise RuntimeError('area normalizer differs')
    cap_one=F(4,3)*F(2,5)
    cap_four=4*cap_one
    cap_to_support=(cap_four/F(8,3))*2*F(1,4)
    if (cap_one,cap_four,cap_to_support)!=(F(8,15),F(32,15),F(2,5)):
        raise RuntimeError('cap coefficient differs')
    print(json.dumps({
        'geometric_moments_T2_T3_T4':'PASS (formal m-polynomials)',
        'full_disk_shell_area_normalizer':'PASS (formal m,t,sqrt2,pi)',
        'full_disk_shell_second_moment_normalizer':'PASS (separate strip/sector summation)',
        'one_cap_deficit_coefficient':str(cap_one),
        'four_cap_deficit_coefficient':str(cap_four),
        'cap_to_support_ratio_at_stationary_scale':str(cap_to_support),
        'net_support_fraction':str(1-cap_to_support),
        'limits':'Exact formal algebra only; no proof of actual core selection, Hausdorff convergence, cap remainder or global optimum.'
    },indent=2,sort_keys=True))


if __name__=='__main__': main()
