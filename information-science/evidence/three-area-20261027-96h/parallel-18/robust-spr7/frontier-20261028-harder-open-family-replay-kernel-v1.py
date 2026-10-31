# Independent exact neighborhood and nested-box replay, Python Eval only.
# The frozen base margin is separately verified by the independent leaf/root checker.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json

root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-harder-box-common-numerator-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='74c3ccc312cb0e7b86b8c76f2e89ab2043d36288454720c583ca2bf8a5027eec':raise ValueError('FROZEN_HASH')
doc=json.loads(raw)
oldraw=(root/'frontier-20261028-anisotropic-common-numerator-frozen-v1.json').read_bytes()
if sha256(oldraw).hexdigest()!='41411d5d0f25108a14e1dad8f8ac770ee580867d573206ce4ea22b6cf71005a4':raise ValueError('PREVIOUS_HASH')
prior=json.loads(oldraw)
lo=[Q(x) for x in doc['lower']];hi=[Q(x) for x in doc['upper']]
plo=[Q(x) for x in prior['lower']];phi=[Q(x) for x in prior['upper']]
if not all(Q(0)<x<y for x,y in zip(lo,hi)):raise ValueError('BOX')
if not all(lo[j]<=plo[j] and phi[j]<=hi[j] for j in range(7)):raise ValueError('NESTING')
new=[Q(x) for x in doc['numerator']];old=[Q(x) for x in doc['old_numerator']];earlier=[Q(x) for x in doc['earlier_base_numerator']]
if not all(x>0 for x in new) or new[7]!=1:raise ValueError('NUMERATOR')
a=[hi[0],hi[1],lo[2],lo[3],hi[4],hi[5],lo[6],Q(1)];t=Q(7,25)
def E(p):return p[0]-p[2]*t+p[4]*t*t-p[6]*t*t*t
def O(p):return p[1]-p[3]*t+p[5]*t*t-p[7]*t*t*t
def pairing(v):return E(a)*E(v)+t*O(a)*O(v)
oldP=pairing(old);earlierP=pairing(earlier)
if oldP!=Q(doc['old_numerator_pairing']) or oldP>=0:raise ValueError('OLD_FAILURE')
if earlierP!=Q(doc['earlier_base_numerator_pairing']) or earlierP>=0:raise ValueError('EARLIER_FAILURE')
base=Q(doc['pairing_margin']);S=1+sum(hi);width=min(y-x for x,y in zip(lo,hi))
if base<=0 or S!=Q(doc['coefficient_sum_upper']):raise ValueError('BASE_MARGIN')
B=sum(abs(x) for x in new);B_old=sum(abs(x) for x in old);B_early=sum(abs(x) for x in earlier)
def check_radius(radius):
    if radius<=0 or 2*radius>=width:raise ValueError('WIDTH')
    new_margin=base-7*radius*B
    if new_margin<=0:raise ValueError('NEW_MARGIN')
    old_margin=-oldP-7*radius*B_old*(1+t)**7
    if old_margin<=0:raise ValueError('OLD_MARGIN')
    earlier_margin=-earlierP-7*radius*B_early*(1+t)**7
    if earlier_margin<=0:raise ValueError('EARLIER_MARGIN')
    return {'width_margin':width-2*radius,'new_margin':new_margin,'old_failure_margin':old_margin,
      'earlier_failure_margin':earlier_margin,'ratio_margin':new_margin/(S+7*radius)**2}
radius=Q(1,10**8);check=check_radius(radius);controls=[]
def expect(rad,reason):
    try:check_radius(rad)
    except ValueError as error:
        if str(error)!=reason:raise ValueError('WRONG_CONTROL')
        controls.append((str(rad),reason));return
    raise ValueError('CONTROL_ACCEPTED')
expect(Q(1),'WIDTH');expect(Q(1,1000),'NEW_MARGIN')
print('nested open-family exact arithmetic:',{'nested':True,'radius':str(radius),'new_B':str(B),'old_B':str(B_old),'earlier_B':str(B_early),
 'old_P':str(oldP),'earlier_P':str(earlierP),'margins':{k:str(v) for k,v in check.items()},'controls':controls})
