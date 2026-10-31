#!/usr/bin/env python3
"""Exact full-target X=L+gamma*A mixed-left SPD check for one rational gamma.

No conclusion about untested gamma, actual map kernel, or global optimality.
All Gram products use bounded int64 blocks and Python-integer accumulation.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('checked',ROOT/'frontier-20261028-level6-446-selected-accretivity-attempt.py')
checked=importlib.util.module_from_spec(spec);spec.loader.exec_module(checked)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--p',type=int,required=True);ap.add_argument('--q',type=int,required=True);args=ap.parse_args()
    g=Q(args.p,args.q);assert g>0;p,q=g.numerator,g.denominator
    out=ROOT/f'frontier-20261028-level6-446-gamma{p}over{q}-case-v1.json'
    if out.exists():raise FileExistsError(out)
    raw=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes();digest=hashlib.sha256(raw).hexdigest()
    assert digest=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);m=P['target_row_count'];n=P['whole_lowest_dim'];D=10368;assert (m,n)==(1780,162)
    L=np.zeros((m,n),dtype=np.int64);E=np.zeros((m,n),dtype=np.int64);K=np.zeros((m,n),dtype=np.int64)
    for i,row in enumerate(P['rows']):
        for z in row['entries']:
            j=z['column'];v=[Q(z[x])*D for x in ('L','E','K')]
            assert all(x.denominator==1 and abs(x)<2**62 for x in v)
            L[i,j],E[i,j],K[i,j]=map(int,v)
    ml=int(np.max(np.abs(L)));me=int(np.max(np.abs(E)));mk=int(np.max(np.abs(K)));assert 6*ml+me<2**63
    A=6*L+E;ma=int(np.max(np.abs(A)));mx=max(ml,ma,mk)
    block=max(1,min(m,(2**63-1)//(2*mx*mx)));assert 2*block*mx*mx<2**63
    mats={key:np.zeros((n,n),dtype=object) for key in ('H0','HL','HA','HK','HAK')}
    for i in range(0,m,block):
        l=L[i:i+block,:];a=A[i:i+block,:];k=K[i:i+block,:]
        mats['H0']+=(l.T@a+a.T@l).astype(object);mats['HL']+=(2*(l.T@l)).astype(object)
        mats['HA']+=(2*(a.T@a)).astype(object);mats['HK']+=(l.T@k+k.T@l).astype(object)
        mats['HAK']+=(a.T@k+k.T@a).astype(object)
    M0=q*mats['H0']+p*mats['HA'];ML=q*mats['HL']+p*mats['H0'];MK=q*mats['HK']+p*mats['HAK']
    R0=checked.sylvester(M0);print('gamma',g,'H0 positive',R0['positive_definite'],'prefix',R0['verified_positive_prefix'],flush=True)
    RL=None
    if R0['positive_definite']:
        RL=checked.sylvester(ML);print('gamma',g,'HL positive',RL['positive_definite'],'prefix',RL['verified_positive_prefix'],flush=True)
    ok=R0['positive_definite'] and RL is not None and RL['positive_definite']
    result={'degree':[4,4,6],'full_target_sha256':digest,'target_rows':m,'source_columns':n,
            'gamma':str(g),'positive_common_scale':q*D*D,'int64_block_size':block,
            'int64_per_block_abs_bound':2*block*mx*mx,'H0_check':R0,'HL_check':RL,
            'status':'BOTH_MIXED_LEFT_BASE_AND_LEADING_FORMS_PD' if ok else 'NO_BOTH_PD_FOR_THIS_GAMMA',
            'scope':'one specific rational gamma, full recorded target; no claim about untested gamma or a D3 kernel'}
    if ok:
        result['matrices_scaled']={name:[[str(v) for v in row] for row in M.tolist()] for name,M in [('H0',M0),('HL',ML),('HK',MK)]}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE',result['status'],out.name,flush=True)

if __name__=='__main__':main()
