# Bounded exact search on distinct non-five-contact oscillatory-centered
# anisotropic boxes. Routh bisection keeps all four actual parity corners
# strictly stable. Grid optima are not all-frequency or negative certificates.
from fractions import Fraction as Q
from random import Random
from pathlib import Path
from hashlib import sha256
import json,z3
RG=Random(2026102824)
def poly_mul(A,B):
 C=[Q(0)]*(len(A)+len(B)-1)
 for i,x in enumerate(A):
  for j,y in enumerate(B):C[i+j]+=x*y
 return C
def box_corners(lo,hi):
 out=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  out.append([((lo[j] if not (e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not (e if j%2==0 else o) else lo[j])) for j in range(7)]+[Q(1)])
 return out
def bvec(a,t):
 E=a[0]-a[2]*t+a[4]*t*t-a[6]*t**3;O=a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
 return [(E*(-t)**(j//2) if j%2==0 else t*O*(-t)**((j-1)//2))/(1+t)**7 for j in range(8)]
def zz(x):return z3.Q(x.numerator,x.denominator)
def solve_box(cs,freq,index):
 B=[z3.Real('ob_'+str(index)+'_'+str(j)) for j in range(8)];D=z3.Real('od_'+str(index));opt=z3.Optimize();opt.set(timeout=10000);opt.add(sum(B)==1)
 for x in B:opt.add(x>=D)
 added=set()
 def push(ci,t):
  if (ci,t) in added:return
  row=bvec(cs[ci],t);opt.add(sum(B[j]*zz(row[j]) for j in range(8))>=D);added.add((ci,t))
 for ci in range(4):
  for t in freq:push(ci,t)
 opt.maximize(D);history=[]
 for iteration in range(12):
  st=opt.check()
  if st!=z3.sat:return {'status':str(st),'iteration':iteration,'history':history,'rows':len(added)}
  model=opt.model();x=model.eval(D);margin=Q(x.numerator_as_long(),x.denominator_as_long());b=[Q(model.eval(v).numerator_as_long(),model.eval(v).denominator_as_long()) for v in B]
  if margin<=0:return {'status':'NONPOSITIVE_GRID_MARGIN','margin':str(margin),'iteration':iteration,'history':history,'rows':len(added),'grid':[[ci,str(t)] for ci,t in sorted(added)]}
  bad=[];proof=[]
  for ci,a in enumerate(cs):
   p=pair(a,b);ch=exact_nonnegative_halfline(p,maxdepth=60,maxnodes=20000);proof.append(ch)
   if ch['status']=='NEGATIVE':bad.append((ci,Q(ch['t'])))
   elif ch['status']!='NONNEGATIVE_PROVED' or not all(Q(x)>0 for leaf in ch['leaves'] for x in leaf['coefficients']):bad.append((ci,None))
  if not bad:return {'status':'COMMON_NUMERATOR_PROVED','margin':str(margin),'b':list(map(str,b)),'leaf_counts':[len(c['leaves']) for c in proof],'iteration':iteration,'history':history,'rows':len(added)}
  if any(t is None for ci,t in bad):return {'status':'SUBDIVISION_INCONCLUSIVE','iteration':iteration,'history':history,'rows':len(added)}
  history.append([[ci,str(t)] for ci,t in bad])
  for ci,t in bad:push(ci,t)
 return {'status':'EXCHANGE_CAP','history':history,'rows':len(added)}
res={'seed':2026102824,'cases':[],'scope':'Only exact finite sampling and explicitly certified all-frequency positive cases; nonpositive grid margin requires separate independent negative-certificate construction.'}
for case in range(16):
 alpha=RG.choice([1,2,3,5]);A=[Q(alpha),Q(1)];params=[]
 for j in range(3):
  re=RG.choice([1,2,3,5]);im=RG.choice([3,7,13,25,50,100]);params.append((re,im));A=poly_mul(A,[Q(re*re+im*im),Q(2*re),Q(1)])
 lower_rate=[Q(RG.choice([1,2,4,8]),8) for _ in range(7)];upper_rate=[Q(RG.choice([1,2,4,8,16,32]),8) for _ in range(7)]
 def endpoints(r):return [A[j]*(1-r*lower_rate[j]) for j in range(7)],[A[j]*(1+r*upper_rate[j]) for j in range(7)]
 a=Q(0);b=min(1/x for x in lower_rate)
 for _ in range(18):
  m=(a+b)/2;l,h=endpoints(m)
  if all(routh_ok(p) for p in box_corners(l,h)):a=m
  else:b=m
 r=a*Q(9999,10000);lo,hi=endpoints(r);cs=box_corners(lo,hi)
 if not r>0 or not all(routh_ok(p) and integer_hurwitz(p) for p in cs):raise ValueError('STABILITY')
 freq={Q(0)}
 for k in range(-4,7):freq.add(Q(10**k) if k>=0 else Q(1,10**(-k)))
 for re,im in params:
  t=Q(re*re+im*im)
  for q in (Q(1,2),Q(9,10),Q(99,100),Q(1),Q(101,100),Q(11,10),Q(2)):freq.add(t*q)
 trial=solve_box(cs,freq,case);trial.update({'case':case,'center_first_order':alpha,'center_pairs':params,'rho_scale':str(r),'lower':list(map(str,lo)),'upper':list(map(str,hi))});res['cases'].append(trial)
 print('oscillatory box',case,trial['status'],'iterations',trial.get('iteration'),'rows',trial['rows'])
 if trial['status']=='NONPOSITIVE_GRID_MARGIN':break
out=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-oscillatory-anisotropic-decision-search-result-v1.json');text=json.dumps(res,indent=2,sort_keys=True)+'\n';out.write_text(text)
print('oscillatory decision search sha256',sha256(text.encode()).hexdigest())
