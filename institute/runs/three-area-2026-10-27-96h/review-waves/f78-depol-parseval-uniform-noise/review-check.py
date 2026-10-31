#!/usr/bin/env python3
"""Independent exact review: no imports of author code or replay files."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, combinations, permutations
from collections import Counter
import json

Z=F(0); ONE=F(1)
def form(q):
    a,b=(1+q)/2,(1-q)/2
    @lru_cache(None)
    def e(x,y,i,j):
        v=ONE
        for bit in (1,2,4,8):
            X,Y,I,J=bool(x&bit),bool(y&bit),bool(i&bit),bool(j&bit)
            if X==Y:
                if I!=J: return Z
                v*=a if I==X else b
            else:
                if I!=X or J!=Y: return Z
                v*=q
        return v
    return a,b,e

def hessian_check():
    B=[x for x in range(16) if x.bit_count()>=2]
    lead=[(0,0)]+[(1<<i,1<<j) for i in range(4) for j in range(4)]
    count=0
    for n in range(1,23):
        t=F(n,24); a,b,E=form(t); D=1-a*b; D4=a*a+b*b
        lam=lambda h:a**(4-h)*b**h
        gaps={(h,k):lam(h)-lam(k.bit_count()) for h in (0,1) for k in B}
        u=t*(1-t*t)
        for x in B:
            for y in B:
                hx,hy=x.bit_count(),y.bit_count()
                for oi,oj in lead:
                    typ=0 if oi==0 else 1
                    val=E(x,y,oi,oj)-(E(0,0,oi,oj) if x==y else 0)
                    for k in B:
                        num=E(x,0,oi,k)*E(0,y,k,oj)+E(0,y,oi,k)*E(x,0,k,oj)
                        if num: val+=num/gaps[(typ,k)]
                    expected=Z
                    if hx==hy:
                        if typ==0:
                            if x==y:
                                expected={2:-a*a*u,3:-a*t*D+a*t**5/D,4:-t*D4+t**7/D4}[hx]
                        else:
                            i,j=oi.bit_length()-1,oj.bit_length()-1
                            if hx==2:
                                if i==j and x==y:
                                    expected=-a*b*u*(1-int(bool(x&(1<<i))))
                                elif i!=j and (x&(1<<i)) and (y&(1<<j)) and (x^(1<<i))==(y^(1<<j)):
                                    expected=a*b*t*t*(1+t)
                            elif hx==3:
                                if i==j and x==y:
                                    expected-=a*a*b*t
                                    if x==(15^(1<<i)): expected-=b*b*t*(1+t)
                                if x==(15^(1<<j)) and y==(15^(1<<i)):
                                    expected+=t*t*b*b+t**5*b/D
                            else:
                                if i==j and x==y: expected=-a*b*t
                    if val!=expected:
                        raise AssertionError(('hessian',str(t),x,y,oi,oj,str(val),str(expected)))
                    count+=1
    return {'t_points':22,'bilinear_coefficient_comparisons':count,
            't_grid':'n/24, n=1,...,22',
            'identity_argument':'Clear product of the three reference gaps and (1-ab)(a^2+b^2); degree <=21. Twenty-two exact zeros imply identity. Excitation-number covariance rules out c*c and conjugate(c)*conjugate(c) terms.'}

def constants():
    V,W,S1,g=F(1,4),F(23),F(1,6),F(3,2)
    Q=W+2*V*S1+12*S1*S1
    first=6*(2*S1)**3*F(2,6)+V*(2*S1)**2+W*(2*S1)*2+29
    second=6*32**2/F(500)+2*V*32+2*24*32/F(500)+45
    assert 512*F(1,100)**2<F(1,16) and 512<23**2
    assert Q==F(281,12) and first==F(4799,108) and second==F(1909,25)
    assert 3*77*F(1,500)<F(15,32)
    assert F(2,250001)>F(1,250000)>20*F(1,10**7)
    d=F(1,10); gap=2*d; s1=1020/d
    q0=510+1020*s1+32*s1*s1; s2=2*q0/d
    e0=min(ONE,1/(4*s1),1/(4*s2),gap/8160,gap/(8*q0))
    C1=16*(2*s1)**3*F(2,6)+510*(2*s1)**2+1020*(2*s1)+1020
    C2=16*(2*s2)**2*e0+1020*(2*s2)+2*q0*(2*s2)*e0+C1
    rad=min(e0,d/(6*C2))
    assert e0==F(1,267174760800) and rad==F(1,10969298228683800)
    assert 2*e0*s1<=F(1,2) and 2*e0*e0*s2<=F(1,2)
    assert 2040*e0<=gap/4 and 510*e0+q0*e0*e0<gap/4 and 3*C2*rad<=d/2
    return {'V_F_squared_upper':str(512*F(1,100)**2),'W_F_squared_upper':'512',
            'Q_F_upper':str(Q),'first_remainder':str(first),'second_remainder':str(second),
            'radius_1_over_500_hessian_remainder_slack':str(F(15,32)-3*77*F(1,500)),
            'tube_delta':str(d),'tube_s1':str(s1),'tube_q0':str(q0),'tube_s2':str(s2),
            'tube_e0':str(e0),'tube_C1':str(C1),'tube_C2':str(C2),'tube_radius':str(rad)}

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def scale(x,s):return (x[0]*s,x[1]*s)
def G(x,y=0):return (F(x),F(y))
G0=G(0)

def tensor_output(q,v):
    _,_,E=form(q); N=sum((abs(c[0])**2+abs(c[1])**2 for c in v.values()),Z)
    return [[scale(sumg(scale(mul(cx,conj(cy)),E(x,y,i,j)) for x,cx in v.items() for y,cy in v.items()),1/N) for j in range(16)] for i in range(16)]
def sumg(xs):
    acc=G0
    for x in xs:acc=add(acc,x)
    return acc

def pauli_output(q,v):
    N=sum((abs(c[0])**2+abs(c[1])**2 for c in v.values()),Z)
    ret=[[G0 for _ in range(16)] for _ in range(16)]
    for ops in product(range(4),repeat=4):
        prob=ONE
        for op in ops:prob*=((1+3*q)/4 if op==0 else (1-q)/4)
        trans={}
        for x,c in v.items():
            dest=x; phase=G(1)
            for n,op in enumerate(ops):
                b=(x>>n)&1
                if op==1:dest^=1<<n
                elif op==2:
                    dest^=1<<n; phase=mul(phase,G(0,1-2*b))
                elif op==3:phase=scale(phase,1-2*b)
            trans[dest]=mul(phase,c)
        for i,vi in trans.items():
            for j,vj in trans.items():
                ret[i][j]=add(ret[i][j],scale(mul(vi,conj(vj)),prob/N))
    return ret

def inertia_ldl(M):
    n=len(M); L=[[G0 for _ in range(n)] for _ in range(n)]; D=[]
    for k in range(n):
        diag=M[k][k]
        for s in range(k):diag=sub(diag,scale(mul(L[k][s],conj(L[k][s])),D[s]))
        assert diag[1]==0 and diag[0]!=0,('zero or complex pivot',k,diag)
        D.append(diag[0]); L[k][k]=G(1)
        for i in range(k+1,n):
            v=M[i][k]
            for s in range(k):v=sub(v,scale(mul(L[i][s],conj(L[k][s])),D[s]))
            L[i][k]=scale(v,1/D[k])
    return (sum(d>0 for d in D),sum(d<0 for d in D),sum(d==0 for d in D))

def shift(M,u):
    return [[sub(G(u if i==j else 0),M[i][j]) for j in range(16)] for i in range(16)]

def endpoint():
    vec={0:G(1500),3:G(1),7:G(0,2),15:G(2)}
    assert sum(abs(c[0])**2+abs(c[1])**2 for c in vec.values())==2250009
    u1=F(390625156249,6250000000000);u2=F(3125000624997,50000000000000)
    rows=[]
    for q in (F(1,10**7),-F(1,10**7)):
        M=tensor_output(q,vec)
        assert M==pauli_output(q,vec)
        assert all(M[i][j]==conj(M[j][i]) for i in range(16) for j in range(16))
        assert sum(M[i][i][0] for i in range(16))==1
        obs=inertia_ldl(M); cap1=inertia_ldl(shift(M,u1));cap2=inertia_ldl(shift(M,u2))
        assert obs==(16,0,0) and cap1==(16,0,0) and cap2==(15,1,0)
        a,b=(1+abs(q))/2,(1-abs(q))/2
        ref=a**4+2*a**3*b; cap=u1+2*u2
        proj=(0,1,2) if q>0 else (15,14,13)
        trace=sum(M[i][i][0] for i in proj)
        assert ref>cap>=trace
        assert cap==F(4687501249993,25000000000000)
        assert ref-cap==F(45399999999999999,160000000000000000000000000000)
        assert trace==F(7500031999996150000066666670861111,40000160000000000000000000000000000)
        rows.append({'q':str(q),'output_inertia':obs,'upper1_inertia':cap1,'upper2_inertia':cap2,
                     'product_reference':str(ref),'top3_upper':str(cap),'gap_lower':str(ref-cap),'projector_trace':str(trace),'pauli_matches_tensor':True})
    return rows

def poly_coeffs(q):
    a,b,E=form(q); L=a**3*b; support=(0,3,5,15); power={0:0,3:1,5:1,15:1}
    def coeff(i,j):
        out=[Z]*3
        for x in support:
            for y in support:out[power[x]+power[y]]+=E(x,y,i,j)
        return out
    return a,b,L,coeff

def pointwise_polynomial():
    for q in (Z,F(1,4),F(1,2),F(3,4),ONE):
        a,b,L,C=poly_coeffs(q)
        expected={(0,0):(a**4,Z,2*a*a*b*b+b**4),
          (2,2):(L,Z,L+2*a*b**3),(4,4):(L,Z,L+2*a*b**3),
          (2,4):(Z,Z,q*q*a*b),(4,2):(Z,Z,q*q*a*b),
          (2,7):(Z,q*q*a*b,Z),(7,2):(Z,q*q*a*b,Z),
          (4,7):(Z,q*q*a*b,Z),(7,4):(Z,q*q*a*b,Z),
          (7,7):(a*b**3,Z,3*L)}
        for ij,want in expected.items():assert tuple(C(*ij))==want
        for ij in ((0,2),(0,4),(0,7),(2,0),(4,0),(7,0)):assert C(*ij)==[Z,Z,Z]
    for n in range(9):
        q=F(n,8);a,b,L,C=poly_coeffs(q); v={2:(ONE,Z),4:(ONE,Z),7:(Z,2*q)}
        ans=[Z]*5
        for i in v:
            for j in v:
                for h in (0,1):
                    for k in range(3):
                        for l in (0,1):ans[h+k+l]+=v[i][h]*C(i,j)[k]*v[j][l]
        ref=[2*L,Z,(6+4*q*q)*L,Z,12*q*q*L]
        diff=[x-y for x,y in zip(ans,ref)]
        assert diff==[Z,Z,2*a*b*q*(2*q*q+q-2),Z,Z]
    return {'channel_entry_interpolation_points':5,'entry_degree_bound':4,
            'w_numerator_interpolation_points':9,'w_q_degree_bound':6,
            'expected_w_numerator_z2':'2*a*b*q*(2*q^2+q-2)'}

def pointwise_examples():
    rows=[]
    for q,z in ((F(4,5),F(1,10)),(F(9,10),F(1,3))):
        a,b,E=form(q);L=a**3*b;N=1+3*z*z
        amp={0:ONE,3:z,5:z,15:z}
        M=[[sum((amp[x]*amp[y]*E(x,y,i,j) for x in amp for y in amp),Z)/N for j in range(16)] for i in range(16)]
        w={2:ONE,4:ONE,7:2*q*z}; norm=sum((u*u for u in w.values()),Z)
        ugap=M[0][0]-L
        wgap=sum((u*v*M[i][j] for i,u in w.items() for j,v in w.items()),Z)/norm-L
        assert all(M[0][i]==0 for i in w)
        assert 2*q*q+q-2>0 and z*z<a**3/(b*(3*a*a+a*b+b*b))
        assert ugap==q*(a**3-b*(3*a*a+a*b+b*b)*z*z)/N
        assert wgap==2*a*b*q*(2*q*q+q-2)*z*z/(N*norm)
        assert ugap>0 and wgap>0
        rows.append({'q':str(q),'z':str(z),'bound_z_squared':str(a**3/(b*(3*a*a+a*b+b*b))),
                     'u_gap':str(ugap),'normalized_w_gap':str(wgap),'lambda_reference':str(L)})
    return rows

def minors():
    out=[]; supp=(0,3,5,15)
    def pack(x,bits):return sum(((x>>bit)&1)<<k for k,bit in enumerate(bits))
    def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    for left in ((0,),(1,),(2,),(3,),(0,1),(0,2),(0,3)):
        right=tuple(i for i in range(4) if i not in left)
        mat={(pack(x,left),pack(x,right)):(0 if x==0 else 1) for x in supp}
        r=2 if len(left)==1 else 3; want=1 if r==2 else 2
        witness=None
        for rr in combinations(range(1<<len(left)),r):
            for cc in combinations(range(1<<len(right)),r):
                poly=Counter()
                for perm in permutations(range(r)):
                    cells=[mat.get((rr[k],cc[perm[k]])) for k in range(r)]
                    if all(x is not None for x in cells):poly[sum(cells)]+=parity(perm)
                poly={k:v for k,v in poly.items() if v}
                if poly in ({want:1},{want:-1}):witness=(rr,cc,poly[want]);break
            if witness:break
        assert witness,('missing nonzero minor',left)
        if r==3:
            assert (len({i for i,j in mat})<4 or len({j for i,j in mat})<4)
        out.append({'left_bits':left,'minor_rows':witness[0],'minor_columns':witness[1],
                    'determinant':'%s*z^%s'%(witness[2],want),'rank_exactly':r})
    return out

result={'hessian':hessian_check(),'constants':constants(),'endpoint':endpoint(),
        'pointwise_polynomial':pointwise_polynomial(),'pointwise_examples':pointwise_examples(),
        'gme_minors':minors()}
print(json.dumps(result,indent=2,sort_keys=True))
