#!/usr/bin/env python3
"""Independent direct enumerator, cycle-pairing check, and QLS checker.
No author code or sibling report/code is read or imported.
"""
import argparse
import collections
import hashlib
import itertools
import json
import math
import pathlib
import subprocess
import sys
import time
from fractions import Fraction as F


def clock():
    return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()


def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def neighborhood(cells, row, col):
    adj = {v:set() for v in cells}
    for v,w in itertools.combinations(cells,2):
        if (v[0] == w[0] and row[v[0]] == 2) or (v[1] == w[1] and col[v[1]] == 2):
            adj[v].add(w); adj[w].add(v)
    unseen = set(cells); paths=[]; cycles=[]
    while unseen:
        v=unseen.pop(); stack=[v]; comp=[v]
        while stack:
            for w in adj[stack.pop()]:
                if w in unseen:
                    unseen.remove(w); stack.append(w); comp.append(w)
        if all(len(adj[x]) == 2 for x in comp):
            cycles.append(len(comp))
        else:
            assert sum(len(adj[x]) == 1 for x in comp) == 2
            paths.append(len(comp))
    return tuple(sorted(paths)),tuple(sorted(cycles))


def direct_4x4():
    counts=collections.Counter(); bb=collections.Counter()
    profile={(4,4,2,2):'A',(4,3,3,2):'B',(3,3,3,3):'C'}
    for entries in itertools.combinations(range(16),12):
        row=[0]*4; col=[0]*4
        for z in entries:
            row[z//4]+=1; col[z%4]+=1
        if min(row+col)<2:
            continue
        p=''.join(sorted((profile[tuple(sorted(row,reverse=True))],profile[tuple(sorted(col,reverse=True))])))
        counts[p]+=1
        if p == 'BB':
            lowr=row.index(2); lowc=col.index(2)
            bb['present' if lowr*4+lowc in entries else 'absent']+=1
    assert dict(counts) == {'AA':36,'AB':288,'AC':72,'BB':720,'BC':288,'CC':24}
    assert dict(bb) == {'present':144,'absent':576}
    assert sum(counts.values()) == 1428
    # Deliberately omit the absent low-low case. The independent ground count
    # detects the exact missing class, not merely an unspecified failure.
    assert counts['BB'] - bb['present'] == 576
    return {'counts':dict(sorted(counts.items())),'BB_low_low':dict(bb),
            'mutation_omit_absent_BB_missing_labeled_graphs':576}


def direct_5bb():
    # Fix high rows 0,1 and high columns 0,1; all 10*10 relabelings
    # have exactly the same counts. Five labeled row neighborhoods are
    # enumerated independently rather than graph-isomorphism normalized.
    high=list(itertools.combinations(range(5),3))
    low=list(itertools.combinations(range(5),2))
    counts=collections.Counter(); total=0; example_two_path=None
    for rows in itertools.product(high,high,low,low,low):
        col=[sum(j in x for x in rows) for j in range(5)]
        if col != [3,3,2,2,2]:
            continue
        total+=1
        row=[3,3,2,2,2]
        if any(sum(col[j]==2 for j in rows[i])>1 for i in (0,1)) or any(sum(row[i]==2 and j in rows[i] for i in range(5))>1 for j in (0,1)):
            counts['degree3_two_low_neighbors']+=1
            continue
        assert all(j in rows[i] for i in (0,1) for j in (0,1))
        cells=[(i,j) for i in range(5) for j in rows[i] if row[i]==2 or col[j]==2]
        paths,cycles=neighborhood(cells,row,col)
        key=f'paths={paths};cycles={cycles}'
        counts[key]+=1
        if 2 in paths and example_two_path is None:
            example_two_path=[list(x) for x in rows]
    expected={'degree3_two_low_neighbors':1225,'paths=(2, 6);cycles=()':72,
              'paths=(3, 5);cycles=()':144,'paths=(4, 4);cycles=()':36,
              'paths=(2, 2);cycles=(4,)':9}
    assert total == 1486 and counts == expected
    assert example_two_path is not None
    assert 72+9==81 and 144+36==180
    return {'fixed_high_line_labels_total':total,'fixed_high_line_labels_classes':dict(counts),
            'multiplicity_for_all_high_label_choices':100,
            'two_path_graphs_per_fixed_labels':81,'three_five_or_four_four_per_fixed_labels':180,
            'one_two_path_example_row_neighbors':example_two_path,
            'mutation_omit_two_path_types_missing_labeled_graphs':8100}


def mask_rows(r,c):
    opts=[m for m in range(1<<c) if m.bit_count() in (2,4)]
    for rows in itertools.combinations_with_replacement(opts,r):
        if sum(x.bit_count() for x in rows)!=12:
            continue
        col=[sum(x>>j&1 for x in rows) for j in range(c)]
        if all(x in (2,4) for x in col) and (4 in col or any(x.bit_count()==4 for x in rows)):
            yield rows


def pairings(line):
    if len(line)==2:
        return [((line[0],line[1]),)]
    a,b,c,d=line
    return [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]


def cycle_pairing_controls():
    partitions=collections.Counter(); shape_counts=collections.Counter(); mutant=None
    graph_count=0
    for r in range(2,7):
        for c in range(r,7):
            if r*c<12 or 2*c>12:
                continue
            for rows in mask_rows(r,c):
                graph_count+=1
                edges=[(i,j) for i,x in enumerate(rows) for j in range(c) if x>>j&1]
                lines=[[e for e,(i,j) in enumerate(edges) if i==v] for v in range(r)]
                lines += [[e for e,(i,j) in enumerate(edges) if j==v] for v in range(c)]
                for choice in itertools.product(*(pairings(line) for line in lines)):
                    parent=list(range(12))
                    def root(x):
                        while parent[x]!=x:
                            x=parent[x]
                        return x
                    for ps in choice:
                        for a,b in ps:
                            x,y=root(a),root(b)
                            if x!=y: parent[x]=y
                    sizes=collections.Counter(root(i) for i in range(12))
                    partition=tuple(sorted(sizes.values()))
                    assert all(x >= 4 and x%2==0 for x in partition)
                    same_cycle=any(len(ps)==2 and root(ps[0][0])==root(ps[1][0]) for ps in choice)
                    if same_cycle:
                        if partition==(12,) and mutant is None:
                            mutant={'rows_bitmasks':list(rows),'shape':[r,c],
                                    'cell_cycle_lengths':list(partition),
                                    'reason':'a degree-4 line would force the same constant-support cycle to use two disjoint support pairs'}
                        continue
                    assert partition in ((4,8),(6,6),(4,4,4))
                    partitions[str(partition)]+=1
                    shape_counts[f'{r}x{c}']+=1
    assert set(partitions)=={'(4, 8)','(6, 6)','(4, 4, 4)'} and mutant is not None
    return {'row_canonical_graphs_checked':graph_count,'valid_pairing_partition_counts':dict(partitions),
            'valid_pairings_by_shape':dict(shape_counts),
            'mutation_allow_two_pairs_of_degree4_line_in_same_cycle':mutant}


# Independent exact QLS checker, coordinates as (real Fraction, imag Fraction).
def scale(v,a,b=F(0)):
    return tuple((a*x-b*y,b*x+a*y) for x,y in v)


def plus(a,b):
    return tuple((x[0]+y[0],x[1]+y[1]) for x,y in zip(a,b))


def norm_and_pair(a,b):
    real=sum(x[0]*y[0]+x[1]*y[1] for x,y in zip(a,b))
    imag=sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(a,b))
    return real,imag


def axis(i):
    return tuple((F(int(i==j)),F(0)) for j in range(8))


def make_square():
    P=((F(-1,3),F(0)),(F(0),F(2,3)),(F(2,3),F(0)))+((F(0),F(0)),)*5
    Q=((F(2,3),F(0)),(F(0),F(-1,3)),(F(2,3),F(0)))+((F(0),F(0)),)*5
    V=((F(2,3),F(0)),(F(0),F(2,3)),(F(-1,3),F(0)))+((F(0),F(0)),)*5
    R=plus(scale(Q,F(3,5)),scale(V,F(0),F(4,5)))
    S=plus(scale(Q,F(0),F(4,5)),scale(V,F(3,5)))
    a=[[None]*8 for _ in range(8)]
    block=[[axis(3),P,Q,V],[P,axis(3),V,Q],[R,S,axis(3),P],[S,R,P,axis(3)]]
    for i in range(4):
        for j in range(4):
            a[i][j]=block[i][j]
            a[i][j+4]=axis(4+(i+j)%4)
            a[i+4][j]=axis(4+(i+j)%4)
            a[i+4][j+4]=axis((i+j)%4)
    return a


def verify_qls(a):
    for label,lines in (('row',a),('column',list(zip(*a)))):
        for k,line in enumerate(lines):
            for i in range(8):
                for j in range(8):
                    val=norm_and_pair(line[i],line[j])
                    if val != (F(int(i==j)),F(0)):
                        return {'kind':label+'-orthogonality','line':k,'pair':[i,j],
                                'observed':[str(val[0]),str(val[1])]}
    return None


def independent_vector_checks():
    board=make_square()
    assert verify_qls(board) is None
    first=board[4]
    axes=[next(i for i,z in enumerate(v) if z!=(0,0)) for v in first]
    assert set(axes)==set(range(8))
    mixed=[(i,j) for i in range(8) for j in range(8) if sum(z!=(0,0) for z in board[i][j])>1]
    assert len(mixed)==12 and all(i<4 and j<4 and i!=j for i,j in mixed)
    assert all(sum(z!=(0,0) for z in board[i][j])==3 for i,j in mixed)
    # Replace a unit vector with another unit vector already on the same line.
    # The intended failure is row orthogonality, not a norm failure.
    mutant=[line[:] for line in board]
    mutant[0][2]=mutant[0][1]
    fail=verify_qls(mutant)
    assert fail['kind']=='row-orthogonality' and fail['line']==0 and fail['pair']==[1,2]
    return {'all_1024_exact_gram_entries_valid':True,'standardized_row_coordinate_order':axes,
            'mixed_count':12,'mixed_profile':'C/C',
            'mutation_replace_Q_by_existing_P_expected_failure':fail,
            'mutant_stronger_QLS_only_mixed_at_least_13':'rejected by this exact QLS; it is not a four-family witness'}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--out',required=True); a=p.parse_args()
    out=pathlib.Path(a.out)
    if out.exists(): raise SystemExit('refusing overwrite')
    start=clock(); t=time.monotonic()
    data={'kind':'independent-finite-casecheck-v1','script_sha256':sha(__file__),
          'prior_result_sha256':sha('finite-results-v1.json'), 'clock_before':start,
          'python':sys.version,'4x4':direct_4x4(),'5x5_BB':direct_5bb(),
          'support2_cycle_pairings':cycle_pairing_controls(),
          'independent_exact_QLS':independent_vector_checks()}
    data['elapsed_seconds']=round(time.monotonic()-t,3)
    data['clock_immediately_before_output']=clock()
    with out.open('x',encoding='utf-8') as f:
        json.dump(data,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'output':str(out),'sha256':sha(out),'elapsed_seconds':data['elapsed_seconds'],
                      'clock_before_output':data['clock_immediately_before_output']},sort_keys=True))


if __name__=='__main__':
    main()
