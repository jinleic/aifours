#!/usr/bin/env python3
"""Seek exact positive-rational PH7 witnesses near the six-rate chart limit."""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from pathlib import Path
import json, numpy as np
ROOT=Path(__file__).resolve().parent
m=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
r=SourceFileLoader('ra',str(ROOT/'frontier-20261028-ph7-nonuniform-range-search.py')).load_module()
seed=np.array([float(F(x)) for x in ['1331/1000','341/250','1339/1000','33/25','257/250','132/125']])
ratios=[F(8201,10000),F(4101,5000),F(8203,10000),F(2051,2500),F(821,1000)]
POP=1024;GENS=5000;rng=np.random.default_rng(20261104);rows=[]
for z in ratios:
    m.Z=z; pop=np.clip(seed+rng.normal(0,.16,(POP,6)),.1,4); scores,_=r.numeric(pop,float(z));exact=None
    for gen in range(GENS):
        ids=rng.integers(0,POP,size=(3,POP));mut=np.clip(pop[ids[0]]+.75*(pop[ids[1]]-pop[ids[2]]),.1,4)
        mask=rng.random((POP,6))<.8;mask[np.arange(POP),rng.integers(0,6,size=POP)]=True
        trial=np.where(mask,mut,pop);ts,_=r.numeric(trial,float(z));keep=ts>scores;pop[keep]=trial[keep];scores[keep]=ts[keep]
        i=int(np.argmax(scores))
        if scores[i]>1e-6:
            for den in (1000,10000,100000,1000000):
                rates=[F(round(float(v)*den),den)for v in pop[i]];data=m.rational_family(rates)
                if data and all(data[k]>0 for k in ('p','q','w','B','C0','phi','D1','D2','D3')):
                    exact=m.actual_check(rates,data);break
            if exact:break
    i=int(np.argmax(scores)); rows.append({'z':str(z),'generations':gen+1,'best_minimum':float(scores[i]),
        'best_rates':pop[i].tolist(),'exact_witness':exact})
    print('z',z,'gens',gen+1,'best',float(scores[i]),'exact',bool(exact),flush=True)
    if exact:seed=np.array([float(F(x))for x in exact['rates']])
out=ROOT/'frontier-20261028-ph7-fine-band-search-result.json'
out.write_text(json.dumps({'seed':20261104,'population':POP,'generation_limit':GENS,'rows':rows,
 'scope':'one restricted chain family; no numerical miss is a proof'},indent=2)+'\n')
print('saved:',out)
