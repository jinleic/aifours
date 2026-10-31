#!/usr/bin/env python3
"""Independent exact v4 off-block constants, normal examples, and endpoints."""
from pathlib import Path
from fractions import Fraction as F
import json
ns={}
exec((Path(__file__).parent/'review-check.py').read_text().split('\nresult=')[0],ns)
G=ns['G']; G0=ns['G0']; add=ns['add']; sub=ns['sub']; mul=ns['mul']; conj=ns['conj']; scale=ns['scale']; form=ns['form']; sumg=ns['sumg']
N=16; Z=F(0)
def matadd(A,B):return [[add(A[i][j],B[i][j]) for j in range(N)] for i in range(N)]
def matsub(A,B):return [[sub(A[i][j],B[i][j]) for j in range(N)] for i in range(N)]
def matscale(A,x):return [[scale(z,x) for z in row] for row in A]
def matmul(A,B):return [[sumg(mul(A[i][k],B[k][j]) for k in range(N) if A[i][k]!=G0 and B[k][j]!=G0) for j in range(N)] for i in range(N)]
def comm(A,B):return matsub(matmul(A,B),matmul(B,A))
def group(i):return 0 if i==0 else 1 if i.bit_count()==1 else 2
def norm2(A):return sum((x*x+y*y for row in A for x,y in row),Z)
def off(A):return [[A[i][j] if group(i)!=group(j) else G0 for j in range(N)] for i in range(N)]
def generator(A,diag):
    return [[scale(A[i][j],-1/(diag[i]-diag[j])) if group(i)!=group(j) else G0 for j in range(N)] for i in range(N)]
def isanti(A):return all(A[i][j]==scale(conj(A[j][i]),-1) for i in range(N) for j in range(N))
def bloch(v,bit):
    x=sumg(mul(conj(v.get(i^(1<<bit),G0)),c) for i,c in v.items())
    y=sumg(mul(mul(conj(v.get(i^(1<<bit),G0)),c),G(0,1-2*((i>>bit)&1))) for i,c in v.items())
    z=sum(((c[0]*c[0]+c[1]*c[1])*(1-2*((i>>bit)&1)) for i,c in v.items()),Z)
    assert x[1]==0 and y[1]==0
    return x[0],y[0],z

def v4_matrices(q,v):
    a,b,E=form(q)
    diag=[(16*a**(4-i.bit_count())*b**i.bit_count()-1)/q for i in range(N)]
    assert max(abs(x) for x in diag)<5
    assert min(abs(diag[i]-diag[j]) for i in range(N) for j in range(N) if group(i)!=group(j))>=2
    V=[];W=[]
    for i in range(N):
        vv=[];ww=[]
        for j in range(N):
            vij=sumg(add(scale(c,E(x,0,i,j)),scale(conj(c),E(0,x,i,j))) for x,c in v.items())
            wij=sub(sumg(scale(mul(cx,conj(cy)),E(x,y,i,j)) for x,cx in v.items() for y,cy in v.items()),G(E(0,0,i,j)))
            vv.append(scale(vij,16/q));ww.append(scale(wij,16/q))
        V.append(vv);W.append(ww)
    rs=[bloch(v,k) for k in range(4)]
    W0=[[G0 for j in range(N)] for i in range(N)]
    for i in range(N):
        W0[i][i]=G(sum(((rs[k][2]-1)*(1-2*((i>>k)&1)) for k in range(4)),Z))
        for k in range(4):
            j=i^(1<<k);W0[i][j]=G(rs[k][0],rs[k][1]*(2*((i>>k)&1)-1))
    S1=generator(V,diag); assert isanti(S1)
    DS=[[scale(S1[i][j],diag[i]-diag[j]) for j in range(N)] for i in range(N)]
    Q=matadd(matadd(W,comm(V,S1)),matscale(comm(DS,S1),F(1,2)))
    S2=generator(Q,diag);assert isanti(S2)
    checks={'V_F':norm2(V)<F(23,1000)**2,'W0_F':norm2(W0)<=16**2,
            'offW0_F':norm2(off(W0))<=8**2,'W_minus_W0_F':norm2(matsub(W,W0))<F(23,1000)**2,
            'S1_F':norm2(S1)<F(3,250)**2,'Q_F':norm2(Q)<17**2,
            'offQ_F':norm2(off(Q))<F(81,10)**2,'S2_F':norm2(S2)<F(41,10)**2}
    assert all(checks.values())
    return checks

def scalar():
    t=F(1,1000);eps=F(1,100); star=F(9,10**6)
    assert 512*t*t<F(23,1000)**2
    v=F(23,1000);s1=F(3,250)
    Q=16+v+2*v*s1+10*s1*s1
    Qoff=8+v+2*v*s1+10*s1*s1
    assert Q<17 and Qoff<F(81,10)
    rem0=v+eps*17; assert rem0<F(1,5)
    first=5*F(3,125)**3/3+v*F(3,125)**2+2*17*F(3,125)+F(1,5)
    second=5*F(41,5)**2/100+2*v*F(41,5)+2*17*F(41,5)/100+F(11,10)
    exact_mat_diff=eps*v+eps**2*17+eps**3*F(1,5)
    approx_mat_diff=eps*v+eps**2*17
    assert first<F(11,10) and second==F(4767,625)<8
    assert exact_mat_diff<F(1,500) and approx_mat_diff<F(1,500)
    assert 3*8*eps<F(15,32) and 20*star<2/F(10001)
    return {'V_F_squared_upper':str(512*t*t),'Q_F_upper':str(Q),'offQ_F_upper':str(Qoff),
            'normalized_initial_remainder_upper':str(rem0),'first_cubic_budget':str(first),
            'second_cubic_budget':str(second),'actual_perturbation_upper':str(exact_mat_diff),
            'approximation_perturbation_upper':str(approx_mat_diff),
            'hessian_remainder_slack':str(F(15,32)-3*8*eps),'far_slack':str(F(2,10001)-20*star)}

def endpoint():
    v={0:G(1500),3:G(1),7:G(0,2),15:G(2)}
    a1=F(312511250077,5000000000000); a2=F(3125056249701,50000000000000)
    rows=[]
    for q in (F(9,10**6),-F(9,10**6)):
        M=ns['tensor_output'](q,v)
        assert M==ns['pauli_output'](q,v)
        I=ns['inertia_ldl']; shift=ns['shift']
        out=I(M);i1=I(shift(M,a1));i2=I(shift(M,a2))
        assert out==(16,0,0) and i1==(16,0,0) and i2==(15,1,0)
        aa,bb=(1+abs(q))/2,(1-abs(q))/2
        ref=aa**4+2*aa**3*bb;cap=a1+2*a2
        tr=sum((M[i][i][0] for i in ((0,1,2) if q>0 else (15,14,13))),Z)
        assert cap==F(2343806250043,12500000000000)
        assert ref==F(3000072000485999999993439,16000000000000000000000000)
        assert ref-cap==F(430959999993439,16000000000000000000000000)>0
        assert tr==F(750021000085500053998683749271,4000016000000000000000000000000) and tr<cap
        rows.append({'q':str(q),'pauli_matches_tensor':True,'output_inertia':out,'u1_inertia':i1,'u2_inertia':i2,'cap':str(cap),'reference':str(ref),'gap_lower':str(ref-cap),'projector_trace':str(tr)})
    return rows

vectors=[{3:G(F(1,3)),7:G(0,F(2,3)),15:G(F(2,3))},
         {3:G(F(1,2)),5:G(0,F(1,2)),6:G(F(1,2)),9:G(0,F(-1,2))}]
for v in vectors:assert sum((x*x+y*y for x,y in v.values()),Z)==1
results=[]
for q in (F(1,1000),F(9,10**6)):
    for v in vectors:results.append({'q':str(q),'nonzero_normal_indices':list(v),'bounds':v4_matrices(q,v)})
print(json.dumps({'scalar':scalar(),'normal_direction_cases':results,'endpoint':endpoint()},indent=2,sort_keys=True))
