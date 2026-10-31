#!/usr/bin/env python3
"""Bounded exact alternate minor search in the entire r=3 quotient map."""
import argparse
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
levi=load('levi','frontier-20261028-levi-lie-engine.py')
det=load('det','frontier-20261028-level5-type-determinant.py')
lift=levi.lift


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--attempt-cap',type=int,default=400);args=ap.parse_args()
    a,b=args.a,args.b;degree=(a,b,5)
    P=json.loads((ROOT/f'frontier-20261028-level5-r3-{a}{b}-quotient-pencil-v1.json').read_text())
    first=json.loads((ROOT/f'frontier-20261028-level5-r3-{a}{b}-quotient-determinant-v1.json').read_text())
    assert first['status']=='MIXED_OR_ZERO_CONSTANT'
    dest=ROOT/f'frontier-20261028-level5-r3-{a}{b}-alternate-minor-search-v1.json'
    if dest.exists():raise FileExistsError(dest)
    words=dict((''.join(map(str,w)),v) for w,v in levi.lie_basis(degree))
    basis=[words[w] for w in P['quotient_source_words']]
    vectors=[lift.combine(basis,{int(i):Q(q) for i,q in c.items()}) for c in P['horizontal_kernel_coefficients']]
    k=len(vectors);spaces=levi.ideal_bases(degree,3,5);T=levi.target_ideal(spaces,degree)
    def dr(v,s):return {w:q for (idx,w),q in T.reduce(levi.delta(v,3,s)).items() if idx==2}
    base=[dr(v,4) for v in vectors];at5=[dr(v,5) for v in vectors]
    def diff(a,b):
        z=dict(a)
        for w,q in b.items():z[w]=z.get(w,0)-q
        return {w:q for w,q in z.items() if q}
    slope=[diff(at5[j],base[j]) for j in range(k)]
    wordset=sorted(set(w for v in base+slope for w in v))
    rows={''.join(map(str,w)):[[base[j].get(w,Q(0)),slope[j].get(w,Q(0))] for j in range(k)] for w in wordset}
    selected=P['selected_target_words']
    for word,expected in zip(selected,P['matrix']):assert rows[word]==[[Q(q) for q in e] for e in expected]
    options=[w for w in rows if w not in set(selected)];attempts=0;found=None;exhausted=True
    for slot in range(k):
        for w in options:
            if attempts>=args.attempt_cap:exhausted=False;break
            attempts+=1;trial=selected[:];trial[slot]=w;rr=[rows[u] for u in trial]
            scales=[math.lcm(*(q.denominator for entry in row for q in entry)) for row in rr]
            ints=[[[int(q*scales[i]) for q in e] for e in row] for i,row in enumerate(rr)];scale=math.prod(scales)
            def value(y):return Q(det.bareiss([[z[0]+y*z[1] for z in row] for row in ints]),scale)
            v0=value(0)
            if not v0:continue
            values=[v0]+[value(j) for j in range(1,k+1)];work=values[:];diffs=[]
            while work:
                diffs.append(work[0]);work=[z-y for y,z in zip(work,work[1:])]
            coef=[Q(0)]*(k+1)
            for j,q in enumerate(diffs):
                for t,c in enumerate(det.falling_binomial(j)):coef[t]+=q*c
            sign=1 if v0>0 else -1
            if all(sign*q>=0 for q in coef):
                assert all(sum(q*j**i for i,q in enumerate(coef))==v for j,v in enumerate(values))
                found={'replaced_position_zero_based':slot,'previous_target_word':selected[slot],
                       'new_target_word':w,'selected_target_words':trial,
                       'matrix':[[[str(q) for q in entry] for entry in rows[u]] for u in trial],
                       'determinant_coefficients':[str(q) for q in coef],
                       'nonzero_coefficient_count':sum(bool(q) for q in coef),'sign':sign,
                       'constant_coefficient':str(coef[0]),'grid_evaluations':k+1}
                break
        if found or not exhausted:break
        print('slots searched',slot+1,'of',k,'attempts',attempts,flush=True)
    result={'degree':degree,'r':3,'s_class':'>=4','attempts':attempts,'attempt_cap':args.attempt_cap,
            'all_one_row_candidates_exhausted':exhausted and not found,'first_pivot_mixed_sign_preserved':True,
            'status':'ONE_SIGN_ALTERNATE' if found else 'NO_ONE_SIGN_ALTERNATE_IN_SEARCH',
            'result':found,'scope':'actual r3 seed quotient; s4 extra154* seed needs separate selected-type exclusion'}
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE r3',degree,result['status'],'attempts',attempts,dest.name,flush=True)

if __name__=='__main__':main()
