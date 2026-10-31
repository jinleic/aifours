# Standalone exact replay of the all-scale three-contact numerator.
# Reads two frozen JSON packets only; imports no producer/search helpers.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from copy import deepcopy
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def frozen(name,digest):
    raw=(root/name).read_bytes()
    if sha256(raw).hexdigest()!=digest:raise ValueError('FROZEN_HASH:'+name)
    return json.loads(raw)
fam=frozen('frontier-20261028-three-gap-family-and-grid-frozen-v1.json','6984f81b8bd94ad5379195b393b2662cfc43ca48a0cf1287e2acf3135ff633a9')
u=frozen('frontier-20261028-three-gap-universal-numerator-frozen-v1.json','6c89ae0515bfb0a8305e0fb8da487b61a629b9a3328a5a7529290d8315299f54')
if u['family_frozen_sha256']!='6984f81b8bd94ad5379195b393b2662cfc43ca48a0cf1287e2acf3135ff633a9':raise ValueError('BINDING')
def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
center=[Q(1),Q(1)]
for v in (2,4,8):center=mul(center,[Q(1+v*v),Q(2),Q(1)])
if [str(v) for v in center]!=fam['center']:raise ValueError('CENTER')
h=[Q(x) for x in fam['halfwidth']]
if len(h)!=7 or not all(0<h[j]<center[j] for j in range(7)):raise ValueError('HALFWIDTH')
def parity(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
def marker(t):
    e,o=parity(center,t);de=sum(h[2*j]*t**j for j in range(4));do=sum(h[2*j+1]*t**j for j in range(3))
    return [e-de,e+de,o-do,o+do]
marks={Q(t):marker(Q(t)) for t in fam['marker_intervals_at_scale_one']}
if any([str(x) for x in marks[Q(t)]]!=vals for t,vals in fam['marker_intervals_at_scale_one'].items()):raise ValueError('MARKERS')
for t in (Q(3),Q(65)):
    e,o=parity(center,t)
    if not marks[t][1]==0 or not marks[t][2]==0 or not e<0<o:raise ValueError('CONTACT_SIGNS')
e,o=parity(center,Q(15))
if not marks[Q(15)][0]==0 or not marks[Q(15)][3]==0 or not o<0<e:raise ValueError('CONTACT_SIGNS')
if not(marks[Q(17,2)][1]<0 and marks[Q(17,2)][3]<0 and marks[Q(30)][0]>0 and marks[Q(30)][2]>0):raise ValueError('SEPARATORS')
lo=[center[j]-h[j] for j in range(7)];hi=[center[j]+h[j] for j in range(7)]
def corners(lo,hi):
    out=[]
    for es in (0,1):
        for oside in (0,1):
            a=[Q(0)]*8;a[7]=Q(1)
            for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
            for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
            out.append(a)
    return out
cs=corners(lo,hi)
for item in fam['boundary_zero_atoms']:
    if parity(cs[item['corner']],Q(item['t']))!=(Q(0),Q(0)):raise ValueError('BOUNDARY_ZERO')

b=[Q(x) for x in u['numerator']]
if len(b)!=8 or b[-1]!=1 or not all(x>0 for x in b):raise ValueError('NUMERATOR')
def pair(a,b):
    E=lambda p:[p[0],-p[2],p[4],-p[6]]
    O=lambda p:[p[1],-p[3],p[5],-p[7]]
    p=mul(E(a),E(b))+[Q(0)]
    for j,x in enumerate(mul(O(a),O(b))):p[j+1]+=x
    return p
def check_product(poly,residual,roots):
    q=residual
    for r in roots:q=mul(q,[r*r,-2*r,Q(1)])
    if q!=poly:raise ValueError('FACTORIZATION')
def bernstein(poly,left,right):
    n=len(poly)-1
    power=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
    affine=[sum(power[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
    return [sum(affine[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def leaf(poly,item,strict):
    left,right=Q(item['left']),Q(item['right'])
    if not 0<=left<right<=1:raise ValueError('LEAF_RANGE')
    coeff=bernstein(poly,left,right)
    if coeff!=[Q(x) for x in item['coefficients']]:raise ValueError('LEAF_MISMATCH')
    if any(x<0 for x in coeff) or (strict and any(x<=0 for x in coeff)):raise ValueError('LEAF_SIGN')
    return coeff
def cover(poly,proof,strict):
    wanted='STRICT_POSITIVITY' if strict else 'NONNEGATIVE_PROVED'
    if proof['status']!=wanted:raise ValueError('PROOF_STATUS')
    ls=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);values=[]
    for item in ls:
        if Q(item['left'])!=at:raise ValueError('LEAF_COVERAGE')
        values.extend(leaf(poly,item,strict));at=Q(item['right'])
    if at!=1:raise ValueError('LEAF_COVERAGE')
    return len(ls),values
counts=[]
for i,a in enumerate(cs):
    poly=pair(a,b)
    if [str(x) for x in poly]!=u['boundary_polynomials'][i]:raise ValueError('PAIRING')
    residual=[Q(x) for x in u['boundary_residual_polynomials'][i]]
    roots=[Q(x) for x in u['boundary_square_factors'][i]]
    check_product(poly,residual,roots)
    count,values=cover(residual,u['boundary_nonnegative_proofs'][i],False)
    if not all(v>0 for v in values):raise ValueError('RESIDUAL_NOT_STRICT')
    counts.append(count)
    a_mid=[(x+y)/2 for x,y in zip(center,a)]
    if pair(a_mid,b)!=[(x+y)/2 for x,y in zip(pair(center,b),poly)]:raise ValueError('AFFINE_PAIRING')
centerpoly=pair(center,b)
if [str(x) for x in centerpoly]!=u['center_polynomial']:raise ValueError('CENTER_PAIRING')
center_count,coeff=cover(centerpoly,u['center_proof'],True)
delta=min(coeff);S=1+sum(hi)
if delta!=Q(u['center_margin']) or S!=Q(u['S_at_scale_one']) or delta/S**2!=Q(u['uniform_ratio_coefficient']):raise ValueError('MARGINS')
controls=[]
def reject(label,reason,f):
    try:f()
    except ValueError as e:
        if str(e)!=reason:raise ValueError('CONTROL_WRONG:'+label+':'+str(e))
        controls.append(label);return
    raise ValueError('CONTROL_ACCEPTED:'+label)
fault=deepcopy(u['boundary_nonnegative_proofs'][0]['leaves'][0]);fault['coefficients'][0]=str(Q(fault['coefficients'][0])+1)
reject('leaf_coefficient','LEAF_MISMATCH',lambda:leaf([Q(x) for x in u['boundary_residual_polynomials'][0]],fault,False))
fault_res=[Q(x) for x in u['boundary_residual_polynomials'][1]];fault_res[0]+=1
reject('square_factor','FACTORIZATION',lambda:check_product(pair(cs[1],b),fault_res,[Q(15)]))
print('independent universal-family replay:',{'center_factorization':True,'exact_sign_markers':len(marks),'boundary_contacts':len(fam['boundary_zero_atoms']),
 'numerator_positive_and_monic':True,'boundary_leaf_counts':counts,'all_boundary_residual_coefficients_strict':True,
 'center_leaf_count':center_count,'center_margin':str(delta),'S_at_one':str(S),'ratio_coefficient':str(delta/S**2),
 'affine_corner_pairings_checked':4,'rejected_mutations':controls})
