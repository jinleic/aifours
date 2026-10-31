# Bounded exact LP on a larger actual-corner frequency grid.
# UNSAT/UNKNOWN is not a verdict outside this grid.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json,z3
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,h):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==h;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293');lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));cs=[]
for e in (-1,1):
 for o in (-1,1):cs.append([(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def row(a,t):return [sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0)/(1+t)**7 for j in range(8)]
ts={F(x) for x in ['1/100','1/10','1/3','1/2','3/4','9/10','1','11/10','3/2','2','3','10','50','90','100','101','110','200','500','1000','1998','2000','2002','3000','10000']}
for t in [F(1),F(3,2),F(100),F(101),F(2000)]:
 for d in (F(1,1000),F(1,100000)):
  ts.add(t*(1-d));ts.add(t*(1+d))
points=[(i,t) for i in range(4) for t in sorted(ts)];R=[row(cs[i],t) for i,t in points];W=[z3.Real('b1_broad_%d'%i) for i in range(len(points))];q=lambda x:z3.Q(x.numerator,x.denominator);S=z3.Solver();S.set(timeout=30000);S.add(*[x>=0 for x in W]);C=[sum(W[i]*q(R[i][j]) for i in range(len(points))) for j in range(8)];S.add(C[1]==1,*[C[j]<=0 for j in range(7) if j!=1],C[7]<=-310000);st=S.check();out={'target':1,'threshold':310000,'point_count':len(points),'status':str(st)}
if st==z3.sat:
 m=S.model();v=[F(m.eval(w).numerator_as_long(),m.eval(w).denominator_as_long()) for w in W];out['support']=[{'corner':points[i][0],'t':str(points[i][1]),'compactified_weight':str(v[i])} for i in range(len(v)) if v[i]>0];out['coordinates']=[str(sum(v[i]*R[i][j] for i in range(len(v)))) for j in range(8)]
text=json.dumps(out,sort_keys=True,indent=2)+'\n';(root/'frontier-20261029-b1-broad-atom-search-result-v1.json').write_text(text);print('b1 grid result',st,'points',len(points),'support',len(out.get('support',[])),'sha256',sha256(text.encode()).hexdigest())
