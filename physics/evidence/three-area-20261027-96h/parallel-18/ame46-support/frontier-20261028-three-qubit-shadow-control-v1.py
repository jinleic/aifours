#!/usr/bin/env python3
"""Exact rank-4 positive control for the three-qubit 2-uniform shadow bound."""
import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path


def marginal(diag,i,j):
    out={(x,y):Fraction(0) for x in (0,1) for y in (0,1)}
    for bits,p in diag.items():out[bits[i],bits[j]]+=p
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    points=list(itertools.product((0,1),repeat=3))
    rho={x:(Fraction(1,4) if sum(x)%2==0 else Fraction(0)) for x in points}
    if sum(rho.values())!=1 or sum(v!=0 for v in rho.values())!=4:raise ValueError('rank-4 example')
    for i,j in itertools.combinations(range(3),2):
        if any(v!=Fraction(1,4) for v in marginal(rho,i,j).values()):raise ValueError('pair nonuniform')
    # Y tensor 3 maps a computational projector to its bitwise complement.
    flip={x:rho[tuple(1-y for y in x)] for x in points}
    if any(flip[x]!=Fraction(1,4)-rho[x] for x in points):raise ValueError('spin-flip identity')
    mutant={x:Fraction(0) for x in points}
    for x in [x for x in points if rho[x]][:3]:mutant[x]=Fraction(1,3)
    if all(all(v==Fraction(1,4) for v in marginal(mutant,i,j).values()) for i,j in itertools.combinations(range(3),2)):
        raise ValueError('rank-3 mutation not detected')
    result={'example_rank':4,'three_two_qubit_marginals':'I4/4 exactly',
            'spin_flip':'rho_tilde = I8/4 - rho exactly on example',
            'rank_3_mutation':'pair marginal uniformity rejected',
            'scope':'Fraction-exact positive and mutation controls; universal rank bound follows from the written Pauli spin-flip argument.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
