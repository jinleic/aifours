#!/usr/bin/env python3
"""Bounded new nonuniform PH7 proposals at higher rational pole ratios.

Use the already independently checked six-rate same-matrix model; seeded
float optimization is only a proposal generator. Every positive candidate is
rationalized and verified by the exact actual-matrix verifier. No infeasibility
or optimal-endpoint claim follows from an optimizer miss.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json, numpy as np
ROOT=Path(__file__).resolve().parent
m=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
r=SourceFileLoader('range',str(ROOT/'frontier-20261028-ph7-nonuniform-range-search.py')).load_module()
prior=json.loads((ROOT/'frontier-20261028-ph7-nonuniform-range-search-result.json').read_text())
seed_rates=np.array([float(F(x)) for x in next(v['exact_witness']['rates'] for v in prior['summaries'] if v['z']=='13/16')])
RATIOS=[F(41,50),F(33,40),F(83,100),F(5,6),F(17,20),F(8,9)]
POP=1024;GENS=4000;SEED=20261101; rng=np.random.default_rng(SEED)
rows=[]
for z in RATIOS:
    m.Z=z; pop=rng.uniform(.1,4.0,(POP,6));pop[:POP//2]=np.clip(seed_rates+rng.normal(0,.24,(POP//2,6)),.1,4.0)
    scores,vals=r.numeric(pop,float(z)); exact=None
    for gen in range(GENS):
        ids=rng.integers(0,POP,size=(3,POP)); mutation=np.clip(pop[ids[0]]+.75*(pop[ids[1]]-pop[ids[2]]),.1,4.0)
        mask=rng.random((POP,6))<.8;mask[np.arange(POP),rng.integers(0,6,size=POP)]=True
        trial=np.where(mask,mutation,pop);ts,tv=r.numeric(trial,float(z));win=ts>scores
        pop[win]=trial[win];scores[win]=ts[win];vals[win]=tv[win];i=int(np.argmax(scores))
        if scores[i]>1e-5:
            for den in (100,1000,10000,100000):
                rates=[F(round(float(v)*den),den) for v in pop[i]]; data=m.rational_family(rates)
                if data and all(data[k]>0 for k in ('p','q','w','B','C0','phi','D1','D2','D3')):
                    exact=m.actual_check(rates,data);break
            if exact: break
    i=int(np.argmax(scores));row={'z':str(z),'generations':gen+1,'numerical_best_minimum':float(scores[i]),
       'numerical_best_rates':pop[i].tolist(),'exact_witness':exact};rows.append(row)
    print('z',z,'generations',gen+1,'best',float(scores[i]),'exact',bool(exact),flush=True)
    if exact:seed_rates=np.array([float(F(v)) for v in exact['rates']])
out=ROOT/'frontier-20261028-ph7-seven-endpoint-refine-result.json'
out.write_text(json.dumps({'seed':SEED,'population':POP,'generation_limit':GENS,'rows':rows,
    'scope':'numerical proposals only; exact Fraction-verified actual matrices if and only if exact_witness is non-null'},indent=2)+'\n')
print('saved:',out)
