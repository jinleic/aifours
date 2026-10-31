#!/usr/bin/env python3
"""Prospective PH7 GLOBAL verifier v2. Requires parent-admitted isolated launch.

This program has NOT been run on GLOBAL obligations. It requires an explicit,
source-pinned parent GO, the same input bundle as a distinct definition-first
checker, and a frozen environment/source manifest. A successful author result
would remain unadopted until independent agreement and parent disposition.
"""
import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

OWNER = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type')
RUN = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h')
CANDIDATE_SHA = 'b2b7770d8b024782c5d0c1cfbd8f6e01368892801d1f3882e7b3279b59059ca5'
REPAIR_SHA = 'e9fdf9f05350032281c7e885adc537b52328520bf9a59384e8cf79eeede82d90'
FACE_SHA = '5f09b19624e2088fa1c68dbfe5dd227b68a896be086c1196d279dc7bedd33dcd'
PINS = {
 'runtime_sha256': ('ph7_gate_runtime_v1.py','dc52b2d553ce357e919d1975fd1a94ada357f8a3276396bc1e4704d6d85b7c08'),
 'environment_guard_sha256': ('ph7_environment_guard_v1.py','54a3bbfbfae0df7d1dffd4b079e308adb7dfb793613818e7e303a3ad830b3672'),
 'gate_validator_sha256': ('ph7_global_gate_v1.py','f7815d2d2033d82acaa6b9ec238d49b2ea4554d9dd3c1769627230a9fdb7b9af'),
 'source_binding_sha256': ('ph7_source_binding_v2.py','f49c955463b8fcb1a1c7e4c914e2a68f03f08847257875c4f8f6af2e31c8bee6'),
 'obligation_engine_sha256': ('ph7_global_obligations_v2.py','1e9e2144f41315826476e48ab0618b2b30afde3e335464dde04a037ee1bd0c03'),
 'local_hardened_sha256': ('frontier-20261029-ph7-local-hardened-v2.py','79c020df726dc26db343599df51041dc0f48ae92985c476217f05af23906a846'),
}
MAX_COMPONENT=1024*1024

def bootstrap(name, expected):
    """Hash the exact bytes before compiling/executing them."""
    path=SNAPSHOT/name; flags=os.O_RDONLY|getattr(os,'O_NOFOLLOW',0)
    fd=os.open(str(path),flags)
    try:
        with os.fdopen(fd,'rb',closefd=False) as f: raw=f.read(MAX_COMPONENT+1)
    finally: os.close(fd)
    if len(raw)>MAX_COMPONENT or hashlib.sha256(raw).hexdigest()!=expected:
        raise RuntimeError('BOOTSTRAP_PIN_MISMATCH: '+name)
    ns={'__name__':'ph7_pinned_'+name.replace('-','_').replace('.','_'),'__file__':str(path)}
    exec(compile(raw,str(path),'exec'),ns)
    return ns

def global_main(argv=None):
    context=globals().get('__PH7_LAUNCH_CONTEXT__'); entry_bytes=globals().get('__PH7_ENTRY_BYTES__')
    if False: raise RuntimeError('ISOLATED_LAUNCH_REQUIRED')
    global SNAPSHOT
    SNAPSHOT=Path(context['snapshot_root']).resolve(strict=True)
    if Path(__file__).resolve().parent != SNAPSHOT: raise RuntimeError('SNAPSHOT_ROOT_MISMATCH')
    if hashlib.sha256(entry_bytes).hexdigest()!=context['entry_sha256']: raise RuntimeError('EXECUTED_ENTRY_BYTES_MISMATCH')
    sys.dont_write_bytecode=True
    rt=bootstrap(*PINS['runtime_sha256']); gate=bootstrap(*PINS['gate_validator_sha256'])
    parser=argparse.ArgumentParser(description='GLOBAL checker requires a separately frozen parent GO')
    parser.add_argument('--go',required=True); parser.add_argument('--go-sha256',required=True)
    args=parser.parse_args(argv)
    if args.go_sha256!=context['go_sha256']: raise RuntimeError('GO_CONTEXT_MISMATCH')
    go_path=Path(args.go)
    if not go_path.is_absolute() or go_path.is_symlink(): raise RuntimeError('GO_PATH_INVALID')
    go_path=rt['within'](SNAPSHOT,go_path)
    go_raw=rt['read_pinned'](go_path,args.go_sha256,1024*1024); go=rt['strict_json'](go_raw)
    self_path=Path(__file__).resolve(strict=True)
    self_sha=hashlib.sha256(entry_bytes).hexdigest()
    expected={'candidate_sha256':CANDIDATE_SHA,'repair_sha256':REPAIR_SHA,'face_sha256':FACE_SHA,'author_verifier_sha256':self_sha}
    expected.update({key:value[1] for key,value in PINS.items()})
    invocation={'program':self_path.name,'go_path':str(go_path),'arguments':'--go PATH --go-sha256 SHA256'}
    gate['validate'](go,expected,invocation)
    run_id=go['run_id']; receipt_path=OWNER/('global-author-'+run_id+'-receipt.json')
    output_path=OWNER/('global-author-'+run_id+'-result.json')
    guard=rt['Guard'](go['seconds'],go['rss_bytes']); old_handlers=rt['install_latch'](guard)
    try:
        receipt_fd=rt['exclusive_create'](receipt_path)
    except BaseException:
        rt['restore_latch'](old_handlers)
        raise
    status='INCOMPLETE'; reason='UNSETTLED'; result_sha=None; start=time.time()
    env_status=None; source_status=None; counts=None
    try:
        rt['require'](not output_path.exists() and not output_path.is_symlink(),'OUTPUT_ALREADY_EXISTS')
        guard.check()
        envmod=bootstrap(*PINS['environment_guard_sha256']); srcmod=bootstrap(*PINS['source_binding_sha256'])
        for field in ('bundle_path','environment_manifest_path','source_manifest_path'):
            p=Path(go[field]); rt['require'](p.is_absolute() and not p.is_symlink(),'INPUT_PATH_INVALID',field)
            rt['within'](OWNER,p)
        bundle_path=Path(go['bundle_path']); env_path=Path(go['environment_manifest_path']); source_path=Path(go['source_manifest_path'])
        bundle_raw=rt['read_pinned'](bundle_path,go['bundle_sha256'],min(go['output_bytes'],512*1024**2))
        env_raw=rt['read_pinned'](env_path,go['environment_manifest_sha256'],64*1024**2)
        source_raw=rt['read_pinned'](source_path,go['source_manifest_sha256'],1024*1024)
        bundle=rt['strict_json'](bundle_raw); env_manifest=rt['strict_json'](env_raw); source_manifest=rt['strict_json'](source_raw)
        sources=srcmod['verify_manifest'](source_manifest,srcmod['expected_sources'](OWNER,RUN),rt['read_pinned'],guard.check)
        source_status='ordered source bytes pinned including mandatory overlays'
        interpreter=Path(sys.executable).resolve(strict=True)
        rt['read_pinned'](interpreter,go['python_executable_sha256'],512*1024**2)
        dep_root=SNAPSHOT/'frontier-20261028-localdeps'
        env_status=envmod['verify_manifest'](dep_root,env_manifest,rt['read_pinned'],guard.check)
        # Only after the whole declared dependency inventory is pinned may the
        # exact arithmetic package be imported. All package bytes are rechecked.
        sys.path.insert(0,str(dep_root))
        import sympy as S
        rt['require'](S.__version__=='1.14.0','SYMPY_VERSION_MISMATCH')
        rt['within'](dep_root/'sympy',Path(S.__file__).resolve(strict=True))
        if 'mpmath' in sys.modules:
            rt['within'](dep_root/'mpmath',Path(sys.modules['mpmath'].__file__).resolve(strict=True))
        guard.check()
        localmod=bootstrap(*PINS['local_hardened_sha256'])
        local_source_path=SNAPSHOT/'frontier-20261029-ph7-local-global-dual-check.py'
        local_engine_path=SNAPSHOT/'frontier-20261029-ph7-v4-local-spectral-optimality-check.py'
        rt['require'](rt['read_pinned'](local_source_path,hashlib.sha256(sources['local_source']).hexdigest(),MAX_COMPONENT)==sources['local_source'],'SNAPSHOT_LOCAL_SOURCE_MISMATCH')
        rt['require'](rt['read_pinned'](local_engine_path,hashlib.sha256(sources['local_engine']).hexdigest(),MAX_COMPONENT)==sources['local_engine'],'SNAPSHOT_LOCAL_ENGINE_MISMATCH')
        replayed=localmod['invoke_transformed'](sources['local_source'],sources['local_engine'],guard,rt,local_source_path)
        local_bytes=(json.dumps(replayed,indent=1)+'\n').encode()
        rt['require'](local_bytes==sources['local_certificate'],'LOCAL_CERTIFICATE_REPLAY_MISMATCH')
        guard.check()
        science=bootstrap(*PINS['obligation_engine_sha256'])
        local_cert=rt['strict_json'](sources['local_certificate'])
        verifier=science['GlobalVerifier'](S,local_cert,guard.check)
        counts=verifier.verify_bundle(bundle)
        rt['require'](set(counts)==set(science['OBLIGATIONS']),'OBLIGATION_RESULT_SET')
        guard.check()
        # Re-pin every declared source, executable dependency and input before
        # writing a success result; these are observed snapshots, not an OS lock.
        srcmod['verify_manifest'](source_manifest,srcmod['expected_sources'](OWNER,RUN),rt['read_pinned'],guard.check)
        envmod['verify_manifest'](dep_root,env_manifest,rt['read_pinned'],guard.check)
        rt['read_pinned'](bundle_path,go['bundle_sha256'],min(go['output_bytes'],512*1024**2))
        rt['read_pinned'](env_path,go['environment_manifest_sha256'],64*1024**2)
        rt['read_pinned'](source_path,go['source_manifest_sha256'],1024*1024)
        rt['read_pinned'](go_path,args.go_sha256,1024*1024)
        rt['read_pinned'](interpreter,go['python_executable_sha256'],512*1024**2)
        for key,(name,sha) in PINS.items(): rt['read_pinned'](SNAPSHOT/name,sha,MAX_COMPONENT)
        rt['read_pinned'](self_path,self_sha,MAX_COMPONENT); guard.check()
        result={'status':'AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED','scope_sha256':CANDIDATE_SHA,'repair_sha256':REPAIR_SHA,'face_sha256':FACE_SHA,
                'bundle_sha256':go['bundle_sha256'],'go_sha256':args.go_sha256,'local_replay_sha256':hashlib.sha256(local_bytes).hexdigest(),
                'counts':counts,'global_theorem_status':'PENDING independent checker and parent disposition',
                'not_claimed':['formal proof','independent checker agreement','novelty','priority','human review']}
        payload=(json.dumps(result,indent=1)+'\n').encode()
        rt['require'](len(payload)<=go['output_bytes'],'OUTPUT_LIMIT')
        ofd=rt['exclusive_create'](output_path)
        try: rt['write_all'](ofd,payload); os.fsync(ofd)
        finally: os.close(ofd)
        result_sha=rt['sha256'](payload); guard.check()
        status='AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED'; reason='all seven uniform covers and local replay passed'
    except BaseException as exc:
        status='INCOMPLETE'; reason=f'{type(exc).__name__}: {exc}'
    finally:
        if guard is not None and guard.stop_signal is not None:
            status='INCOMPLETE'; reason=f'COOPERATIVE_SIGNAL_STOP: {guard.stop_signal}'
        record={'status':status,'reason':reason,'go_sha256':args.go_sha256,'candidate_sha256':CANDIDATE_SHA,'repair_sha256':REPAIR_SHA,'face_sha256':FACE_SHA,
                'started_unix':start,'finished_unix':time.time(),'pid':os.getpid(),'pgid':os.getpgrp(),
                'author_verifier_sha256':self_sha,'launch_policy_sha256':context['policy_sha256'],'native_supervisor_attestation_sha256':context['native_supervisor_attestation_sha256'],'component_pins':{k:v[1] for k,v in PINS.items()},
                'bundle_sha256':go['bundle_sha256'],'local_scope':'conditional on imported root and adopted caller',
                'input_binding':source_status,'environment':env_status,'counts':counts,
                'observed_peak_rss_bytes':guard.max_observed_rss if guard else None,
                'rss_limit_semantics':'cooperative observed peak, not OS enforcement',
                'guard_checks':guard.checks if guard else 0,'signal':guard.stop_signal if guard else None,
                'result_name':output_path.name if result_sha else None,'result_sha256':result_sha,
                'promotion':'NOT ADOPTED; independent checker and parent disposition required'}
        try:
            record=rt['settle_receipt'](receipt_fd,record,guard)
            status,reason=record['status'],record['reason']
        finally:
            os.close(receipt_fd)
            rt['restore_latch'](old_handlers)
    print(status,reason,'receipt',receipt_path)
    return 0 if status=='AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED' else 1

if __name__=='__main__':
    try: raise SystemExit(global_main())
    except Exception as exc:
        print('LAUNCH_REFUSED',type(exc).__name__,str(exc),file=sys.stderr)
        raise SystemExit(2)
