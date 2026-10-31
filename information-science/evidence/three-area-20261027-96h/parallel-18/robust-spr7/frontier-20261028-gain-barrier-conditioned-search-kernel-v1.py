# Deterministic exact conditioned search for five-contact shapes where the
# high-gain tangent direction already fails at the low-frequency derivative.
# A failure of this direction is not a counterexample to common SPR.
from fractions import Fraction as Q
from random import Random
from pathlib import Path
from hashlib import sha256
import json
random_gain=Random(2026102823);gain_edges=[Q(1,1000000),Q(1,1000),Q(1,2),Q(999,1000),Q(999999,1000000)]
def gain_step():
 e=random_gain.randrange(-3,4)
 return Q(random_gain.randrange(1,21))*(Q(10**e) if e>=0 else Q(1,10**(-e)))
def gain_draw():
 ts=[Q(1)]
 for _ in range(4):ts.append(ts[-1]+gain_step())
 a,b,c,d,e=ts;vl=max(e,a+d+e-b-c,a*d*e/(b*c));vh=(a*d+a*e+d*e-b*c)/(b+c)
 if vl>=vh:return None
 S=a+b+e;P=a*b*e;T=a*b+a*e+b*e;C=S*(c+d)-T
 if C<=0:return None
 ul=max(Q(0),(T*(c+d)-S*c*d)/C);uh=min(a,P/(c*d),S-c-d);Z=c*d*T-P*(c+d)
 if Z>0:uh=min(uh,P*c*d/Z)
 if ul>=uh:return None
 u=ul+gain_edges[random_gain.randrange(len(gain_edges))]*(uh-ul);v=vl+gain_edges[random_gain.randrange(len(gain_edges))]*(vh-vl)
 ll=max(Q(1),T/(u*(c+d)+c*d));lh=min(P/(u*c*d),S/(u+c+d))
 if ll>=lh:raise ValueError('U_INTERVAL')
 lam=ll+gain_edges[random_gain.randrange(len(gain_edges))]*(lh-ll)
 return ts,u,lam,v
barrier={'seed':2026102823,'proposals':0,'feasible':0,'singular':0,'derivative_negative':[]}
for trial in range(25000):
 barrier['proposals']+=1;shape=gain_draw()
 if shape is None:continue
 ts,u,lam,v=shape;vertices=vtx(u,lam,v,ts);contacts=[(2,ts[0]),(3,ts[1]),(1,ts[2]),(0,ts[3]),(2,ts[4])];rows=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  rows.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 try:z=solve5([[row[j] for j in (1,2,3,4,5)] for row in rows],[-row[6] for row in rows])
 except ValueError:
  barrier['singular']+=1;continue
 B=[Q(0)]*8;B[6]=Q(1)
 for j,x in zip((1,2,3,4,5),z):B[j]=x
 barrier['feasible']+=1
 bad=[(ci,a[1]*B[1]-a[0]*B[2]) for ci,a in enumerate(vertices) if a[1]*B[1]-a[0]*B[2]<0]
 if bad:
  barrier['derivative_negative'].append({'proposal':trial+1,'nodes':list(map(str,ts)),'u':str(u),'lambda':str(lam),'v':str(v),'corners':[i for i,z in bad],'derivatives':[str(z) for i,z in bad]})
 if len(barrier['derivative_negative'])>=12 or barrier['feasible']>=1500:break
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-gain-barrier-conditioned-search-result-v1.json');s=json.dumps(barrier,indent=2,sort_keys=True)+'\n';path.write_text(s)
print('gain barrier search:',{'proposals':barrier['proposals'],'feasible':barrier['feasible'],'singular':barrier['singular'],'failures':len(barrier['derivative_negative']),'sha256':sha256(s.encode()).hexdigest()})
