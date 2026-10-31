#!/usr/bin/env python3
"""Fresh numerical proposal ONLY; never a scientific PASS or exact bound.
Usage: script.py OUT.json CONTRACT_SHA MODE SOLVER_SECONDS
No old archive, checker, review return or prior point is read. A possible
full-target value is frozen for parent gating, with no certificate/replay here.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json,os,resource,signal,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy as HS
INF=HS.kHighsInf
CONTRACT='frontier-20261029-twin-diamond-copy-proposal-contract-v1.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
GENS=((8,10,7,6,9,3,4,1,2,5),(1,5,6,7,2,3,4,8,9,10))
V=1023
class StopRequested(Exception):pass
DEADLINE=0

def check_time():
    if DEADLINE and time.monotonic()>DEADLINE:raise StopRequested('INTERNAL_TOTAL_DEADLINE')
def onstop(sig,frame):raise StopRequested('SIGNAL_'+str(sig))
signal.signal(signal.SIGTERM,onstop);signal.signal(signal.SIGINT,onstop)
def vm(vs):return sum(1<<(v-1) for v in vs)
def subsets(mask):
    x=mask;seen=0
    while True:
        yield x;seen+=1
        if not x:break
        x=(x-1)&mask
    if seen!=1<<mask.bit_count():raise ValueError('SUBSET_ENUMERATION_COVERAGE')
def move_original(mask,p):return sum(1<<(p[i]-1) for i in range(10) if mask>>i&1)

def group(copies):
    E={frozenset((v,u)) for v in N for u in N[v]};original={tuple(range(1,11))};todo=list(original)
    for g in GENS:
        if {frozenset(g[v-1] for v in e) for e in E}!=E:raise ValueError('GRAPH_GENERATOR')
    while todo:
        p=todo.pop()
        for g in GENS:
            q=tuple(g[p[i]-1] for i in range(10))
            if q not in original:original.add(q);todo.append(q)
    if len(original)!=8 or len(E)!=26:raise ValueError('GRAPH_GROUP')
    lookup={(c['old'],c['over_mask']):i for i,c in enumerate(copies)};out=[]
    for p in sorted(original):
        image=[(p[c['old']-1],move_original(c['over_mask'],p)) for c in copies]
        if set(image)!=set(lookup):continue
        ext=tuple(v-1 for v in p)+tuple(10+lookup[key] for key in image);out.append(ext)
    n=10+len(copies)
    if tuple(range(n)) not in out or any(tuple(p[q[i]] for i in range(n)) not in out for p in out for q in out):raise ValueError('COPY_STABILIZER_CLOSURE')
    return out

def build(copies):
    n=10+len(copies);full=(1<<n)-1;acts=group(copies);maps=[]
    for p in acts:
        image=[0]*(1<<n)
        for a in range(1,1<<n):
            bit=a&-a;image[a]=image[a^bit]|1<<p[bit.bit_length()-1]
        maps.append(image)
    canonical=[min(image[a] for image in maps) for a in range(1<<n)]
    keys=sorted(set(canonical)-{0});position={a:i for i,a in enumerate(keys)};index=[-1 if not a else position[canonical[a]] for a in range(1<<n)]
    rows=[];lo=[];hi=[];names=[];seen=set();raw_counts=Counter()
    def add(ts,l,u,name):
        raw_counts[name[0]]+=1;d={}
        for mask,c in ts:
            if mask:d[index[mask]]=d.get(index[mask],0)+c
        d={i:c for i,c in d.items() if c};sig=(tuple(sorted(d.items())),l,u)
        if not d or sig in seen:return
        seen.add(sig);rows.append(d);lo.append(l);hi.append(u);names.append(name)
    for i in range(n):add(((full,1),(full^(1<<i),-1)),0,INF,('mono',i))
    for i,j in combinations(range(n),2):
        check_time();a,b=1<<i,1<<j
        for K in subsets(full^(a|b)):add(((K|a,1),(K|b,1),(K|a|b,-1),(K,-1)),0,INF,('cmi',i,j,K))
    if raw_counts['cmi']!=n*(n-1)//2*(1<<(n-2)):raise ValueError('FULL_JOINT_CMI_COVERAGE')
    for v in range(1,11):
        a=vm(N[v]);add(((a|1<<(v-1),1),(a,-1)),0,0,('original-fd',v))
        add(((1<<(v-1),1),),-INF,1,('singleton-cap',v))
    for cidx,c in enumerate(copies):
        check_time();old=1<<(c['old']-1);new=1<<(10+cidx);over=c['over_mask']
        if over&old or over.bit_count()!=7:raise ValueError('COPY_DESCRIPTOR')
        for a in subsets(over):add(((a|new,1),(a|old,-1)),0,0,('copy-match',cidx,a))
        add(((over|new,1),(full^new,1),(full,-1),(over,-1)),0,0,('copy-independence',cidx))
        for v in range(1,11):
            nb=vm(N[v]);family=nb|1<<(v-1)
            if family&old and not family&~(over|old):
                def rename(m):return (m&~old)|(new if m&old else 0)
                add(((rename(family),1),(rename(nb),-1)),0,0,('copy-fd',cidx,v))
    return n,acts,keys,rows,lo,hi,names,raw_counts

def main():
    global DEADLINE
    start=time.monotonic();DEADLINE=start+240
    out=ROOT/sys.argv[1]
    if out.exists():raise FileExistsError('EXCLUSIVE_OUTPUT_ALREADY_EXISTS')
    raw=(ROOT/CONTRACT).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[2]:raise ValueError('CONTRACT_SHA')
    contract=json.loads(raw);mode=sys.argv[3];limit=float(sys.argv[4])
    if mode not in contract['copy_modes'] or not 0<limit<=120:raise ValueError('BOUNDED_ARGUMENTS')
    if contract['graph_N']!={str(v):list(N[v]) for v in N}:raise ValueError('LITERAL_GRAPH_BINDING')
    copies=[{'old':c['old'],'over_mask':V^vm(c['excluded']),'excluded':c['excluded']} for c in contract['copy_modes'][mode]]
    report={'kind':'NUMERICAL_PROPOSAL_NOT_A_BOUND_OR_SCIENTIFIC_REPLAY','state':'INCOMPLETE','mode':mode,'copies':copies,'contract_sha256':sys.argv[2],'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'pid':os.getpid(),'pgid':os.getpgrp(),'argv':sys.argv,'clock_start':subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),'threads':1,'solver_limit_s':limit,'internal_total_deadline_s':240,'requested_memory_MiB_from_contract':4096,'OS_memory_enforcement_independently_tested':False,'not_established':['Exact entropy bound','Probability law/winning code','Scientific acceptance/formal proof/novelty','Any authority or replay GO for the old bulk archive']}
    print(json.dumps({k:report[k] for k in ('kind','pid','pgid','mode','source_sha256','contract_sha256')}),flush=True)
    try:
        n,acts,keys,rows,lo,hi,names,raw_counts=build(copies);check_time();nr=len(rows);nc=len(keys)
        report.update(joint_variables=n,raw_entropy_coordinates=(1<<n)-1,canonical_coordinates=nc,group_order=len(acts),group_actions=acts,canonical_entropy_keys=keys,raw_row_counts=dict(raw_counts),unique_rows=nr)
        starts=[0];indices=[];values=[]
        for row in rows:
            for j,c in row.items():indices.append(j);values.append(c)
            starts.append(len(indices))
        cost=np.zeros(nc);cost[keys.index(V)]=-1
        lp=HS.HighsLp();lp.num_col_=nc;lp.num_row_=nr;lp.col_cost_=cost
        lp.col_lower_=np.full(nc,-INF);lp.col_upper_=np.full(nc,INF);lp.row_lower_=np.asarray(lo,dtype=float);lp.row_upper_=np.asarray(hi,dtype=float)
        lp.a_matrix_.format_=HS.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.asarray(starts,dtype=np.int32);lp.a_matrix_.index_=np.asarray(indices,dtype=np.int32);lp.a_matrix_.value_=np.asarray(values,dtype=float)
        h=HS.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',min(limit,max(0.1,DEADLINE-time.monotonic())));h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on');h.passModel(lp);h.run();check_time()
        status=h.modelStatusToString(h.getModelStatus());report['status_float']=status
        info=h.getInfo();report['max_primal_infeasibility_float']=getattr(info,'max_primal_infeasibility',None);report['max_dual_infeasibility_float']=getattr(info,'max_dual_infeasibility',None)
        if status=='Optimal':
            numerical=-h.getObjectiveValue();report['numerical_objective_only']=numerical;report['state']='PROPOSAL_ONLY'
            if numerical<=20/3+1e-7:report['state']='POSSIBLE_FULL_TARGET_CANDIDATE_PARENT_GATING_REQUIRED_NO_FURTHER_ASSAY'
            elif numerical<2603/389-1e-7:report['state']='POSSIBLE_NUMERICAL_IMPROVEMENT_EXACT_CERTIFICATE_NOT_ESTABLISHED'
            sol=h.getSolution();report['column_primal_float']=sol.col_value;report['row_dual_float']=sol.row_dual;report['row_descriptors']=names;report['row_relations']=['eq' if a==b else 'ge' if a==0 and b==INF else 'le' for a,b in zip(lo,hi)]
        else:report['state']='NUMERICAL_UNKNOWN_NO_BOUND'
    except StopRequested as exc:report['state']='INCOMPLETE';report['stop_reason']=str(exc)
    except Exception as exc:report['state']='INCOMPLETE';report['error_type']=type(exc).__name__;report['error']=str(exc)
    report['clock_finish']=subprocess.check_output(['/bin/date'],text=True).rstrip('\n');report['elapsed_s']=time.monotonic()-start
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;report['resource_ru_maxrss_native']=rss;report['peak_RSS_bytes_if_darwin']=rss if sys.platform=='darwin' else None;report['platform']=sys.platform
    with out.open('x') as f:json.dump(report,f);f.write('\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('column_primal_float','row_dual_float','row_descriptors','row_relations','canonical_entropy_keys','group_actions')},indent=1),flush=True)
if __name__=='__main__':main()
