#!/usr/bin/env python3
"""All 24^4 owner objective word numerators vs independent cycle formula.

The reference uses cycle decompositions of tau*p; owner inputs use the prior
fixed-basis swap-trace counter. No author source, target physical state, floats,
or certificate/global identity is used.
"""
import hashlib
import importlib.util
import itertools
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
AUX=ROOT/'frontier-20261028-independent-d4-aux-equality-objective-check.py'
PIN='0949e4945fa5cd20bac6a5d4e976c6756f97a16de2fb5c6b20c759f60798e99c'
OUT=ROOT/'frontier-20261028-d4-owner-objective-cycle-check-results.json'
PERMS=list(itertools.permutations(range(4)));TAU=(3,1,2,0)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def cycles(p):
    seen=set();n=0
    for j in range(4):
        if j not in seen:
            n+=1;k=j
            while k not in seen:seen.add(k);k=p[k]
    return n

def main():
    st=time.monotonic()
    if sha(AUX)!=PIN:raise ValueError('aux helper pin mismatch')
    spec=importlib.util.spec_from_file_location('owner_aux_trace_counter',AUX)
    a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
    counts4=[a.swap_trace_counts(4,p) for p in PERMS]
    counts2=[a.swap_trace_counts(2,p) for p in PERMS]
    f_site=[2*t-s for t,s in counts4];f_aux=[s for _,s in counts2]
    ref_site=[2*4**cycles(p)-4**cycles(tuple(TAU[p[j]] for j in range(4))) for p in PERMS]
    ref_aux=[2**cycles(tuple(TAU[p[j]] for j in range(4))) for p in PERMS]
    failures=[];fault_count=0;words=0
    for i,j,k,l in itertools.product(range(24),repeat=4):
        got=f_site[i]*f_site[j]*f_site[k]*f_aux[l]
        ref=ref_site[i]*ref_site[j]*ref_site[k]*ref_aux[l]
        if got!=ref:failures.append([i,j,k,l])
        # Deliberately omit the auxiliary swap in the owner objective.
        faulty=f_site[i]*f_site[j]*f_site[k]*counts2[l][0]
        fault_count+=faulty!=ref;words+=1
    denominator=8*(2*4**3)**4
    if sha(AUX)!=PIN:raise ValueError('helper changed during audit')
    r={'kind':'all_d4_owner_objective_words_independent_cycle_audit',
       'owner_aux_helper_sha256':PIN,'word_count':words,'denominator':denominator,
       'site_counts_match':f_site==ref_site,'aux_counts_match':f_aux==ref_aux,
       'numerator_mismatch_count':len(failures),'first_mismatches':failures[:10],
       'omitted_aux_swap_fault_mismatch_words':fault_count,
       'method':'Compare every literal owner fixed-basis objective numerator with independently computed permutation-cycle trace formula, and denominator 8*(2*4^3)^4.',
       'scope':'Actual d4 objective local map only. Original physical swap identity, Gram/equalities, all-orbit residual and PSD are separate; no physical state sample, author core, model-family or formal review.',
       'elapsed_seconds':round(time.monotonic()-st,3),
       'verdict':'PASS' if not failures and f_site==ref_site and f_aux==ref_aux and denominator==2**31 and fault_count>0 else 'FAIL'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0 if r['verdict']=='PASS' else 1


if __name__=='__main__':raise SystemExit(main())
