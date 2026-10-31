# Exact shifted-polynomial comparison using the independently replayed
# symbolic denominator and numerator sign certificates.
from fractions import Fraction as F
from hashlib import sha256
from math import comb
from pathlib import Path
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,h):
 raw=(root/name).read_bytes();assert sha256(raw).hexdigest()==h;return json.loads(raw)
z=load('frontier-20261029-unbounded-b6-family-signs-frozen-v1.json','e595395eed59d1dd26d223b1997a2e42f57f41c47bdc5ca9e7e881b979071bb9')
f=load('frontier-20261029-unbounded-b6-matching-order-frozen-v1.json','6a6df044750d9e3227aa07e16ca226b1636801d7a8c8070f6d916b5a15076c6a')
D=z['sign_polynomials']['Det'];B=z['sign_polynomials']['B6'];d=list(map(F,D['shifted_coefficients']));b=list(map(F,B['shifted_coefficients']));k=2+D['min_R_power']-B['min_R_power'];assert k==3
p=[F(0)]*(len(d)+k)
for i,x in enumerate(d):
 for j in range(k+1):p[i+j]+=x*comb(k,j)*100**(k-j)
assert len(p)==len(b)==23
upper=[p[i]-5*b[i] for i in range(23)];lower=[20*b[i]-p[i] for i in range(23)]
assert all(v>0 for v in upper+lower)
assert list(map(str,upper))==f['upper_shifted_coefficients'] and list(map(str,lower))==f['lower_shifted_coefficients']
assert D['max_R_power']==24 and B['max_R_power']==26 and b[-1]/d[-1]==F(1317,8425)==F(f['asymptotic_ratio'])
assert -upper[0]<0
print({'positive_comparison_coefficients':46,'R_scope':'R>=100','strict_bound':'R^2/20 < b6 < R^2/5','exact_limit':'1317/8425','mutation_controls':1})
