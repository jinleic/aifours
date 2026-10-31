#!/usr/bin/env python3
"""Bounded high-precision diagnostic of the LAW642 rounded scalar branch.

This is not an interval proof or source-theorem verification.  It solves the
written H_R equation numerically with Decimal and a convergent arctan series.
"""
import json
from decimal import Decimal as D, getcontext

getcontext().prec = 110
PI = D('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865')


def atan_small(z):
    z2=z*z
    term=total=z
    k=1
    sign=-1
    while True:
        term*=z2
        add=term/D(2*k+1)
        if abs(add)<D('1e-105'):
            return total
        total+=sign*add
        sign=-sign
        k+=1


def asin_dec(x):
    if not 0 <= x < 1:
        raise ValueError('arcsine argument outside diagnostic range')
    z=x/(1-x*x).sqrt()
    return 2*atan_small(z/(1+(1+z*z).sqrt()))


def rounded(b,d):
    m=b/(1-b)
    T2=m+2*m*m
    T3=m+6*m*m+6*m**3
    T4=m+14*m*m+36*m**3+24*m**4
    v=m+m*m
    C0=T3/3-m*T2/2
    P=D(4)/3*d**3+2*m*d*d+m*m*d
    t=(P-C0)/v
    lam=2*t*t+2*d*d+2*m*(t+d)+T2
    c=t-d
    A=lam-v
    w=2*t
    if not (0<d<D('0.5') and c>0 and A>c*c and T2<lam<T4/(3*T2)):
        raise ValueError('selected rounded branch screen failed')
    root=(A-c*c).sqrt()
    J3=(c*root*(5*A-2*c*c)+3*A*A*asin_dec(c/A.sqrt()))/8
    Rint=-D(2)/3*J3+(m*A-m**3/3)*c-c**4/3+lam*c*c/2
    Uint=(w**3/3+m*w*w+(T2-lam)*w)*c
    Uint+=(-w*w-2*m*w+2*lam-T2)*c*c/2+D(2)/3*(w+m)*c**3-D(2)/3*c**4
    M2=w*w+2*m*w+T2
    M4=w**4+4*m*w**3+6*T2*w*w+4*T3*w+T4
    H=D(2)/3*M4-2*lam*M2+8*(Rint-Uint)
    return H,t,lam,T2


def main():
    sqrt2=D(2).sqrt()
    R=(D(4)/(3*PI)).sqrt().sqrt()
    c0=2/(3*PI).sqrt()
    c1=8*sqrt2/(3*PI*R)
    c2=8*sqrt2/(5*PI*R**3*getcontext().power(D(4),D(2)/3))
    c4=1+2/PI
    results=[]
    for s in map(D,('0.000001','0.0000001','0.00000001','0.000000001')):
        b=s**4
        d0=getcontext().power(b/4,D(1)/3)
        lo,hi=D('0.4'),D('0.8')
        if not (rounded(b,d0*(1+lo*s))[0]>0 and rounded(b,d0*(1+hi*s))[0]<0):
            raise ValueError('numerical sign bracket failed')
        for _ in range(160):
            mid=(lo+hi)/2
            if rounded(b,d0*(1+mid*s))[0]>0:
                lo=mid
            else:
                hi=mid
        d=d0*(1+(lo+hi)*s/2)
        H,t,lam,T2=rounded(b,d)
        delta=((lam-T2).sqrt()-sqrt2*t)/s
        delta_scaled=delta/getcontext().power(s,D(2)/3)
        third=(lam-c0*s*s-c1*s**3)/getcontext().power(s,D(11)/3)
        fourth=(lam-c0*s*s-c1*s**3+c2*getcontext().power(s,D(11)/3))/s**4
        results.append({'s':str(s),'value':format(lam,'.16E'),
                        'delta_scaled':format(delta_scaled,'.12f'),
                        'third_scaled':format(third,'.12f'),
                        'fourth_scaled':format(fourth,'.12f'),
                        'rounded_screen':'PASS','sign_bracket':'PASS'})
    print(json.dumps({'precision':getcontext().prec,'samples':results,
        'predicted_delta':format(1/(getcontext().power(D(4),D(2)/3)*R),'.12f'),
        'predicted_third':format(-c2,'.12f'),'predicted_fourth':format(c4,'.12f'),
        'scope':'Numerical branch diagnostic only; not an interval bound, universal proof, or theorem acceptance.'},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
