#!/usr/bin/env python3
"""Exact controls for the maximal-code active-coordinate counting inequality."""
import argparse
import itertools
import json
from pathlib import Path


def lhs(n,alph):
    return sum(6*a-n for a in alph)-sum(alph[i]*alph[j]-n for i,j in itertools.combinations(range(4),2))


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);a=p.parse_args()
    weights=[k-k*(k-1)//2 for k in range(5)]
    if max(weights)!=1:raise ValueError('wrong per-word bound')
    # n=7, all active alphabets of size 3 gives 32>t=29.
    val=lhs(7,(3,3,3,3));t=36-7
    if (val,t)!=(32,29) or val<=t:raise ValueError('n7 contradiction lost')
    # A nearby formal count n=6 is not incorrectly rejected by this bound.
    near=lhs(6,(3,3,3,3))
    if near>36-6:raise ValueError('nearby-count control falsely rejected')
    result={'per_word_weights':weights,'n7_active_alphabets':[3,3,3,3],
      'n7_incidence_minus_pairs':val,'n7_maximal_words':t,
      'nearby_n6_same_alphabets_lhs':near,'nearby_n6_bound':30,
      'scope':'Exact integer controls; the counting identity and its hypotheses are proved separately.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
