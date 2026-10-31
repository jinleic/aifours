#!/usr/bin/env python3
"""Exact singleton-block certificate for both Pandya 60-support faces.

The odd-face coordinates are transcribed from the paper's Eq. (6).
The block partition is phase-independent; no numerical phase sampling is used.
"""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

ODD=('0353','3530','4044','5405','0434','3055','4503','5340','0545','3304','4450','5033')


def load(path):
    spec=importlib.util.spec_from_file_location('a4source',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


def proof(mod,t,odd):
    H=mod.H;maps=mod.MAPS;E={q:v for q,v in t.items() if len(mod.active(q))==2}
    even={q for q,v in t.items() if not mod.active(q)}
    if len(E)!=48 or len(even)!=12 or len(odd)!=12:raise ValueError('unexpected source counts')
    results=[]
    for face,P,wantparity in (('even',even,0),('odd',odd,1)):
        if any(any(x in H for x in q) for q in P):raise ValueError('P contains H')
        cols={tuple(maps[i][q[i]] for i in range(4)) for q in P}
        expected={p for p in itertools.permutations(range(4)) if mod.parity(p)==wantparity}
        if cols!=expected:raise ValueError('wrong color permutation class')
        cuts=[]
        for A in ((0,1),(0,2),(0,3)):
            B=tuple(i for i in range(4) if i not in A)
            pr=[tuple(q[i] for i in A) for q in P];pc=[tuple(q[i] for i in B) for q in P]
            if len(set(pr))!=12 or len(set(pc))!=12:raise ValueError('P row or column uniqueness failure')
            er={tuple(q[i] for i in A) for q in E};ec={tuple(q[i] for i in B) for q in E}
            if len(er)!=24 or len(ec)!=24 or er.intersection(pr) or ec.intersection(pc):
                raise ValueError('E/P row or column overlap')
            if len(er.union(pr))!=36 or len(ec.union(pc))!=36:raise ValueError('incomplete row or column coverage')
            F=[[None]*36 for _ in range(36)]
            for q,val in E.items():
                r=6*q[A[0]]+q[A[1]];c=6*q[B[0]]+q[B[1]];F[r][c]=val
            for i in range(36):
                for j in range(36):
                    real=sur=0
                    for c in range(36):
                        if F[i][c] is not None and F[j][c] is not None:
                            x,y=mod.times(F[i][c],F[j][c]);real+=x;sur+=y
                    target=2 if i==j and (i//6,i%6) in er else 0
                    if (real,sur)!=(target,0):raise ValueError('E Gram identity failed')
            cuts.append({'left':A,'right':B,'P_singleton_rows':12,'P_singleton_columns':12,
                         'E_rows':24,'E_columns':24,'E_gram_entries_checked':1296,
                         'P_E_row_column_disjoint':True})
        results.append({'face':face,'permutation_parity':wantparity,'cuts':cuts})
    return results


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('parser',type=Path);p.add_argument('output',type=Path);args=p.parse_args()
    mod=load(args.parser);t,sha=mod.read_table(args.table)
    odd={tuple(map(int,s)) for s in ODD};results=proof(mod,t,odd)
    # A repeated all-K row violates the singleton-block premise.
    first=next(iter(odd));bad=set(odd)
    for last in range(6):
        candidate=(first[0],first[1],first[2],last)
        if last not in mod.H and candidate not in bad:bad.add(candidate);break
    try:proof(mod,t,bad)
    except ValueError as exc:negative=str(exc)
    else:raise ValueError('bad-P mutation not rejected')
    result={'table_sha256':sha,'odd_face_source':'https://arxiv.org/html/2610.16673#S4.E6',
            'odd_face_physical_tuples':sorted(odd),'faces':results,'added_P_term_control':negative,
            'arbitrary_phase_statement':'On each cut P occupies 12 disjoint singleton rows/columns; replacing each coefficient sqrt(2) by sqrt(2)*unit_phase preserves Gram exactly, independently for all 12 phases.',
            'scope':'Finite source/block certificate; proof of arbitrary phases uses the displayed exact block decomposition.'}
    with args.output.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'table_sha256':sha,'faces':len(results),'cuts_each':3,
      'E_gram_entries_total':2*3*1296,'added_P_term_control':negative,'status':'PASS'},indent=2))


if __name__=='__main__':main()
