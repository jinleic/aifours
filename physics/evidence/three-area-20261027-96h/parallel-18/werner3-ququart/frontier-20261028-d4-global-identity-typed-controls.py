#!/usr/bin/env python3
"""Two in-memory mutation controls: coupled Gram and equality coefficient.

No pinned archive/corrected-data bytes are modified. Each check recomputes
all source-orbit residuals; detected failure is the expected control outcome.
"""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('global_identity_typed_controls',ROOT/'frontier-20261028-independent-d4-global-identity-check.py')
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
original_loader=checker.load_data
original_sha=checker.EXPECTED_CORRECTED
reports=[]

for mode in ('coupled_gram_diagonal','aab_equality_coefficient'):
    checker.EXPECTED_CORRECTED=original_sha
    checker.OUT=ROOT/f'frontier-20261028-d4-global-identity-{mode}-control-residual.json'
    details={}
    def mutated_data():
        pkg,corr=original_loader()
        if mode=='coupled_gram_diagonal':
            idx=next(i for i,t in enumerate(pkg['types']) if t['kind']=='gram')
            num,den=corr['matrices'][idx]['values'][0]
            corr['matrices'][idx]['values'][0]=[str(int(num)+int(den)),den]
            details.update({'type_index':idx,'row':0,'column':0,'delta':'1'})
        else:
            item=next(x for x in corr['equality_coefficients'] if x['group']=='aab')
            item['numerator']=str(int(item['numerator'])+int(item['denominator']))
            details.update({'group':item['group'],'index':item['index'],'delta':'1'})
        checker.EXPECTED_CORRECTED='IN-MEMORY-'+mode.upper()+'-NEGATIVE-CONTROL'
        return pkg,corr
    checker.load_data=mutated_data
    code=checker.main()
    actual=json.loads(checker.OUT.read_text());counts=actual['nonzero_residual_counts']
    ok=code==1 and actual['verdict']=='FAIL' and sum(counts.values())>0
    reports.append({'fault_kind':mode,'fault_details':details,
                    'checker_return_code':code,'checker_verdict':actual['verdict'],
                    'nonzero_orbit_counts':counts,'expected_failure_detected':ok,
                    'elapsed_seconds':actual['elapsed_seconds']})
receipt={'kind':'corrected_certificate_typed_mutation_controls',
         'original_corrected_data_sha256':original_sha,'results':reports,
         'all_expected_failures_detected':all(x['expected_failure_detected'] for x in reports),
         'scope':'In-memory checker fault injection only; not a physical counterexample or original-byte modification.'}
out=ROOT/'frontier-20261028-d4-global-identity-typed-controls-results.json'
out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True,indent=2));raise SystemExit(0 if receipt['all_expected_failures_detected'] else 1)
