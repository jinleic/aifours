#!/usr/bin/env python3
"""Exact Q(sqrt5) spectral-population census for a 15-circulant unitary.

q is the sum of the d=2 and d=7 spectral populations aggregated at each
individual eigenvalue. This checks necessary paired moments and U^5 sector
sums, plus bounds m/6 <= q <= m/2 at multiplicity m.
"""
import collections,datetime,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
Z=(F(0),F(0));O=(F(1),F(0))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def inv(x):
 d=x[0]*x[0]-5*x[1]*x[1];assert d;return(x[0]/d,-x[1]/d)
def div(x,y):return mul(x,inv(y))
def sign(x):
 a,b=x
 if not b:return(a>0)-(a<0)
 if not a:return(b>0)-(b<0)
 if a>0 and b>0:return 1
 if a<0 and b<0:return -1
 q=a*a-5*b*b;s=(q>0)-(q<0);return s if a>0 else -s
c=(F(-1,2),F(1,2));eta=[(O,Z)]
for _ in range(4):
 a,b=eta[-1];eta.append((neg(b),add(a,mul(c,b))))
omega=[(O,Z),(Z,O),(neg(O),neg(O))]
def root15(a):
 a0,a1=omega[(2*a)%3];b0,b1=eta[(2*a)%5]
 return(mul(a0,b0),mul(a1,b0),mul(a0,b1),mul(a1,b1))
# Rows are over Q(sqrt5) in basis 1,omega,eta,omega*eta.
roots=[root15((-2*a)%15)for a in range(15)]
def solve(A,b,n):
 M=[list(row)+[value]for row,value in zip(A,b)];row=0;pivs=[]
 for col in range(n):
  k=next((k for k in range(row,len(M))if M[k][col]!=Z),None)
  if k is None:continue
  M[row],M[k]=M[k],M[row];t=inv(M[row][col]);M[row]=[mul(x,t)for x in M[row]]
  for k in range(len(M)):
   if k!=row and M[k][col]!=Z:
    t=M[k][col];M[k]=[sub(x,mul(t,y))for x,y in zip(M[k],M[row])]
  pivs.append(col);row+=1
  if row==len(M):break
 if any(all(x==Z for x in q[:n]) and q[-1]!=Z for q in M):return None
 point=[Z]*n
 for i,col in enumerate(pivs):point[col]=M[i][-1]
 basis=[]
 for j in range(n):
  if j in pivs:continue
  v=[Z]*n;v[j]=O
  for i,col in enumerate(pivs):v[col]=neg(M[i][j])
  basis.append(v)
 return point,basis

def system(ex):
 S=sorted(set(ex));mult=[ex.count(a)for a in S];counts=[sum(m for a,m in zip(S,mult)if a%3==r)for r in range(3)]
 A=[[roots[a][i]for a in S]for i in range(4)];rhs=[Z]*4
 for r in range(3):
  A.append([O if a%3==r else Z for a in S]);rhs.append((F(counts[r],2)-F(1,3),F(0)))
 sol=solve(A,rhs,len(S));return None if sol is None else(S,mult,*sol)
def feasible(sol):
 S,m,point,basis=sol
 assert len(basis)<=1
 if not basis:
  return all(sign(sub(x,(F(k,6),F(0))))>=0 and sign(sub((F(k,2),F(0)),x))>=0 for x,k in zip(point,m))
 low=high=None
 for x,v,k in zip(point,basis[0],m):
  l=(F(k,6),F(0));h=(F(k,2),F(0));sg=sign(v)
  if not sg:
   if sign(sub(x,l))<0 or sign(sub(h,x))<0:return False
   continue
  lo=div(sub(l,x),v);hi=div(sub(h,x),v)
  if sg<0:lo,hi=hi,lo
  if low is None or sign(sub(lo,low))>0:low=lo
  if high is None or sign(sub(hi,high))<0:high=hi
 return low is None or high is None or sign(sub(low,high))<=0
D={2,5,7,8,10,13};units=[u for u in range(1,15)if math.gcd(u,15)==1 and {(u*d)%15 for d in D}==D];assert units==[1,4,11,14]
def canonical(ex):return min(tuple(sorted((u*a+shift)%15 for a in ex))for u in units for shift in range(15))
census=collections.Counter();survivors=[];classes=collections.Counter()
for rest in itertools.combinations_with_replacement(range(15),5):
 ex=(0,)+rest
 if len({a%3 for a in ex})<3 or math.gcd(15,*ex)!=1:continue
 sol=system(ex)
 if sol is None:census['inconsistent']+=1;continue
 census['consistent_dim_'+str(len(sol[3]))]+=1
 if feasible(sol):survivors.append(ex);classes[canonical(ex)]+=1
expected={(0,0,3,5,10,12):5,(0,1,2,4,5,12):12,(0,1,5,6,10,11):2,(0,2,5,7,10,12):2}
assert dict(classes)==expected and len(survivors)==21
# Verify the two non-coset representative q solutions and their needed moment kernel properties.
rep=(0,0,3,5,10,12);S,m,point,free=system(rep);assert not free
qmap=dict(zip(S,point));assert qmap[5]==qmap[10]==(F(1,6),F(0))
A=[[roots[a][i]for a in S]for i in range(4)];_,ker=solve(A,[Z]*4,len(S));assert all(v[S.index(5)]==v[S.index(10)]for v in ker)
rep2=(0,1,2,4,5,12);S2,m2,point2,free2=system(rep2);X=(F(-1,3),F(1,3));Y=(F(1),F(-1,3));assert not free2 and point2==[X,X,Y,Y,X,Y]
# Both two-coset classes: every possible moment-kernel vector is constant on each 3-cycle.
for ex in survivors:
 if canonical(ex) not in ((0,1,5,6,10,11),(0,2,5,7,10,12)):continue
 S=sorted(set(ex));A=[[roots[a][i]for a in S]for i in range(4)];_,ker=solve(A,[Z]*4,len(S));assert len(ker)==2
 for v in ker:
  for a in S:assert v[S.index(a)]==v[S.index((a+5)%15)]
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'normalized_spectra_examined':sum(census.values()),'census':dict(census),'moment_feasible_spectra':len(survivors),
 'survivors':[list(x)for x in survivors],'symmetry_classes':[{'representative':list(k),'count':v}for k,v in sorted(classes.items())],
 'repeated_representative_q5_q10':'1/6','repeated_p2_p7_kernel_forces_equal_5_10':True,
 'simple_representative_q_pattern':'X,X,Y,Y,X,Y','two_3cycle_kernels_uniform':True,'status':'PASS'}
(P/'frontier-20261029-cyclic15-qroot5-spectrum-census-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
