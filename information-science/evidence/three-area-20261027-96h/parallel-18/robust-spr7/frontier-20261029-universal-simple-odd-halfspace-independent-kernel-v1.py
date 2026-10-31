# Exact replay without search/cofactor helpers: signed monomial accumulation,
# integer Bareiss Hurwitz minors, and direct Sturm half-line positivity.
from fractions import Fraction as F
from math import lcm
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==digest;return json.loads(raw)
box=load('frontier-20261029-seven-dimensional-span-obstruction-frozen-v2.json','3af1b353e3c811b1c39778491407e5ef9e162ebe187c683eda522520b3120293')
z=load('frontier-20261029-universal-simple-odd-halfspace-frozen-v1.json','3891b2e8ee1e2405573dc0aaf9f1194a8909948988e3e24e2e20a14790a5e8bf')
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));assert all(0<lo[j]<hi[j] for j in range(7))
cs=[]
for e in (-1,1):
 for o in (-1,1):
  a=[]
  for j in range(7):
   choice=e if j%2==0 else o
   a.append(hi[j] if choice==(-1)**(j//2) else lo[j])
  cs.append(a+[F(1)])
def monomial(a,j,t):
 return sum(a[k]*((-1)**((j+k)//2+k))*t**((j+k)//2) for k in range(8) if (j+k)%2==0)
def direct_poly(a,b):
 p=[F(0)]*8
 for j in range(8):
  for k in range(8):
   if (j+k)%2==0:p[(j+k)//2]+=b[j]*a[k]*((-1)**((j+k)//2+k))
 return p
def determinant(A):
 A=[x[:] for x in A];n=len(A);sign=1;previous=1
 for k in range(n-1):
  p=next((i for i in range(k,n) if A[i][k]),None)
  if p is None:return 0
  if p!=k:A[p],A[k]=A[k],A[p];sign=-sign
  pivot=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=A[i][j]*pivot-A[i][k]*A[k][j];assert x%previous==0;A[i][j]=x//previous
   A[i][k]=0
  previous=pivot
 return sign*A[-1][-1]
def hurwitz(a):
 D=lcm(*(x.denominator for x in a));v=[int(x*D) for x in a[::-1]];H=[[v[2*j-i+1] if 0<=2*j-i+1<8 else 0 for j in range(7)] for i in range(7)]
 return [determinant([row[:k] for row in H[:k]]) for k in range(1,8)]
assert all(d>0 for a in cs for d in hurwitz(a))
support=z['support'];assert len(support)==8 and all(F(at['t'])>0 and int(at['weight'])>0 and 0<=at['corner']<4 for at in support)
C=[sum(F(at['weight'])*monomial(cs[at['corner']],j,F(at['t'])) for at in support) for j in range(8)]
assert C[3]>0 and all(C[j]==0 for j in (0,1,2,4,6)) and C[5]==-97*C[3]
gap=hi[3]-97*lo[5];assert gap==F(z['threshold_hi3_minus_97lo5'])==F(20699999551,100000000)
assert C[7]==-gap*C[3] and [str(c/C[3]) for c in C]==z['expected_normalized_monomial_coordinates']
def trim(p):
 p=p[:]
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def rem(p,q):
 p=trim(p);q=trim(q)
 while len(p)>=len(q) and p!=[0]:
  offset=len(p)-len(q);factor=p[-1]/q[-1]
  for i in range(len(q)):p[offset+i]-=factor*q[i]
  p=trim(p)
 return p
def variations(seq):
 signs=[1 if x>0 else -1 for x in seq if x];return sum(x!=y for x,y in zip(signs,signs[1:]))
def no_positive_roots(p):
 p=trim(p);d=[i*p[i] for i in range(1,len(p))];chain=[p,trim(d)]
 while chain[-1]!=[0]:
  x=rem(chain[-2],chain[-1])
  if x==[0]:break
  chain.append(trim([-q/abs(x[-1]) for q in x]))
 return variations([q[0] for q in chain]),variations([q[-1] for q in chain])
good=list(map(F,box['good_numerator']));assert good[7]>0 and all(x>0 for x in good)
checks=[]
for a in cs:
 p=direct_poly(a,good);assert p[0]>0 and p[-1]>0;v0,vi=no_positive_roots(p);assert v0==vi;checks.append((v0,vi))
assert good[3]-97*good[5]-gap*good[7]>0
# Mutation controls: a negative weight and a perturbed atom must both be caught.
assert -int(support[0]['weight'])<0
mut=F(support[0]['t'])+F(1,10**7)
C0new=C[0]+int(support[0]['weight'])*(monomial(cs[support[0]['corner']],0,mut)-monomial(cs[support[0]['corner']],0,F(support[0]['t'])))
assert C0new!=0
print({'positive_weights':8,'positive_Hurwitz_minors':28,'zero_coordinates':[0,1,2,4,6],'exact_halfspace':'b3 - 97*b5 > 20699999551/100000000 * b7','independent_good_sturm_variations':checks,'mutation_controls':2})
