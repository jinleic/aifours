#!/usr/bin/env python3
"""Finite exact controls for the 72-family probability/Bloch proof.

These bounded integer and support-set checks are not a proof over R or C.
"""
import argparse
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2))


def comp(pair):return tuple(x for x in range(4) if x not in pair)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def bounded(a,b,q):return all(2*x*y<=q for x,y in zip(a,b))


def good(P):
    for ij in PAIRS:
        i,j=ij;k,l=comp(ij)
        for ab in PAIRS:
            a,b=ab;c,d=comp(ab)
            if P[i][a]*P[j][b]+P[i][b]*P[j][a] != P[k][c]*P[l][d]+P[k][d]*P[l][c]:return False
    return True


def expected_shape(P):
    # Every column has a common baseline a and the outlier b lies once per row and color.
    counts={v:sum(x==v for row in P for x in row) for v in {x for row in P for x in row}}
    if len(counts)==1:return True
    if len(counts)!=2:return False
    return any(counts[a]==12 and counts[b]==4 and
      all(sum(x==b for x in row)==1 for row in P) and
      all(sum(P[i][g]==b for i in range(4))==1 for g in range(4)) for a,b in itertools.permutations(counts,2))


def integer_checks():
    result=[]
    for total in range(2,9):
        rows=[(x,y,z,total-x-y-z) for x in range(total+1) for y in range(total-x+1)
              for z in range(total-x-y+1)]
        count=0
        for i,a in enumerate(rows):
            for j in range(i,len(rows)):
                b=rows[j];q=dot(a,b)
                if q==0 or not bounded(a,b,q):continue
                cand=[k for k in range(j,len(rows)) if dot(a,rows[k])==q and dot(b,rows[k])==q
                      and bounded(a,rows[k],q) and bounded(b,rows[k],q)]
                for m,k in enumerate(cand):
                    c=rows[k]
                    for z in cand[m:]:
                        d=rows[z]
                        if dot(c,d)!=q or not bounded(c,d,q):continue
                        P=(a,b,c,d)
                        if not good(P):continue
                        if not expected_shape(P):raise ValueError(f'classification counterexample: {P}')
                        count+=1
        result.append({'row_sum':total,'row_choices':len(rows),'solutions_up_to_row_permutation':count})
    return result


def support_checks():
    # All four nonempty axis supports whose pairwise intersections are singleton
    # must have a common axis.
    sets=range(1,8);checked=0
    for P in itertools.product(sets,repeat=4):
        if not all((P[i]&P[j]).bit_count()==1 for i,j in PAIRS):continue
        checked+=1
        if not P[0]&P[1]&P[2]&P[3]:raise ValueError(f'axis-intersection counterexample {P}')
    # If all share one axis but each has a nonempty private remainder, four
    # remainders cannot be pairwise disjoint subsets of the other two axes.
    private=0
    for P in itertools.product(range(1,4),repeat=4):
        if all(not (P[i]&P[j]) for i,j in PAIRS):private+=1
    if private:raise ValueError('four nonempty private remainders found')
    return {'pairwise_singleton_intersection_cases':checked,'missing_common_axis_cases':0,
            'four_nonempty_private_remainders':private}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    ints=integer_checks();sets=support_checks()
    positive=((2,1,1,1),(1,2,1,1),(1,1,2,1),(1,1,1,2))
    negative=((3,0,1,1),(1,2,1,1),(1,1,2,1),(1,1,1,2))
    if not good(positive) or not expected_shape(positive):raise ValueError('positive control rejected')
    if good(negative):raise ValueError('negative pair-sum control accepted')
    result={'bounded_integer_cases':ints,'bloch_support_controls':sets,
            'positive_normal_form':'PASS','negative_pair_sum_mutation':'REJECTED',
            'scope':'Bounded exact integer/support checks only; universal classification and qubit proof are written separately.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
