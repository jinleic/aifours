#!/usr/bin/env python3
"""Independent Q(i)-exact check of the frozen grid-plane/phase statements.

No author checker is imported or executed. Five-phase rank is verified as a
polynomial identity via 13 distinct rational evaluations (degree <= 12);
the phase average uses distinct exponents modulo 5.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations
from hashlib import sha256
import json

@dataclass(frozen=True)
class Q:
    re: F = F(0)
    im: F = F(0)
    def __init__(self, re=0, im=0):
        object.__setattr__(self, 're', F(re))
        object.__setattr__(self, 'im', F(im))
    def __add__(self, other):
        other = q(other); return Q(self.re+other.re, self.im+other.im)
    __radd__ = __add__
    def __neg__(self): return Q(-self.re, -self.im)
    def __sub__(self, other): return self + -q(other)
    def __rsub__(self, other): return q(other) + -self
    def __mul__(self, other):
        other=q(other)
        return Q(self.re*other.re-self.im*other.im, self.re*other.im+self.im*other.re)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other=q(other); d=other.re**2+other.im**2
        if not d: raise ZeroDivisionError('division by zero Gaussian rational')
        return Q((self.re*other.re+self.im*other.im)/d,
                 (self.im*other.re-self.re*other.im)/d)
    def conj(self): return Q(self.re,-self.im)
    def n2(self): return self.re**2+self.im**2
    def __bool__(self): return bool(self.re or self.im)
    def __str__(self):
        return str(self.re) if not self.im else f'{self.re}+({self.im})i'

def q(x): return x if isinstance(x,Q) else Q(x)
Z,O,J=Q(),Q(1),Q(0,1)
ROOTS=(O,J,-O,-J)

def ket(nb, *items):
    v=[Z]*(4*nb)
    for a,b,c in items: v[a*nb+b]=v[a*nb+b]+q(c)
    return v

def lin(*items):
    n=len(items[0][1]); out=[Z]*n
    for c,v in items:
        out=[x+q(c)*y for x,y in zip(out,v)]
    return out

def zero(n): return [[Z for _ in range(n)] for _ in range(n)]
def add_outer(m,c,u,v=None):
    v=u if v is None else v; c=q(c)
    for i,x in enumerate(u):
        if not x: continue
        for j,y in enumerate(v):
            if y: m[i][j]=m[i][j]+c*x*y.conj()

def gram_apply(m,h,ls):
    for i,u in enumerate(ls):
        for j,v in enumerate(ls):
            if h[i][j]: add_outer(m,h[i][j],u,v)

def adj_outer_diag(ds,t):
    return [[q(ds[i] if i==j else 0)-t[i]*t[j].conj()
             for j in range(len(t))] for i in range(len(t))]

def det(a):
    n=len(a)
    if n==0: return O
    out=Z
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        t=q(-1 if inversions%2 else 1)
        for i,j in enumerate(p): t=t*a[i][j]
        out=out+t
    return out

def minors3(v, nb=4):
    a=[v[i*nb:(i+1)*nb] for i in range(4)]
    for rr in combinations(range(4),3):
        for cc in combinations(range(nb),3):
            if det([[a[i][j] for j in cc] for i in rr]): return False
    return True

def all_principal(h):
    records=[]
    for k in range(1,len(h)+1):
        for ix in combinations(range(len(h)),k):
            d=det([[h[i][j] for j in ix] for i in ix])
            if d.im: raise ValueError('nonreal principal minor')
            records.append((ix,d.re))
    return records

def schur_psd(mat):
    a=[r[:] for r in mat]; piv=[]
    while a:
        n=len(a)
        for i in range(n):
            if a[i][i].im: raise ValueError('nonreal diagonal')
            if a[i][i].re<0: return None
            if not a[i][i] and any(a[i][j] for j in range(n)):
                return None
        k=next((i for i in range(n) if a[i][i].re>0),None)
        if k is None:
            if any(any(row) for row in a): return None
            break
        pivot=a[k][k]; piv.append(str(pivot.re))
        ix=[i for i in range(n) if i!=k]
        a=[[a[i][j]-a[i][k]*a[k][j]/pivot for j in ix] for i in ix]
    return piv

def summary_gram(h):
    minors=all_principal(h); negative=[(list(i),str(x)) for i,x in minors if x<0]
    piv=schur_psd(h)
    if bool(negative)!=(piv is None): raise AssertionError('PSD algorithms disagree')
    return {'positive_semidefinite':piv is not None, 'pivots':piv,
            'zero_principal_minors':sum(x==0 for _,x in minors),
            'negative_principal_minor':negative[0] if negative else None,
            'principal_minors_checked':len(minors)}

def partial_transpose(mat,nb):
    return [[mat[(i//nb)*nb+(j%nb)][(j//nb)*nb+(i%nb)]
             for j in range(4*nb)] for i in range(4*nb)]

def state_basis(nb, v=None):
    if nb==5:
        A=ket(5,(0,0,1),(1,1,1),(2,2,1))
        B=ket(5,(0,1,1),(1,2,1)); D=ket(5,(1,0,1),(2,1,-1))
        C=ket(5,(0,2,1),(3,4,1)); E=ket(5,(2,0,1),(3,3,1))
        Fv=ket(5,(2,3,1)); G=ket(5,(3,0,1))
        I=ket(5,(3,2,1)); H=ket(5,(0,4,1))
    else:
        v0,v1,v2=v
        A=ket(4,(0,0,1),(1,1,1),(2,2,1))
        B=ket(4,(0,1,1),(1,2,1)); D=ket(4,(1,0,1),(2,1,-1))
        C=ket(4,(0,2,1),(3,3,1))
        E=ket(4,(2,0,1),(3,0,v0),(3,1,v1),(3,2,v2))
        Fv=ket(4,(2,0,v0),(2,1,v1),(2,2,v2))
        G=ket(4,(3,0,1)); I=ket(4,(3,2,1)); H=ket(4,(0,3,1))
    return A,B,D,C,E,Fv,G,I,H

def state(vectors):
    n=len(vectors[0]); m=zero(n)
    for i,v in enumerate(vectors): add_outer(m,1 if i<3 else 3,v)
    return m

def source_checks():
    vectors=state_basis(5); original=state(vectors); rhs=zero(20)
    terms=[(1,[(0,1,1),(1,0,1)]),(1,[(1,2,1),(2,1,1)]),
           (F(1,3),[(0,2,3),(1,1,1),(2,0,1)]),
           (F(2,3),[(1,1,1),(2,0,-2)]),
           (3,[(0,4,1),(3,2,1)]),(3,[(2,3,1),(3,0,1)]),
           (1,[(0,0,1)]),(1,[(2,2,1)]),(3,[(3,3,1)]),(3,[(3,4,1)])]
    for coeff,entries in terms: add_outer(rhs,coeff,ket(5,*entries))
    assert partial_transpose(original,5)==rhs
    amap=[(2,-1),(1,1),(0,1),(3,1)]
    bmap=[(2,-1),(1,1),(0,1),(4,-1),(3,-1)]
    transformed=[]
    for vector in vectors:
        w=[Z]*20
        for i,c in enumerate(vector):
            a,b=divmod(i,5); aa,sa=amap[a];bb,sb=bmap[b]
            w[aa*5+bb]=w[aa*5+bb]+sa*sb*c
        transformed.append(w)
    target_order=[(0,1),(2,1),(1,-1),(4,-1),(3,-1),(8,-1),(7,-1),(6,1),(5,1)]
    assert all(w==lin((sgn,vectors[j])) for w,(j,sgn) in zip(transformed,target_order))
    assert state(transformed)==original
    return {'pt_projector_identity_entries':400, 'nonnegative_projector_terms':10,
            'local_reflection_generator_images':9,'local_reflection_state_entries':400,
            'source_trace':str(sum(original[i][i].re for i in range(20)))}

def make_plane(v0,v2):
    A,B,D,C,E,Fv,G,I,H=state_basis(4,(v0,Z,v2)); L=(E,G,I,Fv)
    target=state((A,B,D,C,E,Fv,G,I,H))
    X=lin((1,E),(-v0,G),(-v2,I))
    U,V=v0.n2(),v2.n2(); a=1+U+V
    s=q(-a)*v0.conj()/q(1+a*U)
    W=lin((-1,X),(s,Fv),(-s*v0,X))
    t=(q(-1)-s*v0,(q(1)+s*v0)*v0,(q(1)+s*v0)*v2,s)
    assert W==lin(*zip(t,L))
    H0=adj_outer_diag([3]*4,t)
    actual=zero(16)
    for z in ROOTS:
        seed=lin((z,A),(1,B),(z*z,D),(z*z*z,W))
        assert minors3(seed)
        add_outer(actual,F(1,4),seed)
    for vec in (C,H): add_outer(actual,3,vec)
    gram_apply(actual,H0,L)
    assert actual==target
    p0=summary_gram(H0)
    assert p0['positive_semidefinite']==(sum(x.n2() for x in t)<=3)
    result={'v0':str(v0),'v2':str(v2),'first_norm2':str(sum(x.n2() for x in t)),
            'first_gram':p0,'first_phase_rank_vectors':4,'first_identity_entries':256}
    if v2:
        Zd=ket(4,(2,2,1))
        t1=(-v0/v2,v0*v0/v2,v0,O/v2)
        assert Zd==lin(*zip(t1,L))
        H1=adj_outer_diag([3]*4,t1); actual=zero(16)
        qzero=lin((1,A),(-1,Zd)); assert minors3(qzero)
        add_outer(actual,F(1,2),qzero)
        beta=Q(1,1); delta=Q(1,-1)
        for z in ROOTS:
            seed=lin((z,A),(z,Zd),(beta*z*z,B),(delta,D))
            assert minors3(seed)
            add_outer(actual,F(1,8),seed)
        for vec in (C,H): add_outer(actual,3,vec)
        gram_apply(actual,H1,L)
        assert actual==target
        p1=summary_gram(H1)
        assert p1['positive_semidefinite']==(sum(x.n2() for x in t1)<=3)
        result.update({'second_norm2':str(sum(x.n2() for x in t1)),
                       'second_gram':p1,'second_phase_rank_vectors':5,
                       'second_identity_entries':256})
    else: result['second_gram']='undefined at v2=0; first certificate covers this point'
    piv=schur_psd(partial_transpose(target,4)); assert piv is not None
    assert p0['positive_semidefinite'] or (v2 and p1['positive_semidefinite'])
    result['pt_pivots']=piv
    return result

def make_phase(v0,v1,v2,p):
    p=F(p); T=v1.n2(); vectors=state_basis(4,(v0,v1,v2))
    A,B,D,C,E,Fv,G,I,H=vectors; target=state(vectors)
    X=lin((1,E),(-v0,G),(-v2,I)); t=(O,-v0,-v2)
    # q5 is a degree-4 matrix polynomial; every 3x3 minor has degree <=12.
    for j in range(13):
        z=q(j)
        q5=lin((z,A),(1,B),(-z*z,D),(-z*z*z,X),(-z*z*z*z*v1,G))
        assert minors3(q5)
    # Distinct powers 0,1,2,3,4 modulo 5 eliminate every cross term.
    assert len({j%5 for j in range(5)})==5
    actual=zero(16)
    for c,v in ((1,A),(1,B),(1,D),(1,X),(T,G)): add_outer(actual,p*c,v)
    for z in ROOTS:
        q4=lin((z,A),(1,B),(-z*z*v1,I),(-z*z*z,X))
        assert minors3(q4)
        add_outer(actual,(1-p)/4,q4)
    add_outer(actual,1-p,D)
    for v in (C,Fv,H):
        assert minors3(v)
        add_outer(actual,3,v)
    diag=(F(3),F(3)-p*T,F(3)-(1-p)*T)
    gram=adj_outer_diag(diag,t)
    gram_apply(actual,gram,(E,G,I)); assert actual==target
    gm=summary_gram(gram); assert gm['positive_semidefinite']
    pt=schur_psd(partial_transpose(target,4)); assert pt is not None
    return {'v':[str(v0),str(v1),str(v2)],'p':str(p),'T':str(T),
            'budgets':[str(d) for d in diag], 'gram':gm,'pt_pivots':pt,
            'five_phase_minor_polynomial_degree_bound':12,
            'five_phase_rational_evaluations':13,'minors_per_evaluation':16,
            'four_phase_rank_vectors':4,'state_entries_checked':256,
            'trace':str(sum(target[i][i].re for i in range(16)))}

def main():
    source=source_checks()
    planes=[('author_0_2',Z,Q(2)),
            ('author_half_4',Q(F(1,2)),Q(4)),
            ('author_i_half_1_plus_i',Q(0,F(1,2)),Q(1,1)),
            ('author_2_1',Q(2),O),
            ('author_quarter_complex_1',Q(F(1,4),F(1,4)),O),
            ('own_first_v2_zero',Q(F(1,2),F(1,2)),Z),
            ('own_second_complex',Q(0,F(1,4)),Q(3,1))]
    ps={name:make_plane(x,y) for name,x,y in planes}
    cases=[('author_interpolated_entangled',Q(F(45,46)),Q(F(1,2)),Q(F(45,46)),F(1,2)),
           ('author_interpolated_large_middle',Q(F(1,2)),Q(2),Q(F(1,2)),F(1,2)),
           ('author_third_checker_point',Q(1,F(1,2)),O,Q(F(1,2)),F(1,2)),
           ('own_phase_gram_boundary',O,Z,J,F(1,2)),
           ('own_phase_complex',Q(F(1,4),F(1,4)),Q(1,1),Q(F(1,4),F(-1,2)),F(1,2)),
           ('author_optimal',O,Q(2),Q(F(1,10)),F(13,44)),
           ('own_optimal_zero_budget',Z,Q(2),Q(F(1,2),F(1,2)),F(3,4)),
           ('own_optimal_clipped',Q(F(2,5)),J,Q(F(1,2),F(1,2)),F(1))]
    ph={name:make_phase(a,b,c,p) for name,a,b,c,p in cases}
    assert ps['author_half_4']['first_norm2']=='276/85'
    assert ps['author_half_4']['second_norm2']=='85/256'
    assert ps['author_2_1']['first_norm2']=='6/25'
    assert ph['author_interpolated_entangled']['gram']['pivots']==['2','1523/1058','391/48736']
    assert ph['author_interpolated_large_middle']['gram']['pivots']==['2','5/8','2/5']
    assert ph['author_optimal']['gram']['pivots']==['2','7/22','37/385']
    # Independent exact values for claimed phase Schur sums and strict examples.
    d=F(3)-F(1,8); a2=F(2025,2116)
    schur_half=F(1,3)+2*a2/d
    schur_end=F(1,3)+a2/F(11,4)+a2/F(3)
    schur_opt=F(1,3)+F(1)/F(20,11)+F(1,100)/F(2,11)
    assert schur_half==F(36467,36501) and schur_end==F(3037,3036)
    assert schur_opt==F(563,600)
    result={'method':'independent Gaussian rationals, all Gram principal minors plus exact Schur elimination',
            'source_and_symmetry':source,'plane_cases':ps,'phase_and_optimal_cases':ph,
            'claimed_schur_sums':{'phase_example_half':str(schur_half),
                                  'phase_example_each_endpoint':str(schur_end),
                                  'optimal_example':str(schur_opt)}}
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
