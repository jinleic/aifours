#!/usr/bin/env python3
"""Exact stationarity plus certified rational positive Hessian; no global claim."""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('near',P/'frontier-20261028-near-hadamard-pair-exact-v1.py')
near=importlib.util.module_from_spec(sp);sp.loader.exec_module(near)
E=near.E

def atan_interval(inv,n):
    x=Q(1,inv);s=sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(n)),Q(0))
    q=(-1)**n*x**(2*n+1)/Q(2*n+1)
    return min(s,s+q),max(s,s+q)
a,b=atan_interval(5,14);c,d=atan_interval(239,5)
pi_lo=16*a-4*d;pi_hi=16*b-4*c
assert 3<pi_lo<pi_hi<4
S=10**12

def round_q(x):return (x+Q(1,2)).numerator//(x+Q(1,2)).denominator
cos_approx=[]
for k in range(20):
    j=min(k,20-k);mid=Q(j,20)*(pi_lo+pi_hi);err=Q(j,20)*(pi_hi-pi_lo)
    total=sum(((-1)**m*mid**(2*m)/factorial(2*m) for m in range(20)),Q(0))
    err+=abs(mid)**40/factorial(40)
    lo=(total-err)*S;hi=(total+err)*S
    lower=round_q(lo);upper=round_q(hi)
    assert lower==upper,(k,lower,upper)
    cos_approx.append(lower)
assert cos_approx[0]==S and cos_approx[5]==0 and cos_approx[10]==-S
# Dephase row0 and column0; all81 remaining phase coordinates.
idx={(t,c):(t-1)*9+(c-1) for t in range(1,10) for c in range(1,10)}
N=len(idx);M=[[0]*N for _ in range(N)];grad=[[0]*20 for _ in range(N)]
for c,d in combinations(range(10),2):
  for t,s in combinations(range(10),2):
    vec={}
    for key,v in (((t,d),1),((t,c),-1),((s,d),-1),((s,c),1)):
        if key in idx:vec[idx[key]]=v
    for shift in (0,1):
        k=(E[t][d]-E[t][c]-E[s][d]+E[s][c]+2*shift*(t-s)*(d-c))%20
        for i,vi in vec.items():
            grad[i][k]+=vi;grad[i][-k%20]-=vi
            for j,vj in vec.items():M[i][j]-=4*cos_approx[k]*vi*vj
# Exact sin coefficients vanish modulo Phi20, so all81 gradients are zero.
assert all(not any(near.rem(p)) for p in grad)
D=100*S
# Prove H_approx - (1/200)I positive by fraction-free symmetric Bareiss.
for i in range(N):M[i][i]-=D//200
prev=1;pivots=[]
for k in range(N-1):
    pivot=M[k][k];assert pivot>0;pivots.append(pivot)
    for i in range(k+1,N):
        for j in range(i,N):
            value=pivot*M[i][j]-M[i][k]*M[k][j]
            assert value%prev==0
            M[i][j]=value//prev;M[j][i]=M[i][j]
    for i in range(k+1,N):M[i][k]=M[k][i]=0
    prev=pivot
assert M[N-1][N-1]>0;pivots.append(M[N-1][N-1])
# At most 18000 full ordered cosine terms, each coefficient bounded by1;
# after /100, each entry differs by <=180/S, hence operator norm <=81*180/S.
assert Q(81*180,S)<Q(1,200)
print('PASS rigorous cos brackets via Machin arctan fractions and alternating Taylor')
print('PASS 81 exact gradient polynomials vanish modulo Phi20')
print('PASS 81 positive Bareiss pivots for Happrox - (1/200)I')
print('entrywise Hessian error <=180/10^12; operator error <=14580/10^12')
print('STRICT LOCAL MINIMUM of full dephased flat-matrix loss; NO GLOBAL CLAIM')
