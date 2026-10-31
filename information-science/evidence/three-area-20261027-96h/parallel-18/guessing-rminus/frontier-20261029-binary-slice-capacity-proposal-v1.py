#!/usr/bin/env python3
"""Direct finite-witness SEARCH only, not a verification/adoption assay.
Usage: script.py OUT BIASED_VERTEX SOLVER_SECONDS
If an actual binary FD support has slice sizes a,b at vertex v, give every
slice0 word rational weight a^2/(a^3+b^3), and slice1 word b^2/(a^3+b^3).
Then Delta >= (1/3)log2(a^3+b^3)-6. Thus a^3+b^3>64^3 would be a
POSSIBLE FULL-TARGET witness; freeze it for parent independent gates, never
promote it or launch additional acceptance checks here.
Search window: 1<=a,b<=64, oriented a>=b, and a selected subcode <=102 words.
1024 code-selection variables are continuous, but the384 local truth-table
bits are binary. An integral truth table defines a REAL full-domain strategy;
its complete winning set is recomputed, independently of selected x values.
"""
from itertools import combinations
from hashlib import sha256
from pathlib import Path
import json,math,os,resource,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy as HS
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
INF=HS.kHighsInf

def vm(vs):return sum(1<<(v-1) for v in vs)
def projection(w,v):return sum(((w>>(u-1))&1)<<j for j,u in enumerate(N[v]))

def main():
    start=time.monotonic();out=ROOT/sys.argv[1];biased=int(sys.argv[2]);limit=float(sys.argv[3])
    if out.exists():raise FileExistsError('EXCLUSIVE_OUTPUT_ALREADY_EXISTS')
    if biased not in N or not 0<limit<=120:raise ValueError('BOUNDED_ARGUMENTS')
    nm=[vm(N[v]) for v in range(1,11)];indep=[I for I in range(1,1024) if all(not(I&nm[i]) for i in range(10) if I>>i&1)];maximal=[I for I in indep if not any(I!=J and I&J==I for J in indep)]
    offsets={};pos=1024
    for v in range(1,11):offsets[v]=pos;pos+=1<<len(N[v])
    truth_end=pos;pairs=[]
    for a in range(51,65):
        b=0
        while a**3+b**3<=64**3:b+=1
        if b<=a:pairs.append((a,b))
    zstart=pos;pos+=len(pairs);tcol=pos;total=pos+1
    starts=[0];idx=[];vals=[];lo=[];hi=[]
    def row(items,l,u):
        for j,c in items:idx.append(j);vals.append(c)
        starts.append(len(idx));lo.append(l);hi.append(u)
    for w in range(1024):
        for v in range(1,11):
            y=offsets[v]+projection(w,v)
            if w>>(v-1)&1:row(((w,1),(y,-1)),-INF,0)
            else:row(((w,1),(y,1)),-INF,1)
    clique_rows=0
    for I in maximal:
        for base in range(1024):
            if base&I:continue
            members=[];u=I
            while True:
                members.append(base|u)
                if not u:break
                u=(u-1)&I
            row(((w,1) for w in members),-INF,1);clique_rows+=1
    zero=[w for w in range(1024) if not w>>(biased-1)&1];one=[w for w in range(1024) if w>>(biased-1)&1]
    row(((zstart+j,1) for j in range(len(pairs))),1,1)
    row([*[(w,1) for w in zero],(tcol,1),*[(zstart+j,-a) for j,(a,b) in enumerate(pairs)]],0,INF)
    row([*[(w,1) for w in one],(tcol,1),*[(zstart+j,-b) for j,(a,b) in enumerate(pairs)]],0,INF)
    row([*[(w,1) for w in zero],*[(w,-1) for w in one]],0,INF)
    row(((w,1) for w in zero),-INF,64);row(((w,1) for w in one),-INF,64);row(((w,1) for w in range(1024)),-INF,102)
    lp=HS.HighsLp();lp.num_col_=total;lp.num_row_=len(lo);cost=np.zeros(total);cost[tcol]=1;lp.col_cost_=cost
    lower=np.zeros(total);lower[0]=1;lp.col_lower_=lower;lp.col_upper_=np.ones(total);lp.integrality_=[HS.HighsVarType.kContinuous]*1024+[HS.HighsVarType.kInteger]*(total-1024)
    lp.row_lower_=np.asarray(lo);lp.row_upper_=np.asarray(hi);lp.a_matrix_.format_=HS.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.asarray(starts,dtype=np.int32);lp.a_matrix_.index_=np.asarray(idx,dtype=np.int32);lp.a_matrix_.value_=np.asarray(vals,dtype=float)
    # An actual64-word constant-biased-vertex code is a feasible t=1 start.
    remaining=set(range(1,11))-{biased};tris=[set(T) for T in combinations(sorted(remaining),3) if all(u in N[v] for u,v in combinations(T,2))]
    partition=next((T for T in combinations(tris,3) if set.union(*T)==remaining and sum(map(len,T))==9),None)
    if partition is None:raise ValueError('NO_BASELINE_CLIQUE_PARTITION')
    baseline=np.zeros(total);table={}
    for v in range(1,11):
        mates=set() if v==biased else next(C-{v} for C in partition if v in C)
        packed=sum(1<<N[v].index(u) for u in mates)
        table[v]=[0 if v==biased else (k&packed).bit_count()%2 for k in range(1<<len(N[v]))]
        baseline[offsets[v]:offsets[v]+len(table[v])]=table[v]
    winners=[w for w in range(1024) if all(((w>>(v-1))&1)==table[v][projection(w,v)] for v in range(1,11))]
    if len(winners)!=64 or any(w>>(biased-1)&1 for w in winners):raise ValueError('BASELINE_CONSTRUCTION')
    baseline[winners]=1;baseline[zstart+pairs.index((64,1))]=1;baseline[tcol]=1
    rep={'kind':'DIRECT_BINARY_SLICE_CAPACITY_PRODUCER_SEARCH_ONLY','biased_vertex':biased,'N':N,'threshold_pairs':pairs,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'pid':os.getpid(),'pgid':os.getpgrp(),'clock_start':subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),'solver_limit_s':limit,'threads':1,'strategy_bits':truth_end-1024,'continuous_selection_variables':1024,'selector_variables':len(pairs),'rows':len(lo),'independent_set_clique_rows':clique_rows,'search_window':'Selected slice counts<=64, total<=102, zero word included, orientationa>=b. A negative solver outcome is NOT a global result.','full_target_boundary':'Any positive producer diagnostic is a candidate only; parent finite-witness pinning, disjoint hostile reviews, independent checkers and explicit acceptance GO remain required. No such replay is run here.','old_packets':'No old archive, declaration, reviewer output or prior witness is read or changed.'}
    h=HS.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit);h.setOptionValue('random_seed',20261029);h.passModel(lp);rep['warm_start_status']=str(h.setSolution(total,np.arange(total,dtype=np.int32),baseline));h.run();rep['solver_status_float']=h.modelStatusToString(h.getModelStatus());sol=h.getSolution();info=h.getInfo()
    rep['solver_objective_float']=h.getObjectiveValue();rep['mip_nodes']=getattr(info,'mip_node_count',None)
    rep['state']='NO_STABLE_INTEGER_STRATEGY_INCUMBENT_NOT_A_NEGATIVE_RESULT'
    if sol.value_valid and len(sol.col_value)==total:
        ys=sol.col_value[1024:truth_end];err=max(abs(v-round(v)) for v in ys);rep['truth_table_integrality_error_float']=err
        if err<1e-6:
            actual={v:[int(round(sol.col_value[offsets[v]+k])) for k in range(1<<len(N[v]))] for v in range(1,11)}
            W=[w for w in range(1024) if all(((w>>(v-1))&1)==actual[v][projection(w,v)] for v in range(1,11))]
            a=sum(not(w>>(biased-1)&1) for w in W);b=len(W)-a;score=a**3+b**3
            rep.update(strategy_tables=actual,winning_words=W,winning_count=len(W),slice_counts=[a,b],integer_cube_sum=score,integer_cube_threshold=64**3)
            rep['state']='POSSIBLE_FULL_TARGET_FINITE_CANDIDATE_PARENT_GATING_REQUIRED' if score>64**3 else 'NO_POSITIVE_PRODUCER_WITNESS_NOT_AN_IMPOSSIBILITY_RESULT'
            if score>64**3:rep['candidate_rational_law']={'denominator':score,'numerator_slice0':a*a,'numerator_slice1':b*b,'proof_lower_bound':'Delta>=log2(a^3+b^3)/3-6>0; this implication and the actual FD support require independent review.'}
    rep['clock_finish']=subprocess.check_output(['/bin/date'],text=True).rstrip('\n');rep['elapsed_s']=time.monotonic()-start;rep['peak_RSS_bytes_if_darwin']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=='darwin' else None;rep['requested_taskpolicy_memory_MiB']=4096;rep['OS_memory_enforcement_independently_tested']=False
    with out.open('x') as f:json.dump(rep,f,indent=1);f.write('\n')
    print(json.dumps({k:v for k,v in rep.items() if k not in ('strategy_tables','winning_words','N')},indent=1),flush=True)
if __name__=='__main__':main()
