#!/usr/bin/env python3
"""Independent field-basis replay for mixed cyclic imbalance branches."""
import collections,datetime,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cyclic15-mixed-branch-proof-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='72c51e1e752a0fbb7a1ce48fb93a4f59d0c7a0fcfb69330457a4ba8973e447ab';D=json.loads(raw)
manifest=P/'frontier-20261029-cyclic15-13-residual-spectra-v1.json';mr=manifest.read_bytes();assert hashlib.sha256(mr).hexdigest()=='eea1390fac4544cab4500e8e3980fdf19285fe9ef30ac2b93900557383c52c7b';MM=json.loads(mr)
z=(F(0),F(0));o=(F(1),F(0))
def a(x,y):return(x[0]+y[0],x[1]+y[1])
def n(x):return(-x[0],-x[1])
def s(x,y):return a(x,n(y))
def m(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def oa(x,y):return(a(x[0],y[0]),a(x[1],y[1]))
def on(x):return(n(x[0]),n(x[1]))
def om(x,y):
 ac=m(x[0],y[0]);bd=m(x[1],y[1]);return(s(ac,bd),s(a(m(x[0],y[1]),m(x[1],y[0])),bd))
c=(F(-1,2),F(1,2))
def km(x,y):
 ac=om(x[:2],y[:2]);bd=om(x[2:],y[2:]);bc=om(x[2:],y[:2]);ad=om(x[:2],y[2:]);cbd=(m(c,bd[0]),m(c,bd[1]));return oa(ac,on(bd))+oa(oa(ad,bc),cbd)
Z=(z,z,z,z);O=(o,z,z,z)
def ka(x,y):return tuple(a(v,w)for v,w in zip(x,y))
def kn(x):return tuple(n(v)for v in x)
def conj(x):
 A,B,C,D=x;return(s(a(s(A,B),m(c,C)),m(c,D)),s(n(B),m(c,D)),s(D,C),D)
def scale(x,k):return tuple((v[0]*k,v[1]*k)for v in x)
zeta=(o,o,n(c),n(c));powers=[O]
for _ in range(15):powers.append(km(powers[-1],zeta))
assert powers[15]==O and conj(zeta)==powers[14]
def summ(xs):
 q=Z
 for x in xs:q=ka(q,x)
 return q
def det(A):
 N=len(A);q=Z
 for perm in itertools.permutations(range(N)):
  v=O
  for i,j in enumerate(perm):v=km(v,A[i][j])
  parity=sum(perm[i]>perm[j]for i in range(N)for j in range(i+1,N))%2;q=ka(q,kn(v)if parity else v)
 return q
def kernel(S,exps,piv):
 assert len(piv)==4 and len(set(piv))==4;V=[[powers[(d*x)%15]for x in S]for d in exps];D=det([[V[i][j]for j in piv]for i in range(4)]);assert D!=Z
 free=[j for j in range(6)if j not in piv];N=[[Z,Z]for _ in range(6)]
 for k,f in enumerate(free):
  N[f][k]=D
  for i,j in enumerate(piv):
   q=list(piv);q[i]=f;N[j][k]=kn(det([[V[r][x]for x in q]for r in range(4)]))
 assert all(summ(km(V[r][j],N[j][k])for j in range(6))==Z for r in range(4)for k in range(2));return N
def coeffs(S,pL,pM):
 L=kernel(S,(0,5,-2,3),pL);M=kernel(S,(0,5,-7,-2),pM);E=[[powers[(d*x)%15]for x in S]for d in (0,-7,2,-5)]
 R=[[km(conj(L[j][a0]),M[j][b])for a0 in range(2)for b in range(2)]for j in range(6)]
 return [(I,km(det([[E[r][j]for j in I]for r in range(4)]),det([R[j]for j in I])))for I in itertools.combinations(range(6),4)]

def ks(x,y):return ka(x,kn(y))
def comps(n,k):
 if n==1:return [((k,),1)]
 q=[]
 for i in range(k+1):
  for rest,v in comps(n-1,k-i):q.append(((i,)+rest,math.comb(k,i)*v))
 return q
def expand(S,coef,L,orient):
 groups=[[j for j,x in enumerate(S)if x%3==r]for r in range(3)];ref=next(v for I,v in coef if v!=Z);out={}
 for I,v in coef:
  if v==Z:continue
  ex=[0]*6
  for j in range(6):
   if j not in I:ex[j]+=1
  val=km(v,conj(ref));val=val if orient>0 else kn(val);assert conj(val)==val;pieces=[(ex,val)]
  for g in groups:
   power=L-sum(ex[j]for j in g);assert power>=0;new=[]
   for cs,weight in comps(len(g),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(g,cs):arr[j]+=k
     new.append((arr,scale(x,weight*3**power)))
   pieces=new
  for arr,x in pieces:
   key=tuple(arr);out[key]=ka(out.get(key,Z),x)
 return out
# Rational enclosures via Machin's identity and alternating Taylor bounds.
def atan_bound(x,N):
 total=sum(((-1)**k*x**(2*k+1)/(2*k+1)for k in range(N)),F(0));rem=(-1)**N*x**(2*N+1)/(2*N+1);return min(total,total+rem),max(total,total+rem)
a0,a1=atan_bound(F(1,5),42);b0,b1=atan_bound(F(1,239),22);pl,ph=16*a0-4*b1,16*a1-4*b0
def cb(x,N=47):
 total=sum(((-1)**k*x**(2*k)/math.factorial(2*k)for k in range(N)),F(0));rem=(-1)**N*x**(2*N)/math.factorial(2*N);return min(total,total+rem),max(total,total+rem)
cos=[(F(1),F(1))]+[(cb(2*j*ph/15)[0],cb(2*j*pl/15)[1])for j in range(1,8)]
def positive_phi(v):
 lo=F(0)
 for x,(l,h)in zip(v,cos):lo+=x*(l if x>=0 else h)
 return lo>0
def phase_real(a0,d,k):
 ph=powers[(-8*k)%15];ph=ph if k%2==0 else kn(ph);v=km(ph,powers[(-d*a0)%15]);return scale(ka(v,conj(v)),F(1,2))
def selfterms(S,d,k,piv):
 N=kernel(S,(0,5,-d,5-d),piv);h=[phase_real(x,d,k)for x in S];tr=[];de=[]
 for j in range(6):tr.append((tuple(x for x in range(6)if x!=j),km(h[j],summ(km(conj(N[j][b]),N[j][b])for b in range(2)))))
 for i,j in itertools.combinations(range(6),2):
  v=ks(km(N[i][0],N[j][1]),km(N[i][1],N[j][0]));de.append((tuple(x for x in range(6)if x not in(i,j)),km(km(h[i],h[j]),km(v,conj(v)))))
 return tr,de
assert 5*1920**2-4289**2==36479>0
def short_groups(S):
 out=[]
 for r in range(3):
  g=[j for j,a in enumerate(S)if a%3==r]
  if len(g)==2 and (S[g[1]]-S[g[0]])%15 in(3,12):out.append(g)
 return out
def transform(S,terms,branch):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];ss=short_groups(S);assert len(ss)==len(branch);choices={tuple(g):lo for g,lo in zip(ss,branch)};T=[[F(0)for _ in range(6)]for _ in range(6)]
 for g in groups:
  if tuple(g)in choices:
   lo=choices[tuple(g)];assert lo in g;hi=next(j for j in g if j!=lo);T[lo][lo]=F(7,240);T[hi][lo]=F(73,240);T[hi][hi]=F(1,3)
  else:
   for j in g:T[j][j]=F(1,3)
 out={}
 for indices,val in terms:
  if val==Z:continue
  pieces=[([0]*6,val)]
  for i in indices:
   new=[]
   for arr,x in pieces:
    for j in range(6):
     if T[i][j]:bb=arr.copy();bb[j]+=1;new.append((bb,scale(x,T[i][j])))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=ka(out.get(tuple(arr),Z),x)
 return out
def homog(S,poly,L):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];out={}
 for exp,val in poly.items():
  if val==Z:continue
  pieces=[(list(exp),val)]
  for g in groups:
   power=L-sum(exp[j]for j in g);assert power>=0;new=[]
   for cnt,fac in comps(len(g),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(g,cnt):arr[j]+=k
     new.append((arr,scale(x,fac)))
   pieces=new
  for arr,x in pieces:out[tuple(arr)]=ka(out.get(tuple(arr),Z),x)
 return out
def check_poly(S,terms,branch,record):
 global signs
 poly=homog(S,transform(S,terms,branch),record['degree_per_residue']);expect={}
 for ex,phi in record['positive_coefficients']:
  key=tuple(ex);assert key not in expect;v=[F(x)for x in phi];assert len(v)==8 and positive_phi(v)
  expect[key]=summ(scale(powers[i],x)for i,x in enumerate(v));assert expect[key]!=Z and conj(expect[key])==expect[key];signs+=1
 assert expect and {k:v for k,v in poly.items()if v!=Z}==expect
allowed={tuple(q['representative'])for q in MM['remaining_spectrum_classes']};assert len(allowed)==13;seen=set();signs=0;kinds=collections.Counter()
for rec in D['records']:
 S=tuple(rec['representative']);assert S in allowed and S not in seen;seen.add(S);groups=short_groups(S)
 assert {tuple(q['low_indices'])for q in rec['branches']}==set(itertools.product(*groups))
 for br in rec['branches']:
  branch=tuple(br['low_indices']);kind=br['kind'];kinds[kind]+=1
  if kind=='collision':
   highs=[next(j for j in g if j!=lo)for g,lo in zip(groups,branch)];i,j=br['high_collision_indices'];assert i in highs and j in highs and i!=j and S[i]%5==S[j]%5
  elif kind=='self':
   tr,de=selfterms(S,br['d'],br['theta_pi_over_15'],br['pivots']);check_poly(S,tr,branch,br['trace']);check_poly(S,de,branch,br['determinant'])
  else:
   assert kind=='cross';co=coeffs(S,br['pivot_L'],br['pivot_M']);ref=next(v for I,v in co if v!=Z);terms=[(tuple(j for j in range(6)if j not in I),km(v,conj(ref)))for I,v in co];check_poly(S,terms,branch,br['cross_determinant'])
assert len(seen)==3 and dict(kinds)=={'self':6,'cross':1,'collision':3}
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(raw).hexdigest(),
 'manifest_sha256':hashlib.sha256(mr).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'classes_checked':len(seen),'branch_kinds':dict(kinds),'strict_positive_coefficients':signs,
 'remaining_classes':len(allowed-seen),'independent_field_basis_and_rational_intervals_pass':True,'status':'PASS'}
(P/'frontier-20261029-cyclic15-mixed-branch-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
