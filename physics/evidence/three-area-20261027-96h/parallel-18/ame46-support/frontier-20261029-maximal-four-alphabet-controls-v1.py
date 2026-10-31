#!/usr/bin/env python3
"""Fraction-exact arithmetic/profile controls for a six-marginal obstruction.

Claim to be proved in a separate packet: if every maximal modulus-1/6 position
uses only four local symbols per party, an AME(4,6) has at most12 such positions.
No tensor generation or quantum numerical optimization is used here.
"""
import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path


def profiles(t):
    return [d for d in itertools.combinations_with_replacement(range(5),4) if sum(d)==t]


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);a=p.parse_args()
    result={}
    for t in range(13,17):
        ps=profiles(t)
        q=[sum(x==4 for x in d) for d in ps]
        if min(q)<1:raise ValueError('high-t profile without degree4')
        surviving=[]
        for ds in itertools.product(ps,repeat=4):
            qs=[sum(x==4 for x in d) for d in ds]
            # HH pair event mass=4/36; each outside degree4 symbol adds2/36.
            if any(2*(qs[i]+qs[j])>4 for i,j in itertools.combinations(range(4),2)):continue
            surviving.append(ds)
        if t>=14 and surviving:raise ValueError('t>=14 survived HH capacity')
        if t==13 and surviving!=[((3,3,3,4),)*4]:raise ValueError('wrong t13 profile survivor')
        result[str(t)]={'local_occurrence_profiles':ps,'minimum_degree4_symbols':min(q),
          'joint_profiles_surviving_HH_probability':len(surviving)}
    t=13
    E_mass=1-Fraction(t,36);D_mass=4*Fraction(2,36)
    all_H_incidence=4*Fraction(2,6);D_H_incidence=3*D_mass
    HH_pair_mass_sum=6*Fraction(4,36);D_HH_pair_mass_sum=3*D_mass
    if HH_pair_mass_sum!=D_HH_pair_mass_sum:raise ValueError('HH exhaustion arithmetic')
    remaining_H=all_H_incidence-D_H_incidence;remaining_mass=E_mass-D_mass
    if not remaining_H>remaining_mass:raise ValueError('final H incidence contradiction absent')
    # Nearby t12 profile (3,3,3,3) has no degree4 symbol and is not excluded
    # by this route; it is the shape of the known 60-term construction's K side.
    if (3,3,3,3) not in profiles(12):raise ValueError('t12 nearby control')
    payload={'occurrence_profiles_by_t':result,'t13_exact_mass_accounting':{
      'E_mass':str(E_mass),'degree4_event_mass':str(D_mass),
      'HH_total_pair_mass':str(HH_pair_mass_sum),'degree4_event_HH_incidence':str(D_HH_pair_mass_sum),
      'remaining_H_incidence':str(remaining_H),'remaining_probability_mass':str(remaining_mass),
      'contradiction_margin':str(remaining_H-remaining_mass)},
      'nearby_t12_degree_profile_not_rejected':[3,3,3,3],
      'scope':'Exact arithmetic and finite local-profile controls; written six-marginal proof is separate.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(payload,f,indent=2);f.write('\n')
    print(json.dumps(payload,indent=2))


if __name__=='__main__':main()
