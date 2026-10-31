#!/usr/bin/env python3
"""One-protection synthetic f249 mutants; never execute GLOBAL obligations."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TEST='ph7_f249_synthetic_tests_v1.py'
MODULES=['ph7_isolated_launcher_v1.py','ph7_isolated_prelude_v1.py','ph7_terminal_consumer_v1.py',
         'ph7_global_obligations_v2.py','ph7_gate_runtime_v1.py','frontier-20261029-ph7-global-verifier-v2.py',TEST]
MUTANTS=[
 ('deny-default','ph7_isolated_launcher_v1.py','APPROVED_PARENT_POLICY_SHA256 = frozenset()',"APPROVED_PARENT_POLICY_SHA256 = frozenset({'0'*64})",'ParentAuthorityTests.test_current_production_policy_is_deny_by_default'),
 ('parent-policy-anchor','ph7_isolated_launcher_v1.py',"need(pin in approved_digests,'PARENT_POLICY_NOT_ADMITTED')","need(True,'PARENT_POLICY_NOT_ADMITTED')",'ParentAuthorityTests.test_fabricated_self_hashed_go_rejected'),
 ('authenticated-go-pin','ph7_isolated_launcher_v1.py',"need(sha(go_bytes)==policy['go_sha256'],'GO_NOT_PARENT_APPROVED')","need(True,'GO_NOT_PARENT_APPROVED')",'ParentAuthorityTests.test_fabricated_self_hashed_go_rejected'),
 ('writable-snapshot','ph7_isolated_launcher_v1.py',"need(mount_check(root),'SNAPSHOT_NOT_READONLY')","need(True,'SNAPSHOT_NOT_READONLY')",'ParentAuthorityTests.test_writable_snapshot_rejected'),
 ('unlisted-snapshot','ph7_isolated_launcher_v1.py',"need(rel in expected,'SNAPSHOT_UNLISTED_FILE')","need(True,'SNAPSHOT_UNLISTED_FILE')",'ParentAuthorityTests.test_unlisted_snapshot_file_rejected'),
 ('executed-entry-bytes','ph7_isolated_launcher_v1.py',"need(isinstance(entry_bytes,bytes) and sha(entry_bytes)==expected_sha,'ENTRY_BYTES_MISMATCH')","need(isinstance(entry_bytes,bytes),'ENTRY_BYTES_MISMATCH')",'ParentAuthorityTests.test_verified_entry_uses_loaded_bytes_not_later_path'),
 ('isolated-launch-flags','ph7_isolated_launcher_v1.py',"need(sys.flags.isolated==1 and sys.flags.no_site==1 and sys.flags.ignore_environment==1,'ISOLATION_FLAGS')","need(True,'ISOLATION_FLAGS')",'ParentAuthorityTests.test_nonisolated_launcher_refused'),
 ('prelude-launcher-pin','ph7_isolated_prelude_v1.py',"if len(raw)>1024*1024 or hashlib.sha256(raw).hexdigest()!=launcher_sha:","if False:",'ParentAuthorityTests.test_prelude_rejects_wrong_launcher_pin'),
 ('entry-requires-launch','frontier-20261029-ph7-global-verifier-v2.py',"if not isinstance(context,dict) or not isinstance(entry_bytes,bytes): raise RuntimeError('ISOLATED_LAUNCH_REQUIRED')","if False: raise RuntimeError('ISOLATED_LAUNCH_REQUIRED')",'ParentAuthorityTests.test_direct_v2_entry_requires_isolated_launch'),
 ('duplicate-leaf','ph7_global_obligations_v2.py',"require(not node, 'DUPLICATE_OR_PREFIX_PATH', path)","require(True, 'DUPLICATE_OR_PREFIX_PATH', path)",'PathAndExactnessTests.test_duplicate_leaf_separately_rejected'),
 ('prefix-conflict','ph7_global_obligations_v2.py',"if not condition:\n        raise ProofError(code, detail)","if not condition and code != 'PATH_PREFIX_CONFLICT':\n        raise ProofError(code, detail)",'PathAndExactnessTests.test_prefix_conflict_separately_rejected'),
 ('malformed-path','ph7_global_obligations_v2.py',"all(c in '01' for c in path)","True",'PathAndExactnessTests.test_malformed_leaf_path_type_and_alphabet'),
 ('float-tensor','ph7_global_obligations_v2.py',"require(all(type(v) is int for v in values), 'NONINTEGER_TENSOR_COEFFICIENT')","require(True, 'NONINTEGER_TENSOR_COEFFICIENT')",'PathAndExactnessTests.test_float_tensor_never_becomes_verdict'),
 ('float-polynomial','ph7_global_obligations_v2.py',"require(not expr.has(S.Float), 'FLOAT_POLYNOMIAL_FORBIDDEN')","require(True, 'FLOAT_POLYNOMIAL_FORBIDDEN')",'PathAndExactnessTests.test_float_polynomial_never_becomes_verdict'),
 ('float-bound','ph7_global_obligations_v2.py',"not isinstance(value, (float, bool)) and getattr(value, 'is_Float', False) is not True","True",'PathAndExactnessTests.test_float_bound_never_becomes_exact_rational'),
 ('incomplete-receipt','ph7_terminal_consumer_v1.py',"need(receipt.get('status')=='AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED','RECEIPT_NOT_COMPLETE')","need(True,'RECEIPT_NOT_COMPLETE')",'TerminalConsumerTests.test_incomplete_receipt_is_unknown_even_when_pinned'),
 ('orphan-unknown','ph7_terminal_consumer_v1.py',"return {'status':'UNKNOWN','reason':str(exc),'promotion':'NO'}","return {'status':'AUTHOR_COMPLETE_BOUND_NOT_ADOPTED','reason':str(exc),'promotion':'NO'}",'TerminalConsumerTests.test_orphan_result_is_unknown'),
 ('supervisor-anchor','ph7_terminal_consumer_v1.py',"need(isinstance(supervisor_bytes,bytes) and digest(supervisor_bytes)==trusted['supervisor_sha256'],'SUPERVISOR_PIN')","need(True,'SUPERVISOR_PIN')",'TerminalConsumerTests.test_fabricated_supervisor_self_hash_is_not_parent_pin'),
 ('terminal-exit','ph7_terminal_consumer_v1.py',"need(type(supervisor.get('exit_code')) is int and supervisor['exit_code']==0,'PROCESS_EXIT_NOT_ZERO')","need(True,'PROCESS_EXIT_NOT_ZERO')",'TerminalConsumerTests.test_nonzero_process_exit_is_unknown'),
 ('actual-os-signal','ph7_gate_runtime_v1.py',"if self.stop_signal is None:\n            self.stop_signal = signum","if False:\n            self.stop_signal = signum",'RealSignalTests.test_os_sigterm_yields_incomplete_receipt'),
]

def sha(b):return hashlib.sha256(b).hexdigest()
def put(p,data):
    with p.open('xb') as f:f.write(data)

def main():
    run=ROOT/'f249-mutation-shadows-v1'/str(os.getpid());run.mkdir(parents=True,exist_ok=False)
    originals={name:(ROOT/name).read_bytes() for name in MODULES};results=[]
    for name,file,old,new,test in MUTANTS:
        source=originals[file].decode()
        if source.count(old)!=1:raise RuntimeError(f'{name}: anchor count {source.count(old)}')
        changed=source.replace(old,new).encode()
        if changed==originals[file]:raise RuntimeError(f'{name}: no change')
        shadow=run/name;shadow.mkdir()
        for component,data in originals.items():put(shadow/component,changed if component==file else data)
        env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PH7_F249_TEST_MODULE_ROOT':str(shadow)}
        try:
            p=subprocess.run([sys.executable,'-O',str(shadow/TEST),test],env=env,capture_output=True,text=True,timeout=30)
            text=p.stdout+p.stderr;valid='Ran 1 test' in text and 'SyntaxError' not in text and 'ImportError' not in text
            status='KILLED' if valid and p.returncode==1 else ('SURVIVED' if valid and p.returncode==0 else 'INVALID')
            code=p.returncode
        except subprocess.TimeoutExpired as exc:text=str(exc);status='INVALID_TIMEOUT';code=None
        put(shadow/'test-output.txt',text.encode())
        results.append({'id':name,'file':file,'test':test,'old_sha256':sha(originals[file]),'mutant_sha256':sha(changed),'status':status,'exit_code':code})
        print(name,status,flush=True)
    report={'schema_version':1,'kind':'PH7_F249_SYNTHETIC_SINGLE_PROTECTION_MUTATIONS_V1',
            'scope':'synthetic only; no GLOBAL obligation executed','mutants':results,
            'all_killed':all(r['status']=='KILLED' for r in results)}
    out=run/'mutation-results.json';put(out,(json.dumps(report,indent=1)+'\n').encode())
    print('result',out,'killed',sum(r['status']=='KILLED' for r in results),'of',len(results),flush=True)
    return 0 if report['all_killed'] else 1
if __name__=='__main__':sys.exit(main())
