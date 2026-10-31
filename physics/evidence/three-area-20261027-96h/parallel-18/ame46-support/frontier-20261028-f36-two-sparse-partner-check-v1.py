#!/usr/bin/env python3
"""Check SAME-cell partner property on the independently verified 12-ray data."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys


def dot(x,y):return sum(a*b for a,b in zip(x,y))


def main():
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    raw=a.input.read_bytes();w=json.loads(raw)['partial_witness'];d=w['denominator'];arr=w['array'];labels=w['labels']
    if d!=65:raise ValueError('unexpected denominator')
    vec=[arr[r][c] for r in range(10) for c in range(10)]
    blocks=([[10*r+c for c in range(10)] for r in range(10)] +
            [[10*r+c for r in range(10)] for c in range(10)] +
            [[10*r+c for r in range(10) for c in range(10) if labels[r][c]==j] for j in range(10)])
    support=[{k for k,v in enumerate(x) if v} for x in vec]
    singles=sum(len(x)==1 for x in support);twos=[i for i,x in enumerate(support) if len(x)==2]
    if singles!=94 or len(twos)!=6 or any(len(s) not in (1,2) for s in support):raise ValueError('unexpected support counts')
    for cell in twos:
        containing=[block for block in blocks if cell in block]
        if len(containing)!=3:raise ValueError('wrong block incidence')
        partners=[]
        for block in containing:
            options=[other for other in block if other!=cell and support[other]==support[cell] and dot(vec[other],vec[cell])==0]
            if len(options)!=1:raise ValueError('nonunique partner')
            partners.append(options[0])
        if len(set(partners))!=3:raise ValueError('partners not distinct')
        if any(abs(dot(vec[partners[0]],vec[j]))!=d*d for j in partners):raise ValueError('partners are not same ray')
    result={'input_sha256':hashlib.sha256(raw).hexdigest(),'singleton_cells':singles,'two_support_cells':len(twos),
            'blocks_per_two_support_cell':3,'distinct_same_ray_partners_per_cell':'PASS',
            'scope':'Finite exact corroboration only; universal theorem is a separate written argument.'}
    with a.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
