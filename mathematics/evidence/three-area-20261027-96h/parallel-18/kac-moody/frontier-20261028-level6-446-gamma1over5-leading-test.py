#!/usr/bin/env python3
"""Check previously untested HL^X at X=L+A/5 on full 446 target."""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('checked',ROOT/'frontier-20261028-level6-446-selected-accretivity-attempt.py')
checked=importlib.util.module_from_spec(spec);spec.loader.exec_module(checked)


def main():
    raw=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);m=P['target_row_count'];n=P['whole_lowest_dim'];D=10368;assert (m,n)==(1780,162)
    L=np.zeros((m,n),dtype=np.int64);E=np.zeros((m,n),dtype=np.int64)
    for i,row in enumerate(P['rows']):
        for e in row['entries']:
            j=e['column'];l,q=Q(e['L'])*D,Q(e['E'])*D
            assert l.denominator==q.denominator==1 and abs(l)<2**62 and abs(q)<2**62
            L[i,j]=int(l);E[i,j]=int(q)
    ml=int(np.max(np.abs(L)));me=int(np.max(np.abs(E)));assert 6*ml+me<2**63
    A=6*L+E;ma=int(np.max(np.abs(A)))
    denominator=2*max(ml*ml,ml*ma)
    block=max(1,min(m,(2**63-1)//denominator));assert block*denominator<2**63
    H0=np.zeros((n,n),dtype=object);HL=np.zeros((n,n),dtype=object)
    for i in range(0,m,block):
        l=L[i:i+block,:];a=A[i:i+block,:]
        H0+=(l.T@a+a.T@l).astype(object);HL+=(2*(l.T@l)).astype(object)
    R=checked.sylvester(5*HL+H0)
    result={'degree':[4,4,6],'full_target_sha256':digest,'gamma':'1/5','common_positive_scale':5*D*D,
            'target_rows':m,'source_columns':n,'int64_block_size':block,'int64_per_block_abs_bound':block*denominator,
            'HL_check':R,'status':'HL_POSITIVE_AT_1OVER5' if R['positive_definite'] else 'HL_NOT_PD_AT_1OVER5',
            'scope':'ONLY leading symmetric form of X=L+A/5; no untested-gamma or original-map-kernel inference'}
    out=ROOT/'frontier-20261028-level6-446-gamma1over5-leading-test-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE',result['status'],'positive prefix',R['verified_positive_prefix'],out.name,flush=True)

if __name__=='__main__':main()
