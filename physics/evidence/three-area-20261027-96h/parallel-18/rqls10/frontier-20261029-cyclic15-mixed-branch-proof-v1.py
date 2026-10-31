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
def realphase(a,d,k):
 phase=powers[(-8*k)%15];phase=phase if k%2==0 else neg(phase);v=mul(phase,powers[(-d*a)%15]);return tuple(x/2 for x in add(v,conj(v)))
def selfterms(S,d,k):
 piv,N=kernel(S,(0,5,-d,5-d));h=[realphase(a,d,k)for a in S];tr=[];de=[]
 for j in range(6):
  weight=ksum(mul(conj(N[j][a]),N[j][a])for a in range(2));tr.append((tuple(i for i in range(6)if i!=j),mul(h[j],weight)))
 for i,j in itertools.combinations(range(6),2):
  v=sub(mul(N[i][0],N[j][1]),mul(N[i][1],N[j][0]));de.append((tuple(k for k in range(6)if k not in (i,j)),mul(mul(h[i],h[j]),mul(v,conj(v)))))
 return piv,tr,de
# Branchwise combinations of short-pair imbalance, row collisions and positive planes.
assert 5*1920**2-4289**2==36479>0
def short_groups(S):
 out=[]
 for r in range(3):
  g=[j for j,a in enumerate(S)if a%3==r]
  if len(g)==2 and (S[g[1]]-S[g[0]])%15 in(3,12):out.append(g)
 return out
def transformation(S,branch):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];short=short_groups(S);assert len(short)==len(branch);choice={tuple(g):lo for g,lo in zip(short,branch)};T=[[F(0)for _ in range(6)]for _ in range(6)]
 for g in groups:
  if tuple(g)in choice:
   lo=choice[tuple(g)];assert lo in g;hi=next(j for j in g if j!=lo);T[lo][lo]=F(7,240);T[hi][lo]=F(73,240);T[hi][hi]=F(1,3)
  else:
   for j in g:T[j][j]=F(1,3)
 return T
def transform(S,terms,branch):
 T=transformation(S,branch);out={}
 for indices,val in terms:
  if val==Z:continue
  pieces=[([0]*6,val)]
  for i in indices:
   new=[]
   for arr,x in pieces:
    for j in range(6):
     if T[i][j]:bb=arr.copy();bb[j]+=1;new.append((bb,tuple(T[i][j]*v for v in x)))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=add(out.get(tuple(arr),Z),x)
 return out
def homog(S,poly,L):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];out={}
 for exp,val in poly.items():
  if val==Z:continue
  pieces=[(list(exp),val)]
  for g in groups:
   power=L-sum(exp[j]for j in g);assert power>=0;new=[]
   for cnt,fac in compositions(len(g),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(g,cnt):arr[j]+=k
     new.append((arr,tuple(fac*v for v in x)))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=add(out.get(tuple(arr),Z),x)
 return out
def checked_poly(S,terms,branch,L):
 poly=homog(S,transform(S,terms,branch),L);out=[]
 for ex,val in sorted(poly.items()):
  if val==Z:continue
  assert positive(val);out.append([list(ex),[str(x)for x in val]])
 assert out;return {'degree_per_residue':L,'positive_coefficients':out}
manifest=P/'frontier-20261029-cyclic15-13-residual-spectra-v1.json';raw=manifest.read_bytes();assert hashlib.sha256(raw).hexdigest()=='eea1390fac4544cab4500e8e3980fdf19285fe9ef30ac2b93900557383c52c7b';D=json.loads(raw);allowed={tuple(q['representative'])for q in D['remaining_spectrum_classes']};assert len(allowed)==13
A=(0,1,2,3,5,10);B=(0,1,2,4,9,11);C0=(0,1,3,5,8,10)
TARGETS=[(A,[((0,2),'self',2,25),((0,4),'cross',0,0),((3,2),'collision',0,0),((3,4),'self',7,13)]),
 (B,[((1,),'self',2,23),((3,),'self',7,29)]),
 (C0,[((0,3),'collision',0,0),((0,4),'self',2,24),((2,3),'self',7,14),((2,4),'collision',0,0)])]
records=[]
for S,branches in TARGETS:
 assert S in allowed;groups=short_groups(S);assert {tuple(b[0])for b in branches}==set(itertools.product(*groups));out=[]
 for branch,kind,d,k in branches:
  rec={'low_indices':branch,'kind':kind}
  if kind=='collision':
   highs=[next(j for j in g if j!=lo)for g,lo in zip(groups,branch)];pairs=[(i,j)for i,j in itertools.combinations(highs,2)if S[i]%5==S[j]%5];assert pairs;rec['high_collision_indices']=pairs[0]
  elif kind=='self':
   piv,tr,de=selfterms(S,d,k);rec.update({'d':d,'theta_pi_over_15':k,'pivots':piv,'trace':checked_poly(S,tr,branch,3),'determinant':checked_poly(S,de,branch,3)})
  else:
   assert kind=='cross';pl,pm,co=coefficients(S);ref=next(v for I,v in co if v!=Z);terms=[(tuple(j for j in range(6)if j not in I),mul(v,conj(ref)))for I,v in co]
   rec.update({'pivot_L':pl,'pivot_M':pm,'cross_determinant':checked_poly(S,terms,branch,2)})
  out.append(rec)
 records.append({'representative':S,'branches':out})
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'records':records,
 'scope':'three cyclic spectra, all imbalance branches rejected by self-plane, cross determinant, or high-population collision','status':'PRODUCED_UNREPLAYED'}
out=P/'frontier-20261029-cyclic15-mixed-branch-proof-v1.json';out.write_text(json.dumps(obj,separators=(',',':'))+'\n')
print(json.dumps({'source_sha256':obj['source_sha256'],'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':obj['clock_finish'],'proved_classes':len(records),'remaining_classes':len(allowed)-len(records),'status':'PRODUCED_UNREPLAYED'},indent=2))
