#!/usr/bin/env python3
"""Exact concrete quotient/retained-rectangle tests, independent of author replay."""
from itertools import product, permutations

def examine(G,one,mul,Q,rows,cols,ri,cl):
    D=list(product(rows,G,cols)); pos={a:i for i,a in enumerate(D)}
    def op(x,y): return (x[0],mul(mul(x[1],Q[x[2]][y[0]]),y[1]),y[2])
    T=[[pos[op(x,y)] for y in D] for x in D]; E=[T[i][i]==i for i in range(len(D))]
    signatures=[]
    for i in range(len(D)):
        sig=bytearray()
        for a in range(-1,len(D)):
            x=i if a==-1 else T[a][i]
            sig.append(E[x]); sig.extend(E[T[x][b]] for b in range(len(D)))
        signatures.append(bytes(sig))
    def q(x): return (ri[x[0]],x[1],cl[x[2]])
    assert all((signatures[i]==signatures[j])==(q(D[i])==q(D[j])) for i in range(len(D)) for j in range(len(D)))
    representatives={}
    for x in D: representatives.setdefault(q(x),x)
    for x,y in product(D,repeat=2):
        qx,qy=q(x),q(y); xr,yr=representatives[qx],representatives[qy]
        # Quotient sandwich and its action weight must not depend on representatives.
        assert Q[x[2]][y[0]]==Q[xr[2]][yr[0]]
        assert q(op(x,y))==q(op(xr,yr))
        assert mul(x[1],Q[x[2]][y[0]])==mul(xr[1],Q[xr[2]][yr[0]])
        # The retained source rectangle and q together recover the natural actor.
        if qx==qy and (x[0],x[2])==(y[0],y[2]): assert x==y
    print(f'natural={len(D)} actual={len(representatives)} checked_actor_pairs={len(D)**2} direct_contexts={len(D)*(len(D)+1)**2}; quotient homomorphism, retained rectangle and weights PASS')

print('five-base:')
examine((0,1),0,lambda x,y:(x+y)%2,((0,0,0),(0,1,1),(0,1,1)),range(3),range(3),(0,1,1),(0,1,1))
print('rectangular S3:')
G=tuple(permutations(range(3))); e=(0,1,2); q=(1,2,0)
def compose(g,h): return tuple(g[h[k]] for k in range(3))
examine(G,e,compose,((e,e,e),(q,q,e)),range(3),range(2),(0,0,1),(0,1))
print('LIMIT: these are only the two concrete quotient actors, not the general pushforward or canonical universal map')
