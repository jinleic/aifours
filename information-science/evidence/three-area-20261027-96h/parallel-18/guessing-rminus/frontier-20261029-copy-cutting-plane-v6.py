#!/usr/bin/env python3
"""Symmetric publisher LP + extra single-copy branches + conditional DFZ cuts.

Usage: python3 script.py OUT.json EXTRA.json PRELOAD.json PRELOAD_SHA DFZ_ROUNDS
EXTRA.json: {"branches": [[S_one_based, T_one_based], ...]}; branch k adds the
11-variable set (a..j, s'k) where s'k copies the single original X_S over X_T
(copy marginal equalities for every subset of T, conditional independence of
s'k from all originals given X_T) with every elemental Shannon inequality.
The model is the v3 symmetric publisher LP (branches='gurpinar-sym') plus these
branches, preloaded DFZ cuts, and DFZ_ROUNDS rounds of original-variable DFZ
scanning. Each solve is cold (IPM with crossover). Proposals only; any bound is
claimed after an exact dual certificate and independent check.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
cp=load('cp3','frontier-20261029-dfz-cutting-plane-v3.py');v5=load('cp5','frontier-20261029-dfz-cutting-plane-v5.py')
L='abcdefghij'

def add_single_copy(M,k,S,T):
    tag=f'x{k}';aux=f"s'{k}";names=list(L)+[aux];pos={x:i for i,x in enumerate(names)}
    def keyf(m):
        if m==0:return None
        return ('o',m) if m<1024 else (tag,m)
    cp.add_shannon(M,names,keyf)
    Y=sum(1<<(t-1) for t in T);new=1<<10;old=1<<(S-1);U=Y
    while True:
        M.add([(keyf(U|new),1),(keyf(U|old),-1)],0,0,('xcopy',k,U))
        if not U:break
        U=(U-1)&Y
    M.add([(keyf(1023|new),1),(keyf(Y),1),(keyf(1023),-1),(keyf(Y|new),-1)],0,0,('xindependence',k))

def main():
    out=ROOT/sys.argv[1];extra=json.loads((ROOT/sys.argv[2]).read_text())['branches']
    raw=(ROOT/sys.argv[3]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[4]:raise ValueError('PRELOAD_HASH')
    rounds=int(sys.argv[5]);t0=time.monotonic();keys=sorted(cp.coefficients());M=cp.build('gurpinar-sym')
    for k,(S,T) in enumerate(extra):
        if len(S)!=1 or set(S)&set(T):raise ValueError('EXTRA_SPEC')
        add_single_copy(M,k,S[0],T)
    seen=set();cuts=[]
    for c in json.loads(raw)['cuts']:
        tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if key in seen:continue
        seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z']);cuts.append(dict(c,tag=tag))
    S0=v5.Scanner(keys,10)
    print('columns',len(M.col),'rows',len(M.rows),'extra branches',len(extra),'cuts',len(cuts),flush=True)
    h,status,obj,x,dt=cp.solve(M);log=[{'round':0,'status':status,'objective':obj,'rows':len(M.rows),'solve_s':round(dt,1)}];print(log[-1],flush=True)
    for rnd in range(1,rounds+1):
        cands=S0.scan(v5.profile(M,x,'o'));cands.sort();per={};chosen=[]
        for val,kk,A,B,C,D,Z in cands:
            key=('o',kk,A,B,C,D,Z)
            if key in seen or per.get(kk,0)>=30:continue
            seen.add(key);per[kk]=per.get(kk,0)+1;chosen.append((val,kk,A,B,C,D,Z))
            if len(chosen)>=300:break
        if not chosen:log.append({'round':rnd,'violations':0});print('no DFZ violations',flush=True);break
        for val,kk,A,B,C,D,Z in chosen:
            v5.add_cut(M,keys,'o',kk,A,B,C,D,Z);cuts.append({'tag':'o','coefficients':list(keys[kk]),'A':A,'B':B,'C':C,'D':D,'Z':Z,'violation_at_add':val})
        h,status,obj,x,dt=cp.solve(M)
        log.append({'round':rnd,'added':len(chosen),'status':status,'objective':obj,'rows':len(M.rows),'solve_s':round(dt,1),'elapsed_s':round(time.monotonic()-t0,1)});print(log[-1],flush=True)
    res={'branches':'gurpinar-sym','extra_single_copies':extra,'tex_sha256':cp.TEX_SHA,'log':log,'final_objective_float':obj,'cuts':cuts,
         'final_original_profile_float':[float(v) for v in v5.profile(M,x,'o')[1:]],
         'limits':'Floating proposal; exact certificate required.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')

if __name__=='__main__':main()
