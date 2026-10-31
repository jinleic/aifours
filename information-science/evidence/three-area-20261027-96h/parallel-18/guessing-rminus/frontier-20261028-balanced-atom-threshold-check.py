#!/usr/bin/env python3
"""Exact integer comparisons for balanced-atom probability thresholds."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-balanced-atom-threshold-check-result.json'


def main():
    cases=[]
    for m,d in ((6,13),(7,11),(8,10),(9,9)):
        left=d**(20*d);right=(d-1)**(20*(d-1))*m**(3*d)
        if left<=right:raise ValueError(('THRESHOLD',m,d))
        cases.append({'maximum_support':m,'minimum_probability_denominator':d,'integer_left_gt_right':True})
    # m=6 and d=14 is outside this particular sufficient criterion.
    if 14**280>13**260*6**42:raise ValueError('CONTROL_ACCEPTED')
    out={'exact_comparisons':cases,'all_checked':True,'controls':{'m6_denominator14_sufficient_test':'rejected'},
         'limits':'Integer entropy comparisons only; strict-law and graph deductions are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
