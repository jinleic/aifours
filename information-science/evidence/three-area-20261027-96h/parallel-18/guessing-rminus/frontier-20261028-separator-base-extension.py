#!/usr/bin/env python3
"""Test full source-copy branches for the one-copy-separator-refined base."""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import gc
import json
import sys
import time

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
spec=spec_from_file_location('extension',ROOT/'frontier-20261028-base-projection-extension.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
OUTPUT=ROOT/'frontier-20261028-separator-base-extension-result.json'


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    data=json.loads(raw);base=set(mod.BASE)
    values={tuple(x['entropy_variables']):Fraction(x['value']) for x in data['primal_values']
            if set(x['entropy_variables'])<=base}
    if len(values)!=1023:raise ValueError('BASE_COUNT')
    forms=[key for key in mod.cert.copy_forms() if key and key[0][1]>0]
    results=[]
    for number,variables in enumerate(mod.BRANCHES,1):
        result=mod.solve_branch(number,variables,values,forms);results.append(result)
        path=ROOT/f'frontier-20261028-separator-base-extension-branch-{number}.json'
        with path.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
        print(json.dumps({k:v for k,v in result.items() if k!='auxiliary_values'},indent=2),flush=True)
        gc.collect()
    output={'input_sha256':EXPECTED,'branches':results,
            'all_three_exact_branch_extensions':all(r.get('exact_rational_branch_extension_found',False) for r in results),
            'elapsed_s':time.monotonic()-start,
            'limits':'Full source-LP feasibility only if exact extensions of all three branches are checked; no entropic realization. Numerical failure is not proof.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(output,stream,indent=2);stream.write('\n')


if __name__=='__main__':main()
