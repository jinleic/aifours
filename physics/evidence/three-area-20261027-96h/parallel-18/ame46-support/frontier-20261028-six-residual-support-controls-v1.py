#!/usr/bin/env python3
"""Bounded exact controls for the n=6, |E|=12 residual classification."""
import argparse
from collections import Counter,deque
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2))


def fiber_options(g,mixed):
    missing=tuple(x for x in range(3) if x!=g)
    alph=((0,1),missing,missing) if mixed else (missing,missing,missing)
    cube=list(itertools.product(*alph));out=[]
    for F in itertools.combinations(cube,4):
        if all(sum(x[j]==v for x in F)==2 for j in range(3) for v in alph[j]):out.append(tuple(F))
    if len(out)!=8:raise ValueError('unexpected balanced fiber count')
    return out


def projections(S):
    return {ij:Counter((x[ij[0]],x[ij[1]]) for x in S) for ij in PAIRS}


def bipartite(vertices):
    color={};edge=[]
    for a,b in itertools.combinations(range(len(vertices)),2):
        if any(vertices[a][j]==vertices[b][j] for j in range(3)):edge.append((a,b))
    for root in range(len(vertices)):
        if root in color:continue
        color[root]=0;queue=deque((root,))
        while queue:
            a=queue.popleft()
            for x,y in edge:
                if a not in (x,y):continue
                b=y if a==x else x
                if b in color and color[b]==color[a]:return False,edge
                if b not in color:color[b]=1-color[a];queue.append(b)
    return True,edge


def analyze(mixed):
    opts=[fiber_options(g,mixed) for g in range(3)];counts=Counter();examples=[]
    for Fs in itertools.product(*opts):
        E={(g,)+x for g,F in enumerate(Fs) for x in F};counts['balanced_normal_forms']+=1
        if len(E)!=12:raise ValueError('fiber cardinality')
        proj=projections(E)
        if not all(len(x)==6 for x in proj.values()):continue
        counts['all_pair_projections_six']+=1
        if not all(set(x.values())=={2} for x in proj.values()):continue
        counts['all_projection_degrees_two']+=1
        if mixed:
            S=sorted({(x[0],x[2],x[3]) for x in E})
            if len(S)!=6 or any((a,b,c,d) not in E for a,c,d in S for b in (0,1)):
                raise ValueError('mixed residual not binary fibered')
            graph,edges=bipartite(S);counts['bipartite' if graph else 'odd_cycle']+=1
            examples.append({'S':S,'graph_edges':edges,'bipartite':graph})
    if counts['balanced_normal_forms']!=512:raise ValueError('incomplete enumeration')
    if not mixed and counts['all_pair_projections_six']!=0:raise ValueError('unexpected all-ternary support')
    if mixed and (counts['all_pair_projections_six'],counts['all_projection_degrees_two'],counts['bipartite'],counts['odd_cycle'])!=(4,4,1,3):raise ValueError('unexpected mixed support classes')
    return {'counts':dict(counts),'examples':examples}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    result={'all_ternary':analyze(False),'one_binary':analyze(True),
            'scope':'Finite checks of canonical balanced 12-term residual supports; normalization and exhaustive normal form require the written proof.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'all_ternary':result['all_ternary']['counts'],'one_binary':result['one_binary']['counts'],'scope':result['scope']},indent=2))


if __name__=='__main__':main()
