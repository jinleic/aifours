from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-unbounded-b6-strong-lower-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='4f439af0c7f7645ce5241731636fba1d4892280559274d09eddeecd1e2962d48';z=json.loads(raw)
c=z['sign_polynomials']['C6'];s=z['sign_polynomials']['minus_slack'];assert c['max_R_power']==26 and s['max_R_power']==28
lc=F(c['shifted_coefficients'][-1]);ls=F(s['shifted_coefficients'][-1]);assert lc>0 and ls>0 and F(7,80)+ls/lc==F(8,91)
print({'degree_C6':26,'degree_minus_slack':28,'exact_dual_asymptote':'8/91'})
