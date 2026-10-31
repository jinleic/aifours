#!/usr/bin/env python3
"""All owner global-checker equality maps versus independent literal indices.

Constructs every used 3-rep site diagram, explicit partial-trace permutation
entries, auxiliary 3/4-rep stiefel/delete entries and Python integer module
contractions. The author core is not executed. Equality metadata/physical
validity and the global exact identity are checked separately.
"""
import collections
import hashlib
import importlib.util
import itertools
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
AUX=ROOT/'frontier-20261028-independent-d4-aux-equality-objective-check.py'
PIN_G='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
PIN_A='0949e4945fa5cd20bac6a5d4e976c6756f97a16de2fb5c6b20c759f60798e99c'
OUT=ROOT/'frontier-20261028-d4-owner-literal-equality-map-check-results.json'
PERMS=list(itertools.permutations(range(4)))

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def pentry(a,b,p):return int(all(a[p[j]]==b[j] for j in range(4)))

def trace_entry(a,b,p,slot,order,n):
    total=0
    for v in range(n):
        row=[None]*4;col=[None]*4;row[slot]=col[slot]=v
        for k,s in enumerate(order):row[s]=a[k];col[s]=b[k]
        total+=pentry(row,col,p)
    return total

def aux_entry(a,b,p,slot,order,kind):
    if kind=='del':return trace_entry(a,b,p,slot,order,2)
    if kind!='stiefel_aux':raise ValueError('unknown aux equality')
    row=[a[i] for i in order];col=[b[i] for i in order]
    return 2*pentry(a,b,p)-int(a[slot]==b[slot])*trace_entry(row,col,p,slot,order,2)

def label_from(mkey):
    f,l,r=mkey.split('|')[-1].split('_')
    return (int(f[1:]),() if l=='e' else tuple(map(int,l)),() if r=='e' else tuple(map(int,r)))

def vec3(key):
    pairs,top,bottom=key;out=collections.Counter()
    for vals in itertools.product(range(4),repeat=len(pairs)):
        row=[None]*3
        for (i,j),v in zip(pairs,vals):row[i]=row[j]=v
        for i,v in top:row[i]=v
        for i,v in bottom:row[i]=4+v
        if any(x is None or not 0<=x<4 for x in row):raise ValueError('invalid 3-rep diagram')
        out[tuple(row)]+=1
    return out

def compress(raw,C):
    n=len(raw);r=len(C[0])
    return [sum(int(C[i][a])*raw[i][j]*int(C[j][b]) for i in range(n) for j in range(n))
            for a in range(r) for b in range(r)]

def rows_for(pkg,spec,mk):
    side,slot,order,kind,_=spec;order=tuple(order);out=[]
    if side=='S':
        keys,C=pkg['diagrams'][(3,())][label_from(mk)];vectors=[vec3(k) for k in keys]
        for p in PERMS:
            raw=[[sum(wa*wb*trace_entry(a,b,p,slot,order,4)
                      for a,wa in va.items() for b,wb in vb.items()) for vb in vectors] for va in vectors]
            out.append(compress(raw,C))
    elif side=='A':
        J=pkg['aux'][mk];replicas=4 if kind=='stiefel_aux' else 3
        basis=list(itertools.product(range(2),repeat=replicas))
        if len(J)!=len(basis):raise ValueError('wrong aux basis dimension')
        for p in PERMS:
            raw=[[aux_entry(a,b,p,slot,order,kind) for b in basis] for a in basis]
            out.append(compress(raw,J))
    else:raise ValueError('wrong side')
    return out

def main():
    st=time.monotonic()
    if sha(GLOBAL)!=PIN_G or sha(AUX)!=PIN_A:raise ValueError('pinned helper mismatch')
    g=load('owner_global_eq',GLOBAL);aux=load('owner_reference_eq_aux',AUX);pkg,corr=g.load_data()
    specs={}
    for group in pkg['eq_groups'].values():
        for part in group['parts']:
            for s in part['local']:
                key=(s[0],s[1],tuple(s[2]),s[3],tuple(s[4]));specs[key]=s
    failures=[];controls={};counts={'site_module_permutation_maps':0,'aux_module_permutation_maps':0,
                                   'site_entries':0,'aux_entries':0};module_count=0
    for key,spec in sorted(specs.items(),key=lambda x:str(x[0])):
        side=spec[0];label='site' if side=='S' else 'aux';obs=g.eq_reference(spec,pkg,aux)
        if obs.shape[1]!=24:raise ValueError('wrong permutation axis')
        cursor=0
        for mk in spec[4]:
            ref=rows_for(pkg,spec,mk);n=len(ref[0]);module_count+=1
            if any(len(row)!=n for row in ref):raise ValueError('inconsistent reference shape')
            for pi,row in enumerate(ref):
                got=[int(obs[cursor+j,pi]) for j in range(n)]
                if row!=got:failures.append({'kind':label,'spec':str(key),'module':mk,'permutation':list(PERMS[pi])})
                counts[label+'_module_permutation_maps']+=1;counts[label+'_entries']+=n
                if label not in controls and row:
                    altered=list(got);altered[0]+=1;controls[label+'_single_entry_fault_detected']=altered!=row
                    controls[label]=True
            cursor+=n
        if cursor!=obs.shape[0]:raise ValueError('wrong compressed axis')
    controls.pop('site',None);controls.pop('aux',None)
    if sha(GLOBAL)!=PIN_G or sha(AUX)!=PIN_A:raise ValueError('helper changed during run')
    r={'kind':'all_used_owner_global_equality_maps_literal_index_audit',
       'archive_sha256':g.EXPECTED_ARCHIVE,'corrected_data_sha256':g.EXPECTED_CORRECTED,
       'owner_global_helper_sha256':PIN_G,'owner_aux_helper_sha256':PIN_A,
       'distinct_specs':len(specs),'source_modules':module_count,'counts':counts,
       'intentional_single_entry_fault_controls':controls,'failure_count':len(failures),'failures':failures,
       'elapsed_seconds':round(time.monotonic()-st,3),
       'method':'Independent explicit three-rep sparse site diagrams, full finite permutation partial traces, auxiliary Stiefel/delete entries and integer module compressions compared entrywise against the actual global-checker equality map.',
       'scope':'Actual d4 equality compressed local maps only. Original same-pair equality, source metadata binding, objective, orbit identity and PSD are separate. No author core or physical state sample; no formal kernel or independent model-family review.',
       'verdict':'PASS' if not failures and len(controls)==2 and all(controls.values()) else 'FAIL'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0 if r['verdict']=='PASS' else 1


if __name__=='__main__':raise SystemExit(main())
