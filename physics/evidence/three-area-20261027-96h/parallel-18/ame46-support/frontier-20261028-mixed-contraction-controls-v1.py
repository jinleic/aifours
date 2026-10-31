#!/usr/bin/env python3
"""Bounded modular controls for the repaired one-restricted-party proof.

Finite samples do not prove the universal complex rank assertions. They
exercise all 12 orientations, including mixed H/K covectors.
"""
import argparse
import collections
import importlib.util
import itertools
import json
from pathlib import Path
import sys

P=17;ROOT2=6;H=(1,2);K=(0,3,4,5)


def rank(mat):
    a=[row[:] for row in mat];r=0
    for c in range(6):
        pivot=next((j for j in range(r,6) if a[j][c]%P),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];inv=pow(a[r][c],-1,P)
        for j in range(r+1,6):
            v=a[j][c]*inv%P
            if v:
                for k in range(c,6):a[j][k]=(a[j][k]-v*a[r][k])%P
        r+=1
        if r==6:break
    return r


def contraction(tensor,C,B,A,D,cweights,u):
    mat=[[0]*6 for _ in range(6)]
    for x,(a,b) in tensor.items():
        coeff=(a+ROOT2*b)*cweights.get(x[C],0)*u[x[B]]
        mat[x[A]][x[D]]=(mat[x[A]][x[D]]+coeff)%P
    return mat


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('parser',type=Path)
    p.add_argument('structure_receipt',type=Path);p.add_argument('output',type=Path);args=p.parse_args()
    spec=importlib.util.spec_from_file_location('structure',args.parser);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    tensor,sha=mod.parse(args.table);cert=json.loads(args.structure_receipt.read_text())
    if cert['table_sha256']!=sha:raise ValueError('source binding mismatch')
    us=[x for x in itertools.product((0,1),repeat=6) if any(x)]
    ts=[x for x in itertools.product((0,1),repeat=4) if any(x)]
    ls=((1,0),(0,1),(1,1));h_hist=collections.Counter();k_hist=collections.Counter();counts=[0,0]
    for case in cert['cases']:
        C,B=case['restricted_C'],case['contracted_B'];A,D=case['remaining_A_D']
        match=dict(case['P_missing_pairs'])
        for lam in ls:
            cw={H[j]:lam[j] for j in range(2)}
            for u in us:
                r=rank(contraction(tensor,C,B,A,D,cw,u));counts[0]+=1;h_hist[r]+=1
                if r<2:raise ValueError(f'H-sector rank<2: C={C},B={B},lambda={lam},u={u},rank={r}')
        for t in ts:
            cw={K[j]:t[j] for j in range(4)};c0=next(K[j] for j in range(4) if t[j])
            for u in us:
                r=rank(contraction(tensor,C,B,A,D,cw,u));counts[1]+=1;k_hist[r]+=1
                if r==0:raise ValueError('unexpected zero K contraction')
                if r==1 and (u[1] or u[2] or u[match[c0]]):
                    raise ValueError(f'K rank-one containment failure: C={C},B={B},t={t},u={u}')
    result={'table_sha256':sha,'prime':P,'root2':ROOT2,'orientations':len(cert['cases']),
            'H_checks':counts[0],'H_rank_histogram':dict(sorted(h_hist.items())),
            'K_checks':counts[1],'K_rank_histogram':dict(sorted(k_hist.items())),
            'assertions':'H rank>=2; K nonzero and any rank-one u lies in source-matching hyperplane',
            'scope':'Finite F17 samples only; universal complex proof is separate.'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
