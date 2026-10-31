#!/usr/bin/env python3
"""Independent arithmetic and tensor-algebra review of the pinned (2,2,6) packet.
Only Python standard library. No author code imported or executed.
"""
import hashlib, itertools, json, math, subprocess
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

R = Path(__file__).resolve().parent
E = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
N = {
 'pencil': ('frontier-20261028-level6-free-22-pencil-v1.json','b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc'),
 'poly': ('frontier-20261028-level6-free-22-determinant-v1.json','874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8'),
 'sign': ('frontier-20261028-level6-226-gap41-sign-certificate-v1.json','998c3acbfbe956542fa16f95cf0506af29db0fd51401eec59d89a0b7b8eeb35d'),
 'witness': ('frontier-20261028-level6-226-naive-accretivity-obstruction-v1.json','0c472e2f56e2fd5bc7305b351f96aa5c1982c36380ed35e2128471497e956520'),
 'wide': ('frontier-20261028-level6-226-wide-gap-minor-obstruction-v1.json','ecdf2fb17a36ed926811a7f8f5d45d9f8086ef06de17c7af81e6108d8de3c168'),
 'brackets': ('frontier-20261028-level6-226-minor-root-brackets-v1.json','5c7de0bf6f4bcf635e0743500d81a7b3ccd2468e80a7202cad32ce832df2aa95')}
data={}
for key,(name,sha) in N.items():
    raw=(E/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha, name
    data[key]=json.loads(raw)

# A literal associative tensor algebra model of the free Lie algebra.
# The ordered alphabet is the eight explicit matrix units in the named
# fixed-Levi import, with two distinct zero-weight letters.
wt=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))
def words_at(n,a,b):
    return [w for w in itertools.product(range(8),repeat=n)
            if sum(wt[i][0] for i in w)==a and sum(wt[i][1] for i in w)==b]
def lyndon(w): return bool(w) and all(w<w[k:] for k in range(1,len(w)))
def bracket(a,b):
    d=defaultdict(Q)
    for u,x in a.items():
        for v,y in b.items():
            d[u+v]+=x*y;d[v+u]-=x*y
    return {k:v for k,v in d.items() if v}
@lru_cache(None)
def lie(w):
    if len(w)==1:return {w:Q(1)}
    k=min(range(1,len(w)),key=lambda i:w[i:])
    assert lyndon(w) and lyndon(w[:k]) and lyndon(w[k:])
    return bracket(lie(w[:k]),lie(w[k:]))
def add(dst,src,c=1):
    for k,v in src.items():dst[k]+=c*v
def tidy(d):return {k:v for k,v in d.items() if v}
def rank(vectors):
    pivots={}
    for v in vectors:
        r=tidy(dict(v))
        while r:
            k=min(r)
            if k not in pivots:
                lead=r[k];pivots[k]={j:x/lead for j,x in r.items()};break
            c=r[k]
            for j,x in pivots[k].items():r[j]=r.get(j,Q(0))-c*x
            r=tidy(r)
    return len(pivots)

# Independently calculate sl3 action by 3x3 matrix multiplication,
# then re-express it in the explicit adjoint basis.
def unit(i,j):return tuple(tuple(Q(int((i,j)==(a,b))) for b in range(3)) for a in range(3))
def linear(*parts):return tuple(tuple(sum(c*M[i][j] for c,M in parts) for j in range(3)) for i in range(3))
def mul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def comm(A,B):return linear((1,mul(A,B)),(-1,mul(B,A)))
basis=(unit(2,0),linear((-1,unit(2,1))),unit(1,0),linear((1,unit(0,0)),(-1,unit(2,2))),linear((1,unit(0,0)),(-1,unit(1,1))),linear((-1,unit(0,1))),linear((-1,unit(1,2))),linear((-2,unit(0,2))))
ops={'f1':unit(1,0),'f2':unit(2,1),'e1':unit(0,1),'e2':unit(1,2),'e12':unit(0,2)}
def coords(M):
    c=(M[2][0],-M[2][1],M[1][0],-M[2][2],-M[1][1],-M[0][1],-M[1][2],-M[0][2]/2)
    assert linear(*[(x,y) for x,y in zip(c,basis)])==M
    return {i:x for i,x in enumerate(c) if x}
acts={g:tuple(coords(comm(A,m)) for m in basis) for g,A in ops.items()}
def apply(v,acts_by_letter):
    out=defaultdict(Q)
    for w,c in v.items():
        for pos,j in enumerate(w):
            for k,a in acts_by_letter[j].items():out[w[:pos]+(k,)+w[pos+1:]]+=c*a
    return tidy(out)
def lower3(v,r,s):
    # Commute [f3,m_j] to the right in U(F(M) semidirect Levi),
    # retaining every action on a suffix letter. Primitive input must have
    # zero residual degree-zero terms after normal-ordering.
    local=({'h3':-1},{'e1':-r},{'e2':-s},{'e12':-r-s},{'e12':-s},{},{},{})
    diag=tuple(({j:Q(2-r*a-s*b)} if 2-r*a-s*b else {}) for j,(a,b) in enumerate(wt))
    aa=dict(acts);aa['h3']=diag
    out=defaultdict(Q);residual=defaultdict(Q)
    for w,c in v.items():
        for pos,j in enumerate(w):
            for g,z in local[j].items():
                removed=w[:pos]+w[pos+1:]
                residual[(removed,g)]+=c*z
                for k in range(pos+1,len(w)):
                    for letter,a in aa[g][w[k]].items():
                        suffix=w[pos+1:k]+(letter,)+w[k+1:]
                        out[w[:pos]+suffix]+=c*z*a
    assert not tidy(residual), 'degree-zero term failed to cancel'
    return tidy(out)

P=data['pencil']; source_words=[w for w in words_at(6,2,2) if lyndon(w)]
assert len(source_words)==74
assert [''.join(map(str,w)) for w in source_words]==P['source_words']
bases=[lie(w) for w in source_words]
assert all(v.get(w)==1 and min(v)==w for w,v in zip(source_words,bases))
horizontal=[]
for v in bases:
    h={}
    for i,g in enumerate(('f1','f2')):
        h.update({(i,w):c for w,c in apply(v,acts[g]).items()})
    horizontal.append(h)
assert rank(horizontal)==40
coefs=[{int(k):Q(v) for k,v in d.items()} for d in P['horizontal_kernel_coefficients']]
assert len(coefs)==34 and rank(coefs)==34
vectors=[]
for row in coefs:
    v=defaultdict(Q);h=defaultdict(Q)
    for j,c in row.items():add(v,bases[j],c);add(h,horizontal[j],c)
    assert not tidy(h)
    vectors.append(tidy(v))
assert len(vectors)==74-rank(horizontal)==34
target_words=words_at(5,2,2)
assert len(target_words)==235
actual_cols=[]
for v in vectors:
    base=lower3(v,6,6);rx=lower3(v,7,6);sy=lower3(v,6,7)
    actual_cols.append((base,{w:rx.get(w,0)-base.get(w,0) for w in target_words},
                        {w:sy.get(w,0)-base.get(w,0) for w in target_words}))
selected=[tuple(map(int,w)) for w in P['selected_target_words']]
assert len(selected)==len(set(selected))==34
assert all(w in target_words for w in selected)
for i,w in enumerate(selected):
    for j in range(34):
        assert tuple(Q(c) for c in P['matrix'][i][j])==tuple(d.get(w,0) for d in actual_cols[j]),(i,j)
print('PASS source 74; horizontal rank 40; 34 complete lowest vectors; all 3468 selected pencil scalars; 235 target words',flush=True)

# Form Hx, Hy only through quadratic dot products; compare both provided
# negative vectors and an independently selected positive vector e_0.
def dotquad(v,axis):
    return 2*sum(sum(c*actual_cols[j][0].get(w,0) for j,c in enumerate(v))*
                 sum(c*actual_cols[j][axis].get(w,0) for j,c in enumerate(v))
                 for w in target_words)
e0=[Q(1)]+[Q(0)]*33
pos=[dotquad(e0,1),dotquad(e0,2)]
assert pos==[32578,32578]
neg=[]
for idx,item in enumerate(data['witness']['witnesses'],1):
    v=list(map(Q,item['vector'])); assert len(v)==34
    value=dotquad(v,idx)
    assert value==Q(item['quadratic_value']) and value<0
    neg.append(str(value))
print('PASS both full-target slope forms have positive and negative vectors',flush=True)

# Independent dense integer Bareiss determinant. Row denominators are cleared
# once for the entire pencil, so both determinant and evaluated polynomial
# are compared as integers on the triangular unisolvent grid.
def det(A):
    n=len(A); A=[r[:] for r in A];sgn=1;prev=1
    for k in range(n-1):
        if A[k][k]==0:
            row=next((i for i in range(k+1,n) if A[i][k]),None)
            if row is None:return 0
            A[k],A[row]=A[row],A[k];sgn=-sgn
        p=A[k][k]
        for i in range(k+1,n):
            q=A[i][k]
            for j in range(k+1,n):
                num=A[i][j]*p-q*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=p
    return sgn*A[-1][-1] if n else 1
coef={}
for term in data['poly']['determinant_coefficients']:
    k=(term['x_power'],term['y_power']);c=Q(term['coefficient'])
    assert k not in coef and c and sum(k)<=34
    coef[k]=c
assert len(coef)==592 and sum(c>0 for c in coef.values())==133 and sum(c<0 for c in coef.values())==459
scales=[math.lcm(*(Q(q).denominator for cell in row for q in cell)) for row in P['matrix']]
M=[[[int(Q(q)*scales[i]) for q in cell] for cell in row] for i,row in enumerate(P['matrix'])]
scale=math.prod(scales)
assert all((c*scale).denominator==1 for c in coef.values())
scaled={k:int(v*scale) for k,v in coef.items()}
def peval(x,y):return sum(c*x**i*y**j for (i,j),c in coef.items())
grid=0
for y in range(35):
    for x in range(35-y):
        A=[[a+b*x+c*y for a,b,c in row] for row in M]
        got=det(A); want=sum(c*x**i*y**j for (i,j),c in scaled.items())
        assert got==want,(x,y)
        grid+=1
assert grid==630
print('PASS exact integer Bareiss determinant agrees with P at all 630 triangular grid points',flush=True)

# Expand x=v,y=v+g, then independently substitute g=41z/(1+z).
f=[defaultdict(Q) for _ in range(35)]
for (a,b),c in coef.items():
    for k in range(b+1): f[a+b-k][k]+=c*math.comb(b,k)
count=0; degs=[]
for j,fj0 in enumerate(f):
    fj=tidy(fj0); assert fj
    m=max(fj);degs.append(m)
    q=[sum(c*41**k*math.comb(m-k,h-k) for k,c in fj.items() if k<=h)
       for h in range(m+1)]
    stored=data['sign']['functions'][j]
    assert stored['x_power']==j and stored['gap_degree']==m
    assert q==list(map(Q,stored['transformed_coefficients']))
    assert all(c<0 for c in q)
    count+=len(q)
assert count==620
assert coef[(0,0)]==Q('-603138104964912067285615430860800000000000000')
assert max(i for (i,j) in coef if j==0)==27 and coef[(27,0)]==4217288785920000000
assert max(j for (i,j) in coef if i==0)==30 and coef[(0,30)]==2071650631680000
print('PASS exactly 620/620 strictly negative transformed coefficients in 35 polynomials',flush=True)

endpoints={(11,0):peval(11,0),(Q(23,2),0):peval(Q(23,2),0),
           (0,41):peval(0,41),(0,Q(83,2)):peval(0,Q(83,2))}
assert endpoints[(11,0)]<0<endpoints[(Q(23,2),0)]
assert endpoints[(0,41)]<0<endpoints[(0,Q(83,2))]
shift=[sum(c*math.comb(j,k)*42**(j-k) for (i,j),c in coef.items() if i==0 and j>=k) for k in range(31)]
assert all(q>0 for q in shift)
assert shift==list(map(Q,data['wide']['shifted_P_0_42_plus_h_coefficients']))
leading=f[34][0]
assert tidy(f[34])=={0:Q(-1454389021504438272000)}
assert leading==Q(data['wide']['v34_coefficient_of_P_v_vplusg'])
print('PASS four endpoint signs, all 31 shifted-axis coefficients, and v^34 leading coefficient',flush=True)
receipt={
 'clock_before_receipt_creation':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip(),
 'input_hashes':{k:v[1] for k,v in N.items()},
 'source_words':74,'horizontal_rank':40,'lowest_vectors':34,'target_tensor_words':235,
 'actual_selected_pencil_scalar_entries_verified':3468,'right_degree_zero_terms_cancelled':True,
 'polynomial_grid':'630 integer fraction-free Bareiss determinants; row-denominator scaling; x+y<=34',
 'polynomial_terms':592,'positive_terms':133,'negative_terms':459,
 'gap_upper':41,'coefficient_functions':35,'gap_degrees':degs,'negative_transformed_coefficients':count,
 'accretivity_positive_quadratic_values':[str(v) for v in pos],
 'accretivity_negative_quadratic_values':neg,
 'endpoint_values':{str(k):str(v) for k,v in endpoints.items()},
 'shifted_axis_coefficients_strictly_positive':len(shift),
 'v34_leading_coefficient':str(leading),
 'limitations':'conditional on named free-Levi/PBW/ideal descent and node-exchange imports; no original global map/novelty claim'}
with (R/'independent-226-receipt-v1.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print('PASS review receipt written exclusively',flush=True)
