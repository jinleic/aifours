# Independent monomial-convolution and integer-Bareiss replay. The finite
# certificate excludes numerators inside the whole coefficient box only.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pinned(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return json.loads(raw)
f=pinned('frontier-20261028-sturm-band-full-box-obstruction-frozen-v1.json','5bc88140adab434f8cfb59a32640e49af34483bad6c0ae1da7c50b8f172fee92')
g=pinned(f['box_file'],f['box_sha256']);good=pinned(f['known_common_numerator_file'],f['known_common_numerator_sha256'])
lo=list(map(F,g['lower']));hi=list(map(F,g['upper']));b=list(map(F,good['b']))
if not all(0<lo[j]<hi[j] for j in range(7)) or b[7]!=1 or not all(x>0 for x in b):raise ValueError('BOUNDS')
def corners(lo,hi):
 ret=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  ret.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return ret
cs=corners(lo,hi)
def det(A):
 n=len(A);den=lcm(*(v.denominator for row in A for v in row));M=[[int(v*den) for v in row] for row in A];prev=1;sgn=1
 for k in range(n-1):
  if not M[k][k]:
   r=next((r for r in range(k+1,n) if M[r][k]),None)
   if r is None:return F(0)
   M[r],M[k]=M[k],M[r];sgn=-sgn
  pivot=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=M[i][j]*pivot-M[i][k]*M[k][j]
    if x%prev:raise ValueError('BAREISS')
    M[i][j]=x//prev
  for i in range(k+1,n):M[i][k]=0
  prev=pivot
 return F(sgn*M[-1][-1],den**n)
for a in cs:
 H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
 for n in range(1,8):
  if det([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
def monomial_row(a,t):
 out=[]
 for k in range(8):
  v=F(0)
  for j in range(8):
   if (j+k)%2:continue
   sign=1 if ((k-j)//2)%2==0 else -1
   v+=a[j]*sign*t**((j+k)//2)
  out.append(v)
 return out
C=[F(0)]*8
for item in f['support']:
 v=monomial_row(cs[item['corner']],F(item['t']));w=F(item['weight'])
 if w<=0:raise ValueError('WEIGHT')
 for j in range(8):C[j]+=w*v[j]
signs=['+' if v>0 else '-' if v<0 else '0' for v in C]
if signs!=f['coefficient_signs']:raise ValueError('COORDINATE_SIGNS')
good_sum=sum(C[j]*b[j] for j in range(8))
if good_sum!=F(f['known_good_numerator_sum']) or good_sum<=0:raise ValueError('GOOD_NUMERATOR_SUM')
maximizer=[hi[j] if C[j]>0 else lo[j] for j in range(7)]+[F(1)]
maximum=sum(C[j]*maximizer[j] for j in range(8))
if maximum!=F(f['full_box_maximum']) or maximum>=0:raise ValueError('FULL_BOX_MAXIMUM')
if ['upper' if C[j]>0 else 'lower' for j in range(7)]!=f['full_box_maximizer_sides']:raise ValueError('MAXIMIZER')
print('full-box numerator obstruction replay:',{'hurwitz_minors':28,'positive_atoms':len(f['support']),'coordinate_signs':signs,'exact_full_box_maximum':str(maximum),'known_good_numerator_sum':str(good_sum),'scope':'no monic numerator in this stable coefficient box; an unrestricted common numerator exists'})
