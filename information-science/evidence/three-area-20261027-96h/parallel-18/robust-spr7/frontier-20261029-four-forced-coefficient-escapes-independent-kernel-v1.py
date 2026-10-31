# Reconstruct four positive actual-atom sums directly in the monomial basis.
# Check full-rank zero-coordinate pivots needed for open persistence.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
z=load('frontier-20261029-four-forced-coefficient-escapes-frozen-v1.json','0880f38b67095511ce397296b19bc978a8fdb7a4a14255488fb95232a4268e28')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));good=list(map(F,box['good_numerator']));assert all(0<lo[j]<hi[j] for j in range(7)) and good[7]>0
corners=[]
for e in (-1,1):
 for o in (-1,1):corners.append([(hi[j] if (e if j%2==0 else o)==(-1)**(j//2) else lo[j]) for j in range(7)]+[F(1)])
def row(a,t):
 return [sum(a[k]*(-1)**((j+k)//2+k)*t**((j+k)//2) for k in range(8) if (j+k)%2==0) for j in range(8)]
def det(M):
 A=[row[:] for row in M];n=len(A);d=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if A[i][k]),None)
  if p is None:return F(0)
  if p!=k:A[p],A[k]=A[k],A[p];d=-d
  v=A[k][k];d*=v
  for i in range(k+1,n):
   f=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=f*A[k][j]
 return d
expected={3:(211000,210000),4:(1000000,900000),5:(2150,2140),6:(909,900)}
assert len(z['certificates'])==4
out=[]
for cert in z['certificates']:
 j=cert['target_index'];T,Topen=expected[j];assert (cert['anchor_threshold'],cert['open_threshold'])==(T,Topen)
 atoms=cert['atoms'];assert all(0<=a['corner']<4 and F(a['t'])>0 and int(a['weight'])>0 for a in atoms)
 rows=[row(corners[a['corner']],F(a['t'])) for a in atoms];weights=[int(a['weight']) for a in atoms];C=[sum(weights[i]*rows[i][k] for i in range(len(rows))) for k in range(8)]
 assert list(map(str,C))==cert['aggregate_coordinates'] and C[j]>0
 zeros=[k for k in range(7) if k!=j and C[k]==0];negative=[k for k in range(7) if k!=j and C[k]<0]
 assert zeros==cert['zero_coordinate_indices'] and negative==cert['negative_coordinate_indices'] and len(zeros)+len(negative)==6
 assert C[7]+T*C[j]<=0 and C[7]+Topen*C[j]<0 and C[7]+(T+1)*C[j]>0
 assert hi[j]<Topen and good[j]>T*good[7]
 piv=cert['pivot_atom_positions'];assert len(piv)==len(zeros) and len(set(piv))==len(piv) and all(0<=p<len(atoms) for p in piv)
 assert det([[rows[p][k] for p in piv] for k in zeros])!=0
 assert not all(v>0 for v in [-weights[0]]+weights[1:])
 out.append({'coefficient':j,'positive_atoms':len(atoms),'zero_rank':len(zeros),'strict_negative_coordinates':negative,'anchor_lower_bound':T,'open_lower_bound':Topen})
print({'independent_bounds':out,'positive_numerator_witness_satisfies_all':True,'negative_weight_controls':4})
