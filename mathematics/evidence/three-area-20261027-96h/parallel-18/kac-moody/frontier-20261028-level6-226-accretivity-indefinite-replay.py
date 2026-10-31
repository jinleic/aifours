#!/usr/bin/env python3
"""Check positive and negative directions of both recorded slope forms."""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('al6',ROOT/'frontier-20261028-level6-alternate-type-minor-search.py')
al6=importlib.util.module_from_spec(spec);spec.loader.exec_module(al6)


def main():
    P=json.loads((ROOT/'frontier-20261028-level6-free-22-pencil-v1.json').read_text())
    old=json.loads((ROOT/'frontier-20261028-level6-226-naive-accretivity-obstruction-v1.json').read_text())
    rows=al6.full_rows(P);n=P['joint_horizontal_kernel_dim'];assert len(rows)==235 and n==34
    result=[]
    for w,z in zip(old['witnesses'],(1,2)):
        x=[Q(v) for v in w['vector']];assert len(x)==n
        p0=2*sum((Q(v[0][0])*Q(v[0][z]) for v in rows.values()),Q(0))
        negative=2*sum((sum((Q(v[i][0])*x[i] for i in range(n)),Q(0))*
                        sum((Q(v[i][z])*x[i] for i in range(n)),Q(0)) for v in rows.values()),Q(0))
        assert p0==32578 and negative==Q(w['quadratic_value']) and negative<0
        result.append({'slope':w['slope'],'positive_vector':'first standard basis vector',
                       'positive_quadratic_value':str(p0),'negative_vector_from_prior_output':True,
                       'negative_quadratic_value':str(negative),'both_signs_exact':True})
    dest=ROOT/'frontier-20261028-level6-226-accretivity-indefinite-replay-v1.json'
    if dest.exists():raise FileExistsError(dest)
    dest.write_text(json.dumps({'degree':P['degree'],'full_target_rows':235,'checks':result,
                                'status':'BOTH_EUCLIDEAN_SLOPE_FORMS_INDEFINITE',
                                'scope':'specific unweighted Euclidean full-target forms; no D3-kernel or impossibility of other inner product'},indent=2)+'\n')
    print('PASS both Euclidean slope forms: +32578 at e0 and independently checked negative vector;',dest.name)

if __name__=='__main__':main()
