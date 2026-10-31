#!/usr/bin/env python3
"""Independent bounded replay of normalized n8 F4/F4-Diţă all-phase no-T.

Regenerate every ordering, same-group row assignment and mu; exact Phi8
balances for same groups; independently find modular pivot rows and compare
cofactor norms at conjugate primitive roots for all remaining branches.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
P=Path(__file__).resolve().parent;p=65521
assert all(p%d for d in range(2,int(p**.5)+1))
w=next(pow(g,(p-1)//8,p) for g in range(2,p) if pow(pow(g,(p-1)//8,p),4,p)==p-1);wi=pow(w,-1,p)
assert w==57852 and wi==8031
perms3=list(itertools.permutations(range(1,8),3));muall=[(0,)+u for u in itertools.permutations((1,2,3))]
def allowed(O,M):
 out=[[False]*8 for _ in range(4)]
 for d in range(1,4):
  for delta in range(1,8):
   v=[0]*4
   for tau in range(8):
    e=(delta*tau+2*d*M[O[tau]%4])%8;v[e%4]+=1 if e<4 else -1
   out[d][delta]=not any(v)
 return out
def ok(R,A):return all(A[c-b][(R[c]-R[b])%8] for b in range(4)for c in range(b+1,4))
def mat(O,R0,R1,M,w):
 loc=[[0]*4 for _ in range(2)]
 for tau,x in enumerate(O):loc[x//4][x%4]=tau
 return [[(pow(w,(R1[c]-R0[b])*loc[0][t]+2*(M[t]*c-t*b),p)-pow(w,(R1[c]-R0[b])*loc[1][t]+2*(M[t]*c-t*b),p))%p for t in range(4)] for b in range(4)for c in range(4)]
def pivots(A):
 basis=[];ids=[]
 for i,row in enumerate(A):
  v=row[:]
  for k,b in basis:
   h=v[k];v=[(a-h*x)%p for a,x in zip(v,b)]
  k=next((j for j,x in enumerate(v) if x),None)
  if k is None:continue
  x=pow(v[k],-1,p);v=[a*x%p for a in v];basis.append((k,v));ids.append(i)
  if len(ids)==4:break
 return ids
def det3(a):
 return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%p
def cof(A,ix):
 out=[]
 for k in range(4):
  cols=[j for j in range(4)if j!=k];d=det3([[A[i][j]for j in cols]for i in ix]);out.append(d if k%2==0 else (-d)%p)
 return out
start=time.monotonic();nO=h0=both=full=unequal=0;other=[]
for perm in itertools.permutations(range(1,8)):
 O=(0,)+perm;nO+=1;A0=allowed(O,(0,1,2,3));As=[allowed(O,M)for M in muall]
 for p0 in perms3:
  R0=(0,)+p0
  if not ok(R0,A0):continue
  h0+=1;rest=[x for x in range(1,8)if x not in p0]
  for R1 in itertools.permutations(rest):
   for M,A1 in zip(muall,As):
    if not ok(R1,A1):continue
    both+=1;C=mat(O,R0,R1,M,w);ix=pivots(C)
    if len(ix)==4:full+=1;continue
    assert len(ix)==3
    Cbar=mat(O,R0,R1,M,wi);u=cof(C,ix);v=cof(Cbar,ix)
    if len({(a*b)%p for a,b in zip(u,v)})>1:unequal+=1
    else:other.append((O,R0,R1,M))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'elapsed_seconds':round(time.monotonic()-start,6),
 'prime':p,'w':w,'conjugate_root':wi,'orderings':nO,'same_h0':h0,'same_both':both,
 'rank4':full,'rank3_unequal_norm':unequal,'unresolved':len(other),'samples':other[:4]}
(P/'frontier-20261028-n8-dita-allphase-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
