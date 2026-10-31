#!/opt/homebrew/bin/python3
"""Finite controls for the even-q/odd-P fourth-derivative coupling."""
import argparse
import itertools
import json
import pathlib
import random


def rank(rows):
    piv={}
    for row in rows:
        x=row
        while x:
            b=x.bit_length()-1
            if b in piv:x^=piv[b]
            else:piv[b]=x;break
    return len(piv)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    # All 4-variable quadratic parts, affine terms and constants: the mod-4
    # weight is twice the Pfaffian, independently of affine terms.
    pairs=list(itertools.combinations(range(4),2));cases=0
    for Bmask in range(64):
        rows=[0]*4
        for i,(a,b) in enumerate(pairs):
            if Bmask>>i&1:rows[a]|=1<<b;rows[b]|=1<<a
        r=rank(rows);assert r in (0,2,4)
        for linear in range(32):
            wt=0
            for x in range(16):
                v=(linear>>4)&1
                for i in range(4):v^=((linear>>i)&1)*((x>>i)&1)
                for i,(a,b) in enumerate(pairs):v^=((Bmask>>i)&1)*((x>>a)&1)*((x>>b)&1)
                wt+=v
            assert wt%4==(2 if r==4 else 0);cases+=1
    assert cases==2048
    # On F_2^8 construct the predicted quartic term for every possible polar
    # rank and sample lower-degree terms; check all 70 coordinate 4-flats.
    rng=random.Random(20261028);lower=[m for m in range(256) if m.bit_count()<=3]
    masks={m:sum(1<<x for x in range(256) if x&m==m) for m in range(256) if m.bit_count()<=4}
    summaries={};first_rank6=None
    for r in range(5):
        quartic=[(3<<(2*i))|(3<<(2*j)) for i in range(r) for j in range(i+1,r)]
        count=0
        for _ in range(25):
            P=0
            for m in quartic:P^=masks[m]
            for m in lower:
                if rng.getrandbits(1):P^=masks[m]
            assert P.bit_count()%4==(2 if r==4 else 0)
            for coords in itertools.combinations(range(8),4):
                origin=rng.randrange(256);parity=0
                for select in range(16):
                    x=origin
                    for j,c in enumerate(coords):
                        if select>>j&1:x^=1<<c
                    parity^=(P>>x)&1
                def B(i,j):return int(i//2==j//2 and i!=j and i//2<r)
                a,b,c,d=coords;pf=B(a,b)*B(c,d)^B(a,c)*B(b,d)^B(a,d)*B(b,c)
                assert parity==pf;count+=1
            if r==3 and first_rank6 is None:first_rank6=P
        summaries[str(2*r)]={'sample_polynomials':25,'coordinate_4flat_checks':count,
                             'peak_unit_weight_mod4':2 if r==4 else 0}
    # A single quartic mutation breaks a forced fourth derivative.
    mutated=first_rank6^masks[15]
    def derivative(bits):return sum((bits>>x)&1 for x in range(16))%2
    assert derivative(mutated)!=derivative(first_rank6)
    receipt={'four_variable_quadratic_affine_cases':cases,'all_expected_weight_mod4':True,
             'rank_samples':summaries,'quartic_mutation_rejected':True,
             'note':'finite checks; all-variable result needs the written proof'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('quadratic4=',cases,'rank_samples=',125,'4flat_checks=',8750,flush=True)


if __name__=='__main__':main()
