# Independent exact replay of the frozen actual-box affine-line obstruction.
# Python Eval only; no producer code, numerical roots or external solver.
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json

raw=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-boundary-affine-obstruction-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='bca55dad8e27f93371bc163093d5d49404eb2bdfd538827b11d7c4076cc131b0':raise ValueError('HASH')
doc=json.loads(raw);lower=[Q(x) for x in doc['lower']];upper=[Q(x) for x in doc['upper']]
if len(lower)!=7 or len(upper)!=7 or not all(Q(0)<l<u for l,u in zip(lower,upper)):raise ValueError('BOX')
verts=[]
for even in (0,1):
    for odd in (0,1):
        a=[Q(0)]*8;a[7]=Q(1)
        for j in (0,2,4,6):a[j]=lower[j] if ((j//2)%2==0)==(even==0) else upper[j]
        for j in (1,3,5):a[j]=lower[j] if ((j//2)%2==0)==(odd==0) else upper[j]
        verts.append(a)
rootpoly={'E-':[lower[0],-upper[2],lower[4],-upper[6]],'E+':[upper[0],-lower[2],upper[4],-lower[6]],
          'O-':[lower[1],-upper[3],lower[5],Q(-1)],'O+':[upper[1],-lower[3],upper[5],Q(-1)]}
if {k:[str(x) for x in v] for k,v in rootpoly.items()}!=doc['root_polynomials']:raise ValueError('ROOT_POLYNOMIAL')
def value(p,t):
    v=Q(0)
    for x in p[::-1]:v=v*t+x
    return v
def check_bracket(poly,left,right):
    if not 0<left<right or value(poly,left)*value(poly,right)>=0:raise ValueError('ROOT_BRACKET')
spans={}
for key,p in rootpoly.items():
    spans[key]=[(Q(l),Q(r)) for l,r in doc['root_intervals'][key]]
    if len(spans[key])!=3 or p[0]<=0 or p[3]>=0:raise ValueError('ROOT_COUNT')
    for left,right in spans[key]:check_bracket(p,left,right)
    if any(spans[key][j][1]>=spans[key][j+1][0] for j in range(2)):raise ValueError('ROOT_OVERLAP')
bands=[]
for i in range(3):
    for parity in ('E','O'):
        bands.append((min(spans[parity+'-'][i][0],spans[parity+'+'][i][0]),max(spans[parity+'-'][i][1],spans[parity+'+'][i][1])))
if any(bands[i][1]>=bands[i+1][0] for i in range(5)):raise ValueError('GLOBAL_BANDS')
def routh(a):
    rows=[[a[7],a[5],a[3],a[1]],[a[6],a[4],a[2],a[0]]]
    for _ in range(6):
        u,v=rows[-2:]
        if v[0]<=0:raise ValueError('ROUTH')
        rows.append([(v[0]*u[k+1]-u[0]*v[k+1])/v[0] for k in range(3)]+[Q(0)])
    col=[x[0] for x in rows]
    if not all(x>0 for x in col):raise ValueError('ROUTH')
    return col
reference=routh(verts[0])
if [str(v) for v in reference]!=doc['reference_routh_first_column']:raise ValueError('ROUTH_BINDING')

lineA=[Q(x) for x in doc['line_a']];lineB=[Q(x) for x in doc['line_b']];theta=Q(doc['threshold'])
if len(lineA)!=8 or len(lineB)!=8 or lineA[7]!=1 or lineB[7]!=1:raise ValueError('LINE_DEGREE')
def pairing_eo(a,b,t):
    E=lambda p:p[0]-p[2]*t+p[4]*t*t-p[6]*t*t*t
    O=lambda p:p[1]-p[3]*t+p[5]*t*t-p[7]*t*t*t
    return E(a)*E(b)+t*O(a)*O(b)
def pairing_direct(a,b,t):
    return sum(a[j]*b[k]*((-1)**abs((k-j)//2))*t**((j+k)//2) for j in range(8) for k in range(8) if (j+k)%2==0)
case_values=[]
for item in doc['line_cases']:
    idx=item['corner_index'];t=Q(item['t']);a=verts[idx]
    if not 0<=idx<4 or t<=0:raise ValueError('ATOM')
    A=pairing_eo(a,lineA,t);B=pairing_eo(a,lineB,t)
    if A!=pairing_direct(a,lineA,t) or B!=pairing_direct(a,lineB,t):raise ValueError('PAIRING_REPLAY')
    D=B-A;P=A+theta*D
    if (str(A),str(D),str(P))!=(item['A'],item['D'],item['value_at_threshold']):raise ValueError('PAIRING_BINDING')
    case_values.append((A,D,P))
def check_contradiction(cases):
    if len(cases)!=2 or cases[0][1]<=0 or cases[1][1]>=0:raise ValueError('SLOPE')
    if cases[0][2]>=0 or cases[1][2]>=0:raise ValueError('THRESHOLD')
check_contradiction(case_values)
controls=[]
def expect(label,reason,fn):
    try:fn()
    except ValueError as error:
        if str(error)!=reason:raise ValueError('WRONG_CONTROL')
        controls.append((label,reason));return
    raise ValueError('CONTROL_ACCEPTED')
left,right=spans['E-'][0]
expect('reverse_bracket','ROOT_BRACKET',lambda:check_bracket(rootpoly['E-'],right,left))
bad=list(case_values);bad[0]=(bad[0][0],-bad[0][1],bad[0][2])
expect('reverse_first_slope','SLOPE',lambda:check_contradiction(bad))
bad=list(case_values);bad[1]=(bad[1][0],bad[1][1],Q(1))
expect('nonnegative_threshold_pairing','THRESHOLD',lambda:check_contradiction(bad))
print('independent affine-line replay:',{'root_brackets':sum(len(x) for x in spans.values()),'global_bands':len(bands),
 'reference_routh_positive':True,'threshold':str(theta),'case_values':[[str(x) for x in v] for v in case_values],'controls':controls})
