#!/usr/bin/env python3
"""Exact full-original invariant source / target level-five experiment.

Each input class is one of 2,3,4,5 where 5 means all >=5.  The complete
Levi orbit and free-Lie ideal of both node-three seeds is recomputed for
that class; all f1/f2/f3 images are reduced in the actual quotient target.
A one-signed 6x6 determinant with nonzero constant certifies its whole
parameter orthant, conditional on the written free-Levi source theorem.
This is an experiment, not independent review or formal verification.
"""
import argparse
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('levi',ROOT/'frontier-20261028-levi-lie-engine.py')
levi=importlib.util.module_from_spec(spec);spec.loader.exec_module(levi)
spec=importlib.util.spec_from_file_location('poly',ROOT/'frontier-20261028-symbolic-minors.py')
poly=importlib.util.module_from_spec(spec);spec.loader.exec_module(poly)
lift=levi.lift
DEGREE=(5,5,5)


def restrict(v,idx):return {k:c for k,c in v.items() if k[0] in idx}


def case(r0,s0):
    spaces=levi.ideal_bases(DEGREE,r0,s0)
    sourceideal=spaces.get(DEGREE,lift.Span())
    targetideal=levi.target_ideal(spaces,DEGREE)
    source=levi.lie_basis(DEGREE)
    extension=lift.Span()
    for row in sourceideal.rows.values():extension.add(row)
    complement=[]
    for word,v in source:
        if extension.add(v) is not None:complement.append((word,v))
    print('class',r0,s0,'free/source ideal/source quotient',len(source),len(sourceideal),len(complement),flush=True)
    columns=[targetideal.reduce(levi.delta(v,r0,s0)) for _,v in complement]
    coeffs=lift.kernel_with_coefficients([restrict(v,(0,1)) for v in columns])
    vectors=[lift.combine([v for _,v in complement],c) for c in coeffs]
    k=len(vectors)
    result={'r_class':'>=5' if r0==5 else r0,'s_class':'>=5' if s0==5 else s0,
            'degree':list(DEGREE),'full_free_source_dim':len(source),'ideal_source_dim':len(sourceideal),
            'quotient_source_dim':len(complement),'joint_horizontal_kernel_dim':k,
            'source_lyndon_words':[''.join(map(str,w)) for w,_ in complement],
            'horizontal_kernel_coefficients':[{str(i):lift.rational_text(q) for i,q in sorted(c.items())} for c in coeffs]}
    if not k:
        result['status']='ZERO_HORIZONTAL_KERNEL';return result
    # Target quotient bases are constant within >=5 classes. The f3 local table
    # is exactly affine in r,s, hence this symbolic map is the whole class.
    base=[restrict(targetideal.reduce(levi.delta(v,r0,s0)),(2,)) for v in vectors]
    dr=[poly.diff(restrict(targetideal.reduce(levi.delta(v,r0+1,s0)),(2,)),base[j])
        if r0==5 else {} for j,v in enumerate(vectors)]
    ds=[poly.diff(restrict(targetideal.reduce(levi.delta(v,r0,s0+1)),(2,)),base[j])
        if s0==5 else {} for j,v in enumerate(vectors)]
    piv=lift.Span()
    for col in base:
        if piv.add(col) is None:
            result['status']='BASELINE_SINGULAR';return result
    rows=sorted(piv.rows);assert len(rows)==k
    matrix=[]
    for row in rows:
        line=[]
        for j in range(k):
            entry={}
            if base[j].get(row,0):entry[(0,0)]=base[j][row]
            if dr[j].get(row,0):entry[(1,0)]=dr[j][row]
            if ds[j].get(row,0):entry[(0,1)]=ds[j][row]
            line.append(entry)
        matrix.append(line)
    det=poly.determinant(matrix)
    assert det.get((0,0),0)
    result['target_f3_word_pivots']=[''.join(map(str,w)) for i,w in rows]
    result['determinant_coefficients']=[{'x_power':i,'y_power':j,'coefficient':lift.rational_text(q)}
                                        for (i,j),q in sorted(det.items())]
    result['variable_meanings']={'x':'r-5' if r0==5 else 'unused','y':'s-5' if s0==5 else 'unused'}
    result['status']='CERTIFIED_ONE_SIGN' if len({1 if q>0 else -1 for q in det.values()})==1 else 'MIXED_SIGNS_NEEDS_ANALYSIS'
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rclass',type=int,choices=(2,3,4,5),required=True)
    ap.add_argument('--sclass',type=int,choices=(2,3,4,5),required=True);args=ap.parse_args()
    out=ROOT/f'frontier-20261028-invariant5-r{args.rclass}-s{args.sclass}-v1.json'
    if out.exists():raise FileExistsError(out)
    result=case(args.rclass,args.sclass)
    result['conditional_on_new_unreviewed_levi_source_theorem']=True
    result['not_formal_or_external_model_review']=True
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('DONE',result['r_class'],result['s_class'],'kernel',result['joint_horizontal_kernel_dim'],result['status'],out.name,flush=True)


if __name__=='__main__':main()
