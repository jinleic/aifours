#!/usr/bin/env python3
"""Independent full d4 orbit identity: reverse row matching/mode contraction.

Uses literal index maps built by the separate compressed/equality references,
full direct-canonical orbit partitions, reverse matching of identical physical
letters, reverse-axis modular contraction, and a freshly recomputed integer
height bound. No author verifier/core or owner global aggregation is run.
"""
import collections
import hashlib
import importlib.util
import itertools
import json
import math
import sys
import time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
G=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
S=ROOT/'frontier-20261028-d4-owner-literal-compressed-map-check.py'
L=ROOT/'frontier-20261028-independent-d4-localmaps-check.py'
E=ROOT/'frontier-20261028-d4-owner-literal-equality-map-check.py'
O=ROOT/'frontier-20261028-d4-owner-objective-cycle-check.py'
C=ROOT/'frontier-20261028-d4-canonical-orbit-audit.py'
R=ROOT/'frontier-20261028-d4-modular-crt-identity-proof-results.json'
PINS={G:'b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d',
      S:'b8b860ef27c89b87abb706258f9b27722694878e8f2e2251c189662823fc068c',
      L:'5ca678583772e2b904ede65b365f0efee53b82323f8ea42f0c71cf7f29b7da3b',
      E:'f3b5cbe975cf0844bc4206191143682ee0ae2d7d5247a4f2616d9cf2b45e8421',
      O:'e84a463dce2e313cbfd8daaa2bbe42f278ca96b02299efbb6f7978c0b9133f6c',
      C:'3688674985ed26f121a9bba51f3e8860b943feaddc3fa516b4e8e8a3f6a3a663',
      R:'f93866ea9171a6dd8b1ecd4ca78fbeb5afe86167aebdc02c701a721da9705d3b'}
OUT=ROOT/'frontier-20261028-d4-reverse-independent-crt-check-results.json'
PROGRESS=ROOT/'frontier-20261028-d4-reverse-independent-crt-progress.json'
LETTERS={'31':'aaab','22':'aabb','13':'bbba'};N=24**4

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def reverse_rule(a,b):
    row=a.split();col=b.split();unc=[];con=[]
    if len(row)!=4 or len(col)!=4:raise ValueError('bad row length')
    for j,(x,y) in enumerate(zip(row,col)):
        if x not in ('a','b','a*','b*') or y not in ('a','b','a*','b*') or x.endswith('*')!=y.endswith('*'):
            raise ValueError('invalid physical row pair')
        if x.endswith('*'):unc.append((y[0],('j',j)));con.append((x[0],('i',j)))
        else:unc.append((x[0],('i',j)));con.append((y[0],('j',j)))
    def match(pool,letters):
        pool=list(pool);out=[]
        for letter in letters:
            matches=[i for i,(value,_) in enumerate(pool) if value==letter]
            if not matches:raise ValueError('unbalanced physical factor')
            out.append(pool.pop(matches[-1])[1]) # deliberately opposite owner tie-break
        return tuple(out)
    matching=[f for f,L in LETTERS.items() if collections.Counter(c for c,_ in unc)==collections.Counter(L)]
    if len(matching)!=1 or collections.Counter(c for c,_ in unc)!=collections.Counter(c for c,_ in con):
        raise ValueError('unknown family')
    f=matching[0];kp=match(unc,LETTERS[f]);lp=match(con,LETTERS[f])
    physical=collections.Counter([(x[0],('i',j),x.endswith('*')) for j,x in enumerate(row)]+
                                 [(x[0],('j',j),not x.endswith('*')) for j,x in enumerate(col)])
    source=collections.Counter([(c,k,False) for c,k in zip(LETTERS[f],kp)]+
                               [(c,l,True) for c,l in zip(LETTERS[f],lp)])
    if physical!=source:raise ValueError('independent factor identity mismatch')
    return f,kp,lp

def rat(num,den,p):
    d=den%p
    if not d:raise ValueError('denominator divides prime')
    return (num%p)*pow(d,-1,p)%p

def mode_reverse(T,A,axis,p):
    if T.shape[axis]!=A.shape[1]:raise ValueError('local contraction dimension mismatch')
    if T.shape[axis]*(p-1)**2>=2**63:raise OverflowError('reverse axis int64 overflow')
    z=np.tensordot(A,T,axes=([1],[axis]))%p
    return np.moveaxis(z,0,axis)

def add_orbit(acc,labels,T,sign,p):
    if T.size!=N or len(labels)!=N or N*(p-1)>=2**63:raise OverflowError('orbit size/overflow')
    s=np.zeros(len(acc),dtype=np.int64);np.add.at(s,labels,np.asarray(T,dtype=np.int64).ravel())
    acc[:]=(acc+sign*s)%p

def main():
    st=time.monotonic();sys.set_int_max_str_digits(0)
    if any(sha(k)!=v for k,v in PINS.items()):raise ValueError('pinned input mismatch')
    loader=load('data_only_owner',G);site=load('independent_local_maps',S);local=load('independent_basis',L)
    eq=load('independent_equality_maps',E);obj=load('independent_objective_cycles',O);canon=load('independent_orbit_canonical',C)
    pkg,corr=loader.load_data();receipt=json.loads(R.read_text())
    if receipt['verdict']!='PASS' or receipt['corrected_data_sha256']!=loader.EXPECTED_CORRECTED:
        raise ValueError('invalid bound/prime receipt')
    primes=receipt['primes_tested']
    if len(primes)!=424 or len(set(primes))!=len(primes):raise ValueError('bad prime list')
    for p in primes:
        if p<3 or any(p%d==0 for d in range(2,math.isqrt(p)+1)):raise ValueError('nonprime modulus')
    matrices=[];lam=[];D=2**31
    for z in corr['matrices']:
        vals=[]
        for a,b in z['values']:
            a=int(a);b=int(b)
            if b<=0:raise ValueError('bad denominator')
            D=math.lcm(D,b);vals.append((a,b))
        matrices.append((int(z['r']),vals))
    for item in corr['equality_coefficients']:
        a=int(item['numerator']);b=int(item['denominator'])
        if b<=0:raise ValueError('bad lambda denominator')
        D=math.lcm(D,b);lam.append((item['group'],tuple(item['index']),a,b))
    if D!=int(receipt['denominator']) or any(D%p==0 for p in primes):raise ValueError('common denominator/prime mismatch')
    perms,ix,compose,invs=canon.permdata();label_cache={};orbits={}
    for f,letters in LETTERS.items():
        stab,maps=canon.maps_for(letters,perms,ix,compose);signature=tuple(stab)
        if signature not in label_cache:
            keys=canon.canonical_all(maps,invs)
            _,labels=np.unique(np.asarray(keys,dtype=np.int64),return_inverse=True)
            label_cache[signature]=labels
        labels=label_cache[signature];orbits[f]=(labels,int(labels.max())+1)
    if {f:v[1] for f,v in orbits.items()}!={'31':1142,'22':2391,'13':1142}:raise ValueError('independent canonical orbit count')
    groups={};sitecache={};auxcache={};eqcache={};factor_count=0
    for ti,t in enumerate(pkg['types']):
        for r,a in enumerate(t['rows']):
            for s,b in enumerate(t['rows']):
                f,kp,lp=reverse_rule(a,b);cut=t['modules'][0].split('|')[1]
                groups.setdefault((f,kp,lp,cut),[]).append((ti,r,s));factor_count+=1
                for mod in t['modules'][:3]:
                    k=(mod,kp,lp)
                    if k not in sitecache:sitecache[k]=np.asarray(site.ref_site(pkg,mod,kp,lp,local),dtype=np.int64)
                mod=t['modules'][3];k=(mod,kp,lp)
                if k not in auxcache:auxcache[k]=np.asarray(site.ref_aux(pkg,mod,kp,lp,local),dtype=np.int64)
    for group in pkg['eq_groups'].values():
        for part in group['parts']:
            for s in part['local']:
                key=(s[0],s[1],tuple(s[2]),s[3],tuple(s[4]))
                if key not in eqcache:
                    eqcache[key]=np.vstack([np.asarray(eq.rows_for(pkg,s,mk),dtype=np.int64).T for mk in s[4]])
    if len(groups)!=17 or factor_count!=1570:raise ValueError('physical group coverage mismatch')
    maxz=max(abs(a)*(D//b) for _,vals in matrices for a,b in vals)
    maxlam=max(abs(a)*(D//b) for _,_,a,b in lam)
    maxw=max(abs(int(x)) for t in pkg['types'] for row in t['W'] for x in row)
    maxlocal=max(int(np.max(np.abs(a))) for a in list(sitecache.values())+list(auxcache.values()))
    maxeq=max(int(np.max(np.abs(a))) for a in eqcache.values())
    blockfactor=sum(len(t['rows'])**2*t['r']**2*(len(t['W'])//len(t['rows']))**2 for t in pkg['types'])
    eqfactor=sum(len(pkg['eq_groups'][name]['parts']) for name,_,_,_ in lam)
    stsite=[2*4**obj.cycles(q)-4**obj.cycles(tuple(obj.TAU[q[j]] for j in range(4))) for q in perms]
    staux=[2**obj.cycles(tuple(obj.TAU[q[j]] for j in range(4))) for q in perms]
    maxobj=max(map(abs,stsite))**3*max(map(abs,staux))
    B=N*(blockfactor*maxz*maxw**2*maxlocal**4+eqfactor*maxlam*maxeq**4+maxobj*(D//2**31))
    total_product=math.prod(primes)
    if total_product<=2*B:raise ValueError('prime product insufficient for freshly recomputed bound')
    bygroup=collections.defaultdict(list)
    for name,index,a,b in lam:bygroup[name].append((index,a,b))
    def run(p,fault=False):
        Z=[]
        for n,vals in matrices:
            Z.append(np.asarray([rat(a,b,p) for a,b in vals],dtype=np.int64).reshape(n,n))
        acc={f:np.zeros(orbits[f][1],dtype=np.int64) for f in LETTERS}
        for (f,kp,lp,_),items in sorted(groups.items(),key=lambda z:str(z[0])):
            smods=sorted({m for ti,_,_ in items for m in pkg['types'][ti]['modules'][:3]})
            amods=sorted({pkg['types'][ti]['modules'][3] for ti,_,_ in items})
            offsets={};ds=0
            for m in smods:offsets[m]=ds;ds+=sitecache[(m,kp,lp)].shape[1]
            da=0
            for m in amods:offsets[m]=da;da+=auxcache[(m,kp,lp)].shape[1]
            As=np.hstack([sitecache[(m,kp,lp)] for m in smods])%p
            Aq=np.hstack([auxcache[(m,kp,lp)] for m in amods])%p
            block=np.zeros((ds,ds,ds,da),dtype=np.int64)
            sub={}
            for ti,r,s in items:sub.setdefault(tuple(pkg['types'][ti]['modules']),[]).append((ti,r,s))
            for mods,triples in sub.items():
                dims=[math.isqrt((auxcache if axis==3 else sitecache)[(m,kp,lp)].shape[1]) for axis,m in enumerate(mods)]
                if any(d*d!=(auxcache if axis==3 else sitecache)[(m,kp,lp)].shape[1] for axis,(d,m) in enumerate(zip(dims,mods))):
                    raise ValueError('nonsquare compressed map')
                n=math.prod(dims);Bsub=np.zeros((n,n),dtype=np.int64)
                for ti,r,s in triples:
                    t=pkg['types'][ti];rank=t['r'];W=t['W']
                    if rank*(p-1)**2>=2**63:raise OverflowError('Gram product overflow')
                    Wr=np.asarray([[int(x)%p for x in row] for row in W[r*n:(r+1)*n]],dtype=np.int64)
                    Ws=np.asarray([[int(x)%p for x in row] for row in W[s*n:(s+1)*n]],dtype=np.int64)
                    Bsub=(Bsub+(Wr@((Z[ti]@Ws.T)%p))%p)%p
                T=Bsub.reshape(dims+dims).transpose((0,4,1,5,2,6,3,7)).reshape([d*d for d in dims])
                sl=tuple(slice(offsets[m],offsets[m]+d*d) for m,d in zip(mods,dims))
                block[sl]=(block[sl]+T)%p
            for axis in (3,2,1,0):block=mode_reverse(block,Aq if axis==3 else As,axis,p)
            add_orbit(acc[f],orbits[f][0],block,-1,p)
        v=np.asarray([x%p for x in stsite],dtype=np.int64);vq=np.asarray([x%p for x in staux],dtype=np.int64)
        T=np.multiply.outer(np.multiply.outer(np.multiply.outer(v,v)%p,v)%p,vq)%p
        T=(T*pow(2**31,-1,p))%p;add_orbit(acc['31'],orbits['31'][0],T,1,p)
        for name,group in pkg['eq_groups'].items():
            for part in group['parts']:
                es=[]
                for s in part['local']:
                    k=(s[0],s[1],tuple(s[2]),s[3],tuple(s[4]));es.append(eqcache[k]%p)
                T=np.zeros(tuple(e.shape[0] for e in es),dtype=np.int64)
                for j,(index,a,b) in enumerate(bygroup[name]):
                    v=rat(a,b,p)
                    if fault and name=='aab' and j==0:v=(v+1)%p
                    T[index]=(T[index]+v)%p
                for axis in (3,2,1,0):T=mode_reverse(T,es[axis].T,axis,p)
                add_orbit(acc[part['family']],orbits[part['family']][0],T,-int(part['sign']),p)
        return {f:int(np.count_nonzero(v)) for f,v in acc.items()}
    tested=[];bad=[];first=run(primes[0]);mutated=run(primes[0],fault=True)
    if any(first.values()) or not any(mutated.values()):raise ValueError('first-prime identity or in-memory aab control failed')
    tested.append(primes[0])
    def progress():
        r={'state':'INCOMPLETE' if len(tested)<len(primes) else 'PRIMES_COMPLETE',
           'tested_count':len(tested),'last_prime':tested[-1],
           'prime_product_bits':math.prod(tested).bit_length(),'height_bound_bits':B.bit_length(),
           'bad_primes':bad,'elapsed_seconds':round(time.monotonic()-st,3),
           'scope':'Actual tested primes only; full exact rational zero requires all primes and product >2B.'}
        PROGRESS.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n');print(json.dumps(r,sort_keys=True),flush=True)
    progress()
    for p in primes[1:]:
        counts=run(p);tested.append(p)
        if any(counts.values()):bad.append({'prime':p,'residual_counts':counts});progress();break
        if len(tested)%50==0:progress()
    complete=len(tested)==len(primes) and not bad and math.prod(tested)>2*B
    if any(sha(k)!=v for k,v in PINS.items()):raise ValueError('pinned input changed during check')
    r={'kind':'independent_reverse_canonical_full_d4_crt_identity','archive_sha256':loader.EXPECTED_ARCHIVE,
       'corrected_data_sha256':loader.EXPECTED_CORRECTED,'prime_receipt_sha256':PINS[R],
       'prime_count':len(tested),'primes_tested':tested,'prime_product':str(math.prod(tested)),
       'prime_product_bits':math.prod(tested).bit_length(),'height_bound':str(B),'height_bound_bits':B.bit_length(),
       'bound_equals_prior_independent_receipt':B==int(receipt['height_bound']),
       'common_denominator_bits':D.bit_length(),'orbit_counts':{f:orbits[f][1] for f in LETTERS},
       'physical_row_pair_occurrences':factor_count,'row_pattern_groups':len(groups),
       'independent_site_maps':len(sitecache),'independent_aux_maps':len(auxcache),'independent_equality_specs':len(eqcache),
       'max_local_map':maxlocal,'max_equality_map':maxeq,'max_W':maxw,
       'block_factor':blockfactor,'equality_part_factor':eqfactor,'max_objective_numerator':maxobj,
       'first_prime_residuals':first,'in_memory_aab_plus_one_fault_residuals':mutated,
       'nonzero_residue_primes':bad,'product_exceeds_twice_fresh_bound':math.prod(tested)>2*B,
       'elapsed_seconds':round(time.monotonic()-st,3),
       'method':'Direct-canonical orbit labels; opposite matching of identical physical letters; explicit literal site/aux/equality maps and cycle objective; reverse-axis independent NumPy int64 contractions; recomputed full-data integer height bound; product of tested distinct primes>2B.',
       'scope':'Exact rational zero on all d4 source-orbit sums conditional on these implementations/runtime and bound proof. Physical original lift, PSD and all-d/operational/formal/human/family review remain separate.',
       'verdict':'PASS' if complete else ('FAIL' if bad else 'INCOMPLETE')}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k not in ('primes_tested','prime_product','height_bound')},sort_keys=True,indent=2),flush=True)
    return 0 if complete else (1 if bad else 2)


if __name__=='__main__':raise SystemExit(main())
