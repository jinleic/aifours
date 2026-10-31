#!/usr/bin/env python3
"""Bounded differential-evolution search in a six-rate PH7 chain family.

At the original z=8/9, allow three independent upstream and three independent
downstream diagonal rates. Exact characteristic matching fixes p,q,w,phi,D.
A numerical feasible point is never a proof: snap it to rational coordinates,
then verify literal 7x7 determinant, adjugate numerator, physical PH rows and
positivity using Fraction. Grid/optimizer failure excludes no continuous family.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
base=SourceFileLoader('frontier_exact',str(ROOT/'frontier-20261028-ph7-chain-search.py')).load_module()
Z=F(8,9); C=F(1)
POP=512; GENERATIONS=1800; SEED=20261028
LO=0.12; HI=4.0


def numeric(x):
    z=8.0/9.0
    a1=x.sum(axis=1)
    # Six-rate elementary coefficients, vectorized without an index table.
    es=[np.ones(x.shape[0])]+[np.zeros(x.shape[0]) for _ in range(6)]
    for j in range(6):
        for k in range(j+1,0,-1): es[k]=es[k]+x[:,j]*es[k-1]
    a,b,c3,e4,e5,e6=es[1:]
    h0=b+4*a-a*a-6
    L=b-4*a+10-2*z
    N=4*h0+4-c3-b*(4-a)-4*z
    with np.errstate(divide='ignore',invalid='ignore',over='ignore'):
        p=N/L; q=(a-4)*p+h0-2*z; w=p+4-a
        B=p-x[:,0]-x[:,1]; C0=q-x[:,0]*x[:,1]-x[:,0]*B
        phi=e4+c3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
        R2=e5+e4*w-(4+4*z)*q-(1+z)**2*p
        R1=e6+e5*w-(1+z)**2*q; R0=e6*w
        su=x[:,0]+x[:,1]+x[:,2]
        su2=x[:,0]*x[:,1]+x[:,0]*x[:,2]+x[:,1]*x[:,2]
        D1=R2-phi*su
        D2=R1-phi*su2-(x[:,4]+x[:,5])*D1
        D3=R0-phi*x[:,0]*x[:,1]*x[:,2]-x[:,4]*x[:,5]*D1-x[:,5]*D2
        values=np.stack([p,q,w,B,C0,phi,D1,D2,D3],axis=1)
        score=np.min(values,axis=1)
    score=np.where(np.isfinite(score)&(np.abs(L)>1.e-7),score,-1.e100)
    return score,values,L


def rational_family(rates):
    z=Z; es=[F(1)]+[F(0)]*6
    for x in rates:
        for k in range(6,0,-1): es[k]+=x*es[k-1]
    a,b,c3,e4,e5,e6=es[1:]
    h0=b+4*a-a*a-6; L=b-4*a+10-2*z
    if L==0: return None
    N=4*h0+4-c3-b*(4-a)-4*z
    p=N/L; q=(a-4)*p+h0-2*z; w=p+4-a
    u1,u2,u3,v1,v2,v3=rates
    B=p-u1-u2; C0=q-u1*u2-u1*B
    phi=e4+c3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
    R2=e5+e4*w-(4+4*z)*q-(1+z)**2*p
    R1=e6+e5*w-(1+z)**2*q; R0=e6*w
    D1=R2-phi*(u1+u2+u3)
    D2=R1-phi*(u1*u2+u1*u3+u2*u3)-(v2+v3)*D1
    D3=R0-phi*u1*u2*u3-v2*v3*D1-v3*D2
    return dict(p=p,q=q,w=w,B=B,C0=C0,phi=phi,D1=D1,D2=D2,D3=D3,L=L)


def actual_check(rates,v):
    u1,u2,u3,v1,v2,v3=rates
    G=[[F(0) for _ in range(7)] for _ in range(7)]
    for i,r in enumerate((u1,u2,u3,v['w'],v1,v2,v3)): G[i][i]=-r
    for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6)): G[i][j]=F(1)
    for i,key in ((4,'D1'),(5,'D2'),(6,'D3')): G[i][0]=v[key]
    G[6][3]=v['phi']
    def pencil(): return [[([(-G[i][j]),F(1)] if i==j else [-G[i][j]]) for j in range(7)] for i in range(7)]
    D=base.det_poly(pencil())
    Dz=base.pol_mul([F(0),F(1)],base.pol_mul([1+Z,F(2),F(1)],[1+Z,F(2),F(1)]))
    if D!=base.pol_mul(Dz,[v['q'],v['p'],F(1)]): raise AssertionError('7x7 determinant mismatch')
    K=C*((C+1)**2+Z)**2
    beta=[v['C0'],v['B'],F(1),F(0),F(0),F(0),F(0)]
    gamma=[F(0)]*6+[K]
    bumped=[[p[:] for p in row] for row in pencil()]
    for i in range(7):
        for j in range(7): bumped[i][j]=base.pol_add(bumped[i][j],[gamma[i]*beta[j]])
    N=base.pol_add(base.det_poly(bumped),[-x for x in D])
    while len(N)>3 and N[-1]==0: N.pop()
    if N!=[K*v['q'],K*v['p'],K]: raise AssertionError('adjugate numerator mismatch')
    A=[[(C if i==j else F(0))-G[i][j] for j in range(7)]+[gamma[i]] for i in range(7)]
    for j in range(7):
        pivot=next((i for i in range(j,7) if A[i][j]!=0),None)
        if pivot is None: raise AssertionError('singular normalizer')
        A[j],A[pivot]=A[pivot],A[j]; q=A[j][j]; A[j]=[x/q for x in A[j]]
        for i in range(7):
            if i!=j:
                q=A[i][j]; A[i]=[x-q*y for x,y in zip(A[i],A[j])]
    h=[row[-1] for row in A]
    if not all(x>0 for x in h): raise AssertionError('normalizer not positive')
    T=[[(G[i][j]-(C if i==j else 0))*h[j]/h[i] for j in range(7)] for i in range(7)]
    alpha=[beta[i]*h[i] for i in range(7)]; omega=[gamma[i]/h[i] for i in range(7)]
    if sum(alpha)!=1 or not all(x>=0 for x in alpha+omega): raise AssertionError('initial/exit')
    for i in range(7):
        if any(T[i][j]<0 for j in range(7) if j!=i) or sum(T[i])+omega[i]!=0: raise AssertionError('rows/Metzler')
    if not(v['p']>0 and v['q']>0): raise AssertionError('hidden stability')
    return {'rates':[str(x) for x in rates],'coefficients':{k:str(x) for k,x in v.items()},
            'G':[[str(x) for x in row] for row in G],'h':[str(x) for x in h],
            'alpha':[str(x) for x in alpha], 'T':[[str(x) for x in row] for row in T],
            'omega':[str(x) for x in omega],
            'exact_checks':['det(yI-G)=D_z(y)Q(y)','actual adjugate numerator=KQ',
                            'positive h and literal row ties','nonnegative alpha/exit and Metzler',
                            'Hurwitz from D_z and positive p,q']}


def main():
    rng=np.random.default_rng(SEED)
    pop=rng.uniform(LO,HI,(POP,6)); scores,vals,_=numeric(pop)
    bestlog=[]; found=None
    for gen in range(GENERATIONS):
        # Three independent draws per target; self-collisions are harmless to validity.
        ids=rng.integers(0,POP,size=(3,POP))
        mutant=pop[ids[0]]+0.75*(pop[ids[1]]-pop[ids[2]])
        mutant=np.clip(mutant,LO,HI)
        mask=rng.random((POP,6))<0.8
        mask[np.arange(POP),rng.integers(0,6,size=POP)]=True
        trial=np.where(mask,mutant,pop)
        ts,tv,_=numeric(trial); keep=ts>scores
        pop[keep]=trial[keep]; scores[keep]=ts[keep]; vals[keep]=tv[keep]
        imax=int(np.argmax(scores))
        if gen%300==0 or gen==GENERATIONS-1:
            bestlog.append({'generation':gen,'minimum_coefficient':float(scores[imax]),'rates':pop[imax].tolist()})
        if scores[imax]>0.000001:
            for denom in (1000,10000,100000,1000000):
                rates=[F(int(round(float(x)*denom)),denom) for x in pop[imax]]
                v=rational_family(rates)
                if v is not None and all(v[k]>0 for k in ('p','q','w','B','C0','phi','D1','D2','D3')):
                    found=actual_check(rates,v); break
            if found: break
    imax=int(np.argmax(scores)); report={'seed':SEED,'population':POP,'generation_limit':GENERATIONS,
        'completed_generations':gen+1,'rate_bounds':[LO,HI],'numerical_best_minimum':float(scores[imax]),
        'numerical_best_rates':pop[imax].tolist(),'numerical_best_coefficients':vals[imax].tolist(),
        'search_log':bestlog,'exact_witness':found,
        'scope':'one nonuniform 3+3 chain family; a numerical miss is not a proof or global exclusion'}
    out=ROOT/'frontier-20261028-ph7-nonuniform-search-result.json'
    out.write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report,indent=2)); print('saved:',out)

if __name__=='__main__': main()
