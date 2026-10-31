#!/opt/homebrew/bin/python3
"""Bounded per-frequency split of the exact eight-flip Boolean search."""
import argparse
import json
import pathlib
import time
import z3

N=512
ALL=(1<<N)-1


def positions(mask):
    while mask:
        bit=mask&-mask; yield bit.bit_length()-1; mask^=bit


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seeds',type=pathlib.Path,required=True)
    p.add_argument('--index',type=int,required=True)
    p.add_argument('--each-timeout-ms',type=int,required=True)
    p.add_argument('--total-seconds',type=int,required=True)
    p.add_argument('--offset',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    p.add_argument('--candidate',type=pathlib.Path,required=True)
    args=p.parse_args()
    if not 1<=args.index<=3 or not 1<=args.each_timeout_ms<=10000 or not 1<=args.total_seconds<=120:
        raise ValueError('invalid bounds')
    if args.output.exists() or args.candidate.exists(): raise FileExistsError('output exists')
    seeds=[s.strip() for s in args.seeds.read_text(encoding='utf-8').splitlines() if s.strip() and not s.startswith('#')]
    binary=bin(int(seeds[args.index-1],16))[2:].zfill(N)
    truth=int(binary[::-1],2)
    chars=[sum(1<<x for x in range(N) if (a&x).bit_count()&1) for a in range(N)]
    w=[N-2*(truth^chars[a]).bit_count() for a in range(N)]
    if max(map(abs,w))!=28 or any(v==0 for v in w): raise ValueError('unexpected seed spectrum')
    flips=[z3.Bool('x_'+str(x)) for x in range(N)]
    s=z3.Solver(); s.set(timeout=args.each_timeout_ms,random_seed=20261028)
    s.add(z3.PbEq([(v,1) for v in flips],8))
    alternatives=[]
    for a,v in enumerate(w):
        bad=(truth^chars[a]) if v>0 else ALL^(truth^chars[a])
        terms=[(flips[x],1) for x in positions(bad)]
        if abs(v)==28: s.add(z3.PbLe(terms,4))
        elif abs(v)==20: s.add(z3.PbLe(terms,6))
        elif abs(v)==12: alternatives.append((0,a,1,terms))
        elif abs(v)==4: alternatives.append((1,a,3,terms))
        else: raise ValueError('unexpected magnitude')
    alternatives.sort(key=lambda r:(r[0],r[1]))
    if not 0<=args.offset<len(alternatives): raise ValueError('offset beyond alternatives')
    rows=[]; started=time.monotonic(); target=False
    for _,frequency,required,terms in alternatives[args.offset:]:
        s.push(); s.add(z3.PbEq(terms,required))
        before=time.monotonic(); status=s.check(); elapsed=time.monotonic()-before
        row={'frequency':frequency,'status':str(status),'solve_seconds':elapsed}
        if status==z3.unknown: row['reason_unknown']=s.reason_unknown()
        if status==z3.sat:
            model=s.model(); selected=[x for x in range(N) if z3.is_true(model.eval(flips[x],model_completion=True))]
            if len(selected)!=8: raise AssertionError('model cardinality')
            changed=truth
            for x in selected: changed ^=1<<x
            actual=[N-2*(changed^chars[a]).bit_count() for a in range(N)]
            if actual[frequency]!=0 or max(map(abs,actual))>28: raise AssertionError('invalid actual spectrum')
            result=changed^chars[frequency]
            if result.bit_count()!=256: raise AssertionError('invalid balanced twist')
            candidate={'format':'boolean-truth-v1','seed_index_1based':args.index,'flip_indices':selected,
                       'affine_twist_frequency':frequency,'bits':''.join(str((result>>x)&1) for x in range(N))}
            with args.candidate.open('x',encoding='utf-8') as out: json.dump(candidate,out,indent=2); out.write('\n')
            row['candidate_written']=True; target=True
        rows.append(row); s.pop()
        print('frequency=',frequency,'status=',status,'seconds=',round(elapsed,3),flush=True)
        if target or time.monotonic()-started>=args.total_seconds: break
    receipt={'seed_index_1based':args.index,'offset':args.offset,'total_alternatives':len(alternatives),
             'evaluated':len(rows),'next_offset':args.offset+len(rows),'target_met':target,
             'complete':args.offset+len(rows)==len(alternatives),'results':rows,
             'each_timeout_ms':args.each_timeout_ms,'total_seconds':args.total_seconds,
             'elapsed_seconds':time.monotonic()-started,'scope':'exact eight-flip subset; unknown is not unsat'}
    with args.output.open('x',encoding='utf-8') as out: json.dump(receipt,out,indent=2,sort_keys=True); out.write('\n')


if __name__=='__main__': main()
