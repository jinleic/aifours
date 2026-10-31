#!/usr/bin/env python3
"""Exact constants for a whole open neighborhood of the certified SPR box.

Inputs are a pinned exact Bernstein/separation receipt; no numerical search
or SDP code is imported. The proof of perturbation inequalities is in the
accompanying manuscript. This script checks the rational hypotheses and
records a non-vacuous positive radius and strict margins.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


def calculate(data,radius):
    if radius<=0:
        raise ValueError('radius must be positive')
    lo=[Q(x) for x in data['lower']]
    hi=[Q(x) for x in data['upper']]
    b=[Q(x) for x in data['exact_unrestricted_common_numerator']]
    if len(lo)!=8 or len(hi)!=8 or len(b)!=8 or lo[7]!=1 or hi[7]!=1 or b[7]!=1:
        raise ValueError('monic degree mismatch')
    if not all(0<lo[j]<hi[j] for j in range(7)):
        raise ValueError('original box interval mismatch')
    smallest_width=min(hi[j]-lo[j] for j in range(7))
    if not 2*radius<smallest_width:
        raise ValueError('radius fails width preservation')
    pairing_margin=Q(data['common_normalized_pairing_lower_bound'])
    sep_margin=-Q(data['exact_no_in_box_weighted_maximum'])
    if pairing_margin<=0 or sep_margin<=0:
        raise ValueError('input does not supply both strict margins')
    S=sum(hi)
    B=sum(abs(x) for x in b)
    pairing_after=pairing_margin-7*radius*B
    if pairing_after<=0:
        raise ValueError('radius fails pairing and stability margin')
    sep_error=77*radius*(2*S+7*radius)
    sep_after=sep_margin-sep_error
    if sep_after<=0:
        raise ValueError('radius fails separation margin')
    return {'radius':str(radius),'minimum_original_width':str(smallest_width),
            'original_normalized_pairing_margin':str(pairing_margin),
            'numerator_coefficient_l1':str(B),'box_upper_coefficient_sum':str(S),
            'normalized_pairing_margin_after_perturbation':str(pairing_after),
            'actual_box_denominator_nonzero_margin':str(pairing_margin/B-7*radius),
            'common_literal_ratio_lower_bound':str(pairing_after/(S+7*radius)**2),
            'original_separation_margin':str(sep_margin),
            'max_weighted_separation_perturbation':str(sep_error),
            'separation_margin_after_perturbation':str(sep_after)}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--input',required=True); p.add_argument('--output',required=True)
    args=p.parse_args(); raw=Path(args.input).read_bytes(); data=json.loads(raw)
    result=calculate(data,Q(1,10**12))
    try:
        calculate(data,Q(1))
    except ValueError as exc:
        if str(exc)!='radius fails width preservation':
            raise
        control={'mutation':'replace 10^-12 radius by 1','reason':str(exc)}
    else:
        raise ValueError('oversized-radius negative control was not rejected')
    with Path(args.output).open('x',encoding='utf-8') as out:
        json.dump({'schema':1,'input_sha256':hashlib.sha256(raw).hexdigest(),
                   'exact_constants':result,'negative_control':control,
                   'scope':'all perturbed closed coefficient boxes with each lower and upper endpoint within radius of the exact original 7-width box; common unrestricted numerator remains valid while every monic numerator in its own box is excluded. Not a universal all-box synthesis theorem.'},out,indent=2,sort_keys=True)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))
    print('NEGATIVE CONTROL:',json.dumps(control))


if __name__=='__main__':
    main()
