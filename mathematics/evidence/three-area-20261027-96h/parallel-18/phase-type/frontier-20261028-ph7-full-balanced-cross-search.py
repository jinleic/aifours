#!/usr/bin/env python3
"""Actual balanced 3+1+3 PH7, with all nine cross-block feedbacks.

This strictly extends the prior balanced-cyclic program, which only allowed
three cross-block entries to the first upstream state. The analytic coefficient
formula is independently compared with a direct Fraction 7x7 determinant and
adjugate on one dense positive rational instance. Numeric optimization and
failed runs never prove infeasibility. Prospective hits require exact checks.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from itertools import combinations
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
cy=SourceFileLoader('cy',str(ROOT/'frontier-20261028-ph7-balanced-cyclic-search.py')).load_module()
base=cy.base;bal=cy.bal
Z=F(8,9);C=F(1);RNG=np.random.default_rng(20261111)
LIMIT=12;EVALS=1000;WALL=90

def data(z,rates,arcs,endpoints):
    u1,u2,u3,v1,v2,v3=rates;ac,ab,ad,ae,bc,bb,bd,be=arcs;t,g=endpoints
    AR=[[[u1,1],[-1],[-ac]],[[-ab],[u2,1],[-1]],[[-ad],[-ae],[u3,1]]]
    BS=[[[v1,1],[-1],[-bc]],[[-bb],[v2,1],[-1]],[[-bd],[-be],[v3,1]]]
    a=cy.det3(AR);b=cy.det3(BS)
    U=[cy.add([1],cy.scale([u2,1],ac)),cy.add([u1,1],[ab*ac]),cy.add(cy.mul([u1,1],[u2,1]),[-ab])]
    V=[cy.add(cy.mul([v2,1],[v3,1]),[-be]),cy.add([v3,1],[bc*be]),cy.add([1],cy.scale([v2,1],bc))]
    NR=cy.add(cy.scale(U[0],t),U[1]);NS=cy.add(V[1],cy.scale(V[2],g))
    xi=NR[0]/NR[1];eta=NS[0]/NS[1];p=xi+eta;q=xi*eta;w=p+4-sum(rates)
    dz=cy.mul([0,1],cy.mul([1+z,2,1],[1+z,2,1]));Q=[q,p,1]
    residual=cy.add(cy.mul([w,1],cy.mul(a,b)),cy.scale(cy.mul(dz,Q),-1))
    generators=[cy.mul(b,x)for x in U]+[cy.mul(a,x)for x in V]+[cy.mul(V[j],U[i])for j in range(3)for i in range(3)]
    six=lambda q:(q+[0]*6)[:6]
    return [six(x)for x in generators],six(residual),w,xi,eta,NR[1]*NS[1]

def actual(rates,arcs,fb,w):
    ac,ab,ad,ae,bc,bb,bd,be=arcs;r=fb[:3];f=fb[3:6];D=fb[6:]
    G=[[F(0)for _ in range(7)]for _ in range(7)]
    for i,x in enumerate((*rates[:3],w,*rates[3:])):G[i][i]=-x
    for i in range(6):G[i][i+1]=F(1)
    for i,j,x in ((0,2,ac),(1,0,ab),(2,0,ad),(2,1,ae),(4,6,bc),(5,4,bb),(6,4,bd),(6,5,be)):G[i][j]=x
    for j in range(3):G[3][j]=r[j]
    for i in range(3):
        G[4+i][3]=f[i]
        for j in range(3):G[4+i][j]=D[3*i+j]
    return G

def determinant(G):
    return base.det_poly([[([-G[i][j],F(1)]if i==j else[-G[i][j]])for j in range(7)]for i in range(7)])

def direct_check(rates,arcs,endpoints,fb,z):
    M,b,w,xi,eta,lead=data(z,rates,arcs,endpoints);G=actual(rates,arcs,fb,w);char=determinant(G)
    dz=base.pol_mul([F(0),F(1)],base.pol_mul([1+z,F(2),F(1)],[1+z,F(2),F(1)]));Q=base.pol_mul([xi,F(1)],[eta,F(1)])
    target=base.pol_mul(dz,Q);res=base.pol_add(char,[-x for x in target]);pred=[b[j]-sum(M[i][j]*fb[i]for i in range(15))for j in range(6)]
    assert res[:6]==pred and all(x==0 for x in res[6:])
    beta=[endpoints[0],F(1),F(0),F(0),F(0),F(0),F(0)];gamma=[F(0)]*5+[F(1),endpoints[1]]
    pencil=[[([-G[i][j],F(1)]if i==j else[-G[i][j]])for j in range(7)]for i in range(7)]
    for i in range(7):
        for j in range(7):pencil[i][j]=base.pol_add(pencil[i][j],[gamma[i]*beta[j]])
    num=base.pol_add(base.det_poly(pencil),[-x for x in char])
    while len(num)>3 and num[-1]==0:num.pop()
    assert num==[lead*x for x in Q]
    return G,w,xi,eta,lead,char,target

def verify(rates,arcs,endpoints,fb,z):
    G,w,xi,eta,lead,char,target=direct_check(rates,arcs,endpoints,fb,z)
    assert char==target and min(w,xi,eta,lead)>0
    K=C*((C+1)**2+z)**2;beta=[endpoints[0],F(1),F(0),F(0),F(0),F(0),F(0)];gamma=[F(0)]*5+[K/lead,K*endpoints[1]/lead]
    A=[[(C if i==j else F(0))-G[i][j]for j in range(7)]for i in range(7)];h=bal.solve_square(A,gamma)
    assert h is not None and all(x>0 for x in h)
    T=[[(G[i][j]-(C if i==j else 0))*h[j]/h[i]for j in range(7)]for i in range(7)]
    alpha=[beta[i]*h[i]for i in range(7)];omega=[gamma[i]/h[i]for i in range(7)]
    assert sum(alpha)==1 and all(x>=0 for x in alpha+omega)
    for i in range(7):assert all(T[i][j]>=0 for j in range(7) if i!=j) and sum(T[i])+omega[i]==0
    return {'z':str(z),'rates':list(map(str,rates)),'arcs':list(map(str,arcs)),'endpoints':list(map(str,endpoints)),
      'feedback':list(map(str,fb)),'w':str(w),'xi':str(xi),'eta':str(eta),'h':list(map(str,h)),
      'G':[[str(x)for x in row]for row in G], 'alpha':list(map(str,alpha)),
      'T':[[str(x)for x in row]for row in T],'omega':list(map(str,omega)),
      'checks':['full actual Fraction determinant and adjugate','positive h, exact row sums, alpha, exits','Hurwitz Q and shift']}

def project(x):
    for denom in (1000,10000,100000):
        rates=[F(round(float(v)*denom),denom)for v in x[:6]];arcs=[F(round(float(v)*denom),denom)for v in x[6:14]]
        ends=[F(round(float(v)*denom),denom)for v in x[14:16]];free=[F(round(float(v)*denom),denom)for v in x[16:]]
        M,b,w,xi,eta,lead=data(Z,rates,arcs,ends)
        if min(w,xi,eta,lead)<=0 or not all(a>0 for a in rates):continue
        choices=sorted(combinations(range(15),6),key=lambda choose:-sum(float(free[i])for i in choose))
        for choose in choices:
            other=[i for i in range(15)if i not in choose]
            rhs=[b[j]-sum(M[i][j]*free[i]for i in other)for j in range(6)]
            sol=bal.solve_square([[M[i][j]for i in choose]for j in range(6)],rhs)
            if sol is None:continue
            fb=free[:]
            for j,a in zip(choose,sol):fb[j]=a
            if all(x>=0 for x in fb):
                try:return verify(rates,arcs,ends,fb,Z)
                except AssertionError:continue
    return None

def fun(x):
    M,b,w,xi,eta,lead=data(float(Z),x[:6],x[6:14],x[14:16]);M=np.asarray(M,float).T;b=np.asarray(b,float);fb=x[16:]
    return np.r_[(M@fb-b)/(1+np.abs(b)+np.abs(M)@fb),min(w,0),min(xi,0),min(eta,0)]

def main():
    # One dense exact rational equivalence check is program-validation evidence,
    # not proof of a universal Schur formula and not an optimization witness.
    rates=[F(3,2),F(5,4),F(7,6),F(8,7),F(9,8),F(10,9)]
    arcs=[F(j+1,20)for j in range(8)];ends=[F(1,5),F(1,4)];fb=[F(j+1,100)for j in range(15)]
    direct_check(rates,arcs,ends,fb,Z)
    start=time.monotonic();runs=[];best=None;witness=None
    lower=np.array([.05]*6+[0.]*25);upper=np.array([10.]*6+[10.]*8+[40.]*2+[100.]*15)
    old=json.loads((ROOT/'frontier-20261028-ph7-balanced-cyclic-search-result.json').read_text())['best_parameters']
    oldfb=old[16:];seed=np.r_[old[:16],oldfb[:6],*[x for d in oldfb[6:9]for x in (d,0.,0.)]]
    for j in range(LIMIT):
        if time.monotonic()-start>WALL:break
        if j==0:x0=np.maximum(seed,1e-10)
        elif j<4:x0=np.clip(seed+RNG.normal(0,.08,31)*np.maximum(.1,np.abs(seed)),lower+1e-10,upper-1e-10)
        else:x0=np.r_[RNG.uniform(.6,2.2,6),RNG.uniform(.001,.4,8),RNG.uniform(.1,3,2),RNG.uniform(.001,2,15)]
        fit=least_squares(fun,x0,bounds=(lower,upper),max_nfev=EVALS,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        err=float(np.linalg.norm(fun(fit.x),ord=np.inf));runs.append({'attempt':j,'max_scaled_residual':err,'nfev':int(fit.nfev)})
        if best is None or err<best[0]:best=(err,fit.x.copy())
        if err<1e-8:
            witness=project(fit.x)
            if witness is not None:break
    report={'seed':20261111,'z':str(Z),'elapsed_seconds':time.monotonic()-start,'runs':runs,
      'best_scaled_residual':best[0] if best else None,'best_parameters':best[1].tolist() if best else None,'exact_witness':witness,
      'dense_rational_direct_determinant_and_numerator_selfcheck':'PASS',
      'topology':'balanced cyclic 3+1+3: all nine downstream-to-upstream cross-feedbacks; strictly contains prior three-entry search',
      'scope':'bounded numerical search only unless an exact witness is returned; no infeasibility or global claim'}
    out=ROOT/'frontier-20261028-ph7-full-balanced-cross-search-result.json'
    out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print('saved:',out)

if __name__=='__main__':main()
