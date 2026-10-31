#!/usr/bin/env python3
"""Further exact-witness search in the nonuniform PH7 chain family.

Float differential evolution proposes rate tuples. A result is called an
actual witness only after Fraction determinant, numerator, h and PH checks.
Misses establish nothing universal.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json, numpy as np
ROOT=Path(__file__).resolve().parent
m=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
r=SourceFileLoader('ra',str(ROOT/'frontier-20261028-ph7-nonuniform-range-search.py')).load_module()
prior=json.loads((ROOT/'frontier-20261028-ph7-seven-endpoint-refine-result.json').read_text())
seed=np.array([float(F(x)) for x in next(v['exact_witness']['rates'] for v in prior['rows'] if v['z']=='41/50')])
RATIOS=[F(821,1000),F(411,500),F(823,1000),F(103,125),F(33,40)]
POP=1280;GENS=6000;SEED=20261102;rng=np.random.default_rng(SEED);rows=[]
for z in RATIOS:
    m.Z=z;pop=rng.uniform(.1,4,(POP,6));pop[:POP//2]=np.clip(seed+rng.normal(0,.15,(POP//2,6)),.1,4)
    scores,vals=r.numeric(pop,float(z));exact=None
    for gen in range(GENS):
        ids=rng.integers(0,POP,size=(3,POP)); v=np.clip(pop[ids[0]]+.75*(pop[ids[1]]-pop[ids[2]]),.1,4)
        mask=rng.random((POP,6))<.8;mask[np.arange(POP),rng.integers(0,6,size=POP)]=True
        trial=np.where(mask,v,pop);ts,tv=r.numeric(trial,float(z));take=ts>scores
        pop[take]=trial[take];scores[take]=ts[take];vals[take]=tv[take];i=int(np.argmax(scores))
        if scores[i]>1e-6:
            for den in (1000,10000,100000):
                rates=[F(round(float(v)*den),den) for v in pop[i]]; data=m.rational_family(rates)
                if data and all(data[k]>0 for k in ('p','q','w','B','C0','phi','D1','D2','D3')):
                    exact=m.actual_check(rates,data);break
            if exact:break
    i=int(np.argmax(scores));rows.append({'z':str(z),'generations':gen+1,'numerical_best_minimum':float(scores[i]),
        'numerical_best_rates':pop[i].tolist(),'exact_witness':exact})
    print('z',z,'gens',gen+1,'best',float(scores[i]),'exact',bool(exact),flush=True)
    if exact:seed=np.array([float(F(x)) for x in exact['rates']])
out=ROOT/'frontier-20261028-ph7-further-endpoint-search-result.json'
out.write_text(json.dumps({'seed':SEED,'population':POP,'generation_limit':GENS,'rows':rows,
  'scope':'nonuniform 3+3 family only; optimizer misses are not an exclusion'},indent=2)+'\n')
print('saved:',out)
