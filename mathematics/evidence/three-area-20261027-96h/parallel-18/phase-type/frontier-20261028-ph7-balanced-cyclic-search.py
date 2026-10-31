#!/usr/bin/env python3
"""Search actual balanced PH7 with both 3x3 principal blocks nontriangular.

Both input/output numerators have degree one, with same-matrix normalization.
No numerical candidate is called a witness: rationalize, solve six polynomial
coefficients exactly, then independently verify the complete actual 7x7 matrix.
A failed local search has no global or family-wide exclusion meaning.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from itertools import permutations, combinations
from pathlib import Path
import json, sys, time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
base=SourceFileLoader('frontier_exact',str(ROOT/'frontier-20261028-ph7-chain-search.py')).load_module()
bal=SourceFileLoader('frontier_bal',str(ROOT/'frontier-20261028-ph7-balanced-search.py')).load_module()
Z=F(8,9); C=F(1); RNG=np.random.default_rng(20261030)
MAX_ATTEMPTS=8; MAX_NFEV=600; WALL_SECONDS=90


def add(a,b):
    n=max(len(a),len(b)); return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
def scale(a,x): return [x*v for v in a]
def det3(a):
    out=[0]
    for p in permutations(range(3)):
        t=[1]; parity=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
        for i,j in enumerate(p): t=mul(t,a[i][j])
        out=add(out,scale(t,-1 if parity else 1))
    return out


def data(z, rates, arcs, endpoints):
    u1,u2,u3,v1,v2,v3=rates; ac,ab,ad,ae,bc,bb,bd,be=arcs; t,g=endpoints
    AR=[[[u1,1],[-1],[-ac]],[[-ab],[u2,1],[-1]],[[-ad],[-ae],[u3,1]]]
    BS=[[[v1,1],[-1],[-bc]],[[-bb],[v2,1],[-1]],[[-bd],[-be],[v3,1]]]
    ar=det3(AR); bs=det3(BS)
    U=[add([1],scale([u2,1],ac)),add([u1,1],[ab*ac]),add(mul([u1,1],[u2,1]),[-ab])]
    V=[add(mul([v2,1],[v3,1]),[-be]),add([v3,1],[bc*be]),add([1],scale([v2,1],bc))]
    NR=add(scale(U[0],t),U[1]); NS=add(V[1],scale(V[2],g))
    xi=NR[0]/NR[1]; eta=NS[0]/NS[1]
    p=xi+eta; q=xi*eta; w=p+4-sum(rates)
    dz=mul([0,1],mul([1+z,2,1],[1+z,2,1])); target=mul(dz,[q,p,1])
    residual=add(mul([w,1],mul(ar,bs)),scale(target,-1))
    generators=[mul(bs,v) for v in U]+[mul(ar,v) for v in V]+[mul(U[0],v) for v in V]
    def six(poly): return (poly+[0]*6)[:6]
    return [six(g) for g in generators],six(residual),w,xi,eta,NR[1]*NS[1]


def fun(x):
    rates=x[:6]; arcs=x[6:14]; endpoints=x[14:16]; fb=x[16:]
    try:
        mat,b,w,_,_,_=data(8/9,rates,arcs,endpoints)
        M=np.asarray(mat,float).T; b=np.asarray(b,float)
        return np.r_[(M@fb-b)/(1+np.abs(b)+np.abs(M)@fb),min(w,0.)]
    except (ValueError,ZeroDivisionError,FloatingPointError): return np.ones(7)*1e8


def exact_project(x):
    for denom in (100,1000,10000,100000):
        rates=[F(round(float(v)*denom),denom) for v in x[:6]]
        arcs=[F(round(float(v)*denom),denom) for v in x[6:14]]
        endpoints=[F(round(float(v)*denom),denom) for v in x[14:16]]
        if not all(v>0 for v in rates) or not all(v>=0 for v in arcs+endpoints): continue
        M,b,w,xi,eta,lead=data(Z,rates,arcs,endpoints)
        if min(w,xi,eta,lead)<=0: continue
        free=[F(round(float(v)*denom),denom) for v in x[16:]]
        for choose in combinations(range(9),6):
            others=[i for i in range(9) if i not in choose]
            rhs=[b[j]-sum(M[i][j]*free[i] for i in others) for j in range(6)]
            sol=bal.solve_square([[M[i][j] for i in choose] for j in range(6)],rhs)
            if sol is None: continue
            fb=free[:]
            for i,v in zip(choose,sol): fb[i]=v
            if all(v>=0 for v in fb):
                try: return verify(rates,arcs,endpoints,fb,w,xi,eta,lead)
                except AssertionError: continue
    return None


def verify(rates,arcs,endpoints,fb,w,xi,eta,lead):
    u1,u2,u3,v1,v2,v3=rates; ac,ab,ad,ae,bc,bb,bd,be=arcs; t,g=endpoints
    r=fb[:3]; f=fb[3:6]; D=fb[6:]
    G=[[F(0) for _ in range(7)] for _ in range(7)]
    for i,v in enumerate((u1,u2,u3,w,v1,v2,v3)): G[i][i]=-v
    for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6)): G[i][j]=F(1)
    for i,j,v in ((0,2,ac),(1,0,ab),(2,0,ad),(2,1,ae),(4,6,bc),(5,4,bb),(6,4,bd),(6,5,be)): G[i][j]=v
    for i in range(3): G[3][i]=r[i]; G[4+i][3]=f[i]; G[4+i][0]=D[i]
    def pencil(): return [[([-G[i][j],F(1)] if i==j else [-G[i][j]]) for j in range(7)] for i in range(7)]
    char=base.det_poly(pencil())
    dz=base.pol_mul([F(0),F(1)],base.pol_mul([1+Z,F(2),F(1)],[1+Z,F(2),F(1)]))
    q=base.pol_mul([xi,F(1)],[eta,F(1)])
    if char!=base.pol_mul(dz,q): raise AssertionError('characteristic mismatch')
    K=C*((C+1)**2+Z)**2
    beta=[t,F(1),F(0),F(0),F(0),F(0),F(0)]
    gamma=[F(0)]*5+[K/lead,K*g/lead]
    bumped=[[p[:] for p in row] for row in pencil()]
    for i in range(7):
        for j in range(7): bumped[i][j]=base.pol_add(bumped[i][j],[gamma[i]*beta[j]])
    num=base.pol_add(base.det_poly(bumped),[-v for v in char])
    while len(num)>3 and num[-1]==0: num.pop()
    if num!=[K*v for v in q]: raise AssertionError('numerator mismatch')
    A=[[(C if i==j else F(0))-G[i][j] for j in range(7)] for i in range(7)]
    h=bal.solve_square(A,gamma)
    if h is None or not all(v>0 for v in h): raise AssertionError('normalizer')
    T=[[(G[i][j]-(C if i==j else 0))*h[j]/h[i] for j in range(7)] for i in range(7)]
    alpha=[beta[i]*h[i] for i in range(7)]; omega=[gamma[i]/h[i] for i in range(7)]
    if sum(alpha)!=1 or not all(v>=0 for v in alpha+omega): raise AssertionError('alpha/exit')
    for i in range(7):
        if any(T[i][j]<0 for j in range(7) if i!=j) or sum(T[i])+omega[i]!=0: raise AssertionError('rows')
    if not(xi>0 and eta>0): raise AssertionError('hidden stability')
    return {'target_z':str(Z),'c':str(C),'rates':[str(v) for v in rates],'arcs':[str(v) for v in arcs],
            'endpoints':[str(v) for v in endpoints],'feedback':[str(v) for v in fb],
            'w':str(w),'xi':str(xi),'eta':str(eta),'K':str(K),
            'G':[[str(v) for v in row] for row in G],'h':[str(v) for v in h],
            'alpha':[str(v) for v in alpha],'T':[[str(v) for v in row] for row in T],
            'omega':[str(v) for v in omega],
            'exact_checks':['all coefficients of full actual determinant','full actual numerator',
                            'positive h/probability/Metzler/literal exit','Hurwitz from exact Q roots']}


def main():
    start=time.monotonic(); best=None; runs=[]; witness=None
    lower=np.array([.05]*6+[0.]*19); upper=np.array([5.]*6+[5.]*8+[20.]*2+[20.]*9)
    for attempt in range(MAX_ATTEMPTS):
        if time.monotonic()-start>WALL_SECONDS: break
        x0=np.r_[RNG.uniform(.7,1.8,6),RNG.uniform(.01,.4,8),RNG.uniform(.1,2.,2),RNG.uniform(.01,1.,9)]
        fit=least_squares(fun,x0,bounds=(lower,upper),max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        err=float(np.linalg.norm(fun(fit.x),ord=np.inf))
        runs.append({'attempt':attempt,'residual_inf':err,'evaluations':int(fit.nfev),'optimality':float(fit.optimality)})
        if best is None or err<best[0]: best=(err,fit.x.copy())
        if err<1e-8:
            witness=exact_project(fit.x)
            if witness is not None: break
    report={'seed':20261030,'attempt_limit':MAX_ATTEMPTS,'wall_seconds_limit':WALL_SECONDS,
            'elapsed_seconds':time.monotonic()-start,'runs':runs,'best_residual_inf':best[0] if best else None,
            'best_parameters':best[1].tolist() if best else None,'exact_witness':witness,
            'scope':'specified balanced nontriangular 3+3 family; numerical miss is not proof or global exclusion'}
    out=ROOT/'frontier-20261028-ph7-balanced-cyclic-search-result.json'
    out.write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report,indent=2)); print('saved:',out)

if __name__=='__main__': main()
