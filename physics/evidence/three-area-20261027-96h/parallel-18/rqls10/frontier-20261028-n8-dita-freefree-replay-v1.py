#!/usr/bin/env python3
"""Independently regenerate FREE/FREE parity-block rejections and survivor list."""
import datetime,hashlib,itertools,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;helper=P/'frontier-20261028-n8-dita-generic-full-replay-v1.py';helper_raw=helper.read_bytes()
assert hashlib.sha256(helper_raw).hexdigest()=='508d571aac0a0fe0118ddb0ad2f0b868acf1688cd945c5925a247ceb954e84a1'
exec(compile(helper_raw.decode().split('cnt=Counter();residual=[];FF=[];',1)[0],str(helper),'exec'),globals())
src=P/'frontier-20261028-n8-dita-generic-full-replay-freefree-v1.jsonl';lines=src.read_text().splitlines();assert len(lines)==57344
cnt=Counter();sur=[]
for line in lines:
 row=json.loads(line);O,R0,R1,M=(tuple(row[k])for k in ('O','R0','R1','mu'));C=cross(O,R0,R1,M,0,0,W,0);Cb=cross(O,R0,R1,M,0,0,WB,0);blocks=[];why=None
 for bp in range(2):
  for cp in range(2):
   ids=[4*b+c for b in range(bp,4,2)for c in range(cp,4,2)];A=[C[i]for i in ids];ix=pivot(A)
   if len(ix)==4:why='block_rank4';break
   if len(ix)==3:
    v=cof(A,ix);vb=cof([Cb[i]for i in ids],ix)
    if len({x*y%p for x,y in zip(v,vb)})>1:why='unequal_unit_norms';break
    blocks.append((bp,cp,v))
  if why:break
 if why:cnt[why]+=1;continue
 for (bp,cp,v),(bq,cq,u) in itertools.combinations(blocks,2):
  db,dc=bp-bq,cp-cq
  if any((v[i]*u[j]-v[j]*u[i])%p for i,j in itertools.combinations(range(4),2) if (not db or i%2==j%2) and (not dc or M[i]%2==M[j]%2)):
   why='phase_invariant_pair';break
  pairs=list(itertools.combinations(range(4),2))
  if any((v[i]*v[j]*u[k]*u[l]-v[k]*v[l]*u[i]*u[j])%p for (i,j),(k,l) in itertools.combinations(pairs,2) if (not db or i%2+j%2==k%2+l%2) and (not dc or M[i]%2+M[j]%2==M[k]%2+M[l]%2)):
   why='phase_invariant_quartic';break
 if why:cnt[why]+=1
 else:cnt['unresolved']+=1;sur.append(row)
(P/'frontier-20261028-n8-dita-freefree-replay-survivors-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256(helper_raw).hexdigest(),'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'counts':dict(cnt),'unresolved':len(sur)}
(P/'frontier-20261028-n8-dita-freefree-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
