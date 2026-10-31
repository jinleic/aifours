# Exact normalized tangent-cone search on the independently frozen set of
# high-gain derivative failures. An inconclusive grid is not a verdict.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json,z3
source=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-gain-barrier-conditioned-search-result-v1.json')
raw=source.read_bytes()
if sha256(raw).hexdigest()!='9183832f233ded9dd96383db1fab249e94d4fce2ccdb321b79657a61ce679739':raise ValueError('PIN')
shapes=json.loads(raw)['derivative_negative']
def toz(q):return z3.Q(q.numerator,q.denominator)
def tangent_case(shape,idx):
 ts=list(map(Q,shape['nodes']));u=Q(shape['u']);lam=Q(shape['lambda']);v=Q(shape['v']);vs=vtx(u,lam,v,ts)
 contacts=[(2,ts[0]),(3,ts[1]),(1,ts[2]),(0,ts[3]),(2,ts[4])];rows=[]
 for ci,t in contacts:
  a=vs[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  rows.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 bases=[]
 for j in (0,6,7):
  b=[Q(0)]*8;b[j]=Q(1);vals=solve5([[row[k] for k in (1,2,3,4,5)] for row in rows],[-row[j] for row in rows])
  for k,x in zip((1,2,3,4,5),vals):b[k]=x
  if any(sum(row[k]*b[k] for k in range(8)) for row in rows):raise ValueError('TANGENCY')
  bases.append(b)
 polys=[];degrees=[]
 for ci,a in enumerate(vs):
  group=[];degrees.append(7-2*sum(k==ci for k,t in contacts))
  for b in bases:
   pp=pair(a,b)
   for k,t in contacts:
    if k==ci:pp=divide(divide(pp,t),t)
   group.append(pp)
  polys.append(group)
 X=[z3.Real('cx_'+str(idx)+'_'+str(j)) for j in range(3)];delta=z3.Real('cd_'+str(idx));opt=z3.Optimize();opt.set(timeout=10000)
 opt.add(sum(X[k]*toz(sum(bases[k])) for k in range(3))==1)
 for j in range(8):opt.add(sum(X[k]*toz(bases[k][j]) for k in range(3))>=delta)
 seen=set()
 def add(ci,t):
  key=(ci,t)
  if key in seen:return
  degree=degrees[ci]
  if t is None:q=[p[degree] if len(p)>degree else Q(0) for p in polys[ci]]
  else:q=[sum(x*t**j for j,x in enumerate(p))/(1+t)**degree for p in polys[ci]]
  opt.add(sum(X[k]*toz(q[k]) for k in range(3))>=delta);seen.add(key)
 grid={Q(0),Q(1,1000),Q(1,100),Q(1,10),Q(1),Q(10),Q(100)}
 for t in ts:grid.update([t/2,t,t*2])
 for a,b in zip(ts,ts[1:]):grid.add((a+b)/2)
 for ci in range(4):
  for t in grid:add(ci,t)
  add(ci,None)
 opt.maximize(delta);history=[]
 for step in range(12):
  status=opt.check()
  if status!=z3.sat:return {'shape':idx,'status':str(status),'step':step,'history':history,'grid_size':len(seen)}
  model=opt.model();val=model.eval(delta);d=Q(val.numerator_as_long(),val.denominator_as_long())
  x=[Q(model.eval(v).numerator_as_long(),model.eval(v).denominator_as_long()) for v in X]
  B=[sum(x[k]*bases[k][j] for k in range(3)) for j in range(8)]
  if d<=0:return {'shape':idx,'status':'NONPOSITIVE_NORMALIZED_GRID_MARGIN','margin':str(d),'step':step,'history':history,'grid_size':len(seen),'grid':[[ci,str(t) if t is not None else 'infinity'] for ci,t in sorted(seen,key=lambda p:(p[0],Q(-1) if p[1] is None else p[1]))]}
  bad=[];proof=[]
  for ci in range(4):
   p=pair(vs[ci],B)
   for k,t in contacts:
    if k==ci:p=divide(divide(p,t),t)
   check=exact_nonnegative_halfline(p,maxdepth=60,maxnodes=10000);proof.append(check)
   if check['status']=='NEGATIVE':bad.append((ci,Q(check['t'])))
   elif check['status']!='NONNEGATIVE_PROVED' or not all(Q(v)>0 for leaf in check['leaves'] for v in leaf['coefficients']):bad.append((ci,None))
  if not bad:return {'shape':idx,'status':'STRICT_BOUNDARY_RESIDUALS_PROVED','step':step,'margin':str(d),'b':list(map(str,B)),'history':history,'grid_size':len(seen),'leaf_counts':[len(k['leaves']) for k in proof]}
  if any(t is None for ci,t in bad):return {'shape':idx,'status':'SUBDIVISION_INCONCLUSIVE','step':step,'history':history,'grid_size':len(seen)}
  history.append([[ci,str(t)] for ci,t in bad])
  for ci,t in bad:add(ci,t)
 return {'shape':idx,'status':'EXCHANGE_CAP','history':history,'grid_size':len(seen)}
results=[]
for i,shape in enumerate(shapes):
 result=tangent_case(shape,i);results.append(result)
 print('tangent-case',i,result['status'],'step',result.get('step'),'grid',result['grid_size'])
 if result['status']=='NONPOSITIVE_NORMALIZED_GRID_MARGIN':break
out={'source_sha256':'9183832f233ded9dd96383db1fab249e94d4fce2ccdb321b79657a61ce679739','scope':'exact sampled/tangent checks; only strict boundary residual proofs include continuum verification; no automatic actual-box negative certificate','results':results}
path=source.with_name('frontier-20261028-gain-barrier-tangent-cone-search-result-v1.json');text=json.dumps(out,sort_keys=True,indent=2)+'\n';path.write_text(text)
print('tangent-cone search sha256',sha256(text.encode()).hexdigest())
