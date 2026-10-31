# Exact independent convolution and dyadic Bernstein replay of V−H>0.
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-resonant-norm-gap-example-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='10fcfca76926f093603e28740f9e20b3c89fef092110c285190c74680d1f2b17':raise ValueError('PIN')
f=json.loads(raw);a=list(map(F,f['center']));r=list(map(F,f['radii']))
def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
E=[a[0],-a[2],a[4],-a[6]];O=[a[1],-a[3],a[5],-a[7]];A=[r[j] for j in (0,2,4,6)];B=[r[j] for j in (1,3,5)];V=mul(E,E)+[F(0)];H=mul(A,A)+[F(0)]
for j,x in enumerate(mul(O,O)):V[j+1]+=x
for j,x in enumerate(mul(B,B)):H[j+1]+=x
D=[x-y for x,y in zip(V,H)]
if list(map(str,D))!=f['V_minus_H_coefficients'] or sum(x<0 for x in D)!=f['negative_power_coefficients']:raise ValueError('CONVOLUTION')
def split(v):
 rows=[v]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [r[0] for r in rows],[r[-1] for r in rows[::-1]]
def leaf(a,b):
 n=len(D)-1;v=[D[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return v
  m=(l+r)/2;L,R=split(v)
  if b<=m:r=m;v=L
  elif a>=m:l=m;v=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('DEPTH')
last=F(0);minimum=None;count=0
for l,r in sorted(f['frequency_leaves'],key=lambda x:F(x[0])):
 l,r=F(l),F(r)
 if l!=last or l>=r:raise ValueError('COVER')
 z=leaf(l,r)
 if not all(v>0 for v in z):raise ValueError('SIGN')
 minimum=min(z) if minimum is None else min(minimum,min(z));last=r;count+=len(z)
if last!=1 or minimum!=F(f['compactified_gap']):raise ValueError('MARGIN')
print('resonant norm-gap independent replay:',{'negative_power_coefficients':f['negative_power_coefficients'],'strict_compactified_bernstein_coefficients':count,'compactified_gap':str(minimum),'scope':'Cauchy norm-gap suffices for the separately pinned resonant stable box; no universal arbitrary-box conclusion'})
