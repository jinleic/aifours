#!/usr/bin/env python3
"""Independent F155 controls. No author code/imports. Python stdlib+numpy only.
Exact arithmetic: Gaussian rationals and Hermitian congruence inertia (1x1/2x2).
Floating eigenvalues only propose dyadic brackets; exact inertia certifies them.
Finite instances supplement, never replace, the separately reconstructed proof.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, math, random, sys, traceback
from datetime import datetime
from itertools import combinations, product
import numpy as np

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'reviewer-exact-controls-v1.result.json'
LOG = {'kind':'INDEPENDENT_BOUNDED_EXACT_MATHEMATICAL_CONTROLS',
       'started_native':datetime.now().astimezone().isoformat(),
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'python':sys.version, 'numpy':np.__version__, 'seed':15520261028,
       'author_code_imported_or_executed':False, 'checks':[], 'negative_controls':[]}
rng = random.Random(LOG['seed'])

class G:
    __slots__=('r','i')
    def __init__(self,r=0,i=0):
        if isinstance(r,G): self.r,self.i=r.r,r.i
        else: self.r,self.i=F(r),F(i)
    def __add__(self,o):
        o=G(o); return G(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return G(-self.r,-self.i)
    def __sub__(self,o): return self+-G(o)
    def __rsub__(self,o): return G(o)+-self
    def __mul__(self,o):
        o=G(o); return G(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=G(o); d=o.r*o.r+o.i*o.i
        return G((self.r*o.r+self.i*o.i)/d,(self.i*o.r-self.r*o.i)/d)
    def __rtruediv__(self,o): return G(o)/self
    def conj(self): return G(self.r,-self.i)
    def abs2(self): return self.r*self.r+self.i*self.i
    def __eq__(self,o):
        o=G(o); return self.r==o.r and self.i==o.i
    def __bool__(self): return bool(self.r or self.i)
    def __complex__(self): return complex(float(self.r),float(self.i))
    def __repr__(self): return str(self.r) if not self.i else f'({self.r}+({self.i})j)'

def Z(n=16,m=None): return [[G() for j in range(m or n)] for i in range(n)]
def eye(n=16): return [[G(i==j) for j in range(n)] for i in range(n)]
def diag(v): return [[G(v[i] if i==j else 0) for j in range(len(v))] for i in range(len(v))]
def add(A,B): return [[a+b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def scale(A,c): return [[a*c for a in ar] for ar in A]
def sub(A,B): return add(A,scale(B,-1))
def mm(A,B):
    out=Z(len(A),len(B[0]))
    for i,ar in enumerate(A):
        for k,a in enumerate(ar):
            if a:
                for j,b in enumerate(B[k]):
                    if b: out[i][j]=out[i][j]+a*b
    return out

def adj(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def trans(A): return [list(a) for a in zip(*A)]
def tr(A): return sum((A[i][i] for i in range(len(A))),G())
def real(x):
    x=G(x); assert x.i==0; return x.r

def outer(v,w=None):
    if w is None: w=v
    return [[G(a)*G(b).conj() for b in w] for a in v]
def norm2(v): return sum(G(a).abs2() for a in v)
def density(v): return scale(outer(v),1/norm2(v))
def bits(x,i): return (x>>(3-i))&1
def flip(x,i): return x^(1<<(3-i))
def wt(x): return x.bit_count()
def block(A,ii,jj=None):
    if jj is None: jj=ii
    return [[A[i][j] for j in jj] for i in ii]
def shift(A,c): return sub(A,scale(eye(len(A)),c))
def frob2(A): return sum(a.abs2() for ar in A for a in ar)
def comm(A,B): return sub(mm(A,B),mm(B,A))
def floats(A): return np.array([[complex(a) for a in ar] for ar in A])

# Local Pauli monomial action, independently from channel implementation.
def pauli(v,word):
    out=[G() for _ in range(16)]
    for x,a in enumerate(v):
        y=x; phase=G(1)
        for i,p in enumerate(word):
            if p==1: y=flip(y,i)
            elif p==2:
                y=flip(y,i); phase=phase*G(0,1 if bits(x,i)==0 else -1)
            elif p==3: phase=phase*(-1 if bits(x,i) else 1)
        out[y]=G(a)*phase
    return out

def pauli_matrix(word):
    cols=[]
    for k in range(16):
        e=[G(x==k) for x in range(16)]; cols.append(pauli(e,word))
    return trans(cols)
PAULIS=[pauli_matrix(tuple(p if j==i else 0 for j in range(4))) for i in range(4) for p in (1,2,3)]
Y4=pauli_matrix((2,2,2,2))

def frame(A):
    out=Z()
    for P in PAULIS: out=add(out,mm(mm(P,A),P))
    return out

def spin(A): return mm(mm(Y4,trans(A)),Y4)
def erase(A,i):
    out=Z(); mask=1<<(3-i)
    for x in range(16):
        for y in range(16):
            if bits(x,i)==bits(y,i):
                u=x&~mask; v=y&~mask
                out[x][y]=(A[u][v]+A[u|mask][v|mask])/2
    return out

def layers(A):
    out=[]
    for k in range(5):
        B=Z()
        for ss in combinations(range(4),k):
            C=A
            for i in ss: C=erase(C,i)
            B=add(B,C)
        out.append(B)
    return out

def channel(A,p):
    B=A
    for i in range(4): B=add(scale(B,1-p),scale(erase(B,i),p))
    return B

def marginal(A,i):
    out=Z(2); mask=1<<(3-i)
    for x in range(16):
        if x&mask==0:
            for a in range(2):
                for b in range(2): out[a][b]=out[a][b]+A[x|a*mask][x|b*mask]
    return out

def h1(A):
    out=Z()
    for i in range(4):
        r=marginal(A,i); mask=1<<(3-i)
        for x in range(16):
            for y in range(16):
                if (x&~mask)==(y&~mask): out[x][y]=out[x][y]+r[bits(x,i)][bits(y,i)]
    return out

def inertia(A):
    """Exact Hermitian congruence; returns positive/zero/negative and pivot sizes."""
    A=[ar[:] for ar in A]; pos=neg=zero=0; pivots=[]
    assert A==adj(A)
    while A:
        n=len(A); k=next((i for i in range(n) if A[i][i]),None)
        if k is not None:
            order=[k]+[i for i in range(n) if i!=k]
            A=block(A,order); d=real(A[0][0]); pos+=d>0; neg+=d<0; pivots.append(1)
            A=[[A[i][j]-A[i][0]*A[0][j]/d for j in range(1,n)] for i in range(1,n)]
        else:
            pair=next(((i,j) for i in range(n) for j in range(i+1,n) if A[i][j]),None)
            if pair is None: zero+=n; break
            i,j=pair; order=[i,j]+[k for k in range(n) if k not in pair]
            A=block(A,order); z=A[0][1]; pos+=1; neg+=1; pivots.append(2)
            A=[[A[i][j]-A[i][0]*A[1][j]/z.conj()-A[i][1]*A[0][j]/z for j in range(2,n)] for i in range(2,n)]
    return {'positive':pos,'zero':zero,'negative':neg,'pivot_sizes':pivots}

def check(name,**kw): LOG['checks'].append({'name':name,**kw}); print('PASS',name,flush=True)
def negative(name,condition,**kw):
    assert condition, name
    LOG['negative_controls'].append({'name':name,'intended_reason_observed':True,**kw})
    print('NEGATIVE-CONTROL',name,flush=True)

def ksum_bounds(A,k=3,prec=38):
    """Finite exact spectral certificate, not numerical eigenvalue acceptance."""
    if all(not A[i][j] for i in range(len(A)) for j in range(len(A)) if i!=j):
        vals=sorted((real(A[i][i]) for i in range(len(A))),reverse=True)
        x=sum(vals[:k]); return x,x,{'diagonal_exact':True,'sum':str(x)}
    vals=np.linalg.eigvalsh(floats(A))[::-1]; den=1<<prec; upper=[]; lower=[]; receipts=[]; cache={}
    for j in range(k):
        center=F(float(vals[j])); u=F(math.ceil(center*den)+4,den); l=F(math.floor(center*den)-4,den)
        for _ in range(10):
            if u not in cache: cache[u]=inertia(shift(A,u))
            if cache[u]['positive']<=j: break
            u+=F(1,den)
        else: raise AssertionError('failed to certify upper bracket')
        for _ in range(10):
            if l not in cache: cache[l]=inertia(shift(A,l))
            if cache[l]['positive']>=j+1: break
            l-=F(1,den)
        else: raise AssertionError('failed to certify lower bracket')
        upper.append(u); lower.append(l)
        receipts.append({'descending_index':j+1,'lower':str(l),'upper':str(u),
                         'inertia_at_lower':cache[l],'inertia_at_upper':cache[u]})
    return sum(lower),sum(upper),{'dyadic_bits':prec,'eigenvalue_brackets':receipts,'sum_lower':str(sum(lower)),'sum_upper':str(sum(upper))}

def pure_data(v):
    A=density(v); rr=[]
    for i in range(4):
        r=marginal(A,i); z=real(r[0][0]-r[1][1]); rr.append(z*z+4*r[0][1].abs2())
    S=sum(rr); C=real(tr(mm(A,spin(A))))
    return A,rr,S,C

def sqbounds(q,bits_=70):
    n=q.numerator; d=q.denominator; den=1<<bits_; a=math.isqrt((n*den*den)//d)
    l=F(a,den); u=l if l*l==q else F(a+1,den)
    assert l*l<=q<=u*u
    return l,u

def region(v,t):
    A,rr,S,C=pure_data(v); m=4*S+8*C
    si=inertia(shift(add(h1(A),spin(A)),3))
    pflag=all(x==1 for x in rr); uflag=all(x==0 for x in rr)
    rb=[sqbounds(x) for x in rr]; lo=sorted(a for a,b in rb); hi=sorted(b for a,b in rb)
    weights=(1,1,3,3); delta_l=8-sum(w*r for w,r in zip(weights,hi)); delta_u=8-sum(w*r for w,r in zip(weights,lo))
    sl,su=sqbounds(39*(15-S)); rhs_l=t*(sl-5); rhs_u=t*(su-5)
    if delta_l>=rhs_u: dflag=True
    elif delta_u<rhs_l: dflag=False
    else: raise AssertionError('D membership interval unresolved')
    return A,{'P':pflag,'U':uflag,'D':dflag,'H':m<=F(64,9) and si['positive']<=1,
              'S':str(S),'C':str(C),'moment_lhs':str(m),'spin_shift_inertia':si,
              'delta_interval':[str(delta_l),str(delta_u)],'D_rhs_interval':[str(rhs_l),str(rhs_u)]}

def random_v(indices=range(16),dominant=None):
    v=[G() for _ in range(16)]
    for i in indices: v[i]=G(rng.randint(-3,3),rng.randint(-3,3))
    if dominant is not None: v[0]=G(dominant)
    assert norm2(v)>0; return v

def rational_unit(indices):
    coords=[F(rng.randint(-3,3),4) for _ in range(2*len(indices)-1)]
    q=sum(x*x for x in coords); coords=[2*x/(1+q) for x in coords]+[(1-q)/(1+q)]
    v=[G() for _ in range(16)]
    for k,i in enumerate(indices): v[i]=G(coords[2*k],coords[2*k+1])
    assert norm2(v)==1; return v

try:
    # Manifest/input verification is repeated here as an executable receipt.
    exp=['b76a11d666237befb1d00756835293d1b0b61e07ad77edcc41d8af2bb55b8321','e82ccb4a61bdeb64a820b300ff1f9ac14e22a46eb6845ebf0da12d186215f27d','c47ab533b912173162451da1ec88344e70fe7bfe86963ff11182c894ab38e841','3ebe180ae09307a8c1ed8aae0e58bb43e82d6c78a516342bb4676ac746a7ff7e']
    LOG['bindings']=[]
    for i,e in enumerate(exp,1):
        p=ROOT/f'manifest-v{i}.json'; b=p.read_bytes(); h=hashlib.sha256(b).hexdigest(); assert h==e
        LOG['bindings'].append({'path':str(p),'sha256':h,'bytes':len(b),'LF':b.count(b'\n')})
    manifest=json.loads((ROOT/'manifest-v4.json').read_bytes())
    for entry in manifest['inputs_in_read_order']:
        p=Path(entry['path']); b=p.read_bytes(); got=(hashlib.sha256(b).hexdigest(),len(b),b.count(b'\n'))
        assert got==(entry['sha256'],entry['bytes'],entry['LF']); LOG['bindings'].append(entry)
    check('all_manifest_v1_to_v4_and_v4_input_bindings')

    e0=[G(i==0) for i in range(16)]; R0=outer(e0); Qref=diag([int(i in (0,8,4)) for i in range(16)])
    reftr=[real(tr(mm(Qref,A))) for A in layers(R0)]
    assert reftr==[F(1),F(3),F(3),F(5,4),F(3,16)]
    for t in (F(0),F(1,200),F(1,3),F(1)):
        a=(1+t)/2; b=(1-t)/2; R=a**4+2*a**3*b
        assert 16*R==3+8*t+6*t*t-t**4
        assert sum(t**(4-m)*(1-t)**m*reftr[m] for m in range(5))==R
    check('product_reference_polynomial_and_five_layers',layer_traces=list(map(str,reftr)))

    for sample in range(3):
        v=random_v(); A=density(v); T=layers(A); FF=frame(A); HH=h1(A); til=spin(A)
        assert T[1]==add(A,scale(FF,F(1,4)))
        assert scale(T[2],4)==sub(add(add(HH,A),add(til,scale(FF,F(1,2)))),eye())
        assert til==add(sub(add(sub(A,scale(T[1],2)),scale(T[2],4)),scale(T[3],8)),scale(T[4],16))
        assert HH==scale(T[3],8) and scale(T[4],16)==eye()
        assert add(HH,til)==sub(scale(eye(),4),sub(h1(til),til))
        assert inertia(sub(h1(til),scale(til,2)))['negative']==0
        for p in (F(1,3),F(2,3),F(4,3)):
            out=channel(A,p)
            er=Z()
            for m in range(5): er=add(er,scale(T[m],(1-p)**(4-m)*p**m))
            assert out==er
            assert out==spin(channel(A,2-p))
        # Pure-state Pauli purity/moment identities, via independent monomial action.
        N=norm2(v); Aj=[F() for _ in range(5)]
        for word in product(range(4),repeat=4):
            w=pauli(v,word); ev=real(sum((G(x).conj()*y for x,y in zip(v,w)),G()))/N
            Aj[sum(x!=0 for x in word)]+=ev*ev
        S=Aj[1]; C=real(tr(mm(A,til)))
        assert Aj[3]==12+S-2*Aj[2] and Aj[4]==3-2*S+Aj[2]
        assert 16*C==1-S+Aj[2]-Aj[3]+Aj[4]
        assert Aj[2]==2+S+4*C
        assert tr(FF)==12 and real(tr(mm(FF,FF)))==16+4*S+8*C
        assert sum(Aj[2:])==15-S
        check('erasure_spin_purity_frame_'+str(sample),S=str(S),C=str(C),frame_second_moment=str(real(tr(mm(FF,FF)))))

    # Unit tests of exact inertia, including zero diagonal 2x2 pivot.
    assert inertia([[G(0),G(0,2)],[G(0,-2),G(0)]])['pivot_sizes']==[2]
    assert inertia(diag((1,0,-2)))['positive']==1
    check('exact_inertia_2x2_and_zero_pivots')
    g=lambda x:x*x/3+(12-x)**2/9
    assert g(F(8))==F(208,9)
    x=F(401,50)
    negative('rank12_moment_threshold_65_over_9_does_not_force_x_le_8',x>8 and g(x)>F(208,9) and g(x)<=F(209,9),
             synthetic_spectrum=['401/150 (3 copies)','199/450 (9 copies)'],x=str(x),second_moment=str(g(x)),
             note='PSD rank12 trace12 spectral lemma control, NOT an actual Pauli-frame counterexample')
    negative('fixed_Q_equality_at_p0_is_not_universal',real(tr(mm(diag([int(i in (1,2,4)) for i in range(16)]),R0)))==0,
             actual_trace='0',reference='1',erratum='127')

    # Exact equal-radius algebra at many rational s and rational probability weights.
    for s in (F(1,20),F(1,3),F(2,3),F(99,100)):
        K=(2-s)/(s*(3-s)); a1=1/(2-s/2)-1/(3-s); a2=1-1/(3-s)
        assert a1==K*s/(4-s) and a2==s*K and a1<=K and a2<=2*K
        for P1,P2,P4 in ((F(0),F(0),F(0)),(F(1,40),F(1,80),F(1,160))):
            P3=(s-P1-2*P2-4*P4)/3; P0=1-P1-P2-P3-P4
            lhs=P0/(3-s)+P1/(2-s/2)+P2+2*P3/s-1-P4/(1-s)
            rhs=(a1-K)*P1+(a2-2*K)*P2-(1/(3-s)+1/(1-s)+4*K)*P4
            assert lhs==rhs
    check('equal_radius_Schur_elimination_exact_algebra')

    def harmonic(v,label):
        A=density(v); B=spin(A)
        # Move each marginal majority to |0>, an exact local X change of basis.
        for i in range(4):
            r=marginal(B,i); assert not r[0][1]
            if real(r[1][1])>F(1,2):
                order=[flip(x,i) for x in range(16)]; B=block(B,order)
        p=[real(marginal(B,i)[1][1]) for i in range(4)]; s=sum(p)
        assert all(x<=s-x for x in p)
        ii=inertia(shift(sub(h1(B),B),1)); out={'label':label,'p':list(map(str,p)),'s':str(s),'inertia_M_minus_I':ii}
        if 0<s<1:
            aa=[3-s-sum((1-2*p[i] for i in range(4) if bits(x,i)),F()) for x in range(15)]
            assert all(x>=0 for x in aa)
            P=[real(B[i][i]) for i in range(16)]
            assert all(P[x]==0 for x in range(15) if aa[x]==0)
            W=sum((P[x]/aa[x] for x in range(15) if aa[x]>0),F()); rhs=1+P[15]/(1-s)
            assert (W<=rhs)==(ii['negative']<=1)
            out.update(W=str(W),rhs=str(rhs),zero_support_indices=[x for x in range(15) if aa[x]==0],passes=W<=rhs)
        elif s>=1: assert ii['negative']<=1
        else: assert s==0 and all(x==0 for x in p)
        return out
    harmonic_cases=[]
    for k in range(8):
        v=random_v([x for x in range(16) if wt(x)%2==0],dominant=12 if k<4 else None)
        harmonic_cases.append(harmonic(v,'random_even_'+str(k)))
    # Actual equality P0/P3 state; equal radii and 0<s<1.
    ve=[G() for _ in range(16)]; ve[0]=G(4)
    for i in (7,11,13,14): ve[i]=G(1)
    he=harmonic(ve,'equal_radius_P0_P3_equality'); assert he['W']==he['rhs']=='1'
    harmonic_cases.append(he)
    negative('harmonic_strict_or_lowered_threshold_rejects_actual_equality',he['inertia_M_minus_I']['negative']==1,
             state_amplitudes='4 at 0000; 1 at all four weight3 words; 0 otherwise',W='1',rhs='1',mutated_rhs='999/1000')
    vz=[G() for _ in range(16)]; vz[0]=G(6); vz[12]=G(1); vz[10]=G(2); vz[9]=G(1,1)
    hz=harmonic(vz,'polygon_equality_zero_support'); assert hz['zero_support_indices']; harmonic_cases.append(hz)
    harmonic_cases.append(harmonic(e0,'product_s_zero'))
    ghz=[G() for _ in range(16)]; ghz[0]=G(1); ghz[15]=G(1)
    harmonic_cases.append(harmonic(ghz,'GHZ_s_two'))
    check('harmonic_IFF_zero_support_equality_endpoints',cases=harmonic_cases)

    w1=[1,2,4,8]; rest=[i for i in range(16) if wt(i)>=2]
    def hessian(v,t):
        N=norm2(v); a=(1+t)/2; b=(1-t)/2
        lam=[a**(4-wt(i))*b**wt(i) for i in range(16)]
        V=channel(add(outer(v,e0),outer(e0,v)),1-t)
        W=channel(sub(outer(v),scale(R0,N)),1-t)
        AA=W[0][0]+sum((V[0][k]*V[k][0]/(lam[0]-lam[k]) for k in rest),G())
        M=[[W[i][j]+sum((V[i][k]*V[k][j]/(lam[i]-lam[k]) for k in rest),G()) for j in w1] for i in w1]
        return real(AA),M,V,W,lam
    def expected_hessian(v,t,h):
        N=norm2(v); a=(1+t)/2; b=(1-t)/2
        if h==2:
            TT=Z(4)
            for ii,i in enumerate(w1):
                for jj,j in enumerate(w1):
                    if i!=j: TT[ii][jj]=v[i|j]
            Gamma=mm(TT,adj(TT)); n=[real(Gamma[i][i]) for i in range(4)]
            AA=-a*a*t*(1-t*t)*N; M=Z(4)
            for i in range(4):
                for j in range(4):
                    M[i][j]=G(-a*b*t*(1-t*t)*(N-n[i])) if i==j else a*b*t*t*(1+t)*Gamma[i][j]
        elif h==3:
            g=[v[15^i] for i in w1]; D3=1-a*b
            AA=(-a*t*D3+a*t**5/D3)*N
            M=add(diag([-a*a*b*t*N-b*b*t*(1+t)*G(z).abs2() for z in g]),
                  scale(outer([G(z).conj() for z in g]),t*t*b*b+t**5*b/D3))
        else:
            D4=a*a+b*b; AA=(-t*D4+t**7/D4)*N; M=scale(eye(4),-a*b*t*N)
        return AA,M
    hessian_cases=[]
    for t in (F(1,200),F(1,3),F(2,5)):
        total=[G() for _ in range(16)]; sumA=F(); sumM=Z(4)
        for h in (2,3,4):
            v=random_v([i for i in range(16) if wt(i)==h]); N=norm2(v)
            AA,M,V,W,lam=hessian(v,t); ea,em=expected_hessian(v,t,h)
            assert AA==ea and M==em
            sumA+=AA; sumM=add(sumM,M); total=[a+b for a,b in zip(total,v)]
            assert V[0][0]==0 and block(V,w1)==Z(4)
            hessian_cases.append({'t':str(t),'weight':h,'norm_squared':str(N),'A':str(AA)})
            if h==2:
                negative('mutated_weight2_A_coefficient_t2_to_t3_at_'+str(t),AA!=-((1+t)/2)**2*t*(1-t**3)*N)
        AA,M,*_=hessian(total,t); assert AA==sumA and M==sumM
        if t==F(1,200):
            lo,up,cert=ksum_bounds(M,2)
            assert AA+up<=-F(15,64)*t*norm2(total)
            hessian_cases.append({'mixed_t':str(t),'A':str(AA),'K2_M_certificate':cert,'norm_squared':str(norm2(total))})
    check('Hessian_17_to_20_complex_matrix_unit_and_cross_weight_identities',cases=hessian_cases)
    for t in (F(1,200),F(1,3),F(2,5)):
        a=(1+t)/2; b=(1-t)/2; D3=1-a*b
        bound=-a*t*D3+a*t**5/D3-2*a*a*b*t+t*t*b*b+t**5*b/D3
        formula=-t*(1-t)*(15+24*t+38*t*t+32*t**3+3*t**4)/(32*D3)
        assert bound==formula
    check('weight3_bound_19_rational_function_identity')

    # Exact second-order 00/11 blocks from independent normalized commutators.
    v=rational_unit(rest); t=F(1,200); AA,M,V,W,lam=hessian(v,t)
    D=scale(sub(scale(channel(R0,1-t),16),eye()),1/t)
    VH=scale(V,16/t); WH=scale(W,16/t)
    group=lambda i:0 if i==0 else (1 if wt(i)==1 else 2)
    OFF=[[VH[i][j] if group(i)!=group(j) else G() for j in range(16)] for i in range(16)]
    SS=Z()
    for i in range(16):
        for j in range(16):
            if group(i)!=group(j): SS[i][j]=-VH[i][j]/(D[i][i]-D[j][j])
    assert adj(SS)==scale(SS,-1) and add(OFF,comm(D,SS))==Z()
    B=add(comm(VH,SS),scale(comm(comm(D,SS),SS),F(1,2))); QQ=add(WH,B)
    assert QQ[0][0]==AA*16/t and block(QQ,w1)==scale(M,16/t)
    W0=Z()
    for i in range(4):
        rv=marginal(outer(v),i)
        for p in (1,2,3):
            if p==1: coeff=2*rv[0][1].r
            elif p==2: coeff=-2*rv[0][1].i
            else: coeff=real(rv[0][0]-rv[1][1])-1
            W0=add(W0,scale(PAULIS[3*i+p-1],coeff))
    assert frob2(VH)<F(23,200)**2 and frob2(sub(WH,W0))<F(23,200)**2
    assert frob2(SS)<=F(23,400)**2 and frob2(B)<F(47,1000)**2
    check('normalized_commutator_leading_blocks_and_Frobenius_bounds',
          V_H_F2=str(frob2(VH)),W_H_minus_W0_F2=str(frob2(sub(WH,W0))),S1_F2=str(frob2(SS)),B_F2=str(frob2(B)))

    eta=F(9,40); s1=F(23,400); x=2*eta*s1
    assert 1/(1-x)<F(103,100) # positive-term geometric majorant for exp(x)
    remainder=F(103,100)*(5*(2*s1)**3/6+F(23,200)*(2*s1)**2/2+F(163,20)*(2*s1))
    assert remainder==F(580473701,600000000) and remainder<1
    assert eta*F(23,200)+eta*eta*F(41,5)==F(441,1000)
    assert 2-2*F(441,1000)>F(11,10)
    error=3*eta+3*F(47,1000)*eta**2+3*F(21,5)**2/F(11,10)*eta**2
    assert error==F(54870831,17600000) and error<F(13,4)
    assert F(15,4)-error>F(1,2)
    assert 512*F(1,200)**2<F(23,200)**2
    assert F(163,20)+F(47,1000)<F(41,5)
    assert 4+F(23,200)+F(47,1000)<F(21,5)
    assert 2*eta**2==F(81,800)>20*F(1,200)
    check('uniform_tube_all_explicit_rational_constants',remainder_coefficient=str(remainder),
          normalized_total_error_coefficient=str(error),far_delta_threshold='81/800',far_remainder_at_endpoint='1/10')
    negative('Hessian_margin_12_over_64_cannot_pay_displayed_errors',F(3)-error<F(1,2),
             mutated_margin='12/64',normalized_margin='3',error=str(error))
    negative('enlarging_uniform_t_to_1_over_190_breaks_far_gap_constant_chain',20*F(1,190)>=F(81,800))

    # Random exact region controls, and exact LDL certified top-three sums at both physical p.
    states=[]
    # Random pure products with genuinely complex rational local factors.
    prodvec=[G(1)]
    for i in range(4):
        q=[G(rng.randint(1,3),rng.randint(-2,2)),G(rng.randint(-3,3),rng.randint(-2,2))]
        prodvec=[x*y for x in prodvec for y in q]
    states.append(('random_product',prodvec))
    # Random locally phase-rotated GHZ, exactly one-uniform.
    z=G(F(3,5),F(4,5)); ug=[G() for _ in range(16)]; ug[0]=G(1); ug[15]=z
    # rational real orthogonal one-qubit rotations keep it one-uniform.
    for i in range(4):
        ang=F(3,5) if rng.randint(0,1) else F(5,13); sn=F(4,5) if ang==F(3,5) else F(12,13)
        vv=[G() for _ in range(16)]
        for k in range(16):
            if not bits(k,i):
                l=flip(k,i); vv[k]=ang*ug[k]-sn*ug[l]; vv[l]=sn*ug[k]+ang*ug[l]
        ug=vv
    states.append(('random_rotated_one_uniform',ug))
    # small even-parity perturbations of GHZ (D interior, typically H too).
    vg=random_v([i for i in range(16) if wt(i)%2==0]); vg[0]=G(40); vg[15]=G(40)
    states.append(('random_near_one_uniform_D',vg))
    for i in range(2): states.append(('random_full_'+str(i),random_v()))
    vp=random_v(); vp[0]=G(50); states.append(('random_near_product_outside_all',vp))
    vn=random_v([i for i in range(16) if wt(i)>=2]); vn[0]=G(70); states.append(('random_normal_near_product_outside_all',vn))
    states.append(('equal_radius_schur_equality',ve)); states.append(('polygon_zero_support',vz))
    region_receipts=[]; R=F(32,81)
    for label,v in states:
        A,flags=region(v,F(1,3)); entry={'label':label,'unnormalized_Gaussian_rational_amplitudes':[repr(x) for x in v],
                                     'norm_squared':str(norm2(v)),'classes_at_t_one_third':flags,'outputs':[]}
        C1=channel(A,F(2,3)); C2=channel(A,F(4,3)); assert C2==spin(C1)
        for p,C in ((F(2,3),C1),(F(4,3),C2)):
            lo,up,cert=ksum_bounds(C)
            if flags['P']:
                # Exact product output spectrum follows the independent one-site eigenspectra.
                assert all(x==1 for x in pure_data(v)[1]); proved='exact_tensor_product_spectrum'; actual=R
            else:
                assert up<=R; proved='exact_LDL_inertia_upper_bounds'; actual=up
            if flags['U']: assert actual<=R-F(2,27)
            entry['outputs'].append({'p':str(p),'reference':str(R),'method':proved,'certificate':cert})
        if flags['H']:
            ff=frame(A); f_lo,f_up,f_cert=ksum_bounds(ff); assert f_up<=8
            entry['K3_frame_certificate']=f_cert
            T=layers(A)
            for m in (1,2):
                ll,uu,cc=ksum_bounds(T[m]); assert uu<=3
                entry['K3_T'+str(m)+'_certificate']=cc
        if label=='random_near_product_outside_all': assert not any(flags[k] for k in ('P','U','D','H'))
        if label=='random_product':
            negative('one_uniform_gap_cannot_be_extended_to_products',R>R-F(2,27),actual_K3=str(R),false_bound=str(R-F(2,27)))
            negative('lowered_product_reference_32over81_minus_1over1000_fails',R>R-F(1,1000),actual_K3=str(R))
        region_receipts.append(entry); print('REGION',label,{k:flags[k] for k in ('P','U','D','H')},flush=True)
    for k in ('P','U','D','H'):
        assert any(e['classes_at_t_one_third'][k] for e in region_receipts)
        assert any(not e['classes_at_t_one_third'][k] for e in region_receipts)
    check('random_pure_states_inside_outside_each_region_and_exact_LDL_at_two_physical_p',cases=region_receipts)

    # Uniform-interval direct control in a rational normal tube; |0> stationarity
    # is exact. The tube proof itself only uses the normal representation.
    v=rational_unit(rest); eta=F(9,41); root=F(40,41)
    tube=[eta*z for z in v]; tube[0]=G(root); assert norm2(tube)==1
    A=density(tube); t=F(1,200); a=(1+t)/2; b=(1-t)/2; R=a**4+2*a**3*b
    out=channel(A,1-t); lo,up,cert=ksum_bounds(out)
    assert up<=R-t*eta*eta/32
    assert channel(A,1+t)==spin(out)
    check('direct_uniform_endpoint_normal_tube_exact_LDL',eta=str(eta),reference=str(R),
          claimed_gap=str(t*eta*eta/32),certificate=cert,
          amplitudes=[repr(z) for z in tube],note='Exact normal representation; no assertion that chosen |0> is the global maximizing product.')
    LOG['status']='PASS_ALL_DECLARED_CONTROLS'
except Exception as e:
    LOG['status']='FAILED'; LOG['error']=repr(e); LOG['traceback']=traceback.format_exc()
    traceback.print_exc()
finally:
    LOG['ended_native']=datetime.now().astimezone().isoformat()
    with RESULT.open('x') as f: json.dump(LOG,f,indent=2,ensure_ascii=False); f.write('\n')
    print('RESULT',RESULT,'STATUS',LOG['status'],flush=True)
if LOG['status']!='PASS_ALL_DECLARED_CONTROLS': sys.exit(1)
