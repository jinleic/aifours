#!/usr/bin/env python3
"""Discharge both-root cross matrices forced by specialized minor gates.

Each nonzero rank4 minor or unequal cofactor norm modulo 65521 is an exact
no-solution certificate; equal norms or lower rank are kept unresolved.
"""
import hashlib,json,datetime
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;helper=P/'frontier-20261028-n8-dita-freefree-specializations-v1.py';raw=helper.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='7ef8837f432ea3dd31b744832ac376fafe64d9c11188f036ab9de7bad540e76b'
code=raw.decode().split('T=[json.loads(x)for x in src.read_text().splitlines()]',1)[0]
exec(compile(code,str(helper),'exec'),globals())
src=P/'frontier-20261028-n8-dita-rank2-resultant-survivors-v1.jsonl';cert=P/'frontier-20261028-n8-dita-rank2-root-certificates-v1.jsonl'
T=[json.loads(x)for x in src.read_text().splitlines()];Q=[json.loads(x)for x in cert.read_text().splitlines()];assert len(T)==len(Q)==8192
cnt=Counter();sur=[];cases=0
for row,gate in zip(T,Q):
 assert gate is not None
 if not gate['allowed_8th_root_exponents']:cnt['only_zero_root']+=1;continue
 for k in gate['allowed_8th_root_exponents']:
  a=(-k)%8 if row['alpha']==-1 else row['alpha'];b=k if row['beta']==-1 else row['beta'];cases+=1
  C=mat(row,a,b,w);ids=pivots(C);rank=len(ids)
  if rank==4:cnt['rank4']+=1;continue
  if rank<3:cnt['rank_below3_unresolved']+=1;sur.append({**row,'alpha':a,'beta':b});continue
  v=cof(C,ids);vb=cof(mat(row,a,b,wi),ids)
  if len({x*y%p for x,y in zip(v,vb)})>1:cnt['unequal_norm']+=1
  else:cnt['equal_norm_unresolved']+=1;sur.append({**row,'alpha':a,'beta':b})
(P/'frontier-20261028-n8-dita-onefree-fixed-roots-survivors-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256(raw).hexdigest(),'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'gate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'cases':cases,'counts':dict(cnt),'unresolved':len(sur)}
(P/'frontier-20261028-n8-dita-onefree-fixed-roots-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
