#!/usr/bin/env python3
"""Exact F2 incidence kernels and independent 2-color quotient enumeration."""
import datetime,hashlib,importlib.util,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;w=P/'frontier-20261028-ols10-switch-v1.py';q=P/'frontier-20261028-parker-13ray-result-v1.json'
spec=importlib.util.spec_from_file_location('w',w);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.check_table()
W=[[m.TABLE[r][c][1]for c in range(10)]for r in range(10)];data=json.loads(q.read_bytes())['partial_witness'];R=data['labels'];assert data['denominator']==3
assert len(data['array'])==10 and all(len(row)==10 for row in data['array']) and all(len(v)==10 and all(isinstance(x,int) for x in v) for row in data['array'] for v in row)
CY=[[(r-c)%10 for c in range(10)]for r in range(10)]
def validate(L):
 n=len(L);target=set(range(n));assert all(set(row)==target for row in L);assert all({L[r][c]for r in range(n)}==target for c in range(n))
def basis(L):
 n=len(L);B={}
 for r in range(n):
  for c in range(n):
   x=(1<<r)|(1<<(n+c))|(1<<(2*n+L[r][c]))
   while x:
    i=x.bit_length()-1
    if i in B:x^=B[i]
    else:B[i]=x;break
 out=[]
 for f in range(3*n):
  if f in B:continue
  x=1<<f
  for i in sorted(B):
   if (B[i]&x).bit_count()%2:x^=1<<i
  assert all(((x>>r)^(x>>(n+c))^(x>>(2*n+L[r][c])))&1==0 for r in range(n)for c in range(n));out.append(x)
 return out
def quotient(L):
 n=len(L);out=[]
 for mask in range(1<<n):
  h=[(mask>>l)&1 for l in range(n)];b=[h[L[0][c]]for c in range(n)];a=[h[L[r][0]]^b[0]for r in range(n)]
  if all((a[r]^b[c]^h[L[r][c]])==0 for r in range(n)for c in range(n)):out.append({'a':a,'b':b,'h':h})
 return out
summary={}
for name,L in [('cyclic',CY),('Weisner_Fig1',W),('Parker',R)]:
 validate(L);B=basis(L);Q=quotient(L)
 assert len(Q)*2==2**len(B)
 summary[name]={'dimension':len(B),'basis_weights':[x.bit_count()for x in B],
                'odd_kernel_exists':any(x.bit_count()%2 for x in B),'a0_zero_quotients':len(Q),'nonconstant_quotients':sum(len(set(x['h']))>1 for x in Q)}
a=[r%2 for r in range(10)];b=[c%2 for c in range(10)];h=[l%2 for l in range(10)]
weights=[a[r]+b[c]+h[CY[r][c]]for r in range(10)for c in range(10)]
assert set(weights)=={0,2} and weights.count(0)==25 and weights.count(2)==75
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'Weisner_loader_sha256':hashlib.sha256(w.read_bytes()).hexdigest(),'Parker_witness_sha256':hashlib.sha256(q.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'cases':summary,
 'cyclic_odd_contexts':sum(a)+sum(b)+sum(h),'cyclic_cell_occurrences':{'0':weights.count(0),'2':weights.count(2)},
 'Parker_projector_denominator_divides':9,'status':'PASS'}
(P/'frontier-20261028-resolution-parity-code-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
