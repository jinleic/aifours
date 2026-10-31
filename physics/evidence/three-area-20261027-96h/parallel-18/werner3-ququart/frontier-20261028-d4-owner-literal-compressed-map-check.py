#!/usr/bin/env python3
"""Compare every owner global-checker compressed local map with literal indices.

Reference builds sparse basis diagrams and explicit finite permutation entries,
then performs integer compression using ordinary Python loops. It imports no
author source or verifier. Row-index rules and package parser are shared with
the owner checker and have separately pinned full formal/source checks.
"""
import hashlib
import importlib.util
import itertools
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
LOCAL=ROOT/'frontier-20261028-independent-d4-localmaps-check.py'
PIN_G='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
PIN_L='5ca678583772e2b904ede65b365f0efee53b82323f8ea42f0c71cf7f29b7da3b'
OUT=ROOT/'frontier-20261028-d4-owner-literal-compressed-map-check-results.json'
PERMS=list(itertools.permutations(range(4)))

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def site_keys(pkg,mod):
    side,cut,label=mod.split('|')
    if side!='S':raise ValueError('wrong site side')
    cut=tuple(map(int,cut.split(','))) if cut else ()
    f,l,r=label.split('_')
    label=(int(f[1:]),() if l=='e' else tuple(map(int,l)),() if r=='e' else tuple(map(int,r)))
    return pkg['diagrams'][(4,cut)][label]

def compress(raw,C):
    n=len(raw);r=len(C[0])
    return [sum(int(C[i][a])*raw[i][j]*int(C[j][b]) for i in range(n) for j in range(n))
            for a in range(r) for b in range(r)]

def ref_site(pkg,mod,kp,lp,local):
    keys,C=site_keys(pkg,mod);vec=[local.explicit_vector(k,4) for k in keys];out=[]
    for p in PERMS:
        raw=[[sum(wa*wb*local.literal_index_entry(a,b,p,kp,lp)
                  for a,wa in va.items() for b,wb in vb.items()) for vb in vec] for va in vec]
        out.append(compress(raw,C))
    return out

def ref_aux(pkg,mod,kp,lp,local):
    J=pkg['aux'][mod];basis=list(itertools.product(range(2),repeat=4));out=[]
    if len(J)!=len(basis):raise ValueError('bad aux row count')
    for p in PERMS:
        raw=[[local.literal_index_entry(a,b,p,kp,lp) for b in basis] for a in basis]
        out.append(compress(raw,J))
    return out

def main():
    st=time.monotonic()
    if sha(GLOBAL)!=PIN_G or sha(LOCAL)!=PIN_L:raise ValueError('pinned helper mismatch')
    g=load('owner_literal',GLOBAL);local=load('separate_explicit_basis',LOCAL)
    pkg,corr=g.load_data();sites=set();auxs=set()
    for t in pkg['types']:
        for a in t['rows']:
            for b in t['rows']:
                for mod in t['modules'][:3]:sites.add((a,b,mod))
                auxs.add((a,b,t['modules'][3]))
    failures=[];counts={'site_permutation_maps':0,'aux_permutation_maps':0,'site_entries':0,'aux_entries':0}
    controls={}
    for side,items in [('site',sites),('aux',auxs)]:
        for a,b,mod in sorted(items):
            f,kp,lp=g.literal_rule(a,b)
            ref=ref_site(pkg,mod,kp,lp,local) if side=='site' else ref_aux(pkg,mod,kp,lp,local)
            observed=g.make_site_map(mod,kp,lp,pkg) if side=='site' else g.make_aux_map(mod,kp,lp,pkg)
            if observed.shape[0]!=24 or len(ref)!=24:raise ValueError('bad permutation axis')
            for pi,row in enumerate(ref):
                got=[int(x) for x in observed[pi]]
                if row!=got:failures.append({'kind':side,'rows':[a,b],'module':mod,'permutation':list(PERMS[pi])})
                counts[side+'_permutation_maps']+=1;counts[side+'_entries']+=len(row)
                if side not in controls and row:
                    altered=list(got);altered[0]+=1;controls[side+'_single_entry_fault_detected']=altered!=row
                    controls[side]=True
    controls.pop('site',None);controls.pop('aux',None)
    if sha(GLOBAL)!=PIN_G or sha(LOCAL)!=PIN_L:raise ValueError('pinned helper changed')
    r={'kind':'all_used_owner_global_compressed_maps_literal_index_audit',
       'archive_sha256':g.EXPECTED_ARCHIVE,'corrected_data_sha256':g.EXPECTED_CORRECTED,
       'global_helper_sha256':PIN_G,'independent_basis_helper_sha256':PIN_L,
       'distinct_site_rowpair_modules':len(sites),'distinct_aux_rowpair_modules':len(auxs),
       'counts':counts,'intentional_single_entry_fault_controls':controls,
       'failure_count':len(failures),'failures':failures,'elapsed_seconds':round(time.monotonic()-st,3),
       'method':'Independently reconstruct finite sparse diagram vectors and exact permutation entries; compress raw maps with Python integer loops; compare every entry of each actual owner global-checker site/aux map for every permutation.',
       'scope':'Actual d4 site/aux Gram compressed map interface only. Row-rule factor validity, equality maps, objective, full orbit identity and PSD are separate. No author core, physical state sampling, formal kernel or independent-family review.',
       'verdict':'PASS' if not failures and all(controls.values()) and len(controls)==2 else 'FAIL'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0 if r['verdict']=='PASS' else 1


if __name__=='__main__':raise SystemExit(main())
