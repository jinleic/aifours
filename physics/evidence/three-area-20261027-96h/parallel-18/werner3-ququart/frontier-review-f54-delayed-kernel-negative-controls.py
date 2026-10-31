#!/usr/bin/env python3
"""Fault controls for independently coded rational delayed-kernel diagnostic."""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'frontier-review-f54-delayed-kernel-independent-check.py'
EXPECTED='62bb0037ff73b5ba0a6157fff11afc70265a2b55053c6030366020053d6babcc'
OUT=ROOT/'frontier-review-f54-delayed-kernel-negative-controls-results.json'
if hashlib.sha256(SRC.read_bytes()).hexdigest()!=EXPECTED:raise ValueError('diagnostic source mismatch')
spec=importlib.util.spec_from_file_location('f54_exact_diagnostic',SRC)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
h=m.H;S=m.T-h;t=F(6,5)
original=m.kernel


def sign_flipped_C(r,hh):
    val=original(r,hh)
    if hh and r>=hh:
        # Replacing the paired BLh+C term by BLh-C changes K_B by -2Qe^(P(r-h))C.
        val=m.add(val,m.scale(F(-2),m.mv(m.Q,m.expP(r-hh,m.C))))
    return val


baseline=m.direct(t,h,S)
m.kernel=sign_flipped_C
wrong_sign=m.via_kernel(t,h,S)
m.kernel=original
correct=m.via_kernel(t,h,S)
wrong_atom=m.add(correct,m.scale(-m.LH*m.v(t-h,S),m.B0))
zero_S=m.T;zero_t=F(11,15)
zero_direct=m.direct(zero_t,F(0),zero_S)
zero_correct=m.via_kernel(zero_t,F(0),zero_S)
wrong_coincident=m.add(zero_correct,m.scale(-m.LH*m.v(zero_t,zero_S),m.B0))
checks={'baseline_positive_delay_exact':baseline==correct,
        'flipped_delayed_C_detected':wrong_sign!=baseline,
        'omitted_delayed_noise_atom_detected':wrong_atom!=baseline,
        'baseline_zero_delay_exact':zero_direct==zero_correct,
        'omitted_combined_tap_atom_detected':wrong_coincident!=zero_direct}
receipt={'kind':'exact_delayed_kernel_checker_fault_controls','checks':checks,
         'positive_delay':'2/5','T':'7/5','positive_delay_test_time':str(t),
         'scope':'Deliberately faulty code conventions on exact rational diagnostics; not physical counterexamples or universal proof.',
         'verdict':'PASS' if all(checks.values()) else 'FAIL'}
OUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True,indent=2));raise SystemExit(0 if receipt['verdict']=='PASS' else 1)
