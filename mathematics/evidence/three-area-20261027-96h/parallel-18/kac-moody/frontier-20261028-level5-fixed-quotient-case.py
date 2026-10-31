#!/usr/bin/env python3
"""Compute one entire actual level-five primitive quotient, exact arithmetic.

Both full Serre ideals, descendants and all three target ideals are retained.
One fixed parameter pair is not extrapolated to any other pair.
"""
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
    ap=argparse.ArgumentParser()
    for n in ('a','b','r','s'):ap.add_argument('--'+n,type=int,required=True)
    args=ap.parse_args();a,b,r,s=args.a,args.b,args.r,args.s;degree=(a,b,5)
    out=ROOT/f'frontier-20261028-level5-fixed-{a}{b}-r{r}-s{s}-v1.json'
    if out.exists():raise FileExistsError(out)
    spaces=levi.ideal_bases(degree,r,s);I=spaces.get(degree,lift.Span());T=levi.target_ideal(spaces,degree)
    source=levi.lie_basis(degree);span=lift.Span()
    for v in I.rows.values():span.add(v)
    basis=[]
    for w,v in source:
        if span.add(v) is not None:basis.append((w,v))
    for v in I.rows.values():assert not T.reduce(levi.delta(v,r,s)),('ideal derivative escaped',degree,r,s)
    def restrict(v,ids):return {k:c for k,c in v.items() if k[0] in ids}
    cols=[T.reduce(levi.delta(v,r,s)) for _,v in basis]
    coeff=lift.kernel_with_coefficients([restrict(v,(0,1)) for v in cols])
    vectors=[lift.combine([v for _,v in basis],c) for c in coeff];k=len(vectors)
    base=[restrict(T.reduce(levi.delta(v,r,s)),(2,)) for v in vectors]
    piv=lift.Span()
    for col in base:piv.add(col)
    case={'r_class':r,'s_class':s,'source_dim':len(basis),'horizontal_kernel_dim':k,
          'free_source_dim':len(source),'ideal_source_dim':len(I),'baseline_f3_rank':len(piv),
          'source_words':[''.join(map(str,w)) for w,_ in basis],
          'horizontal_kernel_coefficients':[{str(i):lift.rational_text(q) for i,q in sorted(c.items())} for c in coeff],
          'full_source_ideal_derivative_lands_in_whole_targets':True}
    if not basis:case['status']='ZERO_SOURCE'
    elif not k:case['status']='ZERO_HORIZONTAL_KERNEL'
    elif len(piv)<k:case['status']='BASELINE_SINGULAR'
    else:
        rows=sorted(piv.rows);matrix=[[Q(base[j].get(row,0)) for j in range(k)] for row in rows]
        scales=[math.lcm(*(q.denominator for q in row)) for row in matrix]
        integer=[[int(q*scales[i]) for q in row] for i,row in enumerate(matrix)]
        d=Q(det.bareiss(integer),math.prod(scales));assert d
        case['target_f3_word_pivots']=[''.join(map(str,w)) for _,w in rows]
        case['determinant_coefficients']=[{'x_power':0,'y_power':0,'coefficient':str(d)}]
        case['status']='CERTIFIED_ONE_SIGN'
    out.write_text(json.dumps({'degree':degree,'case':case,'not_formal_or_external_model_review':True},indent=2)+'\n')
    print('DONE',degree,'r,s',r,s,'free/ideal/quotient',len(source),len(I),len(basis),'horizontal',k,'f3rank',len(piv),case['status'],out.name,flush=True)

if __name__=='__main__':main()
