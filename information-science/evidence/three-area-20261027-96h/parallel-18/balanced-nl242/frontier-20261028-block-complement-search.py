#!/opt/homebrew/bin/python3
"""Enumerate all 16 whole-block complements of an actual balanced table."""
import argparse
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--candidate',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or args.candidate.exists():raise FileExistsError('output exists')
    text=json.loads(args.input.read_text(encoding='utf-8'))['bits']
    if len(text)!=512 or text.count('1')!=256:raise ValueError('invalid balanced table')
    base=int(text[::-1],2);chars=[sum(1<<x for x in range(512) if (a&x).bit_count()%2) for a in range(512)]
    blocks=[((1<<128)-1)<<(128*y) for y in range(4)]
    rows=[];candidate=None
    for mask in range(16):
        bits=base
        for y in range(4):
            if mask>>y&1:bits^=blocks[y]
        assert bits.bit_count()==256
        W=[512-2*(bits^c).bit_count() for c in chars]
        assert W[0]==0 and all(W[r]==0 for r in (128,256,384))
        assert sum(w*w for w in W)==512*512
        peak=max(map(abs,W));rows.append({'mask':mask,'peak':peak,'zeros':sum(not w for w in W),
                                         'tail_32_count':sum(abs(w)==32 for w in W),'target':peak<=28})
        if peak<=28 and candidate is None:
            candidate={'format':'boolean-truth-v1','block_complement_mask':mask,'bits':''.join(str((bits>>x)&1) for x in range(512))}
    if candidate:
        with args.candidate.open('x',encoding='utf-8') as out:json.dump(candidate,out,indent=2);out.write('\n')
    result={'input':str(args.input),'all_16_checked':True,'rows':rows,'target_found':candidate is not None,
            'scope':'only whole-block complement variants; no unrestricted exclusion'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('best_peak=',min(r['peak'] for r in rows),'target=',candidate is not None,flush=True)


if __name__=='__main__':main()
