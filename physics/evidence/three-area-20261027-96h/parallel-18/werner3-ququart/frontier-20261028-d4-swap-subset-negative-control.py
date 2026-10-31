#!/usr/bin/env python3
"""Replace each swap subset by its complement, and require coefficient mismatch.

This is a deliberately faulty index convention, not a physical counterexample.
The baseline coefficient checker and all source bytes remain unchanged.
"""
import importlib.util
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
path=ROOT/'frontier-20261028-d4-original-swap-coefficients-check.py'
spec=importlib.util.spec_from_file_location('source_coefficient_check',path)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
reports=[]
for k in range(m.COPIES+1):
    for subset in itertools.combinations(range(m.COPIES),k):
        complement=tuple(i for i in range(m.COPIES) if i not in subset)
        direct=m.direct_trace_polynomial(subset)
        wrong=m.swap_polynomial(complement)
        mismatches=sum(direct[t]!=wrong[t] for t in set(direct)|set(wrong))
        reports.append({'trace_subset':list(subset),'wrong_swap_complement':list(complement),
                        'coefficient_mismatches':mismatches})
passed=all(r['coefficient_mismatches']>0 for r in reports)
receipt={'kind':'deliberate_swap_subset_complement_negative_control',
         'fault':'replace the actual F_S with F_(S complement) in every swap expression',
         'results':reports,'expected_failure_detected':passed,
         'scope':'Symbolic checker sensitivity only; not a candidate physical operator or source change.'}
out=ROOT/'frontier-20261028-d4-swap-subset-negative-control-results.json'
out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True,indent=2));raise SystemExit(0 if passed else 1)
