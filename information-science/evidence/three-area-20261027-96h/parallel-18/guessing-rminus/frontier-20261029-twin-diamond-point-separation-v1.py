#!/usr/bin/env python3
"""Proposal-only Benders screen of ONE original numerical direction.
Usage: script.py OUT CONTRACT_SHA MODE POINT_JSON POINT_SHA MODEL_SHA LIMIT
No old affine-plane archive or checker is read/replayed. The numerical point
chooses a search direction, not an admitted entropy law or theorem premise.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,os,resource,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
MODEL='frontier-20261029-twin-diamond-copy-proposal-v1.py'
CONTRACT='frontier-20261029-twin-diamond-copy-proposal-contract-v1.json'

def pin(name,expected):
    raw=(ROOT/name).read_bytes()
    if sha256(raw).hexdigest()!=expected:raise ValueError(('INPUT_SHA',name))
    return raw

def main():
    start=time.monotonic();out=ROOT/sys.argv[1]
    if out.exists():raise FileExistsError('EXCLUSIVE_OUTPUT_ALREADY_EXISTS')
    contract=json.loads(pin(CONTRACT,sys.argv[2]));mode=sys.argv[3]
    point=json.loads(pin(sys.argv[4],sys.argv[5]));pin(MODEL,sys.argv[6]);limit=float(sys.argv[7])
    if mode not in contract['copy_modes'] or not 0<limit<=120:raise ValueError('BOUNDED_ARGUMENTS')
    sp=spec_from_file_location('fresh_twin_copy_model',ROOT/MODEL);m=module_from_spec(sp);sp.loader.exec_module(m);m.DEADLINE=start+240
    original={a:float(point['final_columns_float'][repr(('o',a))]) for a in range(1,1024)};original[0]=0.0
    copies=[{'old':c['old'],'over_mask':1023^m.vm(c['excluded']),'excluded':c['excluded']} for c in contract['copy_modes'][mode]]
    rep={'kind':'NUMERICAL_DIRECTION_SEPARATION_PROPOSAL_ONLY','state':'INCOMPLETE','clock_start':subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),'pid':os.getpid(),'pgid':os.getpgrp(),'argv':sys.argv,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'model_sha256':sys.argv[6],'contract_sha256':sys.argv[2],'point_sha256':sys.argv[5],'mode':mode,'threads':1,'solver_limit_s':limit,'internal_deadline_s':240,'requested_memory_MiB':4096,'OS_memory_enforcement_independently_tested':False,'not_established':['Exact separation inequality','Original point feasibility/realizability','Global entropy bound','Scientific acceptance/novelty','Any bulk-archive replay GO']}
    print(json.dumps({k:rep[k] for k in ('kind','pid','pgid','mode','point_sha256')}),flush=True)
    try:
        n,acts,keys,rows,lo,hi,names,rawcounts=m.build(copies);m.check_time();auxkeys=[a for a in keys if a>=1024];auxpos={a:i for i,a in enumerate(auxkeys)}
        core={};asym=0.0
        for a in keys:
            if a>=1024:continue
            orbit={m.move_original(a,tuple(i+1 for i in p[:10])) for p in acts};vals=[original[b] for b in sorted(orbit)];core[a]=sum(vals)/len(vals);asym=max(asym,max(vals)-min(vals))
        nx=len(auxkeys);slack=nx;starts=[0];indices=[];values=[];bounds=[];origins=[];original_residual=0.0
        for r,data in enumerate(rows):
            if names[r][0]=='singleton-cap':continue
            signs=(1,-1) if lo[r]==hi[r]==0 else (1,)
            if signs==(1,) and not (lo[r]==0 and hi[r]==m.INF):raise ValueError('HOMOGENEOUS_SOURCE_ROW')
            constant=sum(c*core[keys[j]] for j,c in data.items() if keys[j]<1024)
            hasaux=any(keys[j]>=1024 for j in data)
            if not hasaux:original_residual=max(original_residual,abs(constant) if len(signs)==2 else max(0.0,-constant))
            for sign in signs:
                for j,c in data.items():
                    key=keys[j]
                    if key>=1024:indices.append(auxpos[key]);values.append(sign*c)
                indices.append(slack);values.append(1);starts.append(len(indices));bounds.append(-sign*constant);origins.append((r,sign))
        lp=m.HS.HighsLp();lp.num_col_=nx+1;lp.num_row_=len(bounds);cost=np.zeros(nx+1);cost[slack]=1;lp.col_cost_=cost
        lower=np.full(nx+1,-m.INF);lower[slack]=0;lp.col_lower_=lower;lp.col_upper_=np.full(nx+1,m.INF);lp.row_lower_=np.asarray(bounds,dtype=float);lp.row_upper_=np.full(len(bounds),m.INF)
        lp.a_matrix_.format_=m.HS.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.asarray(starts,dtype=np.int32);lp.a_matrix_.index_=np.asarray(indices,dtype=np.int32);lp.a_matrix_.value_=np.asarray(values,dtype=float)
        h=m.HS.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',min(limit,max(0.1,m.DEADLINE-time.monotonic())));h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on');h.passModel(lp);h.run();m.check_time();status=h.modelStatusToString(h.getModelStatus())
        rep.update(status_float=status,joint_variables=n,raw_joint_CMI_rows=rawcounts['cmi'],source_unique_rows=len(rows),auxiliary_coordinates=nx,soft_constraint_rows=len(bounds),group_actions=acts,max_original_point_asymmetry_float=asym,original_only_row_residual_float=original_residual,core_direction_averaged_float={str(a):v for a,v in core.items()},symmetry_averaging_explicit=True)
        if status=='Optimal':
            sol=h.getSolution();gap=h.getObjectiveValue();rep['minimum_uniform_slack_float']=gap;rep['state']='NUMERICAL_SEPARATION_CANDIDATE_NEEDS_EXACT_DUAL' if gap>1e-7 else 'NUMERICAL_EXTENSION_ONLY_NOT_AN_EXACT_WITNESS';rep['row_dual_float']=sol.row_dual;rep['constraint_origins']=origins;rep['auxiliary_primal_float']=sol.col_value;rep['auxiliary_keys']=auxkeys
            # Proposal diagnostics only: no rational reconstruction or proof.
            cut={};max_aux_residual=np.zeros(nx)
            for lam,(r,sign) in zip(sol.row_dual,origins):
                if abs(lam)<1e-12:continue
                for j,c in rows[r].items():
                    key=keys[j]
                    if key<1024:cut[key]=cut.get(key,0.0)+lam*sign*c
                    else:max_aux_residual[auxpos[key]]+=lam*sign*c
            rep['cut_original_canonical_float']={str(a):v for a,v in cut.items() if abs(v)>1e-12};rep['cut_value_at_direction_float']=sum(c*core[a] for a,c in cut.items());rep['max_auxiliary_cancellation_residual_float']=float(np.max(np.abs(max_aux_residual))) if nx else 0.0
        else:rep['state']='NUMERICAL_UNKNOWN_NO_CUT'
    except Exception as exc:rep['state']='INCOMPLETE';rep['error_type']=type(exc).__name__;rep['error']=str(exc)
    rep['clock_finish']=subprocess.check_output(['/bin/date'],text=True).rstrip('\n');rep['elapsed_s']=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rep['peak_RSS_bytes_if_darwin']=rss if sys.platform=='darwin' else None
    with out.open('x') as f:json.dump(rep,f);f.write('\n')
    omit={'row_dual_float','constraint_origins','auxiliary_primal_float','auxiliary_keys','core_direction_averaged_float','cut_original_canonical_float','group_actions'}
    print(json.dumps({k:v for k,v in rep.items() if k not in omit},indent=1),flush=True)
if __name__=='__main__':main()
