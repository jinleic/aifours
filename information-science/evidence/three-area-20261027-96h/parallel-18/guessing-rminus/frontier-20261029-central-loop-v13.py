#!/usr/bin/env python3
"""Driver: repeated central solves (with copy programs) and DFZ scans on chosen variable sets.

Usage: python3 script.py PREFIX ROUNDS TAGS PRELOAD.json PRELOAD_SHA EXTRA.json PROGRAMS.json PROGRAMS_SHA [CUTS.json CUTS_SHA ...]
TAGS: comma-separated variable-set tags to scan each round (e.g. o,b1,m2).
Round r: (1) frontier-20261029-central-solve-v12.py with the programs and all cut
files so far -> PREFIX-r-central.json; (2) frontier-20261029-branch-dfz-scan-v3.py
on every tag (parallel single-thread processes) -> PREFIX-r-scan-TAG.json;
(3) every nonempty scan file joins the cut-file list. Stops when no scan finds a
violated instance or when the IPM value moved by less than 1e-8 in a round.
Writes PREFIX-log.json. Proposals only; exact certification is separate.
"""
from hashlib import sha256
from pathlib import Path
import json,subprocess,sys,time,os

ROOT=Path(__file__).resolve().parent
ENV=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()

def main():
    prefix=sys.argv[1];rounds=int(sys.argv[2]);tags=sys.argv[3].split(',');pre=(sys.argv[4],sys.argv[5]);extra=sys.argv[6]
    progs=(sys.argv[7],sys.argv[8]);files=list(zip(sys.argv[9::2],sys.argv[10::2]));log=[];t0=time.monotonic();last=None
    for r in range(rounds):
        central=f'{prefix}-{r}-central.json'
        args=['python3','frontier-20261029-central-solve-v12.py',central,pre[0],pre[1],extra,progs[0],progs[1]]+[x for f in files for x in f]
        p=subprocess.run(args,cwd=ROOT,env=ENV,capture_output=True,text=True)
        if p.returncode:raise RuntimeError(p.stderr[-2000:])
        csha=sha(central);obj=json.loads((ROOT/central).read_text())['objective_ipm']
        moved=None if last is None else last-obj
        procs=[]
        for tag in tags:
            out=f'{prefix}-{r}-scan-{tag}.json'
            procs.append((tag,out,subprocess.Popen(['python3','frontier-20261029-branch-dfz-scan-v3.py',out,central,csha,tag],cwd=ROOT,env=ENV,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)))
        found={}
        for tag,out,pr in procs:
            so,se=pr.communicate()
            if pr.returncode:raise RuntimeError((tag,se[-2000:]))
            n=len(json.loads((ROOT/out).read_text())['cuts']);found[tag]=n
            if n:files.append((out,sha(out)))
        entry={'round':r,'central':central,'central_sha256':csha,'objective_ipm':obj,'moved_since_previous_round':moved,'new_cuts':found,'cut_files':len(files),'elapsed_s':round(time.monotonic()-t0,1)}
        log.append(entry);print(entry,flush=True)
        with open(ROOT/f'{prefix}-log.json','w',encoding='utf-8') as f:json.dump({'log':log,'cut_files':files,'programs':progs},f,indent=1)
        if not any(found.values()) or (moved is not None and moved<1e-8):break
        last=obj

if __name__=='__main__':main()
