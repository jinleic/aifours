# Standalone exact verification of three-gap family and finite-grid duality.
# The all-parameter stability claim follows separately from the marker signs.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json
p=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-three-gap-family-and-grid-frozen-v1.json')
raw=p.read_bytes()
if sha256(raw).hexdigest()!='6984f81b8bd94ad5379195b393b2662cfc43ca48a0cf1287e2acf3135ff633a9':raise ValueError('FROZEN_HASH')
d=json.loads(raw)
def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
center=[Q(1),Q(1)]
for v in (2,4,8):center=mul(center,[Q(1+v*v),Q(2),Q(1)])
if [str(x) for x in center]!=d['center']:raise ValueError('CENTER')
h=[Q(x) for x in d['halfwidth']];rho=Q(d['checked_scale'])
if len(h)!=7 or not all(0<h[i]<center[i] for i in range(7)) or not 0<rho<1:raise ValueError('WIDTH')
lo=[center[j]-rho*h[j] for j in range(7)];hi=[center[j]+rho*h[j] for j in range(7)]
if [str(x) for x in lo]!=d['lower'] or [str(x) for x in hi]!=d['upper']:raise ValueError('BOX')
def parity(a,t):return (a[0]-a[2]*t+a[4]*t**2-a[6]*t**3,a[1]-a[3]*t+a[5]*t**2-a[7]*t**3)
def bounds(t):
    e,o=parity(center,t);de=sum(h[2*j]*t**j for j in range(4));do=sum(h[2*j+1]*t**j for j in range(3))
    return [e-de,e+de,o-do,o+do]
def check_marker(t,stored):
    v=bounds(t)
    if [str(x) for x in v]!=stored:raise ValueError('MARKER_BINDING')
    return v
markers={Q(t):check_marker(Q(t),v) for t,v in d['marker_intervals_at_scale_one'].items()}
for t,sgn in [(Q(3),(-1,1)),(Q(15),(1,-1)),(Q(65),(-1,1))]:
    emin,emax,omin,omax=markers[t];e,o=parity(center,t)
    if sgn==(-1,1) and not (emax==0 and omin==0 and e<0<o):raise ValueError('CONTACT_SIGNS')
    if sgn==(1,-1) and not (emin==0 and omax==0 and o<0<e):raise ValueError('CONTACT_SIGNS')
if not (markers[Q(17,2)][1]<0 and markers[Q(17,2)][3]<0 and markers[Q(30)][0]>0 and markers[Q(30)][2]>0):raise ValueError('SEPARATORS')

def actual_corners(lower,upper):
    out=[]
    for es in (0,1):
        for oside in (0,1):
            a=[Q(0)]*8;a[7]=Q(1)
            for j in (0,2,4,6):a[j]=lower[j] if ((j//2)%2==0)==(es==0) else upper[j]
            for j in (1,3,5):a[j]=lower[j] if ((j//2)%2==0)==(oside==0) else upper[j]
            out.append(a)
    return out
cs=actual_corners(lo,hi);boundary=actual_corners([center[j]-h[j] for j in range(7)],[center[j]+h[j] for j in range(7)])
for item in d['boundary_zero_atoms']:
    if parity(boundary[item['corner']],Q(item['t']))!=(Q(0),Q(0)):raise ValueError('BOUNDARY_ZERO')
def determinant(mat):
    a=[[Q(v) for v in row] for row in mat];ans=Q(1);sign=1;n=len(a)
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return Q(0)
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        x=a[k][k];ans*=x
        for i in range(k+1,n):
            q=a[i][k]/x
            for j in range(k+1,n):a[i][j]-=q*a[k][j]
            a[i][k]=Q(0)
    return sign*ans
def minors(a):
    coeff=a[::-1]
    def c(k):return coeff[k] if 0<=k<8 else Q(0)
    return [determinant([[c(2*j-i) for j in range(1,n+1)] for i in range(1,n+1)]) for n in range(1,8)]
if not all(x>0 for a in cs for x in minors(a)):raise ValueError('HURWITZ_MINOR')
def pairing(a,b,t):
    ea,oa=parity(a,t);eb,ob=parity(b,t)
    return ea*eb+t*oa*ob
failure=d['midpoint_numerator_failure'];value=pairing(cs[failure['corner']],center,Q(failure['t']))
if value!=Q(failure['pairing']) or value>=0:raise ValueError('MIDPOINT_FAILURE')

last=d['search_rounds'][-1];grid=[Q(x) for x in last['nodes'] if x!='infinity'];margin=Q(last['margin'])
b=[Q(x) for x in d['final_grid_dual_monic']]
if len(b)!=8 or b[-1]!=1 or not all(x>0 for x in b):raise ValueError('DUAL_SIGN')
bnorm=[v/sum(b) for v in b]
vals=[pairing(a,bnorm,t)/(1+t)**7 for a in cs for t in grid]+[bnorm[7]]
if len(vals)!=last['atoms'] or min(vals)!=margin or min(vals)<=0:raise ValueError('DUAL_GRID')
support=d['final_grid_primal_support']
def check_support(items):
    if not items or not all(Q(x['weight'])>0 for x in items) or sum(Q(x['weight']) for x in items)!=1:raise ValueError('PRIMAL_SUM')
    for x in items:
        if x['t']=='infinity':
            if x['corner'] is not None:raise ValueError('INFINITY')
        elif Q(x['t']) not in grid or x['corner'] not in range(4):raise ValueError('SUPPORT')
check_support(support)
F=[]
for k in range(8):
    unit=[Q(0)]*8;unit[k]=Q(1);v=Q(0)
    for x in support:
        w=Q(x['weight'])
        v+=w*(pairing(cs[x['corner']],unit,Q(x['t']))/(1+Q(x['t']))**7 if x['t']!='infinity' else unit[7])
    F.append(v)
if max(F)!=margin:raise ValueError('PRIMAL_OPTIMUM')
controls=[]
def reject(label,reason,f):
    try:f()
    except ValueError as e:
        if str(e)!=reason:raise ValueError('CONTROL_WRONG:'+label)
        controls.append(label);return
    raise ValueError('CONTROL_ACCEPTED:'+label)
wrong=deepcopy(d['marker_intervals_at_scale_one']['3']);wrong[1]='1'
reject('marker_corruption','MARKER_BINDING',lambda:check_marker(Q(3),wrong))
wrong=deepcopy(support);wrong[0]['weight']=str(Q(wrong[0]['weight'])+1)
reject('weight_corruption','PRIMAL_SUM',lambda:check_support(wrong))
print('independent three-gap replay:',{'center_factorization':True,'marker_signs':5,'boundary_zero_atoms':len(d['boundary_zero_atoms']),
 'positive_corner_minors':28,'midpoint_failure':str(value),'grid_atoms':len(vals),'support':len(support),'primal_dual_margin':str(margin),
 'dual_all_coefficients_positive':True,'rejected_mutations':controls})
