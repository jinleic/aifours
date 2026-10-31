#!/usr/bin/env python3
"""Exact tiny control of the written tripartite antisymmetry obstruction.

Three low A fibers have full BxC rectangles U x complement(U); two high A
fibers have missing B symbols X, missing C symbols Y (complements), and a local
3x3 missing matching that extends global identity. With local degrees B=C=3,
low frequencies are2 on X and1 on Y. For x in X,y in Y the total ordered counts
satisfy M_xy - M_yx = 2 t_xy - 1, never0. Actual global multiplicity2 would
require both ordered counts2 and is therefore impossible.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path


def local_high(x,y):
    B=[b for b in range(4) if b!=x];C=[c for c in range(4) if c!=y]
    forbidden={(z,z) for z in range(4) if z not in (x,y)}|{(y,x)}
    if len(forbidden)!=3:raise ValueError('local completion wrong')
    edges={(b,c) for b,c in itertools.product(B,C) if (b,c) not in forbidden}
    if len(edges)!=6 or any(sum(b==v for b,c in edges)!=2 for v in B) or any(sum(c==v for b,c in edges)!=2 for v in C):raise ValueError('local pair graph not degree2')
    return edges


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);a=p.parse_args();sets=list(itertools.combinations(range(4),2));patterns=checks=states=0;example=None
    for low in itertools.combinations_with_replacement(sets,3):
        freq={z:sum(z in U for U in low) for z in range(4)}
        if sorted(freq.values())!=[1,1,2,2]:continue
        patterns+=1;X=tuple(z for z in range(4) if freq[z]==2);Y=tuple(z for z in range(4) if freq[z]==1)
        for c_missing in itertools.permutations(Y):
            states+=1;M=Counter()
            for U in low:
                for b,c in itertools.product(U,sorted(set(range(4))-set(U))):M[b,c]+=1
            for x,y in zip(X,c_missing):M.update(local_high(x,y))
            for x,y in itertools.product(X,Y):
                t=int(any(xx==x and yy==y for xx,yy in zip(X,c_missing)))
                if M[x,y]-M[y,x]!=2*t-1:raise ValueError('antisymmetry formula failed')
                if M[x,y]==M[y,x]==2:raise ValueError('uniform ordered pair survived')
                checks+=1
            if all(M[b,c]==2 for b,c in itertools.permutations(range(4),2)):raise ValueError('global uniform count survived')
            if example is None:example={'low_sets':low,'X':X,'Y':Y,'high_missing_C':c_missing,'ordered_count_matrix':[[M[b,c] for c in range(4)] for b in range(4)]}
    if (patterns,states,checks)!=(18,36,144):raise ValueError('unexpected normal form counts')
    result={'low_multiset_patterns':patterns,'high_exclusion_orders':states,'cross_XY_antisymmetry_checks':checks,
      'uniform_offdiagonal_count_states':0,'example':example,
      'control_history':'v1 demanded a relaxed BC+BD positive that does not exist; it failed before writing a receipt. This v2 tests the stronger single-BC antisymmetry identity directly and does not invent that positive.',
      'scope':'Tiny exact arithmetic controls only; original AME degree/profile/no-Hamming-one reduction is separate written mathematics.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
