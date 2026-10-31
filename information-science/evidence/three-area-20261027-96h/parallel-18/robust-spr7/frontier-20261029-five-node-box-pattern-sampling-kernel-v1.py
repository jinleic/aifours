# NONVERDICT exact-sign sampling: random exact-rational eligible boxes (band-root
# construction), random nodes in the classified five-node regions with the
# mandatory oriented corners, then an exact z3 LP for a strict negative
# five-atom certificate. A miss is evidence only, never a theorem.
import random,json
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import z3
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def cub(r,lam):
 a,b,c=r;return [lam*a*b*c,-lam*(a*b+a*c+b*c),lam*(a+b+c),-lam]
def sig(r):return r[0]+r[1]+r[2],r[0]*r[1]+r[0]*r[2]+r[1]*r[2],r[0]*r[1]*r[2]
def make_box(R,Kc):
 (e1a,e1b),(o1a,o1b),(e2a,e2b),(o2a,o2b),(e3a,e3b),(o3a,o3b)=R
 em,ep,om,op=(e1a,e2b,e3a),(e1b,e2a,e3b),(o1a,o2b,o3a),(o1b,o2a,o3b)
 s1m,s2m,s3m=sig(em);s1p,s2p,s3p=sig(ep);lo=max(F(1),s2p/s2m);hi=min(s1p/s1m,s3p/s3m)
 if lo>hi:return None
 a1,a2,a3=sig(om);b1,b2,b3=sig(op)
 if not(b1>=a1 and b2<=a2 and b3>=a3):return None
 K=lo+(hi-lo)*Kc;Em,Ep,Om,Op=cub(em,K),cub(ep,F(1)),cub(om,F(1)),cub(op,F(1))
 if not all(Ep[i]-Em[i]>=0 and Op[i]-Om[i]>=0 for i in range(4)):return None
 return dict(E=(Em,Ep),O=(Om,Op),R=R)
def ev(c,t):return c[0]+c[1]*t+c[2]*t*t+c[3]*t**3
def lp(ts,rho,sx):
 x=[z3.Real('x%d'%k) for k in range(5)];S=z3.Solver();S.set(timeout=2000);q=lambda v:z3.Q(v.numerator,v.denominator)
 S.add(*[x[k]*sx[k]>0 for k in range(5)])
 for r in range(4):
  S.add((-1)**(r+1)*z3.Sum([x[k]*q(ts[k]**r) for k in range(5)])>0,(-1)**(r+1)*z3.Sum([x[k]*q(rho[k]*ts[k]**r) for k in range(5)])>0)
 return S.check()==z3.sat
# Sanity control: the pinned stable-polytope negative example must be detected.
raw=(root/'frontier-20261029-stable-polytope-five-atom-negative-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='eca087b6a3290627a12b8121c8359f12b5b4814a839500a7638f331f2de61bab';zp=json.loads(raw)
tsP=[F(w)**2 for w in zp['frequencies']];rhoP=[];sxP=[]
for i in range(5):
 Ec=cub((F(1,2),F(zp['E_middle_roots'][i]),F(5)),F(zp['even_scales'][i]));Oc=cub((F(zp['O_first_roots'][i]),F(9,2),F(7)),F(1));E=ev(Ec,tsP[i]);O=ev(Oc,tsP[i]);rhoP.append(tsP[i]*O/E);sxP.append(1 if E>0 else -1)
assert lp(tsP,rhoP,sxP)
rng=random.Random(20261029);boxes=[]
while len(boxes)<300:
 c=[];x=rng.uniform(0.05,1.0)
 for k in range(6):c.append(x);x*=rng.uniform(1.5,8.0)
 R=[]
 for k in range(6):
  left=c[k-1] if k else 0.0;right=c[k+1] if k<5 else 3*c[k]
  a=F(round((c[k]-rng.uniform(0,0.45)*(c[k]-left))*1000),1000);b=F(round((c[k]+rng.uniform(0,0.45)*(right-c[k]))*1000),1000);R.append((a,b))
 if not all(R[k][0]<R[k][1] for k in range(6)) or not all(R[k][1]<R[k+1][0] for k in range(5)) or R[0][0]<=0:continue
 bx=make_box(R,F(rng.randint(0,4),4))
 if bx:boxes.append(bx)
def sample(b,pat):
 (e1a,e1b),(o1a,o1b),(e2a,e2b),(o2a,o2b),(e3a,e3b),(o3a,o3b)=b['R'];r=lambda:rng.randint(0,1)
 u=lambda a,c:a+(c-a)*F(rng.randint(1,999),1000)
 if pat=='A':t1=u(o1a,o1b);t2=u(t1,o1b);t3=u(e2a,e2b);t4=u(t3,e2b);t5=u(o2b,e3a);cor=[(r(),0),(r(),1),(1,r()),(0,r()),(r(),r())];ex=[(-1,-1),(-1,1),(1,-1),(-1,-1),(1,1)]
 elif pat=='B':t1=u(o1a,o1b);t2=u(t1,o1b);t3=u(e2a,o2b);t4=u(e3a,e3b);t5=u(t4,e3b);cor=[(r(),0),(r(),1),(r(),r()),(0,r()),(1,r())];ex=[(-1,-1),(-1,1),(1,-1),(-1,1),(1,1)]
 else:t1=u(o1a,e2a);t2=u(o2a,o2b);t3=u(t2,o2b);t4=u(e3a,e3b);t5=u(t4,e3b);cor=[(r(),r()),(r(),1),(r(),0),(0,r()),(1,r())];ex=[(-1,-1),(1,1),(1,-1),(-1,1),(1,1)]
 ts=[t1,t2,t3,t4,t5]
 if not all(ts[i]<ts[i+1] for i in range(4)):return None
 rho=[];sx=[]
 for t,(ei,oi),(se,so) in zip(ts,cor,ex):
  E=ev(b['E'][ei],t);O=ev(b['O'][oi],t)
  if E*se<=0 or O*so<=0:return None
  rho.append(t*O/E);sx.append(se)
 return ts,rho,sx
stats={}
for pat in 'ABC':
 tested=hits=0
 for _ in range(3000):
  s=sample(boxes[rng.randrange(len(boxes))],pat)
  if s is None:continue
  tested+=1;hits+=lp(*s)
 stats[pat]={'tested':tested,'certificates':hits}
print({'eligible_boxes':len(boxes),'polytope_control_detected':True,'per_pattern':stats,'scope':'NONVERDICT sampling evidence'})
