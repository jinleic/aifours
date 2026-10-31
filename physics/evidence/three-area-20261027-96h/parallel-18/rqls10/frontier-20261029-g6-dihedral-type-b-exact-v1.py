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
def check_case(swap):
 t=sub(V,U);X=(O,Z,Z,O,mul(W,t)if swap else W,mul(I,W if swap else mul(W,t)));sp=orbit(spidx,X)
 assert norm(X)==const(4) and len(sp)==12 and all(dot(sp[a],sp[b])==Z for a,b in itertools.combinations(sp,2)if adjacent(a,b))
 nn_results={}
 for sign in (1,-1):
  roots=nullspace(eigrows(hNN,sign)+incidence_rows((3,8),sp));assert len(roots)==1
  nn_results[str(sign)]=rational(overlap2(roots[0],gv(gNN,roots[0])))
  if sign==1:ny=roots[0]
 assert nn_results=={'1':'0','-1':'16/121'}
 nn=orbit(nnidx,ny);assert len(nn)==6
 assert all(dot(sp[i],nn[j])==Z for i in sp for j in nn if adjacent(i,j))
 assert all(dot(nn[i],nn[j])==Z for i,j in itertools.combinations(nn,2)if adjacent(i,j))
 known=[v for j,v in sp.items()if 9 in E[j]]+[v for j,v in nn.items()if 9 in E[j]];assert len(known)==4
 rows=[[conjbit(x,0)for x in v]for v in known];roots=[nullspace(eigrows(hNear,sign)+rows)for sign in (1,-1)];assert all(len(q)==1 for q in roots)
 up,um=roots[0][0],roots[1][0];dp,dm=norm(up),norm(um);a,b=dot(up,gv(s,up)),dot(um,gv(s,um));cc=dot(up,gv(s,um))
 assert add(div(a,dp),div(b,dm))==const(F(-2,3)) and div(mul(cc,conjbit(cc,0)),mul(dp,dm))==const(F(1,8))
 branches={}
 for branch in (1,-1):
  t=div(mul(dp,add(const(F(1,3)),mul(const(branch),mul(I,div(U,const(12)))))),cc)
  y=va(up,vs(t,um));assert dot(y,gv(hNear,y))==dot(y,gv(s,y))==Z
  nf=orbit(nfidx,y);assert len(nf)==12 and all(dot(nf[i],nf[j])==Z for i,j in itertools.combinations(nf,2)if adjacent(i,j))
  assert all(dot(nf[i],d[j])==Z for d in(sp,nn)for i in nf for j in d if adjacent(i,j))
  far={}
  for sign in (1,-1):
   roots=nullspace(eigrows(hFF,sign)+incidence_rows((0,6),nf));assert len(roots)==1
   ratio=overlap2(roots[0],gv(s,roots[0]));assert ratio!=Z;far[str(sign)]=rational(ratio)
  branches[str(branch)]=far
 return {'swap':swap,'near_near_overlap_squared':nn_results,'far_far_overlap_squared':branches}
results=[check_case(False),check_case(True)]
expected=[{'swap':False,'near_near_overlap_squared':{'1':'0','-1':'16/121'},'far_far_overlap_squared':{'1':{'1':'16/49','-1':'64/169'},'-1':{'1':'64/121','-1':'16/49'}}},
 {'swap':True,'near_near_overlap_squared':{'1':'0','-1':'16/121'},'far_far_overlap_squared':{'1':{'1':'64/121','-1':'16/49'},'-1':{'1':'16/49','-1':'64/169'}}}]
assert results==expected
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'seed_choices':2,'near_near_eigenspaces':2,'near_far_phase_choices':2,
 'far_eigenspaces':2,'case_results':results,'all_far_overlaps_nonzero':True,'status':'PASS'}
(P/'frontier-20261029-g6-dihedral-type-b-exact-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
