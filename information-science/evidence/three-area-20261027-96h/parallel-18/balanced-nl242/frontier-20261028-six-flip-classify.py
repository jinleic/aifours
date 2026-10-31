#!/opt/homebrew/bin/python3
"""Classify the independently enumerated 6-flip sets by affine rank and spectrum."""
import argparse
import collections
import json
import pathlib


def affine_rank(points):
    basis={}
    for p in points[1:]:
        v=p^points[0]
        while v:
            i=v.bit_length()-1
            if i not in basis:
                basis[i]=v
                break
            v ^= basis[i]
    return len(basis)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    args=p.parse_args()
    if args.output.exists(): raise FileExistsError(args.output)
    doc=json.loads(args.input.read_text(encoding='utf-8'))
    if not doc['complete'] or doc['target_met']: raise ValueError('not a completed target-free enumeration')
    sets=[tuple(r['flips']) for r in doc['six_sets']]
    assert len(sets)==len(set(sets))==doc['compatible_sixes_checked']
    assert all(len(s)==6 and sorted(s)==list(s) and len(set(s))==6 and 0<=s[0]<s[-1]<512 for s in sets)
    classes=collections.Counter((r['peak'],r['zero_count'],affine_rank(r['flips'])) for r in doc['six_sets'])
    receipt={'seed_index_1based':doc['seed_index_1based'], 'compatible_sixes':len(sets),
             'classes':[{'peak':p,'zero_count':z,'affine_rank':d,'count':n} for (p,z,d),n in sorted(classes.items())],
             'all_in_affine_4flat':all(affine_rank(s)<=4 for s in sets)}
    assert sum(r['count'] for r in receipt['classes'])==len(sets)
    with args.output.open('x',encoding='utf-8') as out: json.dump(receipt,out,indent=2,sort_keys=True); out.write('\n')
    print(receipt)


if __name__=='__main__': main()
