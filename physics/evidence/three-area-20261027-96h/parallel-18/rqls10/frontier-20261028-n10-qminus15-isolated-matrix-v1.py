#!/usr/bin/env python3
"""Exact literal Y_10_0_9A matrix checks in Q(b), 2b²+b+2=0."""
import collections,datetime,hashlib,itertools,json
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
E=[[0,0,0,0,0,0,0,0,0,0],[0,2,4,4,1,2,3,0,2,2],[0,4,4,2,2,0,3,2,1,2],[0,4,3,4,2,2,1,2,2,0],[0,2,2,1,0,0,-1,-2,-2,0],[0,0,2,2,0,-1,1,0,-2,-2],[0,2,0,2,0,-2,1,-2,0,-1],[0,3,1,3,-1,1,2,1,-1,1],[0,2,2,0,-2,0,1,-1,0,-2],[0,1,2,2,-2,-2,-1,0,0,0]]
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]/2)
def power(k):
 x=(Q(1),Q(0));base=(Q(0),Q(1)) if k>=0 else (Q(-1,2),Q(-1))
 for _ in range(abs(k)):x=mul(x,base)
 return x
def sumv(v):return(sum(x[0]for x in v),sum(x[1]for x in v))
for k in range(-4,5):assert mul(power(k),power(-k))==(1,0)
for i,j in itertools.combinations(range(10),2):
 assert sumv(power(E[t][j]-E[t][i])for t in range(10))==(0,0)
 assert sumv(power(E[j][t]-E[i][t])for t in range(10))==(0,0)
R=[];C=[]
for i,j in itertools.combinations(range(10),2):
 if sorted(collections.Counter(E[j][t]-E[i][t]for t in range(10)).values())==[5,5]:R.append([i,j])
 if sorted(collections.Counter(E[t][j]-E[t][i]for t in range(10)).values())==[5,5]:C.append([i,j])
obj={'source':'https://github.com/matrix-toolbox/chm/blob/main/CHM_SINKHORN/Y_10_0_9A.m',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'minimal_polynomial':'2b^2+b+2=0','column_gram_pairs':45,'row_gram_pairs':45,'norm_powers_checked':9,
 'row_5plus5_pairs':R,'col_5plus5_pairs':C,'exponent_matrix':E,'status':'PASS'}
(P/'frontier-20261028-n10-qminus15-isolated-matrix-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
