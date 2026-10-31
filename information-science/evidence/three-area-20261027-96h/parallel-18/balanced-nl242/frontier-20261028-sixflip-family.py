#!/opt/homebrew/bin/python3
"""Materialize every peak-28 six-flip neighbor with direct spectrum checks."""
import argparse
import collections
import json
import pathlib


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seeds',type=pathlib.Path,required=True)
    p.add_argument('--independent',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    p.add_argument('--receipt',type=pathlib.Path,required=True)
    args=p.parse_args()
    if args.output.exists() or args.receipt.exists(): raise FileExistsError('output exists')
    data=json.loads(args.independent.read_text(encoding='utf-8'))
    if not data['complete'] or data['target_met']: raise ValueError('incomplete input')
    lines=[s.strip() for s in args.seeds.read_text(encoding='utf-8').splitlines() if s.strip() and not s.startswith('#')]
    source=int(lines[data['seed_index_1based']-1],16)
    chars=[sum(1<<x for x in range(512) if (a&x).bit_count()&1) for a in range(512)]
    family=[]; hist=collections.Counter()
    for row in data['six_sets']:
        if row['peak']!=28: continue
        x=source
        for i in row['flips']: x ^= 1<<(511-i)
        hextext=format(x,'0128X'); truth=int(format(x,'0512b')[::-1],2)
        w=[512-2*(truth^chars[a]).bit_count() for a in range(512)]
        assert max(map(abs,w))==28 and all(t!=0 for t in w)
        assert sum(t*t for t in w)==512*512
        hist[truth.bit_count()]+=1; family.append(hextext)
    assert len(family)==len(set(family))==120
    with args.output.open('x',encoding='utf-8') as out: out.write('\n'.join(family)+'\n')
    receipt={'seed_index_1based':data['seed_index_1based'],'distinct_truth_tables':len(family),
             'each_direct_512_character_sums_checked':True,'all_zero_free_peak28':True,
             'truth_weight_histogram':dict(sorted(hist.items())),'actual_balanced_witness':False}
    with args.receipt.open('x',encoding='utf-8') as out: json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('seed=',data['seed_index_1based'],'tables=',len(family),'weights=',receipt['truth_weight_histogram'])


if __name__=='__main__': main()
