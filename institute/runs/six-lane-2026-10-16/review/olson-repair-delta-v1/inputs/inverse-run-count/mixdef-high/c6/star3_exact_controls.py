#!/usr/bin/env python3
"""[F] Exact-integer regression controls for seedXstar3.bounds; never reruns the known-broken old float implementation."""
import json,hashlib,time
G={'__name__':'star3lib'}
src=open('seedXstar3.py').read();guard="if __name__ == '__main__':\n    main()"
exec(compile(src.replace(guard,''),'seedXstar3.py','exec'),G)
t=time.time();count=0
for p in range(11,44):
    if not G['NS']['isprime'](p):continue
    for k,kap,B in G['NS']['classes'](p):
        E=2*p-2*k+2*kap;D=2*p-k-E
        for d in range(-min(B,E+1),E+2):
            LA2=D+E+3-max(d,-1);LB2=D+E+3+min(d,1)
            want=(1-(LA2+1)//2,(LB2+1)//2-1)
            got=G['bounds'](p,k,kap,B,d,0)
            if got!=want:raise RuntimeError(('closed form mismatch',p,k,kap,B,d,got,want))
            if G['bounds'](p,k,kap,B,d,3)!=(got[0]+1,got[1]-1):raise RuntimeError('tighten mode mismatch')
            count+=1
p=(1<<61)-1;D=(1<<60)+200;kap=p-D;k=p+kap
lo,hi=G['bounds'](p,k,kap,1,1,0)
if (1-lo,hi+1)!=((1<<59)+101,(1<<59)+102):raise RuntimeError('review large-integer case failed')
large={'p':str(p),'ceil_LA':str(1-lo),'ceil_LB':str(hi+1)}
for p in ((1<<89)-1,(1<<127)-1,(1<<521)-1):
    kap=p//3;E=2*((p//17)//2);k=p+kap-E//2;B=7;D=p-kap-E//2
    for d in (-7,-1,0,1,E+1):
        a=1-(D+E+3-max(d,-1)+1)//2;b=(D+E+3+min(d,1)+1)//2-1
        if G['bounds'](p,k,kap,B,d,0)!=(a,b):raise RuntimeError('large exact bound mismatch')
print(json.dumps({'source_sha256':{f:hashlib.sha256(open(f,'rb').read()).hexdigest() for f in ('star3_exact_controls.py','seedXstar3.py','seedX3.py')},
                  'small_domain_weights':count,'review_large_case':large,'large_bound_checks':15,'seconds':round(time.time()-t,2)}),flush=True)
