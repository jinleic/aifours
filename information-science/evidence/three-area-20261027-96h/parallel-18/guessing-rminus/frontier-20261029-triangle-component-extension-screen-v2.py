#!/usr/bin/env python3
"""Version 2 adds exact component completeness ONLY when a modeled vertex has
just this one selected incident factor: its entire selected tuple equals that
one component up to a bijection, so the variables are identified. All other
vertices retain only the projection premise. The coloring is checked.
Min-uniform-violation screen of actual selected-triangle component extensions.
Usage: python3 script.py OUT.jsonl POINTS.jsonl POINTS_SHA INDICES FACTOR LIMIT
Fifteen variables: Y1..Y10,S,L,U,V,W. L is the selected factor's functional;
S->L is an exact coordinate identification. U,V,W are projections of their
vertex tuples and obey the parity/three inverse FDs. Full elemental Shannon.
Unknown component coordinates are solved, never zero-filled. Positive values
are only leads; proposed Farkas supports are exported for exact reconstruction.
No imported-functional Delta gate or paused source is used.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
s=spec_from_file_location('cp',ROOT/'frontier-20261029-dfz-cutting-plane-v3.py');cp=module_from_spec(s);s.loader.exec_module(cp)
H=cp.highspy;INF=H.kHighsInf
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
S=1<<10;L=1<<11;COMP=(1<<12)|(1<<13)|(1<<14)

def screen(record,factor,limit):
    if not 1<=factor<=10:raise ValueError('FACTOR')
    text=record['colors'];ch=text[factor-1]
    if ch=='-':raise ValueError('FACTOR_NOT_SELECTED')
    color=int(ch);vertices=TRI[factor-1]
    aliases=[]
    for slot,v in enumerate(vertices):
        selected=[t+1 for t,T in enumerate(TRI) if v in T and text[t]!='-']
        if selected==[factor]:aliases.append({'slot':slot,'vertex':v,'selected_incident_factors':selected})
    if not record.get('proposal_available') or record.get('model_sha256')!='3d2404226d11b85b537002b6f7303571d58c9ca1f7c6057b9d32958489e5b4e3':raise ValueError('INDEPENDENT_POINT_SCOPE')
    point={tuple(k):float(v) for k,v in zip(record['keys'],record['float_values'])};acts=[(tuple(p),tuple(cp)) for p,cp in record['actions']]
    def fixed(a,b):
        key=min((sum(1<<(p[i]-1) for i in range(10) if a>>i&1),2+cp[b-2] if b>=2 else b) for p,cp in acts)
        return point[key]
    def K(mask):
        for alias in aliases:
            bit=1<<(12+alias['slot'])
            if mask&bit:mask=(mask&~bit)|(1<<(alias['vertex']-1))
        if mask&S:mask&=~L
        if not mask:return None
        if not mask&COMP:
            a=mask&1023;b=1 if mask&S else (2+color if mask&L else 0)
            return ('f',a,b)
        return ('u',mask)
    M=cp.Model();variable_names=[f'Y{i}' for i in range(1,11)]+['S','L','U','V','W']
    cp.add_shannon(M,variable_names,K)
    for slot,v in enumerate(vertices):
        bit=1<<(12+slot);yv=1<<(v-1);M.add([(K(yv|bit),1),(K(yv),-1)],0,0,('component-projection',slot,v))
    M.add([(K(COMP|L),1),(K(COMP),-1)],0,0,('component-parity',))
    for slot in range(3):M.add([(K(COMP|L),1),(K((COMP^(1<<(12+slot)))|L),-1)],0,0,('component-inverse',slot))
    known={};unknown={};reverse={j:key for key,j in M.col.items()}
    for key,j in M.col.items():
        if key[0]=='f':known[j]=fixed(key[1],key[2])
        else:unknown[j]=len(unknown)
    tc=len(unknown);starts=[];ids=[];values=[];lo=[];hi=[];rowmap=[]
    def push(items,l,u,i):
        starts.append(len(ids));rowmap.append(i)
        for j,c in items:ids.append(j);values.append(c)
        lo.append(l);hi.append(u)
    for i,row in enumerate(M.rows):
        rhs=-sum(c*known[j] for j,c in row.items() if j in known);items=[(unknown[j],float(c)) for j,c in row.items() if j in unknown]
        push(items+[(tc,1.)],rhs,INF,i)
        if M.hi[i]==0:push(items+[(tc,-1.)],-INF,rhs,i)
    lp=H.HighsLp();lp.num_col_=tc+1;lp.num_row_=len(lo);cost=np.zeros(tc+1);cost[tc]=1.;lp.col_cost_=cost
    lower=np.full(tc+1,-INF);lower[tc]=0.;lp.col_lower_=lower;lp.col_upper_=np.full(tc+1,INF)
    lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi);lp.a_matrix_.format_=H.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(values,dtype=float)
    h=H.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit);h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','off')
    h.passModel(lp);t=time.monotonic();h.run();status=h.modelStatusToString(h.getModelStatus());obj=h.getInfo().objective_function_value if status=='Optimal' else None
    report={'index':record['index'],'colors':text,'factor':factor,'vertices':vertices,'functional_color':color,'component_variable_aliases':aliases,'status_float':status,'min_uniform_violation':obj,
      'verdict_float':('cut_lead' if obj>1e-6 else 'extends_within_tolerance') if obj is not None else 'unknown','branch_rows':len(M.rows),'relaxed_rows':len(lo),'unknown_coordinates':tc,'solve_s':time.monotonic()-t,
      'model_contract':'Actual coordinate projections and parity/inverse FDs; full 15-variable Shannon with S->L. Numerical screen only.'}
    if obj is not None and obj>1e-6:
        weights={}
        for i,w in zip(rowmap,h.getSolution().row_dual):weights[i]=weights.get(i,0.)+float(w)
        support=[]
        for i,w in weights.items():
            if abs(w)<=1e-8:continue
            meta=M.meta[i]
            if meta[0]=='cmi':meta=('cmi',*meta[2:])
            elif meta[0]=='mono':meta=('mono',meta[2])
            support.append({'row':meta,'terms':[[list(reverse[j]),int(c)] for j,c in M.rows[i].items()],'kind':'ge' if M.hi[i]==INF else 'eq','weight_float':w})
        report.update({'proposed_farkas_support':support,'support_threshold':1e-8,'fixed_entropy_profile_float':{repr(reverse[j]):v for j,v in known.items()},
          'support_limits':'Floating support proposal only. An exact sign/cancellation proof and independent semantic row reconstruction are required before using a derived cut.'})
    return report

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('POINT_HASH')
    records={r['index']:r for r in (json.loads(l) for l in raw.decode().splitlines())};factor=int(sys.argv[5]);limit=float(sys.argv[6])
    with open(ROOT/sys.argv[1],'x') as f:
        for i in map(int,sys.argv[4].split(',')):
            report=screen(records[i],factor,limit);report['points_sha256']=sys.argv[3];f.write(json.dumps(report)+'\n');f.flush();print(i,factor,report['status_float'],report['min_uniform_violation'],report['verdict_float'],flush=True)
if __name__=='__main__':main()
