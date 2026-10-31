#!/usr/bin/env python3
"""Bounded alternate f3-minor search for mixed-sign critical-type certificates."""
import importlib.util
import json
import random
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('critical',ROOT/'frontier-20261028-levi-critical-minors.py')
critical=importlib.util.module_from_spec(spec);spec.loader.exec_module(critical)
levi,poly,lift=critical.levi,critical.poly,critical.lift


def solve(degree,original,seed):
    rc,sc=original['r_class'],original['s_class']
    r0=4 if rc=='>=4' else rc;s0=4 if sc=='>=4' else sc
    target=levi.target_ideal(levi.ideal_bases(degree,r0,s0),degree)
    basis=[lift.lyndon_bracket(tuple(map(int,w))) for w in original['source_words']]
    coeffs=[{int(k):Fraction(v) for k,v in row.items()} for row in original['horizontal_kernel_coefficients']]
    vectors=[lift.combine(basis,row) for row in coeffs]
    keep=lambda x:critical.restr(x,(2,))
    base=[keep(target.reduce(levi.delta(v,r0,s0))) for v in vectors]
    dr=[poly.diff(keep(target.reduce(levi.delta(v,r0+1,s0))),base[j]) if rc=='>=4' else {} for j,v in enumerate(vectors)]
    ds=[poly.diff(keep(target.reduce(levi.delta(v,r0,s0+1))),base[j]) if sc=='>=4' else {} for j,v in enumerate(vectors)]
    keys=sorted(set().union(*(set(v) for v in base+dr+ds)))
    rng=random.Random(seed)
    for attempt in range(1,501):
        order=keys[:];rng.shuffle(order);priority={key:i for i,key in enumerate(order)}
        sp=lift.Span()
        if any(sp.add({priority[k]:c for k,c in col.items()}) is None for col in base):continue
        rows=[order[i] for i in sorted(sp.rows)]
        matrix=[]
        for row in rows:
            rr=[]
            for j in range(len(vectors)):
                d={}
                if base[j].get(row,0):d[(0,0)]=base[j][row]
                if dr[j].get(row,0):d[(1,0)]=dr[j][row]
                if ds[j].get(row,0):d[(0,1)]=ds[j][row]
                rr.append(d)
            matrix.append(rr)
        determinant=poly.determinant(matrix)
        if determinant.get((0,0),0) and len({1 if c>0 else -1 for c in determinant.values()})==1:
            return {**original,'target_f3_word_pivots':[''.join(map(str,w)) for _,w in rows],
                    'determinant_coefficients':[{'x_power':i,'y_power':j,'coefficient':lift.rational_text(c)} for (i,j),c in sorted(determinant.items())],
                    'status':'CERTIFIED_ONE_SIGN_ALTERNATE','attempt':attempt,'search_seed':seed}
    return {**original,'status':'NO_ONE_SIGN_MINOR_WITHIN_500','search_seed':seed}


def main():
    data=json.loads((ROOT/'frontier-20261028-levi-critical-minors-v1.json').read_text(encoding='utf-8'))
    todo=[(tuple(d['degree']),c) for d in data['degrees'] for c in d['cases'] if c['status']=='MIXED_SIGNS_NEEDS_ANALYSIS']
    assert len(todo)==3
    output=[{'degree':degree,'case':solve(degree,c,1030+j)} for j,(degree,c) in enumerate(todo)]
    path=ROOT/'frontier-20261028-levi-critical-alternates-v1.json'
    if path.exists():raise FileExistsError(path)
    path.write_text(json.dumps({'cases':output,'not_a_formal_proof_or_external_review':True},indent=2)+'\n',encoding='utf-8')
    print('alternates',len(output),'found',sum(x['case']['status']=='CERTIFIED_ONE_SIGN_ALTERNATE' for x in output),
          'attempts',[x['case'].get('attempt') for x in output],path.name)


if __name__=='__main__':main()
