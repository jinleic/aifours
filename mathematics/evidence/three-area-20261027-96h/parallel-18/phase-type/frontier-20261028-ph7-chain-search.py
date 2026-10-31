#!/usr/bin/env python3
"""Bounded exact-rational exploration of one previously published PH7 matrix family.

Scientific scope: z=b^2/d^2=8/9, d=1; scan rational upstream rates u on a
fixed grid. A hit is checked against every coefficient of the exact polynomial
matrix determinant and numerator, together with all literal PH row ties at
c=1. A grid miss is not an all-real-u or all-topology impossibility proof.
No solver, external model, network, process watcher or mutable outside files.
"""
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
Z = F(8, 9)
C = F(1)
N_STEPS = 4000
U_LO = F(1, 2)
U_HI = F(5, 2)


def family(u, z=Z):
    a = 3*u+3
    b = 3*u*u+9*u+3
    c3 = u**3+9*u*u+9*u+1
    e4 = 3*u**3+9*u*u+3*u
    e5 = 3*u**3+3*u*u
    e6 = u**3
    h0 = b+4*a-a*a-6
    L = b-4*a+10-2*z
    if L == 0:
        return None
    N = 4*h0+4-c3-b*(4-a)-4*z
    p = N/L
    q = (a-4)*p+h0-2*z
    w = p+4-a
    B = p-2*u
    C0 = q-u*p+u*u
    phi = e4+c3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
    R2 = e5+e4*w-(4+4*z)*q-(1+z)**2*p
    R1 = e6+e5*w-(1+z)**2*q
    R0 = e6*w
    D1 = R2-3*u*phi
    D2 = R1-3*u*u*phi-2*D1
    D3 = R0-u**3*phi-D1-D2
    return dict(u=u,L=L,p=p,q=q,w=w,B=B,C0=C0,phi=phi,D1=D1,D2=D2,D3=D3)


def pol_add(a,b):
    n=max(len(a),len(b)); return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n)]


def pol_mul(a,b):
    o=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): o[i+j]+=x*y
    return o


def det_poly(matrix):
    n=len(matrix); result=[F(0)]*(n+1)
    for perm in permutations(range(n)):
        term=[F(1)]; inversions=0
        for i,j in enumerate(perm):
            if matrix[i][j] == [F(0)]:
                term=[]; break
            term=pol_mul(term,matrix[i][j])
            inversions+=sum(perm[k]>j for k in range(i))
        if term:
            if inversions%2: term=[-x for x in term]
            result=pol_add(result,term)
    return result


def matrix_for(v):
    u,w=v['u'],v['w']
    G=[[F(0) for _ in range(7)] for _ in range(7)]
    for i in range(3): G[i][i]=-u
    G[0][1]=G[1][2]=F(1); G[2][3]=F(1)
    G[3][3]=-w; G[3][4]=F(1)
    for i in range(4,7): G[i][i]=F(-1)
    G[4][5]=G[5][6]=F(1)
    for i,k in enumerate(('D1','D2','D3'),4): G[i][0]=v[k]
    G[6][3]=v['phi']
    return G


def checked_witness(v):
    u=v['u']; p,q,w=v['p'],v['q'],v['w']
    z=Z; c=C
    G=matrix_for(v)
    def mat_y(shift):
        return [[([F(shift)-G[i][j],F(1)] if i==j else [-G[i][j]]) for j in range(7)] for i in range(7)]
    DG=det_poly(mat_y(F(0)))
    Dz=pol_mul([F(0),F(1)],pol_mul([1+z,F(2),F(1)],[1+z,F(2),F(1)]))
    expected=pol_mul(Dz,[q,p,F(1)])
    if DG != expected: raise AssertionError('actual characteristic polynomial mismatch')
    K=c*((c+1)**2+z)**2
    beta=[v['C0'],v['B'],F(1),F(0),F(0),F(0),F(0)]
    gamma=[F(0)]*6+[K]
    bumped=[[row[:] for row in line] for line in mat_y(F(0))]
    for i in range(7):
        for j in range(7): bumped[i][j]=pol_add(bumped[i][j],[gamma[i]*beta[j]])
    numerator=pol_add(det_poly(bumped),[-x for x in DG])
    while len(numerator)>3 and numerator[-1]==0: numerator.pop()
    if numerator != [K*q,K*p,K]: raise AssertionError('actual numerator polynomial mismatch')
    Qc=c*c+p*c+q
    h=[F(0)]*7
    h[0]=1/Qc; h[1]=(c+u)/Qc; h[2]=(c+u)**2/Qc; h[3]=(c+u)**3/Qc
    h[6]=(K+v['D3']*h[0]+v['phi']*h[3])/(c+1)
    h[5]=(h[6]+v['D2']*h[0])/(c+1)
    h[4]=(h[5]+v['D1']*h[0])/(c+1)
    if not all(x>0 for x in h): raise AssertionError('normalizer not strictly positive')
    for i in range(7):
        residual=sum((G[i][j]-(c if i==j else 0))*h[j] for j in range(7))+gamma[i]
        if residual: raise AssertionError('normalizer equation fails')
    T=[[(G[i][j]-(c if i==j else 0))*h[j]/h[i] for j in range(7)] for i in range(7)]
    alpha=[beta[i]*h[i] for i in range(7)]
    omega=[gamma[i]/h[i] for i in range(7)]
    if sum(alpha)!=1 or not all(x>=0 for x in alpha+omega): raise AssertionError('initial/exit positivity fails')
    for i in range(7):
        if any(T[i][j]<0 for j in range(7) if j!=i): raise AssertionError('Metzler fails')
        if sum(T[i])+omega[i]!=0: raise AssertionError('literal row tie fails')
    if not (p>0 and q>0 and c>0): raise AssertionError('hidden quadratic Hurwitz condition missing')
    return {'target_z':str(z),'c':str(c),'u':str(u),
            'rates':{k:str(x) for k,x in v.items()},'K':str(K),
            'raw_G':[[str(x) for x in row] for row in G],
            'h':[str(x) for x in h], 'alpha':[str(x) for x in alpha],
            'T':[[str(x) for x in row] for row in T], 'omega':[str(x) for x in omega],
            'exact_checks':['actual 7x7 characteristic polynomial','actual rank-one-update numerator polynomial',
                            'positive normalizer and all seven physical row equations',
                            'probability input/nonnegative exit/Metzler','Hurwitz via exact p,q,c positivity']}


def main():
    best=None; hits=[]; valid=0
    positivity=('p','q','w','B','C0','phi','D1','D2','D3')
    for i in range(N_STEPS+1):
        u=U_LO+(U_HI-U_LO)*i/N_STEPS
        v=family(u)
        if v is None: continue
        valid+=1
        margin=min(v[k] for k in positivity)
        if best is None or margin>best[0]: best=(margin,v)
        if margin>=0:
            hits.append(v)
            if len(hits)>=3: break
    report={'target_z':str(Z),'grid':{'u_min':str(U_LO),'u_max':str(U_HI),'steps':N_STEPS},
            'checked_grid_points':valid,'hits':len(hits),'scope':'exact rational grid only; misses are not a universal exclusion'}
    if best:
        report['best_minimum_exact']=str(best[0]); report['best_rate']=str(best[1]['u'])
        report['best_coefficients']={k:str(best[1][k]) for k in positivity}
    if hits:
        report['first_witness']=checked_witness(hits[0])
    out=ROOT/'frontier-20261028-ph7-chain-search-result.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    print('saved:',out)
    return 0

if __name__=='__main__':
    sys.exit(main())
