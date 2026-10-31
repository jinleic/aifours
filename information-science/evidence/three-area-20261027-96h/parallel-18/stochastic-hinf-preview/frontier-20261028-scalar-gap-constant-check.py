#!/usr/bin/env python3
"""Numeric illustration of a written positive scalar literal-gain gap."""
import json
import math


def simpson(fn, lo, hi, n=4000):
    h=(hi-lo)/n
    return h/3*(fn(lo)+fn(hi)+4*sum(fn(lo+(2*j-1)*h) for j in range(1,n//2+1))+2*sum(fn(lo+2*j*h) for j in range(1,n//2)))


def main():
    T=1.0; a=-0.3; sigma=0.7; r=1.0
    rho=2*a+sigma*sigma
    H=math.sqrt((math.expm1(rho*T)-rho*T)/(rho*rho) if rho else T*T/2)
    def f0(s):
        q=2*a
        val=math.expm1(q*(T-s))/q if q else T-s
        return math.sqrt(val)/H
    delta=T/8; I=(T/4,T/3); J=(2*T/3,3*T/4)
    b0=math.sqrt(simpson(lambda s:f0(s)**2,0,delta))
    bI=simpson(f0,*I); bJ=simpson(f0,*J)
    eta=min(bI/(2*math.sqrt(I[1]-I[0])),bJ/(2*math.sqrt(J[1]-J[0])))
    M=abs(a-sigma*sigma/2)*T+2*abs(sigma)*r
    m=math.exp(-M); big=math.exp(M)
    xi=1-math.sqrt(1-m*m/(3*big*big))
    cI=m*math.sqrt(2*T/3)*bI/2
    cJ=m*math.sqrt(T/4)*bJ/2
    length=T-delta
    p=4/math.pi*sum(((-1.0)**k)/(2*k+1)*math.exp(-((2*k+1)**2)*math.pi**2*length/(8*r*r)) for k in range(100))
    terms=[p*p*b0*b0/(128*(1+p)**2),p*eta*eta/16,xi*cI*cJ*p*p/(8*H*H)]
    print(json.dumps({'T':T,'a':a,'sigma':sigma,'r':r,'H':H,'survival_p':p,
        'b0':b0,'bI':bI,'bJ':bJ,'eta':eta,'xi':xi,'cI':cI,'cJ':cJ,
        'epsilon_terms':terms,'epsilon':min(terms),'bound_times_H':(1-min(terms))*H,
        'limits':'Float/Simpson/series numeric illustration only; positivity and uniform gap use the written all-input argument.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
