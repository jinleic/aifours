#!/usr/bin/env python3
"""Bounded, deterministic exact alternate full-source minor search.

A failed bounded search is recorded as such, never as a rank theorem.
"""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helpers',ROOT/'frontier-20261028-level5-35-alternate-minor-search.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
levi=h.levi;lift=levi.lift


def full_rows(P):
    source=levi.lie_basis(tuple(P['degree']))
    assert [''.join(map(str,w)) for w,_ in source]==P['source_words']
    vectors=[lift.combine([v for _,v in source],{int(i):Q(q) for i,q in coeff.items()})
             for coeff in P['horizontal_kernel_coefficients']]
    n=len(vectors)
    base=[levi.lower3(v,4,4) for v in vectors]
    def diff(a,b):
        z=dict(a)
        for w,q in b.items():z[w]=z.get(w,Q(0))-q
        return {w:q for w,q in z.items() if q}
    dr=[diff(levi.lower3(v,5,4),base[j]) for j,v in enumerate(vectors)]
    ds=[diff(levi.lower3(v,4,5),base[j]) for j,v in enumerate(vectors)]
    allwords=sorted(set(w for v in base+dr+ds for w in v))
    rows={''.join(map(str,w)):[[base[j].get(w,Q(0)),dr[j].get(w,Q(0)),ds[j].get(w,Q(0))] for j in range(n)]
          for w in allwords}
    for word,expected in zip(P['selected_target_words'],P['matrix']):
        assert rows[word]==[[Q(q) for q in item] for item in expected]
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--label',required=True);ap.add_argument('--attempt-cap',type=int,default=400);args=ap.parse_args()
    P=json.loads((ROOT/f'frontier-20261028-level5-free-{args.a}{args.b}-pencil-v1.json').read_text())
    first=json.loads((ROOT/f'frontier-20261028-level5-free-{args.a}{args.b}-determinant-v1.json').read_text())
    assert first['status']=='MIXED_OR_ZERO_CONSTANT'
    dest=ROOT/f'frontier-20261028-level5-{args.label}-alternate-minor-search-v1.json'
    if dest.exists():raise FileExistsError(dest)
    rows=full_rows(P);selected=P['selected_target_words'];n=len(selected)
    candidates=[w for w in rows if w not in set(selected)]
    attempts=survivors=0;found=None;exhausted=True
    for slot in range(n):
        for word in candidates:
            if attempts>=args.attempt_cap:exhausted=False;break
            trial=selected[:];trial[slot]=word
            data,scale=h.int_rows([rows[w] for w in trial]);v00=h.value(data,0,0);attempts+=1
            if not v00:continue
            sign=1 if v00>0 else -1
            xvals=[v00]+[h.value(data,i,0) for i in range(1,n+1)]
            if any(sign*q<0 for q in h.axis_coeff(xvals)):continue
            yvals=[v00]+[h.value(data,0,j) for j in range(1,n+1)]
            if any(sign*q<0 for q in h.axis_coeff(yvals)):continue
            survivors+=1
            known={(i,0):q for i,q in enumerate(xvals)};known.update({(0,j):q for j,q in enumerate(yvals)})
            coeff=h.polynomial(data,scale,known)
            if all(sign*q>0 for q in coeff.values()):
                found={'replaced_position_zero_based':slot,'previous_target_word':selected[slot],
                       'new_target_word':word,'selected_target_words':trial,
                       'matrix':[[[str(q) for q in entry] for entry in rows[w]] for w in trial],
                       'determinant_coefficients':[{'x_power':i,'y_power':j,'coefficient':str(q)}
                                                   for (i,j),q in sorted(coeff.items())],
                       'constant_coefficient':str(coeff.get((0,0))),
                       'all_nonzero_coefficients_one_sign':True,'sign':sign,
                       'grid_evaluations':(n+1)*(n+2)//2}
                break
        if found or not exhausted:break
        print('slots searched',slot+1,'of',n,'attempts',attempts,'axis survivors',survivors,flush=True)
    result={'degree':P['degree'],'r_s_region':'r,s>=4','attempts':attempts,'attempt_cap':args.attempt_cap,
            'all_one_row_candidates_exhausted':exhausted and not found,'axis_survivors':survivors,
            'first_pivot_mixed_sign_preserved':True,'result':found,
            'status':'ONE_SIGN_ALTERNATE' if found else 'NO_ONE_SIGN_ALTERNATE_IN_SEARCH',
            'scope':'free-model pencil, not by itself actual-quotient proof or independent review'}
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('DONE',result['status'],'attempts',attempts,'axis survivors',survivors,dest.name,flush=True)

if __name__=='__main__':main()
