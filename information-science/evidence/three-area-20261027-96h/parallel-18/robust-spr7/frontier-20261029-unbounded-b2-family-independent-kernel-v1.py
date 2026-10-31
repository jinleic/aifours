# Exact b2 obstruction, reusing the pinned independently reconstructed
# parametric geometry, with new atom cofactors and new sign arrays.
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
s=(root/'frontier-20261029-unbounded-b6-family-independent-kernel-v1.py').read_bytes();assert sha256(s).hexdigest()=='b28723339572887764ebc355b6739d88fcebd835bd4d1b78988ac0453542ad61'
exec(s.decode().split('d=R**-1/10;atom_defs=',1)[0])
raw=(root/'frontier-20261029-unbounded-b2-family-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='23b5de0abc72b49fa0ea8d6ca878c4ce052e970f3817a80fa4af699413c10099';f=json.loads(raw)
h=R**-1/2;atoms=[(1,R-F(1,2)),(2,one+h),(2,P(3)),(3,P(F(6,5))),(3,F(3,2)+h),(3,L)]
rows=[atomrow(actual[i],t) for i,t in atoms];H=R**4/65;M=[[rows[i][j] for i in range(6)] for j in (1,3,5,6)]+[[rows[i][7]+H*rows[i][2] for i in range(6)]]
w=[(-1)**i*determinant([[row[j] for j in range(6) if j!=i] for row in M]) for i in range(6)];C=[sum((w[i]*rows[i][j] for i in range(6)),P()) for j in range(8)]
assert all(not C[j].d for j in (1,3,5,6)) and not (C[7]+H*C[2]).d
checks={**{'w%d'%i:x for i,x in enumerate(w)},'C2':C[2],'minusC0':-C[0],'minusC4':-C[4]};assert set(checks)==set(f['sign_polynomials']);count=0
for name,p in checks.items():
 lo=min(p.d);hi=max(p.d);a={k-lo:v for k,v in p.d.items()};deg=max(a);v=[sum(c*comb(i,j)*F(1000)**(i-j) for i,c in a.items() if i>=j) for j in range(deg+1)];saved=f['sign_polynomials'][name]
 assert all(x>0 for x in v) and saved['min_R_power']==lo and saved['max_R_power']==hi and list(map(str,v))==saved['shifted_coefficients'];count+=len(v)
assert count==491
sigs=z['sign_polynomials'];de=sigs['Det'];br=sigs['B2'];d=list(map(F,de['shifted_coefficients']));b=list(map(F,br['shifted_coefficients']));k=4+de['min_R_power']-br['min_R_power'];assert k==4
prod=[F(0)]*(len(d)+k)
for i,x in enumerate(d):
 for j in range(k+1):prod[i+j]+=x*comb(k,j)*100**(k-j)
up=[prod[i]-6*b[i] for i in range(len(b))];assert len(up)==24 and all(x>0 for x in up) and list(map(str,up))==f['upper_comparison_shifted_coefficients']
assert br['max_R_power']-de['max_R_power']==4 and b[-1]/d[-1]==F(1251,8425)==F(f['explicit_numerator_asymptote'])
print({'positive_atoms':6,'zero_coordinates':[1,3,5,6],'exact_tail_identity':True,'strict_dual_shift_coefficients':count,'upper_comparison_coefficients':len(up),'parameter':'all real R>=1000','all_numerator_bound':'b2>R^4*b7/65','constructed_upper':'b_R2<R^4/6','constructed_asymptote':'1251/8425'})
