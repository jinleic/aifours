#!/usr/bin/env python3
"""Search exact alternate full 35-type minors, preserving mixed first result.

Deterministically replace one selected target row by another actual target
word row.  Each promising candidate is certified by full total-degree-20
Newton interpolation; necessary one-variable edge sign checks reject quickly.
No numerical probing, random search, or quotient substitution is used.
"""
import importlib.util
import json
import math
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    x=importlib.util.module_from_spec(spec);spec.loader.exec_module(x);return x

levi=load('levi','frontier-20261028-levi-lie-engine.py')
detmod=load('detmod','frontier-20261028-level5-type-determinant.py')
lift=levi.lift


def full_rows(P):
    source=levi.lie_basis(tuple(P['degree']))
    assert [''.join(map(str,w)) for w,_ in source]==P['source_words']
    vectors=[lift.combine([v for _,v in source],{int(i):Q(q) for i,q in coeff.items()})
             for coeff in P['horizontal_kernel_coefficients']]
    n=len(vectors);assert n==20
    base=[levi.lower3(v,4,4) for v in vectors]
    delta_r=[];delta_s=[]
    for j,v in enumerate(vectors):
        def difference(a,b):
            z=dict(a)
            for w,q in b.items():z[w]=z.get(w,Q(0))-q
            return {w:q for w,q in z.items() if q}
        delta_r.append(difference(levi.lower3(v,5,4),base[j]))
        delta_s.append(difference(levi.lower3(v,4,5),base[j]))
    allwords=sorted(set(w for v in base+delta_r+delta_s for w in v))
    rows={''.join(map(str,w)):[[base[j].get(w,Q(0)),delta_r[j].get(w,Q(0)),delta_s[j].get(w,Q(0))] for j in range(n)]
          for w in allwords}
    for word,expected in zip(P['selected_target_words'],P['matrix']):
        assert rows[word]==[[Q(q) for q in item] for item in expected]
    return rows


def int_rows(rows):
    scales=[math.lcm(*(q.denominator for entry in row for q in entry)) for row in rows]
    data=[[[int(q*scales[i]) for q in entry] for entry in row] for i,row in enumerate(rows)]
    return data,math.prod(scales)


def value(data,x,y):return detmod.bareiss([[a+x*b+y*c for a,b,c in row] for row in data])


def axis_coeff(vals):
    work=vals[:];delta=[]
    while work:
        delta.append(work[0]);work=[b-a for a,b in zip(work,work[1:])]
    out=[Q(0)]*len(vals)
    for i,q in enumerate(delta):
        for j,v in enumerate(detmod.falling_binomial(i)):out[j]+=q*v
    return out


def polynomial(data,scale,known):
    n=len(data);vals=dict(known)
    for i in range(n+1):
        for j in range(n+1-i):
            if (i,j) not in vals:vals[i,j]=value(data,i,j)
    newton={}
    for i in range(n+1):
        for j in range(n+1-i):
            newton[i,j]=sum((-1)**(i+j-u-v)*math.comb(i,u)*math.comb(j,v)*vals[u,v]
                            for u in range(i+1) for v in range(j+1))
    bas=[detmod.falling_binomial(i) for i in range(n+1)];out=defaultdict(Q)
    for (i,j),q in newton.items():
        for u,cu in enumerate(bas[i]):
            for v,cv in enumerate(bas[j]):out[u,v]+=Q(q,scale)*cu*cv
    out={ij:q for ij,q in out.items() if q}
    assert all(i+j<=n for i,j in out)
    for (i,j),actual in vals.items():
        assert sum(q*i**u*j**v for (u,v),q in out.items())==Q(actual,scale)
    return out


def main():
    P=json.loads((ROOT/'frontier-20261028-level5-free-32-pencil-v1.json').read_text())
    out=ROOT/'frontier-20261028-level5-35-alternate-minor-search-v1.json'
    if out.exists():raise FileExistsError(out)
    rows=full_rows(P);selected=P['selected_target_words'];n=len(selected)
    candidates=[w for w in rows if w not in set(selected)]
    attempts=axis_pass=0;found=None
    for slot in range(n):
        for word in candidates:
            trial=selected[:];trial[slot]=word
            data,scale=int_rows([rows[w] for w in trial]);v00=value(data,0,0)
            attempts+=1
            if not v00:continue
            sign=1 if v00>0 else -1
            xvals=[v00]+[value(data,i,0) for i in range(1,n+1)]
            if any(sign*q<0 for q in axis_coeff(xvals)):continue
            yvals=[v00]+[value(data,0,j) for j in range(1,n+1)]
            if any(sign*q<0 for q in axis_coeff(yvals)):continue
            axis_pass+=1
            known={(i,0):q for i,q in enumerate(xvals)};known.update({(0,j):q for j,q in enumerate(yvals)})
            coeff=polynomial(data,scale,known)
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
        print('slots searched',slot+1,'of',n,'attempts',attempts,'axis survivors',axis_pass,flush=True)
    result={'degree':P['degree'],'r_s_region':'r,s>=4','attempts':attempts,'axis_survivors':axis_pass,
            'first_pivot_mixed_sign_preserved':True,'result':found,
            'status':'ONE_SIGN_ALTERNATE' if found else 'NO_ONE_ROW_ALTERNATE_FOUND',
            'scope':'free-model pencil, not by itself actual-quotient proof or independent review'}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('DONE',result['status'],'attempts',attempts,'axis survivors',axis_pass,out.name,flush=True)

if __name__=='__main__':main()
