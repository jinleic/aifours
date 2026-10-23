"""Plant a known balanced-after-linear-shift NL>=240 table on a free flat."""
import argparse
import hashlib
import json
from pathlib import Path
from seeds import decode,fwht

p=argparse.ArgumentParser()
p.add_argument('prefix')
p.add_argument('--output',required=True)
a=p.parse_args()
meta=json.loads(Path(a.prefix+'.encoding.json').read_text())
f=decode(meta['seed_hex']); W=fwht(f)
points=meta['points']; selected=None
for origin,w in enumerate(W):
    if abs(w)!=4: continue
    good=[x for x in points if (1-2*(f[x]^(bin(origin&x).count('1')%2)))*w>0]
    if len(good)>=2:
        selected=good[:2]; break
assert selected
g=f.copy()
for x in selected: g[x]^=1
wg=fwht(g)
assert max(map(abs,wg))<=32 and wg[origin]==0
txt=''.join(map(str,g))
Path(a.output).write_text(json.dumps({'bits':txt,'bit_order':'bits[x]=f(x), x=0..511; x_i=(x>>i)&1','sha256_ascii_bits':hashlib.sha256(txt.encode()).hexdigest(),'weight':sum(g),'walsh':wg,'nonlinearity':256-max(map(abs,wg))//2,'flips':selected,'zero_origin':origin,'scope':'Planted free-flat control; becomes balanced after the stated linear shift; relaxed Walsh bound 32 only.'},indent=2)+'\n')
print('Planted points',selected,'zero origin',origin,'max|W|',max(map(abs,wg)))
