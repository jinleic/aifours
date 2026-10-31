#!/usr/bin/env python3
"""Exact structural checks for the 4x12 Horodecki-crosshatch SN3 source."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-hor-crosshatch-coordinate-phase-verify.py'
expected='603aa8aef5591211fbaee1379b9cbb30f842a7ff87270e113c9513c179b9beed'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['coordinate_cuts']==495
Z,O=h['Z'],h['O'];add,mul,psd=h['add'],h['mul'],h['psd'];HQ=h['source'];HR=h['HR'];HPT=h['HPT']
assert len(psd(HR))==len(psd(HPT))==5
nulls=[]
v=[Z]*8;v[0]=(F(-1),F(0));v[5]=O;nulls.append(v)
v=[Z]*8;v[1]=(F(-1),F(0));v[6]=O;nulls.append(v)
v=[Z]*8;v[2]=(F(-1),F(0));v[4]=(F(0),F(-1,2));v[7]=O;nulls.append(v)
for v in nulls:
 for i in range(8):
  y=Z
  for j in range(8):y=add(y,mul(HPT[i][j],v[j]))
  assert y==Z
core=[12*a+b for a in (1,3) for b in (0,3,6,9)]
C=[[Z for _ in range(8)] for _ in range(8)]
for q in HQ:
 for i,x in enumerate(core):
  for j,y in enumerate(core):C[i][j]=add(C[i][j],mul(q[x],q[y]))
assert C==HR
# Linear identities verified on each source ket, hence on its entire range.
for q in HQ:
 for j in (1,4,7,10):
  assert q[12+j]==Z and q[36+j]==Z
 for k,j in enumerate((1,4,7,10)):
  assert q[j-1]==q[24+j]
 for k,j in enumerate((0,3,6,9)):
  assert q[12+j]==q[3*k+2]
 rows={i for i in range(4) if any(q[12*i+j]!=Z for j in range(12))}
 assert len(rows)<=3
# Compare the stated Eq.8 tensor projection against printed Eq.36 in its
# stated relabeling; this is a provenance check, not part of the SN3 proof.
S=h['S']
def pk(*terms):
 v=[Z]*48
 for a,b,c in terms:v[12*a+b]=add(v[12*a+b],c)
 return v
paper=[pk((2,0,S),(2,3,O)),pk((2,8,S),(2,11,O))]
for i in range(3):paper.append(pk((0,9+i,O),(1,i,O),(2,1+i,O)))
paper.append(pk((0,1,O),(3,8,O)))
for i in range(3):paper.append(pk((1,9+i,O),(2,8+i,O),(3,1+i,O)))
paper.append(pk((0,3,O),(1,8,O)))
for i in range(8):paper.append(pk((0,4+i,O),(3,i,O)))
assert len(paper)==18
ours=[[Z for _ in range(48)] for _ in range(48)]
printed=[[Z for _ in range(48)] for _ in range(48)]
for q in HQ:
 v=[Z]*48
 for k,x in enumerate(q):
  a,b=divmod(k,12);aa=(0,1,3,2)[a];bh,bq=divmod(b,3)
  v[12*aa+bh+4*bq]=add(v[12*aa+bh+4*bq],x)
 h['outer'](ours,v)
for v in paper:h['outer'](printed,v)
diffs=[(i,j) for i in range(48) for j in range(48) if ours[i][j]!=printed[i][j]]
assert len(diffs)==90 and ours[9][9]==O and printed[9][9]==(F(2),F(0))
assert sum(ours[i][i][0] for i in range(48))==sum(printed[i][i][0] for i in range(48))==44
print(json.dumps({'horodecki_rank':5,'horodecki_pt_rank':5,'kernel_vectors_checked':3,
 'horodecki_core_entries_checked':64,'source_generators':20,'source_support_relations_per_generator':16,
 'all_source_kets_at_most_three_alice_rows':True,'preceding_495_coordinate_cuts_replayed':True,
 'paper_eq36_difference_entries':len(diffs),'paper_09_diagonal_ours':'1','paper_09_diagonal_eq36':'2',
 'coefficient_field':'Q(sqrt2)','previous_checker_sha256':expected,
 'limits':'SN3 follows from the written product-range and 4x12 core argument; no 4x4 claim.'},indent=2))
