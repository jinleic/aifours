#!/usr/bin/env python3
"""Independent replay of T8B(z,z,z) all-phase adjacent-root gates.

Reconstruct source Gram polynomials in basis 1,i,sqrt2,i sqrt2 (zeta8
represented with denominator2); exact N,D saturation, mod97 coprimality or
exact Q(i,sqrt2) gcd. Unit-root gate returns only explicit mu8 roots.
"""
import datetime,hashlib,itertools,json,math,os,time
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
P=Path(__file__).resolve().parent;p=97;w=64;assert pow(w,4,p)==p-1
rows=[['1','1','1','1','1','1','1','1'],['1','-1','-d','-c','d','c','cd','-cd'],['1','-a','-1','c','a','-ac','-c','ac'],['1','a','d','-1','ad','-a','-d','-ad'],['1','b','-b','-bc','-1','-c','c','bc'],['1','-b','bd','b','-d','-1','d','-bd'],['1','-ab','b','-b','-a','a','-1','ab'],['1','ab','-bd','bc','-ad','ac','-cd','-abcd']]
def token(s):
 sign=-1 if s.startswith('-')else 1;s=s.lstrip('-');return sign,sum(s.count(v)for v in 'abc'),s.count('d')
K=[[token(s)for s in row]for row in rows]
Z=(0,0,0,0);ONE=(1,0,0,0)
roots=[(2,0,0,0),(0,0,1,1),(0,2,0,0),(0,0,-1,1),(-2,0,0,0),(0,0,-1,-1),(0,-2,0,0),(0,0,1,-1)]
Ffac={1:{0:1,2:6,4:9},0:{1:3,3:10,5:3},-1:{2:9,4:6,6:1}}
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mul(a,b):
 a0,a1,a2,a3=a;b0,b1,b2,b3=b
 return (a0*b0-a1*b1+2*(a2*b2-a3*b3),a0*b1+a1*b0+2*(a2*b3+a3*b2),a0*b2+a2*b0-a1*b3-a3*b1,a0*b3+a3*b0+a1*b2+a2*b1)
def trim(a):
 while len(a)>1 and a[-1]==Z:a.pop()
 return a
def norm(a):
 a=trim(list(a))
 while len(a)>1 and a[0]==Z:a=a[1:]
 if a==[Z]:return (Z,)
 den=math.lcm(*(F(x).denominator for v in a for x in v));b=[tuple(int(F(x)*den)for x in v)for v in a];g=math.gcd(*(abs(x)for v in b for x in v));b=[tuple(x//g for x in v)for v in b]
 first=next(x for v in b for x in v if x);return tuple(tuple(-x for x in v)for v in b)if first<0 else tuple(b)
def divide(a,u,v):
 a=[[F(x)for x in c]for c in a];out=[[F(0)]*4 for _ in range(max(0,len(a)-2))]
 for k in range(len(a)-1,1,-1):
  t=[x/v for x in a[k]];out[k-2]=t
  for j in range(4):a[k][j]-=t[j]*v;a[k-2][j]-=t[j]*u
 if any(any(x for x in z)for z in a[:2]):return None
 return norm([tuple(v)for v in out])
@lru_cache(maxsize=None)
def peel(a):
 a=norm(a)
 if a==(Z,):return a
 for u,v in ((1,3),(3,1)):
  while len(a)>2:
   q=divide(a,u,v)
   if q is None:break
   a=q
 return a
def poly(O,c,d,delta):
 out=[[0]*4 for _ in range(13)]
 for t in range(8):
  sc,kc,dc=K[O[t]][c];sd,kd,dd=K[O[t]][d];shift=kd-kc+3;r=roots[(delta*t)%8]
  for e,q in Ffac[dd-dc].items():
   for j in range(4):out[e+shift][j]+=sc*sd*q*r[j]
 return peel(tuple(tuple(v)for v in out))
# ring embeddings i=w², sqrt2=w-w³, i sqrt2=w+w³.
im=w*w%p;sq=(w-pow(w,3,p))%p;isq=(w+pow(w,3,p))%p;embed=(1,im,sq,isq)
def reduction(a):
 b=[sum(v[j]*embed[j]for j in range(4))%p for v in a];stable=(a==(Z,)or b[-1]!=0)
 while len(b)>1 and b[-1]==0:b.pop()
 return b,stable
def remp(a,b):
 a=a[:];iv=pow(b[-1],-1,p)
 while len(a)>=len(b) and a!=[0]:
  k=len(a)-len(b);x=a[-1]*iv%p
  for j,v in enumerate(b):a[k+j]=(a[k+j]-x*v)%p
  while len(a)>1 and a[-1]==0:a.pop()
 return a
def gcdp(a,b):
 while b!=[0]:a,b=b,remp(a,b)
 return a
@lru_cache(maxsize=None)
def inv(a):
 a=tuple(F(x)for x in a);basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)];cols=[mul(a,v)for v in basis];M=[[F(cols[j][i])for j in range(4)]+[F(i==0)]for i in range(4)]
 for j in range(4):
  k=next(i for i in range(j,4)if M[i][j]);M[j],M[k]=M[k],M[j];v=M[j][j];M[j]=[x/v for x in M[j]]
  for i in range(4):
   if i!=j:
    v=M[i][j];M[i]=[x-v*y for x,y in zip(M[i],M[j])]
 return tuple(M[i][4]for i in range(4))
def remK(a,b):
 a=[tuple(F(x)for x in v)for v in a];b=[tuple(F(x)for x in v)for v in b];iv=inv(b[-1])
 while len(a)>=len(b) and a!=[Z]:
  k=len(a)-len(b);q=mul(a[-1],iv)
  for j,v in enumerate(b):a[k+j]=add(a[k+j],neg(mul(q,v)))
  trim(a)
 return a
def gcdK(a,b):
 a=list(a);b=list(b)
 while b!=[Z]:a,b=b,remK(a,b)
 iv=inv(a[-1]);return [mul(v,iv)for v in a]
def roots8(a):
 a=[tuple(F(x)for x in v)for v in a];hits=[]
 for k in range(8):
  r=tuple(F(x,2)for x in roots[k])
  while len(a)>1:
   q=[Z]*(len(a)-1);q[-1]=a[-1]
   for j in range(len(q)-2,-1,-1):q[j]=add(a[j+1],mul(r,q[j+1]))
   if add(a[0],mul(r,q[0]))!=Z:break
   hits.append(k);a=trim(q)
 return sorted(set(hits)) if len(a)==1 and a[0]!=Z else None
def gate(polys):
 polys=[q for q in polys if q!=(Z,)]
 if not polys:return 'unresolved'
 red=[reduction(q)for q in polys]
 if all(ok for _,ok in red):
  g=red[0][0]
  for q,_ in red[1:]:g=gcdp(g,q)
  if len(g)==1:return 'mod_coprime'
 g=list(polys[0])
 for q in polys[1:]:g=gcdK(g,q)
 if len(g)==1:return 'exact_coprime'
 if roots8(g) is not None:return 'only_root8'
 return 'unresolved'
limit=int(os.environ.get('LIMIT','0'));suffix='sample' if limit else 'full';start=time.monotonic();cnt=Counter();bad=[];orders=0
for perm in itertools.permutations(range(1,8)):
 if limit and orders>=limit:break
 O=(0,)+perm;orders+=1;plus=[poly(O,0,c,1)for c in range(1,8)];minus=[poly(O,0,c,7)for c in range(1,8)]
 for c in range(1,8):
  for d in range(1,8):
   if c==d:continue
   A,B=plus[c-1],minus[d-1];q=gate([A,B])
   if q!='unresolved':cnt['pair_'+q]+=1;continue
   C=poly(O,c,d,6);q=gate([A,B,C])
   if q!='unresolved':cnt['triple_'+q]+=1;continue
   cnt['fourth_parent']+=1
   for e in range(1,8):
    if e in (c,d):continue
    X=[poly(O,0,e,2),poly(O,c,e,1),poly(O,d,e,3)];q=gate([A,B,C]+X)
    if q=='unresolved':bad.append({'O':O,'c':c,'d':d,'e':e});cnt['unresolved']+=1
    else:cnt['fourth_'+q]+=1
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'seconds':round(time.monotonic()-start,6),
 'prime':p,'zeta8_root':w,'orders':orders,'limit':limit,'counts':dict(cnt),'unresolved':len(bad),
 'peel_cache_entries':peel.cache_info().currsize,'warning':'root8 cases need separate exact no-T checks'}
(P/f'frontier-20261028-t8b-diagonal-exact-gcd-replay-{suffix}-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
(P/f'frontier-20261028-t8b-diagonal-exact-gcd-replay-{suffix}-unresolved-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in bad))
print(json.dumps(obj,indent=2))
