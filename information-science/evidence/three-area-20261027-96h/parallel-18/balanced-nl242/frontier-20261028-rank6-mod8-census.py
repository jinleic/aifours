#!/opt/homebrew/bin/python3
"""Exact F2-cubic relaxation census for rank-six k mod8 and four zeros."""
import argparse
import collections
import itertools
import json
import pathlib


TERMS=[sum(1<<i for i in subset) for d in range(4) for subset in itertools.combinations(range(8),d)]
N=len(TERMS)


def calc(arf):
    def g0(x):
        return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+arf*((x&1)+((x>>1)&1))
    rows=[];odd=[]
    for x in range(256):
        g=g0(x)
        if g%2:odd.append(x);continue
        lhs=sum(1<<j for j,t in enumerate(TERMS) if x&t==t)
        rhs=((g//2)&1)^int((x&63)!=0)
        rows.append((lhs,rhs,x))
    pivots={};dependent=None
    for original,rhs,x in rows:
        lhs=original;v=rhs
        while lhs:
            p=lhs.bit_length()-1
            if p in pivots:lhs^=pivots[p][0];v^=pivots[p][1]
            else:pivots[p]=(lhs,v);break
        if not lhs:
            assert not v
            if dependent is None:dependent=(original,rhs,x)
    assert dependent is not None
    # Changing a dependent equation's RHS produces an independently detected inconsistency.
    lhs,v,_=dependent;v^=1
    while lhs:
        p=lhs.bit_length()-1;lhs^=pivots[p][0];v^=pivots[p][1]
    assert v==1
    free=[j for j in range(N) if j not in pivots]
    def resolve(seed,inhomogeneous):
        x=seed
        for p in sorted(pivots):
            lhs,rhs=pivots[p]
            value=((x&(lhs^(1<<p))).bit_count()%2)^(rhs if inhomogeneous else 0)
            if value:x|=1<<p
        return x
    first=resolve(0,True);basis=[resolve(1<<j,False) for j in free]
    for lhs,rhs,_ in rows:
        assert (first&lhs).bit_count()%2==rhs
        assert all((b&lhs).bit_count()%2==0 for b in basis)
    evaluation=[sum(1<<j for j,t in enumerate(TERMS) if x&t==t) for x in odd]
    def image(coeff):return sum(1<<i for i,row in enumerate(evaluation) if (coeff&row).bit_count()%2)
    current=sum(1<<i for i,x in enumerate(odd) if g0(x)%4==3)^image(first)
    delta=[image(v) for v in basis];counts=collections.Counter();oldgray=0
    for index in range(1<<len(free)):
        gray=index^(index>>1)
        if index:current ^= delta[(gray^oldgray).bit_length()-1]
        oldgray=gray;counts[current.bit_count()]+=1
    assert sum(counts.values())==1<<len(free)
    return {'arf':arf,'variables':N,'q_zero_points':len(rows),'q_one_points':len(odd),
            'rank':len(pivots),'nullity':len(free),'solution_count':1<<len(free),
            'residue3_count_histogram':{str(k):v for k,v in sorted(counts.items())},
            'dependent_rhs_mutation_rejected':True,'mutated_point':dependent[2]}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    assert N==93
    data={'interpretation':'necessary mod8 polynomial relaxation only; no Boolean realization',
          'models':[calc(0),calc(1)]}
    with args.output.open('x',encoding='utf-8') as out:json.dump(data,out,indent=2,sort_keys=True);out.write('\n')
    for m in data['models']:print('arf=',m['arf'],'rank=',m['rank'],'nullity=',m['nullity'],'hist=',m['residue3_count_histogram'],flush=True)


if __name__=='__main__':main()
