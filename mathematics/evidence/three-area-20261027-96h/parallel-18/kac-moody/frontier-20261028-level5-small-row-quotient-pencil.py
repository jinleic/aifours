#!/usr/bin/env python3
"""Complete fixed-small-r/s>=4 level-five quotient pencil (no shortcuts).

Entire node-3 seed ideal and all direct-sum target ideals are computed.  The
s=4 level-five 154* seed is excluded ONLY for later selected types distinct
from 154*, not by an equality of the two whole Serre quotients.
"""
import argparse
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
levi=load('levi','frontier-20261028-levi-lie-engine.py')
poly=load('poly','frontier-20261028-symbolic-minors.py')
lift=levi.lift


def restrict(v,ids):return {k:c for k,c in v.items() if k[0] in ids}


def main():
    ap=argparse.ArgumentParser()
    for x in ('a','b','r'):ap.add_argument('--'+x,type=int,required=True)
    args=ap.parse_args();a,b,r=args.a,args.b,args.r;degree=(a,b,5);assert r in (1,2,3)
    out=ROOT/f'frontier-20261028-level5-r{r}-{a}{b}-smallrow-pencil-v1.json'
    if out.exists():raise FileExistsError(out)
    spaces=levi.ideal_bases(degree,r,5);I=spaces.get(degree,lift.Span());T=levi.target_ideal(spaces,degree)
    source=levi.lie_basis(degree);span=lift.Span()
    for row in I.rows.values():span.add(row)
    basis=[]
    for w,v in source:
        if span.add(v) is not None:basis.append((w,v))
    for s in (4,5):
        for row in I.rows.values():assert not T.reduce(levi.delta(row,r,s)),('ideal derivative escaped',degree,r,s)
    cols=[T.reduce(levi.delta(v,r,4)) for _,v in basis]
    coeff=lift.kernel_with_coefficients([restrict(v,(0,1)) for v in cols])
    vectors=[lift.combine([v for _,v in basis],c) for c in coeff];k=len(vectors)
    base=[restrict(T.reduce(levi.delta(v,r,4)),(2,)) for v in vectors]
    slope=[poly.diff(restrict(T.reduce(levi.delta(v,r,5)),(2,)),base[j]) for j,v in enumerate(vectors)]
    piv=lift.Span()
    for col in base:piv.add(col)
    result={'degree':degree,'r':r,'s_class':'>=4','variable':'y=s-4',
            'ideal_built_with_parameters':{'r':r,'s':5},
            's4_extra_154star_seed_not_built':'must exclude separately from selected type',
            'free_source_dim':len(source),'source_ideal_dim':len(I),'quotient_source_dim':len(basis),
            'joint_horizontal_kernel_dim':k,'baseline_f3_rank':len(piv),
            'quotient_source_words':[''.join(map(str,w)) for w,_ in basis],
            'horizontal_kernel_coefficients':[{str(i):lift.rational_text(q) for i,q in sorted(c.items())} for c in coeff],
            'whole_fixed_row_source_ideal_derivative_containment_at_s4_and_s5':True}
    if not k:result['status']='ZERO_HORIZONTAL_KERNEL'
    elif len(piv)<k:result['status']='BASELINE_RANK_DEFECT'
    else:
        rows=sorted(piv.rows);result['selected_target_words']=[''.join(map(str,w)) for i,w in rows]
        result['matrix']=[[[lift.rational_text(col.get(row,0)),lift.rational_text(dy.get(row,0))]
                           for col,dy in zip(base,slope)] for row in rows]
        result['status']='BASELINE_MINOR_ONLY_NOT_GLOBAL'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('small-row',r,'degree',degree,'free',len(source),'ideal',len(I),'quotient',len(basis),'horizontal',k,'rank',len(piv),result['status'],out.name,flush=True)

if __name__=='__main__':main()
