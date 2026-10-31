#!/usr/bin/env python3
"""Exact finite check where the Rees actor r is strictly finer than q_tau.

A=(rectangular band with 1) semidirect C2; S=M[A;3,3;P].  The 18-element
actor has duplicate sandwich rows/columns and the actual tau quotient has
8 elements. Checks all source contexts and the explicitly pushed host.
"""
from itertools import product


def require(ok,why):
    if not ok: raise ValueError(why)


def bm(a,b):
    if a is None:return b
    if b is None:return a
    return (a[0],b[1])


def flip(a,h):
    return a if a is None or h==0 else (1-a[0],1-a[1])


def am(a,b):
    return (bm(a[0],flip(b[0],a[1])),(a[1]+b[1])%2)


def main():
    B=[None]+list(product(range(2),repeat=2))
    A=list(product(B,range(2)))
    S=list(product(range(3),A,range(3)))
    P=((0,0,0),(0,0,0),(0,0,1))
    def mul(s,t):
        i,a,lam=s;j,b,mu=t
        return (i,am(am(a,(None,P[lam][j])),b),mu)
    def idem(s):return mul(s,s)==s
    def r(s):return (s[0],s[1][1],s[2])
    def q(s):return (int(s[0]==2),s[1][1],int(s[2]==2))
    def beta(s):return (s[1][0],s[0],s[2])
    def bandmul(x,y):return (bm(x[0],y[0]),x[1],y[2])
    def act(x,h):return (flip(x[0],h),x[1],x[2])
    def context(x,a,y):
        z=a if x is None else mul(x,a)
        return z if y is None else mul(z,y)

    require(all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(S,repeat=3)),'associativity')
    E=[a for a in S if idem(a)]
    require(all(any(mul(mul(a,b),a)==a and mul(mul(b,a),b)==b for b in S) for a in S),'regular')
    nonclosed=next(((a,b,mul(a,b)) for a,b in product(E,repeat=2) if not idem(mul(a,b))),None)
    require(nonclosed is not None,'expected nonorthodox')
    for e in E:
        corner={mul(mul(e,a),e) for a in S}
        ce=[a for a in corner if idem(a)]
        require(all(idem(mul(a,b)) for a,b in product(ce,repeat=2)),'local orthodox')
        require(all(mul(mul(mul(mul(a,b),a),c),a)==mul(mul(mul(a,b),c),a)
                    for a,b,c in product(ce,repeat=3)),'local regular band')
    for a in S:
        left={mul(e,a) for e in E}
        right={mul(a,e) for e in E}
        require(not (left&right&set(E)) or idem(a),'weak E-unitary')
    contexts=[None]+S
    sig={a:bytes(idem(context(x,a,y)) for x,y in product(contexts,repeat=2)) for a in S}
    require(all((sig[a]==sig[b])==(q(a)==q(b)) for a,b in product(S,repeat=2)), 'actual tau')
    require(len({r(a) for a in S})==18 and len({q(a) for a in S})==8,'actor sizes')
    for a,b in product(S,repeat=2):
        weight=(a[1][1]+P[a[2]][b[0]])%2
        require(beta(mul(a,b))==bandmul(beta(a),act(beta(b),weight)),'pushed host law')
    require(len({(beta(a),q(a)) for a in S})==len(S),'pushed host injectivity')
    same=[(e,f) for e,f in product(E,repeat=2) if e!=f and q(e)==q(f)]
    rp=[(e,f) for e,f in same if mul(e,f)==f and mul(f,e)==e]
    lp=[(e,f) for e,f in same if mul(e,f)==e and mul(f,e)==f]
    require(rp and lp and all(beta(e)!=beta(f) for e,f in rp+lp),'R/L separation')
    def broken_beta(s):return (s[1][0],0,s[2])
    require(len({(broken_beta(s),q(s)) for s in S})<len(S),'row-collapse control')
    print('source_size=',len(S),' idempotents=',len(E),' actor_r=',len({r(a) for a in S}),
          ' actor_q=',len({q(a) for a in S}),sep='')
    print('complete_contexts_per_source=',len(contexts)**2,' nonclosed_E=',nonclosed,sep='')
    print('same_q_idempotent_pairs=',len(same),' R_pairs=',len(rp),' L_pairs=',len(lp),sep='')
    print('PASS source regularity, local_r, WEU, full actual tau, pushed host and R/L separation')
    print('CONTROL collapsing original source row rejected by pushed-host injectivity')
    print('LIMIT: one finite example; arbitrary coarsened-actor pushforward needs written proof')


if __name__=='__main__':main()
