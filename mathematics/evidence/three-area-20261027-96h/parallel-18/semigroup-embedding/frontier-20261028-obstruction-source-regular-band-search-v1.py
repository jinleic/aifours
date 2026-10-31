#!/usr/bin/env python3
"""Bounded exact finite band-host synthesis for the displayed 45-source.

A SAT result is rechecked directly against all source products. UNSAT means
only the selected band order/action class; UNKNOWN proves nothing. Three source
generators are checked to generate all 45 elements before transition reduction.
"""
from itertools import product
import sys
import z3

A=range(5)
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,4),(4,4,3))
th=(0,1,0,1,0)
S=tuple(product(range(3),A,range(3)))
ix={s:i for i,s in enumerate(S)}
def mul(s,t):
    return (s[0],T[T[s[1]][P[s[2]][t[0]]]][t[1]],t[2])
def actor(s):
    return (s[0],th[s[1]],s[2])
def weight(s,t):
    return (th[s[1]]+th[P[s[2]][t[0]]])%2
G=((2,4,2),(1,4,1),(0,4,0))
closed=set(G)
while True:
    enlarged=closed|{mul(a,b) for a,b in product(closed,repeat=2)}
    if enlarged==closed:break
    closed=enlarged
assert closed==set(S)


def search(n,pairs,ms):
    invol=list(range(n))
    for k in range(pairs):
        invol[2*k],invol[2*k+1]=2*k+1,2*k
    def act(z):
        out=z3.IntVal(invol[-1])
        for k in range(n-2,-1,-1):out=z3.If(z==k,invol[k],out)
        return out
    m=z3.Function('m_%d_%d'%(n,pairs),z3.IntSort(),z3.IntSort(),z3.IntSort())
    b=[z3.Int('b_%d_%d_%d'%(n,pairs,i)) for i in range(len(S))]
    sol=z3.Solver();sol.set(timeout=ms)
    for v in b:sol.add(v>=0,v<n)
    for i,j in product(range(n),repeat=2):
        sol.add(m(i,j)>=0,m(i,j)<n)
        sol.add(act(m(i,j))==m(invol[i],invol[j]))
    for i in range(n):sol.add(m(i,i)==i)
    for i,j,k in product(range(n),repeat=3):
        sol.add(m(m(i,j),k)==m(i,m(j,k)))
        sol.add(m(m(m(m(i,j),i),k),i)==m(m(m(i,j),k),i))
    for s in S:
        for t in G:
            bt=b[ix[t]]
            sol.add(m(b[ix[s]],act(bt) if weight(s,t) else bt)==b[ix[mul(s,t)]])
    fibers={}
    for s in S:fibers.setdefault(actor(s),[]).append(b[ix[s]])
    for fiber in fibers.values():sol.add(z3.Distinct(*fiber))
    verdict=sol.check()
    print('n=%d involution_pairs=%d verdict=%s'%(n,pairs,verdict),flush=True)
    if verdict!=z3.sat:return False
    model=sol.model()
    mt=tuple(tuple(model.eval(m(i,j)).as_long() for j in range(n)) for i in range(n))
    bs=tuple(model.eval(v).as_long() for v in b)
    for a,c,d in product(range(n),repeat=3):
        assert mt[mt[a][c]][d]==mt[a][mt[c][d]]
        assert mt[mt[mt[mt[a][c]][a]][d]][a]==mt[mt[mt[a][c]][d]][a]
    for a,c in product(range(n),repeat=2):assert invol[mt[a][c]]==mt[invol[a]][invol[c]]
    for a in range(n):assert mt[a][a]==a
    for s,t in product(S,repeat=2):
        v=bs[ix[t]]
        assert bs[ix[mul(s,t)]]==mt[bs[ix[s]]][invol[v] if weight(s,t) else v]
    for s,t in product(S,repeat=2):
        assert actor(s)!=actor(t) or s==t or bs[ix[s]]!=bs[ix[t]]
    print('SAT_EXACT_RECHECK table=',mt,' involution=',invol,' coefficients=',bs,sep='',flush=True)
    return True

if __name__=='__main__':
    lo=int(sys.argv[1]);hi=int(sys.argv[2]);ms=int(sys.argv[3])
    print('45-element source, three verified generators; exact regular-band search',flush=True)
    for n in range(lo,hi+1):
        for pairs in range(n//2+1):
            if search(n,pairs,ms):sys.exit(0)
    print('NO_WITNESS_IN_CONCLUDED_CASES; UNKNOWN cases are not negative results',flush=True)
