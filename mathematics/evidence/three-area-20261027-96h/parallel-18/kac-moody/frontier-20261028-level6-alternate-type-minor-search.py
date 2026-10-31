#!/usr/bin/env python3
"""Bounded exact one-row alternate search for level-six full source minors."""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
h=load('helpers','frontier-20261028-level5-35-alternate-minor-search.py');levi=h.levi;lift=levi.lift


def full_rows(P):
    source=levi.lie_basis(tuple(P['degree']))
    assert [''.join(map(str,w)) for w,_ in source]==P['source_words']
    vectors=[lift.combine([v for _,v in source],{int(i):Q(q) for i,q in c.items()}) for c in P['horizontal_kernel_coefficients']]
    n=len(vectors);base=[levi.lower3(v,6,6) for v in vectors]
    def diff(a,b):
        z=dict(a)
        for w,q in b.items():z[w]=z.get(w,Q(0))-q
        return {w:q for w,q in z.items() if q}
    dx=[diff(levi.lower3(v,7,6),base[j]) for j,v in enumerate(vectors)]
    dy=[diff(levi.lower3(v,6,7),base[j]) for j,v in enumerate(vectors)]
    words=sorted(set(w for v in base+dx+dy for w in v))
    rows={''.join(map(str,w)):[[base[j].get(w,Q(0)),dx[j].get(w,Q(0)),dy[j].get(w,Q(0))] for j in range(n)] for w in words}
    for w,expected in zip(P['selected_target_words'],P['matrix']):assert rows[w]==[[Q(q) for q in e] for e in expected]
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--attempt-cap',type=int,default=400);args=ap.parse_args();a,b=args.a,args.b
    P=json.loads((ROOT/f'frontier-20261028-level6-free-{a}{b}-pencil-v1.json').read_text())
    first=json.loads((ROOT/f'frontier-20261028-level6-free-{a}{b}-determinant-v1.json').read_text())
    assert first['status']=='MIXED_OR_ZERO_CONSTANT'
    out=ROOT/f'frontier-20261028-level6-free-{a}{b}-alternate-v1.json'
    if out.exists():raise FileExistsError(out)
    rows=full_rows(P);selected=P['selected_target_words'];n=len(selected)
    candidates=[w for w in rows if w not in set(selected)];attempts=survivors=0;found=None;exhausted=True
    for slot in range(n):
        for w in candidates:
            if attempts>=args.attempt_cap:exhausted=False;break
            trial=selected[:];trial[slot]=w;data,scale=h.int_rows([rows[u] for u in trial]);v0=h.value(data,0,0);attempts+=1
            if not v0:continue
            sign=1 if v0>0 else -1
            xvals=[v0]+[h.value(data,i,0) for i in range(1,n+1)]
            if any(sign*q<0 for q in h.axis_coeff(xvals)):continue
            yvals=[v0]+[h.value(data,0,j) for j in range(1,n+1)]
            if any(sign*q<0 for q in h.axis_coeff(yvals)):continue
            survivors+=1;known={(i,0):q for i,q in enumerate(xvals)};known.update({(0,j):q for j,q in enumerate(yvals)})
            coeff=h.polynomial(data,scale,known)
            if all(sign*q>0 for q in coeff.values()):
                found={'replaced_position_zero_based':slot,'previous_target_word':selected[slot],
                       'new_target_word':w,'selected_target_words':trial,
                       'matrix':[[[str(q) for q in e] for e in rows[u]] for u in trial],
                       'determinant_coefficients':[{'x_power':i,'y_power':j,'coefficient':str(q)} for (i,j),q in sorted(coeff.items())],
                       'constant_coefficient':str(coeff.get((0,0))),'sign':sign,'grid_evaluations':(n+1)*(n+2)//2}
                break
        if found or not exhausted:break
        print('slots searched',slot+1,'of',n,'attempts',attempts,'axis survivors',survivors,flush=True)
    result={'degree':P['degree'],'r_s_region':'r,s>=6','attempts':attempts,'attempt_cap':args.attempt_cap,
            'all_one_row_candidates_exhausted':exhausted and not found,'axis_survivors':survivors,
            'first_pivot_mixed_sign_preserved':True,'result':found,
            'status':'ONE_SIGN_ALTERNATE' if found else 'NO_ONE_SIGN_ALTERNATE_IN_SEARCH',
            'scope':'free-level6 source/target; full Cartan and absence of node3 ideals are separate written inputs'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE level6',P['degree'],result['status'],'attempts',attempts,'axis survivors',survivors,out.name,flush=True)

if __name__=='__main__':main()
