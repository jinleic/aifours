#!/usr/bin/env python3
"""Independent complete Serre ideals from integral PBW/adjoint words.

Not the producer's Levi queue or native-basis recursion. Generate the whole
bounded initial Levi orbit from ALL e1^i e12^j e2^k PBW monomials on each literal
Serre seed, then ALL bounded V-adjoint words, WITHOUT intermediate RREF. Uniform
nonzero integer multiples of the independently reconstructed matrix-unit
operators clear denominators. Primitive integer normalization/duplicate removal
preserve spans. PBW and Jacobi prove completeness; monotone positive degrees
make truncation exact. Only the FINAL coordinate row spaces use shared FLINT.
All raw generators are independently projected to zero in those spaces.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint
spec=importlib.util.spec_from_file_location('separate_matrix_tree',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec)
spec.loader.exec_module(ind)
TRACE=[]
SCALES={g:math.lcm(*(Q(c).denominator for row in ind.ACTION[g] for c in row.values())) for g in ind.ACTION}
ACTIONS={g:[{target:int(Q(c)*SCALES[g]) for target,c in row.items()} for row in ind.ACTION[g]] for g in ind.ACTION}


def clean_integer(vector):
    v={w:int(c) for w,c in vector.items() if c}
    if not v:
        return {}
    divisor=math.gcd(*(abs(c) for c in v.values()))
    sign=1 if v[min(v)]>0 else -1
    return {w:sign*c//divisor for w,c in v.items()}


def adjoint_letter(j,vector):
    out={}
    letter=str(j)
    for word,c in vector.items():
        out[letter+word]=out.get(letter+word,0)+c
        out[word+letter]=out.get(word+letter,0)-c
    return clean_integer(out)


def integral_action(vector,g):
    out={}
    for word,c in vector.items():
        for position,j in enumerate(word):
            for target,b in ACTIONS[g][int(j)].items():
                w=word[:position]+target+word[position+1:]
                out[w]=out.get(w,0)+c*b
    return clean_integer(out)


@lru_cache(None)
def standard_integer(word):
    v=ind.ind.standard_bracket(word)
    assert v and min(v)==word and v[word]==1
    assert all(Q(c).denominator==1 for c in v.values())
    return {w:int(c) for w,c in v.items()}


def decompose(vector):
    pending={w:Q(c) for w,c in vector.items() if c}
    coordinates={}
    while pending:
        word=min(pending)
        assert ind.ind.lyndon(word), 'independent non-Lie leading word'
        c=pending[word]
        coordinates[word]=coordinates.get(word,Q(0))+c
        for w,b in standard_integer(word).items():
            pending[w]=pending.get(w,Q(0))-c*b
            if not pending[w]:
                del pending[w]
    return coordinates


def decompose_integer(vector):
    pending=dict(vector)
    coordinates={}
    while pending:
        word=min(pending)
        assert ind.ind.lyndon(word)
        c=pending[word]
        coordinates[word]=coordinates.get(word,0)+c
        for w,b in standard_integer(word).items():
            pending[w]=pending.get(w,0)-c*b
            if not pending[w]:
                del pending[w]
    return coordinates


def normal_form(vector,rows):
    pending={w:Q(c) for w,c in vector.items() if c}
    result={}
    while pending:
        w=min(pending)
        c=pending.pop(w)
        row=rows.get(w)
        if row is None:
            result[w]=c
            continue
        assert row[w]==1 and min(row)==w
        for word,b in row.items():
            if word!=w:
                pending[word]=pending.get(word,Q(0))-c*b
                if not pending[word]:
                    del pending[word]
    return result


class CoordinateSpace:
    def __init__(self,rows=()):
        self.rows={min(row):row for row in rows}
        assert all(row[p]==1 for p,row in self.rows.items())

    def __len__(self):
        return len(self.rows)

    def reduce(self,v):
        return normal_form(v,self.rows)


def native_final_span(degree,raw):
    coordinates=[decompose_integer(v) for v in raw]
    labels=sorted({w for v in coordinates for w in v})
    if not labels:
        TRACE.append({'degree':list(degree),'raw_generators':0,'rank':0})
        return CoordinateSpace()
    M=flint.fmpq_mat([[v.get(w,0) for w in labels] for v in coordinates])
    R,rank=M.rref()
    rows=[]
    for i in range(rank):
        row={w:Q(int(R[i,j].numerator),int(R[i,j].denominator)) for j,w in enumerate(labels) if R[i,j]}
        rows.append(row)
    space=CoordinateSpace(rows)
    assert len(space)==rank
    for v in coordinates:
        assert not space.reduce(v), 'independent raw PBW/adjoint generator escaped final span'
    TRACE.append({'degree':list(degree),'raw_generators':len(raw),'coordinate_columns':len(labels),'rank':rank})
    return space


def add_raw(groups,seen,degree,vector):
    if vector:
        key=tuple(sorted(vector.items()))
        if key not in seen[degree]:
            seen[degree].add(key)
            groups[degree].append(vector)


def initial_pbw(bound,index,power):
    m=power+1
    seed={str(index):1}
    for _ in range(power):
        seed=adjoint_letter(0,seed)
    assert seed and not integral_action(seed,'f1') and not integral_action(seed,'f2')
    a0,b0=ind.WEIGHTS[index]
    groups=defaultdict(list)
    seen=defaultdict(set)
    e2=seed
    for k in range(bound[1]-b0+1):
        if not e2:
            break
        e12=e2
        for j in range(min(bound[0]-a0,bound[1]-b0-k)+1):
            if not e12:
                break
            e1=e12
            for i in range(bound[0]-a0-j+1):
                if not e1:
                    break
                degree=(a0+i+j,b0+k+j,m)
                add_raw(groups,seen,degree,e1)
                e1=integral_action(e1,'e1')
            e12=integral_action(e12,'e12')
        e2=integral_action(e2,'e2')
    return groups


def ideal_spaces(queries,r,s):
    assert queries and min(r,s)>=1
    bound=tuple(max(d[i] for d in queries) for i in range(3))
    collected=defaultdict(list)
    collected_seen=defaultdict(set)
    for index,power in ((1,r),(2,s)):
        if power+1>bound[2]:
            continue
        current=initial_pbw(bound,index,power)
        for level in range(power+1,bound[2]+1):
            for degree,rows in current.items():
                if degree in queries:
                    for row in rows:
                        add_raw(collected,collected_seen,degree,row)
            if level==bound[2]:
                break
            following=defaultdict(list)
            seen=defaultdict(set)
            for degree,rows in current.items():
                for j,(a,b) in enumerate(ind.WEIGHTS):
                    target=(degree[0]+a,degree[1]+b,level+1)
                    if target[0]>bound[0] or target[1]>bound[1]:
                        continue
                    for row in rows:
                        add_raw(following,seen,target,adjoint_letter(j,row))
            current=following
    return {degree:native_final_span(degree,collected.get(degree,[])) for degree in sorted(queries)}


def same_space(space,claimed):
    rows={min(v):v for v in claimed}
    assert len(rows)==len(claimed)==len(space)
    for v in claimed:
        assert not space.reduce(v)
    for v in space.rows.values():
        assert not normal_form(v,rows)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--fixed',choices=['r','s'],required=True)
    ap.add_argument('--value',type=int,required=True)
    ap.add_argument('--sha256',required=True)
    args=ap.parse_args()
    name=f'frontier-20261028-level6-{args.fixed}{args.value}-quotient-family-v1.json'
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==args.sha256
    C=json.loads(raw)
    queries={tuple(e['degree']) for e in C['records']}|{(*e['degree'][:2],5) for e in C['records']}
    r,s=(args.value,6) if args.fixed=='r' else (6,args.value)
    spaces=ideal_spaces(queries,r,s)
    results=[]
    for e in C['records']:
        degree=tuple(e['degree'])
        for label,target in (('source',degree),('target',(*degree[:2],5))):
            claimed=[decompose({w:Q(c) for w,c in v.items()}) for v in e[f'{label}_ideal_rows']]
            same_space(spaces[target],claimed)
            results.append({'degree':list(target),'rank':len(spaces[target]),'both_span_directions_checked':True})
    output=ROOT/f'frontier-20261028-level6-{args.fixed}{args.value}-independent-pbw-ideal-control-v1.json'
    with output.open('x') as stream:
        json.dump({'input_sha256':args.sha256,'fixed_parameter':args.fixed,'fixed_value':args.value,'operator_integer_scales':SCALES,
                   'records':results,'construction_trace':TRACE,'status':'PASS_ALL_PBW_ADJOINT_WORD_IDEAL_SPACES',
                   'limits':'whole ideal reconstruction only; not the source quotient or D3 matrices. FLINT final RREF arithmetic shared; no formal/independent-model claim.'},stream,indent=2)
        stream.write('\n')
    print('PASS independent full PBW/adjoint ideals',len(results),'spaces',output.name,flush=True)


if __name__=='__main__':
    main()
