#!/usr/bin/env python3
"""Sequential immutable review-repair receipts. One scientific child at a time; native CPU/file-size caps; wall stop via SIGTERM.
No destructive timeout or SIGKILL. This driver does not execute the old floating implementation.
"""
import os,sys,subprocess,time,resource,json,hashlib
JOBS=[('X3p23',['seedX3.py','0','23','detail']),('star3mode0',['seedXstar3.py','0','31','detail']),
      ('star3mode1',['seedXstar3.py','1','23','detail']),('star3mode3',['seedXstar3.py','3','31','detail'])]
def clock():return subprocess.check_output(['date','+%Y-%m-%dT%H:%M:%S%z'],text=True).strip()
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(1800,1860))
    resource.setrlimit(resource.RLIMIT_FSIZE,(128*1024**2,128*1024**2))
def main():
    receipts=[]
    for name,args in JOBS:
        sv=os.statvfs('.');free=sv.f_bavail*sv.f_frsize
        if free<12_000_000_000:raise RuntimeError('global disk floor reached')
        start=clock();cmd=[sys.executable,'-B',*args]
        with open('out/revision_'+name+'.txt','x') as fo,open('out/revision_'+name+'.err','x') as fe:
            p=subprocess.Popen(cmd,stdout=fo,stderr=fe,preexec_fn=limits)
            interrupted=False
            try:rc=p.wait(timeout=1800)
            except subprocess.TimeoutExpired:
                interrupted=True;p.terminate()
                try:rc=p.wait(timeout=30)
                except subprocess.TimeoutExpired:raise RuntimeError('UNKNOWN: SIGTERM did not finish; child remains running, no next job started')
        rec={'name':name,'argv':cmd,'start':start,'end':clock(),'exit':rc,'status':'UNKNOWN' if interrupted or rc!=0 else 'COMPLETED',
             'free_disk_bytes_at_start':free}
        receipts.append(rec);print(json.dumps(rec),flush=True)
        if interrupted or rc!=0:break
    result={'driver_sha256':hashlib.sha256(open('review_revision_runs.py','rb').read()).hexdigest(),'jobs':receipts,
            'peak_child_rss_bytes':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss}
    with open('out/review_revision_runs.json','x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
if __name__=='__main__':
    main()
