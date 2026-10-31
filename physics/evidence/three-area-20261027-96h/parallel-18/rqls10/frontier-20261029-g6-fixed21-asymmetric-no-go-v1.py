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

def check_anchor(swap):
 t=sub(V,U);seed=(O,Z,Z,O,mul(W,t)if swap else W,mul(I,W if swap else mul(W,t)));sp=orbit(spidx,seed)
 near_seed=nullspace(eigrows(hNN,1)+incidence_rows((3,8),sp));assert len(near_seed)==1;nn=orbit(nnidx,near_seed[0])
 anc={**triangle,**sp,**nn};assert len(anc)==21
 for a,b in itertools.combinations(anc,2):
  assert normratio(anc[a],anc[b])!=O
  if adjacent(a,b):assert dot(anc[a],anc[b])==Z
 # Every near vertex has four fixed orthogonal rays and a 2D complement.
 kb={}
 for v in path[:-1]:
  known=[q for d in(sp,nn)for j,q in d.items()if v in E[j]];assert len(known)==4
  kb[v]=nullspace([[conjbit(x,0)for x in q]for q in known]);assert len(kb[v])==2
 # Near/far orthogonal complement maps are anti-linear; two maps compose linearly.
 M=[[O,Z],[Z,O]]
 for a,b in zip(path,path[1:]):
  A=anti(kb[a],kb[a]);B=anti(kb[a],kb[b]);da=determinant(A);db=determinant(B);assert da!=Z and db!=Z;inv(da);inv(db)
  M=prod(prod(B,conjmat(A)),M)
 tr=add(M[0][0],M[1][1]);det=determinant(M);delta=sub(mul(tr,tr),mul(const(4),det));inv(det);inv(delta)
 discr=rational(div(delta,det));assert discr=='-800/729'
 known=[q for d in(sp,nn)for j,q in d.items()if 9 in E[j]];rows=[[conjbit(x,0)for x in q]for q in known]
 uplus=nullspace(eigrows(hNear,1)+rows);uminus=nullspace(eigrows(hNear,-1)+rows);assert len(uplus)==len(uminus)==1;up,um=uplus[0],uminus[0]
 dp,dm=norm(up),norm(um);a,b=dot(up,gv(s,up)),dot(um,gv(s,um));c=dot(up,gv(s,um))
 assert add(div(a,dp),div(b,dm))==const(F(-2,3)) and div(mul(c,conjbit(c,0)),mul(dp,dm))==const(F(1,8))
 yseeds=[];dets={}
 for branch in (1,-1):
  q=div(mul(dp,add(const(F(1,3)),mul(const(branch),mul(I,div(U,const(12)))))),c);y=va(up,vs(q,um));nf=orbit(nfidx,y);yseeds.append(y)
  assert len(nf)==12 and all(dot(nf[i],nf[j])==Z for i,j in itertools.combinations(nf,2)if adjacent(i,j))
  assert all(dot(nf[i],d[j])==Z for d in(sp,nn)for i in nf for j in d if adjacent(i,j))
  at0=[v for j,v in nf.items()if 0 in E[j]];assert len(at0)==2
  W0=nullspace([[conjbit(x,0)for x in v]for v in at0]);assert len(W0)==4;B0=columns(W0);G0=prod(dag(B0),B0);H=[[neg(G0[i][j])for j in range(4)]for i in range(4)]
  for u in (6,7,11,12):
   L=nullspace(incidence_rows(tuple(sorted((0,u))),nf));assert len(L)==2;BL=columns(L);GL=prod(dag(BL),BL);K=prod(dag(BL),B0);term=prod(prod(dag(K),inv2(GL)),K)
   H=[[add(H[i][j],term[i][j])for j in range(4)]for i in range(4)]
  assert H==dag(H);d=determinant(H);rd=rational(d);assert F(rd)<0;dets[str(branch)]=rd
 distinct=rational(overlap2(yseeds[0],yseeds[1]));assert distinct=='8/9'
 return {'swap':swap,'anchor_rays':len(anc),'near_far_transfer_discriminant_over_determinant':discr,
  'two_distinct_branch_overlap_squared':distinct,'far_vertex_operator_determinant':dets}
results=[check_anchor(False),check_anchor(True)]
expected=[{'swap':False,'anchor_rays':21,'near_far_transfer_discriminant_over_determinant':'-800/729','two_distinct_branch_overlap_squared':'8/9',
 'far_vertex_operator_determinant':{'1':'-7014270/1002001','-1':'-2212249644/523152175'}},
 {'swap':True,'anchor_rays':21,'near_far_transfer_discriminant_over_determinant':'-800/729','two_distinct_branch_overlap_squared':'8/9',
 'far_vertex_operator_determinant':{'1':'-2212249644/523152175','-1':'-7014270/1002001'}}]
assert results==expected
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'anchor_configurations':2,'anchor_rays_each':21,
 'near_far_cycle':path,'intervening_far_vertices':fars,'case_results':results,
 'new_rays_not_assumed_equivariant':True,'status':'PASS'}
(P/'frontier-20261029-g6-fixed21-asymmetric-no-go-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
