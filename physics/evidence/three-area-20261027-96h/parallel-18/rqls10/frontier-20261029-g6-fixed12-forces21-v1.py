#!/usr/bin/env python3
"""Exact four-radical algebra and finite case proof for the remaining D6 action.

The formal algebra has i²=-1, u²=2, v²=3, w²=1+uv/3. Every
pivot inversion is explicitly certified, so identities specialize to the
indicated complex embedding even without assuming algebra irreducibility.
"""
import datetime,hashlib,itertools,json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
P=Path(__file__).resolve().parent;c=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';raw=c.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd';G=[set()for _ in range(15)]
for z in json.loads(raw)['cross_group_incidence']:
 a,b=z['groups']
 for i,row in enumerate(z['shared_H4_ray_matrix']):
  for j,x in enumerate(row):
   if not x:u=5*a+i;v=5*b+j;G[u].add(v);G[v].add(u)
E=sorted((i,j)for i in range(15)for j in G[i]if i<j);emap={e:k for k,e in enumerate(E)};assert len(E)==45 and all(len(x)==6 for x in G)
r=(6,7,5,9,8,10,11,12,13,14,2,1,0,3,4);s=(0,1,2,4,3,10,12,11,13,14,5,7,6,8,9)
e=tuple(range(15));comp=lambda a,b:tuple(a[b[i]]for i in range(15));pows=[e]
for k in range(1,6):pows.append(comp(pows[-1],r))
assert comp(pows[-1],r)==e and comp(s,s)==e and comp(comp(s,r),s)==pows[5]
group=pows+[comp(s,q)for q in pows];assert len(set(group))==12
for g in group:assert all((j in G[i])==(g[j]in G[g[i]])for i in range(15)for j in range(15))
forms={}
for k in range(6):forms[pows[k]]=(False,k);forms[comp(s,pows[k])]=(True,k)
action={g:[emap[tuple(sorted((g[x],g[y])))]for x,y in E]for g in group}
def adjacent(a,b):return bool(set(E[a])&set(E[b]))
# Exact field tuples in monomial basis i^a u^b v^c w^d, exponents 0 or 1.
Z=(F(0),)*16;O=(F(1),)+(F(0),)*15
def const(x):return(F(x),)+(F(0),)*15
def root(bit):return tuple(F(j==(1<<bit))for j in range(16))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
T={}
for i in range(16):
 for j in range(16):
  both=i&j;out=i^j;k=(-1 if both&1 else 1)*(2 if both&2 else 1)*(3 if both&4 else 1);terms=[(out,F(k))]
  if both&8:terms.append((out^6,F(k*(2 if out&2 else 1)*(3 if out&4 else 1),3)))
  T[i,j]=terms
def mul(a,b):
 out=[F(0)]*16
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:
     for k,q in T[i,j]:out[k]+=x*y*q
 return tuple(out)
def conjbit(a,k):return tuple(-x if j&(1<<k)else x for j,x in enumerate(a))
@lru_cache(maxsize=32768)
def inv(a):
 assert a!=Z
 for k in (3,2,1,0):
  if any(a[j]for j in range(16)if j&(1<<k)):
   b=conjbit(a,k);n=mul(a,b);assert not any(n[j]for j in range(16)if j&(1<<k));answer=mul(b,inv(n));assert mul(a,answer)==O;return answer
 answer=const(1/a[0]);assert mul(a,answer)==O;return answer
def div(a,b):return mul(a,inv(b))
I=root(0);U=root(1);V=root(2);W=root(3)
assert mul(I,I)==neg(O) and mul(U,U)==const(2) and mul(V,V)==const(3) and mul(W,W)==add(O,div(mul(U,V),const(3)))
zeta=div(add(O,mul(I,V)),const(2))
def va(a,b):return tuple(add(x,y)for x,y in zip(a,b))
def vs(c,a):return tuple(mul(c,x)for x in a)
def dot(a,b):
 q=Z
 for x,y in zip(a,b):q=add(q,mul(conjbit(x,0),y))
 return q
def rv(a):return(a[2],a[0],a[1],a[3],mul(zeta,a[4]),mul(conjbit(zeta,0),a[5]))
def sv(a):return(a[0],a[2],a[1],neg(a[3]),a[5],a[4])
def gv(g,a):
 iss,k=forms[g];v=a
 for _ in range(k):v=rv(v)
 return sv(v)if iss else v
units=[tuple(O if i==j else Z for i in range(6))for j in range(6)]
def eigrows(g,sgn):
 cols=[gv(g,x)for x in units]
 return [[sub(cols[j][i],const(sgn)if i==j else Z)for j in range(6)]for i in range(6)]
def nullspace(rows):
 A=[list(row)for row in rows];m=len(A);nr=0;pivs=[]
 for col in range(6):
  j=next((j for j in range(nr,m)if A[j][col]!=Z),None)
  if j is None:continue
  A[nr],A[j]=A[j],A[nr];q=inv(A[nr][col]);A[nr]=[mul(x,q)for x in A[nr]]
  for j in range(m):
   if j!=nr and A[j][col]!=Z:
    q=A[j][col];A[j]=[sub(x,mul(q,y))for x,y in zip(A[j],A[nr])]
  pivs.append(col);nr+=1
  if nr==m:break
 out=[]
 for free in [k for k in range(6)if k not in pivs]:
  x=[Z]*6;x[free]=O
  for i,p in enumerate(pivs):x[p]=neg(A[i][free])
  out.append(tuple(x))
 return out
def norm(x):return dot(x,x)
def orbit(idx,vec):return {action[g][idx]:gv(g,vec)for g in group}
def incidence_rows(edge,d):return [[conjbit(x,0)for x in vec]for j,vec in d.items()if set(E[j])&set(edge)]
def overlap2(a,b):
 q=dot(a,b);return div(mul(q,conjbit(q,0)),mul(norm(a),norm(b)))
def rational(a):assert all(x==0 for x in a[1:]);return str(a[0])
spidx=emap[(2,8)];nnidx=emap[(3,8)];nfidx=emap[(0,9)];hNN=comp(s,pows[5]);gNN=comp(s,pows[3]);hNear=comp(s,pows[1]);hFF=comp(s,pows[5])
# Independently check every named graph caller and the exact unitary representation.
checks=[(hNN,(3,8),(3,8)),(gNN,(3,8),(3,14)),(hNear,(0,9),(9,12)),
 (s,(0,9),(0,14)),(hFF,(0,6),(0,6)),(s,(0,6),(0,12)),
 (pows[3],(2,8),(2,9)),(s,(2,8),(2,13)),(comp(s,pows[3]),(2,8),(2,14)),
 (hNear,(2,8),(8,10))]
for g,old,new in checks:assert E[action[g][emap[old]]]==new
for g in (r,s):
 for i in range(6):
  for j in range(6):assert dot(gv(g,units[i]),gv(g,units[j]))==dot(units[i],units[j])
for a in group:
 for b in group:
  for u0 in units:assert gv(comp(a,b),u0)==gv(a,gv(b,u0))
# Non-equivariant continuation of two exact 21-ray anchor configurations.
def sm(xs):
 q=Z
 for x in xs:q=add(q,x)
 return q
def dag(A):return [[conjbit(A[j][i],0)for j in range(len(A))]for i in range(len(A[0]))]
def prod(A,B):return [[sm([mul(A[i][k],B[k][j])for k in range(len(B))])for j in range(len(B[0]))]for i in range(len(A))]
def transpose(A):return [[A[j][i]for j in range(len(A))]for i in range(len(A[0]))]
def conjmat(A):return [[conjbit(x,0)for x in row]for row in A]
def determinant(A):
 out=Z;n=len(A)
 for perm in itertools.permutations(range(n)):
  sign=(-1)**sum(perm[i]>perm[j]for i in range(n)for j in range(i+1,n));z=O
  for i,j in enumerate(perm):z=mul(z,A[i][j])
  out=add(out,z if sign==1 else neg(z))
 return out
def inv2(A):
 d=determinant(A);return [[div(A[1][1],d),div(neg(A[0][1]),d)],[div(neg(A[1][0]),d),div(A[0][0],d)]]
def columns(B):return [[B[j][i]for j in range(len(B))]for i in range(6)]
J=[[Z,neg(O)],[O,Z]]
def anti(B,C):return prod(J,transpose([[dot(B[i],C[j])for j in range(2)]for i in range(2)]))
def normratio(a,b):return overlap2(a,b)
triangle={emap[(5,10)]:units[0],emap[(2,10)]:units[1],emap[(2,5)]:units[2]}
path=[9,3,13,8,4,14,9];fars=[12,7,1,11,6,0]
assert all(f in G[a] and f in G[b]for a,b,f in zip(path,path[1:],fars))

# All forcing below uses only the 12 fixed spokes; later rays have no assumed symmetry.
def gram2(B,C):return [[dot(B[i],C[j])for j in range(2)]for i in range(2)]
def mv2(A,z):return tuple(sm([mul(A[i][j],z[j])for j in range(2)])for i in range(2))
def combine(B,z):return va(vs(z[0],B[0]),vs(z[1],B[1]))
def check_forcing(swap):
 t=sub(V,U);seed=(O,Z,Z,O,mul(W,t)if swap else W,mul(I,W if swap else mul(W,t)));sp=orbit(spidx,seed);assert len(sp)==12
 for a,b in itertools.combinations(sp,2):
  assert overlap2(sp[a],sp[b])!=O
  if adjacent(a,b):assert dot(sp[a],sp[b])==Z
 triangle_checks=[]
 for edge,axis in [((5,10),0),((2,10),1),((2,5),2)]:
  rows=incidence_rows(edge,sp);assert len(rows)==8;Q=nullspace(rows);assert len(Q)==1 and overlap2(Q[0],units[axis])==O;triangle_checks.append({'edge':edge,'nullity':len(Q),'forced_axis':axis})
 n0=nullspace(eigrows(hNN,1)+incidence_rows((3,8),sp));assert len(n0)==1;nn=orbit(nnidx,n0[0]);assert len(nn)==6
 tangent_checks=[]
 for triangle in [[(3,8),(3,14),(8,14)],[(4,9),(4,13),(9,13)]]:
  B=[nullspace(incidence_rows(edge,sp))for edge in triangle];assert all(len(x)==2 for x in B)
  A12,A13=anti(B[0],B[1]),anti(B[0],B[2]);d12,d13=determinant(A12),determinant(A13);inv(d12);inv(d13)
  H=transpose(prod(prod(dag(A12),gram2(B[1],B[2])),A13));Hp=[[div(add(H[i][j],conjbit(H[j][i],0)),const(2))for j in range(2)]for i in range(2)]
  q0=conjbit(zeta,0);expect=[[const(54),neg(mul(const(54),zeta))],[neg(mul(const(54),q0)),const(54)]];assert Hp==expect
  v=[O,q0];y0=combine(B[0],v);cv=[conjbit(x,0)for x in v];y1=combine(B[1],mv2(A12,cv));y2=combine(B[2],mv2(A13,cv))
  for edge,y in zip(triangle,[y0,y1,y2]):assert overlap2(y,nn[emap[edge]])==O
  tangent_checks.append({'edges':triangle,'all_nullities':list(map(len,B)),'positive_form':'54*abs(z1-zeta^-1*z0)^2','all_three_forced_anchor_rays_match':True})
 return {'swap':swap,'fixed_spoke_rays':len(sp),'triangle_checks':triangle_checks,'near_triangle_checks':tangent_checks}
results=[check_forcing(False),check_forcing(True)]
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'configurations':results,
 'no_equivariance_assumed_for_unfixed_rays':True,'status':'PASS'}
(P/'frontier-20261029-g6-fixed12-forces21-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
