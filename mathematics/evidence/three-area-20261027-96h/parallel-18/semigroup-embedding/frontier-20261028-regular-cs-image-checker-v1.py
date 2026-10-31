#!/usr/bin/env python3
"""Check Green inheritance on a proper regular CS subsemigroup of a CS actor."""
from itertools import permutations,product
G=tuple(permutations(range(3)));idx={g:i for i,g in enumerate(G)};e=idx[(0,1,2)]
def comp(g,h):return tuple(g[h[x]] for x in range(3))
M=tuple(tuple(idx[comp(g,h)] for h in G) for g in G)
inv=tuple(next(h for h in range(6) if M[g][h]==e==M[h][g]) for g in range(6))
u=idx[(1,0,2)];v=idx[(0,2,1)];H=(e,u);row=(e,v);col=(e,M[u][v]);Q=((0,0),(0,1))
P=tuple(tuple(M[M[inv[col[l]]][H[Q[l][i]]]][inv[row[i]]] for i in range(2)) for l in range(2))
D=tuple(product(range(2),range(6),range(2)))
def dm(a,b):return(a[0],M[M[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
T=tuple((i,M[M[row[i]][H[h]]][col[l]],l) for i,h,l in product(range(2),range(2),range(2)));Tset=set(T)
assert len(T)==8 and len(D)==24 and all(dm(a,b) in Tset for a,b in product(T,repeat=2))
assert all(any(dm(dm(a,b),a)==a and dm(dm(b,a),b)==b for b in T) for a in T)
def Rclasses(X):return {a:frozenset([a]+[dm(a,b) for b in X]) for a in X}
def Lclasses(X):return {a:frozenset([a]+[dm(b,a) for b in X]) for a in X}
rD,lD=Rclasses(D),Lclasses(D);rT,lT=Rclasses(T),Lclasses(T)
assert all((rT[a]==rT[b])==(rD[a]==rD[b]) and (lT[a]==lT[b])==(lD[a]==lD[b]) for a,b in product(T,repeat=2))
assert all(rT[dm(a,b)]==rT[a] and lT[dm(a,b)]==lT[b] for a,b in product(T,repeat=2))
E=[x for x in T if dm(x,x)==x]
assert all(not(dm(a,b)==a==dm(b,a)) or a==b for a,b in product(E,repeat=2))
print('ambient CS=',len(D),' proper regular actor image=',len(T),' idempotents=',len(E),sep='')
print('PASS all Green R/L inheritance comparisons and xy R x, xy L y')
print('PASS actor image regular and idempotents primitive; general proof is symbolic')
print('LIMIT infinite nonregular subsemigroup example requires the separate written argument')
