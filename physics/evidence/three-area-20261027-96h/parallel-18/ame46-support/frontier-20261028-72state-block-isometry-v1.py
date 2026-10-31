#!/usr/bin/env python3
"""Exact support-block certificate and delta=0+i Gram checks for the 72 state."""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path

ODD=('0353','3530','4044','5405','0434','3055','4503','5340','0545','3304','4450','5033')


def load(path):
    spec=importlib.util.spec_from_file_location('source',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def multiply_conjugate(a,b):return (a[0]*b[0]+a[1]*b[1],a[1]*b[0]-a[0]*b[1])


def certify(mod,t):
    E={q:(val[0],0) for q,val in t.items() if len(mod.active(q))==2}
    P={q for q in t if not mod.active(q)};Q={tuple(map(int,s)) for s in ODD}
    if len(E)!=48 or len(P)!=12 or len(Q)!=12 or P&Q:raise ValueError('source support counts')
    allstates=dict(E);allstates.update({q:(1,0) for q in P});allstates.update({q:(0,1) for q in Q})
    if len(allstates)!=72:raise ValueError('source overlap')
    cuts=[]
    for A in ((0,1),(0,2),(0,3)):
        B=tuple(i for i in range(4) if i not in A);blocks=[]
        for pair in itertools.combinations(range(4),2):
            other=tuple(c for c in range(4) if c not in pair)
            cells={}
            for q in P|Q:
                inp=(mod.MAPS[A[0]][q[A[0]]],mod.MAPS[A[1]][q[A[1]]])
                out=(mod.MAPS[B[0]][q[B[0]]],mod.MAPS[B[1]][q[B[1]]])
                if set(inp)==set(pair):
                    if set(out)!=set(other):raise ValueError('noncomplementary colors')
                    cells[(inp,out)]='P' if q in P else 'Pprime'
            expected={(inp,out) for inp in (pair,pair[::-1]) for out in (other,other[::-1])}
            if set(cells)!=expected:raise ValueError('all-K block not complete')
            for inp in (pair,pair[::-1]):
                if {cells[(inp,out)] for out in (other,other[::-1])}!={'P','Pprime'}:
                    raise ValueError('nonzero P/Pprime sharing failed')
            blocks.append({'input_unordered_colors':pair,'output_unordered_colors':other,
                           'entries':4,'each_input_reaches_both_outputs':True})
        F=[[None]*36 for _ in range(36)]
        for q,value in allstates.items():
            r=6*q[A[0]]+q[A[1]];c=6*q[B[0]]+q[B[1]];F[r][c]=value
        for i in range(36):
            for j in range(36):
                x=y=0
                for c in range(36):
                    if F[i][c] is not None and F[j][c] is not None:
                        a,b=multiply_conjugate(F[i][c],F[j][c]);x+=a;y+=b
                if (x,y)!=((2 if i==j else 0),0):raise ValueError('delta0 exact complex Gram failed')
        cuts.append({'input_parties':A,'output_parties':B,'all_K_2x2_blocks':blocks,
                     'gram_entries_checked':1296})
    return cuts


def main():
    ap=argparse.ArgumentParser();ap.add_argument('table',type=Path);ap.add_argument('parser',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    mod=load(a.parser);t,sha=mod.read_table(a.table);cuts=certify(mod,t)
    bad=dict(t);bad.pop(next(q for q in t if not mod.active(q)))
    try:certify(mod,bad)
    except ValueError as exc:negative=str(exc)
    else:raise ValueError('deleted-P mutation not rejected')
    result={'table_sha256':sha,'source_Pprime':'https://arxiv.org/html/2610.16673#S4.E6',
            'delta0_coefficients':'E=+/-1,P=1,Pprime=i; common normalization 1/sqrt(72)',
            'cuts':cuts,'gram_entries_checked':3888,'deleted_P_control':negative,
            'scope':'Exact support blocks and delta=0 complex-integer Gram. General-parameter claims require the stated invertible blocks.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cuts'},indent=2))


if __name__=='__main__':main()
