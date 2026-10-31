# Bounded exact tangent-cone search at 30 frozen five-contact PLUS origin
# boundary shapes. Positive residual proofs cover their radial subboxes; a
# nonpositive sampled margin is only a candidate, not an actual-box verdict.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import json,z3
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return raw.decode()
s=pin('frontier-20261028-sturm-band-scaled-positive-kernel-v1.py','40e478817389f873c0cfb465dcd89a633b8d8f54c333bfb0fdca70d7769974f9');exec(s[:s.index('result=solve(0)')])
shapes=json.loads(pin('frontier-20261028-zero-five-conditioned-shapes-frozen-v1.json','207df0dfb055442a144805219ae187dfe699ec37a2e24ad84f066323758e3b3f'))['shapes']
def cubic(r,scale):
 p=[-scale]
 for x in r:
  p=poly_mul(p,[-x,Q(1)])
 return p
def box(ts,lam,v):
 a,b,c,d,e=ts;E0=cubic([Q(0),c,d],lam);E1=cubic([a,b,e],Q(1));O0=cubic([a,d,e],Q(1));O1=cubic([b,c,v],Q(1));lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if lo[0]!=0 or not all(lo[j]<hi[j] for j in range(7)) or not all(lo[j]>0 for j in range(1,7)):raise ValueError('WIDTH')
 return lo,hi,corners(lo,hi)
def solve5(A,b):
 M=[list(row)+[b[i]] for i,row in enumerate(A)]
 for k in range(5):
  p=next((i for i in range(k,5) if M[i][k]),None)
  if p is None:raise ValueError('SINGULAR')
  M[k],M[p]=M[p],M[k];v=M[k][k];M[k]=[x/v for x in M[k]]
  for i in range(5):
   if i!=k:
    v=M[i][k]
    if v:M[i]=[x-v*y for x,y in zip(M[i],M[k])]
 return [M[i][-1] for i in range(5)]
def divide(p,r):
 out=[Q(0)]*(len(p)-1);out[-1]=p[-1]
 for j in range(len(out)-2,-1,-1):out[j]=p[j+1]+r*out[j+1]
 if p[0]+r*out[0]:raise ValueError('ROOT')
 while len(out)>1 and out[-1]==0:out.pop()
 return out
def zq(v):return z3.Q(v.numerator,v.denominator)
def run(idx,shape):
 ts=list(map(Q,shape['nodes']));lo,hi,cs=box(ts,Q(shape['lambda']),Q(shape['v']));ct=[(2,ts[0]),(3,ts[1]),(1,ts[2]),(0,ts[3]),(2,ts[4])];rows=[]
 for ci,t in ct:
  a=cs[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  rows.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 bases=[]
 for j in (0,6,7):
  b=[Q(0)]*8;b[j]=Q(1);z=solve5([[row[k] for k in (1,2,3,4,5)] for row in rows],[-row[j] for row in rows])
  for k,x in zip((1,2,3,4,5),z):b[k]=x
  if any(sum(row[k]*b[k] for k in range(8)) for row in rows):raise ValueError('TANGENT')
  bases.append(b)
 def residual(ci,b):
  p=pair(cs[ci],b)
  if ci in (0,1):p=divide(p,Q(0))
  for k,t in ct:
   if k==ci:p=divide(divide(p,t),t)
  return p
 polys=[[residual(ci,b) for b in bases] for ci in range(4)];degrees=[4,4,3,5]
 X=[z3.Real('zero_x_'+str(idx)+'_'+str(k)) for k in range(3)];delta=z3.Real('zero_d_'+str(idx));opt=z3.Optimize();opt.set(timeout=8000);opt.add(sum(X[k]*zq(sum(bases[k])) for k in range(3))==1)
 for j in range(8):opt.add(sum(X[k]*zq(bases[k][j]) for k in range(3))>=delta)
 added=set()
 def add(ci,t):
  if (ci,t) in added:return
  d=degrees[ci]
  values=[p[d] if t is None and len(p)>d else Q(0) if t is None else sum(x*t**j for j,x in enumerate(p))/(1+t)**d for p in polys[ci]]
  opt.add(sum(X[k]*zq(values[k]) for k in range(3))>=delta);added.add((ci,t))
 grid={Q(0),Q(1,10),Q(1),Q(10),Q(100)}
 for t in ts:grid.update((t/2,t,2*t))
 for a,b in zip(ts,ts[1:]):grid.add((a+b)/2)
 for ci in range(4):
  for t in grid:add(ci,t)
  add(ci,None)
 opt.maximize(delta);history=[]
 for step in range(12):
  status=opt.check()
  if status!=z3.sat:return {'case':idx,'status':'SOLVER_'+str(status),'step':step,'history':history}
  m=opt.model();x=[Q(m.eval(z).numerator_as_long(),m.eval(z).denominator_as_long()) for z in X];d=m.eval(delta);d=Q(d.numerator_as_long(),d.denominator_as_long());B=[sum(x[k]*bases[k][j] for k in range(3)) for j in range(8)]
  if d<=0:return {'case':idx,'status':'NONPOSITIVE_GRID_MARGIN','step':step,'margin':str(d),'history':history,'grid':[[ci,'infinity' if t is None else str(t)] for ci,t in sorted(added,key=lambda a:(a[0],Q(-1) if a[1] is None else a[1]))]}
  bad=[];proof=[]
  for ci in range(4):
   q=residual(ci,B);r=sign_halfline(q);proof.append(r)
   if r['status']=='NEGATIVE' and r['t']!='infinity':bad.append((ci,Q(r['t'])))
   elif r['status']!='STRICT_POSITIVITY':bad.append((ci,None))
  if not bad:return {'case':idx,'status':'STRICT_BOUNDARY_RESIDUALS_PROVED','step':step,'b':list(map(str,B)),'history':history,'leaves':[r['leaves'] for r in proof]}
  if any(t is None for ci,t in bad):return {'case':idx,'status':'HALFLINE_INCONCLUSIVE','step':step,'history':history}
  history.append([[ci,str(t)] for ci,t in bad])
  for ci,t in bad:add(ci,t)
 return {'case':idx,'status':'EXCHANGE_CAP','history':history}
for case in range(30):
 res=run(case,shapes[case]);path=root/('frontier-20261028-zero-five-tangent-case-%02d-v1.json'%case);txt=json.dumps(res,sort_keys=True,indent=2)+'\n';path.write_text(txt)
 print('zero-five case',case,res['status'],'step',res.get('step'),'sha256',sha256(txt.encode()).hexdigest())
 if res['status']=='NONPOSITIVE_GRID_MARGIN':break
