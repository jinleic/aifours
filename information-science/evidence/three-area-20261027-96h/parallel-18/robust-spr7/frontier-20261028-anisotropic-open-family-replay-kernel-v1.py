# Independent exact perturbation arithmetic for one frozen anisotropic box.
# Eval-only; no search or previous checker import. The frozen base pairing
# margin is separately bound to the independent root/leaf replay receipt.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json

path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-anisotropic-common-numerator-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='41411d5d0f25108a14e1dad8f8ac770ee580867d573206ce4ea22b6cf71005a4':raise ValueError('FROZEN_HASH')
doc=json.loads(raw); low=[Q(x) for x in doc['lower']];high=[Q(x) for x in doc['upper']]
new=[Q(x) for x in doc['numerator']];old=[Q(x) for x in doc['old_numerator']]
if len(low)!=7 or len(high)!=7 or not all(Q(0)<x<y for x,y in zip(low,high)):raise ValueError('BOX')
if len(new)!=8 or new[7]!=1 or not all(x>0 for x in new):raise ValueError('NEW_NUMERATOR')
# Reconstruct E+/O+ actual corner independently, and evaluate old b at t=7/25.
a=[high[0],high[1],low[2],low[3],high[4],high[5],low[6],Q(1)]
t=Q(7,25)
def E(p,t):return p[0]-p[2]*t+p[4]*t*t-p[6]*t*t*t
def O(p,t):return p[1]-p[3]*t+p[5]*t*t-p[7]*t*t*t
old_pair=E(a,t)*E(old,t)+t*O(a,t)*O(old,t)
if old_pair!=Q(doc['old_numerator_pairing']) or old_pair>=0:raise ValueError('OLD_PAIR')
base_margin=Q(doc['pairing_margin']);S=1+sum(high)
if base_margin<=0 or S!=Q(doc['coefficient_sum_upper']):raise ValueError('BASE_MARGIN')
B=sum(abs(x) for x in new);B_old=sum(abs(x) for x in old);minwidth=min(y-x for x,y in zip(low,high))

def radius_check(radius):
    if radius<=0 or 2*radius>=minwidth:raise ValueError('WIDTH')
    new_margin=base_margin-7*radius*B
    if new_margin<=0:raise ValueError('NEW_MARGIN')
    old_margin=-old_pair-7*radius*B_old*(1+t)**7
    if old_margin<=0:raise ValueError('OLD_MARGIN')
    return {'width_margin':minwidth-2*radius,'new_margin':new_margin,'old_failure_margin':old_margin,
            'ratio_margin':new_margin/(S+7*radius)**2}

open_radius=Q(1,10**8);result=radius_check(open_radius)
controls=[]
def expect(radius,expected):
    try:radius_check(radius)
    except ValueError as e:
        if str(e)!=expected:raise ValueError('WRONG_CONTROL:'+str(e))
        controls.append((str(radius),expected));return
    raise ValueError('CONTROL_ACCEPTED')
expect(Q(1),'WIDTH');expect(Q(1,1000),'NEW_MARGIN')
print('independent open-family arithmetic:',{'radius':str(open_radius),'new_B':str(B),'old_B':str(B_old),
 'min_width':str(minwidth),'old_pair':str(old_pair),'margins':{k:str(v) for k,v in result.items()},'controls':controls})
