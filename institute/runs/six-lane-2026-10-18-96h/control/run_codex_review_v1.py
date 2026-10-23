"""One scoped read-only Codex review, with exclusive output capture and owned SIGTERM settlement."""
import argparse, hashlib, json, os, re, signal, subprocess, time
from pathlib import Path
RUN=Path(__file__).resolve().parent.parent
REGISTRY=Path('/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json')
def clock():
    return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z'],text=True).strip()
def wx(path,value):
    with path.open('x') as f:
        json.dump(value,f,indent=2); f.write('\n'); f.flush(); os.fsync(f.fileno())
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('prompt'); ap.add_argument('--budget-seconds',type=int,default=2400); a=ap.parse_args()
    prompt=Path(a.prompt).resolve()
    if not prompt.is_relative_to(RUN) or not 60<=a.budget_seconds<=3600: raise SystemExit('Out-of-scope prompt or budget')
    base=prompt.with_suffix(''); paths={k:Path(str(base)+s) for k,s in [('stdout','.stdout.txt'),('stderr','.stderr.txt'),('launch','.launch.json'),('receipt','.receipt.json')]}
    if any(p.exists() for p in paths.values()): raise SystemExit('Refusing overwrite')
    cfg=json.loads(REGISTRY.read_text())['codex']
    cmd=['codex','exec','-m',cfg['model'],'-c','model_reasoning_effort='+cfg['effort'],'--sandbox','read-only','--ephemeral','--skip-git-repo-check','-C',str(RUN),prompt.read_text()]
    e=dict(os.environ,TMPDIR=str(RUN/'control/tmp'),TMP=str(RUN/'control/tmp'),TEMP=str(RUN/'control/tmp'),PYTHONDONTWRITEBYTECODE='1')
    t=time.monotonic(); r={'started_at':clock(),'requested_model':cfg['model'],'requested_effort':cfg['effort'],'prompt_sha256':hashlib.sha256(prompt.read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sandbox':'read-only','status':'NO_VERDICT','self_budget_seconds':a.budget_seconds}
    with paths['stdout'].open('x') as out,paths['stderr'].open('x') as err:
        p=subprocess.Popen(cmd,cwd=RUN,env=e,stdin=subprocess.DEVNULL,stdout=out,stderr=err,start_new_session=True)
        wx(paths['launch'],dict(r,pid=p.pid,pgid=os.getpgid(p.pid),cwd=str(RUN),argv_sha256=hashlib.sha256(json.dumps(cmd).encode()).hexdigest()))
        while p.poll() is None and time.monotonic()-t<a.budget_seconds: time.sleep(1)
        if p.poll() is None:
            r.update(status='SELF_BUDGET_SIGTERM_NO_VERDICT',stop_requested_at=clock()); os.killpg(p.pid,signal.SIGTERM); end=time.monotonic()+60
            while p.poll() is None and time.monotonic()<end: time.sleep(.2)
            if p.poll() is None: r['unsettled_pid']=p.pid
        r['returncode']=p.poll()
    r['reported_identity']=dict(re.findall(r'^(model|provider|sandbox|reasoning effort): (.+)$',paths['stderr'].read_text(errors='replace'),re.M))
    if r['returncode']==0 and 'stop_requested_at' not in r and paths['stdout'].stat().st_size:
        r['status']='REVIEW_RETURNED_UNVERIFIED'; r['review_stdout_sha256']=hashlib.sha256(paths['stdout'].read_bytes()).hexdigest()
    r.update(finished_at=clock(),duration_seconds=time.monotonic()-t); wx(paths['receipt'],r); print(json.dumps(r,indent=2),flush=True)
    return 0 if r['status']=='REVIEW_RETURNED_UNVERIFIED' else 1
if __name__=='__main__': raise SystemExit(main())
