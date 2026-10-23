"""Make the referee's limited sorted-path copy and replay every claim there.

The replay directory is hidden only to avoid recursively delivering the
copy itself. Its contents are copied from visible files under the exact
stated caps. No locally generated executable is used.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time


def visible_files(root):
    paths=[]
    for current,dirs,files in os.walk(root,followlinks=False):
        dirs[:]=[d for d in dirs if not d.startswith('.') and d!='__pycache__' and not (Path(current)/d).is_symlink()]
        for name in files:
            path=Path(current)/name
            if name.startswith('.') or path.is_symlink():
                continue
            paths.append(path)
    return sorted(paths,key=lambda p:p.relative_to(root).as_posix())


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--prepare-only',action='store_true')
    a=p.parse_args()
    root=Path.cwd()
    snapshot=root/'.delivery-replay'
    if snapshot.exists():
        shutil.rmtree(snapshot)
    snapshot.mkdir()
    copied=[]; skipped=[]; total=0
    for source in visible_files(root):
        name=source.relative_to(root).as_posix()
        size=source.stat().st_size
        reason=('file>5000000' if size>5000000 else 'file-count' if len(copied)>=2000 else
                'total-bytes' if total+size>50000000 else None)
        if reason:
            skipped.append({'path':name,'bytes':size,'reason':reason})
            continue
        target=snapshot/name
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
        copied.append({'path':name,'bytes':size,'sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
        total+=size
    claims=json.loads((snapshot/'claims.json').read_text())
    evidence={name for c in claims['claims'] for name in c['evidence']}
    assert all((snapshot/name).is_file() for name in evidence),'load-bearing artifact skipped'
    assert all((snapshot/name).read_bytes()==(root/name).read_bytes() for name in evidence)
    manifest={'copied_files':len(copied),'copied_bytes':total,'max_copied_file_bytes':max(r['bytes'] for r in copied),
              'load_bearing_files':len(evidence),'all_load_bearing_files_copied':True,
              'skipped':skipped,'files':copied}
    Path('results/delivery-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    old_skips=Path('SKIPPED.json')
    historical=Path('historical/SKIPPED.json.epoch1')
    if old_skips.exists() and not historical.exists():
        historical.write_bytes(old_skips.read_bytes())
    old_skips.write_text(json.dumps(skipped,indent=2)+'\n')
    print('Limited copy:',len(copied),'files,',total,'bytes;',len(skipped),'skipped; all evidence present.',flush=True)
    if a.prepare_only:
        return
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',
             MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    started=time.monotonic()
    with open('logs/delivery-replay-driver.log','w') as log:
        process=subprocess.run(['python3','code/final_verify.py'],cwd=snapshot,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=1800)
    result_path=snapshot/'results/final-verification.json'
    if result_path.exists():
        result=json.loads(result_path.read_text())
    else:
        result={'status':'FAIL','commands':[]}
    result.update(snapshot_files=len(copied),snapshot_bytes=total,skipped=skipped,
                  outer_exit_code=process.returncode,outer_seconds=time.monotonic()-started,
                  all_load_bearing_files_copied=True,
                  command_timeout_seconds=300,aggregate_timeout_seconds=1800)
    Path('results/delivery-replay.json').write_text(json.dumps(result,indent=2)+'\n')
    # Preserve the exact observed command logs, including expected failures.
    for rec in result['commands']:
        path=Path(rec['log'])
        shutil.copyfile(snapshot/path,root/path)
    for name in ('claims-validation.json','final-verification.json'):
        if (snapshot/'results'/name).exists():
            shutil.copyfile(snapshot/'results'/name,root/'results'/name)
    assert process.returncode==0 and result['status']=='PASS',result
    assert result['claims_sha256']==hashlib.sha256(Path('claims.json').read_bytes()).hexdigest()
    assert all((snapshot/name).read_bytes()==(root/name).read_bytes() for name in evidence)
    print('PASS every claim command and intentional control in the limited copy;',round(result['seconds'],3),'seconds.',flush=True)


if __name__=='__main__':
    main()
