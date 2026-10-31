#!/usr/bin/env python3
"""Independent full orbit partition by explicit group canonicalization.

Uses complete left/right stabilizer pairs, site sorting and simultaneous
inversion, instead of the existing union-find algorithm. Compares every word
against the owner global checker's full label partition, not merely counts.
No physical state, certificate solve, or author code is used.
"""
import hashlib
import importlib.util
import itertools
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
HELP=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
EXPECT='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
OUT=ROOT/'frontier-20261028-d4-canonical-orbit-audit-results.json'
N=24**4


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def reference_module():
    if sha(HELP)!=EXPECT:raise ValueError('reference helper hash mismatch')
    spec=importlib.util.spec_from_file_location('owner_global_orbits',HELP)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

def permdata():
    perms=list(itertools.permutations(range(4)));ix={p:i for i,p in enumerate(perms)}
    def compose(a,b):return tuple(a[b[i]] for i in range(4))
    def inverse(a):
        v=[0]*4
        for i,k in enumerate(a):v[k]=i
        return tuple(v)
    inv=[ix[inverse(p)] for p in perms]
    return perms,ix,compose,inv


def maps_for(letters,perms,ix,compose):
    stab=[g for g in perms if all(letters[g[i]]==letters[i] for i in range(4))]
    # Explicitly enumerate the whole finite stabilizer on the left and right,
    # not generator graph traversal. Every group map is a 24-element table.
    maps=[[ix[compose(compose(g,p),h)] for p in perms] for g in stab for h in stab]
    return stab,maps


def canonical_all(maps,invs):
    out=[0]*N
    for code in range(N):
        z=code;d=z%24;z//=24;c=z%24;z//=24;b=z%24;a=z//24
        ai,bi,ci,di=invs[a],invs[b],invs[c],invs[d]
        best=N
        for m in maps:
            for x,y,z_,w in ((a,b,c,d),(ai,bi,ci,di)):
                u,v,wsite=m[x],m[y],m[z_]
                if u>v:u,v=v,u
                if v>wsite:v,wsite=wsite,v
                if u>v:u,v=v,u
                candidate=((u*24+v)*24+wsite)*24+m[w]
                if candidate<best:best=candidate
        out[code]=best
    return out


def compare(keys,labels):
    key2label={};label2key={};mismatch=0
    for k,raw_l in zip(keys,labels):
        l=int(raw_l)
        if k in key2label and key2label[k]!=l:mismatch+=1
        else:key2label[k]=l
        if l in label2key and label2key[l]!=k:mismatch+=1
        else:label2key[l]=k
    return mismatch,len(key2label),len(label2key)


def main():
    st=time.monotonic();ref=reference_module();perms,ix,compose,invs=permdata()
    by_stabilizer={};reports={}
    for f,letters in [('31','aaab'),('22','aabb'),('13','bbba')]:
        stab,maps=maps_for(letters,perms,ix,compose)
        signature=tuple(stab)
        if signature not in by_stabilizer:by_stabilizer[signature]=canonical_all(maps,invs)
        keys=by_stabilizer[signature]
        labels,refcount=ref.generate_orbits(letters)
        mism,actual,matched=compare(keys,labels)
        # In-memory one-word reassignment must break partition equivalence.
        other=next(i for i,k in enumerate(keys) if k!=keys[0])
        faulty=keys.copy();faulty[0]=keys[other]
        fault_mismatch,_,_=compare(faulty,labels)
        reports[f]={'words':N,'stabilizer_size':len(stab),'two_sided_maps':len(maps),
                    'canonical_count':actual,'reference_union_find_count':int(refcount),
                    'reference_labels_count':matched,'bidirectional_partition_mismatches':mism,
                    'one_word_reassignment_detected':fault_mismatch>0}
        print('family',f,'orbits',actual,'mismatches',mism,'elapsed',round(time.monotonic()-st,2),flush=True)
    expected={'31':1142,'22':2391,'13':1142}
    ok=all(v['canonical_count']==expected[f] and v['reference_union_find_count']==expected[f]
           and v['bidirectional_partition_mismatches']==0 and v['one_word_reassignment_detected']
           for f,v in reports.items())
    if sha(HELP)!=EXPECT:raise ValueError('reference helper changed during check')
    r={'kind':'independent_explicit_canonical_orbit_partition_audit',
       'reference_union_find_helper_sha256':EXPECT,'families':reports,
       'unique_stabilizer_partitions_evaluated':len(by_stabilizer),
       'mathematical_method':'For every 24^4 word, minimize over ALL left/right stabilizer pairs, sorted permutations of the three site factors and simultaneous inversion. Compare partitions in both directions to separately computed union-find labels.',
       'scope':'Full fixed-d4 source-orbit partition only; not certificate coefficients, PSD, physical q3 positivity, or a formal-kernel or independent-family review.',
       'elapsed_seconds':round(time.monotonic()-st,3),'verdict':'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
