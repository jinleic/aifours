#!/usr/bin/env python3
"""Exact exhaustive τ-product check on two nonunital regular sources.

The first factor is a 2x2 rectangular group over C2; the second is an
18-element nonorthodox Rees semigroup. No external code, network or writes.
"""
from itertools import product


def require(ok, label):
    if not ok:
        raise ValueError(label)


def main():
    A = list(product(range(2), range(2), range(2)))
    C = list(product(range(3), range(2), range(3)))
    P = ((0,0,0),(0,0,0),(0,0,1))
    S = list(product(A,C))

    def am(a,b):
        return (a[0],(a[1]+b[1])%2,b[2])
    def cm(a,b):
        return (a[0],(a[1]+P[a[2]][b[0]]+b[1])%2,b[2])
    def sm(a,b):
        return (am(a[0],b[0]),cm(a[1],b[1]))
    def ae(a):
        return am(a,a)==a
    def ce(a):
        return cm(a,a)==a
    def se(a):
        return ae(a[0]) and ce(a[1])
    def theta(a):
        return a[1]
    def cq(c):
        return (int(c[0]==2),c[1],int(c[2]==2))
    def actor(s):
        return (theta(s[0]),cq(s[1]))
    def context(mul,idem,x,a,y):
        z = a if x is None else mul(x,a)
        z = z if y is None else mul(z,y)
        return idem(z)

    require(not any(all(am(e,a)==a==am(a,e) for a in A) for e in A if ae(e)),
            'A unexpectedly unital')
    require(not any(all(cm(e,a)==a==cm(a,e) for a in C) for e in C if ce(e)),
            'C unexpectedly unital')
    require(all((theta(a)==0)==ae(a) for a in A), 'A actor purity')
    require(all(theta(am(a,b))==(theta(a)+theta(b))%2 for a,b in product(A,repeat=2)),
            'A actor multiplication')
    require(all((cq(cm(a,a))==cq(a))==ce(a) for a in C), 'C actor purity')

    def signatures(items,mul,idem):
        ctx = [None]+items
        return {a:bytes(context(mul,idem,x,a,y) for x,y in product(ctx,repeat=2)) for a in items}
    sigA = signatures(A,am,ae)
    sigC = signatures(C,cm,ce)
    require(all((sigA[a]==sigA[b])==(theta(a)==theta(b)) for a,b in product(A,repeat=2)),
            'A actual tau')
    require(all((sigC[a]==sigC[b])==(cq(a)==cq(b)) for a,b in product(C,repeat=2)),
            'C actual tau')
    sigS = signatures(S,sm,se)
    require(all((sigS[a]==sigS[b])==(actor(a)==actor(b)) for a,b in product(S,repeat=2)),
            'product actual tau')

    def beta(s):
        a,c=s
        return (a[0],a[2],c[0],c[2])
    def bandmul(x,y):
        return (x[0],y[1],x[2],y[3])
    require(all(beta(sm(a,b))==bandmul(beta(a),beta(b)) for a,b in product(S,repeat=2)),
            'product band homomorphism')
    require(len({(beta(s),actor(s)) for s in S})==len(S), 'physical host injectivity')
    E = [s for s in S if se(s)]
    same_q = [(a,b) for a,b in product(E,repeat=2) if a!=b and actor(a)==actor(b)]
    r = [(a,b) for a,b in same_q if sm(a,b)==b and sm(b,a)==a]
    l = [(a,b) for a,b in same_q if sm(a,b)==a and sm(b,a)==b]
    require(r and l, 'missing R/L pairs')
    require(all(beta(a)!=beta(b) for a,b in r+l), 'R/L separation')
    require(any(not se(sm(a,b)) for a,b in product(E,repeat=2)), 'expected E nonclosure')
    # Collapse a factor coordinate while retaining a band homomorphism.
    def broken(s):
        a,c=s
        return (0,a[2],c[0],c[2])
    require(all(broken(sm(a,b))==bandmul(broken(a),broken(b)) for a,b in product(S,repeat=2)),
            'broken-map homomorphism')
    require(len({(broken(s),actor(s)) for s in S})<len(S), 'broken-map injectivity control')
    print('factor_sizes=',len(A),'x',len(C),' product=',len(S),' product_contexts=',(len(S)+1)**2,sep='')
    print('idempotents=',len(E),' actor_classes=',len({actor(s) for s in S}),sep='')
    print('ordered_same_q_pairs=',len(same_q),' R_pairs=',len(r),' L_pairs=',len(l),sep='')
    print('PASS both nonunital, complete factor/product tau, purity, host map, R/L separation, E nonclosure')
    print('CONTROL homomorphic first-factor row collapse rejected by host injectivity')
    print('SCOPE: one finite 144-element product, not a proof for all regular sources')


if __name__=='__main__':
    main()
