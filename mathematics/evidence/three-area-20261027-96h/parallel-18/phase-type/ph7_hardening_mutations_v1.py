#!/usr/bin/env python3
"""Mutate one synthetic-test protection at a time; never run GLOBAL obligations.

Each shadow tree is retained under the owner's root. Exactly one unique source
anchor changes in each mutant. A kill requires the intended named single test
actually ran and failed; imports/syntax errors/timeouts are INVALID, not kills.
"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
TEST='ph7_hardening_synthetic_tests_v1.py'
MODULES=['ph7_gate_runtime_v1.py','ph7_environment_guard_v1.py','ph7_global_gate_v1.py',
         'ph7_source_binding_v1.py','ph7_global_obligations_v1.py','frontier-20261029-ph7-local-hardened-v2.py',
         'frontier-20261029-ph7-global-verifier-v1.py',TEST]
MUTANTS=[
 ('duplicate-json','ph7_gate_runtime_v1.py',"require(key not in out, 'DUPLICATE_JSON_KEY', key)","require(True, 'DUPLICATE_JSON_KEY', key)",'RuntimeSafetyTests.test_duplicate_json_rejected'),
 ('input-hash','ph7_gate_runtime_v1.py',"require(sha256(data) == expected_sha, 'INPUT_SHA_MISMATCH', str(path))","require(True, 'INPUT_SHA_MISMATCH', str(path))",'RuntimeSafetyTests.test_bad_hash_and_missing_rejected'),
 ('exclusive-output','ph7_gate_runtime_v1.py','os.O_WRONLY | os.O_CREAT | os.O_EXCL |','os.O_WRONLY | os.O_CREAT |','RuntimeSafetyTests.test_existing_output_never_opened'),
 ('signal-stop','ph7_gate_runtime_v1.py','if self.stop_signal is not None:\n            raise GateError','if False:\n            raise GateError','RuntimeSafetyTests.test_signal_is_sticky_and_checked'),
 ('receipt-signal','ph7_gate_runtime_v1.py',"if guard.stop_signal is not None:\n                record['status'] = 'INCOMPLETE'","if False:\n                record['status'] = 'INCOMPLETE'",'RuntimeSafetyTests.test_signal_during_receipt_is_incomplete'),
 ('deadline-stop','ph7_gate_runtime_v1.py','if self.clock() >= self.end:','if False:','RuntimeSafetyTests.test_deadline_fail_closed'),
 ('rss-stop','ph7_gate_runtime_v1.py','if rss > self.rss_cap:','if False:','RuntimeSafetyTests.test_rss_fail_closed'),
 ('root-containment','ph7_gate_runtime_v1.py',"require(resolved == root or root in resolved.parents, 'PATH_OUTSIDE_ROOT', str(path))","require(True, 'PATH_OUTSIDE_ROOT', str(path))",'RuntimeSafetyTests.test_inside_root_guard'),
 ('unlisted-dependency','ph7_environment_guard_v1.py',"require(rel in expected, 'ENV_UNLISTED_FILE', rel)","require(True, 'ENV_UNLISTED_FILE', rel)",'EnvironmentSafetyTests.test_unlisted_file_fails_for_correct_reason'),
 ('missing-dependency','ph7_environment_guard_v1.py',"require(seen==set(expected), 'ENV_INVENTORY_MISSING', ','.join(sorted(set(expected)-seen)[:5]))","require(True, 'ENV_INVENTORY_MISSING', '')",'EnvironmentSafetyTests.test_missing_inventoried_file'),
 ('ordered-source','ph7_source_binding_v1.py',"require(record=={'role':role,'path':str(path),'sha256':sha}, 'SOURCE_ORDER_OR_PIN_MISMATCH',role)","require(True, 'SOURCE_ORDER_OR_PIN_MISMATCH',role)",'SourceOrderTests.test_mandatory_overlay_order'),
 ('go-authorization','ph7_global_gate_v1.py',"go['status']=='AUTHORIZED'","True",'AdmissionTests.test_no_go_cannot_admit'),
 ('historical-review-finding','ph7_global_gate_v1.py',"rec['verdict']==verdict and _sha(rec['review_sha256']) and rec['scope_sha256']==scope","True",'AdmissionTests.test_historical_majors_not_erased'),
 ('face-review','ph7_global_gate_v1.py',"face['verdict']=='SUPPORTED_NO_MAJOR'","True",'AdmissionTests.test_face_review_required'),
 ('distinct-independent-checker','ph7_global_gate_v1.py',"checker['code_sha256'] not in (expected['author_verifier_sha256'],expected['obligation_engine_sha256'])","True",'AdmissionTests.test_independent_must_be_distinct'),
 ('hardening-review','ph7_global_gate_v1.py',"hard['verdict']=='NO_MAJOR' and _sha(hard['report_sha256']) and hard['verifier_sha256']==expected['author_verifier_sha256']","True",'AdmissionTests.test_hardening_review_required'),
 ('all-seven-covers','ph7_global_obligations_v1.py',"require(isinstance(covers,dict) and set(covers)==set(OBLIGATIONS), 'OBLIGATION_SET_MISMATCH')","require(True, 'OBLIGATION_SET_MISMATCH')",'BernsteinAndCoverageTests.test_missing_bundle_cover_rejected_without_science'),
 ('binary-tree-coverage','ph7_global_obligations_v1.py',"require(set(node) == {'0', '1'}, 'INCOMPLETE_PATH_COVER')","require(True, 'INCOMPLETE_PATH_COVER')",'BernsteinAndCoverageTests.test_coverage_requires_both_children'),
 ('interior-face-strictness','ph7_global_obligations_v1.py','if t.values[idx] <= 0: return False','if t.values[idx] < 0: return False','BernsteinAndCoverageTests.test_internal_admissible_face_must_be_positive'),
 ('sorted-equality','ph7_global_obligations_v1.py','bounds[i][0] > bounds[j][1]','bounds[i][0] >= bounds[j][1]','BernsteinAndCoverageTests.test_sorted_interval_equality_not_discarded'),
 ('exact-anchor-floor','ph7_global_obligations_v1.py','(lower*1024).__floor__()','(lower*1024).__ceil__()','BernsteinAndCoverageTests.test_adaptive_anchor_uses_exact_floor'),
 ('common-basis','ph7_global_obligations_v1.py',"require(all(t.shape == shape for t in tensors), 'COMMON_BASIS_MISMATCH')","require(True, 'COMMON_BASIS_MISMATCH')",'BernsteinAndCoverageTests.test_common_basis_mismatch_rejected'),
 ('optimized-assert-conversion','frontier-20261029-ph7-local-hardened-v2.py',"return builtin_ast.copy_location(builtin_ast.Expr(call), node)","return builtin_ast.copy_location(builtin_ast.Pass(), node)",'RuntimeSafetyTests.test_optimized_mode_assertions_are_active'),
 ('local-engine-pin','frontier-20261029-ph7-local-hardened-v2.py',"runtime['require'](expected == ENGINE_SHA, 'ENGINE_BYTES_NOT_PINNED')","runtime['require'](True, 'ENGINE_BYTES_NOT_PINNED')",'RuntimeSafetyTests.test_local_engine_bytes_must_be_pinned'),
]

def sha(b):return hashlib.sha256(b).hexdigest()
def write_new(path,data):
    with path.open('xb') as f:f.write(data)

def main():
    run=ROOT/'hardening-mutation-shadows-v1'/str(os.getpid())
    run.mkdir(parents=True,exist_ok=False)
    originals={name:(ROOT/name).read_bytes() for name in MODULES}
    results=[]
    for name,file,old,new,test in MUTANTS:
        src=originals[file].decode();count=src.count(old)
        if count!=1:raise RuntimeError(f'{name}: unique anchor count {count}')
        changed=src.replace(old,new).encode()
        if changed==originals[file]:raise RuntimeError(f'{name}: no change')
        shadow=run/name;shadow.mkdir()
        for component,data in originals.items():write_new(shadow/component,changed if component==file else data)
        env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PH7_TEST_MODULE_ROOT':str(shadow)}
        try:
            run_result=subprocess.run([sys.executable,'-O',str(shadow/TEST),test],env=env,capture_output=True,text=True,timeout=30)
            text=run_result.stdout+run_result.stderr
            valid='Ran 1 test' in text and 'SyntaxError' not in text and 'ImportError' not in text
            status='KILLED' if valid and run_result.returncode==1 else ('SURVIVED' if valid and run_result.returncode==0 else 'INVALID')
            code=run_result.returncode
        except subprocess.TimeoutExpired as exc:
            text=str(exc);status='INVALID_TIMEOUT';code=None
        write_new(shadow/'test-output.txt',text.encode())
        results.append({'id':name,'file':file,'test':test,'old_sha256':sha(originals[file]),'mutant_sha256':sha(changed),'status':status,'exit_code':code})
        print(name,status,flush=True)
    report={'schema_version':1,'kind':'PH7_SYNTHETIC_SINGLE_PROTECTION_MUTATIONS_V1',
            'scope':'synthetic tests only; no GLOBAL obligations executed','mutants':results,
            'all_killed':all(r['status']=='KILLED' for r in results)}
    path=run/'mutation-results.json';write_new(path,(json.dumps(report,indent=1)+'\n').encode())
    print('result',path,'killed',sum(r['status']=='KILLED' for r in results),'of',len(results),flush=True)
    return 0 if report['all_killed'] else 1
if __name__=='__main__':sys.exit(main())
