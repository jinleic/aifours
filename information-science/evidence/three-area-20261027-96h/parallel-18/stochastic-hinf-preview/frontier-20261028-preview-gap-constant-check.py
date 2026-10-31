#!/usr/bin/env python3
"""Numerical illustration, not proof, of the two-tap causal gap constants."""
import json
import math


def simpson(f,l,u,n=4000):
    dt=(u-l)/n
    return dt/3*(f(l)+f(u)+4*sum(f(l+(2*k-1)*dt) for k in range(1,n//2+1))+2*sum(f(l+2*k*dt) for k in range(1,n//2)))


def J(rho,x):return math.expm1(rho*x)/rho if rho else x

def F(rho,x):return (math.expm1(rho*x)-rho*x)/(rho*rho) if rho else x*x/2


def main():
    T=1.5; h=.5; S=T-h; a=-.3; sigma=.7; c0=.6; ch=1.2; r=math.sqrt(T)
    rho=2*a+sigma*sigma; cross=ch*ch+2*c0*ch*math.exp(a*h)
    H=math.sqrt(c0*c0*(F(rho,T)-F(rho,h))+cross*F(rho,S))
    def f0(s):return math.sqrt(c0*c0*J(2*a,T-s)+cross*J(2*a,S-s))/H
    delta=S/8; I=(S/4,S/3); K=(2*S/3,3*S/4)
    b0=math.sqrt(simpson(lambda s:f0(s)**2,0,delta))
    bI=simpson(f0,*I); bK=simpson(f0,*K)
    eta=min(bI/(2*math.sqrt(I[1]-I[0])),bK/(2*math.sqrt(K[1]-K[0])))
    m=math.exp(-(abs(a-sigma*sigma/2)*T+2*abs(sigma)*r)); big=1/m
    earliest=c0 if c0>0 else ch; total=c0+ch
    xi=1-math.sqrt(1-earliest**2*m**2*S/(3*total**2*big**2*T))
    cI=total*m*math.sqrt(2*S/3)*bI/2
    cK=total*m*math.sqrt(S/4)*bK/2
    p=4/math.pi*sum((-1.)**j/(2*j+1)*math.exp(-(2*j+1)**2*math.pi**2*(T-delta)/(8*r*r)) for j in range(100))
    terms=[p*p*b0*b0/(128*(1+p)**2),p*eta*eta/16,xi*cI*cK*p*p/(8*H*H)]
    print(json.dumps({'T':T,'h':h,'a':a,'sigma':sigma,'c0':c0,'ch':ch,'r':r,'H':H,'p':p,
      'b0':b0,'bI':bI,'bJ':bK,'eta':eta,'m':m,'xi':xi,'cI':cI,'cJ':cK,
      'epsilon_terms':terms,'epsilon':min(terms),
      'limits':'Floating-point quadrature/series illustrates written constants; not a proof or a gain estimate.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
