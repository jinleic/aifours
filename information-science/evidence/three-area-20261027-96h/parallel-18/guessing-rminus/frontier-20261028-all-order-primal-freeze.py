#!/usr/bin/env python3
"""Freeze an exact sparse-copy relaxation point after all-order refinements."""
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
spec=spec_from_file_location('primal_scan',ROOT/'frontier-20261028-exact-primal-family-scan.py')
probe=module_from_spec(spec);spec.loader.exec_module(probe)
sparse=probe.sparse;cert=probe.cert
CUTS=ROOT/'frontier-20261028-all-order-cut-refinement-result.json'
OUTPUT=ROOT/'frontier-20261028-all-order-primal-frozen.json'
EXPECTED_CUTS='92f5b31ac81956960d9d34e3c72acfa9acdcba8a54487eab603ec83fab910ba1'


def main():
    started=time.monotonic();raw=CUTS.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED_CUTS:raise ValueError('CUT_HASH_MISMATCH')
    cuts=json.loads(raw)['all_added_cuts']
    data={key:(ROOT/info[0]).read_bytes() for key,info in cert.FILES.items()}
    for key,(_,digest) in cert.FILES.items():cert.pin(key,data[key],digest)
    source=cert.parse_input(data['layout'],data['text']);rows=sparse.build_constraints(source,cuts)
    status,keys,col,vals=probe.solve(rows)
    if vals is None:raise ValueError(('LP_NOT_OPTIMAL',status))
    chosen=None; attempts=[]
    for maxden in (1000,10000,100000,1000000):
        x,bad=probe.check_rounding(rows,keys,col,vals,maxden)
        attempts.append({'max_denominator':maxden,'violations':len(bad),'first':bad[:3]})
        if not bad:chosen=x;break
    if chosen is None:raise ValueError(('NO_EXACT_POINT',attempts))
    original=[Fraction(0)]+[chosen[col[tuple(sparse.sets_from_mask(m))]] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in original));numerators=[int(x*scale) for x in original]
    if max(map(abs,numerators))>=10**8:raise ValueError('INTEGER_RANGE')
    scan=probe.exhaustive_all_n(np.array(numerators,dtype=np.int64))
    if scan['status']!='ALL_DISJOINT_BLOCK_SUBSTITUTIONS_AND_ALL_POSITIVE_N_PASS':
        raise ValueError(('ALL_N_SCAN_FAILED',scan))
    out={'source_hashes':{k:v[1] for k,v in cert.FILES.items()},
         'cut_refinement_sha256':EXPECTED_CUTS,'cuts':cuts,
         'solver_status':status,'exact_constraint_rows':len(rows),
         'exact_primal_objective':str(chosen[col[tuple(cert.BASE)]]),
         'rounding_attempts':attempts,'coordinates':len(keys),
         'primal_values':[{'entropy_variables':k,'value':str(chosen[i])} for i,k in enumerate(keys)],
         'base_integer_scale':scale,'all_n_scan':scan,'elapsed_s':time.monotonic()-started,
         'limits':'Point need not be entropic and need not satisfy the full published copy LP. It obstructs only the specific source-certificate core plus original constraints and conditioned F_n family.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='primal_values'},indent=2))


if __name__=='__main__':main()
