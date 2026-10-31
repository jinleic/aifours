#!/opt/homebrew/bin/python3
"""Finite controls for the rank-two cubic minimum-support boundary."""
import argparse
import collections
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    # An explicit affine five-flat and its full period/derivative census.
    S={x for x in range(256) if (x&7)==5};assert len(S)==32
    periods=[];weights=collections.Counter()
    for v in range(256):
        shifted={x^v for x in S};d=len(S^shifted);weights[d]+=1
        if not d:periods.append(v)
    assert len(periods)==32 and set(weights)=={0,64} and weights[64]==224
    assert all((x^y) in periods for x in periods for y in periods)
    # Every affine shift of a rank-two quadratic on F_2^5, and every affine
    # function, has support a multiple of eight.
    counts=collections.Counter()
    for isquadratic in (0,1):
        for linear in range(32):
            for c in range(2):
                w=sum((isquadratic*((x&1)*((x>>1)&1)))^((linear&x).bit_count()%2)^c for x in range(32))
                assert w%8==0;counts[(isquadratic,w)]+=1
    receipt={'fiveflat_weight':32,'period_count':len(periods),'derivative_weight_counts':dict(sorted(weights.items())),
             'rank0_rank2_fivevariable_affine_shifts_checked':128,
             'restricted_Q_weight_multiples_of_8':True,
             'weight_distribution':[{'rank2':bool(q),'weight':w,'forms':n} for (q,w),n in sorted(counts.items())],
             'note':'finite controls; the written proof is all-variable'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('weight32 periods=32 rank0/2_shift_controls=128',flush=True)


if __name__=='__main__':main()
