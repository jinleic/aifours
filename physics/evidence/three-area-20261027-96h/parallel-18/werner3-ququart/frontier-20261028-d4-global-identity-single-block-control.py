#!/usr/bin/env python3
"""Add one to one corrected multiplier entry in memory; require identity failure.

Checker-sensitivity control only, not a candidate counterexample. Original
archive and corrected JSON remain byte unchanged.
"""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
source=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
spec=importlib.util.spec_from_file_location('global_identity_single_block_control',source)
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
original_loader=checker.load_data
original_sha=checker.EXPECTED_CORRECTED
checker.OUT=ROOT/'frontier-20261028-d4-global-identity-single-block-control-residual.json'


def mutated_data():
    pkg,corr=original_loader()
    first=corr['matrices'][0]
    if first['r']!=1 or len(first['values'])!=1:
        raise ValueError('expected first block shape changed')
    num,den=first['values'][0]
    first['values'][0]=[str(int(num)+int(den)),den]
    checker.EXPECTED_CORRECTED='IN-MEMORY-SINGLE-BLOCK-NEGATIVE-CONTROL'
    return pkg,corr


checker.load_data=mutated_data
code=checker.main()
actual=json.loads(checker.OUT.read_text());counts=actual['nonzero_residual_counts']
expected_failure=code==1 and actual['verdict']=='FAIL' and sum(counts.values())>0
receipt={'kind':'deliberate_single_corrected_block_entry_negative_control',
         'original_corrected_data_sha256':original_sha,
         'fault':'add exactly one to the first corrected 1x1 multiplier in memory only',
         'global_checker_return_code':code,'global_checker_verdict':actual['verdict'],
         'observed_nonzero_residual_counts':counts,'expected_failure_detected':expected_failure,
         'scope':'Fault injection tests checker sensitivity, not a physical counterexample or source modification.'}
out=ROOT/'frontier-20261028-d4-global-identity-single-block-control-results.json'
out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True,indent=2));raise SystemExit(0 if expected_failure else 1)
