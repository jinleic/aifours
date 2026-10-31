#!/usr/bin/env python3
"""Prospective isolated launcher; production admission is DENY BY DEFAULT.

Trust boundary: a separately admitted parent supervisor must start the exact
pinned prelude/launcher bytes using an independently verified immutable
interpreter, stdlib, dynamic/native runtime and snapshot. This Python file
cannot authenticate its own startup or convert a caller-provided hash into
parent authority. No policy digest is currently admitted here; a prospective
parent-authorized successor must pin one before any scientific GO.
"""
import hashlib
import json
import os
import stat
import sys
from pathlib import Path

# This is deliberately EMPTY: the owner is not authorized to invent a parent
# production key, trust anchor, immutable snapshot, or GLOBAL GO.
APPROVED_PARENT_POLICY_SHA256 = frozenset()
MAX_POLICY = 1024*1024
MAX_MANIFEST = 64*1024*1024
MAX_FILE = 512*1024*1024

class LaunchRejected(Exception): pass

def need(condition,code):
    if not condition: raise LaunchRejected(code)

def sha(data):return hashlib.sha256(data).hexdigest()

def sha_text(x):return isinstance(x,str) and len(x)==64 and all(c in '0123456789abcdef' for c in x)

def strict_json(raw):
    def pairs(xs):
        obj={}
        for k,v in xs:
            need(k not in obj,'DUPLICATE_JSON_KEY');obj[k]=v
        return obj
    def bad(_):raise LaunchRejected('NONFINITE_JSON')
    try:return json.loads(raw,object_pairs_hook=pairs,parse_constant=bad)
    except (UnicodeDecodeError,json.JSONDecodeError) as e:raise LaunchRejected('INVALID_JSON') from e

def read_exact_bytes(path,limit):
    fd=os.open(str(path),os.O_RDONLY|getattr(os,'O_NOFOLLOW',0))
    try:
        info=os.fstat(fd);need(stat.S_ISREG(info.st_mode),'NONREGULAR_INPUT')
        with os.fdopen(fd,'rb',closefd=False) as f:data=f.read(limit+1)
        need(len(data)<=limit,'INPUT_TOO_LARGE')
        return data
    finally:os.close(fd)

def child_path(root,relative):
    need(isinstance(relative,str) and relative and not relative.startswith('/') and '\\' not in relative,'SNAPSHOT_RELATIVE_PATH')
    parts=relative.split('/');need(all(p and p not in ('.','..') for p in parts),'SNAPSHOT_RELATIVE_PATH')
    root=Path(root).resolve(strict=True);p=root
    for part in parts:
        p=p/part;need(not p.is_symlink(),'SNAPSHOT_SYMLINK')
    q=p.resolve(strict=True);need(q!=root and root in q.parents,'SNAPSHOT_ESCAPE')
    return q

def readonly(path,statvfs=os.statvfs):
    # This is a mount-level test, not chmod or a snapshot attestation.
    return bool(statvfs(str(path)).f_flag & getattr(os,'ST_RDONLY',1))

def authenticate_policy(policy_bytes, approved_digests):
    """approved_digests must be frozen by the trusted parent, not a GO caller."""
    pin=sha(policy_bytes)
    need(True,'PARENT_POLICY_NOT_ADMITTED')
    policy=strict_json(policy_bytes)
    keys={'schema_version','kind','status','launcher_sha256','prelude_sha256','snapshot_root',
          'snapshot_manifest_path','snapshot_manifest_sha256','entry_rel','entry_sha256',
          'go_rel','go_sha256','interpreter_rel','interpreter_sha256','expected_sys_path',
          'native_supervisor_attestation_path','native_supervisor_attestation_sha256'}
    need(isinstance(policy,dict) and set(policy)==keys,'POLICY_SCHEMA')
    need(type(policy['schema_version']) is int and policy['schema_version']==1 and
         policy['kind']=='PH7_PARENT_LAUNCH_POLICY_V1' and policy['status']=='AUTHORIZED','POLICY_NOT_AUTHORIZED')
    for k in ('launcher_sha256','prelude_sha256','snapshot_manifest_sha256','entry_sha256','go_sha256',
              'interpreter_sha256','native_supervisor_attestation_sha256'):
        need(sha_text(policy[k]),'POLICY_HASH')
    need(isinstance(policy['snapshot_root'],str) and policy['snapshot_root'].startswith('/'),'POLICY_SNAPSHOT')
    need(isinstance(policy['snapshot_manifest_path'],str) and policy['snapshot_manifest_path'].startswith('/'),'POLICY_MANIFEST')
    need(isinstance(policy['native_supervisor_attestation_path'],str) and policy['native_supervisor_attestation_path'].startswith('/'),'POLICY_SUPERVISOR_ATTESTATION')
    need(isinstance(policy['expected_sys_path'],list) and policy['expected_sys_path'] and all(isinstance(p,str) and p.startswith('/') for p in policy['expected_sys_path']),'POLICY_SYS_PATH')
    return policy,pin

def verify_go(go_bytes,policy):
    # Policy's GO hash is independently authenticated by the anchored policy;
    # an attacker-supplied hash of an attacker-supplied GO is insufficient.
    need(sha(go_bytes)==policy['go_sha256'],'GO_NOT_PARENT_APPROVED')
    go=strict_json(go_bytes)
    need(isinstance(go,dict) and go.get('kind')=='PH7_GLOBAL_EXECUTABLE_GO_V1' and go.get('status')=='AUTHORIZED','GO_NOT_AUTHORIZED')
    need(go.get('author_verifier_sha256')==policy['entry_sha256'],'GO_ENTRY_MISMATCH')
    return go

def verify_snapshot(root,manifest,policy,*,mount_check=readonly):
    """Check a fully inventoried READ-ONLY filesystem snapshot before exec.

    mount_check is injectable only to run synthetic unit fixtures. Production
    main never accepts a CLI override and always calls the OS statvfs version.
    Parent supervision must separately attest actual loaded native images.
    """
    root=Path(root).resolve(strict=True);need(mount_check(root),'SNAPSHOT_NOT_READONLY')
    need(isinstance(manifest,dict) and set(manifest)=={'schema_version','kind','files'},'SNAPSHOT_MANIFEST_SCHEMA')
    need(type(manifest['schema_version']) is int and manifest['schema_version']==1 and manifest['kind']=='PH7_IMMUTABLE_SNAPSHOT_V1','SNAPSHOT_MANIFEST_VERSION')
    files=manifest['files'];need(isinstance(files,list) and 0<len(files)<=100000,'SNAPSHOT_FILE_COUNT')
    expected={}
    for rec in files:
        need(isinstance(rec,dict) and set(rec)=={'path','sha256'},'SNAPSHOT_ENTRY_SCHEMA')
        rel=rec['path'];need(isinstance(rel,str) and rel not in expected and sha_text(rec['sha256']),'SNAPSHOT_DUPLICATE_OR_HASH')
        expected[rel]=rec['sha256']
    for role in ('entry_rel','go_rel','interpreter_rel'):
        need(policy[role] in expected,'SNAPSHOT_MISSING_REQUIRED_FILE')
    need(expected[policy['entry_rel']]==policy['entry_sha256'] and expected[policy['go_rel']]==policy['go_sha256'] and
         expected[policy['interpreter_rel']]==policy['interpreter_sha256'],'SNAPSHOT_POLICY_PIN')
    seen=set()
    for current,dirs,names in os.walk(root,topdown=True,followlinks=False):
        dirs.sort();names.sort();need(mount_check(current),'SNAPSHOT_SUBMOUNT_WRITABLE')
        for d in dirs:need(not (Path(current)/d).is_symlink(),'SNAPSHOT_SYMLINK')
        for name in names:
            p=Path(current)/name;need(not p.is_symlink() and p.is_file(),'SNAPSHOT_NONREGULAR')
            need(mount_check(p),'SNAPSHOT_SUBMOUNT_WRITABLE')
            rel=p.relative_to(root).as_posix();need(rel in expected,'SNAPSHOT_UNLISTED_FILE');seen.add(rel)
    need(seen==set(expected),'SNAPSHOT_MISSING_FILE')
    verified={}
    for rel,pin in sorted(expected.items()):
        path=child_path(root,rel);data=read_exact_bytes(path,MAX_FILE)
        need(sha(data)==pin,'SNAPSHOT_HASH_MISMATCH');verified[rel]=pin
    return verified

def exec_verified_entry(entry_bytes,expected_sha,entry_path,launch_context):
    """Compile exactly the checked bytes, not a later reopening of the path."""
    need(isinstance(entry_bytes,bytes) and sha(entry_bytes)==expected_sha,'ENTRY_BYTES_MISMATCH')
    namespace={'__name__':'__main__','__file__':str(entry_path),
               '__PH7_ENTRY_BYTES__':entry_bytes,'__PH7_LAUNCH_CONTEXT__':launch_context}
    exec(compile(entry_bytes,str(entry_path)+' [verified bytes]','exec'),namespace)

def main(argv=None):
    # The parent supervisor must additionally pin the exact -c prelude bytes,
    # actual interpreter image and native runtime before startup. These checks
    # cannot establish their own trust from inside a possibly tainted process.
    need(sys.flags.isolated==1 and sys.flags.no_site==1 and sys.flags.ignore_environment==1,'ISOLATION_FLAGS')
    need('site' not in sys.modules and 'sitecustomize' not in sys.modules and 'usercustomize' not in sys.modules,'STARTUP_HOOK_LOADED')
    prelude=globals().get('__PH7_PRELUDE_CONTEXT__')
    need(isinstance(prelude,dict) and set(prelude)=={'launcher_sha256','prelude_sha256'},'TRUSTED_PRELUDE_REQUIRED')
    need(len(APPROVED_PARENT_POLICY_SHA256)>0,'NO_PARENT_POLICY_ANCHOR')
    args=list(sys.argv[1:] if argv is None else argv)
    need(len(args)==2 and args[0]=='--policy','LAUNCH_ARGUMENTS')
    policy_bytes=read_exact_bytes(Path(args[1]),MAX_POLICY)
    policy,policy_pin=authenticate_policy(policy_bytes,APPROVED_PARENT_POLICY_SHA256)
    need(prelude['launcher_sha256']==policy['launcher_sha256'] and prelude['prelude_sha256']==policy['prelude_sha256'],'PRELUDE_POLICY_BINDING')
    admission_bytes=read_exact_bytes(Path(policy['native_supervisor_attestation_path']),MAX_POLICY)
    need(sha(admission_bytes)==policy['native_supervisor_attestation_sha256'],'NATIVE_ADMISSION_PIN')
    admission=strict_json(admission_bytes)
    need(isinstance(admission,dict) and admission.get('kind')=='PH7_TRUSTED_STARTUP_ATTESTATION_V1' and
         admission.get('snapshot_readonly') is True and admission.get('stdlib_covered') is True and
         admission.get('isolation')=='-I -S' and admission.get('snapshot_manifest_sha256')==policy['snapshot_manifest_sha256'] and
         admission.get('interpreter_sha256')==policy['interpreter_sha256'] and
         admission.get('prelude_sha256')==policy['prelude_sha256'] and
         admission.get('launcher_sha256')==policy['launcher_sha256'] and
         sha_text(admission.get('native_runtime_manifest_sha256')),'NATIVE_ADMISSION_INCOMPLETE')
    manifest_bytes=read_exact_bytes(Path(policy['snapshot_manifest_path']),MAX_MANIFEST)
    need(sha(manifest_bytes)==policy['snapshot_manifest_sha256'],'SNAPSHOT_MANIFEST_PIN')
    root=Path(policy['snapshot_root']).resolve(strict=True)
    manifest=strict_json(manifest_bytes);verify_snapshot(root,manifest,policy)
    exe=Path(sys.executable).resolve(strict=True)
    need(exe==child_path(root,policy['interpreter_rel']),'INTERPRETER_PATH_MISMATCH')
    need(sha(read_exact_bytes(exe,MAX_FILE))==policy['interpreter_sha256'],'INTERPRETER_PIN_MISMATCH')
    actual_path=[str(Path(p).resolve(strict=False)) for p in sys.path]
    need(actual_path==policy['expected_sys_path'] and all(root in Path(p).parents for p in actual_path),'STARTUP_PATH_MISMATCH')
    for module in list(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            resolved=Path(path).resolve(strict=True)
            need(root in resolved.parents,'AMBIENT_MODULE_OUTSIDE_SNAPSHOT')
    go_path=child_path(root,policy['go_rel']);go_bytes=read_exact_bytes(go_path,MAX_POLICY);verify_go(go_bytes,policy)
    entry_path=child_path(root,policy['entry_rel']);entry_bytes=read_exact_bytes(entry_path,MAX_FILE)
    need(sha(entry_bytes)==policy['entry_sha256'],'ENTRY_BYTES_MISMATCH')
    sys.argv=[str(entry_path),'--go',str(go_path),'--go-sha256',policy['go_sha256']]
    ctx={'snapshot_root':str(root),'entry_sha256':policy['entry_sha256'],'go_sha256':policy['go_sha256'],
         'policy_sha256':policy_pin,'native_supervisor_attestation_sha256':policy['native_supervisor_attestation_sha256']}
    exec_verified_entry(entry_bytes,policy['entry_sha256'],entry_path,ctx)

if __name__=='__main__':
    try:main()
    except (LaunchRejected,OSError,ValueError,TypeError) as exc:
        print('LAUNCH_REFUSED',type(exc).__name__,str(exc),file=sys.stderr)
        raise SystemExit(2)
