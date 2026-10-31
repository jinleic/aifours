#!/opt/homebrew/bin/python3
"""Finite controls for the cubic weight gap used in the rank-two branch."""
import argparse
import collections
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    allowed={0,64,96,112,120,128,136,144,160,192,256};ranks={}
    for r in range(5):
        counts=collections.Counter()
        for a in range(256):
            for c in range(2):
                wt=sum((sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(r))%2)
                       ^((a&x).bit_count()%2)^c for x in range(256))
                assert wt in allowed;counts[wt]+=1
        ranks[str(2*r)]={str(k):v for k,v in sorted(counts.items())}
    # Explicit Boolean cubics at the minimum and next-weight thresholds.
    minimum=[(x&1)*((x>>1)&1)*((x>>2)&1) for x in range(256)]
    second=[(x&1)*((((x>>1)&1)*((x>>2)&1))^(((x>>3)&1)*((x>>4)&1))) for x in range(256)]
    assert sum(minimum)==32 and sum(second)==48
    # If a weight w<48 cubic exists, every nonzero derivative has weight 64.
    # Its period subgroup would have size z=256-w(256-w)/32.
    impossible={}
    for w in (36,40,44):
        numerator=8192-w*(256-w)
        assert numerator<=0 or numerator%32!=0 or (numerator//32)&(numerator//32-1)
        impossible[str(w)]={'period_size_numerator':numerator,'period_size_denominator':32}
    assert 2*48==96  # threshold example is outside the strict <96 argument
    receipt={'rank_representatives_and_affine_shifts':ranks,'quadratic_weight_set':sorted(allowed),
             'cubic_minimum_example_weight':32,'cubic_next_weight_example':48,
             'period_equation_obstructions':impossible,'threshold_not_applied_at_48':True,
             'note':'finite checks supplement the all-variable proof'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('quadratic_representatives=2560 cubic_examples=32,48 excluded=36,40,44',flush=True)


if __name__=='__main__':main()
