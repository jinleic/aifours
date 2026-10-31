#!/usr/bin/env python3
"""Exact tiny controls for the common-three-cut heavy-core obstruction.

All-split: label the two heavy symbols at each party by0,1. Heavy pair edges
are matchings x_i xor x_j=e_ij. In each complementary cut, the full heavy-row by
heavy-column2x2 rectangle is forced by the eight-entry3x3 unitary block. Union
those forced words and check the elementary obstructions in the written proof.
No SAT solver, phase solver or research checker is imported.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2));CUTS=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
BINARY=list(itertools.product((0,1),repeat=4))


def heavy(q,p,e):return (q[p[0]]^q[p[1]])==e[p]

def core(e):return {q for q in BINARY if any(heavy(q,A,e) and heavy(q,B,e) for A,B in CUTS)}

def completions(e,i,a):
    C={q for q in core(e) if q[i]==a};universe=[q for q in BINARY if q[i]==a]
    found=[]
    for F in itertools.combinations(universe,5):
        F=set(F)
        if not C<=F:continue
        if all(sum(q[j]==(a^e[tuple(sorted((i,j)))]) for q in F)==3 for j in range(4) if j!=i):found.append(F)
    return found


def overfull(S,e):
    for ij in PAIRS:
        counts=Counter((q[ij[0]],q[ij[1]]) for q in S)
        for vals,n in counts.items():
            cap=3 if (vals[0]^vals[1])==e[ij] else 2
            if n>cap:return {'pair':ij,'value':vals,'count':n,'cap':cap}
    return None


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    patterns=Counter();balanced_checks=anti_fibers=anti_two=0;examples={}
    triangles=list(itertools.combinations(range(4),3))
    for bits in itertools.product((0,1),repeat=6):
        e=dict(zip(PAIRS,bits));parities=[e[i,j]^e[i,k]^e[j,k] for i,j,k in triangles];C=core(e)
        if not any(parities):
            patterns['balanced']+=1
            if len(C)!=8 or overfull(C,e):raise ValueError('balanced core control')
            for i in range(4):
                for b in (0,1):
                    if len([q for q in C if q[i]==b])!=4 or completions(e,i,b):raise ValueError('balanced low-heavy fiber unexpectedly feasible')
                    balanced_checks+=1
        elif all(parities):
            patterns['antibalanced']+=1
            if len(C)!=6 or overfull(C,e):raise ValueError('antibalanced nonvacuity core')
            forced={}
            for i in range(4):
                for b in (0,1):
                    F=completions(e,i,b)
                    if len(F)!=1:raise ValueError('antibalanced five-point completion not unique')
                    forced[i,b]=F[0];anti_fibers+=1
            for i,j in PAIRS:
                for b,c in itertools.product((0,1),repeat=2):
                    union=C|forced[i,b]|forced[j,c];w=overfull(union,e)
                    if w is None:raise ValueError('two low-heavy fibers without pair overload')
                    anti_two+=1
                    if 'antibalanced_overload' not in examples:examples['antibalanced_overload']={'signs':bits,'low_heavy_symbols':[[i,b],[j,c]],'witness':w}
        else:
            patterns['mixed']+=1
            w=overfull(C,e)
            if w is None:raise ValueError('mixed core without immediate overload')
            if 'mixed_overload' not in examples:examples['mixed_overload']={'signs':bits,'core_size':len(C),'witness':w}
    # Merged A, three split parties B,C,D. The forced core is a union of the
    # three pair-matching cylinders on the binary3-cube.
    merged=Counter()
    triples=list(itertools.product((0,1),repeat=3))
    for eBC,eBD,eCD in itertools.product((0,1),repeat=3):
        G={q for q in triples if (q[0]^q[1])==eBC or (q[0]^q[2])==eBD or (q[1]^q[2])==eCD}
        rows={b:{(q[1],q[2]) for q in G if q[0]==b} for b in (0,1)}
        if eBC^eBD^eCD==0:
            if len(G)!=8 or any(len(x)!=4 for x in rows.values()):raise ValueError('merged balanced triangle')
            merged['pair_cap_overload']+=1
        else:
            if len(G)!=6 or any(len(x)!=3 for x in rows.values()) or rows[0]==rows[1]:raise ValueError('merged frustrated row supports')
            merged['heavy_rows_different_3column_supports']+=1
    if dict(patterns)!={'balanced':8,'mixed':48,'antibalanced':8} or balanced_checks!=64 or anti_fibers!=64 or anti_two!=192:
        raise ValueError('unexpected signed-core coverage counts')
    result={'signed_K4_patterns':dict(patterns),'balanced_low_heavy_fibers_rejected':balanced_checks,
      'antibalanced_unique_five_point_fibers':anti_fibers,'antibalanced_two_party_low_heavy_overloads':anti_two,
      'merged_triangle_cases':dict(merged),'examples':examples,
      'scope':'Exact finite controls of a small written heavy-core proof; no global AME theorem, certificate checker, or SAT invocation.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
