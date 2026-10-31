#!/usr/bin/env python3
"""Continuous marginal proposals on explicit three-syndrome FD supports."""
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
OUT=ROOT/'frontier-20261028-three-syndrome-nonuniform-search-result.json'

def main():
    raw=(ROOT/HELPER[0]).read_bytes()
    if sha256(raw).hexdigest()!=HELPER[1]:raise ValueError('HASH')
    spec=spec_from_file_location('mixedbase',ROOT/HELPER[0]);mod=module_from_spec(spec);spec.loader.exec_module(mod)
    rng=Random(2026102901);start=monotonic();results=[];witness=None
    for cover in mod.COVERS:
        if monotonic()-start>50:break
        Ts,pos=mod.model_geometry(cover);nb=mod.N
        def syndrome(word):
            z=0
            for j,T in enumerate(Ts):
                parity=0
                for v in T:
                    slot=[k for k,U in enumerate(Ts) if v in U].index(j);parity^=(word>>pos[v][slot])&1
                z|=parity<<j
            return z
        cosets=[[] for _ in range(16)]
        for w in range(4096):cosets[syndrome(w)].append(w)
        bad=set()
        for d in range(1,4096):
            active={v for v in range(1,11) if any(d>>b&1 for b in pos[v])}
            if any(not(set(nb[v])&active) for v in active):bad.add(d)
        triples=[(0,u,v) for u in range(1,16) for v in range(u+1,16) if u|v==15];rng.shuffle(triples)
        for triple in triples[:8]:
            if monotonic()-start>50:break
            Y=[y for y in cosets[triple[1]] if y not in bad];Z=[z for z in cosets[triple[2]] if z not in bad]
            rng.shuffle(Y);rng.shuffle(Z);pairs=[(y,z) for y in Y[:32] for z in Z[:32] if (y^z) not in bad];rng.shuffle(pairs)
            for y,z in pairs[:6]:
                W=[w for w in cosets[0] if (w^y) not in bad and (w^z) not in bad]+[y,z]
                mod.verify(W,pos)
                words=np.array(W,dtype=np.int32);labels=np.empty((len(W),10),dtype=np.int32)
                for i in range(10):
                    labels[:,i]=sum((((words>>b)&1)<<j) for j,b in enumerate(pos[i+1]))
                q=[]
                for i in range(10):
                    row=np.array([1.+.1*rng.random() for _ in range(1<<len(pos[i+1]))]);q.append(row/row.sum())
                maxscore=0.;steps=0
                for step in range(100):
                    score=np.ones(len(W))
                    for i in range(10):score*=q[i][labels[:,i]]**(2/3)
                    total=float(score.sum());maxscore=max(maxscore,total);steps+=1
                    if total>1+1e-9:
                        for scale in (10,100,1000,10000):
                            weights=[]
                            for row in q:
                                a=np.cbrt(row);weights.append([round(scale*x/max(a)) for x in a])
                            S=sum(prod(weights[i][int(labels[j,i])]**2 for i in range(10)) for j in range(len(W)))
                            D=prod(sum(x**3 for x in row)**2 for row in weights)
                            if S**3>D:
                                witness={'factors':cover,'triple':triple,'support_words':W,'weights':weights,'weighted_sum':str(S),'threshold':str(D),'scale':scale};break
                        if witness:break
                    if not total:break
                    new=[np.bincount(labels[:,i],weights=score,minlength=len(q[i]))/total for i in range(10)]
                    diff=max(float(np.max(np.abs(new[i]-q[i]))) for i in range(10));q=new
                    if diff<1e-9:break
                results.append({'factors':cover,'triple':triple,'support_size':len(W),'steps':steps,'max_score_float':maxscore})
                if witness or monotonic()-start>50:break
            if witness:break
        if witness:break
    out={'helper_sha256':HELPER[1],'cases':results,'witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'Continuous floating-point proposals on selected two-outsider supports. A strict integer witness, if found, needs independent exact support and polynomial checks. Finite failures prove nothing globally.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'supports':len(results),'iterations':sum(r['steps'] for r in results),'strict_witness':bool(witness),'elapsed_seconds':out['elapsed_seconds']},indent=2))


if __name__=='__main__':main()
