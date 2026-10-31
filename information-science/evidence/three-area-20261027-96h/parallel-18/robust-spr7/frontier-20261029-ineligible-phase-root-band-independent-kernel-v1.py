# Exact root-band violation in the ineligible five-denominator example.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-individually-stable-five-atom-negative-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='f7248ce91c4802e6888ec05d7934e6f28b3a66724ffc6c929881faf717f5e21f';A=list(map(F,json.loads(raw)['alphas']));amin=min(A);amax=max(A)
def coeff(a):return [F(comb(7,j))*a**(7-j) for j in range(8)]
v=coeff(amax);E=[v[0],-v[2],v[4],-v[6]];beta=[sum(E[k]*F(1,2)**k*F(comb(i,k),comb(3,k)) for k in range(i+1)) for i in range(4)];assert all(x>0 for x in beta)
v=coeff(amin);O0=v[1];Ohalf=v[1]-v[3]*F(1,2)+v[5]*F(1,4)-F(1,8);assert O0>0>Ohalf
print({'E_of_max_alpha_positive_on_0_to_half':True,'positive_Bernstein_coefficients':4,'O_of_min_alpha_negative_at_half':True,'conclusion':'O1(min alpha)<1/2<E1(max alpha)'})
