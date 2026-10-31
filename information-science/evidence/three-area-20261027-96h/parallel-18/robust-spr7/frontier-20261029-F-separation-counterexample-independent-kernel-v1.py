# Exact check that the simple corner-parity test inequality
# sup_{O1}|F| <= inf_{E2}|F|, F=t O_+O_-/(E_+E_-), fails on an eligible box.
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-F-separation-counterexample-frozen-v1.json').read_bytes();assert sha256(raw).hexdigest()=='b8229be24f03feb0d43475b6efefef94d18584c29b4699404ae8f3593a01c6d6';z=json.loads(raw)
R=[(F(a),F(c)) for a,c in z['bands']];flat=[x for ab in R for x in ab];assert flat[0]>0 and all(flat[i]<flat[i+1] for i in range(11))
(e1a,e1b),(o1a,o1b),(e2a,e2b),(o2a,o2b),(e3a,e3b),(o3a,o3b)=R
em,ep,om,op=(e1a,e2b,e3a),(e1b,e2a,e3b),(o1a,o2b,o3a),(o1b,o2a,o3b)
def sig(r):return r[0]+r[1]+r[2],r[0]*r[1]+r[0]*r[2]+r[1]*r[2],r[0]*r[1]*r[2]
def cub(r,lam):s1,s2,s3=sig(r);return [lam*s3,-lam*s2,lam*s1,-lam]
s1m,s2m,s3m=sig(em);s1p,s2p,s3p=sig(ep);lo=max(F(1),s2p/s2m);hi=min(s1p/s1m,s3p/s3m);assert lo<=hi
K=lo+(hi-lo)*F(z['K_fraction_of_interval'])
Em,Ep,Om,Op=cub(em,K),cub(ep,F(1)),cub(om,F(1)),cub(op,F(1))
assert all(Ep[i]-Em[i]>=0 and Op[i]-Om[i]>=0 for i in range(4))
ev=lambda c,t:c[0]+c[1]*t+c[2]*t*t+c[3]*t**3
# Box coefficients: lower/upper endpoints recovered from the four parity cubics.
lower=[Em[0],Om[0],-Ep[1],-Op[1],Em[2],Om[2],-Ep[3]];upper=[Ep[0],Op[0],-Em[1],-Om[1],Ep[2],Op[2],-Em[3]];assert all(0<lower[j]<upper[j] for j in range(7))
t2,t3=F(z['t2']),F(z['t3']);assert o1a<t2<o1b and e2a<t3<e2b
assert ev(Om,t2)<0<ev(Op,t2) and ev(Ep,t2)<0 and ev(Em,t2)<0
assert ev(Em,t3)<0<ev(Ep,t3) and ev(Om,t3)<0 and ev(Op,t3)<0
Fv=lambda t:t*ev(Op,t)*ev(Om,t)/(ev(Ep,t)*ev(Em,t))
assert abs(Fv(t2))>8*abs(Fv(t3))
print({'eligible_box_from_exact_interlaced_roots':True,'positive_widths':7,'F_ratio_gt':8,'t2':str(t2),'t3':str(t3)})
