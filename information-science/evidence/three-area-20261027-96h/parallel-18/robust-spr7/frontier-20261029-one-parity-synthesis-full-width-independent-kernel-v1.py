# Exact independent replay: monomial Sturm chains, Hurwitz determinants,
# ordered parity sign markers and a literal midpoint failure.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-one-parity-synthesis-full-width-frozen-v1.json').read_bytes()
assert sha256(raw).hexdigest()=='c5dccada6b60d4f070be291b7209e3ead2acd316def14280808787ee91daa849'
z=json.loads(raw);mid=list(map(F,z['center']));rad=list(map(F,z['seven_independent_radii']));b=list(map(F,z['scaled_common_numerator']));lo=[mid[i]-rad[i] for i in range(7)];hi=[mid[i]+rad[i] for i in range(7)]
assert len(rad)==7 and all(x>0 for x in lo+rad) and mid[7]==b[7]==1
assert all(b[i]==mid[i]*(F(1,16) if i%2==0 else 1) for i in range(8))
def corner(e,o):
 a=[]
 for j in range(7):
  plus=e if j%2==0 else o
  larger=plus==(-1)**(j//2)
  a.append(hi[j] if larger else lo[j])
 return a+[F(1)]
cs=[corner(e,o) for e in (-1,1) for o in (-1,1)]
def parts(a):return [a[0],-a[2],a[4],-a[6]],[a[1],-a[3],a[5],-a[7]]
def val(p,t):return sum(x*t**j for j,x in enumerate(p))
def mul(p,q):
 out=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):out[i+j]+=x*y
 return out
def pairing(a,b):
 E,O=parts(a);Fv,G=parts(b);p=mul(E,Fv);q=mul(O,G);out=[F(0)]*max(len(p),len(q)+1)
 for i,x in enumerate(p):out[i]+=x
 for i,x in enumerate(q):out[i+1]+=x
 return out
def trim(p):
 p=p[:]
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def remainder(a,d):
 a=trim(a);d=trim(d)
 while len(a)>=len(d) and a!=[0]:
  off=len(a)-len(d);scale=a[-1]/d[-1]
  for j in range(len(d)):a[off+j]-=scale*d[j]
  a=trim(a)
 return a
def sturm(p):
 p=trim(p);d=trim([j*p[j] for j in range(1,len(p))]);chain=[p,d]
 while chain[-1]!=[0]:
  rem=remainder(chain[-2],chain[-1])
  if rem==[0]:break
  rem=[-x/abs(rem[-1]) for x in rem];chain.append(trim(rem))
 def variation(xs):
  s=[1 if x>0 else -1 for x in xs if x];return sum(a!=b for a,b in zip(s,s[1:]))
 v0=variation([q[0] for q in chain]);vinf=variation([q[-1] for q in chain]);return v0,vinf

def determinant(M):
 A=[row[:] for row in M];d=F(1)
 for k in range(len(A)):
  p=next((i for i in range(k,len(A)) if A[i][k]),None)
  if p is None:return F(0)
  if p!=k:A[p],A[k]=A[k],A[p];d=-d
  v=A[k][k];d*=v
  for i in range(k+1,len(A)):
   fac=A[i][k]/v
   for j in range(k+1,len(A)):A[i][j]-=fac*A[k][j]
 return d
def hurwitz(a):
 v=a[::-1];H=[[v[2*j-i+1] if 0<=2*j-i+1<8 else F(0) for j in range(7)] for i in range(7)]
 return [determinant([row[:k] for row in H[:k]]) for k in range(1,8)]
assert all(x>0 for a in cs for x in hurwitz(a))
markers=z['stability_markers_t_and_even_odd_sign']
for t,es,os in markers:
 t=F(t)
 for a in cs:
  E,O=parts(a);assert es*val(E,t)>0 and os*val(O,t)>0
checks=[]
for a in cs:
 p=pairing(a,b);assert p[0]>0 and p[-1]>0
 v0,vi=sturm(p);assert v0-vi==0;checks.append((len(p)-1,v0,vi))
witness=list(map(F,z['midpoint_failure_member']));assert all(lo[i]<=witness[i]<=hi[i] for i in range(7)) and witness[7]==1
assert val(pairing(witness,mid),F(z['midpoint_failure_t']))==F(z['midpoint_failure_pairing'])<0
# Endpoint and sign-margin controls: deliberately violate each predicate.
zero_b=b[:];zero_b[0]=0;assert pairing(cs[0],zero_b)[0]==0
wide=rad[:];wide[1]=F(1,100);wide[3]=wide[5]=F(1,100)
wide_hi=[mid[i]+wide[i] for i in range(7)]
Oplus=[wide_hi[1],-(mid[3]-wide[3]),wide_hi[5],-F(1)]
assert val(Oplus,F(3999,1000))>0
print({'strict_widths':7,'positive_hurwitz_minors':28,'ordered_marker_corner_signs':48,'positive_pairings_sturm':checks,'midpoint_failure':z['midpoint_failure_pairing'],'mutation_controls':2})
