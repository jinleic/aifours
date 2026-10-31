#!/usr/bin/env python3
"""Independent exact field-basis replay of short-pair imbalance certificates."""
import collections,datetime,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cyclic15-imbalance-determinant-proof-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='6e3accab7481596ca29a504d12e7792f735ae5e1c457bdc75fa0adf9887f392f';D=json.loads(raw)
manifest=P/'frontier-20261029-cyclic15-29-residual-spectra-v1.json';mr=manifest.read_bytes();assert hashlib.sha256(mr).hexdigest()=='59962a77982e79225d8104079c682e2f67be1401d991f1d2f818af4f259ca9bb';MM=json.loads(mr)
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
assert 5*1920**2-4289**2==36479>0

def shorts(S):
 out=[]
 for r in range(3):
  g=[j for j,a in enumerate(S)if a%3==r]
  if len(g)==2 and (S[g[1]]-S[g[0]])%15 in(3,12):out.append(g)
 return out
def transform(S,coef,lo,orient):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];ss=shorts(S);assert len(ss)==1 and lo in ss[0];T=[[F(0)for _ in range(6)]for _ in range(6)]
 for g in groups:
  if set(g)==set(ss[0]):
   hi=next(j for j in g if j!=lo);T[lo][lo]=F(7,240);T[hi][lo]=F(73,240);T[hi][hi]=F(1,3)
  else:
   for j in g:T[j][j]=F(1,3)
 ref=next(v for I,v in coef if v!=Z);out={}
 for I,v in coef:
  if v==Z:continue
  i,j=[x for x in range(6)if x not in I];val=km(v,conj(ref));val=val if orient>0 else kn(val);assert conj(val)==val
  for a0 in range(6):
   if not T[i][a0]:continue
   for b in range(6):
    if not T[j][b]:continue
    key=tuple(sorted((a0,b)));out[key]=ka(out.get(key,Z),scale(val,T[i][a0]*T[j][b]))
 return out
def expand_unit(S,terms,L):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];out={}
 for ij,val in terms.items():
  if val==Z:continue
  ex=[0]*6
  for j in ij:ex[j]+=1
  pieces=[(ex,val)]
  for g in groups:
   power=L-sum(ex[j]for j in g);assert power>=0;new=[]
   for cnt,coef in comps(len(g),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(g,cnt):arr[j]+=k
     new.append((arr,scale(x,coef)))
   pieces=new
  for arr,x in pieces:
   key=tuple(arr);out[key]=ka(out.get(key,Z),x)
 return out
allowed={tuple(q['representative'])for q in MM['remaining_spectrum_classes']};assert len(allowed)==29;seen=set();checks=branches=0
for rec in D['records']:
 S=tuple(rec['representative']);assert S in allowed and S not in seen;seen.add(S);ss=shorts(S);assert len(ss)==1;co=coeffs(S,rec['pivot_L'],rec['pivot_M']);assert {q['low_index']for q in rec['branches']}==set(ss[0])
 for br in rec['branches']:
  branches+=1;assert br['orientation']in(-1,1)and br['degree_per_residue']==2
  poly=expand_unit(S,transform(S,co,br['low_index'],br['orientation']),br['degree_per_residue']);expected={}
  for ex,phi in br['positive_coefficients']:
   key=tuple(ex);assert key not in expected;vv=[F(x)for x in phi];assert len(vv)==8 and positive_phi(vv)
   expected[key]=summ(scale(powers[i],x)for i,x in enumerate(vv));assert expected[key]!=Z and conj(expected[key])==expected[key];checks+=1
  assert {k:v for k,v in poly.items()if v!=Z}==expected and expected
assert len(seen)==16 and branches==32
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(raw).hexdigest(),
 'manifest_sha256':hashlib.sha256(mr).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'classes_checked':len(seen),'imbalance_branches_checked':branches,'strict_positive_coefficients':checks,
 'remaining_classes':len(allowed-seen),'independent_field_basis_and_rational_intervals_pass':True,'status':'PASS'}
(P/'frontier-20261029-cyclic15-imbalance-determinant-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
