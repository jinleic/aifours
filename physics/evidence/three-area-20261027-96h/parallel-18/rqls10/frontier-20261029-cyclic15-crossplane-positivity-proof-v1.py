#!/usr/bin/env python3
"""Cyclotomic resultant witnesses for 5 distinct supported eigenvalues."""
import collections,datetime,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
Z=(F(0),)*8;O=(F(1),)+(F(0),)*7;phi=[1,-1,0,1,-1,1,0,-1,1]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 q=[F(0)]*15
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:q[i+j]+=x*y
 for k in range(14,7,-1):
  v=q[k]
  if v:
   for j in range(8):q[k-8+j]-=v*phi[j]
 return tuple(q[:8])
r=(F(0),F(1))+(F(0),)*6;powers=[O]
for _ in range(15):powers.append(mul(powers[-1],r))
assert powers[15]==O and len(set(powers[:15]))==15
C=[add(O,powers[k])for k in range(15)];Inv=[]
for k in range(15):
 q=Z
 for j in range(15):q=add(q,powers[k*j%15]if j%2==0 else neg(powers[k*j%15]))
 q=tuple(x/2 for x in q);assert mul(C[k],q)==O;Inv.append(q)
def conj(x):
 q=Z
 for j,c in enumerate(x):
  if c:q=add(q,tuple(c*y for y in powers[-j%15]))
 return q
# Exact 4x4 determinants and cofactor kernel bases in Q(zeta15).
def ksum(vals):
 q=Z
 for x in vals:q=add(q,x)
 return q
def det(A):
 n=len(A);q=Z
 for perm in itertools.permutations(range(n)):
  v=O
  for i,j in enumerate(perm):v=mul(v,A[i][j])
  parity=sum(perm[i]>perm[j]for i in range(n)for j in range(i+1,n))%2;q=add(q,neg(v)if parity else v)
 return q
def kernel(S,exponents):
 V=[[powers[(d*a)%15]for a in S]for d in exponents]
 for piv in itertools.combinations(range(6),4):
  D=det([[V[i][j]for j in piv]for i in range(4)])
  if D!=Z:break
 else:raise AssertionError('rank deficient')
 free=[j for j in range(6)if j not in piv];N=[[Z,Z]for _ in range(6)]
 for k,f in enumerate(free):
  N[f][k]=D
  for i,col in enumerate(piv):
   t=list(piv);t[i]=f;N[col][k]=neg(det([[V[r][j]for j in t]for r in range(4)]))
 assert all(ksum(mul(V[r][j],N[j][k])for j in range(6))==Z for r in range(4)for k in range(2))
 return piv,N
def coefficients(S):
 pL,L=kernel(S,(0,5,-2,3));pM,M=kernel(S,(0,5,-7,-2));V=[[powers[(d*a)%15]for a in S]for d in (0,-7,2,-5)]
 R=[[mul(conj(L[j][a]),M[j][b])for a in range(2)for b in range(2)]for j in range(6)]
 out=[]
 for I in itertools.combinations(range(6),4):out.append((I,mul(det([[V[r][j]for j in I]for r in range(4)]),det([R[j]for j in I]))))
 return pL,pM,out
def atan_bounds(x,n):
 q=F(0)
 for k in range(n):q+=(-1)**k*x**(2*k+1)/(2*k+1)
 rem=(-1)**n*x**(2*n+1)/(2*n+1);return min(q,q+rem),max(q,q+rem)
a0,a1=atan_bounds(F(1,5),40);b0,b1=atan_bounds(F(1,239),20);pi_lo,pi_hi=16*a0-4*b1,16*a1-4*b0
def cos_bounds(x,n=45):
 q=F(0)
 for k in range(n):q+=(-1)**k*x**(2*k)/math.factorial(2*k)
 rem=(-1)**n*x**(2*n)/math.factorial(2*n);return min(q,q+rem),max(q,q+rem)
COS=[(F(1),F(1))]+[(cos_bounds(2*j*pi_hi/15)[0],cos_bounds(2*j*pi_lo/15)[1])for j in range(1,8)]
def positive(q):
 assert conj(q)==q;lo=F(0)
 for x,(l,h)in zip(q,COS):lo+=x*(l if x>=0 else h)
 return lo>0
def compositions(n,k):
 if n==1:return [((k,),1)]
 out=[]
 for a in range(k+1):
  for b,m in compositions(n-1,k-a):out.append(((a,)+b,math.comb(k,a)*m))
 return out
def expand(S,coef,L,orientation):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];ref=next(v for I,v in coef if v!=Z);out={}
 for I,v in coef:
  if v==Z:continue
  pair=[j for j in range(6)if j not in I];e=[0]*6
  for j in pair:e[j]+=1
  c=mul(v,conj(ref));c=c if orientation>0 else neg(c);assert conj(c)==c;pieces=[(e,c)]
  for group in groups:
   k=L-sum(e[j]for j in group);assert k>=0;new=[]
   for count,weight in compositions(len(group),k):
    for q,val in pieces:
     qq=q.copy()
     for i,w in zip(group,count):qq[i]+=w
     factor=weight*3**k;new.append((qq,tuple(factor*x for x in val)))
   pieces=new
  for q,val in pieces:
   key=tuple(q);out[key]=add(out.get(key,Z),val)
 return out
manifest=P/'frontier-20261029-cyclic15-residual-spectra-v1.json';raw=manifest.read_bytes();assert hashlib.sha256(raw).hexdigest()=='8a34864e6a25a22a8eb01e7c2acafaa1ad2c01c8cd1867fb02f536ee80a1fce0';M=json.loads(raw);allowed={tuple(x['representative'])for x in M['all_orbit_records']if not x['excluded_two_3cosets']};assert len(allowed)==78
TARGETS=[((0, 1, 2, 3, 4, 8), 2, 1), ((0, 1, 2, 3, 5, 6), 2, 1), ((0, 1, 2, 3, 5, 7), 4, 1), ((0, 1, 2, 3, 5, 9), 2, 1), ((0, 1, 2, 3, 5, 12), 2, 1), ((0, 1, 2, 3, 5, 13), 2, 1), ((0, 1, 2, 3, 6, 7), 2, 1), ((0, 1, 2, 3, 6, 11), 2, 1), ((0, 1, 2, 3, 7, 9), 2, 1), ((0, 1, 2, 3, 7, 11), 2, 1), ((0, 1, 2, 3, 8, 10), 2, 1), ((0, 1, 2, 4, 5, 6), 3, 1), ((0, 1, 2, 4, 5, 8), 2, 1), ((0, 1, 2, 4, 5, 11), 2, 1), ((0, 1, 2, 4, 5, 12), 2, -1), ((0, 1, 2, 4, 6, 8), 2, 1), ((0, 1, 2, 4, 7, 8), 3, -1), ((0, 1, 2, 4, 7, 9), 3, 1), ((0, 1, 2, 4, 8, 10), 3, -1), ((0, 1, 2, 4, 9, 10), 3, 1), ((0, 1, 2, 5, 6, 7), 2, 1), ((0, 1, 2, 5, 6, 8), 2, 1), ((0, 1, 2, 5, 6, 10), 2, 1), ((0, 1, 2, 5, 6, 11), 2, 1), ((0, 1, 2, 5, 6, 12), 2, 1), ((0, 1, 2, 5, 7, 12), 2, 1), ((0, 1, 2, 5, 8, 10), 2, 1), ((0, 1, 2, 5, 10, 11), 2, 1), ((0, 1, 2, 6, 7, 9), 2, 1), ((0, 1, 2, 6, 7, 11), 2, 1), ((0, 1, 2, 6, 8, 10), 2, 1), ((0, 1, 2, 6, 8, 11), 2, 1), ((0, 1, 2, 7, 8, 10), 3, -1), ((0, 1, 3, 5, 6, 10), 2, 1), ((0, 1, 3, 5, 7, 8), 2, 1), ((0, 1, 3, 5, 8, 13), 2, 1), ((0, 1, 3, 5, 10, 11), 2, 1), ((0, 1, 3, 6, 8, 10), 3, 1)]
records=[]
for S,L,orientation in TARGETS:
 assert S in allowed;pl,pm,co=coefficients(S);poly=expand(S,co,L,orientation);positive_poly=[]
 for exp,value in sorted(poly.items()):
  if value==Z:continue
  assert positive(value);positive_poly.append([list(exp),[str(x)for x in value]])
 assert positive_poly;records.append({'representative':list(S),'degree_per_residue':L,'orientation':orientation,'pivot_L':list(pl),'pivot_M':list(pm),'positive_coefficients':positive_poly})
assert len(records)==38 and len({tuple(x['representative'])for x in records})==38
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'records':records,
 'scope':'38 cyclic spectrum classes; positive determinant for all strictly positive U5-balanced populations','status':'PRODUCED_UNREPLAYED'}
out=P/'frontier-20261029-cyclic15-crossplane-positivity-proof-v1.json';out.write_text(json.dumps(obj,separators=(',',':'))+'\n')
print(json.dumps({'source_sha256':obj['source_sha256'],'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':obj['clock_finish'],'proved_classes':len(records),'remaining_classes':len(allowed)-len(records),'status':'PRODUCED_UNREPLAYED'},indent=2))
