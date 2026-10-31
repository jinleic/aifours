#!/usr/bin/env python3
"""Directly test all 4950 ray pairs and targeted invalid-input controls."""
import argparse
import collections
import copy
import hashlib
import itertools
import json
from pathlib import Path
import sys


class WitnessError(ValueError): pass


def audit(obj):
    w=obj['partial_witness']; d=w['denominator']; labels=w['labels']; array=w['array']
    if not isinstance(d,int) or d<=0 or len(array)!=10 or any(len(row)!=10 for row in array):
        raise WitnessError('shape')
    if len(labels)!=10 or any(len(row)!=10 or set(row)!=set(range(10)) for row in labels):
        raise WitnessError('label-row')
    if any({labels[r][c] for r in range(10)}!=set(range(10)) for c in range(10)):
        raise WitnessError('label-column')
    values=[array[r][c] for r in range(10) for c in range(10)]
    if any(len(v)!=10 or any(type(x)!=int for x in v) for v in values): raise WitnessError('coordinates')
    if any(sum(x*x for x in v)!=d*d for v in values): raise WitnessError('norm')
    parent=list(range(100))
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    count=0
    for i,j in itertools.combinations(range(100),2):
        dot=sum(x*y for x,y in zip(values[i],values[j]))
        if abs(dot)==d*d:
            count+=1
            x,y=find(i),find(j)
            if x!=y: parent[y]=x
    return {'pairs_directly_checked':4950,'parallel_pairs':count,
            'distinct_rays':len({find(i) for i in range(100)})}


def reject(obj,expected):
    try: audit(obj)
    except WitnessError as exc:
        if str(exc)!=expected: raise WitnessError(f'wrong rejection {exc}, expected {expected}')
        return str(exc)
    raise WitnessError(f'mutant accepted, expected {expected}')


def main():
    p=argparse.ArgumentParser();p.add_argument('w12',type=Path);p.add_argument('w13',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    rows=[]
    for path,expected in ((a.w12,12),(a.w13,13)):
        raw=path.read_bytes();obj=json.loads(raw);res=audit(obj)
        if res['distinct_rays']!=expected: raise WitnessError('ray-count')
        broken=copy.deepcopy(obj);broken['partial_witness']['array'][0][0][0]+=1
        badlabels=copy.deepcopy(obj);badlabels['partial_witness']['labels'][0][0]=badlabels['partial_witness']['labels'][0][1]
        rows.append({'input_sha256':hashlib.sha256(raw).hexdigest(),'result':res,
                     'mutations':{'changed_coordinate':reject(broken,'norm'),'repeated_row_label':reject(badlabels,'label-row')}})
    result={'certificates':rows,'scope':'direct exact real-vector ray comparison; complex competitors not considered'}
    with a.output.open('x',encoding='utf-8') as out: json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
