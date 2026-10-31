#!/usr/bin/env python3
"""Illustrate all-signed preview kernel constants via bounded float quadrature."""
import json
import math


def simpson(f,lo,hi,n=4000):
    dt=(hi-lo)/n
    return dt/3*(f(lo)+f(hi)+4*sum(f(lo+(2*k-1)*dt) for k in range(1,n//2+1))+2*sum(f(lo+2*k*dt) for k in range(1,n//2)))


def J(rho,x):return math.expm1(rho*x)/rho if rho else x

def F(rho,x):return (math.expm1(rho*x)-rho*x)/(rho*rho) if rho else x*x/2


def main():
    T=1.5; h=.5; S=T-h; a=-.3; sigma=.7; c0=1.2; ch=-.6; r=math.sqrt(T)
    rho=2*a+sigma*sigma
    remainder=(c0*math.exp(a*h)+ch)**2+c0*c0*math.exp(2*a*h)*math.expm1(sigma*sigma*h)
    H=math.sqrt(c0*c0*S*J(rho,h)+remainder*F(rho,S))
    def f0(s):return math.sqrt(c0*c0*J(2*a,h)+(c0*math.exp(a*h)+ch)**2*J(2*a,S-s))/H
    delta=S/8; I=(S/4,S/3); K=(2*S/3,3*S/4)
    b0=math.sqrt(simpson(lambda s:f0(s)**2,0,delta))
    bI=simpson(f0,*I); bK=simpson(f0,*K)
    eta=min(bI/(2*math.sqrt(I[1]-I[0])),bK/(2*math.sqrt(K[1]-K[0])))
    m=math.exp(-(abs(a-sigma*sigma/2)*T+2*abs(sigma)*r)); big=1/m
    Q=abs(c0)+abs(ch); prefix=min(h,S/3)
    xi=1-math.sqrt(1-c0*c0*m*m*prefix/(Q*Q*big*big*T))
    lower=abs(c0)*m*math.sqrt(h)
    cI=lower*bI/2; cK=lower*bK/2
    p=4/math.pi*sum((-1.)**j/(2*j+1)*math.exp(-(2*j+1)**2*math.pi**2*(T-delta)/(8*r*r)) for j in range(100))
    terms=[p*p*b0*b0/(128*(1+p)**2),p*eta*eta/16,xi*cI*cK*p*p/(8*H*H)]
    print(json.dumps({'T':T,'h':h,'a':a,'sigma':sigma,'c0':c0,'ch':ch,'r':r,'H':H,
      'tail_mean_square':remainder,'p':p,'b0':b0,'bI':bI,'bJ':bK,'eta':eta,
      'm':m,'xi':xi,'cI':cI,'cJ':cK,'epsilon_terms':terms,'epsilon':min(terms),
      'limits':'Float/Simpson/series illustration only; all-input claims use the written argument.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
