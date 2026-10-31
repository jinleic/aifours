#!/opt/homebrew/bin/python3
"""Exhaust all affine shifts of a fixed quadratic on a symplectic simplex."""
import argparse
import collections
import json
import pathlib


def q(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    S=[0,1,2,7,11,31,47,63];counts=collections.Counter();seen=set()
    for a in range(64):
        for c in range(2):
            def Q(x):return q(x)^((a&x).bit_count()%2)^c
            bits=tuple(Q(x) for x in S);t=sum(bits);assert t in (1,3,5,7)
            assert bits not in seen;seen.add(bits)
            G=sum(1-2*Q(x) for x in range(64));expected=8*(-1 if ((t+1)//2)%2 else 1)
            assert G==expected
            w=4*sum(Q(x) for x in range(64));counts[(w,4*t)]+=1
    assert len(seen)==128
    assert counts=={(112,12):56,(112,28):8,(144,4):8,(144,20):56}
    # A nonzero radical linear term is balanced on each two-dimensional fiber.
    for c in (1,2,3):
        assert sum((c&r).bit_count()%2 for r in range(4))==2
    receipt={'simplex_vertices':S,'distinct_odd_sign_patterns':len(seen),
             'nonbalanced_pairs':[{'Q_weight':w,'intersection':v,'forms':count} for (w,v),count in sorted(counts.items())],
             'balanced_radical_case':{'Q_weight':128,'intersection':16},
             'gauss_sum_formula_checked':True,'note':'finite control; proof covers all simplexes'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('all=128 phase_pairs=',dict(counts),flush=True)


if __name__=='__main__':main()
