#!/usr/bin/env python3
"""Exact fixed-pair Hankel 4x8 source link gap.

Named public inspiration: Johnston-Lovitz arXiv:2609.11849v1,
https://arxiv.org/html/2609.11849v1. No held episode is used.
Integer/Fraction matrix checks do not constitute formal verification.
"""
from fractions import Fraction as F
from math import comb
import json

V=[[2,0,-2,-2,-1,-2,-1,-1],
   [2,-1,1,-2,2,1,2,0],
   [-2,1,0,-1,-1,1,1,2],
   [0,2,-3,-2,-2,2,-2,1]]
m,n=4,8;N=m*n;Nlink=n*n
h=[[int(i//n+i%n==r) for i in range(N)] for r in range(m+n-1)]
counts=[sum(v) for v in h]
v=[F(V[i][j]) for i in range(m) for j in range(n)]
PL=[[sum(F(e[i]*e[j],c) for e,c in zip(h,counts)) for j in range(N)] for i in range(N)]
vp=[v[i]-sum(PL[i][j]*v[j] for j in range(N)) for i in range(N)]
beta=sum(x*x for x in vp)
assert beta==F(337,6)
P=[[F(i==j)-PL[i][j]-vp[i]*vp[j]/beta for j in range(N)] for i in range(N)]
L=[[F(0) for _ in range(Nlink)] for _ in range(Nlink)]
for r,e in enumerate(h):
    nz=[(i//n,i%n) for i,x in enumerate(e) if x]
    weight=F(1,comb(10,r))
    for i,q in nz:
        for j,s in nz:
            for p in range(n):
                for t in range(n):
                    L[p*n+q][t*n+s]+=weight*P[i*n+p][j*n+t]
u=[F(i//n==i%n) for i in range(Nlink)]
assert all(sum(L[i][j]*u[j] for j in range(Nlink))==0 for i in range(Nlink))
gap=F(1,10**12)
G=[[L[i][j]-gap*(F(i==j)-u[i]*u[j]/n) for j in range(Nlink)] for i in range(Nlink)]
def psd_rank(a):
    a=[r[:] for r in a];rank=0
    while a:
        if any(a[i][i]<0 for i in range(len(a))):return None
        p=next((i for i in range(len(a)) if a[i][i]>0),None)
        if p is None:return rank if all(x==0 for row in a for x in row) else None
        pivot=a[p][p];idx=[i for i in range(len(a)) if i!=p]
        a=[[a[i][j]-a[i][p]*a[p][j]/pivot for j in idx] for i in idx];rank+=1
    return rank
rank=psd_rank(G)
assert rank==63
M=16*25**4;delta=F(1,2*(M+1)**2);K=2041200
rank7_margin=K*gap/16-F(81,2)*delta
rank4_margin=K*gap/4-F(81,2)*delta
assert rank7_margin>0 and rank4_margin>0
print(json.dumps({
    'link_dimension':Nlink,
    'scalar_identity_null':True,
    'exact_PSD_rank_after_gap_subtraction':rank,
    'gap':'1/1000000000000',
    'all_singular_filter_margin':str(rank7_margin),
    'rank_at_most_four_margin':str(rank4_margin),
    'scope':'The global inequalities also use the written rank-two witness proof and exact separable integral; no claim about other pairs or the 4x4 target.'
},indent=2))
