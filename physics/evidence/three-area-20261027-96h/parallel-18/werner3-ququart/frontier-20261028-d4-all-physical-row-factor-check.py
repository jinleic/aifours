#!/usr/bin/env python3
"""All used d4 Gram row-pair maps vs formal arbitrary-complex factors.

Checks the owner exact-global checker's literal row-family mapping for every
actual single/coupled d4 block against independently constructed symbolic
factor multisets, plus a cross-letter index fault control. No physical input
is chosen; no author verifier/core is executed.
"""
import collections
import hashlib
import importlib.util
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
EXPECT='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
OUT=ROOT/'frontier-20261028-d4-all-physical-row-factor-check-results.json'
LETTERS={'31':'aaab','22':'aabb','13':'bbba'}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load():
    if sha(GLOBAL)!=EXPECT:raise ValueError('global helper hash mismatch')
    spec=importlib.util.spec_from_file_location('owner_global_rows',GLOBAL)
    g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
    pkg,corr=g.load_data()
    return g,pkg,corr

def physical_factors(a,b):
    r=a.split();s=b.split()
    if len(r)!=4 or len(s)!=4:raise ValueError('bad row length')
    if any(t not in ('a','b','a*','b*') for t in r+s):raise ValueError('bad token')
    if any(x.endswith('*')!=y.endswith('*') for x,y in zip(r,s)):raise ValueError('cut mismatch')
    # Component factors of row ket times conjugate of column ket.
    return collections.Counter([(x[0],('i',j),x.endswith('*')) for j,x in enumerate(r)] +
                               [(x[0],('j',j),not x.endswith('*')) for j,x in enumerate(s)])

def source_factors(f,kp,lp):
    return collections.Counter([(c,tuple(k),False) for c,k in zip(LETTERS[f],kp)]+
                               [(c,tuple(l),True) for c,l in zip(LETTERS[f],lp)])

def main():
    st=time.monotonic();g,pkg,corr=load();checked=0;fails=[];pairs={};kinds=collections.Counter()
    for ti,t in enumerate(pkg['types']):
        kinds[t['kind']]+=1
        for a in t['rows']:
            for b in t['rows']:
                f,kp,lp=g.literal_rule(a,b)
                direct=physical_factors(a,b);src=source_factors(f,kp,lp)
                if direct!=src:fails.append({'type_index':ti,'rows':[a,b],'family':f})
                checked+=1;pairs[(a,b)]=(f,kp,lp)
    fault_failures=[]
    for (a,b),(f,kp,lp) in pairs.items():
        letters=LETTERS[f]
        i,j=next((i,j) for i in range(4) for j in range(i+1,4) if letters[i]!=letters[j])
        bad=list(kp);bad[i],bad[j]=bad[j],bad[i]
        if source_factors(f,bad,lp)==physical_factors(a,b):fault_failures.append([a,b])
    if sha(GLOBAL)!=EXPECT:raise ValueError('global helper changed during run')
    r={'kind':'all_used_d4_gram_rows_formal_factor_closure',
       'archive_sha256':g.EXPECTED_ARCHIVE,'source_certificate_sha256':g.EXPECTED_CERT,
       'corrected_data_sha256':g.EXPECTED_CORRECTED,'reference_global_helper_sha256':EXPECT,
       'actual_type_count':len(pkg['types']),'type_kind_counts':dict(kinds),
       'all_type_row_pairs_checked':checked,'distinct_row_pairs':len(pairs),
       'formal_mismatches':fails,'cross_letter_fault_undetected':fault_failures,
       'method':'Factor each actual row ket times conjugate of column ket into symbolic a/b coordinate factors; compare to the exact-global helper family and ket/bra source indices as a multiset. Applies to all coordinates and complex vectors, including repetitions.',
       'scope':'Original physical factor-to-source-family index closure for every actual d4 Gram row pair only. Does not prove twirl/source span, objective, equality, exact residual, PSD, or independent model-family/formal review.',
       'elapsed_seconds':round(time.monotonic()-st,3),
       'verdict':'PASS' if not fails and not fault_failures else 'FAIL'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0 if r['verdict']=='PASS' else 1


if __name__=='__main__':raise SystemExit(main())
