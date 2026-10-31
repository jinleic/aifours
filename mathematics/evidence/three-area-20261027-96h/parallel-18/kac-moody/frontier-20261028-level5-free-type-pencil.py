#!/usr/bin/env python3
"""Full actual local lowering pencil on free level-five Levi-lowest sources.

This is a FREE-model pencil; quotient descent must be proved separately for
an individual type and parameter region.  No determinant or global rank is
claimed merely by generating a baseline-invertible minor.
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


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    args=ap.parse_args();a,b=args.a,args.b;degree=(a,b,5)
    out=ROOT/f'frontier-20261028-level5-free-{a}{b}-pencil-v1.json'
    if out.exists():raise FileExistsError(out)
    source=levi.lie_basis(degree)
    horizontal=[]
    for _,v in source:
        col={}
        for i,g in enumerate(('f1','f2')):
            col.update({(i,w):q for w,q in levi.levi_action(v,g,4,4).items()})
        horizontal.append(col)
    coeffs=lift.kernel_with_coefficients(horizontal)
    vectors=[lift.combine([v for _,v in source],c) for c in coeffs]
    k=len(vectors)
    base=[levi.lower3(v,4,4) for v in vectors]
    dr=[poly.diff(levi.lower3(v,5,4),base[j]) for j,v in enumerate(vectors)]
    ds=[poly.diff(levi.lower3(v,4,5),base[j]) for j,v in enumerate(vectors)]
    for j,v in enumerate(vectors):
        check=dict(base[j])
        for d in (dr[j],ds[j]):
            for key,q in d.items():check[key]=check.get(key,0)+q
        check={key:q for key,q in check.items() if q}
        assert check==levi.lower3(v,5,5),('affine mismatch',j)
    span=lift.Span()
    for col in base:span.add(col)
    result={'degree':degree,'free_source_dim':len(source),'joint_horizontal_kernel_dim':k,
            'baseline_f3_rank':len(span),'source_words':[''.join(map(str,w)) for w,_ in source],
            'horizontal_kernel_coefficients':[{str(i):lift.rational_text(q) for i,q in sorted(c.items())} for c in coeffs],
            'baseline':{'r':4,'s':4},'variables':'x=r-4,y=s-4',
            'affine_check_all_rows_at_5_5':True,
            'caution':'free model only; full actual source/target ideals and determinant nonvanishing require separate proof'}
    if len(span)==k:
        rows=sorted(span.rows);result['selected_target_words']=[''.join(map(str,w)) for w in rows]
        result['matrix']=[[[lift.rational_text(col.get(row,0)),lift.rational_text(dx.get(row,0)),lift.rational_text(dy.get(row,0))]
                           for col,dx,dy in zip(base,dr,ds)] for row in rows]
        result['status']='BASELINE_MINOR_ONLY_NOT_GLOBAL'
    else:result['status']='BASELINE_RANK_DEFECT'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('degree',degree,'source',len(source),'horizontal',k,'baseline f3 rank',len(span),result['status'],out.name,flush=True)

if __name__=='__main__':main()
