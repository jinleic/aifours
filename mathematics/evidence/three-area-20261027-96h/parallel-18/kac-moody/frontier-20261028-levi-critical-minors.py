#!/usr/bin/env python3
"""Exact symbolic f3 minors on full joint Levi-lowest quotient spaces.

Conditional on the independently written level-one and free-Lie-over-Levi
source theorem.  All Serre seed descendants and original quotient targets
are retained.  Computes ALL 16 threshold parameter classes per degree.
"""
import importlib.util
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('levi',ROOT/'frontier-20261028-levi-lie-engine.py')
levi=importlib.util.module_from_spec(spec);spec.loader.exec_module(levi)
spec2=importlib.util.spec_from_file_location('poly',ROOT/'frontier-20261028-symbolic-minors.py')
poly=importlib.util.module_from_spec(spec2);spec2.loader.exec_module(poly)
lift=levi.lift


def restr(v,indices):return {k:c for k,c in v.items() if k[0] in indices}


def case(degree,rc,sc):
    r0=4 if rc=='>=4' else rc;s0=4 if sc=='>=4' else sc
    spaces=levi.ideal_bases(degree,r0,s0)
    sourceideal=spaces.get(degree,lift.Span())
    target=levi.target_ideal(spaces,degree)
    extension=lift.Span()
    for row in sourceideal.rows.values():extension.add(row)
    complement=[]
    for word,v in levi.lie_basis(degree):
        if extension.add(v) is not None:complement.append((word,v))
    m=len(complement)
    if not m:return {'r_class':rc,'s_class':sc,'source_dim':0,'horizontal_kernel_dim':0,'status':'ZERO_SOURCE'}
    cols=[target.reduce(levi.delta(v,r0,s0)) for _,v in complement]
    h=[restr(v,(0,1)) for v in cols]
    coeffs=lift.kernel_with_coefficients(h)
    vectors=[lift.combine([v for _,v in complement],c) for c in coeffs]
    k=len(vectors)
    if not k:return {'r_class':rc,'s_class':sc,'source_dim':m,'horizontal_kernel_dim':0,
                     'source_words':[''.join(map(str,w)) for w,_ in complement],
                     'status':'ZERO_HORIZONTAL_KERNEL'}
    base=[restr(target.reduce(levi.delta(v,r0,s0)),(2,)) for v in vectors]
    dr=[poly.diff(restr(target.reduce(levi.delta(v,r0+1,s0)),(2,)),base[j])
        if rc=='>=4' else {} for j,v in enumerate(vectors)]
    ds=[poly.diff(restr(target.reduce(levi.delta(v,r0,s0+1)),(2,)),base[j])
        if sc=='>=4' else {} for j,v in enumerate(vectors)]
    piv=lift.Span()
    for col in base:
        if piv.add(col) is None:
            return {'r_class':rc,'s_class':sc,'source_dim':m,'horizontal_kernel_dim':k,'status':'BASELINE_SINGULAR'}
    rows=sorted(piv.rows)
    symbolic=[]
    for row in rows:
        p=[]
        for j in range(k):
            e={}
            if base[j].get(row,0):e[(0,0)]=base[j][row]
            if dr[j].get(row,0):e[(1,0)]=dr[j][row]
            if ds[j].get(row,0):e[(0,1)]=ds[j][row]
            p.append(e)
        symbolic.append(p)
    det=poly.determinant(symbolic)
    assert det.get((0,0),0)
    return {
        'r_class':rc,'s_class':sc,'source_dim':m,'horizontal_kernel_dim':k,
        'source_words':[''.join(map(str,w)) for w,_ in complement],
        'horizontal_kernel_coefficients':[{str(j):lift.rational_text(c) for j,c in sorted(row.items())} for row in coeffs],
        'target_f3_word_pivots':[''.join(map(str,w)) for i,w in rows],
        'determinant_coefficients':[{'x_power':i,'y_power':j,'coefficient':lift.rational_text(c)} for (i,j),c in sorted(det.items())],
        'status':'CERTIFIED_ONE_SIGN' if len({1 if c>0 else -1 for c in det.values()})==1 else 'MIXED_SIGNS_NEEDS_ANALYSIS',
    }


def main():
    degrees=[(3,2,4),(3,3,3),(3,3,4),(4,4,4)]
    classes=(1,2,3,'>=4')
    result=[]
    for degree in degrees:
        cases=[case(degree,r,s) for r,s in itertools.product(classes,repeat=2)]
        good=('ZERO_SOURCE','ZERO_HORIZONTAL_KERNEL','CERTIFIED_ONE_SIGN')
        result.append({'degree':degree,'cases':cases,'covered':sum(c['status'] in good for c in cases)})
        print('degree',degree,'covered',result[-1]['covered'],'of16',flush=True)
    out=ROOT/'frontier-20261028-levi-critical-minors-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degrees':result,'conditional_on_Levi_free_source_theorem':True,
                               'not_a_formal_proof_or_external_review':True},indent=2)+'\n',encoding='utf-8')
    print('WROTE',out.name)


if __name__=='__main__':main()
