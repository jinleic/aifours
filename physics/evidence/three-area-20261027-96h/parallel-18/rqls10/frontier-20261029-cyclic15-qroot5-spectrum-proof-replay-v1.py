#!/usr/bin/env python3
"""Check 7740 explicit golden-field row/interval witnesses; no elimination."""
import collections,datetime,gzip,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;pr=P/'frontier-20261029-cyclic15-qroot5-spectrum-proof-v1.json.gz';raw=pr.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='d4c2b4ce5bcfbe6dd88eec35bf5da0af49534da1ed2b770639558b693a39b949'
with gzip.open(pr,'rt',encoding='utf8')as f:D=json.load(f)
old=P/'frontier-20261029-cyclic15-qroot5-spectrum-census-v1.json';oldraw=old.read_bytes()
assert hashlib.sha256(oldraw).hexdigest()=='fa4f2fcfa29b8ed7f4daf875eb8d3df5601321cf357977d3120d8ed702451a3f'
z=(F(0),F(0));o=(F(1),F(0))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def div(x,y):
 d=y[0]*y[0]-5*y[1]*y[1];assert d;return mul(x,(y[0]/d,-y[1]/d))
def sign(x):
 a,b=x
 if not b:return(a>0)-(a<0)
 if not a:return(b>0)-(b<0)
 if a>0 and b>0:return 1
 if a<0 and b<0:return -1
 d=a*a-5*b*b;s=(d>0)-(d<0);return s if a>0 else -s
def decode(x):return(F(x[0]),F(x[1]))
def summ(xs):
 q=z
 for x in xs:q=add(q,x)
 return q
# Independently regenerate roots by multiplication by zeta, not the producer's CRT exponent formula.
def oa(x,y):return(add(x[0],y[0]),add(x[1],y[1]))
def on(x):return(neg(x[0]),neg(x[1]))
def om(x,y):
 ac=mul(x[0],y[0]);bd=mul(x[1],y[1]);return(sub(ac,bd),sub(add(mul(x[0],y[1]),mul(x[1],y[0])),bd))
c=(F(-1,2),F(1,2))
def km(x,y):
 ac=om(x[:2],y[:2]);bd=om(x[2:],y[2:]);bc=om(x[2:],y[:2]);ad=om(x[:2],y[2:]);cbd=(mul(c,bd[0]),mul(c,bd[1]));return oa(ac,on(bd))+oa(oa(ad,bc),cbd)
one=(o,z,z,z);zeta=(o,o,neg(c),neg(c));powers=[one]
for _ in range(15):powers.append(km(powers[-1],zeta))
assert powers[15]==one

def system(ex):
 S=sorted(set(ex));mult=[ex.count(a)for a in S];counts=[sum(k for a,k in zip(S,mult)if a%3==r)for r in range(3)]
 A=[[powers[(-2*a)%15][i]for a in S]for i in range(4)];b=[z]*4
 for r in range(3):A.append([o if a%3==r else z for a in S]);b.append((F(counts[r],2)-F(1,3),F(0)))
 return mult,A,b
def rowcomb(comb,A,b):
 L=[decode(x)for x in comb];assert len(L)==7
 return [summ(mul(L[i],A[i][j])for i in range(7))for j in range(len(A[0]))],summ(mul(L[i],b[i])for i in range(7))
def reference(ref,f,A,b,m,desired):
 i=ref['i'];assert 0<=i<len(m) and ref['side'] in ('lower','upper')
 if ref['comb'] is None:assert i==f;point=z;slope=o
 else:
  coeff,point=rowcomb(ref['comb'],A,b);assert i!=f and coeff[i]==o and all(coeff[j]==z for j in range(len(m))if j not in (i,f));slope=neg(coeff[f]);assert slope!=z
 bound=(F(m[i],6),F(0))if ref['side']=='lower'else(F(m[i],2),F(0));sg=sign(slope)
 is_lower=(ref['side']=='lower' and sg>0)or(ref['side']=='upper' and sg<0)
 assert is_lower==(desired=='lower');return div(sub(bound,point),slope)
expected=[]
for rest in itertools.combinations_with_replacement(range(15),5):
 ex=(0,)+rest
 if len({a%3 for a in ex})>=3 and math.gcd(15,*ex)==1:expected.append(ex)
assert len(expected)==len(D['records'])==7740
counts=collections.Counter();survivors=[]
for expected_ex,(ex,cert)in zip(expected,D['records']):
 ex=tuple(ex);assert ex==expected_ex;m,A,b=system(ex);typ=cert['case'];counts[typ]+=1
 if typ=='inconsistent':
  v,t=rowcomb(cert['comb'],A,b);assert all(x==z for x in v)and t!=z
 elif typ=='bound':
  i=cert['i'];v,t=rowcomb(cert['comb'],A,b);assert v==[o if j==i else z for j in range(len(m))]
  if cert['side']=='lower':assert sign(sub(t,(F(m[i],6),F(0))))<0
  else:assert cert['side']=='upper'and sign(sub(t,(F(m[i],2),F(0))))>0
 elif typ=='interval':
  f=cert['free'];assert 0<=f<len(m);lo=reference(cert['lower'],f,A,b,m,'lower');hi=reference(cert['upper'],f,A,b,m,'upper');assert sign(sub(lo,hi))>0
 elif typ=='feasible':
  q=[decode(x)for x in cert['q']];assert len(q)==len(m)
  assert all(summ(mul(x,y)for x,y in zip(row,q))==value for row,value in zip(A,b))
  assert all(sign(sub(x,(F(k,6),F(0))))>=0 and sign(sub((F(k,2),F(0)),x))>=0 for x,k in zip(q,m));survivors.append(ex)
 else:raise AssertionError(typ)
assert survivors==[tuple(x)for x in json.loads(oldraw)['survivors']]
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(raw).hexdigest(),
 'census_sha256':hashlib.sha256(oldraw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'records_checked':len(expected),'certificate_counts':dict(counts),'all_row_equalities_and_bound_witnesses_checked':True,
 'survivor_list_matches':True,'status':'PASS'}
(P/'frontier-20261029-cyclic15-qroot5-spectrum-proof-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
