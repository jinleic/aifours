#!/usr/bin/env python3
"""Freeze exact point with all copy equalities and evaluable branch Shannon rows.

Recomputes the bounded separation sequence; missing entropy coordinates are
not filled or classified. The output remains a partial relaxation witness.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from math import lcm
from pathlib import Path
import json
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('closure',ROOT/'frontier-20261028-source-closure-refinement.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
probe=mod.probe;sparse=mod.sparse;cert=mod.cert
OUTPUT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'


def main():
    started=time.monotonic();cutraw=mod.CUTS.read_bytes()
    cuts=json.loads(cutraw)['all_added_cuts']
    data={k:(ROOT/info[0]).read_bytes() for k,info in cert.FILES.items()}
    for k,(_,digest) in cert.FILES.items():cert.pin(k,data[k],digest)
    source=cert.parse_input(data['layout'],data['text'])
    rows=sparse.build_constraints(source,cuts)+mod.copy_rows()
    existing={mod.row_signature(t,lo,hi) for t,lo,hi,_ in rows}
    rounds=[];selected_rows=[];chosen=None;keys=None
    for r in range(15):
        status,keys,col,vals=probe.solve(rows)
        if vals is None:raise ValueError(('LP_NOT_OPTIMAL',r,status))
        reconstruction=[];chosen=None
        for maxden in (1000,10000,100000,1000000):
            x,bad=probe.check_rounding(rows,keys,col,vals,maxden)
            reconstruction.append({'max_denominator':maxden,'bad_count':len(bad),'first':bad[:2]})
            if not bad:chosen=x;break
        if chosen is None:raise ValueError(('EXACT_POINT_NOT_RECONSTRUCTED',r,reconstruction))
        checked,unknown,violated=mod.scan_branch_cmi(keys,vals,existing)
        ordered=sorted(violated.items(),key=lambda item:item[1][0])[:600]
        rounds.append({'round':r,'exact_row_count':len(rows),'reconstruction':reconstruction,
                       'branch_checks':checked,'unknown':unknown,'unique_violated':len(violated),
                       'added':len(ordered)})
        for signature,(slack,terms,meta) in ordered:
            existing.add(signature);rows.append((terms,0.0,highspy.kHighsInf,meta))
            selected_rows.append({'terms':[[list(key),value] for key,value in sorted(terms.items())],
                                  'metadata':meta})
        if not ordered:break
    else:raise ValueError('NO_CLOSURE_IN_15_ROUNDS')
    original=[Fraction(0)]+[chosen[col[tuple(sparse.sets_from_mask(m))]] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in original));ints=[int(x*scale) for x in original]
    if max(map(abs,ints))>=10**8:raise ValueError('INTEGER_RANGE')
    family=probe.exhaustive_all_n(np.array(ints,dtype=np.int64))
    if family['status']!='ALL_DISJOINT_BLOCK_SUBSTITUTIONS_AND_ALL_POSITIVE_N_PASS':
        raise ValueError(('FAMILY_VIOLATION',family))
    out={'input_cut_sha256':sha256(cutraw).hexdigest(),
         'source_hashes':{k:info[1] for k,info in cert.FILES.items()},
         'exact_primal_objective':str(chosen[col[tuple(cert.BASE)]]),
         'coordinates':len(keys),'base_integer_scale':scale,
         'primal_values':[{'entropy_variables':key,'value':str(chosen[i])} for i,key in enumerate(keys)],
         'initial_fn_cuts':cuts,'added_branch_CMI_rows':selected_rows,
         'full_copy_equalities_included':True,'rounds':rounds,'all_n_scan':family,
         'elapsed_s':time.monotonic()-started,
         'limits':'Only entropy coordinates actually present are assigned; unevaluable full-source Shannon rows are not passed. Not a full LP or an entropic-law witness.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('primal_values','added_branch_CMI_rows')},indent=2))
    print('added_branch_CMI_rows',len(selected_rows))


if __name__=='__main__':main()
