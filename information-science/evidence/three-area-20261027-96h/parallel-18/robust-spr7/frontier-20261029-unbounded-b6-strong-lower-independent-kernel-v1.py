# Reuse the pinned, independently reconstructed parameter-box geometry;
# generate a different 5-atom functional and check all shifted signs.
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
s=(root/'frontier-20261029-unbounded-b6-family-independent-kernel-v1.py').read_bytes();assert sha256(s).hexdigest()=='b28723339572887764ebc355b6739d88fcebd835bd4d1b78988ac0453542ad61'
exec(s.decode().split('d=R**-1/10;atom_defs=',1)[0])
raw=(root/'frontier-20261029-unbounded-b6-strong-lower-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='4f439af0c7f7645ce5241731636fba1d4892280559274d09eddeecd1e2962d48';f=json.loads(raw)
d=R**-1/10;atoms=[(3,F(3,2)*(one+d)),(1,R*(one+d)),(0,(R+1)*(one-d)),(0,P(F(1,3))),(0,L*F(14,25))]
rows=[atomrow(actual[i],t) for i,t in atoms];M=[[rows[i][j] for i in range(5)] for j in (1,2,3,5)]
w=[(-1)**(i+1)*determinant([[row[j] for j in range(5) if j!=i] for row in M]) for i in range(5)]
C=[sum((w[i]*rows[i][j] for i in range(5)),P()) for j in range(8)];assert all(not C[j].d for j in (1,2,3,5))
checks={**{'w%d'%i:x for i,x in enumerate(w)},'minus_C0':-C[0],'minus_C4':-C[4],'C6':C[6],'minus_slack':-(C[7]+R*R*C[6]*F(7,80))};assert set(checks)==set(f['sign_polynomials'])
count=0
for name,p in checks.items():
 low=min(p.d);high=max(p.d);a={k-low:v for k,v in p.d.items()};deg=max(a);v=[sum(c*comb(i,j)*F(5000)**(i-j) for i,c in a.items() if i>=j) for j in range(deg+1)];saved=f['sign_polynomials'][name]
 assert all(x>0 for x in v) and saved['min_R_power']==low and saved['max_R_power']==high and list(map(str,v))==saved['shifted_coefficients'];count+=len(v)
assert count==424 and -F(f['sign_polynomials']['w0']['shifted_coefficients'][0])<0
print({'positive_atom_weights':5,'exact_zero_aggregate_coordinates':[1,2,3,5],'strict_shifted_coefficients':count,'parameter_scope':'all real R>=5000','lower_bound':'b6 > (7/80)*R^2*b7','mutation_controls':1})
