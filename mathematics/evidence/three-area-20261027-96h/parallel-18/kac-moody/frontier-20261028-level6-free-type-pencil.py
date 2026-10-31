#!/usr/bin/env python3
"""Build an entire level-six free-Levi primitive D3 pencil on r,s>=6.

No node3 Serre seed occurs through level six in the claimed region. Actual
source identification and any full-parameter rank require separate proof.
"""
import argparse
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
levi=load('levi','frontier-20261028-levi-lie-engine.py');poly=load('poly','frontier-20261028-symbolic-minors.py');lift=levi.lift


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);args=ap.parse_args()
    a,b=args.a,args.b;degree=(a,b,6);out=ROOT/f'frontier-20261028-level6-free-{a}{b}-pencil-v1.json'
    if out.exists():raise FileExistsError(out)
    source=levi.lie_basis(degree);horizontal=[]
    for _,v in source:
        c={}
        for i,g in enumerate(('f1','f2')):c.update({(i,w):q for w,q in levi.levi_action(v,g,6,6).items()})
        horizontal.append(c)
    coeffs=lift.kernel_with_coefficients(horizontal)
    vectors=[lift.combine([v for _,v in source],c) for c in coeffs];k=len(vectors)
    base=[levi.lower3(v,6,6) for v in vectors]
    dx=[poly.diff(levi.lower3(v,7,6),base[j]) for j,v in enumerate(vectors)]
    dy=[poly.diff(levi.lower3(v,6,7),base[j]) for j,v in enumerate(vectors)]
    span=lift.Span()
    for col in base:span.add(col)
    result={'degree':degree,'free_source_dim':len(source),'joint_horizontal_kernel_dim':k,'baseline_f3_rank':len(span),
            'source_words':[''.join(map(str,w)) for w,_ in source],
            'horizontal_kernel_coefficients':[{str(i):lift.rational_text(q) for i,q in sorted(c.items())} for c in coeffs],
            'baseline':{'r':6,'s':6},'variables':'x=r-6,y=s-6',
            'scope':'full free-Levi selected type only, source/target ideal absence and actual full-Cartan identification are written inputs'}
    if not k:result['status']='ZERO_HORIZONTAL_KERNEL'
    elif len(span)<k:result['status']='BASELINE_RANK_DEFECT'
    else:
        rows=sorted(span.rows);result['selected_target_words']=[''.join(map(str,w)) for w in rows]
        result['matrix']=[[[lift.rational_text(col.get(row,0)),lift.rational_text(xx.get(row,0)),lift.rational_text(yy.get(row,0))]
                           for col,xx,yy in zip(base,dx,dy)] for row in rows]
        result['status']='BASELINE_MINOR_ONLY_NOT_GLOBAL'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('level6',degree,'source',len(source),'lowest',k,'baseline rank',len(span),result['status'],out.name,flush=True)

if __name__=='__main__':main()
