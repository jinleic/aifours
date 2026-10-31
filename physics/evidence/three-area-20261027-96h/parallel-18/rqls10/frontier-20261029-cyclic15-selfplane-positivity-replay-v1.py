#!/usr/bin/env python3
"""Independent Q(sqrt5) and rational-interval replay of self-plane certificates."""
import collections,datetime,hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-cyclic15-selfplane-positivity-proof-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='f150d1f050f2e55051ccc239e8c64c2ae2b1eb89ce766991303b8808eb3689ad';D=json.loads(raw)
manifest=P/'frontier-20261029-cyclic15-semicircle-filter-v1.json';mr=manifest.read_bytes();assert hashlib.sha256(mr).hexdigest()=='4d598b2b856faff3dabd74633dc3d7c3611d10b43b42602e5a6a2325756cf937';MM=json.loads(mr)
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
def ks(x,y):return ka(x,kn(y))
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
def phase_real(a0,d,k):
 ph=powers[(-8*k)%15];ph=ph if k%2==0 else kn(ph);v=km(ph,powers[(-d*a0)%15]);return scale(ka(v,conj(v)),F(1,2))
def selfterms(S,d,k,piv):
 N=kernel(S,(0,5,-d,5-d),piv);h=[phase_real(x,d,k)for x in S];tr=[];de=[]
 for j in range(6):tr.append((tuple(x for x in range(6)if x!=j),km(h[j],summ(km(conj(N[j][b]),N[j][b])for b in range(2)))))
 for i,j in itertools.combinations(range(6),2):
  v=ks(km(N[i][0],N[j][1]),km(N[i][1],N[j][0]));de.append((tuple(x for x in range(6)if x not in(i,j)),km(km(h[i],h[j]),km(v,conj(v)))))
 return tr,de
def hpoly(S,terms,L):
 groups=[[j for j,x in enumerate(S)if x%3==r]for r in range(3)];out={}
 for indices,val in terms:
  if val==Z:continue
  ex=[0]*6
  for j in indices:ex[j]+=1
  pieces=[(ex,val)]
  for group in groups:
   power=L-sum(ex[j]for j in group);assert power>=0;new=[]
   for cnt,coef in comps(len(group),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(group,cnt):arr[j]+=k
     new.append((arr,scale(x,coef*3**power)))
   pieces=new
  for arr,x in pieces:
   key=tuple(arr);out[key]=ka(out.get(key,Z),x)
 return out
allowed={tuple(q['representative'])for q in MM['remaining']};assert len(allowed)==32;seen=set();checks=0
for rec in D['records']:
 S=tuple(rec['representative']);assert S in allowed and S not in seen;seen.add(S);d,k=rec['d'],rec['theta_pi_over_15'];assert d in (2,7)and 0<=k<30
 tr,de=selfterms(S,d,k,rec['pivots']);assert [q['kind']for q in rec['polynomials']]==['trace','determinant']
 for q,terms in zip(rec['polynomials'],[tr,de]):
  poly=hpoly(S,terms,q['degree_per_residue']);expected={}
  for exp,phi in q['positive_coefficients']:
   key=tuple(exp);assert key not in expected;vv=[F(x)for x in phi];assert len(vv)==8 and positive_phi(vv)
   expected[key]=summ(scale(powers[i],x)for i,x in enumerate(vv));assert expected[key]!=Z and conj(expected[key])==expected[key];checks+=1
  assert {k:v for k,v in poly.items()if v!=Z}==expected and expected
assert len(seen)==3
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(raw).hexdigest(),
 'manifest_sha256':hashlib.sha256(mr).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'classes_checked':len(seen),'strict_positive_coefficients':checks,'remaining_classes':len(allowed-seen),
 'exact_field_reconstruction_and_rational_intervals_pass':True,'status':'PASS'}
(P/'frontier-20261029-cyclic15-selfplane-positivity-replay-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
