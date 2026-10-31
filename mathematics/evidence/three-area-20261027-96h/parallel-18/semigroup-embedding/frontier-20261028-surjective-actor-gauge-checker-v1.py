#!/usr/bin/env python3
"""Exact finite check of pure-CS actor pushforward with nontrivial row gauges.

D0 is a 3x3 Rees semigroup over C2, D1 a 2x2 quotient with duplicate
row/column images. All host elements and source pairs are checked directly.
"""
from itertools import product


def require(ok,why):
    if not ok:raise ValueError(why)


def bm(a,b):
    if a is None:return b
    if b is None:return a
    return (a[0],b[1])


def flip(a,h):
    return a if a is None or h==0 else (1-a[0],1-a[1])


def main():
    B=[None]+list(product(range(2),repeat=2))
    G=range(2); I=range(3); L=range(3)
    rows=(0,0,1);cols=(0,0,1)
    u=(0,1,0);v=(0,1,0)
    Q=((0,0),(0,1))
    P=tuple(tuple((v[lam]+Q[cols[lam]][rows[i]]+u[i])%2 for i in I) for lam in L)
    D=list(product(I,G,L));D1=list(product(range(2),G,range(2)))
    def dm(x,y):return (x[0],(x[1]+P[x[2]][y[0]]+y[1])%2,y[2])
    def em(x,y):return (x[0],(x[1]+Q[x[2]][y[0]]+y[1])%2,y[2])
    def f(x):return (rows[x[0]],(u[x[0]]+x[1]+v[x[2]])%2,cols[x[2]])
    def ei(x):return dm(x,x)==x
    def ej(x):return em(x,x)==x
    require(all(dm(dm(a,b),c)==dm(a,dm(b,c)) for a,b,c in product(D,repeat=3)),'actor associative')
    require(all(f(dm(a,b))==em(f(a),f(b)) for a,b in product(D,repeat=2)),'actor homomorphism')
    require(set(map(f,D))==set(D1),'actor surjectivity')
    require(all(ei(a)==ej(f(a)) for a in D),'actor purity')
    # Complete source syntactic contexts including both independently absent factors.
    contexts=[None]+D
    def context(x,a,y):
        z=a if x is None else dm(x,a)
        return z if y is None else dm(z,y)
    signatures={a:bytes(ei(context(x,a,y)) for x,y in product(contexts,repeat=2)) for a in D}
    require(all((signatures[a]==signatures[b])==(f(a)==f(b)) for a,b in product(D,repeat=2)),
            'actual tau kernel')
    for e in [a for a in D if ei(a)]:
        loc={dm(dm(e,a),e) for a in D}
        e1=f(e);loc1={em(em(e1,a),e1) for a in D1}
        require(set(map(f,loc))==loc1 and len(loc)==len(loc1),'local group isomorphism')

    Host=list(product(B,D))
    def hm(x,y):
        b,(i,g,lam)=x;d,(j,h,mu)=y
        return (bm(b,flip(d,(g+P[lam][j])%2)),dm(x[1],y[1]))
    def pushed(x):
        b,(i,g,lam)=x
        return ((i,lam,flip(b,u[i])),f(x[1]))
    def pm(x,y):
        (i,lam,b),v0=x;(j,mu,d),v1=y
        w=(v0[1]+Q[v0[2]][v1[0]])%2
        return ((i,mu,bm(b,flip(d,w))),em(v0,v1))
    require(len(set(map(pushed,Host)))==len(Host),'pushed injection')
    require(all(pushed(hm(x,y))==pm(pushed(x),pushed(y)) for x,y in product(Host,repeat=2)),
            'pushed host law')
    def broken(x):
        b,(i,g,lam)=x
        return ((i,lam,b),f(x[1]))
    wrong=sum(broken(hm(x,y))!=pm(broken(x),broken(y)) for x,y in product(Host,repeat=2))
    require(wrong>0,'row gauge mutation')
    print('source_actor=',len(D),' quotient_actor=',len(D1),' source_host=',len(Host),sep='')
    print('source_sandwich=',P,' row_gauges=',u,' col_gauges=',v,sep='')
    print('PASS full tau, pure surjective actor, every local-group isomorphism')
    print('PASS all 8100 source-host products and pushed-host injection with nontrivial row gauges')
    print('CONTROL omitted-row-gauge mismatches=',wrong,sep='')
    print('LIMIT: one finite example; general CS pushforward requires the written proof')


if __name__=='__main__':main()
