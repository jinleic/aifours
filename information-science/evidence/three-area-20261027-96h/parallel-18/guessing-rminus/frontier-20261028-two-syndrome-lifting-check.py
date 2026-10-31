#!/usr/bin/env python3
"""Exact graph, incidence, and bit-gadget checks for the two-syndrome lifting."""
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent/'frontier-20261028-two-syndrome-lifting-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))

def check_graph(neighbors):
    for t in TRI:
        if len(set(t))!=3:raise ValueError('TRIANGLE_VERTEX')
        for v in t:
            if any(u not in neighbors[v] for u in t if u!=v):raise ValueError('MISSING_TRIANGLE_EDGE')
    if any(sum(v in t for t in TRI)!=3 for v in neighbors):raise ValueError('INCIDENCE')

def check_gadget(mutate=False):
    for s in (0,1):
        bit_counts=[[0,0] for _ in range(3)]
        for a in (0,1):
            for b in (0,1):
                x=(a,b,a^b^(0 if mutate else s))
                if x[0]^x[1]^x[2]!=s:raise ValueError('PARITY')
                for i in range(3):
                    bit_counts[i][x[i]]+=1
                    if x[i]!=(s^x[(i+1)%3]^x[(i+2)%3]):raise ValueError('LOCAL_DECODE')
        if any(z!=[2,2] for z in bit_counts):raise ValueError('UNIFORM_BIT')


def main():
    check_graph(N);check_gadget();cover=0;noncover=0;fiber_vertices=0;added_factors=0
    for J in range(1,1<<10):
        selected=[TRI[t] for t in range(10) if J>>t&1]
        if set().union(*map(set,selected))!=set(N):noncover+=1;continue
        cover+=1;K=10-len(selected);added_factors+=K
        k={v:sum(v in t for t in selected) for v in N}
        if sum(3-k[v] for v in N)!=3*K:raise ValueError('GAP_LIFT')
        for v in N:
            t=next(t for t in selected if v in t)
            if not set(t).difference({v})<=set(N[v]):raise ValueError('SYNDROME_DECODING')
            if not 1<=k[v]<=3:raise ValueError('BLOCK_SIZE')
            fiber_vertices+=1
    if (cover,noncover)!=(420,603):raise ValueError('COVER_CENSUS')
    controls={};bad={v:list(nb) for v,nb in N.items()};bad[1].remove(2)
    try:check_graph(bad)
    except ValueError as e:controls['missing_triangle_edge']=str(e)
    else:raise ValueError('EDGE_CONTROL')
    try:check_gadget(True)
    except ValueError as e:controls['incorrect_parity']=str(e)
    else:raise ValueError('PARITY_CONTROL')
    out={'all_checked':True,'nonzero_cover_masks':cover,'nonzero_noncover_masks':noncover,'cover_vertex_syndrome_reconstructions':fiber_vertices,
         'added_factors_over_cover_masks':added_factors,'uniform_gadget_cases':8,'negative_controls':controls,
         'limits':'Exact finite incidence, bit parity/decoder and uniform-marginal checks. Entropy chain rule, conditional tensorization and universal dual proof remain written mathematical arguments.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
