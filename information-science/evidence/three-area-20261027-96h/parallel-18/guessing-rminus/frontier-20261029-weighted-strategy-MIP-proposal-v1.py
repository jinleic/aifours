#!/usr/bin/env python3
"""Global binary strategy SEARCH for the established integer BL polynomial.
Usage: script.py OUT INTEGER_T0 INTEGER_T1 SECONDS
Every truth table is full-domain. For its actual winning set W and positive
integer t, put S=sum_W product_v t_v(w_v)^2, D=product_v(t_v(0)^3+t_v(1)^3)^2.
S^3>D would produce a POSSIBLE FULL-TARGET entropy witness, not acceptance:
freeze data and request parent gates; do not run an independent verifier here.
No fixed coordinate, fixed support size or local-neighborhood pool is imposed.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,math,os,resource,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
CORE='frontier-20261029-binary-slice-capacity-proposal-v1.py'
CORE_SHA='a6dad6aa6632409810d0e64e13b6fa01ff33c69ed96323598239608af56a37aa'
SEED='frontier-20261028-fd-law-search-precise-result.json'
SEED_SHA='c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc'

def main():
    start=time.monotonic();out=ROOT/sys.argv[1];t0,t1=int(sys.argv[2]),int(sys.argv[3]);limit=float(sys.argv[4])
    if out.exists():raise FileExistsError('EXCLUSIVE_OUTPUT_ALREADY_EXISTS')
    if not (1<=t0<=32 and 1<=t1<=32 and 0<limit<=120):raise ValueError('BOUNDED_ARGUMENTS')
    corebytes=(ROOT/CORE).read_bytes();seedbytes=(ROOT/SEED).read_bytes()
    if sha256(corebytes).hexdigest()!=CORE_SHA or sha256(seedbytes).hexdigest()!=SEED_SHA:raise ValueError('SOURCE_INPUT_SHA')
    sp=spec_from_file_location('binary_strategy_core',ROOT/CORE);c=module_from_spec(sp);sp.loader.exec_module(c);HS=c.HS;N=c.N
    weights=[t0**(2*(10-w.bit_count()))*t1**(2*w.bit_count()) for w in range(1024)];D=(t0**3+t1**3)**20
    seed=json.loads(seedbytes)['support_words_one_based_bitsets'];shift=max(range(1024),key=lambda a:sum(weights[w^a] for w in seed));seed=sorted(w^shift for w in seed)
    offsets={};total=1024
    for v in range(1,11):offsets[v]=total;total+=1<<len(N[v])
    tables={}
    for v in range(1,11):
        table=[None]*(1<<len(N[v]))
        for w in seed:
            k=c.projection(w,v);bit=(w>>(v-1))&1
            if table[k] is not None and table[k]!=bit:raise ValueError('SEED_FD_LOOKUP')
            table[k]=bit
        tables[v]=[0 if value is None else value for value in table]
    def winning(ts):return [w for w in range(1024) if all(((w>>(v-1))&1)==ts[v][c.projection(w,v)] for v in range(1,11))]
    initial_W=winning(tables);initial_S=sum(weights[w] for w in initial_W)
    rep={'kind':'FULL_TEN_WEIGHT_DIRECT_STRATEGY_PRODUCER_SEARCH_ONLY','source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'model_helper_sha256':CORE_SHA,'warm_source_sha256':SEED_SHA,'warm_translation':shift,'clock_start':subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),'pid':os.getpid(),'pgid':os.getpgrp(),'threads':1,'solver_limit_s':limit,'weights_t':[[t0,t1] for _ in range(10)],'N':N,'initial_winner_count':len(initial_W),'initial_integer_S':str(initial_S),'integer_D':str(D),'scope':'Search every binary full-domain strategy with this fixed positive product weight. Numerical status/bounds are not scientific results. Any integer-positive producer diagnostic is frozen for parent finite-witness verification; no acceptance checker or old archive replay is invoked.'}
    def save_actual(ts,status):
        W=winning(ts);S=sum(weights[w] for w in W);positive=S**3>D
        rep.update(strategy_tables=ts,winning_words=W,winning_count=len(W),integer_S=str(S),integer_cube_gap=str(S**3-D),positive_producer_diagnostic=positive,solver_status_float=status,state='POSSIBLE_FULL_TARGET_FINITE_CANDIDATE_PARENT_GATING_REQUIRED' if positive else 'NO_POSITIVE_PRODUCER_WITNESS_NOT_AN_IMPOSSIBILITY_RESULT')
        if positive:rep['candidate_rational_law']={'denominator':str(S),'aligned_word_numerators':[str(weights[w]) for w in W],'proof_lower_bound':'Delta>=log2(S^3/D)/3>0. Both actual FD validity and the entropy-to-guessing-number bridge require independent review.'}
    if initial_S**3>D:save_actual(tables,'NOT_RUN_INITIAL_CANDIDATE_FROZEN')
    else:
        starts=[0];ids=[];vals=[];lo=[];hi=[]
        def row(items,upper):
            for j,w in items:ids.append(j);vals.append(w)
            starts.append(len(ids));lo.append(-HS.kHighsInf);hi.append(upper)
        for w in range(1024):
            for v in range(1,11):
                y=offsets[v]+c.projection(w,v)
                row(((w,1),(y,-1)),0) if w>>(v-1)&1 else row(((w,1),(y,1)),1)
        nm=[c.vm(N[v]) for v in range(1,11)];indep=[I for I in range(1,1024) if all(not(I&nm[i]) for i in range(10) if I>>i&1)];maximal=[I for I in indep if not any(I!=J and I&J==I for J in indep)];cliques=0
        for I in maximal:
            for base in range(1024):
                if base&I:continue
                members=[];x=I
                while True:
                    members.append(base|x)
                    if not x:break
                    x=(x-1)&I
                row(((w,1) for w in members),1);cliques+=1
        lp=HS.HighsLp();lp.num_col_=total;lp.num_row_=len(lo);scale=max(weights);cost=np.zeros(total);cost[:1024]=[-w/scale for w in weights];lp.col_cost_=cost;lp.col_lower_=np.zeros(total);lp.col_upper_=np.ones(total);lp.integrality_=[HS.HighsVarType.kContinuous]*1024+[HS.HighsVarType.kInteger]*(total-1024)
        lp.row_lower_=np.asarray(lo);lp.row_upper_=np.asarray(hi);lp.a_matrix_.format_=HS.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.asarray(starts,dtype=np.int32);lp.a_matrix_.index_=np.asarray(ids,dtype=np.int32);lp.a_matrix_.value_=np.asarray(vals,dtype=float)
        init=np.zeros(total);init[initial_W]=1
        for v in range(1,11):init[offsets[v]:offsets[v]+len(tables[v])]=tables[v]
        h=HS.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit);h.setOptionValue('random_seed',20261029);h.passModel(lp);rep['warm_start_status']=str(h.setSolution(total,np.arange(total,dtype=np.int32),init));h.run();status=h.modelStatusToString(h.getModelStatus());sol=h.getSolution();rep.update(rows=len(lo),truth_table_bits=total-1024,clique_rows=cliques,solver_status_float=status,solver_objective_float=h.getObjectiveValue(),state='NO_STABLE_INTEGER_STRATEGY_INCUMBENT_NOT_A_NEGATIVE_RESULT')
        info=h.getInfo();rep['mip_nodes']=getattr(info,'mip_node_count',None)
        if sol.value_valid and len(sol.col_value)==total:
            err=max(abs(v-round(v)) for v in sol.col_value[1024:]);rep['truth_table_integrality_error_float']=err
            if err<1e-6 and all(round(v) in (0,1) for v in sol.col_value[1024:]):
                actual={v:[int(round(sol.col_value[offsets[v]+k])) for k in range(1<<len(N[v]))] for v in range(1,11)};save_actual(actual,status)
    rep['clock_finish']=subprocess.check_output(['/bin/date'],text=True).rstrip('\n');rep['elapsed_s']=time.monotonic()-start;rep['peak_RSS_bytes_if_darwin']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=='darwin' else None;rep['requested_taskpolicy_memory_MiB']=4096;rep['OS_memory_enforcement_independently_tested']=False
    with out.open('x') as f:json.dump(rep,f,indent=1);f.write('\n')
    print(json.dumps({k:v for k,v in rep.items() if k not in ('strategy_tables','winning_words','N','candidate_rational_law')},indent=1),flush=True)
if __name__=='__main__':main()
