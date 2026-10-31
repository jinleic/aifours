#!/usr/bin/env python3
"""Exact Q(sqrt5) spectral-population census for a 15-circulant unitary.

q is the sum of the d=2 and d=7 spectral populations aggregated at each
individual eigenvalue. This checks necessary paired moments and U^5 sector
sums, plus bounds m/6 <= q <= m/2 at multiplicity m.
"""
import collections,datetime,gzip,hashlib,itertools,json,math
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
# Produce explicit row-combination or interval certificates for each spectrum.
def encode(x):return [str(x[0]),str(x[1])]
def encvec(v):return [encode(x)for x in v]
def make_system(ex):
 S=sorted(set(ex));mult=[ex.count(a)for a in S];counts=[sum(m for a,m in zip(S,mult)if a%3==r)for r in range(3)]
 A=[[roots[a][i]for a in S]for i in range(4)];b=[Z]*4
 for r in range(3):A.append([O if a%3==r else Z for a in S]);b.append((F(counts[r],2)-F(1,3),F(0)))
 return S,mult,A,b
def certify(ex):
 S,m,A,b=make_system(ex);n=len(S);M=[list(r)+[bb]+[O if i==j else Z for j in range(7)]for i,(r,bb)in enumerate(zip(A,b))];row=0;pivs=[]
 for col in range(n):
  k=next((k for k in range(row,7)if M[k][col]!=Z),None)
  if k is None:continue
  M[row],M[k]=M[k],M[row];t=inv(M[row][col]);M[row]=[mul(x,t)for x in M[row]]
  for k in range(7):
   if k!=row and M[k][col]!=Z:
    t=M[k][col];M[k]=[sub(x,mul(t,y))for x,y in zip(M[k],M[row])]
  pivs.append(col);row+=1
  if row==7:break
 for r in M:
  if all(x==Z for x in r[:n])and r[n]!=Z:return {'case':'inconsistent','comb':encvec(r[n+1:])}
 free=[j for j in range(n)if j not in pivs];assert len(free)<=1
 point=[Z]*n;slopes=[Z]*n;comb=[None]*n
 for i,col in enumerate(pivs):point[col]=M[i][n];comb[col]=M[i][n+1:]
 if free:
  f=free[0];slopes[f]=O
  for i,col in enumerate(pivs):slopes[col]=neg(M[i][f])
 low=high=None;lo_ref=hi_ref=None
 for i,(x,v,k)in enumerate(zip(point,slopes,m)):
  lb=(F(k,6),F(0));ub=(F(k,2),F(0));sg=sign(v)
  if not sg:
   if sign(sub(x,lb))<0:return {'case':'bound','i':i,'side':'lower','comb':encvec(comb[i])}
   if sign(sub(ub,x))<0:return {'case':'bound','i':i,'side':'upper','comb':encvec(comb[i])}
   continue
  l=div(sub(lb,x),v);h=div(sub(ub,x),v);ls,hs=('lower','upper')if sg>0 else('upper','lower')
  if sg<0:l,h=h,l
  cr=None if i==f else encvec(comb[i]);L={'i':i,'side':ls,'comb':cr};H={'i':i,'side':hs,'comb':cr}
  if low is None or sign(sub(l,low))>0:low=l;lo_ref=L
  if high is None or sign(sub(h,high))<0:high=h;hi_ref=H
 if low is not None and high is not None and sign(sub(low,high))>0:return {'case':'interval','free':f,'lower':lo_ref,'upper':hi_ref}
 if not free:t=Z
 elif low is None:t=high if high is not None else Z
 elif high is None:t=low
 else:t=div(add(low,high),(F(2),F(0)))
 vals=[add(x,mul(v,t))for x,v in zip(point,slopes)]
 return {'case':'feasible','q':encvec(vals)}
expected=P/'frontier-20261029-cyclic15-qroot5-spectrum-census-v1.json';raw=expected.read_bytes();assert hashlib.sha256(raw).hexdigest()=='fa4f2fcfa29b8ed7f4daf875eb8d3df5601321cf357977d3120d8ed702451a3f';D=json.loads(raw)
records=[];counts=collections.Counter();surv=[]
for rest in itertools.combinations_with_replacement(range(15),5):
 ex=(0,)+rest
 if len({a%3 for a in ex})<3 or math.gcd(15,*ex)!=1:continue
 cert=certify(ex);records.append([list(ex),cert]);counts[cert['case']]+=1
 if cert['case']=='feasible':surv.append(ex)
assert len(records)==7740 and surv==[tuple(x)for x in D['survivors']]
obj={'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'census_sha256':hashlib.sha256(raw).hexdigest(),'records':records}
out=P/'frontier-20261029-cyclic15-qroot5-spectrum-proof-v1.json.gz'
with gzip.open(out,'wt',encoding='utf8')as f:json.dump(obj,f,separators=(',',':'))
summary={'producer_sha256':obj['producer_sha256'],'census_sha256':obj['census_sha256'],'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'records':len(records),'case_counts':dict(counts),'status':'PRODUCED_UNREPLAYED'}
(P/'frontier-20261029-cyclic15-qroot5-spectrum-proof-v1.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
