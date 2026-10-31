#!/usr/bin/env python3
"""Cutting plane over single-copy branches and conditional DFZ cuts.

Usage: python3 script.py OUT.json PRELOAD.json PRELOAD_SHA MAX_ROUNDS [EXTRA.json]
Start: the v3 symmetric publisher LP, preloaded DFZ cuts and optional extra
single-copy branches. Each round: cold IPM solve; screen every one of the 725
automorphism-orbit representatives (S single original, T nonempty) of single
copy structures at the current floating original profile (LP feasibility of
the 11-variable copy extension, as in frontier-20261029-general-copy-screen-h1.py);
add each infeasible structure as a new branch; scan original-variable DFZ
instances and add violated ones. Stops when a round adds nothing. Proposals
only: the final model is certified separately by an exact dual.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
cp=load('cp3','frontier-20261029-dfz-cutting-plane-v3.py');v5=load('cp5','frontier-20261029-dfz-cutting-plane-v5.py')
v6=load('cp6','frontier-20261029-copy-cutting-plane-v6.py');gs=load('gs','frontier-20261029-general-copy-scan.py')

def screen(Hfloat,reps):
    base={m:Fraction(float(Hfloat[m])) for m in range(1,1024)};base[0]=Fraction(0)
    sh=gs.shannon_rows(base,1);bad=[]
    for S,T in reps:
        if quick_status(sh+gs.copy_rows(base,S,T),base)=='Infeasible':bad.append((S,T))
    return bad

def quick_status(rows,base):
    hs=gs.highspy;ncol=1024;starts=[];ids=[];vals=[];lo=[];hi=[]
    for full,eq,meta in rows:
        starts.append(len(ids));rhs=-sum((Fraction(c)*base[m] for m,c in full.items() if m<1024),Fraction())
        for m,c in full.items():
            if m>=1024:ids.append(m-1024);vals.append(float(c))
        r=float(rhs);lo.append(r);hi.append(r if eq else hs.kHighsInf)
    lp=hs.HighsLp();lp.num_col_=ncol;lp.num_row_=len(rows)
    lp.col_cost_=np.zeros(ncol);lp.col_lower_=np.full(ncol,-hs.kHighsInf);lp.col_upper_=np.full(ncol,hs.kHighsInf)
    lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi);lp.a_matrix_.format_=hs.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32)
    lp.a_matrix_.value_=np.array(vals,dtype=float)
    h=hs.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',12.0)
    h.passModel(lp);h.run();return h.modelStatusToString(h.getModelStatus())

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('PRELOAD_HASH')
    rounds=int(sys.argv[4]);extra=json.loads((ROOT/sys.argv[5]).read_text())['branches'] if len(sys.argv)>5 else []
    t0=time.monotonic();keys=sorted(cp.coefficients());M=cp.build('gurpinar-sym');G=gs.group();reps=gs.representatives(G,1)
    for k,(S,T) in enumerate(extra):v6.add_single_copy(M,k,S[0],T)
    have={(tuple(S),tuple(sorted(T))) for S,T in extra};seen=set();cuts=[]
    for c in json.loads(raw)['cuts']:
        tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if key in seen:continue
        seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z']);cuts.append(dict(c,tag=tag))
    S0=v5.Scanner(keys,10);log=[]
    for rnd in range(rounds+1):
        h,status,obj,x,dt=cp.solve(M);H=v5.profile(M,x,'o')
        entry={'round':rnd,'status':status,'objective':obj,'rows':len(M.rows),'branches_extra':len(extra),'solve_s':round(dt,1)}
        if rnd==rounds:log.append(entry);print(entry,flush=True);break
        bad=[(S,T) for S,T in screen(H,reps) if ((S[0]+1,),tuple(t+1 for t in T)) not in have]
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
        entry.update({'new_copy_branches':[[[S[0]+1],[t+1 for t in T]] for S,T in bad],'new_dfz':len(chosen),'elapsed_s':round(time.monotonic()-t0,1)})
        log.append(entry);print(entry,flush=True)
        if not bad and not chosen:break
    res={'branches':'gurpinar-sym','extra_single_copies':extra,'tex_sha256':cp.TEX_SHA,'log':log,'final_objective_float':obj,'cuts':cuts,
         'final_original_profile_float':[float(v) for v in H[1:]],'limits':'Floating proposal; exact certificate required.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')

if __name__=='__main__':main()
