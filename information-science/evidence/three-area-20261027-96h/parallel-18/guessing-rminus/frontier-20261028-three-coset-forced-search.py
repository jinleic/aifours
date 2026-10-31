#!/usr/bin/env python3
"""Bounded weighted 3-syndrome search in four-factor mixed alphabets."""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from math import prod
from pathlib import Path
from random import Random
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
HELPER=('frontier-20261028-four-factor-weighted-mip.py','d832596e188a646bb0d340a0c8d676e5fe88c401e46514b4389c36cdeb8cdad0')
OUT=ROOT/'frontier-20261028-three-coset-forced-search-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy


def main():
    raw=(ROOT/HELPER[0]).read_bytes()
    if sha256(raw).hexdigest()!=HELPER[1]:raise ValueError('HELPER_HASH')
    spec=spec_from_file_location('mixedbase',ROOT/HELPER[0]);mod=module_from_spec(spec);spec.loader.exec_module(mod)
    rng=Random(2026102900);start=monotonic();records=[];witness=None
    for cover in mod.COVERS:
        if monotonic()-start>58:break
        Ts,pos=mod.model_geometry(cover);nb=mod.N
        def syndrome(word):
            z=0
            for j,T in enumerate(Ts):
                parity=0
                for v in T:
                    slot=[k for k,U in enumerate(Ts) if v in U].index(j)
                    parity^=(word>>pos[v][slot])&1
                z|=parity<<j
            return z
        cosets=[[] for _ in range(16)]
        for w in range(4096):cosets[syndrome(w)].append(w)
        if any(len(x)!=256 for x in cosets):raise ValueError('COSET_SIZE')
        bad=[]
        for d in range(1,4096):
            active={v for v in range(1,11) if any(d>>b&1 for b in pos[v])}
            if any(not(set(nb[v])&active) for v in active):bad.append(d)
        badset=set(bad)
        triples=[(0,u,v) for u in range(1,16) for v in range(u+1,16) if (u|v)==15]
        rng.shuffle(triples)
        for trial,triple in enumerate(triples[:5]):
            if monotonic()-start>58:break
            pool=sorted(w for j in triple for w in cosets[j]);index={w:i for i,w in enumerate(pool)}
            starts=[];inds=[]
            for w in pool:
                for d in bad:
                    u=w^d
                    if u>w and u in index:
                        starts.append(len(inds));inds.extend((index[w],index[u]))
            weights=[[1+rng.randrange(3) for _ in range(1<<len(pos[v]))] for v in range(1,11)]
            def score(w):return prod(weights[v-1][sum(((w>>b)&1)<<j for j,b in enumerate(pos[v]))]**2 for v in range(1,11))
            scores=[score(w) for w in pool];D=prod(sum(x**3 for x in row)**2 for row in weights)
            # Find a genuine three-coset seed. Translation by C_0 makes a
            # compatible triple contain 0 without loss of existence.
            ylist=[y for y in cosets[triple[1]] if y not in badset]
            zlist=[z for z in cosets[triple[2]] if z not in badset]
            pair=next(((y,z) for y in ylist for z in zlist if (y^z) not in badset),None)
            if pair is None:
                records.append({'factors':cover,'triple':triple,'trial':trial,'no_three_word_seed_exact':True,'strict_integer_witness':False,'represented_syndromes':[]});continue
            y,z=pair;seed=[w for w in cosets[0] if (w^y) not in badset and (w^z) not in badset]+[y,z];seedset=set(seed)
            mod.verify(seed,pos)
            edges=len(starts);lower=[-highspy.kHighsInf]*edges;upper=[1.]*edges
            for j in triple:
                starts.append(len(inds));inds.extend(index[w] for w in cosets[j]);lower.append(1.);upper.append(highspy.kHighsInf)
            lp=highspy.HighsLp();lp.num_col_=len(pool);lp.num_row_=len(starts)
            lp.col_cost_=np.array(scores,dtype=float)/max(scores);lp.col_lower_=np.zeros(len(pool));lp.col_upper_=np.ones(len(pool))
            lp.integrality_=[highspy.HighsVarType.kInteger]*len(pool);lp.row_lower_=np.array(lower);lp.row_upper_=np.array(upper)
            lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.array(starts+[len(inds)],dtype=np.int32)
            lp.a_matrix_.index_=np.array(inds,dtype=np.int32);lp.a_matrix_.value_=np.ones(len(inds));lp.sense_=highspy.ObjSense.kMaximize
            h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',1.8)
            h.passModel(lp);h.setSolution(len(pool),np.arange(len(pool),dtype=np.int32),np.array([int(w in seedset) for w in pool],float))
            h.run();sol=h.getSolution();chosen=[pool[i] for i in range(len(pool)) if sol.col_value[i]>.5] if sol.value_valid else seed
            mod.verify(chosen,pos)
            if len(set(syndrome(w) for w in chosen))!=3:raise ValueError('THREE_SYNDROMES_REQUIRED')
            S=sum(score(w) for w in chosen);strict=S**3>D;represented=sorted(set(syndrome(w) for w in chosen))
            rec={'factors':cover,'triple':triple,'trial':trial,'conflict_edges':edges,'status_float_unverified':h.modelStatusToString(h.getModelStatus()),
                 'support_size':len(chosen),'represented_syndromes':represented,'integer_weights':weights,'weighted_sum':str(S),'threshold':str(D),'strict_integer_witness':strict}
            records.append(rec)
            if strict:witness={**rec,'support_words':chosen};break
        if witness:break
    out={'helper_sha256':HELPER[1],'cases':records,'strict_witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'Bounded numerical MIP proposals forced to use all three syndromes, with exact neighbour-lookup and integer witness checks. No negative search result proves a no-go; a strict candidate requires independent replay.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'cases':len(records),'strict_witness':bool(witness),'represented_three':sum(len(r['represented_syndromes'])==3 for r in records),'elapsed_seconds':out['elapsed_seconds']},indent=2))


if __name__=='__main__':main()
