#!/usr/bin/env python3
"""Replay independent full d4 identity with script/helper bytes pinned.

This is a binding/reproducibility replay of our own independent implementation,
not an additional independent model, formal kernel or physical experiment.
"""
import hashlib
import importlib.util
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
EXPECTED={
 'frontier-20261028-independent-d4-global-identity-check.py':'b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d',
 'frontier-20261028-independent-d4-base-check.py':'bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec',
 'frontier-20261028-independent-d4-aux-equality-objective-check.py':'0949e4945fa5cd20bac6a5d4e976c6756f97a16de2fb5c6b20c759f60798e99c',
 'frontier-20261028-tomar-release-ep3-v3.tar.gz':'2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3',
 'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz':'c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94',
}


def hashes():
    return {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in EXPECTED}


def main():
    start=time.monotonic(); before=hashes()
    if before!=EXPECTED:raise ValueError('pinned implementation, helper, or data bytes changed')
    name='frontier-20261028-independent-d4-global-identity-check.py'
    spec=importlib.util.spec_from_file_location('pinned_independent_global',ROOT/name)
    checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
    out=ROOT/'frontier-20261028-d4-bound-independent-identity-result.json'
    checker.OUT=out
    code=checker.main()
    after=hashes()
    if after!=EXPECTED:raise ValueError('pinned input changed during the check')
    data=out.read_bytes();result=json.loads(data)
    ok=code==0 and result['verdict']=='PASS' and all(v==0 for v in result['nonzero_residual_counts'].values())
    receipt={'kind':'pinned_independent_d4_exact_identity_binding_replay',
             'input_sha256_before':before,'input_sha256_after':after,
             'result_path':out.name,'result_sha256':hashlib.sha256(data).hexdigest(),
             'actual_orbit_counts':result['independent_orbit_counts'],
             'nonzero_residual_counts':result['nonzero_residual_counts'],
             'common_denominator_bits':result['common_denominator_bits'],
             'elapsed_seconds':round(time.monotonic()-start,3),
             'scope':'Same independent global implementation rerun with verified helper/input hashes; not a second independently developed implementation or a formal theorem gate.',
             'verdict':'PASS' if ok else 'FAIL'}
    p=ROOT/'frontier-20261028-d4-bound-independent-identity-replay-receipt.json'
    p.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps(receipt,sort_keys=True,indent=2));return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
