#!/opt/homebrew/bin/python3
"""Exact finite controls for the three four-entry fiber inequalities."""
import argparse
import itertools
import json
import pathlib


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    groups=[('qzero',(-4,4),640),('qone',(-6,2),864),('odd_Q0',(-7,-3,1,5),1464),
            ('odd_Q1',(-5,-1,3,7),1464)]
    results={}
    for name,vals,C in groups:
        best=None;ties=[];count=0
        for row in itertools.combinations_with_replacement(vals,4):
            E=sum(x*x for x in row);S=sum(row)**2;value=10*E-S;count+=1
            if best is None or value>best:best=value;ties=[row]
            elif value==best:ties.append(row)
        assert best==C
        # Lowering the proposed constant by one must fail at an equality tuple.
        assert any(10*sum(x*x for x in row)-sum(row)**2>C-1 for row in ties)
        results[name]={'multisets':count,'best_10E_minus_S2':best,'equality_examples':ties,
                       'constant_minus_one_mutation_rejected':True}
    margins={}
    for z in (112,144):
        n0=(z-4)//4;n1=(256-z)//4
        C=640*n0+864*n1+1464*64
        gap=9*16384-C
        assert gap==56*(z-16) and gap>0
        margins[str(z)]={'qzero_nonradical_fibers':n0,'qone_fibers':n1,'odd_fibers':64,
                         'required_sum_squares_lower_bound':16384+gap,'contradiction_gap':gap}
    receipt={'four_entry_inequalities':results,'aggregate_margins':margins,
             'note':'finite checks supplement the written all-variable proof'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('fiber maxima=640,864,1464 aggregate gaps=5376,7168',flush=True)


if __name__=='__main__':main()
