#!/usr/bin/env python3
"""Exact arithmetic controls for the N=46,t=26 active-alphabet reductions."""
import argparse
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2))


def counts(r):
    active=sum(6*x-10 for x in r);pair=sum(r[i]*r[j]-10 for i,j in PAIRS)
    return active,pair,26-(active-pair)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    profiles=[x for x in itertools.combinations_with_replacement(range(2,6),4)
              if all(x[i]*x[j]>=10 for i,j in PAIRS)]
    expected=[(2,5,5,5),(3,4,4,4),(3,4,4,5),(3,4,5,5),(3,5,5,5),
              (4,4,4,4),(4,4,4,5),(4,4,5,5),(4,5,5,5),(5,5,5,5)]
    if profiles!=expected:raise ValueError('profile list mismatch')
    alpha,beta,slack=counts((3,4,4,4))
    if (alpha,beta,slack)!=(50,24,0):raise ValueError('zero-slack arithmetic')
    # The required single-active count per symbol at a size-4 party is 2d-5;
    # it cannot be 0 for integral d.
    if any(2*d-5==0 for d in range(7)):raise ValueError('parity obstruction failed')
    alpha2,beta2,slack2=counts((2,5,5,5))
    if (alpha2,beta2,slack2)!=(62,45,9) or not 30>3*slack2:raise ValueError('three-five deficit check')
    remaining=[x for x in profiles if x not in ((2,5,5,5),(3,4,4,4),(3,5,5,5),(5,5,5,5))]
    result={'all_alphabet_profiles':profiles,'profile_3444':{'active_incidences':alpha,'active_pair_incidences':beta,'slack':slack},
      'profile_2555':{'active_incidences':alpha2,'active_pair_incidences':beta2,'slack':slack2,'required_weighted_triple_quad_incidences':30,'available_upper_bound':27},
      'four_written_candidate_exclusions':[(2,5,5,5),(3,4,4,4),(3,5,5,5),(5,5,5,5)],
      'remaining_profiles':remaining,'scope':'Exact profile/arithmetic controls; full exclusion proofs and parity lemmas are written separately.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
