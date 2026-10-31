# Exact Newton-exponent and limiting-coefficient checks against the
# independently replayed Laurent sign data; root convergence is written.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-unbounded-b6-family-signs-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='e595395eed59d1dd26d223b1997a2e42f57f41c47bdc5ca9e7e881b979071bb9';z=json.loads(raw)['sign_polynomials'];D=z['Det'];B=[z['B%d'%j] for j in range(8)];dc=F(D['shifted_coefficients'][-1]);growth=[x['max_R_power']-D['max_R_power'] for x in B];c=[F(x['shifted_coefficients'][-1])/dc for x in B]
assert growth==[2,3,4,3,4,2,2,0]
assert c==list(map(F,['3/10','3/10','1251/8425','2002/8425','8/337','2002/8425','1317/8425','1']))
expected={2:(14,[6,7]),1:(8,[4,6]),0:(4,[2,4]),-1:(2,[0,1,2])}
for h,(degree,inds) in expected.items():
 values=[growth[j]+h*j for j in range(8)];assert max(values)==degree and [j for j,x in enumerate(values) if x==degree]==inds
assert c[4]/c[6]==F(200,1317) and c[2]/c[4]==F(1251,200)
disc=c[1]**2-4*c[0]*c[2];assert disc==F(-14859,168500)<0
re=-c[1]/(2*c[2]);im2=c[0]/c[2]-re**2;assert re==F(-1685,1668) and im2==F(2781935,2782224)
print({'scaled_limits_at_R2_R_1_invR':['z^6(z+1317/8425)','z^4((1317/8425)z^2+8/337)','z^2((8/337)z^2+1251/8425)','(1251/8425)z^2+(3/10)z+3/10'],'slow_real_part':str(re),'slow_imag_squared':str(im2),'distinct_scales':4})
