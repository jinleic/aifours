#!/opt/homebrew/bin/python3
"""Counterexample to summing four congruent mod4 coset weights as divisible by8."""
import argparse
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    terms=(7,56,193)
    h=[sum((x&t)==t for t in terms)%2 for x in range(256)]
    cosets=[sum(h[x] for x in range(256) if x&3==i) for i in range(4)]
    acoeff=h[:]
    for j in range(8):
        for x in range(256):
            if x&(1<<j):acoeff[x]^=acoeff[x^(1<<j)]
    assert [i for i,v in enumerate(acoeff) if v]==list(terms)
    assert cosets==[8,20,8,32] and len({v%4 for v in cosets})==1
    assert sum(h)==68 and sum(h)%8==4
    out={'scope':'eight-variable cubic algebraic counterexample; NOT a Boolean target witness',
         'ANF_masks':list(terms),'degree':3,'coset_weights':cosets,
         'coset_weights_equal_mod4':True,'total_weight':68,'total_mod8':4}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('cubic weight68; four six-coset weights 8,20,8,32 all congruent 0 mod4')


if __name__=='__main__':main()
