#!/usr/bin/env python3
"""Exact finite witness that unit band coordinates need not be constant.

The source A=R^1 semidirect C2 embeds faithfully in (R x R^1) semidirect C2
with nonconstant unit coefficients. Its 40-element Rees lift is checked fully.
"""
from itertools import product


def require(ok,why):
    if not ok:raise ValueError(why)


def rect(a,b):return (a[0],b[1])

def band(a,b):
    if a is None:return b
    if b is None:return a
    return rect(a,b)

def flip(x,g):
    return x if x is None or g==0 else (1-x[0],1-x[1])

def action(x,g):return (flip(x[0],g),flip(x[1],g))

def bm(x,y):return (rect(x[0],y[0]),band(x[1],y[1]))

def am(x,y):return (band(x[0],flip(y[0],x[1])),(x[1]+y[1])%2)

def main():
    R=list(product(range(2),repeat=2))
    B0=[None]+R
    A=list(product(B0,range(2)))
    eR=(0,0)
    def bcoef(a):return (rect(eR,flip(eR,a[1])),a[0])
    def theta(a):return a[1]
    one=(None,0);u=(None,1);e=bcoef(one)
    require(bcoef(u)!=e,'unit coefficients unexpectedly constant')
    require(bcoef(u)==bm(e,action(e,theta(u))),'unit formula')
    require(len({(bcoef(a),theta(a)) for a in A})==len(A),'A embedding')
    require(all(bcoef(am(a,b))==bm(bcoef(a),action(bcoef(b),theta(a)))
                for a,b in product(A,repeat=2)),'A host law')
    require(all(bm(bcoef(a),action(e,theta(a)))==bcoef(a) for a in A),'right identity law')
    require(all(bm(e,bcoef(a))==bcoef(a) for a in A),'left identity law')
    S=list(product(range(2),A,range(2)))
    def P(lam,i):return u if lam==1 and i==1 else one
    def mul(s,t):return (s[0],am(am(s[1],P(s[2],t[0])),t[1]),t[2])
    def actor(s):return (s[0],theta(s[1]),s[2])
    def idem(s):return mul(s,s)==s
    require(all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(S,repeat=3)),'associativity')
    E=[s for s in S if idem(s)]
    require(all(any(mul(mul(s,t),s)==s and mul(mul(t,s),t)==t for t in S) for s in S),'regularity')
    def actor_idem(d):return d[1]==int(d[0]==1 and d[2]==1)
    require(all(idem(s)==actor_idem(actor(s)) for s in S),'actor purity')
    def source_beta(s):return bcoef(s[1])
    def host_band(s,t):
        weight=(theta(s[1])+theta(P(s[2],t[0])))%2
        return bm(source_beta(s),action(source_beta(t),weight))
    require(all(source_beta(mul(s,t))==host_band(s,t) for s,t in product(S,repeat=2)),'lift host law')
    require(len({(source_beta(s),actor(s)) for s in S})==len(S),'lift injection')
    contexts=[None]+S
    def ctx(x,a,y):
        z=a if x is None else mul(x,a)
        return z if y is None else mul(z,y)
    sig={s:bytes(idem(ctx(x,s,y)) for x,y in product(contexts,repeat=2)) for s in S}
    require(all((sig[s]==sig[t])==(actor(s)==actor(t)) for s,t in product(S,repeat=2)), 'actual tau')
    same=[(s,t) for s,t in product(E,repeat=2) if s!=t and actor(s)==actor(t)]
    rp=[(s,t) for s,t in same if mul(s,t)==t and mul(t,s)==s]
    lp=[(s,t) for s,t in same if mul(s,t)==s and mul(t,s)==t]
    require(rp and lp and all(source_beta(s)!=source_beta(t) for s,t in rp+lp),'R/L separation')
    wrong=sum(source_beta(mul(s,t))!=bm(source_beta(s),action(source_beta(t),theta(s[1])))
              for s,t in product(S,repeat=2))
    require(wrong>0,'missing actor sandwich control')
    print('source_A=',len(A),' source_rees=',len(S),' idempotents=',len(E),sep='')
    print('unit_band_coefficients=',(e,bcoef(u)),' distinct=True',sep='')
    print('actual_actor_classes=',len(set(map(actor,S))),' same_q_R=',len(rp),' same_q_L=',len(lp),sep='')
    print('PASS automatic unit formula, identity absorption, faithful A and full Rees host, complete tau')
    print('CONTROL omit sandwich group action mismatches=',wrong,sep='')
    print('LIMIT: one finite representation only; universal identity requires written proof')


if __name__=='__main__':main()
