#!/usr/bin/env python3
"""Exact all six head-tail kernel representatives on both subsystems."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
from itertools import product
import io,json,runpy
path='frontier-20261028-grid55-single-coordinate-check.py'
expected='963dd8014c9f614b02433168325e37293f1375c8c2482f3da5bd3b6b35c7660f'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['cases_count']==10
O,Z=h['O'],h['Z'];add,neg,mul,conj=h['add'],h['neg'],h['mul'],h['conj']
combine,outer,psd,rank2=h['combine'],h['outer'],h['psd'],h['rank2rect']
basis,roots,scale=h['basis'],h['roots'],h['scale']
weights=tuple(map(F,(1,1,1,1,1,1,1,1,2,2,1)))
def projected(edges,head,tail,side):
 v=[Z]*20
 keep=[x for x in range(5) if x!=tail]
 for a,b in edges:
  if side=='alice':aa=head if a==tail else a;k=5*keep.index(aa)+b
  else:bb=head if b==tail else b;k=4*a+keep.index(bb)
  v[k]=add(v[k],O)
 return v
def transpose(v):return [v[5*j+i] for i in range(5) for j in range(4)]
def cross(m,c,v,w):
 for i,x in enumerate(v):
  for j,y in enumerate(w):m[i][j]=add(m[i][j],mul(c,mul(x,conj(y))))
def newmatrix():return [[Z for _ in range(20)] for _ in range(20)]
cases=[]
for head,tail in product(range(3),(3,4)):
 v=[projected(q,head,tail,'alice') for q in basis]
 target=newmatrix();actual=newmatrix()
 for wt,q in zip(weights,v):outer(target,wt,q)
 pair=(head,tail); excluded=set()
 if pair in ((0,4),(2,3)):
  loop,edge=(3,6) if pair==(0,4) else (2,4)
  for z in roots:
   q=combine((O,v[0]),(z,v[loop]),(conj(z),v[edge]));assert rank2(q,4,5);outer(actual,F(1,4),q)
  excluded={0,loop,edge}
 elif pair in ((1,3),(2,4)):
  loop,edge,overlap,other=(2,4,9,5) if pair==(1,3) else (3,6,10,8)
  row=[i for i in range(5) if i!=tail].index(head)
  X=[Z]*20;Y=[Z]*20
  X[5*row+(2 if pair==(1,3) else 1)]=O
  Y[5*row+(4 if pair==(1,3) else 3)]=O
  for z in roots:
   q=combine((O,v[0]),(z,v[loop]),(conj(z),X));assert rank2(q,4,5);outer(actual,F(1,4),q)
  # residual Gram of b[X+Y]+f[X]+h[Y]-[X]
  b,f,hh=weights[edge],weights[overlap],weights[other]
  H=[[(b+f-1,F(0)),(b,F(0))],[(b,F(0)),(b+hh,F(0))]]
  assert psd(H) is not None
  for i,left in enumerate((X,Y)):
   for j,right in enumerate((X,Y)):cross(actual,H[i][j],left,right)
  excluded={0,loop,edge,overlap,other}
 else:
  loop,edge,overlap,other=(2,4,9,5) if pair==(0,3) else (3,6,10,8)
  q1=combine((O,v[0]),(neg(O),v[overlap]));assert rank2(q1,4,5);outer(actual,F(1,2),q1)
  bp=(F(1),F(1));kp=(F(1),F(-1));hp=(F(0),F(-1))
  for z in roots:
   q=combine((O,v[0]),(O,v[overlap]),(mul(z,bp),v[loop]),
             (mul(conj(z),kp),v[edge]),(mul(mul(z,z),hp),v[other]))
   assert rank2(q,4,5);outer(actual,F(1,8),q)
  if weights[overlap]>1:outer(actual,weights[overlap]-1,v[overlap])
  if weights[other]>F(1,2):outer(actual,weights[other]-F(1,2),v[other])
  excluded={0,loop,edge,overlap,other}
 for i,(wt,q) in enumerate(zip(weights,v)):
  if i not in excluded:
   assert rank2(q,4,5);outer(actual,wt,q)
 assert all(actual[i][j]==target[i][j] for i in range(20) for j in range(20))
 pt=[[target[5*(i//5)+j%5][5*(j//5)+i%5] for j in range(20)] for i in range(20)]
 assert psd(pt) is not None
 # Source is swap-invariant, so actual Bob cut equals transpose of Alice cut.
 vb=[projected(q,head,tail,'bob') for q in basis];tb=newmatrix()
 for wt,q in zip(weights,vb):outer(tb,wt,q)
 ttarget=[[target[5*(i%4)+i//4][5*(j%4)+j//4] for j in range(20)] for i in range(20)]
 assert tb==ttarget
 ptb=[[tb[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(20)] for i in range(20)]
 assert psd(ptb) is not None
 cases.append({'kernel':f'|{tail}>-|{head}>','alice_entries':400,'bob_entries':400,
               'alice_pt_rank':len(psd(pt)),'bob_pt_rank':len(psd(ptb)),'branch':str(pair)})
print(json.dumps({'cases':cases,'alice_and_bob_outputs':12,'total_entries_checked':4800,
 'all_pt_psd':True,'source_trace':18,'previous_checker_sha256':expected,'previous_cases_replayed':10},indent=2))
