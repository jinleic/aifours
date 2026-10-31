#!/usr/bin/env python3
"""Exact BH(10,5) source transcription and all half-row matching checks.

The construction is from the cited thesis Appendix D, not a generated search
snippet. Every matrix assertion is rechecked by integer exponent counts.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
K=(
 (0,0,0,0,0,0,0,0,0,0),
 (0,1,2,3,4,2,4,1,3,0),
 (0,2,4,1,3,3,2,1,0,4),
 (0,3,1,4,2,3,4,0,1,2),
 (0,4,3,2,1,2,0,3,1,4),
 (0,3,2,2,3,0,1,4,4,1),
 (0,2,0,4,4,1,1,3,2,3),
 (0,1,3,1,0,4,3,4,2,2),
 (0,0,1,3,1,4,2,2,4,3),
 (0,4,4,0,2,1,3,2,3,1),
)


def validate():
    assert len(K)==10 and all(len(row)==10 for row in K)
    for a,b in combinations(range(10),2):
        rowdiff=Counter((K[a][t]-K[b][t])%5 for t in range(10))
        coldiff=Counter((K[t][a]-K[t][b])%5 for t in range(10))
        assert rowdiff=={i:2 for i in range(5)},('row',a,b,rowdiff)
        assert coldiff=={i:2 for i in range(5)},('col',a,b,coldiff)


def half_graph(rows):
    edges=[]
    for a,b in combinations(range(10),2):
        diffs={(K[t][a]-K[t][b])%5 for t in rows}
        if len(diffs)==5:edges.append((a,b))
    return edges


def matching(edges):
    adjacency={i:set() for i in range(10)}
    for a,b in edges:adjacency[a].add(b);adjacency[b].add(a)
    def rec(left,chosen):
        if not left:return chosen
        a=min(left,key=lambda x:len(adjacency[x]&left))
        for b in sorted(adjacency[a]&left):
            result=rec(left-{a,b},chosen+[(a,b)])
            if result is not None:return result
        return None
    return rec(set(range(10)),[])


def main():
    validate()
    records=[]; edge_hist=Counter(); matched=0
    for rows in combinations(range(10),5):
        edges=half_graph(rows); perfect=matching(edges)
        edge_hist[len(edges)]+=1
        matched+=int(perfect is not None)
        records.append({'rows':rows,'edge_count':len(edges),'perfect_matching':perfect})
    print('BH(10,5) exact row/column orthogonality: PASS')
    print('all 252 five-row choices, edge-count histogram',dict(sorted(edge_hist.items())))
    print('five-row choices with a perfect matching:',matched,'of252')
    example=next((r for r in records if r['perfect_matching'] is not None),None)
    print('first matching example',example)
    out=ROOT/'frontier-20261028-butson10-half-matching-result-v1.json'
    out.write_text(json.dumps({'matrix_exponents':K,'rows':records,'matched_count':matched,
      'source':'explicit thesis Appendix D B10, independently checked',
      'scope':'one BH matrix and necessary half-row condition, not a QLS existence conclusion'},indent=2,sort_keys=True)+'\n')
    print('wrote',out.name)


if __name__=='__main__':main()
