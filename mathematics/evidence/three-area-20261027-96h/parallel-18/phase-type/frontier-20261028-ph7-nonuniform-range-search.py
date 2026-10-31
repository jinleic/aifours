#!/usr/bin/env python3
"""Seek exact PH7 witnesses beyond the fixed-chain obstruction.

A bounded numerical proposal search varies six actual principal rates. Each
positive-margin proposal is converted to rational parameters and sent through
the exact 7x7 determinant/numerator/PH-row verifier in the companion module.
A numerical fit or failed run alone is never an existence/exclusion proof.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
mod=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
POP=768; GENERATIONS=2500; LO=.10; HI=3.5; SEED=20261031
RATIOS=[F(79,100),F(4,5),F(13,16),F(5,6),F(17,20),F(7,8),F(8,9)]


def numeric(x,z):
    es=[np.ones(x.shape[0])]+[np.zeros(x.shape[0]) for _ in range(6)]
    for j in range(6):
        for k in range(j+1,0,-1): es[k]=es[k]+x[:,j]*es[k-1]
    a,b,c3,e4,e5,e6=es[1:]
    h0=b+4*a-a*a-6; L=b-4*a+10-2*z; N=4*h0+4-c3-b*(4-a)-4*z
    with np.errstate(divide='ignore',invalid='ignore',over='ignore'):
        p=N/L; q=(a-4)*p+h0-2*z; w=p+4-a
        B=p-x[:,0]-x[:,1]; C=q-x[:,0]*x[:,1]-x[:,0]*B
        phi=e4+c3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
        R2=e5+e4*w-(4+4*z)*q-(1+z)**2*p
        R1=e6+e5*w-(1+z)**2*q; R0=e6*w
        su=x[:,0]+x[:,1]+x[:,2]
        su2=x[:,0]*x[:,1]+x[:,0]*x[:,2]+x[:,1]*x[:,2]
        D1=R2-phi*su; D2=R1-phi*su2-(x[:,4]+x[:,5])*D1
        D3=R0-phi*x[:,0]*x[:,1]*x[:,2]-x[:,4]*x[:,5]*D1-x[:,5]*D2
        vals=np.stack([p,q,w,B,C,phi,D1,D2,D3],axis=1); score=np.min(vals,axis=1)
    return np.where(np.isfinite(score)&(np.abs(L)>1e-7),score,-1e100),vals


def main():
    rng=np.random.default_rng(SEED); summaries=[]; all_witness=[]; prior=None
    for z in RATIOS:
        mod.Z=z
        pop=rng.uniform(LO,HI,(POP,6))
        if prior is not None:
            pop[:POP//3]=np.clip(prior+rng.normal(0,.15,(POP//3,6)),LO,HI)
        scores,vals=numeric(pop,float(z)); exact=None
        for gen in range(GENERATIONS):
            ids=rng.integers(0,POP,size=(3,POP))
            trial=np.clip(pop[ids[0]]+.75*(pop[ids[1]]-pop[ids[2]]),LO,HI)
            mask=rng.random((POP,6))<.8; mask[np.arange(POP),rng.integers(0,6,size=POP)]=True
            trial=np.where(mask,trial,pop)
            ts,tv=numeric(trial,float(z)); keep=ts>scores
            pop[keep]=trial[keep]; scores[keep]=ts[keep]; vals[keep]=tv[keep]
            idx=int(np.argmax(scores))
            if scores[idx]>1e-5:
                for denom in (1000,10000,100000):
                    rates=[F(int(round(float(v)*denom)),denom) for v in pop[idx]]
                    exact_data=mod.rational_family(rates)
                    if exact_data and all(exact_data[k]>0 for k in ('p','q','w','B','C0','phi','D1','D2','D3')):
                        exact=mod.actual_check(rates,exact_data); break
                if exact is not None: break
        idx=int(np.argmax(scores)); prior=pop[idx].copy()
        row={'z':str(z),'generations':gen+1,'best_minimum':float(scores[idx]),
             'best_rates':pop[idx].tolist(),'best_coefficients':vals[idx].tolist(),'exact_witness':exact}
        summaries.append(row)
        if exact: all_witness.append(str(z))
        print('z',z,'gens',gen+1,'best_min',float(scores[idx]),'exact_witness',bool(exact),flush=True)
    report={'seed':SEED,'population':POP,'generation_limit':GENERATIONS,'rate_bounds':[LO,HI],
            'summaries':summaries,'certified_witness_ratios':all_witness,
            'scope':'specified nonuniform 3+3 chain; numerical failures do not prove impossibility'}
    out=ROOT/'frontier-20261028-ph7-nonuniform-range-search-result.json'
    out.write_text(json.dumps(report,indent=2)+'\n'); print('saved:',out)

if __name__=='__main__': main()
