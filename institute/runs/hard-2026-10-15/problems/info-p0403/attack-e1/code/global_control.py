"""Normalize a known balanced NL=240 control to support XOR=e0."""
import hashlib
import json
from pathlib import Path
from seeds import fwht

source=json.loads(Path('results/heuristic-best.json').read_text())
f=list(map(int,source['bits']))
v=0
for x,b in enumerate(f):
    if b: v^=x
assert v and v&(v-1)==0
j=v.bit_length()-1
def permutation(x):
    t=((x>>0)^(x>>j))&1
    return x^(t<<0)^(t<<j)
g=[f[permutation(x)] for x in range(512)]
if g[0]: g=[1-b for b in g]
txt=''.join(map(str,g)); W=fwht(g)
vnew=0
for x,b in enumerate(g):
    if b: vnew^=x
assert sum(g)==256 and max(map(abs,W))==32 and vnew==1 and g[0]==0
parity=[(w//4)%2 for w in W]
assert parity==[a&1 for a in range(512)]
q=[(w//8)%2 for w in W]
coeff=q.copy()
for i in range(9):
    for mask in range(512):
        if mask&(1<<i): coeff[mask]^=coeff[mask^(1<<i)]
assert all(not b or bin(mask).count('1')<=2 for mask,b in enumerate(coeff))
out={'bits':txt,'bit_order':'bits[x]=f(x), x=0..511; x_i=(x>>i)&1','sha256_ascii_bits':hashlib.sha256(txt.encode()).hexdigest(),'weight':sum(g),'walsh':W,'nonlinearity':240,'support_xor':vnew,'scope':'planted relaxed-bound control only, not a target witness','quadratic_spectral_bit_coefficients':[m for m,b in enumerate(coeff) if b]}
Path('results/global-planted240.json').write_text(json.dumps(out,indent=2)+'\n')
print('Control: balanced NL240, f(0)=0, support XOR=1, quadratic spectral bit checked.')
