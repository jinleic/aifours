#!/usr/bin/env python3
"""Exact independent CRT replay of BOTH gamma=1/5 negative determinants.

Uses all 1780 target rows, blockwise bounded int64 Gram products, Python-int
accumulation, and distinct small-prime modular determinants until their
product exceeds twice both rigorous row-L1 determinant bounds.  No floats.
"""
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('mod',ROOT/'frontier-20261028-level6-446-modular-determinant-replay.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)


def main():
    raw=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);m=P['target_row_count'];n=P['whole_lowest_dim'];D=10368;assert (m,n)==(1780,162)
    j0=json.loads((ROOT/'frontier-20261028-level6-446-gamma1over5-case-v1.json').read_text())
    j1=json.loads((ROOT/'frontier-20261028-level6-446-gamma1over5-leading-test-v1.json').read_text())
    assert j0['gamma']==j1['gamma']=='1/5' and not j0['H0_check']['positive_definite'] and not j1['HL_check']['positive_definite']
    assert j0['H0_check']['verified_positive_prefix']==j1['HL_check']['verified_positive_prefix']==161
    expected=[int(j0['H0_check']['pivot']),int(j1['HL_check']['pivot'])];assert all(x<0 for x in expected)
    L=np.zeros((m,n),dtype=np.int64);E=np.zeros((m,n),dtype=np.int64)
    for i,row in enumerate(P['rows']):
        for e in row['entries']:
            l,q=Q(e['L'])*D,Q(e['E'])*D;assert l.denominator==q.denominator==1 and abs(l)<2**62 and abs(q)<2**62
            L[i,e['column']]=int(l);E[i,e['column']]=int(q)
    ml=int(np.max(np.abs(L)));me=int(np.max(np.abs(E)));assert 6*ml+me<2**63
    A=6*L+E;ma=int(np.max(np.abs(A)));mx=max(ml,ma)
    block=max(1,min(m,(2**63-1)//(2*mx*mx)));assert 2*block*mx*mx<2**63
    H0=np.zeros((n,n),dtype=object);HL=np.zeros((n,n),dtype=object);HA=np.zeros((n,n),dtype=object)
    for i in range(0,m,block):
        l=L[i:i+block,:];a=A[i:i+block,:]
        H0+=(l.T@a+a.T@l).astype(object);HL+=(2*(l.T@l)).astype(object);HA+=(2*(a.T@a)).astype(object)
    matrices=[[[int(v) for v in row] for row in M.tolist()] for M in (5*H0+HA,5*HL+H0)]
    bounds=[math.prod(sum(abs(v) for v in row) for row in M) for M in matrices]
    assert all(abs(v)<=b for v,b in zip(expected,bounds))
    product=1;primes=[];limit=2*max(bounds)
    for p in range(32749,16384,-2):
        if not mod.prime(p):continue
        for M,d in zip(matrices,expected):assert mod.modular_det(M,p)==d%p,('residue mismatch',p)
        primes.append(p);product*=p
        if product>limit:break
    assert product>limit
    result={'degree':[4,4,6],'gamma':'1/5','full_target_sha256':digest,'target_rows':m,'source_columns':n,
            'scaled_baseline_determinant':str(expected[0]),'scaled_leading_determinant':str(expected[1]),
            'both_strictly_negative':True,'primes':primes,'prime_count':len(primes),
            'modulus_product_bits':product.bit_length(),'twice_max_row_L1_bound_bits':limit.bit_length(),
            'int64_block_size':block,'int64_per_block_abs_bound':2*block*mx*mx,
            'status':'PASS_EXACT_BOTH_NEGATIVE_DETERMINANTS_BY_CRT',
            'scope':'given full target tree/suffix pencil; no D3 kernel, arbitrary-left impossibility, formal or independent-model review'}
    out=ROOT/'frontier-20261028-level6-446-allgamma-obstruction-CRT-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact both 162x162 negative determinants:',len(primes),'primes, modulus bits',product.bit_length(),'bound bits',limit.bit_length(),out.name,flush=True)

if __name__=='__main__':main()
