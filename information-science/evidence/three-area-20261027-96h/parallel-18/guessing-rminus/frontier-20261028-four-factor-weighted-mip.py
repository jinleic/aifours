#!/usr/bin/env python3
"""Bounded integer-weighted mixed-alphabet FD search on four-factor covers.

Each vertex receives its bits from the four selected triangles. A support of
more than 256 words would have positive entropy-balance gap. MIP statuses are
not proofs; every incumbent is checked by exact neighbour lookups.
"""
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
from random import Random
import numpy as np

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-four-factor-weighted-mip-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
COVERS=((2,3,5,6),(1,3,6,7),(3,4,6,7),(3,5,6,7),(2,5,6,9),(3,4,7,10))


def model_geometry(factors):
    Ts=[TRI[t-1] for t in factors];positions={};k=0
    for v in range(1,11):
        positions[v]=[k+j for j in range(sum(v in T for T in Ts))];k+=len(positions[v])
    if k!=12 or any(not positions[v] for v in positions):raise ValueError('COVER')
    return Ts,positions


def verify(words,pos):
    if len(words)!=len(set(words)) or any(not 0<=w<4096 for w in words):raise ValueError('WORDS')
    for v in range(1,11):
        lookup={}
        for w in words:
            key=tuple((w>>j)&1 for u in N[v] for j in pos[u]);val=tuple((w>>j)&1 for j in pos[v])
            if key in lookup and lookup[key]!=val:raise ValueError('FD')
            lookup[key]=val
    return len(words)>256


def xor_seed(Ts,pos):
    out=[]
    for pattern in range(1<<8):
        w=0
        for t,T in enumerate(Ts):
            a=(pattern>>(2*t))&1;b=(pattern>>(2*t+1))&1
            for v,bit in zip(T,(a,b,a^b)):
                slot=pos[v][[j for j,U in enumerate(Ts) if v in U].index(t)]
                w|=bit<<slot
        out.append(w)
    if len(set(out))!=256 or verify(out,pos):raise ValueError('SEED')
    return out


def run_cover(factors,case):
    Ts,pos=model_geometry(factors);seed=xor_seed(Ts,pos);state=np.arange(4096,dtype=np.uint32)
    offsets={};ncol=4096
    for v in range(1,11):
        nb=[j for u in N[v] for j in pos[u]]
        for bit in pos[v]:offsets[(v,bit)]=(ncol,nb);ncol+=1<<len(nb)
    starts=[];inds=[];vals=[];upper=[]
    for v in range(1,11):
        for bit in pos[v]:
            off,nb=offsets[v,bit];patterns=np.zeros(4096,dtype=np.int32)
            for k,j in enumerate(nb):patterns|=((state>>j)&1).astype(np.int32)<<k
            for w in range(4096):
                value=(w>>bit)&1;starts.append(len(inds));inds.extend((w,off+int(patterns[w])))
                vals.extend((1.,-1. if value else 1.));upper.append(0. if value else 1.)
    # Full clique rows for maximal independent vertex sets.
    masks=[sum(1<<(u-1) for u in N[v]) for v in range(1,11)]
    independent=[I for I in range(1,1024) if all(not(I&masks[i]) for i in range(10) if I>>i&1)]
    maximal=[I for I in independent if not any(I!=J and I&J==I for J in independent)]
    clique_count=0
    for I in maximal:
        free=[j for v in range(1,11) if I>>(v-1)&1 for j in pos[v]];mask=sum(1<<j for j in free)
        for base in range(4096):
            if base&mask:continue
            starts.append(len(inds));z=mask
            while True:
                inds.append(base|z);vals.append(1.)
                if not z:break
                z=(z-1)&mask
            upper.append(1.);clique_count+=1
    rng=Random(2026102820+case);weights=[];score=np.ones(4096,dtype=np.int64)
    for v in range(1,11):
        k=len(pos[v]);row=[1+int(rng.random()<.35) for _ in range(1<<k)];weights.append(row)
        symbol=np.zeros(4096,dtype=np.int32)
        for j,bit in enumerate(pos[v]):symbol|=((state>>bit)&1).astype(np.int32)<<j
        score*=np.array([x*x for x in row],dtype=np.int64)[symbol]
    D=1
    for row in weights:D*=sum(x**3 for x in row)**2
    lp=highspy.HighsLp();lp.num_col_=ncol;lp.num_row_=len(starts);lp.col_cost_=np.concatenate((score.astype(float),np.zeros(ncol-4096)))
    lp.col_lower_=np.zeros(ncol);lp.col_upper_=np.ones(ncol);lp.integrality_=[highspy.HighsVarType.kInteger]*ncol
    lp.row_lower_=np.full(len(starts),-highspy.kHighsInf);lp.row_upper_=np.array(upper)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.array(starts+[len(inds)],np.int32)
    lp.a_matrix_.index_=np.array(inds,np.int32);lp.a_matrix_.value_=np.array(vals,float);lp.sense_=highspy.ObjSense.kMaximize
    initial=np.zeros(ncol);initial[seed]=1
    for v in range(1,11):
        for bit in pos[v]:
            off,nb=offsets[v,bit];seen={}
            for w in seed:
                p=sum(((w>>j)&1)<<k for k,j in enumerate(nb));val=(w>>bit)&1
                if p in seen and seen[p]!=val:raise ValueError('SEED_FD')
                seen[p]=val
            for p,val in seen.items():initial[off+p]=val
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',6.)
    h.passModel(lp);seedstatus=str(h.setSolution(ncol,np.arange(ncol,dtype=np.int32),initial));t0=monotonic();h.run();sol=h.getSolution()
    chosen=[w for w in range(4096) if sol.col_value[w]>.5] if sol.value_valid else []
    if chosen:verify(chosen,pos)
    S=sum(int(score[w]) for w in chosen);strict=S**3>D
    return {'factor_indices':factors,'integer_weights':weights,'weighted_sum':str(S),'threshold_product':str(D),'vertex_bit_positions':pos,'support_variables':4096,'decoder_variables':ncol-4096,
            'FD_implication_rows':4096*12,'clique_rows':clique_count,'seed_size':len(seed),'seed_status':seedstatus,
            'status_float_unverified':h.modelStatusToString(h.getModelStatus()),'elapsed_seconds':monotonic()-t0,
            'incumbent_size':len(chosen),'strict_integer_polynomial_witness':strict,'incumbent_words':chosen}


def main():
    start=monotonic();results=[];witness=None
    for cover in COVERS:
        if monotonic()-start>65:break
        result=run_cover(cover,len(results));results.append(result)
        if result['strict_integer_polynomial_witness']:witness=result;break
    out={'cover_representatives':COVERS,'cases':results,'strict_witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'Six representative mixed-alphabet integer-weighted MIP proposals only. No floating status proves nonexistence; any strict polynomial incumbent needs independently checked graph decoding and balancing.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('cases','strict_witness')},indent=2))
    print(json.dumps([{k:v for k,v in case.items() if k!='incumbent_words'} for case in results],indent=2))


if __name__=='__main__':main()
