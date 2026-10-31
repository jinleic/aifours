#!/usr/bin/env python3
"""Bounded seven-state PH search with nontriangular principal blocks.

The actual beta has three upstream entries; gamma has one downstream exit.
Both 3x3 principal blocks admit backward arcs, A also a forward skip, and the
center/return couplings are fully nonnegative. The downstream skip is excluded
because it would shorten the original four-edge path. Numeric fits are not
witnesses; a fit is converted to rational data and checked on the full matrix.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from itertools import combinations
from pathlib import Path
import json, sys, time
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
base=SourceFileLoader('frontier_exact',str(ROOT/'frontier-20261028-ph7-chain-search.py')).load_module()
bal=SourceFileLoader('frontier_bal',str(ROOT/'frontier-20261028-ph7-balanced-search.py')).load_module()
cyc=SourceFileLoader('frontier_cyc',str(ROOT/'frontier-20261028-ph7-balanced-cyclic-search.py')).load_module()
Z=F(8,9);C=F(1);MAX_ATTEMPTS=12;MAX_NFEV=1000;WALL_SECONDS=100;RNG=np.random.default_rng(20261103)


def data(z,rates,arcs,initial):
    u1,u2,u3,v1,v2,v3=rates; ac,ab,ad,ae,bb,bd,be=arcs;t0,t1=initial
    ar=cyc.det3([[[u1,1],[-1],[-ac]],[[-ab],[u2,1],[-1]],[[-ad],[-ae],[u3,1]]])
    bs=cyc.det3([[[v1,1],[-1],[0]],[[-bb],[v2,1],[-1]],[[-bd],[-be],[v3,1]]])
    U=[cyc.add([1],cyc.scale([u2,1],ac)),cyc.add([u1,1],[ab*ac]),cyc.add(cyc.mul([u1,1],[u2,1]),[-ab])]
    V=[cyc.add(cyc.mul([v2,1],[v3,1]),[-be]),[v3,1],[1]]
    Q=cyc.add(cyc.add(cyc.scale(U[0],t0),cyc.scale(U[1],t1)),U[2]);q,p=Q[:2]
    w=p+4-sum(rates)
    dz=cyc.mul([0,1],cyc.mul([1+z,2,1],[1+z,2,1]))
    target=cyc.mul(dz,Q)
    residual=cyc.add(cyc.mul([w,1],cyc.mul(ar,bs)),cyc.scale(target,-1))
    gens=[cyc.mul(bs,x) for x in U]+[cyc.mul(ar,x) for x in V]+[cyc.mul(V[j],U[i]) for j in range(3) for i in range(3)]
    def six(a):return (a+[0]*6)[:6]
    return [six(g) for g in gens],six(residual),w,p,q,Q


def fun(x):
    rates=x[:6];arcs=x[6:13];initial=x[13:15];fb=x[15:]
    M,b,w,p,q,_=data(8/9,rates,arcs,initial)
    M=np.asarray(M,float).T;b=np.asarray(b,float)
    return np.r_[(M@fb-b)/(1+np.abs(b)+np.abs(M)@fb),min(w,0.),min(q,0.)]


def exact_project(x):
    for denom in (100,1000,10000,100000):
        rates=[F(round(float(v)*denom),denom) for v in x[:6]]
        arcs=[F(round(float(v)*denom),denom) for v in x[6:13]]
        initial=[F(round(float(v)*denom),denom) for v in x[13:15]]
        M,b,w,p,q,Q=data(Z,rates,arcs,initial)
        if min(w,p,q)<=0 or not all(v>0 for v in rates) or not all(v>=0 for v in arcs+initial):continue
        free=[F(round(float(v)*denom),denom) for v in x[15:]]
        choices=sorted(combinations(range(15),6),key=lambda a:-sum(float(free[i]) for i in a))
        for choose in choices:
            others=[i for i in range(15) if i not in choose]
            rhs=[b[j]-sum(M[i][j]*free[i] for i in others) for j in range(6)]
            sol=bal.solve_square([[M[i][j] for i in choose] for j in range(6)],rhs)
            if sol is None:continue
            fb=free[:]
            for i,v in zip(choose,sol):fb[i]=v
            if all(v>=0 for v in fb):
                try:return verify(rates,arcs,initial,fb,w,p,q,Q)
                except AssertionError:continue
    return None


def verify(rates,arcs,initial,fb,w,p,q,Q):
    u1,u2,u3,v1,v2,v3=rates;ac,ab,ad,ae,bb,bd,be=arcs;t0,t1=initial
    r=fb[:3];f=fb[3:6];D=[fb[6:9],fb[9:12],fb[12:15]]
    G=[[F(0) for _ in range(7)]for _ in range(7)]
    for i,v in enumerate((u1,u2,u3,w,v1,v2,v3)):G[i][i]=-v
    for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6)):G[i][j]=F(1)
    for i,j,v in ((0,2,ac),(1,0,ab),(2,0,ad),(2,1,ae),(5,4,bb),(6,4,bd),(6,5,be)):G[i][j]=v
    for j in range(3):G[3][j]=r[j]
    for i in range(3):
        G[4+i][3]=f[i]
        for j in range(3):G[4+i][j]=D[i][j]
    def pencil():return [[([-G[i][j],F(1)]if i==j else[-G[i][j]])for j in range(7)]for i in range(7)]
    char=base.det_poly(pencil());dz=base.pol_mul([F(0),F(1)],base.pol_mul([1+Z,F(2),F(1)],[1+Z,F(2),F(1)]))
    if char!=base.pol_mul(dz,Q):raise AssertionError('char')
    K=C*((C+1)**2+Z)**2;beta=[t0,t1,F(1),F(0),F(0),F(0),F(0)];gamma=[F(0)]*6+[K]
    bump=[[a[:]for a in row]for row in pencil()]
    for i in range(7):
        for j in range(7):bump[i][j]=base.pol_add(bump[i][j],[gamma[i]*beta[j]])
    num=base.pol_add(base.det_poly(bump),[-v for v in char])
    while len(num)>3 and num[-1]==0:num.pop()
    if num!=[K*v for v in Q]:raise AssertionError('numerator')
    A=[[(C if i==j else F(0))-G[i][j]for j in range(7)]for i in range(7)]
    h=bal.solve_square(A,gamma)
    if h is None or not all(x>0 for x in h):raise AssertionError('h')
    T=[[(G[i][j]-(C if i==j else 0))*h[j]/h[i]for j in range(7)]for i in range(7)]
    alpha=[beta[i]*h[i]for i in range(7)];omega=[gamma[i]/h[i]for i in range(7)]
    if sum(alpha)!=1 or not all(v>=0 for v in alpha+omega):raise AssertionError('input')
    for i in range(7):
        if any(T[i][j]<0 for j in range(7) if i!=j)or sum(T[i])+omega[i]!=0:raise AssertionError('rows')
    if p<=0 or q<=0:raise AssertionError('stableQ')
    return {'rates':[str(v)for v in rates],'arcs':[str(v)for v in arcs],
      'initial':[str(v)for v in initial],'feedback':[str(v)for v in fb],'w':str(w),'p':str(p),'q':str(q),
      'G':[[str(v)for v in row]for row in G],'h':[str(v)for v in h],
      'alpha':[str(v)for v in alpha],'T':[[str(v)for v in row]for row in T],
      'omega':[str(v)for v in omega],
      'checks':['actual full7x7 determinant','actual adjugate numerator','h/input/exit/Metzler/rows','Hurwitz']}


def main():
    start=time.monotonic();best=None;runs=[];witness=None
    lower=np.array([.05]*6+[0.]*24);upper=np.array([5.]*6+[8.]*7+[15.]*2+[25.]*15)
    for attempt in range(MAX_ATTEMPTS):
        if time.monotonic()-start>WALL_SECONDS:break
        x0=np.r_[RNG.uniform(.7,1.8,6),RNG.uniform(.001,.4,7),RNG.uniform(.1,2.,2),RNG.uniform(.001,1.,15)]
        fit=least_squares(fun,x0,bounds=(lower,upper),max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        err=float(np.linalg.norm(fun(fit.x),ord=np.inf));runs.append({'attempt':attempt,'residual_inf':err,'nfev':int(fit.nfev)})
        if best is None or err<best[0]:best=(err,fit.x.copy())
        if err<1e-8:
            witness=exact_project(fit.x)
            if witness is not None:break
    report={'z':str(Z),'seed':20261103,'attempt_limit':MAX_ATTEMPTS,'elapsed_seconds':time.monotonic()-start,
      'runs':runs,'best_residual_inf':best[0] if best else None,'best_parameters':best[1].tolist() if best else None,
      'exact_witness':witness,'scope':'specified nontriangular ordered 3+1+3 family, not a global PH7 search or impossibility proof'}
    out=ROOT/'frontier-20261028-ph7-generalized-ordered-search-result.json'
    out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print('saved:',out)

if __name__=='__main__':main()
