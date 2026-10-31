#!/usr/bin/env python3
"""Validate actual grouped d4 Gram aggregation against direct per-type traces.

At one denominator-safe prime, compare two exact tensor-product weighted sums
on every actual row-pattern group. No author core and no physical states. This
is a finite aggregation diagnostic, not a substitute for the full exact identity.
"""
import hashlib
import importlib.util
import math
import json
import time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
PIN='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
OUT=ROOT/'frontier-20261028-d4-grouped-versus-per-type-contraction-check-results.json'
PRIME=65521

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load():
    if sha(GLOBAL)!=PIN:raise ValueError('global helper pin mismatch')
    sp=importlib.util.spec_from_file_location('actual_global_source',GLOBAL)
    g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
    pkg,corr=g.load_data();return g,pkg,corr

def rat(num,den,p):
    d=int(den)%p
    if d==0:raise ValueError('denominator not invertible')
    return (int(num)%p)*pow(d,-1,p)%p

def weights(which,axis,p):
    return np.array([((j+1)**(axis+1)+3*(axis+1)+which*(2*j+1)**(axis+2))%p for j in range(24)],dtype=np.int64)

def projection(T,vectors,p):
    # Reverse axes avoids reindexing; each product is reduced modulo p.
    for axis in range(3,-1,-1):
        moved=np.moveaxis(T,axis,0);shape=moved.shape
        if shape[0]*(p-1)**2>=2**63:raise OverflowError('projection product overflow')
        T=((vectors[axis]@moved.reshape(shape[0],-1))%p).reshape(shape[1:])
    return int(T)

def main():
    st=time.monotonic();g,pkg,corr=load();p=PRIME
    if any(p%d==0 for d in range(2,math.isqrt(p)+1)):raise ValueError('modulus not prime')
    Z=[]
    for t,z in zip(pkg['types'],corr['matrices']):
        r=t['r']
        if z['r']!=r or len(z['values'])!=r*r:raise ValueError('matrix shape mismatch')
        Z.append(np.array([rat(a,b,p) for a,b in z['values']],dtype=np.int64).reshape(r,r))
    if len(Z)!=len(pkg['types']):raise ValueError('type count mismatch')
    groups={}
    for ti,t in enumerate(pkg['types']):
        for r,a in enumerate(t['rows']):
            for s,b in enumerate(t['rows']):
                f,kp,lp=g.literal_rule(a,b);cut=t['modules'][0].split('|')[1]
                groups.setdefault((f,kp,lp,cut),[]).append((ti,r,s))
    sitecache={};auxcache={};weightcache={};kcache={};reports=[];fault_detected=False
    for group,items in sorted(groups.items(),key=lambda z:str(z[0])):
        family,kp,lp,_=group
        smods=sorted({m for ti,_,_ in items for m in pkg['types'][ti]['modules'][:3]})
        amods=sorted({pkg['types'][ti]['modules'][3] for ti,_,_ in items})
        def smap(mod):
            key=(mod,kp,lp)
            if key not in sitecache:sitecache[key]=np.asarray(g.make_site_map(mod,kp,lp,pkg),dtype=np.int64)%p
            return sitecache[key]
        def amap(mod):
            key=(mod,kp,lp)
            if key not in auxcache:auxcache[key]=np.asarray(g.make_aux_map(mod,kp,lp,pkg),dtype=np.int64)%p
            return auxcache[key]
        offsets={};ds=0
        for mod in smods:offsets[mod]=ds;ds+=smap(mod).shape[1]
        da=0
        for mod in amods:offsets[mod]=da;da+=amap(mod).shape[1]
        As=np.hstack([smap(mod) for mod in smods]);Aa=np.hstack([amap(mod) for mod in amods])
        block=np.zeros((ds,ds,ds,da),dtype=np.int64);direct=[0,0]
        for ti,r,s in items:
            t=pkg['types'][ti];mods=tuple(t['modules'])
            dims=[math.isqrt((amap(mod) if axis==3 else smap(mod)).shape[1]) for axis,mod in enumerate(mods)]
            if any(d*d!=(amap(mod) if axis==3 else smap(mod)).shape[1] for axis,(d,mod) in enumerate(zip(dims,mods))):raise ValueError('nonsquare local map')
            n=math.prod(dims);rank=t['r'];W=t['W']
            if rank*(p-1)**2>=2**63 or n*n*(p-1)**2>=2**63:raise OverflowError('per-type product overflow')
            Wr=np.asarray([[int(x)%p for x in row] for row in W[r*n:(r+1)*n]],dtype=np.int64)
            Ws=np.asarray([[int(x)%p for x in row] for row in W[s*n:(s+1)*n]],dtype=np.int64)
            B=(((Wr@Z[ti])%p)@Ws.T)%p
            T=B.reshape(dims+dims).transpose((0,4,1,5,2,6,3,7)).reshape([d*d for d in dims])
            sl=tuple(slice(offsets[mod],offsets[mod]+d*d) for mod,d in zip(mods,dims))
            block[sl]=(block[sl]+T)%p
            for which in range(2):
                ck=(mods,kp,lp,which)
                if ck not in kcache:
                    local=[]
                    for axis,(mod,d) in enumerate(zip(mods,dims)):
                        mp=amap(mod) if axis==3 else smap(mod)
                        wk=(which,axis,mod,kp,lp)
                        if wk not in weightcache:weightcache[wk]=(weights(which,axis,p)@mp%p).reshape(d,d)
                        local.append(weightcache[wk])
                    K=local[0]
                    for L in local[1:]:K=np.kron(K,L)%p
                    kcache[ck]=K
                direct[which]=(direct[which]+int(np.sum((B*kcache[ck])%p,dtype=np.int64)) )%p
        grouped=[]
        for which in range(2):
            vectors=[weights(which,axis,p)@(Aa if axis==3 else As)%p for axis in range(4)]
            val=projection(block,vectors,p);grouped.append(val)
            if not fault_detected:
                choices=[next((i for i,x in enumerate(v) if x),None) for v in vectors]
                if all(x is not None for x in choices):
                    bad=block.copy();idx=tuple(choices);bad[idx]=(int(bad[idx])+1)%p
                    fault_detected=projection(bad,vectors,p)!=val
        reports.append({'family':family,'type_row_pairs':len(items),'direct':direct,'grouped':grouped,'match':direct==grouped})
        print('group',len(reports),'of',len(groups),'match',direct==grouped,'elapsed',round(time.monotonic()-st,2),flush=True)
    if sha(GLOBAL)!=PIN:raise ValueError('global helper changed during run')
    ok=len(groups)==17 and all(x['match'] for x in reports) and fault_detected
    r={'kind':'all_d4_grouped_versus_per_type_weighted_aggregation','prime':p,'prime_trial_division':'PASS',
       'archive_sha256':g.EXPECTED_ARCHIVE,'corrected_data_sha256':g.EXPECTED_CORRECTED,
       'global_helper_sha256':PIN,'row_pattern_groups':len(groups),'weight_tensors':2,
       'groups':reports,'one_tensor_entry_fault_detected':fault_detected,
       'elapsed_seconds':round(time.monotonic()-st,3),
       'method':'Compare independently arranged direct per-type Kronecker contractions against grouped offset/reshape tensor projection for two deterministic weights over ALL source words in each actual row-pattern group, using exact overflow-bounded prime arithmetic.',
       'scope':'Finite weighted aggregation diagnostic only: not an independent all-coefficient identity, physical state sample, corrected PSD, formal kernel, or separate model-family review.',
       'verdict':'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
