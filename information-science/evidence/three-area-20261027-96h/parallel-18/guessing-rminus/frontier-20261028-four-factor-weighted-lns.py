#!/usr/bin/env python3
"""Bounded weighted local-neighborhood search on a 4-factor mixed alphabet."""
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
HELPER=('frontier-20261028-four-factor-cover-mip.py','e1308e6a85572dd52028ff4ef344ebff51b3fd112b94449ddbe4e5d8466c5fd1')
OUT=ROOT/'frontier-20261028-four-factor-weighted-lns-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy


def helper():
    raw=(ROOT/HELPER[0]).read_bytes()
    if sha256(raw).hexdigest()!=HELPER[1]:raise ValueError('HASH')
    spec=spec_from_file_location('mixedhelper',ROOT/HELPER[0]);mod=module_from_spec(spec);spec.loader.exec_module(mod);return mod


def forbidden(mod,pos):
    out=[]
    for x in range(1,4096):
        active={v for v in range(1,11) if any(x>>j&1 for j in pos[v])}
        if any(not set(mod.N[v])&active for v in active):out.append(x)
    return out


def choose(pool,score,seed,seconds):
    index={v:i for i,v in enumerate(pool)};starts=[];inds=[];vals=[];hi=[]
    for a,b in combinations(pool,2):
        if (a^b) in BAD:
            starts.append(len(inds));inds.extend((index[a],index[b]));vals.extend((1.,1.));hi.append(1.)
    lp=highspy.HighsLp();lp.num_col_=len(pool);lp.num_row_=len(starts)
    maximum=max(score[w] for w in pool);lp.col_cost_=np.array([score[w]/maximum for w in pool]);lp.col_lower_=np.zeros(len(pool));lp.col_upper_=np.ones(len(pool));lp.integrality_=[highspy.HighsVarType.kInteger]*len(pool)
    lp.row_lower_=np.full(len(starts),-highspy.kHighsInf);lp.row_upper_=np.array(hi);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],np.int32);lp.a_matrix_.index_=np.array(inds,np.int32);lp.a_matrix_.value_=np.array(vals,float);lp.sense_=highspy.ObjSense.kMaximize
    initial=np.array([int(w in seed) for w in pool],float);h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',seconds)
    h.passModel(lp);h.setSolution(len(pool),np.arange(len(pool),dtype=np.int32),initial);h.run();sol=h.getSolution()
    result=[pool[i] for i in range(len(pool)) if sol.col_value[i]>.5] if sol.value_valid else []
    return result,h.modelStatusToString(h.getModelStatus())


def main():
    global BAD
    start=monotonic();mod=helper();rng=Random(2026102821);allrecords=[];witness=None
    for case,cover in enumerate(mod.COVERS):
        if monotonic()-start>55:break
        Ts,pos=mod.model_geometry(cover);current=set(mod.xor_seed(Ts,pos));BAD=set(forbidden(mod,pos));universe=(1<<4096)-1
        conflicts=[sum(1<<(x^d) for d in BAD) for x in range(4096)]
        weights=[]
        for v in range(1,11):
            size=1<<len(pos[v]);weights.append([4+int(rng.random()<.5) for _ in range(size)])
        D=prod(sum(a**3 for a in row)**2 for row in weights);score=[]
        for w in range(4096):
            score.append(prod(weights[v-1][sum(((w>>j)&1)<<k for k,j in enumerate(pos[v]))]**2 for v in range(1,11)))
        initial=sum(score[w] for w in current);records=[]
        for trial in range(18):
            if monotonic()-start>55:break
            remove_count=(20,30,40,60)[trial%4];removed=set(rng.sample(sorted(current),min(remove_count,len(current))));keep=current-removed
            blocked=0
            for w in keep:blocked|=conflicts[w]|(1<<w)
            available=universe&~blocked;pool=[w for w in range(4096) if available>>w&1]
            if not removed<=set(pool):raise ValueError('POOL')
            if len(pool)>500:
                records.append({'trial':trial,'pool':len(pool),'status':'SKIPPED_POOL_LIMIT'});continue
            chosen,status=choose(pool,score,removed,.7);candidate=keep|set(chosen)
            if chosen:
                mod.verify(list(candidate),pos);old=sum(score[w] for w in current);new=sum(score[w] for w in candidate)
                if new>=old:current=candidate
            S=sum(score[w] for w in current);strict=S**3>D
            records.append({'trial':trial,'pool':len(pool),'status_float_unverified':status,'support_size':len(current),'weighted_sum':str(S),'strict_integer_witness':strict})
            if strict:
                witness={'factor_indices':cover,'integer_weights':weights,'weighted_sum':str(S),'threshold_product':str(D),'support_words':sorted(current)};break
        allrecords.append({'factor_indices':cover,'forbidden_differences':len(BAD),'integer_weights':weights,'threshold_product':str(D),
                           'initial_weighted_sum':str(initial),'records':records})
        if witness:break
    out={'helper_sha256':HELPER[1],'cases':allrecords,'strict_witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'Bounded local neighborhoods on selected factor covers and integer weights; failure is not a global bound. Any strict witness needs independent exact decoding and balancing.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'cases':len(allrecords),'trials':sum(len(x['records']) for x in allrecords),'strict_witness':bool(witness),'elapsed_seconds':out['elapsed_seconds']},indent=2))


if __name__=='__main__':main()
