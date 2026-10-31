#!/usr/bin/env python3
"""Exact-integer local support/weight search in four-factor mixed alphabets."""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from math import prod
from pathlib import Path
from random import Random
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
HELPER=('frontier-20261028-four-factor-weighted-mip.py','d832596e188a646bb0d340a0c8d676e5fe88c401e46514b4389c36cdeb8cdad0')
OUT=ROOT/'frontier-20261028-fourfactor-local-weighted-search-result.json'

def main():
    raw=(ROOT/HELPER[0]).read_bytes()
    if sha256(raw).hexdigest()!=HELPER[1]:raise ValueError('HELPER_HASH')
    spec=spec_from_file_location('mixedbase',ROOT/HELPER[0]);mod=module_from_spec(spec);spec.loader.exec_module(mod)
    rng=Random(2026102902);start=monotonic();records=[];witness=None
    for cover in mod.COVERS:
        Ts,pos=mod.model_geometry(cover);N=mod.N
        bad=[]
        for d in range(1,4096):
            active={v for v in range(1,11) if any(d>>b&1 for b in pos[v])}
            if any(not(set(N[v])&active) for v in active):bad.append(d)
        bad=np.array(bad,dtype=np.int32)
        for trial in range(40):
            if monotonic()-start>25:break
            weights=[[1+rng.randrange(3) for _ in range(1<<len(pos[v]))] for v in range(1,11)]
            D=prod(sum(x**3 for x in row)**2 for row in weights)
            words=np.arange(4096,dtype=np.int32);scores=np.ones(4096,dtype=np.int64)
            for v in range(1,11):
                label=sum((((words>>b)&1)<<j) for j,b in enumerate(pos[v]))
                scores*=np.array(weights[v-1],dtype=np.int64)[label]**2
            current=set(mod.xor_seed(Ts,pos))
            for step in range(100):
                bestdelta=0;best=None
                for z in rng.sample(range(4096),384):
                    if z in current:continue
                    victims=set((z^bad).tolist())&current
                    delta=int(scores[z])-sum(int(scores[w]) for w in victims)
                    if delta>bestdelta:bestdelta=delta;best=(z,victims)
                if best is None:break
                z,victims=best;current.difference_update(victims);current.add(z)
            mod.verify(list(current),pos);S=sum(int(scores[w]) for w in current);strict=S**3>D
            records.append({'factors':cover,'trial':trial,'steps':step+1,'support_size':len(current),'weighted_sum':str(S),'threshold':str(D),'strict_integer_witness':strict})
            if strict:witness={'factors':cover,'weights':weights,'support_words':sorted(current),'weighted_sum':str(S),'threshold':str(D)};break
        if witness or monotonic()-start>25:break
    out={'helper_sha256':HELPER[1],'cases':records,'witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'Bounded greedy local improvements; exact integer objective and neighbor-FD checks. No failure proves a global bound; any witness requires independent replay.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'trials':len(records),'strict_witness':bool(witness),'elapsed_seconds':out['elapsed_seconds']},indent=2))


if __name__=='__main__':main()
