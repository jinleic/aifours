#!/usr/bin/env python3
"""Independently check order-10 classical, 12-ray and 13-ray RQLS data.

Includes exact definition-level validation, direct Parker 1959 source-table
reconstruction and independent sparse tangent-matrix assembly. No author code
is imported. All vector and orthogonality calculations are integer exact.
"""
import argparse
import collections
import hashlib
import itertools
import json
from math import gcd
from pathlib import Path
import sys

N=10
WEISNER=(
'00 28 59 84 67 32 15 93 71 46',
'82 11 30 69 05 78 43 26 94 57',
'95 03 22 41 79 16 80 54 37 68',
'48 96 14 33 52 89 27 01 65 70',
'76 50 97 25 44 63 09 38 12 81',
'23 87 61 98 36 55 74 19 40 02',
'51 34 08 72 90 47 66 85 29 13',
'39 62 45 10 83 91 58 77 06 24',
'17 49 73 56 21 04 92 60 88 35',
'64 75 86 07 18 20 31 42 53 99')
PARKER_A=('0417298365','8152739406','9826374510','5983047621','7698415032',
          '6709852143','3071986254','1234560789','2345601897','4560123978')
PARKER_B=('0786935412','6178094523','5027819634','9613782045','3902478156',
          '8491357260','7859246301','4560123789','1234560978','2345601897')


def sha(raw): return hashlib.sha256(raw).hexdigest()


def dot(x,y): return sum(a*b for a,b in zip(x,y))


def make_blocks(labels):
    target=set(range(N))
    if len(labels)!=N or any(len(row)!=N or set(row)!=target for row in labels):
        raise ValueError('resolution labels are not a Latin square: row')
    if any({labels[r][c] for r in range(N)}!=target for c in range(N)):
        raise ValueError('resolution labels are not a Latin square: column')
    rows=[[r*N+c for c in range(N)] for r in range(N)]
    cols=[[r*N+c for r in range(N)] for c in range(N)]
    trans=[[r*N+c for r in range(N) for c in range(N) if labels[r][c]==k] for k in range(N)]
    if any(len(block)!=N for block in trans): raise ValueError('invalid transversal size')
    return rows+cols+trans


def canonical(v):
    div=0
    for x in v: div=gcd(div,abs(x))
    if div==0: raise ValueError('zero vector')
    v=tuple(x//div for x in v)
    return tuple(-x for x in v) if next(x for x in v if x)!=abs(next(x for x in v if x)) else v


def validate(obj,expected):
    w=obj['partial_witness']; denominator=w['denominator']; array=w['array']; labels=w['labels']
    if type(denominator)!=int or denominator<=0 or len(array)!=N or any(len(row)!=N for row in array):
        raise ValueError('invalid vector-array shape or denominator')
    vectors=[array[r][c] for r in range(N) for c in range(N)]
    if any(len(v)!=N or any(type(x)!=int for x in v) for v in vectors): raise ValueError('invalid vector coordinates')
    blocks=make_blocks(labels)
    for x in vectors:
        if dot(x,x)!=denominator**2: raise ValueError('unit norm failure')
    for block in blocks:
        for x,y in itertools.combinations(block,2):
            if dot(vectors[x],vectors[y])!=0: raise ValueError('block orthogonality failure')
    rays=collections.Counter(canonical(v) for v in vectors)
    if len(rays)!=expected: raise ValueError(f'expected {expected} rays, found {len(rays)}')
    parallel=sum(k*(k-1)//2 for k in rays.values())
    return {'denominator':denominator,'unit_norms':100,'basis_blocks':len(blocks),
            'offdiagonal_block_checks':len(blocks)*45,'pairwise_ray_checks':4950,
            'ray_count':len(rays),'parallel_pairs':parallel,
            'ray_multiplicity_histogram':dict(sorted(collections.Counter(rays.values()).items()))},vectors,blocks,labels


def parker_oa():
    if any(len(x)!=N for x in PARKER_A+PARKER_B): raise ValueError('bad Parker source table')
    points=[(r,c,int(PARKER_A[r][c]),int(PARKER_B[r][c])) for r in range(N) for c in range(N)]
    for i,j in itertools.combinations(range(4),2):
        if len({(x[i],x[j]) for x in points})!=100: raise ValueError('Parker OA strength-two failure')
    return points


def match_parker(vectors,labels,denominator,points,mode):
    # Color=original Parker row, array row=original column,
    # array column=first square, resolution label=second square.
    by_cell={(q[1],q[2]):q for q in points}
    if len(by_cell)!=100: raise ValueError('Parker cell mapping not bijective')
    if mode=='13':
        for r in range(N):
            for c in range(N):
                q=by_cell[r,c]
                if labels[r][c]!=q[3]: raise ValueError('Parker label mismatch')
                expected=[0]*N
                if all(z in (7,8,9) for z in q):
                    for k in (7,8,9): expected[k]=(3 if k==q[0] else 0)-2
                else: expected[q[0]]=3
                if vectors[r*N+c]!=expected: raise ValueError(f'Householder-source mismatch {(r,c)}')
        return {'source':'Parker 1959 section 3; color original row, array axes original column and first square',
                'subarray_size':sum(all(z in (7,8,9) for z in q) for q in points),
                'exact_householder_reconstruction':'PASS'}
    # Identify every two-colour component directly, then reconstruct the
    # six-cell switch from the two exact observed rays.
    selected=[q for q in points if q[0] in (7,8)]
    graph={q:set() for q in selected}
    for axis in (1,2,3):
        for k in range(N):
            block=[q for q in selected if q[axis]==k]
            if len(block)!=2 or block[0][0]==block[1][0]: raise ValueError('invalid color-pair block')
            graph[block[0]].add(block[1]); graph[block[1]].add(block[0])
    unseen=set(selected); components=[]
    while unseen:
        node=unseen.pop(); stack=[node]; comp={node}
        while stack:
            for v in graph[stack.pop()]:
                if v in unseen: unseen.remove(v); comp.add(v); stack.append(v)
        components.append(comp)
    if sorted(map(len,components))!=[6,14]: raise ValueError('unexpected two-colour graph components')
    short=next(c for c in components if len(c)==6)
    for r in range(N):
        for c in range(N):
            q=by_cell[r,c]
            if labels[r][c]!=q[3]: raise ValueError('Parker label mismatch')
            expected=[0]*N
            if q in short:
                expected[7],expected[8]=(39,52) if q[0]==7 else (-52,39)
            else: expected[q[0]]=65
            if vectors[r*N+c]!=expected: raise ValueError(f'two-colour source mismatch {(r,c)}')
    return {'source':'Parker 1959 section 3; color original row, array axes original column and first square',
            'two_colour_component_sizes':[6,14], 'selected_short_component':6,
            'exact_rotated_source_reconstruction':'PASS'}


def weisner_check():
    data=[[tuple(map(int,token)) for token in row.split()] for row in WEISNER]
    if len(data)!=N or any(len(row)!=N for row in data): raise ValueError('Weisner shape')
    for axis in (0,1):
        for r in range(N):
            if {data[r][c][axis] for c in range(N)}!=set(range(N)): raise ValueError('Weisner row')
        for c in range(N):
            if {data[r][c][axis] for r in range(N)}!=set(range(N)): raise ValueError('Weisner column')
    if len({data[r][c] for r in range(N) for c in range(N)})!=100: raise ValueError('Weisner orthogonality')
    labels=[[data[r][c][1] for c in range(N)] for r in range(N)]
    blocks=make_blocks(labels)
    colors=[data[r][c][0] for r in range(N) for c in range(N)]
    sizes=collections.Counter()
    for a,b in itertools.combinations(range(N),2):
        nodes={j for j,v in enumerate(colors) if v in (a,b)}
        graph={j:set() for j in nodes}
        for block in blocks:
            pair=[j for j in block if colors[j] in (a,b)]
            if len(pair)!=2: raise ValueError('color-pair block failure')
            graph[pair[0]].add(pair[1]);graph[pair[1]].add(pair[0])
        unseen=set(nodes); comp=[]
        while unseen:
            x=unseen.pop(); stack=[x]; count=1
            while stack:
                for y in graph[stack.pop()]:
                    if y in unseen: unseen.remove(y);stack.append(y);count+=1
            comp.append(count)
        sizes[tuple(sorted(comp))]+=1
    return {'latin_and_orthogonal':'PASS','pair_graph_components':[[list(k),v] for k,v in sorted(sizes.items())]}


def sparse_tangents(vectors,blocks):
    real=[];imag=[]
    for idx,v in enumerate(vectors):
        real.append({10*idx+k:value for k,value in enumerate(v) if value})
    for block in blocks:
        for x,y in itertools.combinations(block,2):
            r={};i={}
            for k in range(N):
                if vectors[y][k]: r[10*x+k]=vectors[y][k]; i[10*x+k]=-vectors[y][k]
                if vectors[x][k]: r[10*y+k]=vectors[x][k]; i[10*y+k]=vectors[x][k]
            real.append(r); imag.append(i)
    if len(real)!=1450 or len(imag)!=1350: raise ValueError('wrong tangent row count')
    return real,imag


def write_matrix(path,rows):
    with path.open('x',encoding='utf-8') as out:
        out.write(f'{len(rows)} 1000\n')
        for row in rows:
            entries=sorted(row.items())
            out.write(str(len(entries))+''.join(f' {i} {v}' for i,v in entries)+'\n')


def main():
    p=argparse.ArgumentParser();p.add_argument('w12',type=Path);p.add_argument('w13',type=Path)
    p.add_argument('out',type=Path);p.add_argument('real',type=Path);p.add_argument('imag',type=Path);a=p.parse_args()
    raw12=a.w12.read_bytes();raw13=a.w13.read_bytes()
    res12,v12,blocks12,l12=validate(json.loads(raw12),12)
    res13,v13,blocks13,l13=validate(json.loads(raw13),13)
    points=parker_oa()
    res12['source_reconstruction']=match_parker(v12,l12,res12['denominator'],points,'12')
    res13['source_reconstruction']=match_parker(v13,l13,res13['denominator'],points,'13')
    real,imag=sparse_tangents(v13,blocks13)
    write_matrix(a.real,real);write_matrix(a.imag,imag)
    result={'w12_sha256':sha(raw12),'w13_sha256':sha(raw13),'weisner':weisner_check(),
            'parker_strength_two_all_six_pairs':'PASS', 'w12':res12,'w13':res13,
            'tangent_matrices':{'real':str(a.real),'real_rows':len(real),'real_nnz':sum(map(len,real)),
                                'imag':str(a.imag),'imag_rows':len(imag),'imag_nnz':sum(map(len,imag)),
                                'columns':1000},
            'scope':'Exact integer constraints for these certificates; tangent matrix generation, not its rank or local integrability.'}
    with a.out.open('x',encoding='utf-8') as out: json.dump(result,out,indent=2);out.write('\n')
    json.dump(result,sys.stdout,indent=2);print()


if __name__=='__main__':main()
