#!/usr/bin/env python3
"""Regenerate one-free and specialized FF linear/rank gates independently."""
import datetime,hashlib,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;helper=P/'frontier-20261028-n8-dita-generic-full-replay-v1.py';helper_raw=helper.read_bytes()
assert hashlib.sha256(helper_raw).hexdigest()=='508d571aac0a0fe0118ddb0ad2f0b868acf1688cd945c5925a247ceb954e84a1'
exec(compile(helper_raw.decode().split('cnt=Counter();residual=[];FF=[];',1)[0],str(helper),'exec'),globals())
def gate(row):
 O,R0,R1,M=(tuple(row[k])for k in ('O','R0','R1','mu'));a,b=row['alpha'],row['beta'];assert (a==-1)!=(b==-1)
 mode=1 if a==-1 else 2;aa=0 if a==-1 else a;bb=0 if b==-1 else b
 C=cross(O,R0,R1,M,aa,bb,W,mode);ids=pivot(C);r=len(ids)
 if r==4:return 'rank4'
 if r<3:return 'unresolved'
 v=cof(C,ids);vb=cof(cross(O,R0,R1,M,aa,bb,WB,mode),ids)
 if len({x*y%p for x,y in zip(v,vb)})>1:return 'unequal_norm'
 plus=cross(O,R0,R1,M,aa,bb,W,0);minus=cross(O,R0,R1,M,4 if a==-1 else a,4 if b==-1 else b,W,0)
 U=[sum(x*y for x,y in zip(q,v))%p for q in plus];V=[sum(x*y for x,y in zip(q,v))%p for q in minus]
 A=[(x+y)%p for x,y in zip(U,V)];B=[(x-y)%p for x,y in zip(U,V)]
 if any((A[i]*B[j]-A[j]*B[i])%p for i in range(16)for j in range(i+1,16)):return 'inconsistent_linear'
 if not any(B) and any(A):return 'nonzero_constant'
 return 'unresolved'
source1=P/'frontier-20261028-n8-dita-generic-full-replay-unresolved-v1.jsonl';T=[json.loads(x)for x in source1.read_text().splitlines()];assert len(T)==40960
c1=Counter();u1=[]
for row in T:
 q=gate(row);c1[q]+=1
 if q=='unresolved':u1.append(row)
assert ''.join(json.dumps(x,separators=(',',':'))+'\n'for x in u1).encode()==(P/'frontier-20261028-n8-dita-rank2-resultant-survivors-v1.jsonl').read_bytes()
source2=P/'frontier-20261028-n8-dita-freefree-replay-survivors-v1.jsonl';cert=P/'frontier-20261028-n8-dita-freefree-separable-full-certs-v1.jsonl'
T=[json.loads(x)for x in source2.read_text().splitlines()];Q=[json.loads(x)for x in cert.read_text().splitlines()];assert len(T)==len(Q)==30720
c2=Counter();u2=[];cases=0
for ix,(row,q) in enumerate(zip(T,Q)):
 if q is None:c2['no_separable_gate']+=1;continue
 if not q['x_roots'] and not q['y_roots']:c2['nonzero_monomial']+=1;continue
 for a,b in [((-k)%8,-1)for k in q['x_roots']]+[(-1,k)for k in q['y_roots']]:
  cases+=1;case={**row,'alpha':a,'beta':b,'parent_index':ix};v=gate(case);c2[v]+=1
  if v=='unresolved':u2.append(case)
assert ''.join(json.dumps(x,separators=(',',':'))+'\n'for x in u2).encode()==(P/'frontier-20261028-n8-dita-freefree-specializations-survivors-v1.jsonl').read_bytes()
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256(helper_raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'onefree_counts':dict(c1),'onefree_survivors':len(u1),'ff_counts':dict(c2),'ff_specializations':cases,'ff_survivors':len(u2),'status':'PASS'}
(P/'frontier-20261028-n8-dita-linear-gate-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
