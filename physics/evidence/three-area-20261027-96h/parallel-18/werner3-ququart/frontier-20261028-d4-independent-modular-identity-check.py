#!/usr/bin/env python3
"""Recompute ALL d4 orbit identities with an independent modular backend.

Uses the previously independently generated literal maps/orbits but a new
int64 modular tensor contraction, not FLINT fmpz global arithmetic and not
author code. Two finite primes provide a cross-check, not an exact rational
proof on their own. All int64 intermediate bounds are checked explicitly.
"""
import hashlib
import importlib.util
import json
import math
import sys
import time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
EXPECTED_GLOBAL='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
OUT=ROOT/'frontier-20261028-d4-independent-modular-identity-check-results.json'


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def prime(n):
    if n<2:return False
    for d in range(2,math.isqrt(n)+1):
        if n%d==0:return False
    return True


def choose_primes(corr,count):
    dens={int(den) for m in corr['matrices'] for _,den in m['values']}
    dens.update(int(x['denominator']) for x in corr['equality_coefficients'])
    chosen=[]
    for p in range(65521,60000,-1):
        if p%2 and prime(p) and all(d%p for d in dens):
            chosen.append(p)
            if len(chosen)==count:return chosen
    raise ValueError('not enough denominator-safe primes')


def mod_mode(T,A,axis,p):
    x=np.moveaxis(T,axis,0);shape=x.shape
    if shape[0]*(p-1)**2 >=2**63:raise OverflowError('matrix contraction could overflow int64')
    y=(A@x.reshape(shape[0],-1))%p
    return np.moveaxis(y.reshape((A.shape[0],)+shape[1:]),0,axis)


def add_orbits(acc,oid,T,sign,p):
    if len(oid)*(p-1)>=2**53:raise OverflowError('orbit sum bound exceeded')
    sums=np.zeros(len(acc),dtype=np.int64)
    np.add.at(sums,oid,np.asarray(T,dtype=np.int64).ravel())
    acc[:]=(acc+sign*sums)%p


def run_prime(g,pkg,corr,p,orbits,sitecache,auxcache,eqcache):
    def rat(n,d):
        d=int(d)%p
        if not d:raise ValueError('denominator not invertible')
        return (int(n)%p)*pow(d,-1,p)%p
    Z=[]
    for t,m in zip(pkg['types'],corr['matrices']):
        n=t['r']
        if m['r']!=n or len(m['values'])!=n*n:raise ValueError('matrix shape mismatch')
        Z.append(np.array([rat(a,b) for a,b in m['values']],dtype=np.int64).reshape(n,n))
    bygroup={}
    for x in corr['equality_coefficients']:
        bygroup.setdefault(x['group'],[]).append((tuple(x['index']),rat(x['numerator'],x['denominator'])))
    if set(bygroup)!=set(pkg['eq_groups']):raise ValueError('equality group mismatch')
    groups={}
    for ti,t in enumerate(pkg['types']):
        for r,a in enumerate(t['rows']):
            for s,b in enumerate(t['rows']):
                fam,kp,lp=g.literal_rule(a,b);cut=t['modules'][0].split('|')[1]
                groups.setdefault((fam,kp,lp,cut),[]).append((ti,r,s))
    acc={f:np.zeros(orbits[f][1],dtype=np.int64) for f in g.LETTERS}
    for group,items in sorted(groups.items(),key=lambda x:str(x[0])):
        fam,kp,lp,_=group
        smods=sorted({m for ti,_,_ in items for m in pkg['types'][ti]['modules'][:3]})
        amods=sorted({pkg['types'][ti]['modules'][3] for ti,_,_ in items})
        def site(m):
            key=(m,kp,lp)
            if key not in sitecache:sitecache[key]=g.make_site_map(m,kp,lp,pkg)
            return sitecache[key]
        def aux(m):
            key=(m,kp,lp)
            if key not in auxcache:auxcache[key]=g.make_aux_map(m,kp,lp,pkg)
            return auxcache[key]
        offsets={};off=0
        for m in smods:offsets[m]=off;off+=site(m).shape[1]
        ds=off;off=0
        for m in amods:offsets[m]=off;off+=aux(m).shape[1]
        da=off
        As=np.asarray(np.hstack([site(m) for m in smods]),dtype=np.int64)%p
        Aa=np.asarray(np.hstack([aux(m) for m in amods]),dtype=np.int64)%p
        block=np.zeros((ds,ds,ds,da),dtype=np.int64)
        sub={}
        for ti,r,s in items:sub.setdefault(tuple(pkg['types'][ti]['modules']),[]).append((ti,r,s))
        for mods,triples in sub.items():
            dims=[math.isqrt((aux(m) if i==3 else site(m)).shape[1]) for i,m in enumerate(mods)]
            n=math.prod(dims);B=np.zeros((n,n),dtype=np.int64)
            for ti,r,s in triples:
                t=pkg['types'][ti];z=Z[ti];rank=t['r'];W=t['W']
                if rank*(p-1)**2>=2**63:raise OverflowError('Gram multiplication could overflow')
                Wr=np.asarray([[int(x)%p for x in row] for row in W[r*n:(r+1)*n]],dtype=np.int64)
                Ws=np.asarray([[int(x)%p for x in row] for row in W[s*n:(s+1)*n]],dtype=np.int64)
                B=(B+(((Wr@z)%p)@Ws.T)%p)%p
            tensor=B.reshape(dims+dims).transpose((0,4,1,5,2,6,3,7)).reshape([d*d for d in dims])
            sl=tuple(slice(offsets[m],offsets[m]+d*d) for m,d in zip(mods,dims))
            block[sl]=(block[sl]+tensor)%p
        for axis in range(4):block=mod_mode(block,Aa if axis==3 else As,axis,p)
        add_orbits(acc[fam],orbits[fam][0],block,-1,p)
    auxmod=g.module('aux_literal_modular',ROOT/'frontier-20261028-independent-d4-aux-equality-objective-check.py')
    site=[auxmod.swap_trace_counts(4,x) for x in g.PERMS]
    qaux=[auxmod.swap_trace_counts(2,x) for x in g.PERMS]
    v=np.array([(2*x-y)%p for x,y in site],dtype=np.int64)
    q=np.array([y%p for _,y in qaux],dtype=np.int64)
    obj=np.multiply.outer(np.multiply.outer(np.multiply.outer(v,v)%p,v)%p,q)%p
    obj=(obj*pow(8*(2*4**3)**4,-1,p))%p
    add_orbits(acc['31'],orbits['31'][0],obj,1,p)
    for name,group in pkg['eq_groups'].items():
        for part in group['parts']:
            Es=[]
            for spec in part['local']:
                key=(spec[0],spec[1],tuple(spec[2]),spec[3],tuple(spec[4]))
                if key not in eqcache:eqcache[key]=g.eq_reference(spec,pkg,auxmod)
                Es.append(np.asarray(eqcache[key],dtype=np.int64)%p)
            T=np.zeros(tuple(e.shape[0] for e in Es),dtype=np.int64)
            for index,vv in bygroup[name]:T[index]=(T[index]+vv)%p
            for axis,e in enumerate(Es):T=mod_mode(T,e.T,axis,p)
            add_orbits(acc[part['family']],orbits[part['family']][0],T,-int(part['sign']),p)
    return {f:int(np.count_nonzero(v)) for f,v in acc.items()}


def main():
    start=time.monotonic();sys.set_int_max_str_digits(0)
    if hashlib.sha256(GLOBAL.read_bytes()).hexdigest()!=EXPECTED_GLOBAL:raise ValueError('global helper changed')
    g=load_module('independent_literal_helpers',GLOBAL)
    pkg,corr=g.load_data();primes=choose_primes(corr,2)
    orbits={f:g.generate_orbits(letters) for f,letters in g.LETTERS.items()}
    sitecache={};auxcache={};eqcache={};runs=[]
    for p in primes:
        t=time.monotonic();counts=run_prime(g,pkg,corr,p,orbits,sitecache,auxcache,eqcache)
        runs.append({'prime':p,'residual_nonzero_counts':counts,'elapsed_seconds':round(time.monotonic()-t,3)})
        print('prime',p,'nonzero',counts,'seconds',runs[-1]['elapsed_seconds'],flush=True)
    ok=all(all(v==0 for v in r['residual_nonzero_counts'].values()) for r in runs)
    receipt={'kind':'independent_modular_d4_full_identity_crosscheck','primes':primes,'runs':runs,
             'corrected_data_sha256':g.EXPECTED_CORRECTED,'source_archive_sha256':g.EXPECTED_ARCHIVE,
             'global_literal_map_helper_sha256':EXPECTED_GLOBAL,
             'orbit_counts':{f:orbits[f][1] for f in g.LETTERS},
             'site_map_cache_entries':len(sitecache),'aux_map_cache_entries':len(auxcache),'equality_map_cache_entries':len(eqcache),
             'method':'Independent NumPy int64 modular tensor aggregation with proven no-overflow bounds; source literal map/orbit generators reused from the independent exact checker. No author core imported.',
             'elapsed_seconds':round(time.monotonic()-start,3),'verdict':'PASS' if ok else 'FAIL',
             'scope':'Two finite-prime cross-checks only; not independent exact rational zero proof, not a formal theorem acceptance.'}
    OUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps(receipt,sort_keys=True,indent=2));return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
