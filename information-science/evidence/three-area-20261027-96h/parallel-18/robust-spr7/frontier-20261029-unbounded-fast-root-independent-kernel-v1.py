# Exact degree/leading-coefficient inference from the previously replayed
# determinant sign manifest; root convergence is a written deduction.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-unbounded-b6-family-signs-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='e595395eed59d1dd26d223b1997a2e42f57f41c47bdc5ca9e7e881b979071bb9';z=json.loads(raw)['sign_polynomials'];D=z['Det'];B=[z['B%d'%j] for j in range(8)]
assert B[7]==D and D['max_R_power']==24
growth=[B[j]['max_R_power']-D['max_R_power'] for j in range(8)];assert growth==[2,3,4,3,4,2,2,0]
scale=[growth[j]+2*j-14 for j in range(8)];assert scale==[-12,-9,-6,-5,-2,-2,0,0]
c=F(B[6]['shifted_coefficients'][-1])/F(D['shifted_coefficients'][-1]);assert c==F(1317,8425)>0
assert not (scale[5]==0)
print({'numerator_coefficient_growth_exponents':growth,'scaled_polynomial_exponents':scale,'coefficientwise_limit':'z^7+(1317/8425)*z^6','mutation_controls':1})
