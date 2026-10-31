#!/usr/bin/env python3
"""Driver: repeated central solves and parallel DFZ scans on all variable sets.

Usage: python3 script.py PREFIX ROUNDS PRELOAD.json PRELOAD_SHA EXTRA.json [CUTS.json CUTS_SHA ...]
Round r: (1) frontier-20261029-central-solve-v9.py on the symmetric publisher LP
with the extra single-copy branches and all cut files so far -> PREFIX-r-central.json;
(2) frontier-20261029-branch-dfz-scan-v2.py on tags o,b1,b2,b3 of that central
point, as four parallel single-thread processes -> PREFIX-r-scan-TAG.json;
(3) every nonempty scan file is appended to the cut-file list. Stops when no
scan finds a violated instance. Writes PREFIX-log.json. Proposals only.
"""
from hashlib import sha256
from pathlib import Path
import json,subprocess,sys,time,os

ROOT=Path(__file__).resolve().parent
ENV=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()

def main():
    prefix=sys.argv[1];rounds=int(sys.argv[2]);pre=(sys.argv[3],sys.argv[4]);extra=sys.argv[5]
    files=list(zip(sys.argv[6::2],sys.argv[7::2]));log=[];t0=time.monotonic()
    for r in range(rounds):
        central=f'{prefix}-{r}-central.json'
        args=['python3','frontier-20261029-central-solve-v9.py',central,pre[0],pre[1],extra]+[x for f in files for x in f]
        p=subprocess.run(args,cwd=ROOT,env=ENV,capture_output=True,text=True)
        if p.returncode:raise RuntimeError(p.stderr[-2000:])
        csha=sha(central);obj=json.loads((ROOT/central).read_text())['objective_ipm']
        procs=[]
        for tag in ('o','b1','b2','b3'):
            out=f'{prefix}-{r}-scan-{tag}.json'
            procs.append((tag,out,subprocess.Popen(['python3','frontier-20261029-branch-dfz-scan-v2.py',out,central,csha,tag],cwd=ROOT,env=ENV,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)))
        found={}
        for tag,out,pr in procs:
            so,se=pr.communicate()
            if pr.returncode:raise RuntimeError((tag,se[-2000:]))
            n=len(json.loads((ROOT/out).read_text())['cuts']);found[tag]=n
            if n:files.append((out,sha(out)))
        entry={'round':r,'central':central,'central_sha256':csha,'objective_ipm':obj,'new_cuts':found,'cut_files':len(files),'elapsed_s':round(time.monotonic()-t0,1)}
        log.append(entry);print(entry,flush=True)
        with open(ROOT/f'{prefix}-log.json','w',encoding='utf-8') as f:json.dump({'log':log,'cut_files':files},f,indent=1)
        if not any(found.values()):break

if __name__=='__main__':main()
