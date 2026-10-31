# Exact rational positive-numerator exchange on the already frozen Sturm-band
# boxes. A finite grid or an exchange cap is not an all-frequency proof.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from collections import deque
from math import comb
import json,z3
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def mul(A,B):
 C=[Q(0)]*(len(A)+len(B)-1)
 for i,x in enumerate(A):
  for j,y in enumerate(B):C[i+j]+=x*y
 return C
def poly_pair(a,b):
 E=lambda p:[p[0],-p[2],p[4],-p[6]];O=lambda p:[p[1],-p[3],p[5],-p[7]]
 z=mul(E(a),E(b))+[Q(0)];v=mul(O(a),O(b))
 for j,x in enumerate(v):z[j+1]+=x
 while len(z)>1 and z[-1]==0:z.pop()
 return z
def half(beta):
 table=[beta]
 while len(table[-1])>1:table.append([(a+b)/2 for a,b in zip(table[-1],table[-1][1:])])
 return [a[0] for a in table],[a[-1] for a in table[::-1]]
def halfline(p):
 n=len(p)-1;work=deque([(Q(0),Q(1),[p[j]/comb(n,j) for j in range(n+1)],0)]);leaves=[];nodes=0
 while work:
  l,r,b,d=work.popleft();nodes+=1
  if all(x>0 for x in b):leaves.append({'left':str(l),'right':str(r),'coefficients':list(map(str,b))});continue
  for x,y in ((l,b[0]),(r,b[-1])):
   if y<0:return {'status':'NEGATIVE','t':str(x/(1-x)) if x<1 else 'infinity','nodes':nodes}
  if d>=65 or nodes>=15000:return {'status':'INCONCLUSIVE','nodes':nodes}
  L,R=half(b);m=(l+r)/2;work.append((l,m,L,d+1));work.append((m,r,R,d+1))
 return {'status':'STRICT_POSITIVITY','nodes':nodes,'leaves':leaves}
def exchange(case):
 src=root/('frontier-20261028-sturm-band-strict-certificate-case-%02d-v1.json'%case);raw=src.read_bytes();f=json.loads(raw)
 if f['status']!='unsat':return {'case':case,'status':'INPUT_NOT_UNSAT'}
 lo=list(map(Q,f['lower']));hi=list(map(Q,f['upper']));cs=corners(lo,hi);base=sorted(Q(t) for b in f['bands'] for t in b['nodes']);freq=set(base+[base[0]/2,base[-1]*2]);freq.update((a+b)/2 for a,b in zip(base,base[1:]))
 B=[z3.Real('positive_'+str(case)+'_'+str(j)) for j in range(8)];s=z3.Solver();s.set(timeout=5000);s.add(sum(B)==1);s.add(*(x>0 for x in B));added=set()
 def add(ci,t):
  if (ci,t) in added:return
  v=row(cs[ci],t);s.add(sum(B[j]*z3.Q(v[j].numerator,v[j].denominator) for j in range(8))>0);added.add((ci,t))
 for ci in range(4):
  for t in freq:add(ci,t)
 history=[]
 for step in range(15):
  st=s.check()
  if st!=z3.sat:return {'case':case,'status':'SOLVER_'+str(st),'history':history,'source_sha256':sha256(raw).hexdigest()}
  m=s.model();b=[]
  for v in B:
   z=m.eval(v,model_completion=True);b.append(Q(z.numerator_as_long(),z.denominator_as_long()))
  proofs=[];bad=[]
  for ci,a in enumerate(cs):
   p=poly_pair(a,b);ch=halfline(p);proofs.append(ch)
   if ch['status']=='NEGATIVE' and ch['t']!='infinity':bad.append((ci,Q(ch['t'])))
   elif ch['status']!='STRICT_POSITIVITY':bad.append((ci,None))
  if not bad:return {'case':case,'status':'COMMON_NUMERATOR_PROVED','b':list(map(str,b)),'proofs':proofs,'history':history,'source_sha256':sha256(raw).hexdigest()}
  if any(t is None for ci,t in bad):return {'case':case,'status':'CHECK_INCONCLUSIVE','history':history,'source_sha256':sha256(raw).hexdigest()}
  history.append([[ci,str(t)] for ci,t in bad])
  for ci,t in bad:add(ci,t)
 return {'case':case,'status':'EXCHANGE_CAP','history':history,'source_sha256':sha256(raw).hexdigest()}
for case in range(12):
 out=exchange(case);file=root/('frontier-20261028-sturm-band-positive-case-%02d-v1.json'%case);text=json.dumps(out,indent=2,sort_keys=True)+'\n';file.write_text(text)
 print('positive-band case',case,out['status'],'steps',len(out.get('history',[])),'sha256',sha256(text.encode()).hexdigest())
