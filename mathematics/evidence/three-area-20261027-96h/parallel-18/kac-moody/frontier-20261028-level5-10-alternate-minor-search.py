#!/usr/bin/env python3
"""Exact one-row alternative search on the FULL level-five 10-type pencil.

Uses generic exact helpers from the separately pinned 35 search; the mixed
initial 10 minor remains unchanged and is never called a quadrant proof.
"""
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helpers',ROOT/'frontier-20261028-level5-35-alternate-minor-search.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)


def main():
    P=json.loads((ROOT/'frontier-20261028-level5-free-43-pencil-v1.json').read_text())
    dest=ROOT/'frontier-20261028-level5-10-alternate-minor-search-v1.json'
    if dest.exists():raise FileExistsError(dest)
    rows=h.full_rows(P);selected=P['selected_target_words'];n=len(selected)
    candidates=[w for w in rows if w not in set(selected)]
    attempts=survivors=0;found=None
    for slot in range(n):
        for word in candidates:
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
        if found:break
        print('slots searched',slot+1,'of',n,'attempts',attempts,'axis survivors',survivors,flush=True)
    result={'degree':P['degree'],'r_s_region':'r,s>=4','attempts':attempts,'axis_survivors':survivors,
            'first_pivot_mixed_sign_preserved':True,'result':found,
            'status':'ONE_SIGN_ALTERNATE' if found else 'NO_ONE_ROW_ALTERNATE_FOUND',
            'scope':'free-model pencil, not by itself actual-quotient proof or independent review'}
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('DONE',result['status'],'attempts',attempts,'axis survivors',survivors,dest.name,flush=True)

if __name__=='__main__':main()
