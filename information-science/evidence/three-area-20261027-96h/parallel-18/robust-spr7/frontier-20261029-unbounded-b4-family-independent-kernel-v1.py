# Exact quartic-coordinate obstruction, using pinned base geometry and
# independently reconstructed positive-shift sign arrays.
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
s=(root/'frontier-20261029-unbounded-b6-family-independent-kernel-v1.py').read_bytes();assert sha256(s).hexdigest()=='b28723339572887764ebc355b6739d88fcebd835bd4d1b78988ac0453542ad61'
exec(s.decode().split('d=R**-1/10;atom_defs=',1)[0])
raw=(root/'frontier-20261029-unbounded-b4-family-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='7dda51dc349ebc51b5e2f58f20c3b2e0e1a2e1d46091db48940ef50c8b99fba5';f=json.loads(raw)
d=R**-1/10;atoms=[(3,F(3,2)*(one+d)),(1,R*(one+d)),(0,(R+1)*(one-d)),(2,L*(one-d)),(0,P(F(1,3)))]
rows=[atomrow(actual[i],t) for i,t in atoms];H=R**4/100;M=[[rows[i][j] for i in range(5)] for j in (0,1,5)]+[[rows[i][7]+H*rows[i][4] for i in range(5)]]
w=[(-1)**i*determinant([[row[j] for j in range(5) if j!=i] for row in M]) for i in range(5)];C=[sum((w[i]*rows[i][j] for i in range(5)),P()) for j in range(8)]
assert all(not C[j].d for j in (0,1,5)) and not (C[7]+H*C[4]).d
checks={**{'w%d'%i:x for i,x in enumerate(w)},'C4':C[4],'minusC2':-C[2],'minusC3':-C[3],'minusC6':-C[6]};assert set(checks)==set(f['sign_polynomials']);count=0
for name,p in checks.items():
 lo=min(p.d);hi=max(p.d);a={k-lo:v for k,v in p.d.items()};deg=max(a);v=[sum(c*comb(i,j)*F(100)**(i-j) for i,c in a.items() if i>=j) for j in range(deg+1)];saved=f['sign_polynomials'][name]
 assert all(x>0 for x in v) and saved['min_R_power']==lo and saved['max_R_power']==hi and list(map(str,v))==saved['shifted_coefficients'];count+=len(v)
assert count==466
sigs=z['sign_polynomials'];de=sigs['Det'];br=sigs['B4'];d0=list(map(F,de['shifted_coefficients']));b0=list(map(F,br['shifted_coefficients']));k=4+de['min_R_power']-br['min_R_power'];assert k==5
prod=[F(0)]*(len(d0)+k)
for i,x in enumerate(d0):
 for j in range(k+1):prod[i+j]+=x*comb(k,j)*100**(k-j)
up=[prod[i]-40*b0[i] for i in range(len(b0))];assert len(up)==25 and all(x>0 for x in up) and list(map(str,up))==f['upper_comparison_shifted_coefficients']
assert br['max_R_power']-de['max_R_power']==4 and b0[-1]/d0[-1]==F(8,337)==F(f['explicit_numerator_asymptote'])
print({'positive_atoms':5,'zero_coordinates':[0,1,5],'exact_tail_identity':True,'strict_dual_shift_coefficients':count,'upper_comparison_coefficients':len(up),'parameter':'all real R>=100','all_numerator_bound':'b4>R^4*b7/100','constructed_upper':'b_R4<R^4/40','constructed_asymptote':'8/337'})
