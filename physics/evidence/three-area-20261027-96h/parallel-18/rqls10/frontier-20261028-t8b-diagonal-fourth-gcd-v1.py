#!/usr/bin/env python3
"""Screen 96 third-pair-degenerate cases by all 5 row-2 column choices.

Modular/peeled gcd only, not a proof. Rows0,1,2,7 have columns0,c,e,d.
"""
import datetime,hashlib,json
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;helper=P/'frontier-20261028-t8b-diagonal-third-gcd-v1.py';third_raw=helper.read_bytes()
assert hashlib.sha256(third_raw).hexdigest()=='a16b78583d502001f2129afb7d9f7395a863eaf1137b598ae8c148d4d97818e8'
exec(compile(third_raw.decode().split('for row in items:',1)[0],str(helper),'exec'),globals())
src=P/'frontier-20261028-t8b-diagonal-third-gcd-retained-v1.jsonl';rows=[json.loads(x)for x in src.read_text().splitlines()];assert len(rows)==2112
cnt=Counter();ret=[]
def gram(O,c,d,delta):
 v=[0]*13
 for tau in range(8):
  sc,kc,dc=K[O[tau]][c];sd,kd,dd=K[O[tau]][d];shift=kd-kc+3;z=pow(w,(delta*tau)%8,p)
  for e,k in F[dd-dc].items():v[e+shift]=(v[e+shift]+sc*sd*k*z)%p
 while len(v)>1 and not v[0]:v=v[1:]
 return peel(v)
for row in rows:
 O=tuple(row['O']);c,d=row['c'],row['d'];A,B=c0polys(O)[c-1][0],c0polys(O)[d-1][1];C=third(O,c,d)
 if C!=[0] and C[-1]:continue
 cnt['input_degenerate']+=1
 for e in range(1,8):
  if e in (c,d):continue
  g=gcd(A,B)
  for u,v,delta in [(0,e,2),(c,e,1),(d,e,3)]:
   q=gram(O,u,v,delta)
   if q!=[0]:g=gcd(g,q)
  degree=len(g)-1;cnt['degree_'+str(degree)]+=1
  if degree:
   if degree==1:
    x=(-g[0]*pow(g[1],-1,p))%p;ks=[k for k in range(8)if pow(w,k,p)==x]
    cnt['root8' if ks else 'nonroot8']+=1
   ret.append({**row,'e':e,'degree':degree})
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256(third_raw).hexdigest(),'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'counts':dict(cnt),'retained':len(ret),
 'warning':'modular gcd screen only; exact no-go not inferred'}
(P/'frontier-20261028-t8b-diagonal-fourth-gcd-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
(P/'frontier-20261028-t8b-diagonal-fourth-gcd-retained-v1.jsonl').write_text(''.join(json.dumps(x,separators=(',',':'))+'\n'for x in ret))
print(json.dumps(obj,indent=2))
