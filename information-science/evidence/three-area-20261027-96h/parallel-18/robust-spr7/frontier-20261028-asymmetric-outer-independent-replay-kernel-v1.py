# Standalone independent replay of frozen asymmetric outer-box certificate.
# Python Eval only. Imports no producer, optimizer or search code.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from copy import deepcopy
import json

path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-asymmetric-outer-common-numerator-frozen-v1.json')
blob=path.read_bytes()
if sha256(blob).hexdigest()!='a639c58f792bf88bad9f99d13b7a4e5bc404a6e9c9b39e44ecd1aa39123aac9d':raise ValueError('FROZEN_HASH')
doc=json.loads(blob);lo=[Q(v) for v in doc['lower']];hi=[Q(v) for v in doc['upper']]
nom=[Q(1),Q(1)]
for w in (2,5,11):
    nxt=[Q(0)]*(len(nom)+2)
    for i,v in enumerate(nom):
        nxt[i]+=v*(1+w*w);nxt[i+1]+=2*v;nxt[i+2]+=v
    nom=nxt
if not all(lo[j]<=nom[j]<=hi[j] for j in range(7)):raise ValueError('NOMINAL_NOT_IN_BOX')
if len(lo)!=7 or len(hi)!=7 or not all(0<l<u for l,u in zip(lo,hi)):raise ValueError('BOX')
cs=[]
for even_side in (0,1):
    for odd_side in (0,1):
        a=[Q(0)]*8;a[7]=Q(1)
        for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(even_side==0) else hi[j]
        for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(odd_side==0) else hi[j]
        cs.append(a)
root_poly={'E-':[lo[0],-hi[2],lo[4],-hi[6]],'E+':[hi[0],-lo[2],hi[4],-lo[6]],
           'O-':[lo[1],-hi[3],lo[5],Q(-1)],'O+':[hi[1],-lo[3],hi[5],Q(-1)]}
if {k:[str(x) for x in p] for k,p in root_poly.items()}!=doc['root_polynomials']:raise ValueError('ROOT_POLYS')
def evaluate(p,t):
    v=Q(0)
    for c in reversed(p):v=v*t+c
    return v
def bracket(p,l,r):
    if not 0<l<r or evaluate(p,l)*evaluate(p,r)>=0:raise ValueError('ROOT_BRACKET')
intervals={}
for name,p in root_poly.items():
    if len(p)!=4 or p[0]<=0 or p[-1]>=0:raise ValueError('CUBIC')
    intervals[name]=[(Q(l),Q(r)) for l,r in doc['root_intervals'][name]]
    if len(intervals[name])!=3:raise ValueError('ROOT_COUNT')
    for l,r in intervals[name]:bracket(p,l,r)
    if any(intervals[name][i][1]>=intervals[name][i+1][0] for i in range(2)):raise ValueError('ROOT_ORDER')
bands=[]
for i in range(3):
    for parity in ('E','O'):
        bands.append((min(intervals[parity+'-'][i][0],intervals[parity+'+'][i][0]),max(intervals[parity+'-'][i][1],intervals[parity+'+'][i][1])))
if any(bands[i][1]>=bands[i+1][0] for i in range(5)):raise ValueError('BAND_ORDER')

def det(m):
    A=[[Q(x) for x in row] for row in m];out=Q(1);sign=1;n=len(A)
    for k in range(n):
        j=next((i for i in range(k,n) if A[i][k]),None)
        if j is None:return Q(0)
        if j!=k:A[k],A[j]=A[j],A[k];sign=-sign
        pivot=A[k][k];out*=pivot
        for i in range(k+1,n):
            q=A[i][k]/pivot
            for j in range(k+1,n):A[i][j]-=q*A[k][j]
            A[i][k]=Q(0)
    return sign*out
def hurwitz_minors(a):
    rev=a[::-1]
    def c(i):return rev[i] if 0<=i<8 else Q(0)
    return [det([[c(2*j-i) for j in range(1,n+1)] for i in range(1,n+1)]) for n in range(1,8)]
minors=[hurwitz_minors(a) for a in cs]
if not all(x>0 for row in minors for x in row):raise ValueError('HURWITZ_MINOR')
def routh_col(a):
    rows=[[a[7],a[5],a[3],a[1]],[a[6],a[4],a[2],a[0]]]
    for n in range(6):
        up,cur=rows[-2:]
        if cur[0]<=0:raise ValueError('ROUTH')
        rows.append([(cur[0]*up[k+1]-up[0]*cur[k+1])/cur[0] for k in range(3)]+[Q(0)])
    col=[row[0] for row in rows]
    if not all(v>0 for v in col):raise ValueError('ROUTH')
    return col
if [str(x) for x in routh_col(cs[0])]!=doc['reference_routh_first_column']:raise ValueError('ROUTH_BINDING')

def mul(a,b):
    p=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):p[i+j]+=x*y
    return p
def pair(a,b):
    E=lambda p:[p[0],-p[2],p[4],-p[6]]
    O=lambda p:[p[1],-p[3],p[5],-p[7]]
    ans=mul(E(a),E(b))+[Q(0)]
    for i,v in enumerate(mul(O(a),O(b))):ans[i+1]+=v
    return ans
def bernstein(poly,left,right):
    powers=[sum(poly[k]*(-1)**(j-k)*comb(7-k,j-k) for k in range(j+1)) for j in range(8)]
    sub=[sum(powers[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,8)) for j in range(8)]
    return [sum(sub[j]*Q(comb(i,j),comb(7,j)) for j in range(i+1)) for i in range(8)]
def leaf_check(poly,leaf):
    left,right=Q(leaf['left']),Q(leaf['right'])
    if not 0<=left<right<=1:raise ValueError('LEAF_RANGE')
    coeffs=bernstein(poly,left,right)
    if coeffs!=[Q(x) for x in leaf['coefficients']]:raise ValueError('LEAF_MISMATCH')
    if not all(x>0 for x in coeffs):raise ValueError('LEAF_NONPOSITIVE')
    return coeffs
b=[Q(x) for x in doc['numerator']]
if len(b)!=8 or b[-1]!=1 or not all(x>0 for x in b):raise ValueError('NUMERATOR')
counts=[];minimum=[]
for i,a in enumerate(cs):
    poly=pair(a,b)
    if [str(x) for x in poly]!=doc['pairing_polynomials'][i]:raise ValueError('POLY_BINDING')
    proof=doc['bernstein_proofs'][i]
    if proof['status']!='STRICT_POSITIVITY':raise ValueError('PROOF_STATUS')
    leaves=sorted(proof['leaves'],key=lambda x:Q(x['left']));position=Q(0)
    for leaf in leaves:
        if Q(leaf['left'])!=position:raise ValueError('LEAF_COVERAGE')
        minimum.extend(leaf_check(poly,leaf));position=Q(leaf['right'])
    if position!=1:raise ValueError('LEAF_COVERAGE')
    counts.append(len(leaves))
delta=min(minimum);S=1+sum(hi)
if delta!=Q(doc['pairing_margin']) or S!=Q(doc['coefficient_sum_upper']) or delta/(S*S)!=Q(doc['ratio_margin']):raise ValueError('MARGINS')
controls=[]
def reject(label,reason,fn):
    try:fn()
    except ValueError as error:
        if str(error)!=reason:raise ValueError('CONTROL_WRONG:'+label)
        controls.append(label);return
    raise ValueError('CONTROL_ACCEPTED:'+label)
fault=deepcopy(doc['bernstein_proofs'][0]['leaves'][0]);fault['coefficients'][0]=str(Q(fault['coefficients'][0])+1)
reject('leaf_coefficient','LEAF_MISMATCH',lambda:leaf_check(pair(cs[0],b),fault))
a,z=intervals['E-'][0];reject('root_reversal','ROOT_BRACKET',lambda:bracket(root_poly['E-'],z,a))
print('independent asymmetric outer-box replay:',{'minors_positive':sum(len(x) for x in minors),'root_brackets':sum(len(x) for x in intervals.values()),
 'separated_root_bands':len(bands),'routh_positive':True,'leaf_counts':counts,'delta':str(delta),'S':str(S),
 'ratio':str(delta/S**2),'rejected_mutations':controls})
