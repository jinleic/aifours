#!/usr/bin/env python3
"""Entire r=3, s>=4 level-five quotient-lowering pencil.

Builds all r=3 seed-ideal descendants and full direct-sum target ideals.
The s=4 level-five 154* seed is deliberately not built; using the resulting
pencil there requires a separate finite-Levi proof that the selected primitive
type is disjoint from 154*.  It is not a whole-space quotient identification.
"""
import argparse
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('levi',ROOT/'frontier-20261028-levi-lie-engine.py')
levi=importlib.util.module_from_spec(spec);spec.loader.exec_module(levi)
spec2=importlib.util.spec_from_file_location('poly',ROOT/'frontier-20261028-symbolic-minors.py')
poly=importlib.util.module_from_spec(spec2);spec2.loader.exec_module(poly)
lift=levi.lift


def restrict(v,indices):return {k:c for k,c in v.items() if k[0] in indices}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    args=ap.parse_args();a,b=args.a,args.b;degree=(a,b,5)
    out=ROOT/f'frontier-20261028-level5-r3-{a}{b}-quotient-pencil-v1.json'
    if out.exists():raise FileExistsError(out)
    spaces=levi.ideal_bases(degree,3,5)
    I=spaces.get(degree,lift.Span());T=levi.target_ideal(spaces,degree)
    free=levi.lie_basis(degree);extend=lift.Span()
    for row in I.rows.values():extend.add(row)
    complement=[]
    for w,v in free:
        if extend.add(v) is not None:complement.append((w,v))
    for s in (4,5):
        for row in I.rows.values():assert not T.reduce(levi.delta(row,3,s)),('ideal derivative escapes',degree,s)
    columns=[T.reduce(levi.delta(v,3,4)) for _,v in complement]
    h=[restrict(v,(0,1)) for v in columns]
    coeffs=lift.kernel_with_coefficients(h)
    vectors=[lift.combine([v for _,v in complement],c) for c in coeffs];k=len(vectors)
    base=[restrict(T.reduce(levi.delta(v,3,4)),(2,)) for v in vectors]
    ds=[poly.diff(restrict(T.reduce(levi.delta(v,3,5)),(2,)),base[j]) for j,v in enumerate(vectors)]
    for j,v in enumerate(vectors):
        expected=dict(base[j])
        for word,q in ds[j].items():expected[word]=expected.get(word,0)+2*q
        expected={word:q for word,q in expected.items() if q}
        assert expected==restrict(T.reduce(levi.delta(v,3,6)),(2,))
    span=lift.Span()
    for col in base:span.add(col)
    result={'degree':degree,'r':3,'s_class':'>=4','variable':'y=s-4',
            'ideal_built_with_parameters':{'r':3,'s':5},
            's4_extra_154star_seed_not_built':'must be excluded separately from the selected type',
            'free_source_dim':len(free),'source_ideal_dim':len(I),'quotient_source_dim':len(complement),
            'joint_horizontal_kernel_dim':k,'baseline_f3_rank':len(span),
            'quotient_source_words':[''.join(map(str,w)) for w,_ in complement],
            'horizontal_kernel_coefficients':[{str(i):lift.rational_text(q) for i,q in sorted(c.items())} for c in coeffs],
            'whole_r3_source_ideal_derivative_containment_at_s4_and_s5':True,
            'affine_s6_check_all_target_rows':True}
    if len(span)==k:
        rows=sorted(span.rows);result['selected_target_words']=[''.join(map(str,w)) for i,w in rows]
        result['matrix']=[[[lift.rational_text(col.get(row,0)),lift.rational_text(dy.get(row,0))]
                           for col,dy in zip(base,ds)] for row in rows]
        result['status']='BASELINE_MINOR_ONLY_NOT_GLOBAL'
    else:result['status']='BASELINE_RANK_DEFECT'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('r3 degree',degree,'free',len(free),'ideal',len(I),'quotient',len(complement),'horizontal',k,'baseline rank',len(span),result['status'],out.name,flush=True)

if __name__=='__main__':main()
