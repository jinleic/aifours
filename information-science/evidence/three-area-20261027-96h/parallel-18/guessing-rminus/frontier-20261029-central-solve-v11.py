#!/usr/bin/env python3
"""Central solve of the current model plus multi-step copy-program branches.

Usage: python3 script.py OUT.json PRELOAD.json PRELOAD_SHA EXTRA.json PROGRAMS.json PROGRAMS_SHA [CUTS.json CUTS_SHA ...]
Same model as frontier-20261029-central-solve-v9.py (symmetric publisher LP,
DFZ cuts of any tag, extra single-copy branches) plus one branch per program in
PROGRAMS.json (format of frontier-20261029-multistep-screen.py). A program
branch (tag m<k>) has the ten originals and its copy variables, every elemental
Shannon inequality of that whole set, every copy marginal equality and every
step independence equality (sequential copy lemma => valid for every almost
entropic profile). IPM without crossover; all columns exported.
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
ms=load('ms','frontier-20261029-multistep-screen.py')

def add_program(M,tag,prog):
    n,steps=ms.compile_program(prog);names=[str(v) for v in range(n)]
    def keyf(m):
        if m==0:return None
        return ('o',m) if m<1024 else (tag,m)
    cp.add_shannon(M,names,keyf)
    for si,(new,old,Y,E) in enumerate(steps):
        k=len(new);Nn=sum(1<<b for b in new)
        for q in range(1,1<<k):
            nm=sum(1<<new[a] for a in range(k) if q>>a&1);om=sum(1<<old[a] for a in range(k) if q>>a&1)
            U=Y
            while True:
                M.add([(keyf(U|nm),1),(keyf(U|om),-1)],0,0,('mcopy',tag,si,q,U))
                if not U:break
                U=(U-1)&Y
        M.add([(keyf(E|Nn),1),(keyf(Y),1),(keyf(E),-1),(keyf(Y|Nn),-1)],0,0,('mindependence',tag,si))
    return n

def main():
    out=ROOT/sys.argv[1];keys=sorted(cp.coefficients());M=cp.build('gurpinar-sym');t0=time.monotonic()
    extra=json.loads((ROOT/sys.argv[4]).read_text())['branches']
    for k,(S,T) in enumerate(extra):v6.add_single_copy(M,k,S[0],T)
    raw=(ROOT/sys.argv[5]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[6]:raise ValueError('PROGRAMS_HASH')
    progs=json.loads(raw)['programs']
    sizes=[add_program(M,f'm{i}',p) for i,p in enumerate(progs)]
    files=[(sys.argv[2],sys.argv[3])]+list(zip(sys.argv[7::2],sys.argv[8::2]))
    seen=set();cuts=[]
    for p,s in files:
        raw=(ROOT/p).read_bytes()
        if sha256(raw).hexdigest()!=s:raise ValueError(('HASH',p))
        for c in json.loads(raw)['cuts']:
            tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
            if key in seen:continue
            seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z']);cuts.append(dict(c,tag=tag))
    status,obj,x,dt=v8.solve_central(M)
    res={'branches':'gurpinar-sym','extra_single_copies':extra,'programs':progs,'program_sizes':sizes,'cuts':cuts,'status':status,
         'objective_ipm':obj,'rows':len(M.rows),'solve_s':dt,'final_columns_float':{repr(k):float(x[j]) for k,j in M.col.items()},
         'limits':'Central floating point of the optimal face; for separation only.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')
    print(status,obj,len(M.rows),round(time.monotonic()-t0,1))

if __name__=='__main__':main()
