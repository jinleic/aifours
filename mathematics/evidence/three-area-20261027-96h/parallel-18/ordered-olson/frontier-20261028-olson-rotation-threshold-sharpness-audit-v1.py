#!/usr/bin/env python3
"""Independently audit sharpness words by negative-gap and parity accounting."""
import argparse
import hashlib
import json


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('input');ap.add_argument('--output',required=True);args=ap.parse_args()
    with open(args.input,'rb') as f:raw=f.read()
    data=json.loads(raw);out=[]
    for c in data['cases']:
        p=c['p'];w=c['word'];b=(-pow(2,-1,p))%p
        expected=[[0,1] for _ in range(2*p-1)]+[[b,0]]
        for j in range(1,p):expected.extend([[j,1],[b,0]])
        if w!=expected:raise ValueError('WRONG_WORD')
        masks=0
        for mask in range(1,1<<(p-1)):
            chosen=[j for j in range(1,p) if mask>>(j-1)&1];t=len(chosen)
            alt=sum(j*(1 if k%2==0 else -1) for k,j in enumerate(chosen))
            L=alt if t%2 else -alt
            if not 1<=L<=p-1:raise ValueError('TAIL_INTERVAL_BOUND')
            neg=sum((t+sum(j<=q for j in chosen))%2 for q in range(p))
            if neg!=L:raise ValueError('NEGATIVE_GAP_COUNT')
            masks+=1
        arithmetic=0
        for L in range(1,p):
            for qneg in range(L+1):
                for qpos in range(p-L+1):
                    k=qneg+qpos
                    if k%2:continue
                    C=2*L+qpos-qneg
                    if C%2 or not 1<=C<=2*p-1 or C%p==0:raise ValueError('EVEN_COEFFICIENT_OBSTRUCTION')
                    arithmetic+=1
        # No-tail selections require even nonzero k<=p-1, coefficient b*k.
        if any(b*k%p==0 for k in range(2,p,2)):raise ValueError('NO_TAIL_OBSTRUCTION')
        out.append({'p':p,'tail_subsets_checked':masks,'rotation_count_pairs_checked':arithmetic})
    # Positive control: insert ONE extra identity rotation. The first 2p-1 zeros + it have even reflection count? 
    # Instead insert an extra sigma0: then the first2p zero reflections explicitly give identity.
    c=data['cases'][0];p=c['p'];positive=[[0,1]]+c['word'];off,sgn=0,1
    for y,e in positive[:2*p]:off=(off+sgn*y)%p;sgn*=(-1 if e else 1)
    if (off,sgn)!=(0,1):raise ValueError('POSITIVE_CONTROL')
    result={'result':'PASS_INDEPENDENT_R_P_SHARPNESS_CONTROL','input_sha256':hashlib.sha256(raw).hexdigest(),
            'cases':out,'positive_control':'one extra zero reflection gives first2p zero-reflection identity',
            'scope':'exact parity proof diagnostics, not novelty or full original-word enumeration'}
    with open(args.output,'x',encoding='utf-8') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
    print(json.dumps({'result':result['result'],'cases':out},sort_keys=True))


if __name__=='__main__':main()
