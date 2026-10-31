#!/usr/bin/env python3
"""Independently transcribed source, exact Q(sqrt(-15)) integer-scaled Gram replay."""
import collections,datetime,hashlib,itertools,json
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
S=[
 ['1','1','1','1','1','1','1','1','1','1'],
 ['1','c','e','e','b','c','d','1','c','c'],
 ['1','e','e','c','c','1','d','c','b','c'],
 ['1','e','d','e','c','c','b','c','c','1'],
 ['1','c','c','b','1','1','B','C','C','1'],
 ['1','1','c','c','1','B','b','1','C','C'],
 ['1','c','1','c','1','C','b','C','1','B'],
 ['1','d','b','d','B','b','c','b','B','b'],
 ['1','c','c','1','C','1','b','B','1','C'],
 ['1','b','c','c','C','C','B','1','1','1']]
exp={'1':0,'b':1,'c':2,'d':3,'e':4,'B':-1,'C':-2};E=[[exp[x]for x in row]for row in S]
def mul(x,y):return(x[0]*y[0]-15*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def power(k):
 x=(Q(1),Q(0));b=(Q(-1,4),Q(-1,4)if k>=0 else Q(1,4))
 for _ in range(abs(k)):x=mul(x,b)
 return x
def integer(k):
 a,b=power(k);assert (256*a).denominator==(256*b).denominator==1;return (int(256*a),int(256*b))
K=[[integer(x)for x in row]for row in E]
def conj(x):return(x[0],-x[1])
def sm(v):return(sum(x[0]for x in v),sum(x[1]for x in v))
for row in K:
 for x in row:assert mul(conj(x),x)==(65536,0)
for i,j in itertools.combinations(range(10),2):
 assert sm(mul(conj(K[t][i]),K[t][j])for t in range(10))==(0,0)
 assert sm(mul(conj(K[i][t]),K[j][t])for t in range(10))==(0,0)
rowpairs=[];colpairs=[];nonconstant=0
for i,j in itertools.combinations(range(10),2):
 a=[E[j][t]-E[i][t]for t in range(10)];b=[E[t][j]-E[t][i]for t in range(10)];assert len(set(b))>1;nonconstant+=1
 if sorted(collections.Counter(a).values())==[5,5]:rowpairs.append([i,j])
 if sorted(collections.Counter(b).values())==[5,5]:colpairs.append([i,j])
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'norms':100,'column_grams':45,'row_grams':45,'nonconstant_column_ratio_exponent_pairs':nonconstant,
 'row_5plus5_pairs':rowpairs,'col_5plus5_pairs':colpairs,'exponent_matrix':E,'status':'PASS'}
(P/'frontier-20261028-n10-qminus15-isolated-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='exponent_matrix'},indent=2))
