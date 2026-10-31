#!/usr/bin/env python3
"""Fault-inject zero certificate terms and require independent identity failure.

This is a checker sensitivity control, NOT a scientific counterexample. Input
bytes remain unchanged; every corrected Z and lambda is replaced with zero only
in memory after the baseline data hash has been checked.
"""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
source=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
spec=importlib.util.spec_from_file_location('global_identity_fault_control',source)
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
original_loader=checker.load_data
original_sha=checker.EXPECTED_CORRECTED
checker.OUT=ROOT/'frontier-20261028-d4-global-identity-zeroed-control-residual.json'


def zeroed_data():
    pkg,corr=original_loader()
    for matrix in corr['matrices']:
        matrix['values']=[['0','1'] for _ in matrix['values']]
    for entry in corr['equality_coefficients']:
        entry['numerator']='0';entry['denominator']='1'
    checker.EXPECTED_CORRECTED='IN-MEMORY-ZEROED-NEGATIVE-CONTROL'
    return pkg,corr


checker.load_data=zeroed_data
code=checker.main()
actual=json.loads(checker.OUT.read_text())
nonzero=actual['nonzero_residual_counts']
expected_failure=code==1 and actual['verdict']=='FAIL' and sum(nonzero.values())>0
receipt={'kind':'deliberate_zeroed_certificate_terms_negative_control',
         'original_corrected_data_sha256':original_sha,
         'fault':'all Z multipliers and all equality coefficients replaced by zero in memory only',
         'global_checker_return_code':code,'global_checker_verdict':actual['verdict'],
         'observed_nonzero_residual_counts':nonzero,
         'expected_failure_detected':expected_failure,
         'scope':'Fault injection tests checker sensitivity. It is not a physical counterexample or a modification of pinned input files.'}
out=ROOT/'frontier-20261028-d4-global-identity-negative-control-results.json'
out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True,indent=2))
raise SystemExit(0 if expected_failure else 1)
