#!/usr/bin/env python3
"""Source-only exact certificate for the A4/Pauli representation.

Also checks the three 2|2 unitary flattenings in Z[sqrt(2)] and the
50,625 finite nonempty support-mask configurations.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

H=(1,2);K=(0,3,4,5)
MAPS=({0:3,3:2,4:0,5:1},{0:3,3:0,4:2,5:1},
      {0:3,3:0,4:2,5:1},{0:3,3:2,4:1,5:0})
I=(1,0,0,1);X=(0,1,1,0);Z=(1,0,0,-1);J=(0,1,-1,0)
PAULIS={'I':I,'X':X,'Z':Z,'J':J}


def read_table(path):
    data={}
    raw=path.read_bytes()
    for line in raw.decode('utf-8').splitlines():
        if not line or line.startswith('#'):continue
        a,b,*terms=line.split()
        for term in terms:
            if len(term)!=3 or term[0] not in '+-s':raise ValueError('invalid term')
            q=(int(a),int(b),int(term[1]),int(term[2]))
            if q in data:raise ValueError('duplicate term')
            data[q]={'+' : (1,0), '-' : (-1,0), 's' : (0,1)}[term[0]]
    if len(data)!=60:raise ValueError('wrong support')
    return data,hashlib.sha256(raw).hexdigest()


def active(q):return tuple(i for i,x in enumerate(q) if x in H)


def parity(p):return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2


def certify_source(t):
    even={p for p in itertools.permutations(range(4)) if parity(p)==0}
    p=[q for q in t if not active(q)]
    if len(p)!=12 or any(t[q]!=(0,1) for q in p):raise ValueError('P coefficient/support mismatch')
    colours={tuple(MAPS[i][q[i]] for i in range(4)) for q in p}
    if colours!=even:raise ValueError('P is not A4')
    table=[]
    for i,j in itertools.combinations(range(4),2):
        k,l=[z for z in range(4) if z not in (i,j)]
        blocks={}
        for q,coef in t.items():
            if active(q)!=(i,j):continue
            a,b=MAPS[k][q[k]],MAPS[l][q[l]]
            if a!=b:raise ValueError('spectator equality mismatch')
            if coef[1] or abs(coef[0])!=1:raise ValueError('bad E coefficient')
            if a not in blocks:blocks[a]=[0,0,0,0]
            ix=2*H.index(q[i])+H.index(q[j])
            if blocks[a][ix]:raise ValueError('duplicate E block cell')
            blocks[a][ix]=coef[0]
        if set(blocks)!=set(range(4)):raise ValueError('missing Pauli block')
        types={}
        for g,block in blocks.items():
            options=[name for name,Q in PAULIS.items() if tuple(block)==Q or tuple(block)==tuple(-x for x in Q)]
            if len(options)!=1:raise ValueError('not signed Pauli')
            types[g]=options[0]
        if set(types.values())!=set(PAULIS):raise ValueError('Pauli types not complete')
        table.append({'active':[i,j],'spectators':[k,l],'pauli_type_by_colour':types})
    if sum(1 for q in t if len(active(q))==2)!=48:raise ValueError('unexpected source sectors')
    return sorted(colours),table


def times(x,y):return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])


def flattening_checks(t):
    checked=0
    for A in ((0,1),(0,2),(0,3)):
        B=tuple(i for i in range(4) if i not in A)
        F=[[None]*36 for _ in range(36)]
        for q,value in t.items():
            r=6*q[A[0]]+q[A[1]];c=6*q[B[0]]+q[B[1]];F[r][c]=value
        for i in range(36):
            for j in range(36):
                x=y=0
                for c in range(36):
                    if F[i][c] is not None and F[j][c] is not None:
                        a,b=times(F[i][c],F[j][c]);x+=a;y+=b
                if (x,y)!=((2 if i==j else 0),0):
                    raise ValueError('unnormalized flattening isometry failure')
                checked+=1
    return checked


def support_masks():
    even=[p for p in itertools.permutations(range(4)) if not parity(p)]
    admissible=[]
    for masks in itertools.product(range(1,16),repeat=4):
        if all(sum(bool(masks[i] & (1<<p[i])) for i in range(4)) in (0,1,4) for p in even):
            admissible.append(masks)
    if len(admissible)!=17:raise ValueError('wrong admissible mask count')
    same=0;distinct=0;full=0
    for masks in admissible:
        if all(x==15 for x in masks):full+=1
        elif all(x.bit_count()==1 for x in masks):
            vals=tuple(x.bit_length()-1 for x in masks)
            if len(set(vals))==1:same+=1
            elif vals in even:distinct+=1
            else:raise ValueError('unexpected singleton tuple')
        else:raise ValueError('unexpected mask structure')
    if (same,distinct,full)!=(4,12,1):raise ValueError('wrong classification')
    return {'configurations_examined':15**4,'admissible':len(admissible),
            'same_colour_singletons':same,'distinct_even_singletons':distinct,
            'all_colours_all_parties':full,'admissible_masks':admissible}


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('output',type=Path);args=p.parse_args()
    t,sha=read_table(args.table);even,pauli=certify_source(t);n=flattening_checks(t);masks=support_masks()
    bad=dict(t);bad.pop(next(q for q in t if not active(q)))
    try:certify_source(bad)
    except ValueError as exc:negative=str(exc)
    else:raise ValueError('source-deletion negative control not rejected')
    result={'table_sha256':sha,'K_colour_relabelling':MAPS,'P_even_permutations':even,
      'E_pair_pauli_blocks':pauli,'three_flattening_FFt_exact_entries_checked':n,
      'identity':'F F^T = 2 I over Z[sqrt(2)] for all 3 cuts',
      'support_mask_classification':masks,'deleted_P_control':negative,
      'scope':'Exact finite source facts and mask classification, not the universal complex argument.'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('P_even_permutations','E_pair_pauli_blocks','support_mask_classification')},indent=2))
    print(json.dumps(masks,indent=2))


if __name__=='__main__':main()
