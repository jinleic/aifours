#!/usr/bin/env python3
"""Classify the exact common SO(2) rotation orbit of the 60-term witness."""
import argparse
import collections
import importlib.util
import itertools
import json
from pathlib import Path
import sys

Z=(0,0)


def add(x,y):
    return x[0]+y[0],x[1]+y[1]


def mult(x,y):
    return x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]


def accumulate(out,key,value):
    value=add(out.get(key,Z),value)
    if value==Z:
        out.pop(key,None)
    else:
        out[key]=value


def apply_345(tensor,axis):
    """Unnormalized block [[3,4],[-4,3]], 5I on other levels."""
    out={}
    for coord,value in tensor.items():
        level=coord[axis]
        if level not in (1,2):
            accumulate(out,coord,(5*value[0],5*value[1]))
            continue
        p=coord[:axis]+(1,)+coord[axis+1:]
        q=coord[:axis]+(2,)+coord[axis+1:]
        if level==1:
            accumulate(out,p,(3*value[0],3*value[1]))
            accumulate(out,q,(-4*value[0],-4*value[1]))
        else:
            accumulate(out,p,(4*value[0],4*value[1]))
            accumulate(out,q,(3*value[0],3*value[1]))
    return out


def verify(tensor,denominator):
    norm=Z
    for v in tensor.values(): norm=add(norm,mult(v,v))
    if norm!=(denominator,0): raise ValueError(f'norm {norm} != {denominator}')
    for pair in itertools.combinations(range(4),2):
        rest=tuple(i for i in range(4) if i not in pair)
        grouped=collections.defaultdict(list)
        for index,coefficient in tensor.items():
            grouped[tuple(index[i] for i in rest)].append((tuple(index[i] for i in pair),coefficient))
        gram=collections.defaultdict(lambda: Z)
        for entries in grouped.values():
            for i,x in entries:
                for j,y in entries:
                    gram[(i,j)]=add(gram[(i,j)],mult(x,y))
        for i in itertools.product(range(6),repeat=2):
            for j in itertools.product(range(6),repeat=2):
                expected=(denominator//36,0) if i==j else Z
                if gram[(i,j)]!=expected: raise ValueError(f'marginal mismatch {pair},{i},{j}')
    return {'norm_numerator':norm,'denominator':denominator,'six_marginals':'I/36',
            'entries_per_marginal':1296}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('table',type=Path)
    parser.add_argument('dense_verifier',type=Path)
    parser.add_argument('phase_search',type=Path)
    parser.add_argument('output',type=Path)
    args=parser.parse_args()
    spec=importlib.util.spec_from_file_location('dense',args.dense_verifier)
    dense=importlib.util.module_from_spec(spec); spec.loader.exec_module(dense)
    tensor,sha=dense.load_table(args.table)
    blocks=collections.defaultdict(dict)
    p_count=0
    for coord,coefficient in tensor.items():
        active=tuple(i for i,v in enumerate(coord) if v in (1,2))
        if len(active)==0:
            p_count+=1
        elif len(active)==2:
            rest=tuple(i for i in range(4) if i not in active)
            key=(active,tuple(coord[i] for i in rest))
            slots=tuple(coord[i] for i in active)
            if slots in blocks[key]: raise ValueError('duplicate block cell')
            blocks[key][slots]=coefficient
        else:
            raise ValueError(f'unexpected active count: {coord}')
    types=collections.Counter()
    details=[]
    for key,entries in sorted(blocks.items()):
        if len(entries)!=2 or any(value[1]!=0 for value in entries.values()):
            raise ValueError(f'unexpected block {key}: {entries}')
        if set(entries)=={(1,1),(2,2)}:
            typ='I' if entries[(1,1)]==entries[(2,2)] else 'Z'
        elif set(entries)=={(1,2),(2,1)}:
            typ='X' if entries[(1,2)]==entries[(2,1)] else 'J'
        else:
            raise ValueError(f'unexpected block support {key}: {entries}')
        types[typ]+=1
        details.append({'active_parties':key[0],'fixed_other_indices':key[1],
                        'type_up_to_overall_sign':typ,'cells':[[*pos,*value] for pos,value in sorted(entries.items())]})
    if p_count!=12 or dict(types)!={'J':6,'I':6,'X':6,'Z':6}:
        raise ValueError(f'unexpected support decomposition: P={p_count}, types={types}')
    rotated=tensor
    for axis in range(4): rotated=apply_345(rotated,axis)
    if len(rotated)!=84:
        raise ValueError(f'generic rational-angle support {len(rotated)} != 84')
    rational_check=verify(rotated,72*5**8)
    spec2=importlib.util.spec_from_file_location('phase_search',args.phase_search)
    phase=importlib.util.module_from_spec(spec2); spec2.loader.exec_module(phase)
    state={k:(a,b,0,0) for k,(a,b) in tensor.items()}
    for axis in range(4): state=phase.apply_gate(state,axis,1,2,0)
    if len(state)!=60: raise ValueError('equal-angle endpoint not 60')
    endpoint_check=phase.verify_six(state,4)
    overlap=set(state)&set(tensor)
    unchanged=sum(state[k]==(4*tensor[k][0],4*tensor[k][1],0,0) for k in overlap)
    result={'table_sha256':sha,'classical_terms':p_count,'two_active_blocks':len(blocks),
            'block_type_histogram':dict(sorted(types.items())),'blocks':details,
            'generic_angle_symbolic_support':84,
            'rational_rotation':{'cos': '3/5','sin':'4/5','support':len(rotated),'exact_check':rational_check},
            'equal_angle_endpoint':{'support':len(state),'intersection_with_source_support':len(overlap),
                                    'coefficients_unchanged_on_overlap':unchanged,'exact_check':endpoint_check},
            'limits':'Same LU orbit; this is not an improved support or a global AME minimum.'}
    with args.output.open('x',encoding='utf-8') as out:
        json.dump(result,out,indent=2); out.write('\n')
    json.dump({k:result[k] for k in ('table_sha256','classical_terms','two_active_blocks','block_type_histogram','generic_angle_symbolic_support','rational_rotation','equal_angle_endpoint','limits')},sys.stdout,indent=2)
    print()


if __name__=='__main__': main()
