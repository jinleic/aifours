#!/usr/bin/env python3
"""Exact proof check where neither weighted endpoint Gram is PSD."""
from fractions import Fraction as F
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy
path='frontier-20261028-grid-unbounded-plane-check.py'
expected='03de2fa6e1670e2f5ab7c7906169ce8da3dcdae7ad00bc25d00a195ee0214ca3'
assert sha256(open(path,'rb').read()).hexdigest()==expected
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert len(json.loads(buf.getvalue())['cases'])==5
O,Z=h['O'],h['Z'];add,neg,mul,conj=h['add'],h['neg'],h['mul'],h['conj']
vec,combine,cross,outer=h['vec'],h['combine'],h['cross'],h['outer']
rank2,psd=h['rank2'],h['psd']
a,b,d,g,e,f,j,k,n=map(F,(1,1,2,3,9,9,9,F(1,10),100))
v0=Z;v2=(F(8,25),F(0));V=F(64,625);p=F(1,2)
A=vec((0,0,O),(1,1,O),(2,2,O));B=vec((0,1,O),(1,2,O))
D=vec((1,0,O),(2,1,neg(O)));V_C=vec((0,2,O),(3,3,O))
E=vec((2,0,O),(3,2,v2));V_F=vec((2,2,v2))
G=vec((3,0,O));V_I=vec((3,2,O));V_H=vec((0,3,O));X=vec((2,0,O));V_Z=vec((2,2,O))
target=[[Z for _ in range(16)] for _ in range(16)]
for w,x in zip((a,b,d,g,e,f,j,k,n),(A,B,D,V_C,E,V_F,G,V_I,V_H)):outer(target,w,x)
actual=[[Z for _ in range(16)] for _ in range(16)]
for z in h['ROOTS']:
 z2=mul(z,z);z3=mul(z2,z)
 q=combine((z,A),(O,B),(z2,D),(neg(z3),X))
 assert rank2(q);outer(actual,p/4,q)
q0=combine((O,A),(neg(O),V_Z));assert rank2(q0);outer(actual,(1-p)/2,q0)
beta=(F(1),F(1));delta=(F(1),F(-1))
for z in h['ROOTS']:
 q=combine((z,A),(z,V_Z),(mul(beta,mul(z,z)),B),(delta,D))
 assert rank2(q);outer(actual,(1-p)/8,q)
for w,x in ((d-1,D),(g,V_C),(n,V_H)):outer(actual,w,x)
t1=(neg(O),Z,v2,Z);t2=(Z,Z,Z,h['div'](O,v2));weights=(e,j,k,f)
H=[]
for i in range(4):
 row=[]
 for q in range(4):
  val=(weights[i] if i==q else F(0),F(0))
  val=add(val,neg(h['scale'](mul(t1[i],conj(t1[q])),p)))
  val=add(val,neg(h['scale'](mul(t2[i],conj(t2[q])),1-p)))
  row.append(val)
 H.append(row)
for i,left in enumerate((E,G,V_I,V_F)):
 for q,right in enumerate((E,G,V_I,V_F)):cross(actual,H[i][q],left,right)
assert all(actual[i][q]==target[i][q] for i in range(16) for q in range(16))
pt=[[target[4*(i//4)+q%4][4*(q//4)+i%4] for q in range(16)] for i in range(16)]
def vec5(*terms):
 v=[Z]*20
 for aa,bb,c in terms:v[5*aa+bb]=add(v[5*aa+bb],c)
 return v
basis5=(vec5((0,0,O),(1,1,O),(2,2,O)),vec5((0,1,O),(1,2,O)),
 vec5((1,0,O),(2,1,neg(O))),vec5((0,2,O),(3,4,O)),
 vec5((2,0,O),(3,3,O)),vec5((2,3,O)),vec5((3,0,O)),vec5((3,2,O)),vec5((0,4,O)))
rho=[[Z for _ in range(20)] for _ in range(20)]
for w,x in zip((a,b,d,g,e,f,j,k,n),basis5):outer(rho,w,x)
pt5=[[rho[5*(i//5)+q%5][5*(q//5)+i%5] for q in range(20)] for i in range(20)]
assert psd(H) is not None and psd(pt) is not None and psd(pt5) is not None
cost1=F(1,e)+V/k;cost2=F(1)/(V*f)
assert cost1==F(1277,1125) and cost2==F(625,576)
print(json.dumps({'source_weights':list(map(str,(a,b,d,g,e,f,j,k,n))),'v0':'0','v2':'8/25',
 'first_cost':str(cost1),'second_cost':str(cost2),'mix_p':str(p),'mixed_gram_pivots':psd(H),
 'projection_pt_pivots':psd(pt),'source_pt_pivots':psd(pt5),'rank2_phase_vectors':9,
 'source_pt_entries_checked':400,'projection_entries_checked':256,'helper_hash':expected,
 'helper_cases_replayed':5},indent=2))
