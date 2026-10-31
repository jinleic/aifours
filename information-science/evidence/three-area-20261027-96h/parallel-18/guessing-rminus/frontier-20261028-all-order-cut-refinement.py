#!/usr/bin/env python3
"""Refine source-certificate LP by exact separated conditioned F_n cuts.

Primal points are checked exactly after rationalization; solver objectives are
still numerical proposals. An improved bound requires a separate exact dual.
"""
from fractions import Fraction
from importlib.util import module_from_spec,spec_from_file_location
from math import lcm
from pathlib import Path
import hashlib
import json
import sys
import time

import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
spec=spec_from_file_location('primal_scan',ROOT/'frontier-20261028-exact-primal-family-scan.py')
probe=module_from_spec(spec);spec.loader.exec_module(probe)
sparse=probe.sparse;cert=probe.cert
OUTPUT=ROOT/'frontier-20261028-all-order-cut-refinement-result.json'
PREV=ROOT/'frontier-20261028-sparse-certificate-cutting-result.json'
MAX_ROUNDS=20
MAX_WALL_SECONDS=100.0


def main():
    started=time.monotonic()
    data={key:(ROOT/info[0]).read_bytes() for key,info in cert.FILES.items()}
    for key,(_,expected) in cert.FILES.items():cert.pin(key,data[key],expected)
    source=cert.parse_input(data['layout'],data['text'])
    old=PREV.read_bytes();extras=json.loads(old)['added_cuts']
    # The known exact separating block from the previous independent scan.
    initial={'kind':'copy-family','A_mask':2,'B_mask':512,'C_mask':32,
             'D_mask':12,'condition_mask':401}
    for n in (12,24,48):extras.append(dict(initial,n=n))
    seen={(m['n'],m.get('A_mask'),m.get('B_mask'),m.get('C_mask'),m.get('D_mask'),m.get('condition_mask')) for m in extras}
    rounds=[];stop='round limit'
    for round_index in range(MAX_ROUNDS):
        if time.monotonic()-started > MAX_WALL_SECONDS:
            stop='wall limit';break
        rows=sparse.build_constraints(source,extras)
        t=time.monotonic();status,keys,col,vals=probe.solve(rows)
        record={'round':round_index,'constraints':len(rows),'extra_cuts':len(extras),
                'solver_status':status,'solve_elapsed_s':time.monotonic()-t}
        if vals is None:
            stop='LP not optimal';rounds.append(record);break
        float_obj=float(vals[col[tuple(cert.BASE)]])
        record['objective_float_unverified']=float_obj
        chosen=None; rounding=[]
        for maxden in (1000,10000,100000,1000000):
            x,bad=probe.check_rounding(rows,keys,col,vals,maxden)
            # Here an objective DIFFERENT from 1847/276 is sought, not an error.
            bad=[entry for entry in bad if entry['kind']!='objective']
            rounding.append({'max_denominator':maxden,'bad_count':len(bad),'first_bad':bad[:2]})
            if not bad:chosen=x;break
        record['exact_primal_rounding']=rounding
        if chosen is None:
            stop='could not reconstruct a feasible exact primal';rounds.append(record);break
        objective=chosen[col[tuple(cert.BASE)]]
        record['exact_feasible_primal_objective']=str(objective)
        H=[Fraction(0)]+[chosen[col[tuple(sparse.sets_from_mask(m))]] for m in range(1,1024)]
        scale=lcm(*(x.denominator for x in H)); integers=[int(x*scale) for x in H]
        record['base_integer_scale']=scale
        if max(map(abs,integers))>=10**8:
            stop='base integer range blocker';rounds.append(record);break
        scan=probe.exhaustive_all_n(np.array(integers,dtype=np.int64));record['scan']=scan
        new=[]
        if scan['status']=='VIOLATION_AT_LARGE_N':
            A,B,C,D,Z=scan['assignment_masks']; a=scan['a_scaled']; c=scan['c_scaled']
            if scan['d_scaled']!=0 or c>=0:
                raise ValueError('invalid large-n scan result')
            n=a//(-c)+1
        elif scan['status']=='EXACT_VIOLATION':
            A,B,C,D,Z=scan['example']['assignment_masks'];n=scan['example']['n']
        elif scan['status']=='ALL_DISJOINT_BLOCK_SUBSTITUTIONS_AND_ALL_POSITIVE_N_PASS':
            stop='exact primal passes all scanned block substitutions and all n';rounds.append(record);break
        else:
            stop=scan['status'];rounds.append(record);break
        if n>10000:
            stop='separating n exceeds bounded coefficient guard';rounds.append(record);break
        for multiplier in (1,2,4):
            order=n*multiplier
            if order>10000:continue
            item={'kind':'copy-family','n':order,'A_mask':A,'B_mask':B,
                  'C_mask':C,'D_mask':D,'condition_mask':Z}
            key=(order,A,B,C,D,Z)
            if key not in seen:
                seen.add(key);extras.append(item);new.append(item)
        record['new_cuts']=new
        rounds.append(record)
        checkpoint=ROOT/f'frontier-20261028-all-order-cut-round-{round_index}.json'
        with checkpoint.open('x',encoding='utf-8') as stream:
            json.dump(record,stream,indent=2);stream.write('\n')
        if not new:
            stop='duplicate violated cut';break
    out={'source_rows':len(source),'previous_sha256':hashlib.sha256(old).hexdigest(),
         'source_pins':{key:value[1] for key,value in cert.FILES.items()},
         'rounds':rounds,'all_added_cuts':extras,'stop':stop,
         'total_elapsed_s':time.monotonic()-started,
         'limits':'Feasible exact primal points are polymatroid/copy relaxation witnesses, not entropic laws. Solver optimality and improved upper bounds require a separate exact dual certificate.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
