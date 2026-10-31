# Condition on exact nonempty u/lambda/v intervals before generating diverse
# five-contact shapes. A failed high-gain sufficient criterion is NOT a
# counterexample to the original all-member common-SPR problem.
from fractions import Fraction as Q
from random import Random
from pathlib import Path
from hashlib import sha256
import json
R=Random(2026102822)
edge=[Q(1,1000000),Q(1,1000),Q(1,2),Q(999,1000),Q(999999,1000000)]
record={'seed':2026102822,'proposals':0,'feasible':0,'strict_residual_success':0,'negative':[],'inconclusive':[],'examples':[]}
def rr():
 exp=R.randrange(-3,4);return Q(R.randrange(1,21))* (Q(10**exp) if exp>=0 else Q(1,10**(-exp)))
def vtx(u,lam,v,ts):
 a,b,c,d,e=ts;E0=rootpoly([u,c,d],lam);E1=rootpoly([a,b,e],Q(1));O0=rootpoly([a,d,e],Q(1));O1=rootpoly([b,c,v],Q(1))
 lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if not all(Q(0)<x<y for x,y in zip(lo,hi)):raise ValueError('WIDTH')
 def mk(E,O):return [E[0],O[0],-E[1],-O[1],E[2],O[2],-E[3],Q(1)]
 return [mk(E0,O0),mk(E0,O1),mk(E1,O0),mk(E1,O1)]
for trial in range(12000):
 record['proposals']+=1;ts=[Q(1)]
 for j in range(4):ts.append(ts[-1]+rr())
 a,b,c,d,e=ts;vlow=max(e,a+d+e-b-c,a*d*e/(b*c));vhigh=(a*d+a*e+d*e-b*c)/(b+c)
 if vlow>=vhigh:continue
 S=a+b+e;P=a*b*e;T=a*b+a*e+b*e;C=S*(c+d)-T
 if C<=0:continue
 ulo=max(Q(0),(T*(c+d)-S*c*d)/C);uhi=min(a,P/(c*d),S-c-d)
 Z=c*d*T-P*(c+d)
 if Z>0:uhi=min(uhi,P*c*d/Z)
 if ulo>=uhi:continue
 u=ulo+edge[R.randrange(len(edge))]*(uhi-ulo);v=vlow+edge[R.randrange(len(edge))]*(vhigh-vlow)
 llo=max(Q(1),T/(u*(c+d)+c*d));lhi=min(P/(u*c*d),S/(u+c+d))
 if llo>=lhi:raise ValueError('U_INTERVAL')
 lam=llo+edge[R.randrange(len(edge))]*(lhi-llo);vertices=vtx(u,lam,v,ts);contacts=[(2,a),(3,b),(1,c),(0,d),(2,e)]
 record['feasible']+=1
 Trows=[]
 for ci,t in contacts:
  p=vertices[ci];ep=-p[2]+2*p[4]*t-3*p[6]*t*t;op=-p[3]+2*p[5]*t-3*t*t
  Trows.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 B=[Q(0)]*8;B[6]=Q(1)
 try:vals=solve5([[row[j] for j in (1,2,3,4,5)] for row in Trows],[-row[6] for row in Trows])
 except ValueError as ex:
  record['inconclusive'].append({'trial':trial+1,'reason':str(ex)});continue
 for j,x in zip((1,2,3,4,5),vals):B[j]=x
 if any(sum(row[j]*B[j] for j in range(8)) for row in Trows):raise ValueError('TANGENT')
 desc={'trial':trial+1,'contacts':[str(x) for x in ts],'u':str(u),'lambda':str(lam),'v':str(v)}
 if not all(x>0 for x in B[1:7]):
  record['negative'].append({'reason':'NONPOSITIVE_HIGH_GAIN_COEFFICIENT','shape':desc,'b':[str(x) for x in B]});break
 grouped={i:[] for i in range(4)}
 for ci,t in contacts:grouped[ci].append(t)
 good=True
 for ci,p in enumerate(vertices):
  poly=divide(pair(p,B),Q(0))
  for t in grouped[ci]:poly=divide(divide(poly,t),t)
  check=exact_nonnegative_halfline(poly,maxdepth=60,maxnodes=12000)
  if check['status'].startswith('NEGATIVE'):
   record['negative'].append({'reason':'NEGATIVE_HIGH_GAIN_RESIDUAL','shape':desc,'corner':ci,'result':check,'b':[str(x) for x in B],'residual':[str(x) for x in poly]});good=False;break
  if check['status']!='NONNEGATIVE_PROVED' or not all(Q(x)>0 for leaf in check['leaves'] for x in leaf['coefficients']):
   record['inconclusive'].append({'trial':trial+1,'corner':ci,'reason':check['status'],'shape':desc});good=False;break
 if good:
  record['strict_residual_success']+=1
  if len(record['examples'])<5:record['examples'].append(desc)
 if record['negative'] or record['feasible']>=100:break
print('conditioned extreme five-contact screen:',record)
