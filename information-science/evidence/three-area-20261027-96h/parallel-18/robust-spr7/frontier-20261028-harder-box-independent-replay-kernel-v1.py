# Independent exact replay of the frozen actual-box numerator certificate.
# Run in Python Eval only. No search, optimizer, or previous checker is imported.
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from math import comb
from copy import deepcopy
import json

frozen_path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-harder-box-common-numerator-frozen-v1.json')
raw=frozen_path.read_bytes()
if sha256(raw).hexdigest()!='74c3ccc312cb0e7b86b8c76f2e89ab2043d36288454720c583ca2bf8a5027eec':raise ValueError('FROZEN_HASH')
frozen=json.loads(raw)
lo=[Q(x) for x in frozen['lower']];hi=[Q(x) for x in frozen['upper']]
if len(lo)!=7 or len(hi)!=7 or not all(0<x<y for x,y in zip(lo,hi)):raise ValueError('BOX')

# Reconstruct the four actual corners without importing producer code.
cs=[]
for es in (0,1):
    for odd_index in (0,1):
        a=[Q(0)]*8;a[7]=Q(1)
        for j in (0,2,4,6):a[j]=(lo[j] if ((j//2)%2==0)==(es==0) else hi[j])
        for j in (1,3,5):a[j]=(lo[j] if ((j//2)%2==0)==(odd_index==0) else hi[j])
        cs.append(a)

polys={'E-':[lo[0],-hi[2],lo[4],-hi[6]],'E+':[hi[0],-lo[2],hi[4],-lo[6]],
       'O-':[lo[1],-hi[3],lo[5],Q(-1)],'O+':[hi[1],-lo[3],hi[5],Q(-1)]}
if {k:[str(x) for x in v] for k,v in polys.items()}!=frozen['root_polynomials']:raise ValueError('ROOT_POLYNOMIAL')
def ev(p,x):
    value=Q(0)
    for c in p[::-1]:value=value*x+c
    return value
def verify_bracket(p,left,right):
    if not 0<left<right or ev(p,left)*ev(p,right)>=0:raise ValueError('ROOT_BRACKET')
intervals={}
for key,p in polys.items():
    if len(p)!=4 or p[0]<=0 or p[3]>=0:raise ValueError('CUBIC_DEGREE')
    intervals[key]=[(Q(x),Q(y)) for x,y in frozen['root_intervals'][key]]
    if len(intervals[key])!=3:raise ValueError('ROOT_COUNT')
    for l,r in intervals[key]:verify_bracket(p,l,r)
    if any(intervals[key][i][1]>=intervals[key][i+1][0] for i in range(2)):raise ValueError('ROOT_DISJOINT')
bands=[]
for i in range(3):
    for parity in ('E','O'):
        bands.append((min(intervals[parity+'-'][i][0],intervals[parity+'+'][i][0]),
                      max(intervals[parity+'-'][i][1],intervals[parity+'+'][i][1])))
if any(bands[i][1]>=bands[i+1][0] for i in range(5)):raise ValueError('GLOBAL_BANDS')

# Independent rational Gaussian determinant calculation for every Hurwitz minor.
def determinant(matrix):
    A=[[Q(x) for x in row] for row in matrix];sign=1;out=Q(1);n=len(A)
    for col in range(n):
        row=next((r for r in range(col,n) if A[r][col]),None)
        if row is None:return Q(0)
        if row!=col:A[col],A[row]=A[row],A[col];sign=-sign
        pivot=A[col][col];out*=pivot
        for r in range(col+1,n):
            f=A[r][col]/pivot
            for k in range(col+1,n):A[r][k]-=f*A[col][k]
            A[r][col]=Q(0)
    return sign*out

def determinants(a):
    c=[a[7-j] for j in range(8)]
    def coef(k):return c[k] if 0<=k<8 else Q(0)
    return [determinant([[coef(2*(j+1)-(i+1)) for j in range(n)] for i in range(n)]) for n in range(1,8)]
dets=[determinants(a) for a in cs]
if not all(v>0 for row in dets for v in row):raise ValueError('HURWITZ_DETERMINANT')

# Recompute reference Routh column by rational recurrence, independently of dets.
def routh_col(a):
    rows=[[a[7],a[5],a[3],a[1]],[a[6],a[4],a[2],a[0]]]
    for _ in range(6):
        u,v=rows[-2:]
        if v[0]<=0:raise ValueError('ROUTH')
        rows.append([(v[0]*u[k+1]-u[0]*v[k+1])/v[0] for k in range(3)]+[Q(0)])
    col=[r[0] for r in rows]
    if not all(x>0 for x in col):raise ValueError('ROUTH')
    return col
col=routh_col(cs[0])
if [str(x) for x in col]!=frozen['reference_routh_first_column']:raise ValueError('ROUTH_BINDING')

b=[Q(x) for x in frozen['numerator']]
if len(b)!=8 or b[-1]!=1 or not all(x>0 for x in b):raise ValueError('NUMERATOR')
def multiply(x,y):
    out=[Q(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):out[i+j]+=a*b
    return out

def pair(a,b):
    E=lambda p:[p[0],-p[2],p[4],-p[6]]
    O=lambda p:[p[1],-p[3],p[5],-p[7]]
    p=multiply(E(a),E(b))+[Q(0)]
    for k,x in enumerate(multiply(O(a),O(b))):p[k+1]+=x
    return p

# Direct affine power substitution, independently of de Casteljau subdivision.
def bernstein_interval(poly,left,right):
    q=[sum(poly[k]*((-1)**(n-k))*comb(7-k,n-k) for k in range(n+1)) for n in range(8)]
    power=[sum(q[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,8)) for j in range(8)]
    return [sum(power[j]*Q(comb(i,j),comb(7,j)) for j in range(i+1)) for i in range(8)]

def verify_leaf(poly,leaf):
    left,right=Q(leaf['left']),Q(leaf['right'])
    if not 0<=left<right<=1:raise ValueError('LEAF_RANGE')
    reconstructed=bernstein_interval(poly,left,right)
    if reconstructed!=[Q(x) for x in leaf['coefficients']]:raise ValueError('LEAF_MISMATCH')
    if not all(x>0 for x in reconstructed):raise ValueError('LEAF_NONPOSITIVE')
    return reconstructed

leaf_counts=[];mins=[]
for i,a in enumerate(cs):
    p=pair(a,b)
    if [str(x) for x in p]!=frozen['pairing_polynomials'][i]:raise ValueError('PAIRING_POLYNOMIAL')
    proof=frozen['bernstein_proofs'][i]
    if proof['status']!='STRICT_POSITIVITY':raise ValueError('PROOF_STATUS')
    leaves=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0)
    for leaf in leaves:
        if Q(leaf['left'])!=at:raise ValueError('LEAF_COVERAGE')
        mins.extend(verify_leaf(p,leaf));at=Q(leaf['right'])
    if at!=1:raise ValueError('LEAF_COVERAGE')
    leaf_counts.append(len(leaves))
delta=min(mins)
if delta!=Q(frozen['pairing_margin']):raise ValueError('MARGIN')
S=1+sum(hi)
if S!=Q(frozen['coefficient_sum_upper']) or delta/(S*S)!=Q(frozen['ratio_margin']):raise ValueError('RATIO_MARGIN')
old=[Q(x) for x in frozen['old_numerator']];old_t=Q(frozen['old_numerator_failing_t'])
old_p=ev(pair(cs[frozen['old_numerator_failing_corner']],old),old_t)
if old_p!=Q(frozen['old_numerator_pairing']) or old_p>=0:raise ValueError('OLD_FAILURE')

controls=[]
def expect(label,reason,fn):
    try:fn()
    except ValueError as error:
        if str(error)!=reason:raise ValueError('CONTROL_WRONG:'+label+':'+str(error))
        controls.append((label,str(error)));return
    raise ValueError('CONTROL_ACCEPTED:'+label)
leaf=deepcopy(frozen['bernstein_proofs'][0]['leaves'][0]);leaf['coefficients'][0]=str(Q(leaf['coefficients'][0])+1)
expect('corrupt_leaf','LEAF_MISMATCH',lambda:verify_leaf(pair(cs[0],b),leaf))
left,right=intervals['E-'][0]
expect('reverse_root_bracket','ROOT_BRACKET',lambda:verify_bracket(polys['E-'],right,left))
print('independent actual-box replay:',{'four_corner_minor_counts':[len(x) for x in dets],
 'all_corner_minors_positive':True,'root_brackets':sum(len(x) for x in intervals.values()),
 'global_root_bands':len(bands),'reference_routh_positive':True,'leaf_counts':leaf_counts,
 'pairing_margin':str(delta),'ratio_margin':str(delta/(S*S)),'old_numerator_negative_pairing':str(old_p),'controls':controls})
