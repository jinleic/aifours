#!/usr/bin/env python3
"""Search a physical balanced 3+1+3 PH7 family at the original z=8/9.

Six independent positive chain rates, two nonnegative input/exit offsets and
nine actual feedback entries are optimized. Numeric fits are ONLY candidates.
Each prospective hit is rationalized, solved exactly in six feedback variables,
and checked by the literal 7x7 determinant/adjugate, positive similarity, PH
row ties and Hurwitz polynomial. Failure never excludes another PH7 topology.
"""
from fractions import Fraction as F
from itertools import combinations
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json, sys, time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
base=SourceFileLoader('frontier_exact',str(ROOT/'frontier-20261028-ph7-chain-search.py')).load_module()
Z=F(8,9); CZ=F(1)
RNG=np.random.default_rng(20261029)
ATTEMPTS=24; MAX_NFEV=1300; WALL_SECONDS=90


def coeffs(z, rates, offsets):
    u1,u2,u3,v1,v2,v3=rates
    xi=u1+offsets[0]; eta=v3+offsets[1]
    p=xi+eta; q=xi*eta
    w=p+4-sum(rates)
    U=base.pol_mul(base.pol_mul([u1,1],[u2,1]),[u3,1])
    V=base.pol_mul(base.pol_mul([v1,1],[v2,1]),[v3,1])
    D=base.pol_mul([0,1],base.pol_mul([1+z,2,1],[1+z,2,1]))
    residual=base.pol_add(base.pol_mul([w,1],base.pol_mul(U,V)),[-t for t in base.pol_mul(D,[q,p,1])])
    Vb=[base.pol_mul([v2,1],[v3,1]),[v3,1],[1]]
    Ub=[[1],[u1,1],base.pol_mul([u1,1],[u2,1])]
    generators=[base.pol_mul(V,x) for x in Ub]+[base.pol_mul(U,x) for x in Vb]+Vb
    def six(a): return (a+[0]*6)[:6]
    return [six(g) for g in generators],six(residual),w,xi,eta


def residual_numeric(x):
    rates=x[:6]; offsets=x[6:8]; f=x[8:]
    generators,r,w,xi,eta=coeffs(8/9,rates,offsets)
    g=np.asarray(generators,dtype=float).T; r=np.asarray(r,dtype=float)
    scale=1+np.abs(r)+np.abs(g)@f
    e=(g@f-r)/scale
    return np.r_[e, min(w,0.0)]


def solve_square(A,b):
    n=len(b); M=[[F(x) for x in A[i]]+[F(b[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if M[i][j]),None)
        if pivot is None: return None
        M[j],M[pivot]=M[pivot],M[j]; v=M[j][j]; M[j]=[x/v for x in M[j]]
        for i in range(n):
            if i!=j:
                v=M[i][j]; M[i]=[x-v*y for x,y in zip(M[i],M[j])]
    return [row[-1] for row in M]


def exact_project(x):
    for denom in (100,1000,10000,100000):
        rates=[F(round(float(v)*denom),denom) for v in x[:6]]
        offsets=[F(round(float(v)*denom),denom) for v in x[6:8]]
        g,r,w,xi,eta=coeffs(Z,rates,offsets)
        if not(w>0 and all(v>0 for v in rates) and all(v>=0 for v in offsets)): continue
        free=[F(round(float(v)*denom),denom) for v in x[8:]]
        for choice in combinations(range(9),6):
            others=[i for i in range(9) if i not in choice]
            rhs=[r[j]-sum(g[i][j]*free[i] for i in others) for j in range(6)]
            sol=solve_square([[g[i][j] for i in choice] for j in range(6)],rhs)
            if sol is None: continue
            candidate=free[:]
            for i,v in zip(choice,sol): candidate[i]=v
            if all(v>=0 for v in candidate):
                try: return actual_check(rates,offsets,candidate,w,xi,eta)
                except AssertionError: continue
    return None


def actual_check(rates, offsets, fb,w,xi,eta):
    u1,u2,u3,v1,v2,v3=rates; r=fb[:3]; f=fb[3:6]; D=fb[6:]
    G=[[F(0) for _ in range(7)] for _ in range(7)]
    for i,v in enumerate((u1,u2,u3,w,v1,v2,v3)): G[i][i]=-v
    for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6)): G[i][j]=F(1)
    for j in range(3): G[3][j]=r[j]
    for i in range(3): G[4+i][3]=f[i]; G[4+i][0]=D[i]
    def pencil(): return [[([-G[i][j],F(1)] if i==j else [-G[i][j]]) for j in range(7)] for i in range(7)]
    char=base.det_poly(pencil())
    target=base.pol_mul([F(0),F(1)],base.pol_mul([1+Z,F(2),F(1)],[1+Z,F(2),F(1)]))
    Q=base.pol_mul([xi,F(1)],[eta,F(1)])
    if char!=base.pol_mul(target,Q): raise AssertionError('actual characteristic')
    K=CZ*((CZ+1)**2+Z)**2
    beta=[offsets[0],F(1),F(0),F(0),F(0),F(0),F(0)]
    gamma=[F(0)]*5+[K,K*offsets[1]]
    bumped=[[poly[:] for poly in row] for row in pencil()]
    for i in range(7):
        for j in range(7): bumped[i][j]=base.pol_add(bumped[i][j],[gamma[i]*beta[j]])
    numerator=base.pol_add(base.det_poly(bumped),[-x for x in char])
    while len(numerator)>3 and numerator[-1]==0: numerator.pop()
    if numerator!=[K*q for q in Q]: raise AssertionError('actual numerator')
    A=[[(CZ if i==j else F(0))-G[i][j] for j in range(7)] for i in range(7)]
    h=solve_square(A,gamma)
    if h is None or not all(x>0 for x in h): raise AssertionError('strictly positive normalizer')
    T=[[(G[i][j]-(CZ if i==j else 0))*h[j]/h[i] for j in range(7)] for i in range(7)]
    alpha=[beta[i]*h[i] for i in range(7)]; omega=[gamma[i]/h[i] for i in range(7)]
    if sum(alpha)!=1 or not all(x>=0 for x in alpha+omega): raise AssertionError('alpha/exit')
    for i in range(7):
        if any(T[i][j]<0 for j in range(7) if i!=j) or sum(T[i])+omega[i]!=0: raise AssertionError('Metzler/row')
    if not(xi>0 and eta>0): raise AssertionError('hidden Q stability')
    return {'z':str(Z),'c':str(CZ),'rates':[str(x) for x in rates],
            'offsets':[str(x) for x in offsets], 'feedback':[str(x) for x in fb],
            'w':str(w),'xi':str(xi),'eta':str(eta),'K':str(K),
            'G':[[str(v) for v in row] for row in G], 'h':[str(v) for v in h],
            'alpha':[str(v) for v in alpha],'T':[[str(v) for v in row] for row in T],
            'omega':[str(v) for v in omega],
            'checks':['exact full determinant','exact adjugate numerator','positive h',
                      'probability input, nonnegative exit, Metzler, exact row sums','Hurwitz from Q roots and c>0']}


def main():
    start=time.monotonic(); best=None; runs=[]; witness=None
    lower=np.array([.05]*6+[0.]*11); upper=np.array([4.]*6+[5.]*2+[12.]*9)
    for attempt in range(ATTEMPTS):
        if time.monotonic()-start>WALL_SECONDS: break
        x0=np.r_[RNG.uniform(.5,2.0,6),RNG.uniform(.1,1.5,2),RNG.uniform(.01,1.0,9)]
        fit=least_squares(residual_numeric,x0,bounds=(lower,upper),max_nfev=MAX_NFEV,
                          ftol=1e-12,xtol=1e-12,gtol=1e-12)
        norm=float(np.linalg.norm(residual_numeric(fit.x),ord=np.inf))
        item={'attempt':attempt,'residual_inf':norm,'evaluations':int(fit.nfev),'optimality':float(fit.optimality)}
        runs.append(item)
        if best is None or norm<best[0]: best=(norm,fit.x.copy())
        if norm<1e-8:
            witness=exact_project(fit.x)
            if witness is not None: break
    report={'seed':20261029,'attempt_limit':ATTEMPTS,'wall_seconds_limit':WALL_SECONDS,
            'elapsed_seconds':time.monotonic()-start,'runs':runs,
            'best_residual_inf':best[0] if best else None,
            'best_parameters':best[1].tolist() if best else None,'exact_witness':witness,
            'scope':'balanced 3+1+3 chain only; numerical fit or failure is never proof'}
    out=ROOT/'frontier-20261028-ph7-balanced-search-result.json'
    out.write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report,indent=2)); print('saved:',out)

if __name__=='__main__': main()
