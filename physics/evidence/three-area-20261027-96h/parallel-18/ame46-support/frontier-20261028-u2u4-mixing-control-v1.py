#!/usr/bin/env python3
"""Exact 4-party control with nonmonomial blocks on BOTH 2D and 4D sectors."""
import argparse
import collections
import importlib.util
import json
from pathlib import Path
import sys


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def add(out,key,val):
    old=out.get(key,(0,0));new=(old[0]+val[0],old[1]+val[1])
    if new==(0,0):out.pop(key,None)
    else:out[key]=new


def apply(tensor,axis):
    # Unnormalized operator 2*(R(pi/4) on H ⊕ H4/2 on K).
    # The H block is sqrt(2)*[[1,1],[-1,1]]; K is the signed H4.
    hs=(1,2);ks=(0,3,4,5)
    hm=((1,1),(-1,1));km=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1))
    out={}
    for coord,(a,b) in tensor.items():
        old=coord[axis]
        if old in hs:
            j=hs.index(old)
            for i,level in enumerate(hs):
                sign=hm[i][j];dest=coord[:axis]+(level,)+coord[axis+1:]
                add(out,dest,(sign*2*b,sign*a))
        else:
            j=ks.index(old)
            for i,level in enumerate(ks):
                sign=km[i][j];dest=coord[:axis]+(level,)+coord[axis+1:]
                add(out,dest,(sign*a,sign*b))
    return out


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('dense',type=Path)
    p.add_argument('general_verifier',type=Path);p.add_argument('out',type=Path);a=p.parse_args()
    dense=load('dense',a.dense);verify=load('common',a.general_verifier)
    source,sha=dense.load_table(a.table);state=source
    for axis in range(4):state=apply(state,axis)
    gram=verify.verify(state,72*2**8)
    sectors=collections.Counter(tuple(i for i,x in enumerate(k) if x in (1,2)) for k in state)
    result={'table_sha256':sha,'support':len(state),'sector_support':[
              {'active_parties':k,'count':v} for k,v in sorted(sectors.items())],
            'normalization_and_six_marginals':gram,
            'transform':'identical local R(pi/4) on H and normalized 4x4 Walsh on K; both blocks nonmonomial',
            'scope':'Specific exact control only; theorem for arbitrary U(2)⊕U(4) follows from separate sector flattening rank proof.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
