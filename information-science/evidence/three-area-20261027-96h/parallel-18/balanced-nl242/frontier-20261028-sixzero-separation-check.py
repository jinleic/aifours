#!/opt/homebrew/bin/python3
"""Finite controls for the six-point mixed-energy separation argument."""
import argparse
import collections
import itertools
import json
import pathlib


def B8(a,b):return sum((((a>>(2*i))&1)*((b>>(2*i+1))&1)) ^ (((a>>(2*i+1))&1)*((b>>(2*i))&1)) for i in range(4))%2

def subspaces(n,d):
    for pivots in itertools.combinations(range(n),d):
        free=[x for x in range(n) if x not in pivots]
        slots=[(r,c) for c in free for r in range(d) if c>pivots[r]]
        for a in range(1<<len(slots)):
            basis=[1<<x for x in pivots]
            for i,(r,c) in enumerate(slots):
                if a>>i&1:basis[r]|=1<<c
            span=[0]
            for v in basis:span += [x^v for x in span]
            yield basis,span


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    Z={0,1,4,16,64,85};diffs=Z-{0};assert len(Z)==6
    incidences=collections.Counter();Dcount=0;avoid8=0
    for basis,D in subspaces(8,3):
        if any(B8(x,y) for x,y in itertools.combinations(basis,2)):continue
        Dcount+=1;L={x for x in range(256) if all(not B8(x,d) for d in basis)}
        assert len(L)==32
        for x in L-{0}:incidences[x]+=1
        if not (diffs&L):avoid8+=1
    assert Dcount==11475 and len(incidences)==255 and set(incidences.values())=={1395}
    assert avoid8>=11475-5*1395>0
    # A rank-six radical vector r=128 and all five-spaces containing it are
    # parameterized by four-spaces of the seven-dimensional quotient.
    r=128;assert r not in diffs
    Lcount=0;avoid6=0;perdiff=collections.Counter();first=None
    for basis,Lbar in subspaces(7,4):
        L=set(Lbar)|{x^r for x in Lbar};assert len(L)==32
        Lcount+=1
        for d in diffs:
            if d in L:perdiff[d]+=1
        if not diffs.intersection(L):
            avoid6+=1
            if first is None:first=L
    assert Lcount==11811 and set(perdiff.values())=={1395}
    assert avoid6>=11811-5*1395>0 and first is not None
    def q(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2
    # Enumerate the eight cosets of first and check q/4 parity is constant.
    unused=set(range(256));parities=[]
    while unused:
        a=min(unused);A={a^x for x in first};unused-=A
        nq=sum(q(x) for x in A);assert nq%4==0;parities.append((nq//4)%2)
    assert len(parities)==8 and len(set(parities))==1
    receipt={'rank8_isotropic3_subspaces':Dcount,'rank8_per_nonzero_incidence':1395,
             'rank8_separating_count_for_control':avoid8,'rank6_five_spaces_through_r':Lcount,
             'rank6_per_difference_incidence':1395,'rank6_separating_count_for_control':avoid6,
             'rank6_coset_quadratic_parities':parities,'control_six_points':sorted(Z),
             'scope':'finite geometric controls; no Boolean target asserted'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('rank8=',Dcount,'avoid=',avoid8,'rank6=',Lcount,'avoid=',avoid6,flush=True)


if __name__=='__main__':main()
