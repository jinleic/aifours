#!/usr/bin/env python3
"""Floating-point illustration of arbitrary-matrix preview gap constants."""
import json
import math


def gv(t,x,y):
    k=math.sqrt(.59); factor=math.exp(-.3*t); co=math.cos(k*t); si=math.sin(k*t)/k
    v0=factor*(co*x+si*(.1*x+y)); v1=factor*(co*y+si*(-.6*x-.1*y))
    return (v0+.2*v1,-.3*v0+.7*v1)


def n2(v):return v[0]**2+v[1]**2


def simpson(f,lo,hi,n=160):
    dt=(hi-lo)/n
    return dt/3*(f(lo)+f(hi)+4*sum(f(lo+(2*k-1)*dt) for k in range(1,n//2+1))+2*sum(f(lo+2*k*dt) for k in range(1,n//2)))


def main():
    T=1.5; h=.45; S=T-h; sigma=.7; r=math.sqrt(T)
    def b(v):return gv(v,1,.4)
    def c(v):return gv(v,-.4,1.2)
    def normG(g,x):return math.sqrt(simpson(lambda v:n2(g(v)),0,x,800))
    early=lambda v:math.exp(sigma*sigma*v)*n2(b(v))
    def late(v):
        B=b(h+v); C=c(v); joint=(B[0]+C[0],B[1]+C[1])
        return (S-v)*math.exp(sigma*sigma*v)*(n2(joint)+math.expm1(sigma*sigma*h)*n2(B))
    H=math.sqrt(S*simpson(early,0,h,800)+simpson(late,0,S,800))
    early_mean=simpson(lambda v:n2(b(v)),0,h,200)
    def f0(s):
        def sq(v):
            B=b(h+v); C=c(v)
            return (B[0]+C[0])**2+(B[1]+C[1])**2
        return math.sqrt(early_mean+simpson(sq,0,S-s,160))/H
    delta=S/8; I=(S/4,S/3); J=(2*S/3,3*S/4)
    b0=math.sqrt(simpson(lambda s:f0(s)**2,0,delta,160))
    bI=simpson(f0,*I,160); bJ=simpson(f0,*J,160)
    eta=min(bI/(2*math.sqrt(I[1]-I[0])),bJ/(2*math.sqrt(J[1]-J[0])))
    m=math.exp(-sigma*sigma*T/2-2*abs(sigma)*r); M=1/m
    Q=normG(b,T)+normG(c,T); P=m*normG(b,min(h,S/3))
    xi=1-math.sqrt(1-P*P/(M*M*Q*Q))
    lam=m*normG(b,h); cI=lam*bI/2; cJ=lam*bJ/2
    p=4/math.pi*sum((-1.)**k/(2*k+1)*math.exp(-(2*k+1)**2*math.pi**2*(T-delta)/(8*r*r)) for k in range(100))
    terms=[p*p*b0*b0/(128*(1+p)**2),p*eta*eta/16,xi*cI*cJ*p*p/(8*H*H)]
    print(json.dumps({'T':T,'h':h,'sigma':sigma,'r':r,'H':H,'p':p,'b0':b0,'bI':bI,'bJ':bJ,
      'eta':eta,'m':m,'Q':Q,'P':P,'xi':xi,'lambdaI':lam,'lambdaJ':lam,
      'cI':cI,'cJ':cJ,'epsilon_terms':terms,'epsilon':min(terms),
      'limits':'Floating-point nested quadrature / Brownian series only; not proof.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
