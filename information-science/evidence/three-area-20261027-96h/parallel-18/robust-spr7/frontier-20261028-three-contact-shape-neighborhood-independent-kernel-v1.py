# Standalone exact bivariate replay. No search helpers imported.
# Cramer determinants give numerator coefficients of x-degree <=3, and
# affine box corners give pairing coefficients of x-degree <=4. Five exact
# evaluations thus determine every parameter polynomial identically.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,digest):
    raw=(root/name).read_bytes()
    if sha256(raw).hexdigest()!=digest:raise ValueError('HASH:'+name)
    return json.loads(raw)
p=load('frontier-20261028-three-contact-shape-neighborhood-frozen-v1.json','f7888e1b48d2cb7de599e4d0c4f62082eb1e0d2d0e83a83d50e92888f87a9439')
fam=load('frontier-20261028-three-gap-family-and-grid-frozen-v1.json','6984f81b8bd94ad5379195b393b2662cfc43ca48a0cf1287e2acf3135ff633a9')
u=load('frontier-20261028-three-gap-universal-numerator-frozen-v1.json','6c89ae0515bfb0a8305e0fb8da487b61a629b9a3328a5a7529290d8315299f54')
if p['family_frozen_sha256']!='6984f81b8bd94ad5379195b393b2662cfc43ca48a0cf1287e2acf3135ff633a9' or p['universal_frozen_sha256']!='6c89ae0515bfb0a8305e0fb8da487b61a629b9a3328a5a7529290d8315299f54':raise ValueError('BINDING')
center=[Q(x) for x in fam['center']];orig_h=[Q(x) for x in fam['halfwidth']]
base=[Q(x) for x in p['even_width_base']];slope=[Q(x) for x in p['even_width_slope']];odd=[Q(x) for x in p['fixed_odd_widths']]
xc=Q(p['x_center']);left=Q(p['left']);right=Q(p['right']);eps=Q(p['epsilon'])
if xc-left!=eps or right-xc!=eps:raise ValueError('INTERVAL')
def widths(x):return [base[0]+slope[0]*x,odd[0],base[1]+slope[1]*x,odd[1],base[2]+slope[2]*x,odd[2],x]
if widths(xc)!=orig_h:raise ValueError('WIDTH_CENTER')
def parity(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
def corners(lo,hi):
    out=[]
    for es in (0,1):
        for oside in (0,1):
            a=[Q(0)]*8;a[7]=Q(1)
            for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
            for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
            out.append(a)
    return out
def boundary(x):
    h=widths(x)
    if not all(0<h[j]<center[j] for j in range(7)):raise ValueError('WIDTH')
    return corners([center[j]-h[j] for j in range(7)],[center[j]+h[j] for j in range(7)])
contacts=list(zip(p['contact_corners'],[Q(x) for x in p['contact_points']]))
if contacts!=[(2,Q(3)),(1,Q(15)),(2,Q(65))]:raise ValueError('CONTACT_LIST')
for x in (left,right):
    v=boundary(x)
    for ci,t in contacts:
        if parity(v[ci],t)!=(Q(0),Q(0)):raise ValueError('CONTACT')
    # All corners obey E<0,O<0 at 17/2 and E>0,O>0 at 30.
    if not all(e<0 and o<0 for e,o in (parity(a,Q(17,2)) for a in v)):raise ValueError('FIRST_SEPARATOR')
    if not all(e>0 and o>0 for e,o in (parity(a,Q(30)) for a in v)):raise ValueError('SECOND_SEPARATOR')
    for ci,t in contacts:
        e,o=parity(center,t)
        if not ((t in (3,65) and e<0<o) or (t==15 and o<0<e)):raise ValueError('CENTER_SIGN')
free={int(k):Q(v) for k,v in p['fixed_monic_numerator_coefficients'].items()}
if set(free)!={1,3,5,6,7} or free[7]!=1:raise ValueError('FREE')
if any(free[j]!=Q(u['numerator'][j]) for j in free):raise ValueError('FREE_BINDING')
def det(A):
    return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def pair(a,b):
    E=lambda p:[p[0],-p[2],p[4],-p[6]]
    O=lambda p:[p[1],-p[3],p[5],-p[7]]
    out=mul(E(a),E(b))+[Q(0)]
    for i,v in enumerate(mul(O(a),O(b))):out[i+1]+=v
    return out
def divide(poly,r):
    q=[Q(0)]*(len(poly)-1);q[-1]=poly[-1]
    for i in range(len(q)-2,-1,-1):q[i]=poly[i+1]+r*q[i+1]
    if poly[0]+r*q[0]!=0:raise ValueError('FACTOR_REMAINDER')
    return q
def beta(poly,left,right):
    n=len(poly)-1
    q=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
    a=[sum(q[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
    return [sum(a[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def intervals(proof):
    arr=sorted([(Q(s['left']),Q(s['right'])) for s in proof['leaves']]);at=Q(0)
    for a,b in arr:
        if a!=at or not a<b:raise ValueError('LEAF_COVERAGE')
        at=b
    if at!=1:raise ValueError('LEAF_COVERAGE')
    return arr
regions=[intervals(v) for v in u['boundary_nonnegative_proofs']]+[intervals(u['center_proof'])]
if [len(v) for v in regions]!=p['t_leaf_counts']:raise ValueError('LEAF_COUNTS')

def samples_at(x):
    vertices=boundary(x);A=[];rhs=[]
    for ci,t in contacts:
        a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
        ob=free[1]-free[3]*t+free[5]*t*t-t**3
        A.append([ep,-t*ep,t*t*ep]);rhs.append(ep*free[6]*t**3-t*op*ob)
    D=det(A);sgn=p['determinant_sign'];numerator=[Q(0)]*8
    for k,v in free.items():numerator[k]=sgn*D*v
    for j,k in enumerate((0,2,4)):
        Aj=[[rhs[r] if c==j else A[r][c] for c in range(3)] for r in range(3)]
        numerator[k]=sgn*det(Aj)
    if numerator[7]<=0:raise ValueError('NUMERATOR_SIGN')
    vals=numerator[:];root_lists={1:[Q(15)],2:[Q(3),Q(65)]}
    for ci,a in enumerate(vertices):
        poly=pair(a,numerator);res=poly
        for t in root_lists.get(ci,[]):res=divide(divide(res,t),t)
        rebuilt=res
        for t in root_lists.get(ci,[]):rebuilt=mul(rebuilt,[t*t,-2*t,Q(1)])
        if rebuilt!=poly:raise ValueError('FACTOR_REBUILD')
        for lo,hi in regions[ci]:vals.extend(beta(res,lo,hi))
    cp=pair(center,numerator)
    for lo,hi in regions[4]:vals.extend(beta(cp,lo,hi))
    return vals
# Independent interpolation through monomials, then conversion to Bernstein.
def inverse(A):
    n=len(A);M=[[Q(v) for v in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        i=next((i for i in range(k,n) if M[i][k]),None)
        if i is None:raise ValueError('SINGULAR')
        M[k],M[i]=M[i],M[k];v=M[k][k];M[k]=[x/v for x in M[k]]
        for i in range(n):
            if i!=k:
                v=M[i][k];M[i]=[x-v*y for x,y in zip(M[i],M[k])]
    return [row[n:] for row in M]
z=[Q(j,4) for j in range(5)];Vinv=inverse([[v**k for k in range(5)] for v in z])
samples=[samples_at(left+(right-left)*v) for v in z]
if not all(len(v)==p['checked_t_coefficient_polynomials'] for v in samples):raise ValueError('DIMENSIONS')
def parameter_coeffs(values):
    power=[sum(Vinv[k][r]*values[r] for r in range(5)) for k in range(5)]
    return [sum(power[k]*Q(comb(i,k),comb(4,k)) for k in range(i+1)) for i in range(5)]
def require_positive(coeff):
    if not all(v>0 for v in coeff):raise ValueError('PARAMETER_SIGN')
mins=[]
for j in range(len(samples[0])):
    c=parameter_coeffs([row[j] for row in samples]);require_positive(c);mins.append(min(c))
if min(mins)!=Q(p['minimum']) or len(mins)*5!=p['parameter_bernstein_coefficients']:raise ValueError('MINIMUM')
try:require_positive([Q(1),Q(-1)])
except ValueError as e:
    if str(e)!='PARAMETER_SIGN':raise
else:raise ValueError('CONTROL_ACCEPTED')
Smax=max(1+sum(center[j]+widths(x)[j] for j in range(7)) for x in (left,right))
print('independent shape-neighborhood replay:',{'interval':[str(left),str(right)],'width_and_marker_endpoints':2,
 'contact_identities_at_endpoints':6,'t_leaf_counts':[len(v) for v in regions],'t_coefficient_polynomials':len(mins),
 'positive_parameter_bernstein_coefficients':len(mins)*5,'minimum':str(min(mins)),'Smax':str(Smax),
 'negative_sign_control_rejected':True})
