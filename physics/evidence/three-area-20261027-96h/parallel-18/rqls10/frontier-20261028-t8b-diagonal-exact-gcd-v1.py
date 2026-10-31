#!/usr/bin/env python3
"""Complete exact saturation/gcd gate for T8B(z,z,z) even Fourier T.

Source-order0 anchored, T=(0,0), inspect rows1,7 and when needed row2.
Unit z means z,N=1+3z²,D'=3+z² are nonzero; exact division removes only
these factors. Degree-stable coprime reductions are exact resultant gates;
other cases use Euclidean gcd over Q(zeta8) and retain all non-mu8 roots.
"""
import datetime,hashlib,itertools,json,math,time
from collections import Counter
from fractions import Fraction as Fr
from functools import lru_cache
from pathlib import Path
P=Path(__file__).resolve().parent;source=P/'frontier-20261028-t8b-diagonal-root-superset-v1.py';raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='17e28e2f6c8d437f2d6b420e3bec07422a65ec6f225bb2b6f8ae233b36be098a'
exec(compile(raw.decode().split('unique=set();zero=0;',1)[0],str(source),'exec'),globals())
p=65521;w=57852;Z=(0,0,0,0)
def add4(a,b):return tuple(x+y for x,y in zip(a,b))
def neg4(a):return tuple(-x for x in a)
def mul4(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return (a0*b0-a1*b3-a2*b2-a3*b1,a0*b1+a1*b0-a2*b3-a3*b2,a0*b2+a1*b1+a2*b0-a3*b3,a0*b3+a1*b2+a2*b1+a3*b0)
def conj4(a):return (a[0],-a[3],-a[2],-a[1])
def r8(k):
 k%=8;v=[0]*4;v[k%4]=1 if k<4 else -1;return tuple(v)
def trim(a):
 while len(a)>1 and a[-1]==Z:a.pop()
 return a
def norm(a):
 a=trim(list(a))
 while len(a)>1 and a[0]==Z:a=a[1:] # z is nonzero on the unit torus
 if a==[Z]:return (Z,)
 den=math.lcm(*(Fr(x).denominator for v in a for x in v));q=[tuple(int(Fr(x)*den)for x in v)for v in a]
 g=math.gcd(*(abs(x)for v in q for x in v));q=[tuple(x//g for x in v)for v in q]
 return min(tuple(mul4(v,r8(k))for v in q)for k in range(8))
def divide_scalar_quad(a,u,v): # u+v*z²; rational quotient iff exact remainder0
 a=[[Fr(x)for x in c]for c in a];q=[[Fr(0)]*4 for _ in range(max(0,len(a)-2))]
 for i in range(len(a)-1,1,-1):
  z=[x/v for x in a[i]];q[i-2]=z
  for k in range(4):a[i][k]-=z[k]*v;a[i-2][k]-=z[k]*u
 if any(any(x for x in q0)for q0 in a[:2]):return None
 return norm([tuple(x)for x in q])
@lru_cache(maxsize=None)
def peel(a):
 a=norm(a)
 if a==(Z,):return a
 for u,v in [(1,3),(3,1)]:
  while len(a)>2:
   q=divide_scalar_quad(a,u,v)
   if q is None:break
   a=q
 return a
def pol(O,c,d,delta):
 out=[[0]*4 for _ in range(13)]
 for t in range(8):
  sc,kc,dc=K[O[t]][c];sd,kd,dd=K[O[t]][d];shift=kd-kc+3;r=r8(delta*t)
  for e,q in F[dd-dc].items():
   for j in range(4):out[e+shift][j]+=sc*sd*q*r[j]
 return peel(tuple(tuple(v)for v in out))
def reduction(a):
 z=[sum(v[j]*pow(w,j,p)for j in range(4))%p for v in a]
 stable=(a==(Z,) or z[-1]!=0)
 while len(z)>1 and not z[-1]:z.pop()
 return z,stable
def remp(a,b):
 a=a[:];iv=pow(b[-1],-1,p)
 while len(a)>=len(b) and a!=[0]:
  d=len(a)-len(b);q=a[-1]*iv%p
  for j,v in enumerate(b):a[d+j]=(a[d+j]-q*v)%p
  while len(a)>1 and not a[-1]:a.pop()
 return a
def gcdp(a,b):
 while b!=[0]:a,b=b,remp(a,b)
 return a
# Exact Q(zeta8) polynomial gcd, used only after modular screening.
@lru_cache(maxsize=None)
def inv4(a):
 a=tuple(Fr(x)for x in a);M=[]
 cols=[mul4(a,r8(j))for j in range(4)]
 for i in range(4):M.append([Fr(cols[j][i])for j in range(4)]+[Fr(int(i==0))])
 for c in range(4):
  k=next(i for i in range(c,4)if M[i][c]);M[c],M[k]=M[k],M[c];q=M[c][c];M[c]=[x/q for x in M[c]]
  for i in range(4):
   if i!=c:
    q=M[i][c];M[i]=[x-q*y for x,y in zip(M[i],M[c])]
 return tuple(M[i][4]for i in range(4))
def remK(a,b):
 a=[tuple(Fr(x)for x in v)for v in a];b=[tuple(Fr(x)for x in v)for v in b];iv=inv4(b[-1])
 while len(a)>=len(b) and a!=[Z]:
  d=len(a)-len(b);q=mul4(a[-1],iv)
  for j,v in enumerate(b):a[d+j]=add4(a[d+j],neg4(mul4(q,v)))
  trim(a)
 return a
def gcdK(a,b):
 a=list(a);b=list(b)
 while b!=[Z]:a,b=b,remK(a,b)
 iv=inv4(a[-1]);return [mul4(v,iv)for v in a]
def all_root8(a):
 a=[tuple(Fr(x)for x in v)for v in a];ks=[]
 if a==[Z]:return None
 for k in range(8):
  r=r8(k)
  while len(a)>1:
   q=[Z]*(len(a)-1);q[-1]=a[-1]
   for j in range(len(q)-2,-1,-1):q[j]=add4(a[j+1],mul4(r,q[j+1]))
   if add4(a[0],mul4(r,q[0]))!=Z:break
   ks.append(k);a=trim(q)
 return sorted(set(ks)) if len(a)==1 and a[0]!=Z else None

def gate(polys):
 polys=[x for x in polys if x!=(Z,)]
 if not polys:return ('unresolved',None)
 red=[reduction(x)for x in polys]
 if all(flag for _,flag in red):
  g=red[0][0]
  for a,_ in red[1:]:g=gcdp(g,a)
  if len(g)==1:return ('mod_coprime',None)
 g=list(polys[0])
 for a in polys[1:]:g=gcdK(g,list(a))
 if len(g)==1:return ('exact_coprime',None)
 k=all_root8(g)
 if k is not None:return ('only_root8',k)
 return ('unresolved',None)
# K and F in source helper are token matrix and numerator/denominator polynomials.
start=time.monotonic();cnt=Counter();unresolved=[];details=[];orders=0
for perm in itertools.permutations(range(1,8)):
 O=(0,)+perm;orders+=1
 plus=[pol(O,0,c,1)for c in range(1,8)];minus=[pol(O,0,c,7)for c in range(1,8)]
 for c in range(1,8):
  for d in range(1,8):
   if c==d:continue
   A,B=plus[c-1],minus[d-1];kind,ks=gate([A,B])
   if kind in ('mod_coprime','exact_coprime','only_root8'):cnt['pair_'+kind]+=1;continue
   C=pol(O,c,d,6);kind,ks=gate([A,B,C])
   if kind in ('mod_coprime','exact_coprime','only_root8'):cnt['triple_'+kind]+=1;continue
   # A true T chooses one of the remaining five columns in physical row2.
   cnt['fourth_parent']+=1
   for e in range(1,8):
    if e in (c,d):continue
    extra=[pol(O,0,e,2),pol(O,c,e,1),pol(O,d,e,3)]
    kind,ks=gate([A,B,C]+extra)
    if kind=='unresolved':unresolved.append({'O':O,'c':c,'d':d,'e':e});cnt['unresolved']+=1
    else:cnt['fourth_'+kind]+=1
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256(raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'seconds':round(time.monotonic()-start,6),'orders':orders,'ordered_pairs_per_order':42,
 'counts':dict(cnt),'unresolved':len(unresolved),'peel_cache_entries':peel.cache_info().currsize,
 'warning':'unit-root cases still require separate exact rejection'}
(P/'frontier-20261028-t8b-diagonal-exact-gcd-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
(P/'frontier-20261028-t8b-diagonal-exact-gcd-unresolved-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n' for x in unresolved))
print(json.dumps(obj,indent=2))
