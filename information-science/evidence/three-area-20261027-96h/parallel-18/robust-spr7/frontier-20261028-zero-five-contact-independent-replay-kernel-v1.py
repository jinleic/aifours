# Standalone exact zero-plus-five-contact family replay; no producer/search imports.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import comb
from copy import deepcopy
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-zero-five-contact-uniform-numerator-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='db0016d05c0792617af81724ed40875df4fb0eb34521a75fa707afb5c912a763':raise ValueError('HASH')
d=json.loads(raw);lo=[Q(x) for x in d['boundary_lower']];hi=[Q(x) for x in d['boundary_upper']]
if len(lo)!=7 or lo[0]!=0 or not all(lo[j]<hi[j] for j in range(7)) or not all(lo[j]>0 for j in range(1,7)):raise ValueError('BOX')
center=[(lo[j]+hi[j])/2 for j in range(7)]+[Q(1)]
if [str(x) for x in center]!=d['center']:raise ValueError('CENTER')
def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def from_roots(spec):
    v=[Q(1)]
    for r in spec['roots']:v=mul(v,[-Q(r),Q(1)])
    return [-Q(spec['negative_scale'])*x for x in v]
polys={'E-':[lo[0],-hi[2],lo[4],-hi[6]],'E+':[hi[0],-lo[2],hi[4],-lo[6]],
       'O-':[lo[1],-hi[3],lo[5],Q(-1)],'O+':[hi[1],-lo[3],hi[5],Q(-1)]}
if any(polys[k]!=from_roots(d['boundary_root_spec'][k]) for k in polys):raise ValueError('ROOT_FACTORIZATION')
def parity(a,t):return a[0]-a[2]*t+a[4]*t*t-a[6]*t**3,a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
def corners(lower,upper):
    result=[]
    for es in (0,1):
        for oside in (0,1):
            a=[Q(0)]*8;a[7]=Q(1)
            for j in (0,2,4,6):a[j]=lower[j] if ((j//2)%2==0)==(es==0) else upper[j]
            for j in (1,3,5):a[j]=lower[j] if ((j//2)%2==0)==(oside==0) else upper[j]
            result.append(a)
    return result
cs=corners(lo,hi)
if not all(parity(cs[ci],Q(0))[0]==0 for ci in (0,1)):raise ValueError('ORIGIN_CONTACT')
contacts=[(z['corner'],Q(z['t'])) for z in d['contacts']]
if contacts!=[(2,Q(1)),(3,Q(2)),(1,Q(4)),(0,Q(7)),(2,Q(10))]:raise ValueError('CONTACT_LIST')
for ci,t in contacts:
    if parity(cs[ci],t)!=(Q(0),Q(0)):raise ValueError('CONTACT_ZERO')
    ev=[parity(a,t)[0] for a in cs];ov=[parity(a,t)[1] for a in cs]
    if [[str(min(ev)),str(max(ev))],[str(min(ov)),str(max(ov))]]!=d['marker_intervals'][str(t)]:raise ValueError('MARKER')
    e,o=parity(center,t)
    expected={Q(1):(-1,1),Q(2):(-1,-1),Q(4):(1,-1),Q(7):(1,1),Q(10):(-1,1)}[t]
    if (1 if e>0 else -1,1 if o>0 else -1)!=expected or not e or not o:raise ValueError('CENTER_SIGN')
def routh(a):
    rows=[[a[7],a[5],a[3],a[1]],[a[6],a[4],a[2],a[0]]]
    for _ in range(6):
        p,q=rows[-2:]
        if q[0]<=0:raise ValueError('ROUTH')
        rows.append([(q[0]*p[j+1]-p[0]*q[j+1])/q[0] for j in range(3)]+[Q(0)])
    return [r[0] for r in rows]
col=routh(center)
if not all(x>0 for x in col) or [str(x) for x in col]!=d['reference_routh_first_column']:raise ValueError('ROUTH')
def det(m):
    A=[[Q(x) for x in row] for row in m];v=Q(1);sign=1;n=len(A)
    for k in range(n):
        r=next((r for r in range(k,n) if A[r][k]),None)
        if r is None:return Q(0)
        if r!=k:A[k],A[r]=A[r],A[k];sign=-sign
        pivot=A[k][k];v*=pivot
        for r in range(k+1,n):
            q=A[r][k]/pivot
            for j in range(k+1,n):A[r][j]-=q*A[k][j]
            A[r][k]=Q(0)
    return sign*v
def minors(a):
    a=a[::-1]
    def c(k):return a[k] if 0<=k<8 else Q(0)
    return [det([[c(2*j-i) for j in range(1,n+1)] for i in range(1,n+1)]) for n in range(1,8)]
rho=Q(999,1000);smalllo=[center[j]-rho*(hi[j]-lo[j])/2 for j in range(7)];smallhi=[center[j]+rho*(hi[j]-lo[j])/2 for j in range(7)]
if not all(x>0 for a in corners(smalllo,smallhi) for x in minors(a)):raise ValueError('HURWITZ_MINORS')
b=[Q(x) for x in d['numerator']]
if len(b)!=8 or b[-1]!=1 or not all(x>0 for x in b):raise ValueError('NUMERATOR')
def pair(a,b):
    E=lambda p:[p[0],-p[2],p[4],-p[6]]
    O=lambda p:[p[1],-p[3],p[5],-p[7]]
    out=mul(E(a),E(b))+[Q(0)]
    for j,x in enumerate(mul(O(a),O(b))):out[j+1]+=x
    return out
def factor(poly,res,roots):
    q=res
    for t,mult in roots:
        for _ in range(mult):q=mul(q,[-t,Q(1)])
    if q!=poly:raise ValueError('FACTORIZATION')
def beta(poly,left,right):
    n=len(poly)-1
    p=[sum(poly[k]*(-1)**(j-k)*comb(n-k,j-k) for k in range(j+1)) for j in range(n+1)]
    a=[sum(p[k]*comb(k,j)*left**(k-j)*(right-left)**j for k in range(j,n+1)) for j in range(n+1)]
    return [sum(a[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]
def leaf(poly,item):
    l,r=Q(item['left']),Q(item['right'])
    if not 0<=l<r<=1:raise ValueError('LEAF_RANGE')
    c=beta(poly,l,r)
    if c!=[Q(v) for v in item['coefficients']]:raise ValueError('LEAF_MISMATCH')
    if not all(x>0 for x in c):raise ValueError('LEAF_SIGN')
    return c
def cover(poly,proof,status):
    if proof['status']!=status:raise ValueError('PROOF_STATUS')
    leaves=sorted(proof['leaves'],key=lambda x:Q(x['left']));at=Q(0);coeff=[]
    for item in leaves:
        if Q(item['left'])!=at:raise ValueError('LEAF_COVERAGE')
        coeff.extend(leaf(poly,item));at=Q(item['right'])
    if at!=1:raise ValueError('LEAF_COVERAGE')
    return len(leaves),coeff
counts=[]
for i,a in enumerate(cs):
    p=pair(a,b)
    if [str(x) for x in p]!=d['boundary_polynomials'][i]:raise ValueError('PAIR')
    res=[Q(x) for x in d['boundary_residual_polynomials'][i]];roots=[(Q(t),int(mult)) for t,mult in d['boundary_factors'][i]]
    factor(p,res,roots);n,c=cover(res,d['boundary_proofs'][i],'NONNEGATIVE_PROVED');counts.append(n)
    if pair([(x+y)/2 for x,y in zip(center,a)],b)!=[(x+y)/2 for x,y in zip(pair(center,b),p)]:raise ValueError('AFFINE')
cp=pair(center,b)
if [str(x) for x in cp]!=d['center_polynomial']:raise ValueError('CENTER_PAIR')
cn,coeff=cover(cp,d['center_proof'],'STRICT_POSITIVITY');delta=min(coeff);S=1+sum(hi)
if delta!=Q(d['center_margin']) or S!=Q(d['S_at_one']) or delta/S**2!=Q(d['uniform_ratio_coefficient']):raise ValueError('MARGINS')
controls=[]
def reject(label,reason,f):
    try:f()
    except ValueError as e:
        if str(e)!=reason:raise ValueError('CONTROL_WRONG:'+label)
        controls.append(label);return
    raise ValueError('CONTROL_ACCEPTED:'+label)
err=deepcopy(d['boundary_proofs'][0]['leaves'][0]);err['coefficients'][0]=str(Q(err['coefficients'][0])+1)
reject('leaf','LEAF_MISMATCH',lambda:leaf([Q(x) for x in d['boundary_residual_polynomials'][0]],err))
rr=[Q(x) for x in d['boundary_residual_polynomials'][2]];rr[0]+=1
reject('factor','FACTORIZATION',lambda:factor(pair(cs[2],b),rr,[(Q(1),2),(Q(10),2)]))
print('independent zero-plus-five-contact replay:',{'root_factorizations':4,'boundary_contacts':5,'center_signs':5,'routh_positive':True,'corner_minors_positive':28,
 'boundary_leaf_counts':counts,'center_leaf_count':cn,'center_margin':str(delta),'S_at_one':str(S),'ratio_coefficient':str(delta/S**2),'controls':controls})
