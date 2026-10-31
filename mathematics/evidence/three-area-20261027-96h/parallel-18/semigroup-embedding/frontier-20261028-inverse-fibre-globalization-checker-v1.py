#!/usr/bin/env python3
"""Exact small inverse-monoid control for the constructed preorder model.

A={1,z,p}, p^2=z, z^2=z, zp=pz=p, pure quotient C2. Builds the quotient
GxE relation, preorder, actual principal downsets and an explicit 12-element
Rees source. No author checker import, external packages, randomness or writes.
"""
from itertools import product


def require(ok,why):
    if not ok:raise ValueError(why)


def mul(a,b):
    if a=='1':return b
    if b=='1':return a
    if a=='z':return b
    if b=='z':return a
    return 'z'


def main():
    A=('1','z','p');G=(0,1);E=('1','z')
    theta={'1':0,'z':0,'p':1}
    inv={'1':'1','z':'z','p':'p'}
    def le(e,f):return mul(e,f)==e
    pairs=list(product(G,E))
    parent={x:x for x in pairs}
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    def union(a,b):
        a,b=root(a),root(b)
        if a!=b:parent[b]=a
    for g,e,s in product(G,E,A):
        if le(e,mul(s,inv[s])):
            union((g,e),((g+theta[s])%2,mul(mul(inv[s],e),s)))
    classes={}
    for x in pairs:classes.setdefault(root(x),[]).append(x)
    Y=tuple(classes)
    def cl(g,e):return root((g,e))
    def leq(x,y):
        for g,e in classes[x]:
            for h,f in classes[y]:
                for s in A:
                    if (g+theta[s])%2==h and le(e,mul(s,inv[s])) and le(mul(mul(inv[s],e),s),f):
                        return True
        return False
    require(all(leq(x,x) for x in Y),'reflexivity')
    require(all(not (leq(x,y) and leq(y,z)) or leq(x,z) for x,y,z in product(Y,repeat=3)), 'transitivity')
    def shift(g,x):
        vals={cl((g+h)%2,e) for h,e in classes[x]}
        require(len(vals)==1,'shift well-defined')
        return next(iter(vals))
    def shiftset(g,D):return frozenset(shift(g,x) for x in D)
    def down(g,e):return frozenset(x for x in Y if leq(x,cl(g,e)))
    def beta(a):return down(0,mul(a,inv[a]))
    for a,b in product(A,repeat=2):
        require(beta(mul(a,b))==beta(a)&shiftset(theta[a],beta(b)), 'semidirect coefficient law')
    require(len({(beta(a),theta[a]) for a in A})==len(A),'base injection')
    e=beta('1')
    require(beta('p')==e&shiftset(1,e),'nonunit maximum not tight')
    require(beta('z')!=e,'proper idempotent separation')
    require(beta('p')!=e&shiftset(0,e),'wrong-action control')

    P=(('1','1'),('1','p'))
    S=list(product(range(2),A,range(2)))
    def sm(x,y):return (x[0],mul(mul(x[1],P[x[2]][y[0]]),y[1]),y[2])
    def idem(x):return sm(x,x)==x
    def actor(x):return (x[0],theta[x[1]],x[2])
    def ctx(x,a,y):
        v=a if x is None else sm(x,a)
        return v if y is None else sm(v,y)
    E_S=[s for s in S if idem(s)]
    require(all(any(sm(sm(s,t),s)==s and sm(sm(t,s),t)==t for t in S) for s in S),'source regularity')
    contexts=[None]+S
    sig={s:bytes(idem(ctx(x,s,y)) for x,y in product(contexts,repeat=2)) for s in S}
    require(all((sig[s]==sig[t])==(actor(s)==actor(t)) for s,t in product(S,repeat=2)), 'source actual tau')
    for s,t in product(S,repeat=2):
        weight=(theta[s[1]]+theta[P[s[2]][t[0]]])%2
        require(beta(sm(s,t)[1])==beta(s[1])&shiftset(weight,beta(t[1])),'Rees host law')
    require(len({(beta(s[1]),actor(s)) for s in S})==len(S),'Rees host injection')
    require(any(not idem(sm(s,t)) for s,t in product(E_S,repeat=2)), 'expected nonorthodox')
    print('inverse_A_size=3 equivalence_classes=',len(Y),' preorder_pairs=',sum(leq(x,y) for x,y in product(Y,repeat=2)),sep='')
    print('downset_sizes=',{a:len(beta(a)) for a in A},' nonunit_max_tight=True',sep='')
    print('Rees_source_size=12 idempotents=',len(E_S),' actual_actor_classes=',len(set(map(actor,S))),sep='')
    print('PASS full finite equivalence/preorder, action, base injection, all Rees contexts and host law')
    print('CONTROL omitting nontrivial group shift fails tightness as intended')
    print('LIMIT: one finite inverse monoid; infinite quotient/well-definedness are proved separately')


if __name__=='__main__':main()
