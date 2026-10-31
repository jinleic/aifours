#!/usr/bin/env python3
"""Check exact PSD guard sensitivity; mutations are in memory only."""
import hashlib
import importlib.util
import json
import lzma
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
script=ROOT/'frontier-20261028-independent-saved-d4-psd-check.py'
spec=importlib.util.spec_from_file_location('saved_psd_checker_control',script)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sys.set_int_max_str_digits(0)
raw=m.DATA.read_bytes();sha=hashlib.sha256(raw).hexdigest()
if sha!=m.EXPECTED:raise ValueError('corrected data changed')
data=json.loads(lzma.decompress(raw,memlimit=256*1024*1024))
first=data['matrices'][0]
if first['r']!=1:raise ValueError('first stored matrix not 1x1')
num,den=first['values'][0]
negative=[[str(-abs(int(num))-int(den)),den]]
fail_negative=not m.exact_psd(negative,1)[0]
fail_zero_nonzero_row=not m.exact_psd([['0','1'],['1','1'],['1','1'],['0','1']],2)[0]
pass_zero_matrix=m.exact_psd([['0','1'],['0','1'],['0','1'],['0','1']],2)==(True,False)
ok=fail_negative and fail_zero_nonzero_row and pass_zero_matrix
receipt={'kind':'saved_corrected_psd_guard_negative_controls','corrected_data_sha256':sha,
         'mutations':'first stored 1x1 diagonal made negative in memory; zero-pivot off-diagonal matrix; zero matrix',
         'negative_diagonal_rejected':fail_negative,'zero_diagonal_nonzero_row_rejected':fail_zero_nonzero_row,
         'zero_matrix_accepted_psd_not_pd':pass_zero_matrix,'all_expected_outcomes':ok,
         'scope':'Checker guard controls only; no physical state, scientific witness or pinned-byte mutation.'}
out=ROOT/'frontier-20261028-d4-psd-negative-controls-results.json'
out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True,indent=2));raise SystemExit(0 if ok else 1)
