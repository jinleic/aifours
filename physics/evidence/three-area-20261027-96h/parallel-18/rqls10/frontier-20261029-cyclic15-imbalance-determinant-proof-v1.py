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
# A strict rational relaxation of the short-pair population imbalance.
assert 5*1920**2-4289**2==36479>0 # sqrt5>4289/1920 implies delta>11/80.
def short_groups(S):
 out=[]
 for r in range(3):
  g=[j for j,a in enumerate(S)if a%3==r]
  if len(g)==2 and (S[g[1]]-S[g[0]])%15 in(3,12):out.append(g)
 return out
def transformed(S,coef,low,orientation):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];short=short_groups(S);assert len(short)==1 and low in short[0];T=[[F(0)for _ in range(6)]for _ in range(6)]
 for g in groups:
  if set(g)==set(short[0]):
   high=next(j for j in g if j!=low);T[low][low]=F(7,240);T[high][low]=F(73,240);T[high][high]=F(1,3)
  else:
   for j in g:T[j][j]=F(1,3)
 ref=next(v for I,v in coef if v!=Z);terms={}
 for I,v in coef:
  if v==Z:continue
  i,j=[x for x in range(6)if x not in I];val=mul(v,conj(ref));val=val if orientation>0 else neg(val);assert conj(val)==val
  for a in range(6):
   if not T[i][a]:continue
   for b in range(6):
    if not T[j][b]:continue
    key=tuple(sorted((a,b)));q=T[i][a]*T[j][b];terms[key]=add(terms.get(key,Z),tuple(q*x for x in val))
 return terms
def expand_x(S,terms,L):
 groups=[[j for j,a in enumerate(S)if a%3==r]for r in range(3)];out={}
 for ij,val in terms.items():
  if val==Z:continue
  ex=[0]*6
  for j in ij:ex[j]+=1
  pieces=[(ex,val)]
  for g in groups:
   power=L-sum(ex[j]for j in g);assert power>=0;new=[]
   for cnt,coef in compositions(len(g),power):
    for arr,x in pieces:
     arr=arr.copy()
     for j,k in zip(g,cnt):arr[j]+=k
     new.append((arr,tuple(coef*q for q in x)))
   pieces=new
  for arr,x in pieces:
   key=tuple(arr);out[key]=add(out.get(key,Z),x)
 return out
manifest=P/'frontier-20261029-cyclic15-29-residual-spectra-v1.json';raw=manifest.read_bytes();assert hashlib.sha256(raw).hexdigest()=='59962a77982e79225d8104079c682e2f67be1401d991f1d2f818af4f259ca9bb';D=json.loads(raw);allowed={tuple(q['representative'])for q in D['remaining_spectrum_classes']};assert len(allowed)==29
TARGETS=[((0, 1, 2, 3, 4, 6), [((1,), 2, 1), ((4,), 2, -1)]), ((0, 1, 2, 3, 4, 7), [((0,), 2, 1), ((3,), 2, -1)]), ((0, 1, 2, 3, 4, 9), [((1,), 2, 1), ((4,), 2, -1)]), ((0, 1, 2, 3, 5, 8), [((0,), 2, 1), ((3,), 2, -1)]), ((0, 1, 2, 4, 5, 7), [((2,), 2, 1), ((4,), 2, -1)]), ((0, 1, 2, 4, 5, 10), [((2,), 2, 1), ((4,), 2, -1)]), ((0, 1, 2, 4, 5, 13), [((2,), 2, 1), ((4,), 2, -1)]), ((0, 1, 2, 4, 6, 9), [((1,), 2, 1), ((3,), 2, -1)]), ((0, 1, 2, 4, 6, 12), [((1,), 2, 1), ((3,), 2, -1)]), ((0, 1, 2, 4, 7, 12), [((0,), 2, 1), ((5,), 2, -1)]), ((0, 1, 2, 4, 9, 12), [((1,), 2, 1), ((3,), 2, -1)]), ((0, 1, 2, 4, 10, 12), [((0,), 2, 1), ((5,), 2, -1)]), ((0, 1, 2, 5, 7, 10), [((2,), 2, 1), ((3,), 2, -1)]), ((0, 1, 3, 5, 6, 8), [((3,), 2, -1), ((5,), 2, 1)]), ((0, 1, 3, 5, 10, 13), [((0,), 2, 1), ((2,), 2, -1)]), ((0, 1, 3, 6, 8, 13), [((1,), 2, 1), ((5,), 2, -1)])]
records=[]
for S,branches in TARGETS:
 assert S in allowed and len(short_groups(S))==1;pl,pm,co=coefficients(S);out=[]
 for choice,L,orientation in branches:
  assert len(choice)==1 and L==2;low=choice[0];poly=expand_x(S,transformed(S,co,low,orientation),L);entries=[]
  for exp,val in sorted(poly.items()):
   if val==Z:continue
   assert positive(val);entries.append([list(exp),[str(x)for x in val]])
  assert entries;out.append({'low_index':low,'degree_per_residue':L,'orientation':orientation,'positive_coefficients':entries})
 assert {q['low_index']for q in out}==set(short_groups(S)[0]);records.append({'representative':S,'pivot_L':pl,'pivot_M':pm,'branches':out})
assert len(records)==16
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'records':records,
 'scope':'16 cyclic spectra; both strict short-pair imbalance branches have nonzero cross determinant','status':'PRODUCED_UNREPLAYED'}
out=P/'frontier-20261029-cyclic15-imbalance-determinant-proof-v1.json';out.write_text(json.dumps(obj,separators=(',',':'))+'\n')
print(json.dumps({'source_sha256':obj['source_sha256'],'proof_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'clock_finish':obj['clock_finish'],'proved_classes':16,'remaining_classes':13,'status':'PRODUCED_UNREPLAYED'},indent=2))
