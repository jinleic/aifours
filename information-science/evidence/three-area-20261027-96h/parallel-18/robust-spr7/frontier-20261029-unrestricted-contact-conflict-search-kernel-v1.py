# Exact three-parameter unrestricted boundary-tangency search at the four
# frozen 7D-span conflict shapes. A solver/grid failure is not a verdict.
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json,z3
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return raw.decode()
s=pin('frontier-20261029-positive-contact-seven-span-shapes-frozen-v1.json','2ee71031d831bce8bce95b96448c734ff52b9754088b3ec21062f1c09f106097');shapes=json.loads(s)['shapes']
s=(root/'frontier-20261029-positive-contact-seven-span-search-kernel-v1.py').read_text();exec(s[:s.index('for i in range(150):')])
def zq(v):return z3.Q(v.numerator,v.denominator)
def run8(case):
 ts,lo,hi,cs=boundary(shapes[case]);ct=[(2,ts[0]),(3,ts[1]),(1,ts[2]),(0,ts[3]),(2,ts[4])];T=[]
 for ci,t in ct:
  a=cs[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in T];bases=[]
 try:
  for k in (0,6,7):
   b=[Q(0)]*8;b[k]=Q(1)
   for j,x in zip((1,2,3,4,5),solve(A,[-row[k] for row in T])):b[j]=x
   if any(sum(row[j]*b[j] for j in range(8)) for row in T):raise ValueError('TANGENCY')
   bases.append(b)
 except ValueError as e:
  if str(e)=='SINGULAR':return {'case':case,'status':'SINGULAR'}
  raise
 residual=[]
 for ci,a in enumerate(cs):
  pol=[]
  for b in bases:
   p=pair(a,b)
   for cj,t in ct:
    if cj==ci:p=divide(divide(p,t),t)
   pol.append(p)
  residual.append(pol)
 X=[z3.Real('unrestricted_%d_%d'%(case,i)) for i in range(3)];d=z3.Real('unrestricted_delta_%d'%case);opt=z3.Optimize();opt.set(timeout=12000)
 opt.add(sum(X[k]*zq(sum(bases[k])) for k in range(3))==1)
 for j in range(8):opt.add(sum(X[k]*zq(bases[k][j]) for k in range(3))>=d)
 added=set()
 def add(ci,t):
  if (ci,t) in added:return
  degree=7-2*sum(cj==ci for cj,x in ct)
  vals=[p[degree] if t is None and len(p)>degree else Q(0) if t is None else sum(v*t**j for j,v in enumerate(p))/(1+t)**degree for p in residual[ci]]
  opt.add(sum(X[k]*zq(vals[k]) for k in range(3))>=d);added.add((ci,t))
 grid={Q(0),Q(1,100),Q(1,10),Q(1),Q(10),Q(100),Q(1000)}
 for t in ts:grid.update((t/2,t,t*2))
 for a,b in zip(ts,ts[1:]):grid.add((a+b)/2)
 for ci in range(4):
  for t in grid:add(ci,t)
  add(ci,None)
 opt.maximize(d);history=[]
 for step in range(15):
  st=opt.check()
  if st!=z3.sat:return {'case':case,'status':'SOLVER_'+str(st),'step':step,'history':history}
  model=opt.model();dv=model.eval(d);margin=Q(dv.numerator_as_long(),dv.denominator_as_long());x=[Q(model.eval(v).numerator_as_long(),model.eval(v).denominator_as_long()) for v in X];b=[sum(x[k]*bases[k][j] for k in range(3)) for j in range(8)]
  if margin<=0:return {'case':case,'status':'NONPOSITIVE_GRID_MARGIN','step':step,'margin':str(margin),'history':history}
  bad=[];proof=[]
  for ci,a in enumerate(cs):
   p=pair(a,b)
   for cj,t in ct:
    if cj==ci:p=divide(divide(p,t),t)
   check=sign_halfline(p);proof.append(check)
   if check['status']=='NEGATIVE' and check['t']!='infinity':bad.append((ci,Q(check['t'])))
   elif check['status']!='STRICT_POSITIVITY':bad.append((ci,None))
  if not bad:return {'case':case,'status':'STRICT_BOUNDARY_RESIDUALS_PROVED','step':step,'b':list(map(str,b)),'history':history,'leaves':[p['leaves'] for p in proof]}
  if any(t is None for ci,t in bad):return {'case':case,'status':'HALFLINE_INCONCLUSIVE','step':step,'history':history}
  history.append([[ci,str(t)] for ci,t in bad])
  for ci,t in bad:add(ci,t)
 return {'case':case,'status':'EXCHANGE_CAP','history':history}
for case in (84,86,93,133):
 out=run8(case);path=root/('frontier-20261029-unrestricted-contact-conflict-case-%03d-v1.json'%case);text=json.dumps(out,sort_keys=True,indent=2)+'\n';path.write_text(text);print('unrestricted conflict shape',case,out['status'],'step',out.get('step'),'sha256',sha256(text.encode()).hexdigest())
