#!/usr/bin/env python3
"""Third rank engine: dense FLINT modular rank of witness square submatrices.

Rows are reconstructed using the separately authored witness replay helper;
rank arithmetic is independent of both sparse-elimination implementations.
"""
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-python-deps'))
import flint
HELPER=ROOT/'frontier-20261028-independent-local-commutant-witness-check.py'
WIT=ROOT/'frontier-20261028-local-commutant-pivot-rows.json'
OUT=ROOT/'frontier-20261028-dense-local-commutant-witness-check-results.json'
EXPECTED_HELPER='5a9a0e017900e4a978e6824e4b0d4510634726c4d397f0f7c33f1deff85e8a1f'
EXPECTED_WIT='1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    start=time.monotonic()
    if sha(HELPER)!=EXPECTED_HELPER or sha(WIT)!=EXPECTED_WIT:raise ValueError('input hash mismatch')
    spec=importlib.util.spec_from_file_location('independent_commutant_reference',HELPER)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    witness=json.loads(WIT.read_bytes());p=witness['prime']
    if not helper.isprime(p):raise ValueError('modulus not prime')
    out=[]
    for case in witness['cases']:
        n=case['dimension'];_,coords,lookup=helper.universe(n)
        cols=case['pivot_columns'];labels=case['witness_rows'];r=len(cols)
        if len(labels)!=r or len(set(cols))!=r or r!=case['required_commutator_rank']:
            raise ValueError('bad witness dimensions')
        selected={c:j for j,c in enumerate(cols)}
        values=[0]*(r*r)
        for i,label in enumerate(labels):
            row=helper.row_from_label(n,label,lookup)
            for c,v in row.items():
                if c in selected:values[i*r+selected[c]]=v%p
        matrix=flint.nmod_mat(r,r,values,p)
        print('BEGIN dense modular rank',n,'size',r,flush=True)
        t=time.monotonic();rank=matrix.rank()
        item={'dimension':n,'square_size':r,'rank_mod_p':rank,'elapsed_seconds':round(time.monotonic()-t,3)}
        if rank!=r:raise ValueError('witness square not full rank')
        if n==2:
            for j in range(r):matrix[r-1,j]=matrix[0,j]
            item['duplicate_row_rank']=matrix.rank()
            if item['duplicate_row_rank']>=r:raise ValueError('duplicate-row control failed')
        out.append(item)
        print('DONE',item,flush=True)
    receipt={'kind':'dense_modular_commutant_witness_rank_replay','prime':p,'prime_trial_division':'PASS',
             'witness_sha256':EXPECTED_WIT,'row_reconstruction_helper_sha256':EXPECTED_HELPER,
             'cases':out,'elapsed_seconds':round(time.monotonic()-start,3),'flint_version':flint.__version__,
             'scope':'Independent dense rank engine on saved selected rows/columns; shares row reconstruction with the separate witness checker. Not a different model-family/formal-kernel review.',
             'verdict':'PASS'}
    OUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps(receipt,sort_keys=True,indent=2));return 0


if __name__=='__main__':raise SystemExit(main())
