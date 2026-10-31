# Exact seven-dimensional real-span synthesis at a zero-constant plus
# five-contact boundary. Residual cuts are added as normalized residual rows,
# not physical rows that vanish at contact nodes. No unresolved cap is verdict.
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from math import lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return raw.decode()
s=pin('frontier-20261028-sturm-band-scaled-positive-kernel-v1.py','40e478817389f873c0cfb465dcd89a633b8d8f54c333bfb0fdca70d7769974f9');exec(s[:s.index('result=solve(0)')])
s=pin('frontier-20261028-bounded-exact-dual-search-kernel-v1.py','bc10ea9be94ff63d729eccae52ad60e33079883a4b4ad33af898cea98535896a');exec(s[s.index('def bareiss_det'):s.index('def integer_hurwitz')])
shapes=json.loads(pin('frontier-20261028-zero-five-conditioned-shapes-frozen-v1.json','207df0dfb055442a144805219ae187dfe699ec37a2e24ad84f066323758e3b3f'))['shapes']
def det(A):
 d=lcm(*(v.denominator for row in A for v in row));return Q(bareiss_det([[int(v*d) for v in row] for row in A]),d**len(A))
def cubic(rs,scale):
 p=[-scale]
 for x in rs:p=poly_mul(p,[-x,Q(1)])
 return p
def boundary(sh):
 ts=list(map(Q,sh['nodes']));a,b,c,d,e=ts;v=Q(sh['v']);lam=Q(sh['lambda']);Em=cubic([Q(0),c,d],lam);Ep=cubic([a,b,e],Q(1));Om=cubic([a,d,e],Q(1));Op=cubic([b,c,v],Q(1));lo=[Em[0],Om[0],-Ep[1],-Op[1],Em[2],Om[2],-Ep[3]];hi=[Ep[0],Op[0],-Em[1],-Om[1],Ep[2],Op[2],-Em[3]]
 if lo[0]!=0 or not all(lo[j]<hi[j] for j in range(7)):raise ValueError('WIDTH')
 return ts,lo,hi,corners(lo,hi)
def solve(A,y):
 n=len(y);M=[A[i][:]+[y[i]] for i in range(n)]
 for k in range(n):
  p=next((i for i in range(k,n) if M[i][k]),None)
  if p is None:raise ValueError('SINGULAR')
  M[p],M[k]=M[k],M[p];v=M[k][k];M[k]=[x/v for x in M[k]]
  for i in range(n):
   if i!=k:
    v=M[i][k]
    if v:M[i]=[x-v*y for x,y in zip(M[i],M[k])]
 return [M[i][-1] for i in range(n)]
def divide(p,r):
 z=[Q(0)]*(len(p)-1);z[-1]=p[-1]
 for j in range(len(z)-2,-1,-1):z[j]=p[j+1]+r*z[j+1]
 if p[0]+r*z[0]:raise ValueError('DIVISION')
 while len(z)>1 and z[-1]==0:z.pop()
 return z
def run(case):
 ts,lo,hi,cs=boundary(shapes[case]);mid=[(lo[j]+hi[j])/2 for j in range(7)]+[Q(1)];ds=[mid]
 for _ in range(3):ds.append([Q(j+1)*ds[-1][j+1] for j in range(7)]+[Q(0)])
 G=[[cs[2*e][j] if j%2==0 else Q(0) for j in range(8)] for e in (0,1)]+[[cs[o][j] if j%2 else Q(0) for j in range(8)] for o in (0,1)]+ds[1:4];ct=[(2,ts[0]),(3,ts[1]),(1,ts[2]),(0,ts[3]),(2,ts[4])];T=[]
 for ci,t in ct:
  a=cs[ci];e=-a[2]+2*a[4]*t-3*a[6]*t*t;o=-a[3]+2*a[5]*t-3*t*t;row=[e*(-t)**(j//2) if j%2==0 else t*o*(-t)**((j-1)//2) for j in range(8)];T.append([sum(row[j]*g[j] for j in range(8)) for g in G])
 for ix in combinations(range(7),5):
  A=[[r[j] for j in ix] for r in T]
  if det(A):break
 else:return {'case':case,'status':'RANK_DEFICIENT'}
 free=[j for j in range(7) if j not in ix];N=[];Ncoef=[]
 for k in free:
  z=[Q(0)]*7;z[k]=1
  for j,x in zip(ix,solve(A,[-r[k] for r in T])):z[j]=x
  Ncoef.append(z);N.append([sum(z[k]*G[k][j] for k in range(7)) for j in range(8)])
 if not N[1][7]:N.reverse();Ncoef.reverse()
 if not N[1][7]:return {'case':case,'status':'NO_LEADING_DIRECTION'}
 U=[v/N[1][7] for v in N[1]];V=[N[0][j]-N[0][7]*U[j] for j in range(8)];UC=[v/N[1][7] for v in Ncoef[1]];VC=[Ncoef[0][j]-N[0][7]*UC[j] for j in range(7)]
 residual=[]
 for ci,a in enumerate(cs):
  pairset=[]
  for b in (U,V):
   p=pair(a,b)
   if ci in (0,1):p=divide(p,Q(0))
   for cj,t in ct:
    if ci==cj:p=divide(divide(p,t),t)
   pairset.append(p)
  residual.append(pairset)
 rows={(ci,t) for ci in range(4) for t in [Q(0)]+ts}
 for step in range(30):
  low=None;high=None
  for ci,t in rows:
   A=sum(v*t**j for j,v in enumerate(residual[ci][0]));B=sum(v*t**j for j,v in enumerate(residual[ci][1]))
   if B>0:low=-A/B if low is None else max(low,-A/B)
   elif B<0:high=-A/B if high is None else min(high,-A/B)
   elif A<0:return {'case':case,'status':'POINT_NEGATIVE','step':step,'corner':ci,'t':str(t)}
  if low is not None and high is not None and low>=high:return {'case':case,'status':'GRID_NO_STRICT','step':step,'lower':str(low),'upper':str(high)}
  x=Q(0) if low is None and high is None else high-1 if low is None else low+1 if high is None else (low+high)/2;b=[U[j]+x*V[j] for j in range(8)];coef=[UC[j]+x*VC[j] for j in range(7)];bad=[];proof=[]
  for ci in range(4):
   a0,a1=residual[ci];p=[(a0[j] if j<len(a0) else Q(0))+x*(a1[j] if j<len(a1) else Q(0)) for j in range(max(len(a0),len(a1)))];z=sign_halfline(p);proof.append(z)
   if z['status']=='NEGATIVE' and z['t']!='infinity':bad.append((ci,Q(z['t'])))
   elif z['status']!='STRICT_POSITIVITY':bad.append((ci,None))
  if not bad:return {'case':case,'status':'STRICT_RESIDUALS_PROVED','step':step,'b':list(map(str,b)),'generator_coefficients':list(map(str,coef)),'all_coeff_positive':all(v>0 for v in b),'leaves':[v['leaves'] for v in proof]}
  if any(t is None for ci,t in bad):return {'case':case,'status':'CHECK_INCONCLUSIVE','step':step}
  rows.update(bad)
 return {'case':case,'status':'EXCHANGE_CAP'}
for i in range(30):
 res=run(i);p=root/('frontier-20261029-zero-seven-span-residual-case-%02d-v1.json'%i);txt=json.dumps(res,indent=2,sort_keys=True)+'\n';p.write_text(txt);print('zero-seven residual',i,res['status'],'step',res.get('step'),'positive coefficients',res.get('all_coeff_positive'),'sha256',sha256(txt.encode()).hexdigest())
 if res['status']=='GRID_NO_STRICT':break
