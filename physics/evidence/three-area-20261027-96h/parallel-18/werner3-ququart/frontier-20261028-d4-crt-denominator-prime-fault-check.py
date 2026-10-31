#!/usr/bin/env python3
"""Isolate the CRT prime-versus-common-denominator guard, in memory only."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
AUDIT=ROOT/'frontier-20261028-d4-bound-entrypoint-stdlib-receipt-v2.py'
V3=ROOT/'frontier-20261028-d4-reverse-entrypoint-snapshot-v3-results.json'
OLD=ROOT/'frontier-20261028-d4-modular-crt-identity-proof-results.json'
PINS={AUDIT:'7c879e1c5968ccd367e21ee8589cd93c4bd951af615478c8ed321a69039dbec3',
      V3:'50f53a57e59eda9f40bb28ba2df1feb9ace8ce43e3a2d60530b1db8a34c95687',
      OLD:'f93866ea9171a6dd8b1ecd4ca78fbeb5afe86167aebdc02c701a721da9705d3b'}
OUT=ROOT/'frontier-20261028-d4-crt-denominator-prime-fault-check-results.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if any(sha(p)!=h for p,h in PINS.items()):raise ValueError('input pin mismatch')
spec=importlib.util.spec_from_file_location('bound_receipt_guard',AUDIT)
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
# D is a decimal string far above Python's conservative default digit limit.
import sys
sys.set_int_max_str_digits(0)
D=int(json.loads(OLD.read_bytes())['denominator']);primes=json.loads(V3.read_bytes())['primes_tested']
original=a.valid_primes(primes,D)
fault=list(primes);fault[-1]=2
shape_and_primality=(len(fault)==424 and len(set(fault))==424 and all(type(p)==int and a.prime(p) for p in fault))
all_other_coprime=all(D%p for p in fault[:-1]);guard_rejects=not a.valid_primes(fault,D)
reason_is_coprimality=shape_and_primality and all_other_coprime and D%2==0
if any(sha(p)!=h for p,h in PINS.items()):raise ValueError('actual input changed')
r={'kind':'isolated_crt_denominator_prime_fault_control','auditor_sha256':PINS[AUDIT],
   'v3_result_sha256':PINS[V3],'prior_denominator_receipt_sha256':PINS[OLD],
   'actual_list_guard_passed':original,'mutated_list_still_424_distinct_primes':shape_and_primality,
   'all_untouched_primes_coprime':all_other_coprime,'injected_prime_2_divides_D':D%2==0,
   'correct_guard_rejected':guard_rejects,'rejection_isolated_to_coprimality':reason_is_coprimality,
   'scope':'In-memory prime-list guard sensitivity only; prime 2 is an arithmetic mutation, not a physical target state/control. No 424 residuals, theorem or runtime-integrity proof is performed.',
   'verdict':'PASS' if original and guard_rejects and reason_is_coprimality else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
