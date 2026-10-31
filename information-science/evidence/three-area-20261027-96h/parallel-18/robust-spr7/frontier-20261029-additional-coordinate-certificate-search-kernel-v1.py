# Bounded exact physical-atom LP for two further forced-coordinate leads.
# UNSAT/UNKNOWN here is only for this finite grid, not an original verdict.
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json,z3
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));cs=[]
for e in (-1,1):
 for o in (-1,1):cs.append([(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def row(a,t):return [sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0)/(1+t)**7 for j in range(8)]
base=load('frontier-20261029-universal-simple-odd-halfspace-frozen-v1.json','3891b2e8ee1e2405573dc0aaf9f1194a8909948988e3e24e2e20a14790a5e8bf')['support'];points={(a['corner'],F(a['t'])) for a in base}
for ci,t in [(2,F(1)),(3,F(3,2)),(1,F(100)),(0,F(101)),(2,F(2000))]:
 for d in [F(1,10),F(1,100),F(1,1000),F(1,10000),F(1,100000),F(1,1000000)]:
  points.add((ci,t*(1-d)));points.add((ci,t*(1+d)))
points=sorted(points);rs=[row(cs[ci],t) for ci,t in points]
q=lambda v:z3.Q(v.numerator,v.denominator)
for j,T in [(1,310000),(2,11000)]:
 W=[z3.Real('coordinate_%d_atom_%d'%(j,i)) for i in range(len(points))];S=z3.Solver();S.set(timeout=8000);S.add(*[v>=0 for v in W]);C=[sum(W[i]*q(rs[i][k]) for i in range(len(points))) for k in range(8)];S.add(C[j]==1,*[C[k]<=0 for k in range(7) if k!=j],C[7]<=-T);st=S.check();out={'target':j,'threshold':T,'point_count':len(points),'status':str(st)}
 if st==z3.sat:
  m=S.model();L=[F(m.eval(x).numerator_as_long(),m.eval(x).denominator_as_long()) for x in W];out['support']=[{'corner':points[i][0],'t':str(points[i][1]),'compactified_weight':str(v)} for i,v in enumerate(L) if v>0];out['coordinates']=[str(sum(L[i]*rs[i][k] for i in range(len(points)))) for k in range(8)]
 text=json.dumps(out,sort_keys=True,indent=2)+'\n';path=root/('frontier-20261029-additional-coordinate-certificate-target-%d-v1.json'%j);path.write_text(text);print('additional exact coordinate grid',j,str(st),'points',len(points),'support',len(out.get('support',[])),'sha256',sha256(text.encode()).hexdigest())
