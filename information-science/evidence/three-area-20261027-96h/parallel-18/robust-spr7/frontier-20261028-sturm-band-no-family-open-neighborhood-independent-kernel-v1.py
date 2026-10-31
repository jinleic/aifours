# Independent exact arithmetic replay of the explicit endpoint-neighborhood
# inequalities; the pinned anchor's stability/positive-pairing replay and
# pinned three-atom full-box replay are separate prerequisites.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 data=(root/name).read_bytes()
 if sha256(data).hexdigest()!=h:raise ValueError('PIN:'+name)
 return json.loads(data)
f=pin('frontier-20261028-sturm-band-no-family-open-neighborhood-frozen-v1.json','f6b46be8749712e19172764e0ae6274189b3d08daa6d1bf16234e5e421362ca0')
box=pin(f['source_box'],f['source_box_sha256']);positive=pin(f['positive_numerator_frozen'],f['positive_numerator_sha256']);ob=pin(f['three_atom_frozen'],f['three_atom_sha256'])
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));b=list(map(F,positive['b']));eps=F(f['radius'])
if not all(0<lo[j]<hi[j] for j in range(7)) or not all(v>0 for v in b) or b[7]!=1:raise ValueError('INPUT')
def corners(lo,hi):
 ret=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  ret.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return ret
cs=corners(lo,hi);C=[F(0)]*8;A=[F(0)]*8
for item in ob['support']:
 a=cs[item['corner']];t=F(item['t']);w=F(item['weight'])
 if t<=0 or w<=0:raise ValueError('ATOM')
 for k in range(8):
  for j in range(8):
   if (j+k)%2:continue
   sign=1 if ((k-j)//2)%2==0 else -1
   C[k]+=w*a[j]*sign*t**((j+k)//2)
   if j<7:A[k]+=w*t**((j+k)//2)
maxval=C[7]+sum(C[j]*(hi[j] if C[j]>0 else lo[j]) for j in range(7));M=-maxval
L=sum(abs(C[j]) for j in range(7))+sum(A[j]*(hi[j]+1) for j in range(7))+A[7]
delta=F(positive['compactified_pairing_minimum']);B=sum(b);width=min(hi[j]-lo[j] for j in range(7));lower=min(lo)
if M!=F(ob['full_box_maximum'])*(-1) or M!=F(f['obstruction_margin']) or L!=F(f['obstruction_lipschitz_bound']) or delta!=F(f['compactified_pairing_margin']) or B!=F(f['numerator_coefficient_sum']) or width!=F(f['minimum_width']) or lower!=F(f['minimum_lower']):raise ValueError('RECOMPUTATION')
checks=[eps<=1,4*eps<=width,2*eps<=lower,14*eps*B<=delta,2*eps*L<=M]
if not all(checks):raise ValueError('NEIGHBORHOOD_BOUND')
print('independent open-neighborhood replay:',{'radius':str(eps),'endpoint_dimensions':14,'exact_inequalities':len(checks),'all_hold':all(checks),'compactified_pairing_margin':str(delta),'obstruction_margin':str(M),'scope':'every endpoint-perturbed box has fixed external common numerator but no normalized common numerator inside itself'})
