#!/opt/homebrew/bin/python3
"""Exhaust quadratic weights and simplex/affine-flat intersections in F_2^6."""
import argparse
import collections
import itertools
import json
import pathlib


def flats():
    for pivots in itertools.combinations(range(6),4):
        free=[j for j in range(6) if j not in pivots]
        slots=[(r,c) for c in free for r in range(4) if c>pivots[r]]
        for assignment in range(1<<len(slots)):
            basis=[1<<p for p in pivots]
            for j,(r,c) in enumerate(slots):
                if assignment>>j&1:basis[r]|=1<<c
            span=[0]
            for v in basis:span += [x^v for x in span]
            for coset in range(4):
                origin=sum(1<<free[j] for j in range(2) if coset>>j&1)
                yield sum(1<<(origin^x) for x in span)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    simplex={0,1,2,7,11,31,47,63};smask=sum(1<<x for x in simplex)
    allflats=set(flats());assert len(allflats)==2604
    inter=collections.Counter((smask&F).bit_count() for F in allflats)
    assert max(inter)==5
    changed=collections.Counter((smask^F).bit_count() for F in allflats)
    assert min(changed)>=14
    # Exhaust the 22 coefficients of a quadratic polynomial on six variables.
    terms=[m for m in range(64) if m.bit_count()<=2]
    masks=[sum(1<<x for x in range(64) if x&m==m) for m in terms]
    assert len(terms)==22
    q=0;oldgray=0;weights=collections.Counter();weight16=0
    for i in range(1<<22):
        gray=i^(i>>1)
        if i:q^=masks[(gray^oldgray).bit_length()-1]
        oldgray=gray;wt=q.bit_count();weights[wt]+=1
        if wt==16:
            assert q in allflats;weight16+=1
        elif wt:assert wt>=24
    assert weight16==2604
    # A rank-six quartic-form slice of weight ten does exist; this control
    # prevents confusing the eight-point lower bound with a stronger claim.
    S10={4,21,22,23,35,40,47,55,56,59};a=[int(x in S10) for x in range(64)]
    for i in range(6):
        for x in range(64):
            if x>>i&1:a[x]^=a[x^(1<<i)]
    degree=max(x.bit_count() for x,v in enumerate(a) if v)
    quartic=[x for x,v in enumerate(a) if v and x.bit_count()==4]
    assert degree==4 and quartic==[15,51,60]
    receipt={'affine_four_flats':len(allflats),'simplex_intersection_histogram':dict(sorted(inter.items())),
             'largest_flat_intersection':max(inter),'smallest_distinct_quadratic_slice_weight':min(changed),
             'quadratics_checked':1<<22,'quadratic_weight_distribution':dict(sorted(weights.items())),
             'all_weight16_quadratics_are_affine4flat_indicators':True,
             'rank6_quartic_weight10_control':sorted(S10),'rank6_quartic_weight10_degree':degree,
             'note':'finite controls; the all-variable bound is proved separately'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('quadratics=',1<<22,'flat_count=',len(allflats),'simplex_max_intersection=',max(inter),flush=True)


if __name__=='__main__':main()
