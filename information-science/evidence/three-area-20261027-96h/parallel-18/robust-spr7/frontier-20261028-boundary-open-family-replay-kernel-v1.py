# Exact endpoint-neighborhood and nested-box arithmetic for the boundary box.
# Python Eval only. Base full-frequency margin has a separate root/leaf replay.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-boundary-common-numerator-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='bb6ddc529d7e37543bcee5799e688494dd9ca902cef765e620866e31230fced9':raise ValueError('FROZEN_HASH')
doc=json.loads(raw); priorraw=(root/'frontier-20261028-harder-box-common-numerator-frozen-v1.json').read_bytes()
if sha256(priorraw).hexdigest()!='74c3ccc312cb0e7b86b8c76f2e89ab2043d36288454720c583ca2bf8a5027eec':raise ValueError('PREVIOUS_HASH')
prior=json.loads(priorraw);lo=[Q(x) for x in doc['lower']];hi=[Q(x) for x in doc['upper']]
plo=[Q(x) for x in prior['lower']];phi=[Q(x) for x in prior['upper']]
if not all(Q(0)<x<y for x,y in zip(lo,hi)):raise ValueError('BOX')
if not all(lo[j]<=plo[j] and phi[j]<=hi[j] for j in range(7)):raise ValueError('NESTING')
new=[Q(x) for x in doc['numerator']];old=[Q(x) for x in doc['old_numerator']]
if len(new)!=8 or new[7]!=1 or not all(x>0 for x in new):raise ValueError('NUMERATOR')
# (E-,O+) actual corner, selected by the frozen prior-numerator failure.
a=[lo[0],hi[1],hi[2],lo[3],lo[4],hi[5],hi[6],Q(1)];t=Q(197,59)
def E(p):return p[0]-p[2]*t+p[4]*t*t-p[6]*t*t*t
def O(p):return p[1]-p[3]*t+p[5]*t*t-p[7]*t*t*t
oldP=E(a)*E(old)+t*O(a)*O(old)
if oldP!=Q(doc['old_numerator_pairing']) or oldP>=0:raise ValueError('OLD_FAILURE')
base=Q(doc['pairing_margin']);S=1+sum(hi);width=min(y-x for x,y in zip(lo,hi))
if base<=0 or S!=Q(doc['coefficient_sum_upper']):raise ValueError('BASE_MARGIN')
B=sum(abs(x) for x in new);B_old=sum(abs(x) for x in old)
def check_radius(rad):
    if rad<=0 or 2*rad>=width:raise ValueError('WIDTH')
    new_margin=base-7*rad*B
    if new_margin<=0:raise ValueError('NEW_MARGIN')
    old_margin=-oldP-7*rad*B_old*(1+t)**7
    if old_margin<=0:raise ValueError('OLD_MARGIN')
    return {'width_margin':width-2*rad,'new_margin':new_margin,'old_failure_margin':old_margin,'ratio_margin':new_margin/(S+7*rad)**2}
radius=Q(1,10**9);check=check_radius(radius);controls=[]
def expect(rad,reason):
    try:check_radius(rad)
    except ValueError as error:
        if str(error)!=reason:raise ValueError('WRONG_CONTROL')
        controls.append((str(rad),reason));return
    raise ValueError('CONTROL_ACCEPTED')
expect(Q(1),'WIDTH');expect(Q(1,1000),'NEW_MARGIN')
print('boundary open-family exact arithmetic:',{'nested':True,'radius':str(radius),'new_B':str(B),'old_B':str(B_old),
 'old_P':str(oldP),'margins':{k:str(v) for k,v in check.items()},'controls':controls})
