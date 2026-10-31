#!/usr/bin/env python3
"""Exact nonnormal-H coinduction and finite nonregular subsource controls."""
from itertools import permutations,product
G=tuple(permutations(range(3)));idx={g:i for i,g in enumerate(G)};e=idx[(0,1,2)]
def comp(g,h):return tuple(g[h[x]] for x in range(3))
M=tuple(tuple(idx[comp(g,h)] for h in G) for g in G)
inv=tuple(next(h for h in range(6) if M[g][h]==e==M[h][g]) for g in range(6))
u=idx[(1,0,2)];v=idx[(0,2,1)];H=(e,u);assert M[u][v]!=M[v][u]
assert M[M[v][u]][inv[v]] not in H
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4));sigma=(0,3,4,1,2)
def bm(a,b):return B[a][b]
def bh(h,b):return b if h==e else sigma[b]
assert all(bh(u,bm(a,b))==bm(bh(u,a),bh(u,b)) for a,b in product(range(5),repeat=2))
unseen=set(range(6));decomp={};reps=[]
while unseen:
 r=min(unseen);reps.append(r)
 for h in H:
  x=M[r][h];assert x not in decomp;decomp[x]=(r,h);unseen.remove(x)
assert len(decomp)==6 and e in reps
def embed(b):return tuple(bh(decomp[x][1],b) for x in range(6))
def gamma(g,F):return tuple(F[M[x][g]] for x in range(6))
def point(F,H0):return tuple(bm(x,y) for x,y in zip(F,H0))
for a,b in product(range(5),repeat=2):assert embed(bm(a,b))==point(embed(a),embed(b))
for h,b in product(H,range(5)):assert gamma(h,embed(b))==embed(bh(h,b))
assert len({embed(b) for b in range(5)})==5
wrong=sum(tuple(embed(b)[M[inv[h]][x]] for x in range(6))!=embed(bh(h,b)) for h,b in product(H,range(5)))
assert wrong>0
Q=((0,0),(0,1));ph=(e,u);row=(e,v);col=(e,M[u][v])
P=tuple(tuple(M[M[inv[col[l]]][ph[Q[l][i]]]][inv[row[i]]] for i in range(2)) for l in range(2))
S=tuple(product(range(5),range(2),range(2),range(2))) # band,i,h,lambda

def source(a,b):
 w=a[2]^Q[a[3]][b[1]];c=b[0] if w==0 else sigma[b[0]]
 return(bm(a[0],c),a[1],w^b[2],b[3])
def actor(a):return(a[1],M[M[row[a[1]]][ph[a[2]]]][col[a[3]]],a[3])
def actorprod(a,b):return(a[0],M[M[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def beta(a):return gamma(row[a[1]],embed(a[0]))
for a,b in product(S,repeat=2):
 d=actor(a);e0=actor(b);weight=M[d[1]][P[d[2]][e0[0]]]
 assert actor(source(a,b))==actorprod(d,e0)
 assert beta(source(a,b))==point(beta(a),gamma(weight,beta(b)))
 assert a==b or actor(a)!=actor(b) or beta(a)!=beta(b)
# The original 45-element source contains a finite but nonregular subsemigroup.
A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
R=((4,4,4),(4,1,3),(4,4,1))
def sm(a,b):return(a[0],A[A[a[1]][R[a[2]][b[0]]]][b[1]],b[2])
s=(1,4,1);F={s};
while True:
 n=F|{sm(a,b) for a,b in product(F,repeat=2)}
 if n==F:break
 F=n
assert len(F)==3 and not any(sm(sm(s,t),s)==s for t in F)
print('G=S3, H=C2 nonnormal, left-coset count=',len(reps),' wrong-left-shift failures=',wrong,sep='')
print('PASS coinduced embedding B→B^G, full H-equivariance and band law')
print('PASS nontrivial row/column gauges, all1600 40-source ambient-D products and injection')
print('nonregular finite subsemigroup in original 45-source=',sorted(F),' generator=',s,sep='')
print('LIMIT finite check; compactness and Brown theorems are separate written arguments')
