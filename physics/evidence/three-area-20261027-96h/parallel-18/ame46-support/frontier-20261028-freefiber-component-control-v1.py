#!/usr/bin/env python3
"""Exact 6x6 mixed-alphabet free-fiber unitary positive and mutation controls."""
import argparse
import itertools
import json
from pathlib import Path


def parity(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2


def check(E):
    for A in ((0,1),(0,2),(0,3)):
        B=tuple(i for i in range(4) if i not in A);rows=sorted({tuple(q[i] for i in A) for q in E});cols=sorted({tuple(q[i] for i in B) for q in E})
        if len(rows)!=6 or len(cols)!=6:raise ValueError('wrong mixed cut size')
        F=[[0]*6 for _ in range(6)];ri={r:i for i,r in enumerate(rows)};ci={c:i for i,c in enumerate(cols)}
        for q,v in E.items():F[ri[tuple(q[i] for i in A)]][ci[tuple(q[i] for i in B)]]=v
        for i in range(6):
            for j in range(6):
                if sum(F[i][k]*F[j][k] for k in range(6))!=(2 if i==j else 0):raise ValueError('mixed cut Gram mismatch')
    return True


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    E={}
    for p in itertools.permutations(range(3)):
        E[p+(0,)]=1;E[p+(1,)]=(-1 if parity(p) else 1)
    check(E)
    chosen=[q for q in E if q[3]==parity(q[:3])]
    if len(chosen)!=6 or any(len({(q[i],q[j]) for q in chosen})!=6 for i,j in itertools.combinations(range(4),2)):
        raise ValueError('bipartition selection not pair-injective')
    bad=dict(E);bad[next(iter(bad))]*=-1
    try:check(bad)
    except ValueError as exc:
        if str(exc)!='mixed cut Gram mismatch':raise
        mutation=str(exc)
    else:raise ValueError('sign mutation accepted')
    result={'base_triples':6,'free_coordinate_values':2,'support':12,'cut_dimensions':[6,6,6],
      'Gram':'F F^T = 2 I exactly for all three cuts','selected_pair_injective_words':len(chosen),
      'single_sign_flip_control':mutation,
      'scope':'A valid mixed-alphabet residual component only; no full AME(4,6) or maximal-code completion.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
