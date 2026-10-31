#!/usr/bin/env python3
"""Independent exact controls for the N47 heavy-support CNF primitives.

Checks every at-most counter at n<=8 on all input assignments: valid inputs
have a constructed satisfying extension, invalid inputs cause unit propagation
conflict. Separately exhausts the 16-cell (y,h) truth relation and constructs a
20-word relaxed support satisfying the shared degree/heavy constraints on two
opposite party pairs. No encoder or mathematical theorem is accepted here.
"""
import argparse
from collections import Counter
import importlib.util
import itertools
import json
from pathlib import Path


def load(path):
    s=importlib.util.spec_from_file_location('heavy_encoder',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def unit_conflict(clauses,assignment):
    a=dict(assignment)
    while True:
        changed=False
        for row in clauses:
            unknown=[];sat=False
            for lit in row:
                if abs(lit) not in a:unknown.append(lit)
                elif a[abs(lit)]==(lit>0):sat=True;break
            if sat:continue
            if not unknown:return True
            if len(unknown)==1:a[abs(unknown[0])]=(unknown[0]>0);changed=True
        if not changed:return False


def all_satisfied(clauses,a):
    return all(any(a[abs(x)]==(x>0) for x in row) for row in clauses)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('encoder',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args();enc=load(a.encoder)
    valid=invalid=0
    for n in range(1,9):
      for k in range(n+1):
       for polarity in (1,-1):
        e=enc.Encoder();xs=[e.var() for _ in range(n)];e.amk([polarity*x for x in xs],k)
        for bits in itertools.product((False,True),repeat=n):
            base={i+1:bits[i] for i in range(n)};count=sum(b if polarity==1 else not b for b in bits)
            if count>k:
                if not unit_conflict(e.C,base):raise ValueError('invalid counter input did not conflict')
                invalid+=1
            else:
                extended=dict(base)
                if 0<k<n:
                    for i in range(n-1):
                        prefix=sum(b if polarity==1 else not b for b in bits[:i+1])
                        for j in range(k):extended[n+i*k+j+1]=prefix>=j+1
                if not all_satisfied(e.C,extended):raise ValueError('valid counter input lacks canonical extension')
                valid+=1
    # Relation for a pair cell: y iff at least one; y=>at least2; cap3;
    # h=>at least3; count>=3=>h. This is exactly count in {0,2,3}.
    rel=0
    for count in range(17):
      for y,h in itertools.product((False,True),repeat=2):
        constraints=(y==(count>0)) and (not y or count>=2) and count<=3 and (not h or (y and count>=3)) and (count<3 or h)
        expected=(count,y,h) in ((0,False,False),(2,True,False),(3,True,True))
        if constraints!=expected:raise ValueError('pair-cell truth relation')
        rel+=1
    # Fixed 4x4 count matrix: local degrees(2,2,2,3), heavy excess(1,1,0,0).
    matrix=((3,0,0,2),(0,3,0,2),(2,0,2,0),(0,2,2,2))
    AB=[(i,j) for i in range(4) for j in range(4) for rep in range(matrix[i][j])]
    seed=20261029;selected=None
    for attempt in range(2000):
        CD=AB[:]
        for i in range(len(CD)-1,0,-1):
            seed=(1664525*seed+1013904223)%(1<<32);j=seed%(i+1);CD[i],CD[j]=CD[j],CD[i]
        S=[ab+cd for ab,cd in zip(AB,CD)]
        if len(set(S))==20:selected=S;break
    if selected is None:raise ValueError('relaxed positive construction')
    for i in range(4):
        if [sum(q[i]==v for q in selected) for v in range(4)]!=[5,5,4,6]:raise ValueError('relaxed fiber count')
    for i,j in ((0,1),(2,3)):
        C=Counter((q[i],q[j]) for q in selected)
        if len(C)!=9 or Counter(C.values())!={2:7,3:2}:raise ValueError('relaxed pair multiplicity')
    result={'counter_valid_assignments_with_satisfying_aux_extension':valid,
      'counter_invalid_assignments_rejected_by_unit_propagation':invalid,
      'pair_cell_truth_relation_cases':rel,'relaxed_positive_support':sorted(selected),
      'relaxed_positive_pairs':[[0,1],[2,3]],'relaxed_positive_fibers':[5,5,4,6],
      'scope':'Exact primitive-gadget and relaxed-support controls; no full N47 support, no proof of encoder completeness.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='relaxed_positive_support'},indent=2))


if __name__=='__main__':main()
