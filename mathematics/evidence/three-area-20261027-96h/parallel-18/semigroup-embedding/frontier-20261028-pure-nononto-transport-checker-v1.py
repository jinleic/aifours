#!/usr/bin/env python3
"""Direct whole-host check: pure nononto CS map with collapsed rows/columns."""
from itertools import permutations,product
G=tuple(permutations(range(3)));ix={g:i for i,g in enumerate(G)};e=ix[(0,1,2)]
def compose(g,h):return tuple(g[h[x]] for x in range(3))
M=tuple(tuple(ix[compose(g,h)] for h in G) for g in G)
inv=tuple(next(h for h in range(6) if M[g][h]==e==M[h][g]) for g in range(6))
u=ix[(1,0,2)];v=ix[(0,2,1)];H=(e,u);assert M[M[v][u]][inv[v]] not in H
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4));sig=(0,3,4,1,2)
def bm(a,b):return B[a][b]
def ha(bit,b):return sig[b] if bit else b
unseen=set(range(6));decomp={}
while unseen:
 r=min(unseen)
 for bit,h in enumerate(H):
  x=M[r][h];assert x not in decomp;decomp[x]=(r,bit);unseen.remove(x)
def emb(b):return tuple(ha(decomp[g][1],b) for g in range(6))
def gamma(g,F):return tuple(F[M[x][g]] for x in range(6))
def point(F,H0):return tuple(bm(a,b) for a,b in zip(F,H0))
assert all(emb(bm(a,b))==point(emb(a),emb(b)) for a,b in product(range(5),repeat=2))
assert all(gamma(h,emb(b))==emb(ha(bit,b)) for bit,h in enumerate(H) for b in range(5))
rowmap=(0,1,1);colmap=(0,1,1);row=(e,v,v);col=(e,M[u][v],M[u][v])
Q1=((0,0),(0,1));Q=tuple(tuple(Q1[colmap[l]][rowmap[i]] for i in range(3)) for l in range(3))
R=(e,v);C=(e,M[u][v]);P=tuple(tuple(M[M[inv[C[l]]][H[Q1[l][i]]]][inv[R[i]]] for i in range(2)) for l in range(2))
D0=tuple(product(range(3),range(2),range(3)))
def dm(a,b):return(a[0],a[1]^Q[a[2]][b[0]]^b[1],b[2])
def f(a):return(rowmap[a[0]],M[M[row[a[0]]][H[a[1]]]][col[a[2]]],colmap[a[2]])
def dn(a,b):return(a[0],M[M[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
assert len({f(a) for a in D0})<len(D0) and len({f(a) for a in D0})<24
assert all(f(dm(a,b))==dn(f(a),f(b)) for a,b in product(D0,repeat=2))
assert all((dm(a,a)==a)==(dn(f(a),f(a))==f(a)) for a in D0)
S=tuple(product(range(5),range(3),range(2),range(3)))
def sm(a,b):
 w=a[2]^Q[a[3]][b[1]]
 return(bm(a[0],ha(w,b[0])),a[1],w^b[2],b[3])
def psi(a):return((a[1],a[3]),gamma(row[a[1]],emb(a[0])),f((a[1],a[2],a[3])))
def outprod(a,b):
 rect=(a[0][0],b[0][1]);d,e0=a[2],b[2];w=M[d[1]][P[d[2]][e0[0]]]
 return(rect,point(a[1],gamma(w,b[1])),dn(d,e0))
for a,b in product(S,repeat=2):
 assert psi(sm(a,b))==outprod(psi(a),psi(b))
 assert a==b or psi(a)!=psi(b)
x=(0,1,0,1);y=(0,2,0,1)
assert x!=y and psi(x)[1:]==psi(y)[1:] and psi(x)[0]!=psi(y)[0]
print('pure map D0=',len(D0),' image=',len({f(a) for a in D0}),' target=24; group C2→S3 nonnormal; rows/cols collapse',sep='')
print('PASS entire90-element physical host, all8100 products and injection with rectangle')
print('CONTROL removing rectangle identifies two distinct source elements')
print('LIMIT finite same-author sample; arbitrary pure-CS transport is symbolic')
