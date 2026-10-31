#!/usr/bin/env python3
"""Exact symbolic correspondence of owner/reverse repeated-letter rules.

For every actual row-pair type, prove their ket/bra reassignments are family
stabilizers and verify the induced left/right permutation identity for all S4.
No physical state, source verifier or sampled numeric parameter is used.
"""
import hashlib
import importlib.util
import itertools
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
G=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
R=ROOT/'frontier-20261028-d4-reverse-independent-crt-check.py'
PIN_G='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
PIN_R='423e58d82a5be68486b8940199335b677f3d69cbb3ba33a37065e1bded42ebbc'
OUT=ROOT/'frontier-20261028-d4-reverse-rule-stabilizer-check-results.json'
LETTERS={'31':'aaab','22':'aabb','13':'bbba'};PERMS=list(itertools.permutations(range(4)))

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def preserve(p,L):return sorted(p)==list(range(4)) and all(L[p[i]]==L[i] for i in range(4))
def inverse(p):
    out=[0]*4
    for i,j in enumerate(p):out[j]=i
    return out

def main():
    st=time.monotonic()
    if sha(G)!=PIN_G or sha(R)!=PIN_R:raise ValueError('helper pin mismatch')
    g=load('owner_rule',G);rv=load('reverse_rule',R);pkg,corr=g.load_data()
    tested={};occurrences=0;failures=[];faults=[]
    for t in pkg['types']:
        for a in t['rows']:
            for b in t['rows']:
                occurrences+=1;pair=(a,b)
                if pair in tested:continue
                f,k,l=g.literal_rule(a,b);fr,kr,lr=rv.reverse_rule(a,b)
                if f!=fr or len(set(k))!=4 or len(set(l))!=4:raise ValueError('invalid factor rule')
                sigma=tuple(k.index(v) for v in kr);tau=tuple(l.index(v) for v in lr);L=LETTERS[f]
                if not preserve(sigma,L) or not preserve(tau,L):failures.append({'rows':pair,'kind':'nonstabilizer'})
                inv=inverse(tau)
                for p in PERMS:
                    q=tuple(sigma[p[inv[i]]] for i in range(4))
                    if sorted(q)!=list(range(4)) or any(kr[p[j]]!=k[q[tau[j]]] or lr[j]!=l[tau[j]] for j in range(4)):
                        failures.append({'rows':pair,'kind':'source_index_permutation','p':p})
                i,j=next((i,j) for i in range(4) for j in range(i+1,4) if L[i]!=L[j])
                bad=list(sigma);bad[i],bad[j]=bad[j],bad[i]
                if preserve(bad,L):faults.append(pair)
                tested[pair]={'family':f,'sigma':sigma,'tau':tau,'permutations_checked':len(PERMS)}
    if sha(G)!=PIN_G or sha(R)!=PIN_R:raise ValueError('helper changed')
    r={'kind':'all_d4_reverse_row_rules_exact_stabilizer_correspondence',
       'archive_sha256':g.EXPECTED_ARCHIVE,'corrected_data_sha256':g.EXPECTED_CORRECTED,
       'owner_rule_sha256':PIN_G,'reverse_rule_sha256':PIN_R,
       'type_row_pair_occurrences':occurrences,'distinct_physical_row_pairs':len(tested),
       'local_permutation_equalities_checked':len(tested)*len(PERMS),'failures':failures,
       'cross_letter_stabilizer_faults_undetected':faults,
       'elapsed_seconds':round(time.monotonic()-st,3),
       'method':'Derive actual sigma/tau by exact index-position matching, verify both preserve family letters, and check q=sigma*p*tau^-1 on all 24 source permutations for each distinct physical row pair.',
       'scope':'Exact source-row reindexing/orbit-stabilizer correspondence only; the independent CRT residual, height bound, physical PSD/lift and full theorem are separate.',
       'verdict':'PASS' if occurrences==1570 and len(tested)==17 and not failures and not faults else 'FAIL'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0 if r['verdict']=='PASS' else 1


if __name__=='__main__':raise SystemExit(main())
