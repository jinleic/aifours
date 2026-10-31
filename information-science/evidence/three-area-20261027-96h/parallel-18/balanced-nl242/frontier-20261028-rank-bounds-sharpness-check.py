#!/opt/homebrew/bin/python3
"""Finite controls for ten-point rank-six slices and a rank-eight quartic example."""
import argparse
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
                yield {origin^x for x in span}


def anf(values,n):
    a=values[:]
    for i in range(n):
        for x in range(1<<n):
            if x>>i&1:a[x]^=a[x^(1<<i)]
    return a


def q6(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    S8={0,1,2,7,11,31,47,63};S10={4,21,22,23,35,40,47,55,56,59}
    a=anf([int(x in S10) for x in range(64)],6)
    assert [x for x,v in enumerate(a) if v and x.bit_count()==4]==[15,51,60]
    assert max(x.bit_count() for x,v in enumerate(a) if v)==4
    xsum=0
    for x in S10:xsum^=x
    assert xsum==0
    flat_list=list(flats());assert len(flat_list)==2604
    assert max(len(F&S8) for F in flat_list)==5
    assert max(len(F&S10) for F in flat_list)==7
    for linear in range(64):
        for c in range(2):
            assert sum(q6(x)^((linear&x).bit_count()%2)^c for x in S10)%2==1
    def Q(x):return q6(x)^((x&12).bit_count()%2)^1
    assert sum(Q(x) for x in range(64))==28 and sum(Q(x) for x in S8)==7
    # Three 8-point slices and one 22-point slice give a quartic-only
    # rank-eight example with complement weight 46 and P-weight 210.
    h=[int((x&63) in S8) ^ (int((x>>6)==3)*Q(x&63)) for x in range(256)]
    assert sum(h)==46
    full=anf(h,8)
    quartic=[x for x,v in enumerate(full) if v and x.bit_count()==4]
    assert quartic==[15,51,60,195,204,240]
    assert max(x.bit_count() for x,v in enumerate(full) if v)==4
    receipt={'affine4flats_checked':len(flat_list),'simplex_max_intersection':5,
             'rank6_weight10_max_flat_intersection':7,'rank6_weight10_Q_shifts_checked':128,
             'fullrank_quartic_example_complement_weight':46,'fullrank_quartic_example_P_weight':210,
             'quartic_terms':quartic,'actual_boolean_witness':False,
             'scope':'sharpness only for the isolated quartic filter, not full Walsh realizability'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('fullrank_quartic_example_P=210 S10_max_intersection=7',flush=True)


if __name__=='__main__':main()
