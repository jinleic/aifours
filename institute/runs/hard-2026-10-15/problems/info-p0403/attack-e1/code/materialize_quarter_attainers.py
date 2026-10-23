"""Explicit balanced attainers from planted quarter-class controls.

Standalone direct character sums; no producing-code imports. Checks
class membership before applying the stated output linear function.
"""
import hashlib
import json
from pathlib import Path

batch=json.loads(Path('results/free128-batch.json').read_text())
assert batch['complete'] and len(batch['cases'])==12
for case in batch['cases']:
    meta=json.loads(Path(case['prefix']+'.encoding.json').read_text())
    control=json.loads(Path(case['control_prefix']+'-input.json').read_text())
    g=list(map(int,control['bits']))
    f=[int(b) for ch in meta['seed_hex'] for b in format(int(ch,16),'04b')]
    domain=set(meta['points'])
    assert all(g[x]==f[x] for x in range(512) if x not in domain)
    origin=control['zero_origin']
    balanced=[g[x]^(bin(x&origin).count('1')%2) for x in range(512)]
    assert sum(balanced)==256
    W=[sum((-1)**(balanced[x]+(bin(a&x).count('1')%2)) for x in range(512)) for a in range(512)]
    assert max(map(abs,W))==32 and W[0]==0
    text=''.join(map(str,balanced))
    out={'bits':text,'bit_order':'bits[x]=f(x), x=0..511; x_i=(x>>i)&1','sha256_ascii_bits':hashlib.sha256(text.encode()).hexdigest(),'weight':256,'walsh':W,'nonlinearity':240,'class_prefix':case['prefix'],'linear_shift':origin,'scope':'Exact maximum attainer for this restricted quarter-table class, not a headline 242 witness.'}
    path=case['control_prefix']+'-balanced-attainer.json'
    Path(path).write_text(json.dumps(out,indent=2)+'\n')
    print(case['prefix'],'balanced NL240 attainer',path)
