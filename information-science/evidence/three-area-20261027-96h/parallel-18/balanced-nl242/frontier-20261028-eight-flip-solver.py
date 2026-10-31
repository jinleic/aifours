#!/opt/homebrew/bin/python3
"""Bounded pseudo-Boolean search for an actual eight-flip balanceable table."""
import argparse
import json
import pathlib
import time
import z3

N=512
ALL=(1<<N)-1


def positions(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask^=bit


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seeds',type=pathlib.Path,required=True)
    p.add_argument('--index',type=int,required=True)
    p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    p.add_argument('--candidate',type=pathlib.Path,required=True)
    args=p.parse_args()
    if not 1<=args.index<=3 or not 1<=args.timeout_ms<=60000: raise ValueError('invalid bounds')
    if args.output.exists() or args.candidate.exists(): raise FileExistsError('output exists')
    seeds=[s.strip() for s in args.seeds.read_text(encoding='utf-8').splitlines() if s.strip() and not s.startswith('#')]
    binary=bin(int(seeds[args.index-1],16))[2:].zfill(N)
    truth=int(binary[::-1],2)
    chars=[sum(1<<x for x in range(N) if (a&x).bit_count()&1) for a in range(N)]
    w=[N-2*(truth^chars[a]).bit_count() for a in range(N)]
    if max(map(abs,w))!=28 or any(v==0 for v in w): raise ValueError('unexpected input spectrum')
    flips=[z3.Bool('flip_'+str(x)) for x in range(N)]
    one=[(v,1) for v in flips]
    s=z3.Solver(); s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(z3.PbEq(one,8))
    zeros=[]; peak_rows=0; near_rows=0
    for a,v in enumerate(w):
        bad=(truth^chars[a]) if v>0 else ALL^(truth^chars[a])
        terms=[(flips[x],1) for x in positions(bad)]
        # W' in the original sign orientation is |W|-16+4*bad_count.
        if abs(v)==28:
            s.add(z3.PbLe(terms,4)); peak_rows+=1
        elif abs(v)==20:
            s.add(z3.PbLe(terms,6)); near_rows+=1
        elif abs(v)==12:
            zeros.append(z3.PbEq(terms,1))
        elif abs(v)==4:
            zeros.append(z3.PbEq(terms,3))
        else:
            raise ValueError('unexpected seed Walsh magnitude')
    s.add(z3.Or(zeros))
    started=time.monotonic(); result=s.check(); elapsed=time.monotonic()-started
    receipt={'status':str(result),'seed_index_1based':args.index,'timeout_ms':args.timeout_ms,
             'solve_seconds':elapsed,'peak_inequalities':peak_rows,'near_peak_inequalities':near_rows,
             'zero_frequency_alternatives':len(zeros),'scope':'exact eight truth flips, arbitrary affine twist'}
    if result==z3.unknown: receipt['reason_unknown']=s.reason_unknown()
    if result==z3.sat:
        model=s.model()
        selected=[x for x in range(N) if z3.is_true(model.eval(flips[x],model_completion=True))]
        if len(selected)!=8: raise AssertionError('model cardinality')
        changed=truth
        for x in selected: changed ^=1<<x
        actual=[N-2*(changed^chars[a]).bit_count() for a in range(N)]
        zero=[a for a,v in enumerate(actual) if v==0]
        peak=max(map(abs,actual))
        if not zero or peak>28: raise AssertionError('model does not satisfy actual spectrum')
        twist=zero[0]; result_bits=changed^chars[twist]
        if result_bits.bit_count()!=256: raise AssertionError('twist is not balanced')
        candidate={'format':'boolean-truth-v1','seed_index_1based':args.index,'flip_indices':selected,
                   'affine_twist_frequency':twist,
                   'bits':''.join(str((result_bits>>x)&1) for x in range(N))}
        with args.candidate.open('x',encoding='utf-8') as out: json.dump(candidate,out,indent=2); out.write('\n')
        receipt.update({'flip_indices':selected,'peak':peak,'zero_frequency_count':len(zero),'candidate_written':True})
    with args.output.open('x',encoding='utf-8') as out: json.dump(receipt,out,indent=2,sort_keys=True); out.write('\n')
    print('status=',result,'solve_seconds=',round(elapsed,3),'peak_rows=',peak_rows,flush=True)


if __name__=='__main__': main()
