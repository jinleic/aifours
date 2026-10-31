#!/usr/bin/env python3
"""Exact rank/duplicate checks for 5x5 two-regular incidence graphs."""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path


def f2rank(rows):
    basis={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p not in basis:basis[p]=x;break
            x^=basis[p]
    return len(basis)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    masks=[x for x in range(32) if x.bit_count()==2];counts=Counter();duplicates=Counter();graphs=0;selected=0
    for rows in itertools.product(masks,repeat=5):
        if any(sum(bool(x>>j&1) for x in rows)!=2 for j in range(5)):continue
        graphs+=1;rank=f2rank(rows);freq=Counter(rows)
        if max(freq.values())>2:raise ValueError('triple duplicate')
        rep=[tuple(i for i,x in enumerate(rows) if x==q) for q,v in freq.items() if v==2]
        if rank==3:
            if len(rep)!=1:raise ValueError('rank3 duplicate classification')
            p=rep[0];duplicates[p]+=1
            two=rows[p[0]];remaining=[rows[i] for i in range(5) if i not in p]
            if any(x&two for x in remaining):raise ValueError('duplicate component not isolated')
        elif rank==4:
            if rep:raise ValueError('rank4 duplicate found')
        else:raise ValueError('unexpected graph rank')
        counts[rank]+=1
        for excluded in range(5):
            selected+=1
            if f2rank([rows[i] for i in range(5) if i!=excluded])<3:raise ValueError('four-row rank below3')
    if graphs!=2040 or dict(counts)!={3:600,4:1440} or selected!=10200:raise ValueError('unexpected graph counts')
    if len(duplicates)!=10 or set(duplicates.values())!={60}:raise ValueError('duplicate pair distribution')
    # Paired graphs with equal duplicate row pair: exactly the possible size-2
    # zero-XOR rectangle configurations.
    paired=sum(x*x for x in duplicates.values())
    if paired!=36000:raise ValueError('unexpected duplicate-pair count')
    result={'graphs':graphs,'F2_rank_counts':dict(sorted(counts.items())),
      'selected_four_row_rank_checks':selected,'minimum_selected_four_rank':3,
      'possible_duplicate_row_pairs':len(duplicates),'graphs_per_duplicate_pair':60,
      'ordered_graph_pairs_with_shared_duplicate_pair':paired,
      'scope':'Exact incidence-graph controls. Full rectangle parity and AME conclusions are written separately.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
