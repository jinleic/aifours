#!/usr/bin/env python3
"""Central-point cutting plane: separate the relative interior of the optimal face.

Usage: python3 script.py OUT.json PRELOAD.json PRELOAD_SHA MAX_ROUNDS [EXTRA.json]
Vertex solutions of a degenerate LP are easy to cut without lowering the
optimum. Here each round solves the current model by IPM WITHOUT crossover,
which returns a point in the relative interior of the optimal face, and then
screens that central original profile against (i) every conditional union DFZ
instance on the ten original variables and (ii) all 725 orbit representatives
of single-copy structures (as in frontier-20261029-copy-cutting-plane-v7.py).
All separators are added (DFZ rows; new 11-variable copy branches) and the model
is re-solved. Proposals only; final models are certified by an exact dual.
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
v6=load('cp6','frontier-20261029-copy-cutting-plane-v6.py');v7=load('cp7','frontier-20261029-copy-cutting-plane-v7.py')
INF=cp.INF

def solve_central(M):
    hs=cp.highspy;h=hs.Highs();h.silent();h.setOptionValue('threads',1)
    lp=hs.HighsLp();n=len(M.col);lp.num_col_=n;cost=np.zeros(n);cost[M.col[('o',1023)]]=-1.0
    lp.col_cost_=cost;lp.col_lower_=np.full(n,-INF);lp.col_upper_=np.full(n,INF)
    starts=[];ids=[];vals=[]
    for t in M.rows:
        starts.append(len(ids))
        for j,x in t.items():ids.append(j);vals.append(float(x))
    lp.num_row_=len(M.rows);lp.row_lower_=np.array(M.lo,dtype=float);lp.row_upper_=np.array(M.hi,dtype=float)
    lp.a_matrix_.format_=hs.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(vals,dtype=float)
    h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','off');h.passModel(lp)
    t=time.monotonic();h.run();status=h.modelStatusToString(h.getModelStatus())
    return status,-h.getInfo().objective_function_value,np.array(h.getSolution().col_value),time.monotonic()-t

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('PRELOAD_HASH')
    rounds=int(sys.argv[4]);extra=json.loads((ROOT/sys.argv[5]).read_text())['branches'] if len(sys.argv)>5 else []
    t0=time.monotonic();keys=sorted(cp.coefficients());M=cp.build('gurpinar-sym');G=v7.gs.group();reps=v7.gs.representatives(G,1)
    for k,(S,T) in enumerate(extra):v6.add_single_copy(M,k,S[0],T)
    have={(tuple(S),tuple(sorted(T))) for S,T in extra};seen=set();cuts=[]
    for c in json.loads(raw)['cuts']:
        tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if key in seen:continue
        seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z']);cuts.append(dict(c,tag=tag))
    S0=v5.Scanner(keys,10);log=[]
    for rnd in range(rounds+1):
        status,obj,x,dt=solve_central(M);H=v5.profile(M,x,'o')
        entry={'round':rnd,'status':status,'objective_ipm':obj,'rows':len(M.rows),'extra_branches':len(extra),'solve_s':round(dt,1)}
        if rnd==rounds:log.append(entry);print(entry,flush=True);break
        bad=[(S,T) for S,T in v7.screen(H,reps) if ((S[0]+1,),tuple(t+1 for t in T)) not in have]
        for S,T in bad:
            spec=[[S[0]+1],[t+1 for t in T]];v6.add_single_copy(M,len(extra),spec[0][0],spec[1]);extra.append(spec);have.add((tuple(spec[0]),tuple(spec[1])))
        cands=S0.scan(H);cands.sort();per={};chosen=[]
        for val,kk,A,B,C,D,Z in cands:
            key=('o',kk,A,B,C,D,Z)
            if key in seen or per.get(kk,0)>=30:continue
            seen.add(key);per[kk]=per.get(kk,0)+1;chosen.append((val,kk,A,B,C,D,Z))
            if len(chosen)>=300:break
        for val,kk,A,B,C,D,Z in chosen:
            v5.add_cut(M,keys,'o',kk,A,B,C,D,Z);cuts.append({'tag':'o','coefficients':list(keys[kk]),'A':A,'B':B,'C':C,'D':D,'Z':Z,'violation_at_add':val})
        entry.update({'new_copy_branches':[[[S[0]+1],[t+1 for t in T]] for S,T in bad],'new_dfz':len(chosen),'most_violated_dfz':chosen[0][0] if chosen else None,'elapsed_s':round(time.monotonic()-t0,1)})
        log.append(entry);print(entry,flush=True)
        if not bad and not chosen:break
    res={'branches':'gurpinar-sym','extra_single_copies':extra,'tex_sha256':cp.TEX_SHA,'log':log,'final_objective_ipm':obj,'cuts':cuts,
         'final_original_profile_float':[float(v) for v in H[1:]],'limits':'Floating proposal; exact certificate required.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')

if __name__=='__main__':main()
