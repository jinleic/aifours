#!/usr/bin/env python3
"""Copy the real delivery limits and replay every final command, Python only.
Hidden paths, symlinks, __pycache__, files >5,000,000 bytes, files after 2000,
and files exceeding a 50,000,000-byte total are omitted in sorted path order.
The temporary snapshot stays inside the work directory. No local executable
can be invoked: every declared command must start with python3.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import time


def snapshot(root):
    files=[]
    for base,dirs,names in os.walk('.'):
        dirs[:]=[d for d in dirs if not d.startswith('.') and d!='__pycache__' and not Path(base,d).is_symlink()]
        for name in names:
            if not name.startswith('.'):files.append(Path(base,name))
    used=0;copied=[];skipped=[]
    for p in sorted(files,key=lambda p:p.as_posix()):
        reason=None
        if p.is_symlink():reason='symlink'
        elif p.stat().st_size>5000000:reason='file-size'
        elif len(copied)>=2000:reason='file-count'
        elif used+p.stat().st_size>50000000:reason='total-size'
        if reason:skipped.append(dict(path=str(p),reason=reason));continue
        target=root/p;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
        used+=p.stat().st_size;copied.append(str(p))
    return dict(files=len(copied),bytes=used,copied=copied,skipped=skipped)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--package-only',action='store_true')
    parser.add_argument('--keep',action='store_true');args=parser.parse_args()
    root=Path('.delivery-epoch2');shutil.rmtree(root,ignore_errors=True);root.mkdir()
    package=snapshot(root)
    claims=json.loads((root/'claims.json').read_text())
    for c in claims['claims']:
        for file in c['evidence']:
            if not (root/file).is_file():raise ValueError('load-bearing file omitted: '+file)
    result=dict(package=package,commands=[],total_command_seconds=0,max_command_seconds=0)
    output=Path('evidence/epoch2/snapshot-replay.json')
    if args.package_only:
        Path('evidence/epoch2/package-check.json').write_text(json.dumps(package,indent=2)+'\n')
        print(json.dumps(dict(files=package['files'],bytes=package['bytes'],skipped=len(package['skipped']))));return
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
    for c in claims['claims']:
        for field in ('verify_command','check_command','control_command'):
            command=c[field]
            if not command:continue
            argv=shlex.split(command)
            if argv[0]!='python3':raise ValueError('non-Python claim command: '+command)
            remaining=1800-result['total_command_seconds']
            if remaining<=0:raise TimeoutError('total replay budget exhausted')
            begin=time.monotonic();run=subprocess.run(argv,cwd=root,env=env,capture_output=True,
                                                     text=True,timeout=min(295,remaining))
            duration=time.monotonic()-begin;negative=field=='control_command'
            passed=(run.returncode!=0 and 'CHECK FAILED:' in run.stderr) if negative else run.returncode==0
            row=dict(cid=c['cid'],field=field,command=command,returncode=run.returncode,
                     passed=passed,seconds=duration,stdout=run.stdout,stderr=run.stderr)
            result['commands'].append(row);result['total_command_seconds']+=duration
            result['max_command_seconds']=max(result['max_command_seconds'],duration)
            output.write_text(json.dumps(result,indent=2)+'\n')
            print(c['cid'],field,'PASS' if passed else 'FAIL','%.3fs'%duration,flush=True)
            if not passed:raise SystemExit(1)
    result['all_passed']=True;output.write_text(json.dumps(result,indent=2)+'\n')
    Path('evidence/epoch2/package-check.json').write_text(json.dumps(package,indent=2)+'\n')
    print('ALL PASSED: %.3fs total; %.3fs max'%(result['total_command_seconds'],result['max_command_seconds']),flush=True)
    if not args.keep:shutil.rmtree(root)


if __name__=='__main__':main()
