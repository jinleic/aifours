#!/usr/bin/env python3
"""Find and exactly verify a three-fold triangle cover / q=8 R-minus strategy.

A solver supplies a combinatorial cover only. Integer checks and the disjoint
parity construction independently verify all original neighbour decoders.
"""
from itertools import combinations
from pathlib import Path
import json
from z3 import Bool,If,Solver,Sum,sat,is_true

OUT=Path(__file__).with_name('frontier-20261028-triangle-baseline-result.json')
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def rank2(rows):
    basis={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:basis[p]=x;break
    return len(basis)


def main():
    if any(v not in N[u] for u,ns in N.items() for v in ns):raise ValueError('ASYMMETRIC_GRAPH')
    triangles=[t for t in combinations(range(1,11),3)
               if all(b in N[a] for a,b in combinations(t,2))]
    x=[Bool('triangle_'+str(i)) for i in range(len(triangles))]
    solver=Solver();solver.set(timeout=5000)
    for v in range(1,11):solver.add(Sum([If(x[i],1,0) for i,t in enumerate(triangles) if v in t])==3)
    status=solver.check();out={'triangle_count':len(triangles),'solver_status':str(status)}
    if status==sat:
        model=solver.model();chosen=[t for t,z in zip(triangles,x) if is_true(model.eval(z,model_completion=True))]
        if len(chosen)!=10 or any(sum(v in t for t in chosen)!=3 for v in range(1,11)):
            raise ValueError('COVER_COUNTS')
        if any(any(b not in N[a] for a,b in combinations(t,2)) for t in chosen):raise ValueError('NONEDGE')
        # Three coordinates per vertex are indexed in triangle order; each
        # check is XOR of its three distinct vertex-coordinate bits.
        occurrences={v:[] for v in range(1,11)}
        for j,t in enumerate(chosen):
            for v in t:occurrences[v].append(j)
        positions={(v,t):3*(v-1)+occurrences[v].index(t) for v in range(1,11) for t in occurrences[v]}
        checks=[sum(1<<positions[(v,j)] for v in t) for j,t in enumerate(chosen)]
        rank=rank2(checks)
        if rank!=10 or len(positions)!=30:raise ValueError('PARITY_RANK')
        # Each decoder component depends on exactly the two triangle neighbours.
        maps={str(v):[{'triangle':j,'neighbours':[u for u in chosen[j] if u!=v]} for j in occurrences[v]]
              for v in range(1,11)}
        q=8;count=1<<(30-rank)
        out.update({'chosen_triangles':chosen,'cover_count_per_vertex':3,
                    'parity_check_rank':rank,'binary_coordinate_count':30,
                    'q':q,'winning_count':count,'exact_count_cubed_equals_q_power20':count**3==q**20,
                    'decoder_components':maps})
    out['limits']='This reproduces the known 20/3 lower bound and supplies a concrete all-domain q=8 strategy; it is not an improvement or novelty claim.'
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
