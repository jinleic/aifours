# Exact rational arithmetic for the resonance-localization extension. The
# anchor phase deficit and stable wide box are separately pinned prerequisites.
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return json.loads(raw)
f=pin('frontier-20261029-resonant-root-localization-frozen-v1.json','f60dc422263b765f47db62340084394829ce3e28dcf97645479dd21ba6259250');a=pin('frontier-20261029-four-nonreal-roots-box-frozen-v1.json',f['source_frozen_sha256']);wide=pin('frontier-20261029-four-nonreal-roots-wide-box-frozen-v1.json',f['wide_frozen_sha256'])
R=F(f['radius']);e=F(f['quadratic_phase_deficit']);lo=F(f['segment_lower']);hi=F(f['segment_upper']);piL=16*(F(1,5)-F(1,5)**3/3)-4*F(1,239)
if F(a['quadratic_phase_deficit_upper'])!=e or [F(x) for x in a['endpoint_frequencies']]!=[lo,hi] or F(f['pi_lower_machin'])!=piL:raise ValueError('INPUT')
if not(0<R<lo<hi and hi-lo==F(1,5) and piL>F(157,50) and piL>5*(hi-lo)/R+3*e):raise ValueError('LOCALIZATION_GAP')
if wide['center']!=a['center'] or F(wide['radius'])<=0:raise ValueError('WIDE_BOX')
print('resonant root localization independent replay:',{'radius':str(R),'positive_imaginary_segment':[str(lo),str(hi)],'pi_rational_lower':str(piL),'strict_gap':True,'minimum_upper_half_roots':2,'scope':'every common numerator for the wide box has two upper roots within the stated segment neighborhood and conjugate lower roots'})

rawsharp=(root/'frontier-20261029-resonant-root-localization-sharp-frozen-v1.json').read_bytes()
if sha256(rawsharp).hexdigest()!='a3b737dcc2ac85b2ca14be92c9f447e440f7cf9f2975518e921eab74dbc93d50':raise ValueError('SHARP_PIN')
g=json.loads(rawsharp);R2=F(g['radius']);D=hi-lo
if not(0<R2<lo and 2*piL>3*e+3*D/R2+4*D/(2*lo) and piL>3*e+2*D/R2+3*D/(2*lo)):raise ValueError('SHARP_BOUND')
print('independent sharper root localization:',{'radius':str(R2),'j0_j1_bounds':2,'minimum_upper_half_roots':2,'scope':'every common numerator has two roots within this sharper resonant segment neighborhood'})
