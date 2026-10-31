#!/opt/homebrew/bin/python3
"""Finite controls for rank-six complement weight 44 phase obstruction."""
import argparse
import collections
import importlib.util
import json
import pathlib


def q(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    path=pathlib.Path(__file__).with_name('frontier-20261028-rank-bounds-sharpness-check.py')
    spec=importlib.util.spec_from_file_location('flatbase',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    flats=list(base.flats());assert len(flats)==2604
    cases={'simplex8':({0,1,2,7,11,31,47,63},5),
           'rank6weight10':({4,21,22,23,35,40,47,55,56,59},7)}
    results={}
    for name,(S,expected_intersection) in cases.items():
        matches=[H for H in flats if len(S&H)==expected_intersection]
        outcomes=collections.Counter();phasecases=0
        for H in matches:
            T=S^H
            for a in range(64):
                for c in range(2):
                    def Q(x):return q(x)^((a&x).bit_count()%2)^c
                    if name=='simplex8':
                        t5=sum(Q(x) for x in S&H);wh=sum(Q(x) for x in H)
                        if t5==3:assert wh==10
                        phasecases+=1
                    if sum(Q(x) for x in range(64))!=28:continue
                    sums=sum(Q(x) for x in S)+sum(Q(x) for x in T)
                    assert sums>=8
                    outcomes[sums]+=1
        if name=='simplex8':assert len(matches)==56
        else:assert len(matches)==3
        results[name]={'affine4flats':len(matches),'phase_checks':phasecases,
                       'nonbalanced_weight28_sum_distribution':{str(k):v for k,v in sorted(outcomes.items())},
                       'minimum_sum':min(outcomes)}
    receipt={'cases':results,'simplex_fivepoint_three_ones_forces_flat_weight10':True,
             'note':'finite examples; universal statement is proved algebraically'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('simplex_flats=56 weight10_flats=3 minimum_sums=',[v['minimum_sum'] for v in results.values()],flush=True)


if __name__=='__main__':main()
