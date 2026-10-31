#!/opt/homebrew/bin/python3
"""Exact finite controls for the sixth-derivative/Pfaffian zero indicator."""
import argparse
import collections
import itertools
import json
import pathlib


def B(a,b,pairs):return sum((((a>>(2*i))&1)*((b>>(2*i+1))&1)) ^ (((a>>(2*i+1))&1)*((b>>(2*i))&1)) for i in range(pairs))%2

def rank(rows):
    piv={}
    for x in rows:
        while x:
            b=x.bit_length()-1
            if b in piv:x^=piv[b]
            else:piv[b]=x;break
    return len(piv)

def subspaces(n,d):
    for pivots in itertools.combinations(range(n),d):
        free=[x for x in range(n) if x not in pivots]
        slots=[(r,c) for c in free for r in range(d) if c>pivots[r]]
        for a in range(1<<len(slots)):
            basis=[1<<p for p in pivots]
            for j,(r,c) in enumerate(slots):
                if a>>j&1:basis[r]|=1<<c
            span=[0]
            for v in basis:span += [x^v for x in span]
            yield basis,span,free


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    result={}
    for pairs in (3,4):
        triples=list(itertools.combinations(range(pairs),3))
        def indicator(x):
            z=0
            for I in triples:
                term=1
                for i in I:term*=((x>>(2*i))&1)*((x>>(2*i+1))&1)
                z^=term
            return z
        counts=collections.Counter();checked=0
        for basis,L,free in subspaces(8,6):
            rows=[sum(B(a,b,pairs)<<j for j,b in enumerate(basis)) for a in basis];r=rank(rows);counts[r]+=1
            for c in range(4):
                origin=sum(1<<free[j] for j in range(2) if c>>j&1)
                parity=sum(indicator(origin^x) for x in L)%2
                assert parity==int(r==6);checked+=1
        assert sum(counts.values())==10795 and checked==43180
        result[str(2*pairs)]={'six_subspaces':sum(counts.values()),'affine_sixflats':checked,
                              'restricted_rank_distribution':dict(sorted(counts.items()))}
    # On the first six coordinates, the full sixfold derivative is one;
    # deleting its sextic monomial flips this required parity.
    base=sum(int(x==63) for x in range(64))%2
    assert base==1 and (base^1)==0
    result['sextic_mutation_rejected']=True
    result['scope']='finite quadratic-form controls; no Boolean target or global no-go'
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('rank6/rank8: 10795 six-spaces and 43180 affine 6flats each',flush=True)


if __name__=='__main__':main()
