#!/usr/bin/env python3
"""Bounded batch search for good visibility sets on covering binary planes.

Floating LP proposals only. Each good result records the visibility rows its
dual actually uses; exact certificates must be reconstructed and checked.
Usage: python3 script.py OUT.json [PRIOR.json ...]
"""
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
from time import monotonic
import json,sys

ROOT=Path(__file__).resolve().parent
spec=spec_from_file_location('vis',ROOT/'frontier-20261028-visibility-set-stable-lp.py');vis=module_from_spec(spec);spec.loader.exec_module(vis)
TRI=vis.TRI;P=vis.P

def bits(vs):return sum(1<<(v-1) for v in vs)
def img(W,p):return sum(1<<(p[v]-1) for v in range(10) if W>>v&1)

def main():
    out=ROOT/sys.argv[1];prior=[json.loads((ROOT/x).read_text()) for x in sys.argv[2:]]
    good={bits((6,7)),bits((1,5,7,8,9))};bad=set();records=[]
    for doc in prior:
        for r in doc['records']:
            if r['status']=='good':good.add(bits(r['used']))
            elif r['status']=='bad':bad.add(bits(r['W']))
            records.append(r)
    good={img(g,p) for g in good for p in P};bad={img(b,p) for b in bad for p in P}
    inc=[sum(1<<t for t,T in enumerate(TRI) if v in T) for v in range(1,11)];classes={}
    for a in range(1,1024):
        for b in range(a+1,1024):
            c=a^b
            if b>=c:continue
            J=a|b|c
            if set().union(*(set(TRI[t]) for t in range(10) if J>>t&1))!=set(range(1,11)):continue
            W=sum(1<<v for v in range(10) if a&inc[v] and b&inc[v] and c&inc[v])
            key=min(img(W,p) for p in P);classes[key]=classes.get(key,0)+1
    start=monotonic();done={bits(r['W']) for r in records if r['status']!='unknown'}
    order=sorted(classes,key=lambda W:(-bin(W).count('1'),-classes[W]))
    for W in order:
        if monotonic()-start>95:break
        if W in done or any(W&g==g for g in good) or any(W|bb==bb for bb in bad):continue
        Wset={v+1 for v in range(10) if W>>v&1};stab=[p for p in P if {p[v-1] for v in Wset}==Wset]
        r=vis.solve(Wset,stab,limit=40.0);rec={'W':sorted(Wset),'planes':classes[W],'group_size':len(stab),'solver':r['status_float_unverified']}
        if r['status_float_unverified']=='Optimal' and abs(r['objective_float_unverified'])<1e-7:
            used={x['name'][1] for x in r['dual_support'] if x['name'][0]=='syndrome-neighborhood'}
            used={p[v-1] for v in used for p in stab};rec.update(status='good',used=sorted(used))
            good|={img(bits(used),p) for p in P}
        elif r['status_float_unverified']=='Unbounded':
            rec['status']='bad';bad|={img(W,p) for p in P}
        else:rec['status']='unknown'
        records.append(rec);done.add(W);print(json.dumps(rec),flush=True)
    remaining=sum(n for W,n in classes.items() if not any(W&g==g for g in good))
    res={'records':records,'remaining_covering_planes_without_good_set':remaining,'elapsed_seconds':monotonic()-start,
         'limits':'Floating LP proposals; used-visibility sets come from numerical duals and require exact certificates.'}
    with out.open('x',encoding='utf-8') as f:json.dump(res,f,indent=2);f.write('\n')
    print(json.dumps({'records':len(records),'remaining':remaining}),flush=True)


if __name__=='__main__':main()
