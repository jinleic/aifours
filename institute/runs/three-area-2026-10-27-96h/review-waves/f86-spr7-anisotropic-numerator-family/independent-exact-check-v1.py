#!/usr/bin/env python3
"""Independent exact review, using only rational arithmetic and no author code."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json

ROOT = Path('/Users/jinleic/repos/aifours')
WAVE = ROOT/'institute/runs/three-area-2026-10-27-96h/review-waves/f86-spr7-anisotropic-numerator-family'
RELEASE = ROOT/'institute/runs/three-area-2026-10-27-96h/written-releases/info-2-septic-box-definitions-v1.md'
EVID = ROOT/'information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7'
CAND = EVID/'frontier-20261028-anisotropic-new-numerator-open-family-v1.md'
FROZEN = EVID/'frontier-20261028-anisotropic-common-numerator-frozen-v1.json'
AUTH_RECEIPT = EVID/'frontier-20261028-anisotropic-independent-replay-result-v1.json'
SEARCH_RECEIPT = EVID/'frontier-20261028-anisotropic-exact-search-result-v1.json'
PINS = {
    RELEASE: 'd86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad',
    CAND: '25db31d50117b74462a3fc25f22d46f48d2e44e79d28455c0b875eef93063d2f',
    FROZEN: '41411d5d0f25108a14e1dad8f8ac770ee580867d573206ce4ea22b6cf71005a4',
    AUTH_RECEIPT: 'aa6ec5a8487861998a8acfc6bbea2ff4ff66c9bc1160da9b2a96774320ff6311',
    SEARCH_RECEIPT: 'af830d936a56ca8b446d09b4082ff2bcfa0b4c036e969c0cb98dfc5a9fa60d66',
}
def require(cond, reason):
    if not cond:
        raise ValueError(reason)
for path, expected in PINS.items():
    require(sha256(path.read_bytes()).hexdigest() == expected, 'PIN '+str(path))
frozen = json.loads(FROZEN.read_text())
author_receipt = json.loads(AUTH_RECEIPT.read_text())
search_receipt = json.loads(SEARCH_RECEIPT.read_text())

# Arrays are low-to-high power and are copied from the candidate, NOT its code.
lo = list(map(F,['886849/200000','2148651/200000','2366653/100000','4096899/100000','425163/40000','653239/50000','2207/2000']))
hi = list(map(F,['917351/200000','2299949/200000','2436747/100000','4319301/100000','448797/40000','716061/50000','453/400']))
bnew = list(map(F,['1/25','30987/50','112341/100','291423/100','92178/25','17402/25','58911/100','1']))
bold = list(map(F,['1/1000','883/25','7183/100','16691/100','23757/100','3851/100','3413/100','1']))
base_lo = list(map(F,['887/200','10747/1000','2367/100','2049/50','1329/125','13071/1000','1089/1000']))
base_hi = list(map(F,['2293/500','1437/125','6091/250','21591/500','11217/1000','2863/200','1147/1000']))
require([F(x) for x in frozen['lower']] == lo and [F(x) for x in frozen['upper']] == hi, 'BOX')
require([F(x) for x in frozen['numerator']] == bnew and [F(x) for x in frozen['old_numerator']] == bold, 'NUMERATOR')
require([F(x) for x in search_receipt['base_lower']] == base_lo and [F(x) for x in search_receipt['base_upper']] == base_hi, 'PRIOR_BOX_METADATA')
require(all(0 < lo[i] < hi[i] for i in range(7)), 'BOX_WIDTHS_OR_POSITIVITY')
require(all((lo[i]+hi[i]) == (base_lo[i]+base_hi[i]) for i in range(7)), 'PRIOR_MIDPOINTS')
require(all((hi[i]-lo[i]) == (base_hi[i]-base_lo[i])*(F(1,2) if i==6 else F(101,100)) for i in range(7)), 'PRIOR_WIDTH_FACTORS')

def parity_corners(lower,upper):
    ans=[]
    for ev,od in product(range(2),repeat=2):
        a=[]
        for j in range(7):
            # sign of the coefficient in E(t) or O(t) is (-1)^(j//2)
            plus = (j//2)%2==0
            want_hi = (ev if j%2==0 else od)==1
            a.append(upper[j] if plus==want_hi else lower[j])
        ans.append(a+[F(1)])
    return ans
corners=parity_corners(lo,hi)

# Direct complex monomial pairing: Re(a(iw) b(-iw)), independent of E/O code.
def pairing(a,b):
    p=[F(0)]*8
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            if (i+j)%2 == 0:
                p[(i+j)//2] += ai*bj * (-1 if ((i-j)//2)%2 else 1)
    return p

def evaluate(p,x):
    y=F(0)
    for c in reversed(p): y=y*x+c
    return y

def modulus_squared(a,t):
    return evaluate(pairing(a,a),t)

def require_bracket(p,left,right):
    require(0<left<right and evaluate(p,left)*evaluate(p,right)<0,'ROOT_BRACKET')

root_poly={
    'E-':[lo[0],-hi[2],lo[4],-hi[6]],
    'E+':[hi[0],-lo[2],hi[4],-lo[6]],
    'O-':[lo[1],-hi[3],lo[5],-F(1)],
    'O+':[hi[1],-lo[3],hi[5],-F(1)],
}
root_signs={}
for key,p in root_poly.items():
    require([F(x) for x in frozen['root_polynomials'][key]]==p,'ROOT_POLYNOMIAL '+key)
    require(len(p)==4 and p[0]>0 and p[-1]<0,'ROOT_DEGREE')
    intervals=[[F(q) for q in x] for x in frozen['root_intervals'][key]]
    require(len(intervals)==3 and all(intervals[i][1] < intervals[i+1][0] for i in range(2)),'ROOT_ORDER')
    for l,r in intervals: require_bracket(p,l,r)
    root_signs[key]=[('+' if evaluate(p,l)>0 else '-', '+' if evaluate(p,r)>0 else '-') for l,r in intervals]

bands=[]
for parity in 'EO':
    for k in range(3):
        intervals=[[F(q) for q in frozen['root_intervals'][parity+sign][k]] for sign in '-+']
        bands.append((min(x[0] for x in intervals),max(x[1] for x in intervals),parity+str(k+1)))
bands.sort()
require([x[2] for x in bands]==['E1','O1','E2','O2','E3','O3'],'BAND_ORDER')
require(all(bands[i][1]<bands[i+1][0] for i in range(5)),'BAND_OVERLAP')
expected_bands=[
 ('2669023231/13421772800','1156003953/5368709120'),
 ('362900403/1342177280','4221316401/13421772800'),
 ('70863980953/26843545600','45719303009/13421772800'),
 ('46576076907/13421772800','142434266679/26843545600'),
 ('155163355863/26843545600','196289908087/26843545600'),
 ('40202548589/5368709120','141418767751/13421772800')]
require([(l,r) for l,r,_ in bands] == [(F(l),F(r)) for l,r in expected_bands],'BAND_VALUES')

# Fraction Gaussian elimination of the Hurwitz matrix, independently of Routh.
def determinant(matrix):
    a=[list(row) for row in matrix]
    total=F(1)
    for i in range(len(a)):
        pivot=next((j for j in range(i,len(a)) if a[j][i]),None)
        if pivot is None: return F(0)
        if pivot!=i: a[i],a[pivot]=a[pivot],a[i]; total=-total
        v=a[i][i];total*=v
        for j in range(i+1,len(a)):
            m=a[j][i]/v
            for k in range(i+1,len(a)): a[j][k]-=m*a[i][k]
    return total

def hurwitz_minors(a):
    c=list(reversed(a))
    def coeff(k): return c[k] if 0<=k<len(c) else F(0)
    mat=[[coeff(2*j-i+1) for j in range(7)] for i in range(7)]
    return [determinant([row[:k] for row in mat[:k]]) for k in range(1,8)]

def routh_column(a):
    rev=list(reversed(a))
    rows=[rev[0::2],rev[1::2]]
    for k in range(2,8):
        up,prev=rows[-2:]
        require(prev[0]!=0,'ROUTH_ZERO_PIVOT')
        rows.append([(prev[0]*up[j+1]-up[0]*prev[j+1])/prev[0] for j in range(3)]+[F(0)])
    return [row[0] for row in rows]

routh=routh_column(corners[0])
require(all(x>0 for x in routh) and routh==[F(x) for x in frozen['reference_routh_first_column']],'ROUTH')
corner_dets=[hurwitz_minors(a) for a in corners]
require(all(x>0 for row in corner_dets for x in row),'HURWITZ_MINORS')
require(corner_dets == [[F(x) for x in row] for row in author_receipt['hurwitz_minors']],'MINORS_RECEIPT')

# Bernstein coefficients for Q(x)=sum p_k x^k(1-x)^(7-k): p_k/C(7,k).
# de Casteljau splits restrict this same polynomial to each claimed interval.
def split(coeffs,u):
    left=[coeffs[0]];right=[coeffs[-1]];level=list(coeffs)
    while len(level)>1:
        level=[(1-u)*level[i]+u*level[i+1] for i in range(len(level)-1)]
        left.append(level[0]);right.append(level[-1])
    return left,list(reversed(right))

def restrict(p,l,r):
    require(0<=l<r<=1,'LEAF_INTERVAL')
    coeffs=[p[k]/comb(7,k) for k in range(8)]
    left,_=split(coeffs,r)
    _,segment=split(left,l/r)
    return segment

def verify_leaf(p,leaf):
    result=restrict(p,F(leaf['left']),F(leaf['right']))
    require(result==[F(x) for x in leaf['coefficients']],'LEAF_MISMATCH')
    require(all(x>0 for x in result),'LEAF_NONPOSITIVE')
    return result

all_bounds={F(0),F(1)}
leaf_counts=[];case_min=[];checked_coeffs=0
for i,proof in enumerate(frozen['bernstein_proofs']):
    p=pairing(corners[i],bnew)
    require(p==[F(x) for x in frozen['pairing_polynomials'][i]],'PAIR_POLY')
    require(proof['status']=='STRICT_POSITIVITY','LEAF_STATUS')
    prev=F(0);vals=[]
    for leaf in proof['leaves']:
        l,r=F(leaf['left']),F(leaf['right'])
        require(l==prev,'LEAF_GAP')
        vals.extend(verify_leaf(p,leaf));checked_coeffs+=8
        all_bounds.update((l,r));prev=r
    require(prev==1,'LEAF_COVER')
    require(proof['nodes']==2*len(proof['leaves'])-1,'NODE_COUNT')
    require(min(vals)==F(proof['margin']),'LEAF_MARGIN')
    leaf_counts.append(len(proof['leaves']));case_min.append(min(vals))
require(leaf_counts==[6,6,7,9] and checked_coeffs==224,'LEAF_COUNTS')
d=min(case_min)
require(d==F('1050465553521003/96207267430400000')==F(frozen['pairing_margin']),'GLOBAL_MARGIN')

# Exercise four supplied corners and two explicitly specified strictly interior
# coefficient vectors on the common refinement of all four leaf partitions.
weights=[[F(1,2)]*7,list(map(F,['1/4','3/4','1/3','2/3','1/5','4/5','2/5']))]
interiors=[[lo[j]+weights[i][j]*(hi[j]-lo[j]) for j in range(7)]+[F(1)] for i in range(2)]
require(all(lo[j]<a[j]<hi[j] for a in interiors for j in range(7)),'INTERIOR')
grid=sorted(all_bounds)
six=[]
for name,a in zip(['E-O-','E-O+','E+O-','E+O+','midpoint','mixed'],corners+interiors):
    p=pairing(a,bnew)
    checks=[q for l,r in zip(grid,grid[1:]) for q in restrict(p,l,r)]
    local_min=min(checks)
    ds=hurwitz_minors(a)
    require(local_min>0 and all(x>0 for x in ds),'SIX_MEMBER_SPR')
    t=F(7,25); denom=modulus_squared(a,t); pair=evaluate(p,t)
    require(denom>0 and pair>0,'SIX_MEMBER_PAIR')
    norm=sum(abs(x) for x in a)
    six.append({'member':name,'ascending_coefficients':a,'positive_hurwitz_minors':len(ds),
                'bernstein_refined_intervals':len(grid)-1,'minimum_bernstein_coefficient':local_min,
                'own_uniform_ratio_lower_bound':local_min/norm**2,
                'pair_at_t_7_25':pair,'denominator_squared_at_t_7_25':denom,
                'ratio_at_t_7_25':pair/denom})

S=1+sum(max(abs(lo[i]),abs(hi[i])) for i in range(7))
require(S==F('178113/1600')==F(frozen['coefficient_sum_upper']),'BOX_COEFF_SUM')
base_ratio=d/S**2
require(base_ratio==F('116718394835667/132469727243471421440')==F(frozen['ratio_margin']),'BASE_RATIO')
t0=F(7,25)
old_pair=evaluate(pairing(corners[3],bold),t0)
old_modulus=modulus_squared(corners[3],t0)
require(old_pair==F('-553009337053/39062500000000') and old_modulus>0,'OLD_FAILURE')
require(old_pair==F(frozen['old_numerator_pairing']) and t0==F(frozen['old_numerator_failing_t']) and frozen['old_numerator_failing_corner']==3,'OLD_CERT')

rho=F(1,100000000)
B=sum(abs(x) for x in bnew);Bold=sum(abs(x) for x in bold)
width=min(hi[i]-lo[i] for i in range(7))
require(B==F('963073/100') and Bold==F('585271/1000') and width==F('29/1000'),'PERTURBATION_CONSTANTS')
def radius_check(r):
    require(r>0 and 2*r<width,'WIDTH')
    require(d-7*r*B>0,'NEW_MARGIN')
    require(-old_pair-7*r*Bold*(1+t0)**7>0,'OLD_MARGIN')
    return (width-2*r,d-7*r*B,-old_pair-7*r*Bold*(1+t0)**7,(d-7*r*B)/(S+7*r)**2)
wm,nm,om,ratio=radius_check(rho)
require(wm==F('1449999/50000000') and nm==F('3080022869858764583/300647710720000000000'),'NEW_ENDPOINT_MARGINS')
require(om==F('1062500322801560113/76293945312500000000') and ratio==F('48125357341543196609375/58214235678253038721514340352'),'OLD_AND_RATIO_ENDPOINT_MARGINS')

# Controls must fail for the intended reason, not merely throw an exception.
def expect_error(name,reason,fn):
    try: fn()
    except ValueError as exc:
        require(str(exc)==reason,'CONTROL_WRONG_REASON '+name+' '+str(exc))
        return [name,reason]
    raise ValueError('CONTROL_ACCEPTED '+name)
leaf=dict(frozen['bernstein_proofs'][0]['leaves'][0]);leaf['coefficients']=list(leaf['coefficients']);leaf['coefficients'][0]=str(F(leaf['coefficients'][0])+1)
controls=[expect_error('corrupt_leaf','LEAF_MISMATCH',lambda:verify_leaf(pairing(corners[0],bnew),leaf))]
l,r=map(F,frozen['root_intervals']['E-'][0]);controls.append(expect_error('reverse_root_bracket','ROOT_BRACKET',lambda:require_bracket(root_poly['E-'],r,l)))
controls.append(expect_error('radius_1','WIDTH',lambda:radius_check(F(1))))
controls.append(expect_error('radius_1_1000','NEW_MARGIN',lambda:radius_check(F(1,1000))))

# The separately named search receipt supplies the previous box coordinates.
# Establish its old-numerator property directly, with adaptive exact subdivision.
def adaptive_positive(p,maxdepth=32,maxleaves=20000):
    stack=[([p[k]/comb(7,k) for k in range(8)],0,F(0),F(1))]; leaves=[]
    while stack:
        beta,depth,l,r=stack.pop()
        if min(beta)>0:
            leaves.append((l,r,min(beta)))
            require(len(leaves)<=maxleaves,'PRIOR_LEAF_LIMIT')
        else:
            require(max(beta)>0,'PRIOR_NEGATIVE_INTERVAL')
            require(depth<maxdepth,'PRIOR_DEPTH_LIMIT')
            a,b=split(beta,F(1,2));m=(l+r)/2
            stack.append((b,depth+1,m,r));stack.append((a,depth+1,l,m))
    return leaves
prior_corners=parity_corners(base_lo,base_hi)
prior_leaves=[adaptive_positive(pairing(a,bold)) for a in prior_corners]
prior_routh=routh_column(prior_corners[0])
require(all(x>0 for x in prior_routh),'PRIOR_REFERENCE_ROUTH')

result={
 'scope':'Exact rational review of one base box, its endpoint neighborhood, and separately named preceding search-box metadata; not a universal SPR theorem or a novelty review',
 'input_sha256':{str(k):v for k,v in PINS.items()},
 'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
 'box_widths':[hi[i]-lo[i] for i in range(7)],
 'prior_box_midpoints_match':True,'prior_width_factors':[F(101,100)]*6+[F(1,2)],
 'root_signs':root_signs,'root_bands':bands,'brackets_checked':12,
 'routh_reference_column':routh,'corner_hurwitz_minors':corner_dets,
 'bernstein_leaves':leaf_counts,'bernstein_coefficients_checked':checked_coeffs,
 'bernstein_corner_minima':case_min,'base_pairing_margin':d,'base_ratio_margin':base_ratio,
 'six_member_checks':six,'refined_partition':grid,
 'old_corner_pair_t_7_25':old_pair,'old_corner_modulus_squared_t_7_25':old_modulus,
 'old_corner_ratio_t_7_25':old_pair/old_modulus,
 'radius':rho,'new_B':B,'old_B':Bold,'box_coefficient_bound':S,
 'new_width_margin':wm,'new_pairing_margin':nm,'old_failure_margin':om,'open_uniform_ratio_margin':ratio,
 'controls':controls,
 'prior_box_old_numerator':{'corner_leaf_counts':[len(x) for x in prior_leaves],
    'corner_bernstein_minima':[min(y[2] for y in x) for x in prior_leaves],
    'reference_routh_column':prior_routh},
}
def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(v) for v in x]
    return x
receipt=WAVE/'independent-exact-receipt-v1.json'
with receipt.open('x') as f: json.dump(encode(result),f,indent=2);f.write('\n')
print('PASS: 12 brackets; 28 corner determinants; 224 leaf coefficients; 4 corners and 2 strict interior members; old negative witness; endpoint margins; 4 intended-reason controls; prior-box old numerator')
print('receipt:',receipt)
