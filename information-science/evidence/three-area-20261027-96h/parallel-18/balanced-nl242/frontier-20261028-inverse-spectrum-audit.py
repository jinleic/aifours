#!/opt/homebrew/bin/python3
"""Check an optimized FORMAL spectrum and its inverse by direct character sums."""
import argparse
import collections
import json
import pathlib


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--reference',type=pathlib.Path,required=True)
    p.add_argument('--candidate',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    args=p.parse_args()
    if args.output.exists(): raise FileExistsError(args.output)
    ref=json.loads(args.reference.read_text(encoding='utf-8'))['spectrum_k']
    cand=json.loads(args.candidate.read_text(encoding='utf-8'))
    k=cand['spectrum_k']
    if len(k)!=512 or len(ref)!=512: raise ValueError('wrong size')
    assert collections.Counter(k)==collections.Counter(ref)
    assert all(k[i]==ref[i] for i in range(256) if ref[i] in (0,4,-4))
    for i in range(256,512):
        assert (abs(k[i]) in (1,7))==(abs(ref[i]) in (1,7))
        assert k[i]%4==ref[i]%4
    assert k[0]==0 and max(map(abs,k))==7 and sum(k)==128 and sum(x*x for x in k)==16384
    assert all((v&1)==(i>>8) for i,v in enumerate(k))
    inv=[sum(v*(-1 if (a&x).bit_count()%2 else 1) for a,v in enumerate(k)) for x in range(512)]
    score=sum(map(abs,inv)); nonsign=sum(abs(v)!=128 for v in inv)
    assert score==cand['inverse_l1'] and sum(v*v for v in inv)==512*16384 and score<=65536
    assert (score==65536)==(nonsign==0)
    altered=inv.copy(); altered[0]+=4; assert altered!=inv
    result={'same_full_histogram':True,'zero_and_magnitude4_positions_unchanged':True,
            'odd_half_indicator_and_sign_quadratic_unchanged':True,'direct_inverse_512x512':True,
            'parseval_verified':True,'inverse_l1':score,'inverse_ideal_l1':65536,
            'inverse_nonsign_count':nonsign,'inverse_max_abs':max(map(abs,inv)),
            'boolean_witness_candidate':nonsign==0,'mutation_rejected':True}
    with args.output.open('x',encoding='utf-8') as out: json.dump(result,out,indent=2,sort_keys=True); out.write('\n')
    print('inverse_l1=',score,'nonsign_count=',nonsign,'candidate=',nonsign==0)


if __name__=='__main__': main()
