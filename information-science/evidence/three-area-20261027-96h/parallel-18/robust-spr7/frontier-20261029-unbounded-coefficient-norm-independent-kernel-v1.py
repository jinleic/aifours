# Recompute the actual radial upper coefficient sum and compare exact
# leading growth against the independently checked numerator determinants.
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
s=(root/'frontier-20261029-unbounded-b6-family-independent-kernel-v1.py').read_bytes();assert sha256(s).hexdigest()=='b28723339572887764ebc355b6739d88fcebd835bd4d1b78988ac0453542ad61'
exec(s.decode().split('d=R**-1/10;atom_defs=',1)[0])
raw=(root/'frontier-20261029-unbounded-coefficient-norm-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='be18e89408d87461d3c7dc89b30930bb15704fcef666680ccba167ea6be8ab8c';f=json.loads(raw)
U=one+sum(hi,P());G=R**3-U;low=min(G.d);high=max(G.d);a={k-low:v for k,v in G.d.items()};deg=max(a);v=[sum(c*comb(i,j)*F(1000)**(i-j) for i,c in a.items() if i>=j) for j in range(deg+1)]
assert all(x>0 for x in v) and list(map(str,v))==f['gap_shifted_coefficients'] and (low,high)==(f['gap_min_R_power'],f['gap_max_R_power'])
assert max(U.d)==3 and U.d[3]==F(1,2)==F(f['denominator_norm_leading_coefficient'])
D=z['sign_polynomials']['Det'];B2=z['sign_polynomials']['B2'];B4=z['sign_polynomials']['B4'];d=F(D['shifted_coefficients'][-1]);c2=F(B2['shifted_coefficients'][-1])/d;c4=F(B4['shifted_coefficients'][-1])/d
assert c2+c4==F(1451,8425)==F(f['common_numerator_norm_leading_coefficient'])
assert 2*(c2+c4)==F(2902,8425)==F(f['constructed_norm_ratio_asymptotic_coefficient'])
assert F(1,65)+F(1,100)==F(33,1300)==F(f['universal_lower_coefficient'])
print({'strict_shifted_box_norm_gap_coefficients':len(v),'sup_denominator_norm_leading':'R^3/2','witness_norm_leading':'(1451/8425)*R^4','universal_ratio_lower':'(33/1300)*R','witness_ratio_asymptote':'(2902/8425)*R'})
