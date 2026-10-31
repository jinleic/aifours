#!/usr/bin/env python3
"""Solve the current model once for a central optimal point and export all columns.

Usage: python3 script.py OUT.json PRELOAD.json PRELOAD_SHA [EXTRA.json [EXTRA_CUTS.json EXTRA_CUTS_SHA ...]]
Model: v3 symmetric publisher LP + preloaded DFZ cuts (any tag) + optional extra
single-copy branches + optional further cut files. IPM without crossover gives
a point in the relative interior of the optimal face; every column value is
written in the v5 result format ('final_columns_float') so that standalone
branch scans (frontier-20261029-branch-dfz-scan.py) can test it.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time

ROOT=Path(__file__).resolve().parent
def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
cp=load('cp3','frontier-20261029-dfz-cutting-plane-v3.py');v5=load('cp5','frontier-20261029-dfz-cutting-plane-v5.py')
v6=load('cp6','frontier-20261029-copy-cutting-plane-v6.py');v8=load('cp8','frontier-20261029-central-cutting-plane-v8.py')

def main():
    out=ROOT/sys.argv[1];keys=sorted(cp.coefficients());M=cp.build('gurpinar-sym');t0=time.monotonic()
    files=[(sys.argv[2],sys.argv[3])]+list(zip(sys.argv[5::2],sys.argv[6::2]))
    extra=json.loads((ROOT/sys.argv[4]).read_text())['branches'] if len(sys.argv)>4 else []
    for k,(S,T) in enumerate(extra):v6.add_single_copy(M,k,S[0],T)
    seen=set();cuts=[]
    for p,s in files:
        raw=(ROOT/p).read_bytes()
        if sha256(raw).hexdigest()!=s:raise ValueError(('HASH',p))
        for c in json.loads(raw)['cuts']:
            tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
            if key in seen:continue
            seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z']);cuts.append(dict(c,tag=tag))
    status,obj,x,dt=v8.solve_central(M)
    res={'branches':'gurpinar-sym','extra_single_copies':extra,'cuts':cuts,'status':status,'objective_ipm':obj,'rows':len(M.rows),'solve_s':dt,
         'final_columns_float':{repr(k):float(x[j]) for k,j in M.col.items()},
         'limits':'Central floating point of the optimal face; for separation only.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')
    print(status,obj,len(M.rows),round(time.monotonic()-t0,1))

if __name__=='__main__':main()
