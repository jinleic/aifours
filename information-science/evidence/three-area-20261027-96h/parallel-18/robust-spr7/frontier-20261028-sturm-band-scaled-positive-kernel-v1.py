# Exact rational rescaling of numerator coordinates and each frequency row.
# This avoids artificial coefficient-scale imbalance. Grid positivity alone
# is not an all-frequency theorem.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from collections import deque
import json,z3
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def corners(lo,hi):
 ret=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  ret.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[Q(1)])
 return ret
def poly_mul(A,B):
 z=[Q(0)]*(len(A)+len(B)-1)
 for i,x in enumerate(A):
  for j,y in enumerate(B):z[i+j]+=x*y
 return z
def pair(a,b):
 ea=[a[0],-a[2],a[4],-a[6]];oa=[a[1],-a[3],a[5],-a[7]];eb=[b[0],-b[2],b[4],-b[6]];ob=[b[1],-b[3],b[5],-b[7]]
 z=poly_mul(ea,eb)+[Q(0)]
 for i,x in enumerate(poly_mul(oa,ob)):z[i+1]+=x
 return z
def full_row(a,t):
 e=a[0]-a[2]*t+a[4]*t*t-a[6]*t**3;o=a[1]-a[3]*t+a[5]*t*t-t**3
 return [e*(-t)**(j//2) if j%2==0 else t*o*(-t)**((j-1)//2) for j in range(8)]
def half(beta):
 tab=[beta]
 while len(tab[-1])>1:tab.append([(x+y)/2 for x,y in zip(tab[-1],tab[-1][1:])])
 return [x[0] for x in tab],[x[-1] for x in tab[::-1]]
def sign_halfline(poly):
 n=len(poly)-1;queue=deque([(Q(0),Q(1),[poly[j]/comb(n,j) for j in range(n+1)],0)]);leaves=[];nodes=0
 while queue:
  a,b,v,depth=queue.popleft();nodes+=1
  if all(x>0 for x in v):leaves.append({'left':str(a),'right':str(b),'coefficients':list(map(str,v))});continue
  for x,y in ((a,v[0]),(b,v[-1])):
   if y<0:return {'status':'NEGATIVE','t':str(x/(1-x)) if x<1 else 'infinity','nodes':nodes}
  if depth>=65 or nodes>=16000:return {'status':'INCONCLUSIVE','nodes':nodes}
  L,R=half(v);m=(a+b)/2;queue.append((a,m,L,depth+1));queue.append((m,b,R,depth+1))
 return {'status':'STRICT_POSITIVITY','leaves':leaves,'nodes':nodes}
def solve(case):
 src=root/('frontier-20261028-sturm-band-strict-certificate-case-%02d-v1.json'%case);raw=src.read_bytes();f=json.loads(raw)
 lo=list(map(Q,f['lower']));hi=list(map(Q,f['upper']));cs=corners(lo,hi);C=[(lo[j]+hi[j])/2 for j in range(7)]+[Q(1)]
 base=sorted(Q(t) for band in f['bands'] for t in band['nodes']);freq=set(base+[base[0]/2,base[-1]*2]);freq.update((a+b)/2 for a,b in zip(base,base[1:]))
 Y=[z3.Real('sy_'+str(case)+'_'+str(j)) for j in range(8)];s=z3.Solver();s.set(timeout=10000);s.add(*(y>=1 for y in Y));added=set()
 def add(ci,t):
  if (ci,t) in added:return
  row=[C[j]*v for j,v in enumerate(full_row(cs[ci],t))];scale=max(abs(v) for v in row)
  if not scale:raise ValueError('ZERO_ROW')
  row=[v/scale for v in row];s.add(sum(Y[j]*z3.Q(v.numerator,v.denominator) for j,v in enumerate(row))>=1);added.add((ci,t))
 for ci in range(4):
  for t in freq:add(ci,t)
 history=[]
 for step in range(15):
  st=s.check()
  if st!=z3.sat:return {'case':case,'status':'SOLVER_'+str(st),'history':history,'source_sha256':sha256(raw).hexdigest()}
  m=s.model();y=[]
  for z in Y:
   v=m.eval(z,model_completion=True);y.append(Q(v.numerator_as_long(),v.denominator_as_long()))
  b=[C[j]*y[j] for j in range(8)];b=[x/b[7] for x in b];bad=[];proof=[]
  for ci,a in enumerate(cs):
   p=pair(a,b);ch=sign_halfline(p);proof.append(ch)
   if ch['status']=='NEGATIVE' and ch['t']!='infinity':bad.append((ci,Q(ch['t'])))
   elif ch['status']!='STRICT_POSITIVITY':bad.append((ci,None))
  if not bad:return {'case':case,'status':'COMMON_NUMERATOR_PROVED','b':list(map(str,b)),'proofs':proof,'history':history,'source_sha256':sha256(raw).hexdigest()}
  if any(t is None for ci,t in bad):return {'case':case,'status':'CHECK_INCONCLUSIVE','history':history,'source_sha256':sha256(raw).hexdigest()}
  history.append([[ci,str(t)] for ci,t in bad])
  for ci,t in bad:add(ci,t)
 return {'case':case,'status':'EXCHANGE_CAP','history':history,'source_sha256':sha256(raw).hexdigest()}
result=solve(0);p=root/'frontier-20261028-sturm-band-scaled-positive-case-00-v1.json';text=json.dumps(result,indent=2,sort_keys=True)+'\n';p.write_text(text)
print('scaled-positive case',result['status'],'steps',len(result.get('history',[])),'sha256',sha256(text.encode()).hexdigest())
