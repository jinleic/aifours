#!/usr/bin/env python3
"""Tiny exact controls for the two partial support48 written arguments.

1. Full3x3 heavy block: a one-cut heavy rectangle is consistent with multiplicity3,
   while all3 major/minor rectangles force4 extensions of every major/major pair.
2. Exact3x3 Fourier Gram over Z[omega], omega^2+omega+1=0, is3I (nonvacuity).
3. Perfect-match partitions of6 fibers yield self-dual F2 column spaces; two such
   spaces are orthogonal exactly when the partitions coincide.
No global AME or support48 feasibility conclusion is computed.
"""
import argparse
import itertools
import json
from pathlib import Path

CUTS=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))


def heavy(q,p,m):return not(q[p[0]]!=m[p[0]] and q[p[1]]!=m[p[1]])


def mul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)


def conj(x):return (x[0]-x[1],-x[1])

def omega(e):return ((1,0),(0,1),(-1,-1))[e%3]


def matchings(values):
    if not values:yield ();return
    first=values[0]
    for partner in values[1:]:
        rest=[x for x in values if x not in (first,partner)]
        for tail in matchings(rest):yield ((first,partner),)+tail


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args();overloads=single=0
    for m in itertools.product((0,1),repeat=4):
        cube=list(itertools.product((0,1),repeat=4))
        F={q for q in cube if any(heavy(q,A,m) and heavy(q,B,m) for A,B in CUTS)}
        one={q for q in cube if heavy(q,CUTS[0][0],m) and heavy(q,CUTS[0][1],m)}
        if len(F)!=11 or len(one)!=9:raise ValueError('full-three heavy core sizes')
        for i,j in itertools.combinations(range(4),2):
            count=sum((q[i],q[j])==(m[i],m[j]) for q in F)
            if count!=4:raise ValueError('major pair not overloaded')
            overloads+=1
        if sum((q[0],q[1])==(m[0],m[1]) for q in one)!=3:raise ValueError('one-cut positive control')
        single+=1
    checked=0
    for i,j in itertools.product(range(3),repeat=2):
        acc=(0,0)
        for k in range(3):
            v=mul(omega(i*k),conj(omega(j*k)));acc=(acc[0]+v[0],acc[1]+v[1])
        if acc!=((3 if i==j else 0),0):raise ValueError('Fourier exact Gram')
        checked+=1
    M=list(matchings(list(range(6))))
    if len(M)!=15:raise ValueError('six-fiber matching count')
    equal=unequal=0
    for P,Q in itertools.product(M,repeat=2):
        B=[sum(1<<v for v in pair) for pair in P];C=[sum(1<<v for v in pair) for pair in Q]
        ortho=all((x&y).bit_count()%2==0 for x in B for y in C)
        if ortho!=(set(map(frozenset,P))==set(map(frozenset,Q))):raise ValueError('partition orthogonality characterization')
        if ortho:equal+=1
        else:unequal+=1
        if not all((x&y).bit_count()%2==0 for x in B for y in B):raise ValueError('matching span not self-orthogonal')
    result={'major_minor_labelings':16,'major_pair_overloads':overloads,'single_cut_rectangles_with_cap3':single,
      'Fourier3_exact_Zomega_Gram_entries':checked,'six_fiber_partitions':15,
      'equal_partition_orthogonal_pairs':equal,'unequal_partition_nonorthogonal_pairs':unequal,
      'scope':'Tiny exact controls of partial support48 arguments; not a proof, witness, or global exclusion.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
