#!/usr/bin/env python3
"""Exact controls for the short n=5 projection/XOR lemma."""
import argparse
import itertools
import json
from pathlib import Path


def options(fixed):
    universe=range(3);pairs=list(itertools.combinations(universe,2));result=[]
    for singleton,a,b in itertools.product(universe,pairs,pairs):
        rest=iter((frozenset(a),frozenset(b)))
        result.append(tuple(frozenset((singleton,)) if j==fixed else next(rest) for j in range(3)))
    if len(set(result))!=27:raise ValueError('wrong options')
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);args=ap.parse_args()
    V=[options(j) for j in range(3)];tested=matched=wrong_or=0;witness=None
    for j,k in itertools.combinations(range(3),2):
        l=next(x for x in range(3) if x not in (j,k))
        for A,B in itertools.product(V[j],V[k]):
            pairs={(a,b) for fiber in range(3) for a in A[fiber] for b in B[fiber]}
            in_base=A[j].issubset(A[l]) and B[k].issubset(B[l])
            eqj=(A[k]==A[l]);eqk=(B[j]==B[l]);pred=in_base and (eqj!=eqk)
            if (len(pairs)==5)!=pred:raise ValueError(f'XOR characterization failure {j,k,A,B}')
            tested+=1;matched+=int(pred)
            mutated=in_base and ((not eqj) or (not eqk))
            if mutated!=(len(pairs)==5):
                wrong_or+=1
                if witness is None:witness={'coordinate_pair':[j,k],'projection_size':len(pairs),
                  'equal_flags':[eqj,eqk],'both_singletons_in_base':in_base}
    flags=[e for e in itertools.product((False,True),repeat=3)
           if e[0]!=e[1] and e[0]!=e[2] and e[1]!=e[2]]
    if tested!=2187 or matched!=432 or flags or not wrong_or:raise ValueError('unexpected counts')
    result={'two_coordinate_cases':tested,'five_projection_cases':matched,
      'xor_characterization_failures':0,'pairwise_distinct_three_boolean_flags':len(flags),
      'weakened_or_mutation_rejections':wrong_or,'mutation_witness':witness,
      'scope':'Bounded check of projection lemma; general proof is the four-cell rectangle argument.'}
    with args.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
