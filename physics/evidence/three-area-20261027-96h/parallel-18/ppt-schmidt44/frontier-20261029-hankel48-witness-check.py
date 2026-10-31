#!/usr/bin/env python3
"""Exact new 4x8 PPT source and 2-block-positive witness arithmetic.

Named public inspiration: Johnston-Lovitz, arXiv:2609.11849v1,
https://arxiv.org/html/2609.11849v1. The concrete rational construction
and its Pluecker-distance proof are given in the accompanying packet.
This script is exact arithmetic, not formal proof-assistant verification.
"""
from fractions import Fraction as F
from math import comb, lcm
import json

V=[[2,0,-2,-2,-1,-2,-1,-1],
   [2,-1,1,-2,2,1,2,0],
   [-2,1,0,-1,-1,1,1,2],
   [0,2,-3,-2,-2,2,-2,1]]
m,n=4,8;N=m*n
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
C=[[V[j][t+i]-V[i][t+j] for i,j in pairs] for t in range(5)]
pstar=[1,0,0,0,0,1]
assert all(sum(x*y for x,y in zip(row,pstar))==0 for row in C)
assert pstar[0]*pstar[5]-pstar[1]*pstar[4]+pstar[2]*pstar[3]==1

def det(A):
    a=[[F(x) for x in row] for row in A];n=len(a);out=F(1)
    for i in range(n):
        p=next((j for j in range(i,n) if a[j][i]),None)
        if p is None:return F(0)
        if p!=i:a[i],a[p]=a[p],a[i];out=-out
        pivot=a[i][i];out*=pivot
        for j in range(i+1,n):
            q=a[j][i]/pivot
            for k in range(i+1,n):a[j][k]-=q*a[i][k]
            a[j][i]=0
    return out
minor=det([row[:5] for row in C])
assert minor==174 and max(abs(x) for row in C for x in row)<=5
H=[[int(i//n+i%n==r) for i in range(N)] for r in range(m+n-1)]
counts=[sum(h) for h in H]
assert counts==[1,2,3,4,4,4,4,4,3,2,1]
flat=[F(V[i][j]) for i in range(m) for j in range(n)]
assert sum(x*x for x in flat)==81
PL=[[sum(F(h[i]*h[j],c) for h,c in zip(H,counts)) for j in range(N)] for i in range(N)]
vp=[flat[i]-sum(PL[i][j]*flat[j] for j in range(N)) for i in range(N)]
beta=sum(x*x for x in vp)
assert beta==F(337,6)
PK=[[F(i==j)-PL[i][j]-vp[i]*vp[j]/beta for j in range(N)] for i in range(N)]
assert lcm(*(x.denominator for row in PK for x in row))==8088
avec=[F(0)]*N;avec[1*n+0]=F(1,2);avec[0*n+1]=F(-1,2)
assert sum(x*y for x,y in zip(avec,flat))==1
assert all(sum(x*y for x,y in zip(avec,h))==0 for h in H)
M=16*25**4;delta=F(1,2*(M+1)**2)
W=[[PK[i][j]-delta*avec[i]*avec[j] for j in range(N)] for i in range(N)]
assert M==6250000 and delta*(M+1)**2==F(1,2)
assert all(sum(F(h[i])*W[i][j]*F(h[j]) for i in range(N) for j in range(N))==0 for h in H)
assert sum(flat[i]*W[i][j]*flat[j] for i in range(N) for j in range(N))==-delta
Sig=[[sum(F(h[i]*h[j],comb(10,r)) for r,h in enumerate(H)) for j in range(N)] for i in range(N)]
PT=[[Sig[(i//n)*n+j%n][(j//n)*n+i%n] for j in range(N)] for i in range(N)]
A=[[PT[i][j]-F(i==j,12600) for j in range(N)] for i in range(N)]
def psd_rank(a):
    a=[r[:] for r in a];rank=0
    while a:
        if any(a[i][i]<0 for i in range(len(a))):return None
        p=next((i for i in range(len(a)) if a[i][i]>0),None)
        if p is None:return rank if all(x==0 for row in a for x in row) else None
        pivot=a[p][p];idx=[i for i in range(len(a)) if i!=p]
        a=[[a[i][j]-a[i][p]*a[p][j]/pivot for j in idx] for i in idx];rank+=1
    return rank
assert psd_rank(A)==32
assert 2041200*F(1,12600)-81==81
print(json.dumps({
    'pluecker_compatibility_matrix':C,
    'five_by_five_minor':str(minor),
    'kernel_generator_pfaffian':1,
    'projected_V_norm_squared':str(beta),
    'projector_common_denominator':8088,
    'sigma_partial_transpose_minus_I_over_12600_psd_rank':32,
    'V_norm_squared':81,
    'rho_formula':'2041200 * sigma + [V]',
    'rho_PT_written_lower_bound':'81 I',
    'witness_delta':str(delta),
    'witness_source_pairing':str(-delta),
    'scope':'Exact arithmetic checks the finite identities and PPT bound; rank-two positivity relies on the written all-variable Pluecker-distance argument. No 4x4 filter result or formal verification.'
},indent=2))
