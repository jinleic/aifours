#!/usr/bin/env python3
"""Integer-only primality, primitive eighth root and conjugate checks."""
import datetime,hashlib,json,math
from pathlib import Path
P=Path(__file__).resolve().parent;p=65521;w=57852;bar=8031
s=math.isqrt(p);assert s==255 and s*s<p<(s+1)*(s+1)
assert all(p%d for d in range(2,s+1))
assert pow(w,4,p)==p-1 and pow(w,8,p)==1 and w*bar%p==1 and pow(bar,4,p)==p-1
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'prime':p,'integer_sqrt':s,
 'root':w,'inverse_root':bar,'integer_trial_divisors_checked':s-1}
(P/'frontier-20261028-n8-dita-prime-check-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
