#!/usr/bin/env python3
"""Lazy source-certificate-core search with joint-copy entropy constraints.

Missing entropy coordinates are assigned zero for separation and introduced
only when a valid cut references them. Every bound remains an unverified float
until a separate exact dual certificate is checked.
"""
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy

spec=spec_from_file_location('cross','frontier-20261028-cross-copy-upper-search.py')
cross=module_from_spec(spec);spec.loader.exec_module(cross)
cert=cross.cert;base=cross.base
OUTPUT=ROOT/'frontier-20261028-cross-copy-lazy-result.json'
MAX_ROUNDS=12
SOLVE_SECONDS=20.0
MAX_WALL_SECONDS=110.0
MAX_CUTS_PER_ROUND=1200


def initial_rows(source):
    rows={}; inf=highspy.kHighsInf
    for terms,lo,hi,meta in cross.sparse.build_constraints(source,[]):
        cross.add_to(rows,[(cross.mask_for(labels),value) for labels,value in terms.items()],lo,hi,meta)
    for key in cert.copy_forms():
        if key and key[0][1]<0:continue
        cross.add_to(rows,[(cross.mask_for(labels),value) for labels,value in key],0,0,{'kind':'full-copy-equality'})
    return rows


def solve(rows):
    masks={m for (key,_,_) in rows for m,_ in key};masks.update(range(1,1024))
    masks=sorted(masks);col={m:i for i,m in enumerate(masks)}
    starts=[]; inds=[]; vals=[]; lo=[];hi=[];labels=[]
    for (key,l,u),meta in rows.items():
        starts.append(len(inds))
        for mask,value in key:inds.append(col[mask]);vals.append(float(value))
        lo.append(l);hi.append(u);labels.append((key,meta))
    n=len(masks);lower=np.zeros(n);upper=np.full(n,highspy.kHighsInf)
    for i in range(10):upper[col[1<<i]]=1.0
    objective=np.zeros(n);objective[col[1023]]=1.0
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=n,len(starts)
    lp.col_cost_,lp.col_lower_,lp.col_upper_=objective,lower,upper
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(inds,dtype=np.int32)
    lp.a_matrix_.value_=np.array(vals,dtype=float);lp.sense_=highspy.ObjSense.kMaximize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1)
    solver.setOptionValue('time_limit',SOLVE_SECONDS);solver.passModel(lp)
    t=time.monotonic();solver.run();elapsed=time.monotonic()-t
    status=solver.modelStatusToString(solver.getModelStatus());sol=solver.getSolution()
    result={'status':status,'objective_float_unverified':float(solver.getInfo().objective_function_value),
            'rows':len(starts),'columns':n,'nnz':len(inds),'solve_elapsed_s':elapsed}
    if status!='Optimal':return result,None
    result['nonzero_row_duals_float']=[{'meta':meta,'row':key,'dual':float(value)}
        for (key,meta),value in zip(labels,sol.row_dual) if abs(float(value))>1e-8]
    result['nonzero_col_duals_float']=[{'mask':masks[i],'dual':float(value)}
        for i,value in enumerate(sol.col_dual) if abs(float(value))>1e-8]
    h=np.zeros(1<<17)
    for m,i in col.items():h[m]=sol.col_value[i]
    return result,h


def shannon_violations(h,existing):
    inf=highspy.kHighsInf;violations={};checks=0
    def offer(terms,slack,meta):
        key=cross.compressed(terms)
        if key and (key,0,inf) not in existing:
            old=violations.get(key)
            if old is None or slack<old[0]:violations[key]=(float(slack),meta)
    for size in range(1,6):
        for subset in combinations(range(17),size):
            mask=sum(1<<i for i in subset)
            for i in subset:
                smaller=mask^(1<<i);slack=h[mask]-h[smaller];checks+=1
                if slack < -1e-8:
                    offer(((mask,1),(smaller,-1)),slack,{'kind':'lazy-conditional-entropy','mask':mask,'vertex':i})
    for i,j in combinations(range(17),2):
        other=[k for k in range(17) if k not in (i,j)]
        for zsize in range(4):
            for cond in combinations(other,zsize):
                z=sum(1<<k for k in cond);a,b=1<<i,1<<j
                slack=h[a|z]+h[b|z]-h[a|b|z]-h[z];checks+=1
                if slack < -1e-8:
                    offer(base.cmi(a,b,z),slack,{'kind':'lazy-CMI','i':i,'j':j,'z':z})
    return checks,violations


def main():
    start=time.monotonic();data={key:(ROOT/info[0]).read_bytes() for key,info in cert.FILES.items()}
    for key,(_,expected) in cert.FILES.items():cert.pin(key,data[key],expected)
    source=cert.parse_input(data['layout'],data['text']);rows=initial_rows(source);initial=len(rows)
    rounds=[];stop='round limit'
    for r in range(MAX_ROUNDS):
        if time.monotonic()-start>MAX_WALL_SECONDS:stop='wall limit before next round';break
        result,h=solve(rows);result['round']=r
        if h is None:
            result['stop']='LP not optimal';rounds.append(result);stop='LP not optimal';break
        t=time.monotonic();c1,sh=shannon_violations(h,rows);c2,non=cross.separate(h,rows)
        merged=dict(sh)
        for key,item in non.items():
            if key not in merged or item[0]<merged[key][0]:merged[key]=item
        chosen=sorted(merged.items(),key=lambda item:item[1][0])[:MAX_CUTS_PER_ROUND]
        result.update({'shannon_checks':c1,'shannon_violations':len(sh),
                       'copy_family_checks':c2,'copy_family_violations':len(non),
                       'minimum_slack_float':min((v[0] for v in merged.values()),default=0.0),
                       'scan_elapsed_s':time.monotonic()-t,'cuts_added':len(chosen)})
        for key,(value,meta) in chosen:rows[(key,0,highspy.kHighsInf)]=meta
        rounds.append(result)
        checkpoint=ROOT/f'frontier-20261028-cross-copy-lazy-round-{r}.json'
        with checkpoint.open('x',encoding='utf-8') as stream:
            json.dump({k:v for k,v in result.items() if not k.startswith('nonzero_')},stream,indent=2);stream.write('\n')
        if not chosen:stop='no violations in scanned family';break
    output={'source_pins':{k:v[1] for k,v in cert.FILES.items()},'initial_rows':initial,
            'symbols':cross.SYMBOLS,'max_rounds':MAX_ROUNDS,'wall_limit_checked_between_rounds_s':MAX_WALL_SECONDS,
            'solver_threads':1,'per_solve_time_limit_s':SOLVE_SECONDS,'stop':stop,'rounds':rounds,
            'total_elapsed_s':time.monotonic()-start,
            'limits':'All results are floating LP proposals; exact dual certification and independent mathematics review are mandatory. A restricted cut family is not a global impossibility result.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(output,stream,indent=2);stream.write('\n')
    print(json.dumps([{k:v for k,v in x.items() if not k.startswith('nonzero_')} for x in rounds],indent=2))
    print('initial_rows',initial,'stop',stop,'total_elapsed_s',output['total_elapsed_s'])


if __name__=='__main__':main()
