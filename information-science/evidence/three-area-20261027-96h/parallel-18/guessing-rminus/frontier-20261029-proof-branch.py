#!/usr/bin/env python3
"""Replace a conditional DFZ instance by the full copy program of its proof.

Usage: python3 script.py OUT.json CENTRAL.json CENTRAL_SHA INSTANCES.json [EXTRA.json]
INSTANCES.json: {"instances": [{"coefficients": [...], "A": mask, "B": mask,
"C": mask, "D": mask, "Z": mask}]} with masks over the ten originals.
For each instance, the copy steps listed with its coefficient tuple in the
pinned DFZ TeX are executed on the originals: role letters a,b,c,d stand for
the tuples X_A,...,X_D; every copy is an atomic variable copying the stated
tuple(s) over the stated roles together with the conditioning tuple X_Z, and
is conditionally independent of every previously existing variable given that
over-set. The branch carries every elemental Shannon inequality of its whole
variable set, every subset copy marginal equality (subsets of the individual
over-set variables) and every independence equality, so it implies the DFZ
instance and possibly more. Sequential copy lemma => valid. The model is the
current central program (v9 inputs: cuts and extra branches as recorded in
CENTRAL.json) plus these branches; solved by IPM without crossover.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,re,sys,time

ROOT=Path(__file__).resolve().parent
def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
cp=load('cp3','frontier-20261029-dfz-cutting-plane-v3.py');v5=load('cp5','frontier-20261029-dfz-cutting-plane-v5.py')
v6=load('cp6','frontier-20261029-copy-cutting-plane-v6.py');v8=load('cp8','frontier-20261029-central-cutting-plane-v8.py')
vf=load('vf','frontier-20261029-dfz-inequality-verify.py')

def copy_steps_of(coef):
    lines=(ROOT/cp.TEX).read_text().split('\n')
    s=next(i for i,l in enumerate(lines) if 'label{FourCopies}' in l);e=next(i for i,l in enumerate(lines) if 'label{infinite}' in l)
    for l in lines[s:e]:
        m=re.match(r'\s*\\item\s+((?:\d+\s+){9})(.*)',l)
        if m and tuple(int(x) for x in m.group(1).split())==tuple(coef):return m.group(2).strip()
    if tuple(coef)==(1,2,1,1,1,0,0,1,0):return 'r c ab.'
    raise ValueError(('NO_STEPS',coef))

def add_proof_branch(M,tag,inst):
    steps=vf.parse_steps(copy_steps_of(inst['coefficients']))
    roles={'a':inst['A'],'b':inst['B'],'c':inst['C'],'d':inst['D']};Z=inst['Z']
    names=[str(v) for v in range(10)];bit={}
    for new,items,over in steps:
        for x in new:bit[x]=len(names);names.append(x)
    n=len(names)
    def keyf(m):
        if m==0:return None
        return ('o',m) if m<1024 else (tag,m)
    def mask_of(letters):
        m=0
        for x in letters:m|=roles[x] if x in roles else 1<<bit[x]
        return m
    cp.add_shannon(M,names,keyf);existing=(1<<10)-1
    for new,items,over in steps:
        Y=mask_of(over)|Z;Nn=sum(1<<bit[x] for x in new)
        for q in range(1,1<<len(new)):
            nm=sum(1<<bit[new[k]] for k in range(len(new)) if q>>k&1);om=0
            for k in range(len(new)):
                if q>>k&1:om|=mask_of(items[k])
            U=Y
            while True:
                M.add([(keyf(U|nm),1),(keyf(U|om),-1)],0,0,('pcopy',tag,''.join(new),q,U))
                if not U:break
                U=(U-1)&Y
        M.add([(keyf(existing|Nn),1),(keyf(Y),1),(keyf(existing),-1),(keyf(Y|Nn),-1)],0,0,('pindependence',tag,''.join(new)))
        existing|=Nn
    return n

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    central=json.loads(raw);insts=json.loads((ROOT/sys.argv[4]).read_text())['instances']
    keys=sorted(cp.coefficients());M=cp.build('gurpinar-sym');extra=central['extra_single_copies']
    for k,(S,T) in enumerate(extra):v6.add_single_copy(M,k,S[0],T)
    seen=set()
    for c in central['cuts']:
        tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if key in seen:continue
        seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
    sizes=[add_proof_branch(M,f'p{i}',inst) for i,inst in enumerate(insts)]
    print('columns',len(M.col),'rows',len(M.rows),'proof branch sizes',sizes,flush=True)
    status,obj,x,dt=v8.solve_central(M)
    res={'central_sha256':sys.argv[3],'instances':insts,'proof_branch_sizes':sizes,'status':status,'objective_ipm':obj,'rows':len(M.rows),'solve_s':dt,
         'extra_single_copies':extra,'cuts':central['cuts'],'final_columns_float':{repr(k):float(x[j]) for k,j in M.col.items()},
         'limits':'Floating proposal; exact certificate required.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')
    print(status,obj,round(dt,1))

if __name__=='__main__':main()
