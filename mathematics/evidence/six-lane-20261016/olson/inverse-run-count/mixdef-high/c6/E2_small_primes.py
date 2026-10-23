#!/usr/bin/env python3
"""[F] Explicit finite E=2 instantiations for primes below31, using the repaired exact X* criterion.
This is a finite class implication, NOT an avoider census. No map/IND* label code is executed or needed.
"""
import json,hashlib,subprocess,time,resource
G={'__name__':'seedXstar3lib'}
src=open('seedXstar3.py').read();guard="if __name__ == '__main__':\n    main()"
exec(compile(src.replace(guard,''),'seedXstar3.py','exec'),G)
print(json.dumps({'host_time':subprocess.check_output(['date','+%Y-%m-%dT%H:%M:%S%z'],text=True).strip(),
                  'source_sha256':{f:hashlib.sha256(open(f,'rb').read()).hexdigest() for f in ('E2_small_primes.py','seedXstar3.py','seedX3.py')}}),flush=True)
t0=time.time();stats={};fail=[]
for p in (7,11,13,17,19,23,29):
    cnt={}
    for k,kap,B in G['NS']['classes'](p):
        E=2*p-2*k+2*kap
        if E!=2:continue
        r=G['class_report'](p,k,kap,B,0)
        print(json.dumps({'class':[p,k,kap,B],**r}),flush=True)
        cnt[r['verdict']]=cnt.get(r['verdict'],0)+1
        if r['verdict']!='pass':fail.append([p,k,kap,B,r])
    stats[p]=cnt
print(json.dumps({'counts':stats,'nonpassing':fail,'seconds':round(time.time()-t0,2),'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
