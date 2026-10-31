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
manifest=P/'frontier-20261029-cyclic15-40-residual-spectra-v1.json';raw=manifest.read_bytes();assert hashlib.sha256(raw).hexdigest()=='dd178c5ee25f214b97d843adbe5ed1fe93a0b8eccacb738fb09f1644ddc5a153';D=json.loads(raw);allowed={tuple(x['representative'])for x in D['remaining_spectrum_classes']};assert len(allowed)==40
TARGETS=[((0, 1, 2, 3, 4, 5), (9999, 1, 9999, 1, 9999, 1), (1, 1, 6910, 9999, 9999, 3090)), ((0, 1, 2, 3, 4, 6), (38, 52, 60, 14, 8, 8), (23, 1, 60, 34, 59, 3)), ((0, 1, 2, 3, 4, 7), (58, 14, 60, 2, 12, 34), (40, 8, 60, 20, 46, 6)), ((0, 1, 2, 3, 4, 9), (3, 22, 60, 38, 38, 19), (37, 6, 60, 5, 54, 18)), ((0, 1, 2, 3, 5, 8), (14, 60, 45, 46, 13, 2), (3, 60, 19, 57, 5, 36)), ((0, 1, 2, 3, 5, 10), (59, 15, 54, 1, 6, 45), (9, 35, 32, 51, 28, 25)), ((0, 1, 2, 3, 5, 11), (32, 60, 35, 28, 22, 3), (3, 60, 5, 57, 54, 1)), ((0, 1, 2, 3, 6, 8), (23, 60, 11, 16, 21, 49), (3, 60, 52, 23, 34, 8)), ((0, 1, 2, 3, 6, 10), (6, 45, 60, 33, 21, 15), (39, 11, 60, 5, 16, 49)), ((0, 1, 2, 3, 7, 8), (22, 28, 45, 38, 32, 15), (4, 50, 35, 56, 10, 25)), ((0, 1, 2, 3, 7, 10), (57, 37, 60, 3, 19, 4), (45, 26, 60, 15, 25, 9)), ((0, 1, 2, 3, 8, 9), (31, 60, 6, 4, 54, 25), (1, 60, 12, 4, 48, 55)), ((0, 1, 2, 4, 5, 7), (60, 1, 59, 30, 1, 29), (60, 1, 42, 35, 18, 24)), ((0, 1, 2, 4, 5, 9), (35, 24, 35, 36, 25, 25), (11, 55, 1, 5, 59, 49)), ((0, 1, 2, 4, 5, 10), (60, 17, 56, 41, 4, 2), (60, 15, 37, 18, 23, 27)), ((0, 1, 2, 4, 5, 13), (60, 45, 58, 2, 2, 13), (60, 29, 40, 9, 20, 22)), ((0, 1, 2, 4, 6, 7), (50, 6, 60, 50, 10, 4), (45, 50, 60, 3, 15, 7)), ((0, 1, 2, 4, 6, 9), (39, 40, 60, 20, 15, 6), (6, 5, 60, 55, 15, 39)), ((0, 1, 2, 4, 6, 10), (59, 13, 60, 36, 1, 11), (21, 22, 60, 26, 39, 12)), ((0, 1, 2, 4, 6, 11), (50, 42, 8, 18, 10, 52), (36, 3, 15, 57, 24, 45)), ((0, 1, 2, 4, 6, 12), (32, 44, 60, 16, 27, 1), (51, 6, 60, 54, 3, 6)), ((0, 1, 2, 4, 6, 13), (53, 35, 60, 18, 7, 7), (1, 34, 60, 19, 59, 7)), ((0, 1, 2, 4, 7, 12), (58, 41, 60, 14, 5, 2), (41, 3, 60, 48, 9, 19)), ((0, 1, 2, 4, 9, 11), (9999, 6910, 1, 3090, 1, 9999), (1, 9999, 1, 1, 9999, 9999)), ((0, 1, 2, 4, 9, 12), (17, 25, 60, 35, 20, 23), (45, 3, 60, 57, 5, 10)), ((0, 1, 2, 4, 10, 11), (60, 34, 57, 7, 19, 3), (60, 3, 23, 3, 54, 37)), ((0, 1, 2, 4, 10, 12), (56, 51, 60, 3, 6, 4), (13, 12, 60, 23, 25, 47)), ((0, 1, 2, 5, 7, 8), (60, 10, 4, 2, 50, 54), (60, 44, 41, 5, 16, 14)), ((0, 1, 2, 5, 7, 10), (60, 43, 58, 2, 1, 16), (60, 49, 11, 49, 2, 9)), ((0, 1, 2, 5, 7, 11), (60, 9, 31, 23, 51, 6), (60, 46, 46, 1, 14, 13)), ((0, 1, 2, 6, 7, 8), (58, 18, 53, 2, 42, 7), (22, 10, 23, 38, 50, 37)), ((0, 1, 2, 6, 8, 9), (14, 60, 4, 9, 56, 37), (12, 60, 41, 14, 19, 34)), ((0, 1, 2, 7, 8, 9), (3, 55, 56, 5, 4, 57), (22, 33, 39, 27, 21, 38)), ((0, 1, 3, 5, 6, 8), (1, 60, 36, 1, 23, 59), (35, 60, 24, 44, 1, 16)), ((0, 1, 3, 5, 7, 10), (15, 14, 45, 60, 13, 33), (1, 5, 59, 60, 12, 43)), ((0, 1, 3, 5, 7, 13), (46, 35, 14, 60, 2, 23), (2, 17, 58, 60, 23, 20)), ((0, 1, 3, 5, 8, 10), (9999, 9999, 1, 1, 9999, 1), (9999, 9999, 1, 9999, 1, 1)), ((0, 1, 3, 5, 10, 13), (37, 20, 23, 60, 28, 12), (5, 8, 55, 60, 28, 24)), ((0, 1, 3, 5, 11, 13), (1, 1, 9999, 5000, 5000, 9999), (9999, 1, 1, 1, 9999, 9999)), ((0, 1, 3, 6, 8, 13), (15, 56, 24, 21, 60, 4), (13, 8, 42, 5, 60, 52))]
records=[]
for S,negative,positive_counts in TARGETS:
 assert S in allowed;pl,pm,co=coefficients(S);ref=next(v for I,v in co if v!=Z);answers=[]
 for label,counts in [('negative',negative),('positive',positive_counts)]:
  groups=[sum(counts[j]for j,a in enumerate(S)if a%3==r)for r in range(3)];assert len(set(groups))==1 and min(counts)>0
  val=Z
  for I,v in co:
   ij=[j for j in range(6)if j not in I];val=add(val,tuple(counts[ij[0]]*counts[ij[1]]*x for x in mul(v,conj(ref))))
  assert conj(val)==val and (positive(val)if label=='positive'else positive(neg(val)))
  answers.append({'sign':label,'counts':counts,'group_count':groups[0],'value_phi15_basis':[str(x)for x in val]})
 records.append({'representative':S,'pivot_L':pl,'pivot_M':pm,'witnesses':answers})
assert len(records)==40 and {tuple(x['representative'])for x in records}==allowed
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'records':records,
 'scope':'opposite exact determinant-polynomial signs at two strictly positive U5-balanced populations per spectrum; not Gram realizations','status':'PRODUCED_UNREPLAYED'}
out=P/'frontier-20261029-cyclic15-crossplane-zero-proof-v1.json';out.write_text(json.dumps(obj,separators=(',',':'))+'\n')
print(json.dumps({'source_sha256':obj['source_sha256'],'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':obj['clock_finish'],'classes':len(records),'status':'PRODUCED_UNREPLAYED'},indent=2))
