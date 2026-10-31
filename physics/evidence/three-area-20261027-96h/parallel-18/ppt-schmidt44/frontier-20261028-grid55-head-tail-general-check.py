#!/usr/bin/env python3
"""Exact nontrivial parameter checks for the six universal head-tail families."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
from itertools import product
import io,json,runpy
path='frontier-20261028-grid55-head-tail-check.py'
expected='985dc982c8be4e5e1a8693d91bcf1caced6d04601fc57586dc3f56ea6de13442'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['alice_and_bob_outputs']==12
O,Z=h['O'],h['Z'];add,neg,mul,conj=h['add'],h['neg'],h['mul'],h['conj']
combine,outer,psd,rank2=h['combine'],h['outer'],h['psd'],h['rank2']
basis,weights,roots,scale=h['basis'],h['weights'],h['roots'],h['scale']; cross=h['cross']
def projected(edges,head,tail,r,side):
 v=[Z]*20;keep=[i for i in range(5) if i!=tail]
 for a,b in edges:
  if side=='alice':coeff=r if a==tail else O;aa=head if a==tail else a;k=5*keep.index(aa)+b
  else:coeff=r if b==tail else O;bb=head if b==tail else b;k=4*a+keep.index(bb)
  v[k]=add(v[k],coeff)
 return v
def nm():return [[Z for _ in range(20)] for _ in range(20)]
cases=[]
for head,tail in product(range(3),(3,4)):
 pair=(head,tail)
 if pair==(0,3): r=(F(2),F(0))
 elif pair==(1,4):r=(F(3,4),F(0))
 else:r=(F(1),F(1))
 R=r[0]**2+r[1]**2;v=[projected(q,head,tail,r,'alice') for q in basis]
 target=nm();actual=nm()
 for wt,q in zip(weights,v):outer(target,wt,q)
 if pair in ((0,4),(2,3)):
  loop,edge=(3,6) if pair==(0,4) else (2,4)
  for z in roots:
   q=combine((O,v[0]),(z,v[loop]),(conj(z),v[edge]));assert rank2(q,4,5);outer(actual,F(1,4),q)
  excluded={0,loop,edge}
 elif pair in ((1,3),(2,4)):
  loop,edge,overlap,other=(2,4,9,5) if pair==(1,3) else (3,6,10,8)
  row=[i for i in range(5) if i!=tail].index(head);X=[Z]*20;Y=[Z]*20
  X[5*row+(2 if pair==(1,3) else 1)]=O;Y[5*row+(4 if pair==(1,3) else 3)]=O
  for z in roots:
   q=combine((O,v[0]),(z,v[loop]),(conj(z),X));assert rank2(q,4,5);outer(actual,F(1,4),q)
  b,f,hh=weights[edge],weights[overlap],weights[other]
  H=[[(b+f*R-1,F(0)),scale(conj(r),b)],[scale(r,b),(b*R+hh,F(0))]]
  assert psd(H) is not None
  for i,left in enumerate((X,Y)):
   for j,right in enumerate((X,Y)):cross(actual,H[i][j],left,right)
  excluded={0,loop,edge,overlap,other}
 else:
  loop,edge,overlap,other=(2,4,9,5) if pair==(0,3) else (3,6,10,8)
  invr=(r[0]/R,-r[1]/R)
  q1=combine((O,v[0]),(neg(invr),v[overlap]));assert rank2(q1,4,5)
  if pair==(0,3):s=F(1,9);p=1-s;lam=F(8);bp=F(3);kp=F(3);hp=(F(2),F(0))
  else:s=F(16,25);p=1-s;lam=F(9,16);bp=F(5,4);kp=F(5,4);hp=(F(3,4),F(0))
  outer(actual,p,q1)
  for z in roots:
   q=combine((O,v[0]),(scale(invr,lam),v[overlap]),(scale(z,bp),v[loop]),
             (scale(conj(z),kp),v[edge]),(mul(mul(z,z),hp),v[other]))
   assert rank2(q,4,5);outer(actual,s/4,q)
  used_other=s*(hp[0]**2+hp[1]**2)
  assert used_other<=weights[other]
  outer(actual,weights[other]-used_other,v[other])
  excluded={0,loop,edge,overlap,other}
 for i,(wt,q) in enumerate(zip(weights,v)):
  if i not in excluded:
   assert rank2(q,4,5);outer(actual,wt,q)
 assert all(actual[i][j]==target[i][j] for i in range(20) for j in range(20))
 pt=[[target[5*(i//5)+j%5][5*(j//5)+i%5] for j in range(20)] for i in range(20)]
 assert psd(pt) is not None
 vb=[projected(q,head,tail,r,'bob') for q in basis];tb=nm()
 for wt,q in zip(weights,vb):outer(tb,wt,q)
 assert tb==[[target[5*(i%4)+i//4][5*(j%4)+j//4] for j in range(20)] for i in range(20)]
 ptb=[[tb[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(20)] for i in range(20)]
 assert psd(ptb) is not None
 cases.append({'head':head,'tail':tail,'r':list(map(str,r)),'alice_entries':400,'bob_entries':400,
               'alice_pt_rank':len(psd(pt)),'bob_pt_rank':len(psd(ptb))})
print(json.dumps({'cases':cases,'alice_bob_outputs':12,'total_entries_checked':4800,'all_pt_psd':True,
 'previous_representatives_replayed':True,'previous_checker_sha256':expected},indent=2))
