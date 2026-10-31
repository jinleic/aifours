#!/usr/bin/env python3
"""Select and exactly reconstruct a component-entropy Farkas cut.
Usage: python3 script.py OUT.json LEAD.jsonl LEAD_SHA [CASE_INDEX]
The floating support is a proposal. A nonnegative, unit-L1 cancellation LP
selects a basic ray. Its selected integer matrix is solved exactly with flint;
all unknown coefficients, signs, normalization and the proposed separator
value are then checked with Fractions. Independent semantic checking is STILL
required: this producer uses the supplied row coefficient proposals.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-flint'));import flint
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'));import highspy as H
INF=H.kHighsInf

def main():
    t=time.monotonic();raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('LEAD_HASH')
    index=int(sys.argv[4]) if len(sys.argv)>4 else 493;lead=next(r for r in (json.loads(l) for l in raw.decode().splitlines()) if r['index']==index)
    support=lead['proposed_farkas_support'];fixed={}
    from ast import literal_eval
    for k,v in lead['fixed_entropy_profile_float'].items():fixed[literal_eval(k)]=Fraction(float(v))
    unknown=sorted({tuple(k) for row in support for k,c in row['terms'] if k[0]=='u'});ui={k:i for i,k in enumerate(unknown)};norm=len(unknown)
    columns=[];source=[];cost=[];starts=[];ids=[];values=[]
    for i,row in enumerate(support):
        terms=[(tuple(k),int(c)) for k,c in row['terms']];base=sum((fixed[k]*c for k,c in terms if k[0]=='f'),Fraction())
        signs=(1,) if row['kind']=='ge' else (1,-1)
        for sign in signs:
            col={ui[k]:sign*c for k,c in terms if k[0]=='u'};col[norm]=1
            columns.append(col);source.append((i,sign));cost.append(float(sign*base));starts.append(len(ids))
            for j,c in col.items():ids.append(j);values.append(c)
    nv=len(columns);nr=norm+1;target=np.zeros(nr);target[-1]=1.
    lp=H.HighsLp();lp.num_col_=nv;lp.num_row_=nr;lp.col_cost_=np.array(cost)
    lp.col_lower_=np.zeros(nv);lp.col_upper_=np.full(nv,INF);lp.row_lower_=target;lp.row_upper_=target
    lp.a_matrix_.format_=H.MatrixFormat.kColwise;lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(values,dtype=float)
    h=H.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',180);h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on')
    h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-10)
    h.passModel(lp);h.run();status=h.modelStatusToString(h.getModelStatus())
    report={'source_lead_sha256':sys.argv[3],'index':index,'factor':lead['factor'],'vertices':lead['vertices'],'functional_color':lead['functional_color'],
      'model_contract':'Fifteen-variable full Shannon, actual component projections/parity/inverse FDs, and S->L identification. Specific triangle encoding only.',
      'cancellation_lp_status':status,'cancellation_lp_objective_float':h.getInfo().objective_function_value,'unknown_equations':norm,'ray_variables':nv,
      'proof_found':False,'attempts':[],'validity_limits':'Exact producer arithmetic only until independent semantic row reconstruction; no general graph-law, code or Delta exclusion claim.'}
    if status=='Optimal':
        x=h.getSolution().col_value
        for threshold in (1e-9,1e-12,0.):
            chosen=[j for j,v in enumerate(x) if v>threshold];touched=sorted({i for j in chosen for i in columns[j]});pos={i:k for k,i in enumerate(touched)}
            attempt={'threshold':threshold,'columns':len(chosen),'touched_equations':len(touched)}
            if not chosen or norm not in pos:attempt['result']='EMPTY';report['attempts'].append(attempt);continue
            dense=[[0]*len(chosen) for _ in touched]
            for k,j in enumerate(chosen):
                for i,c in columns[j].items():dense[pos[i]][k]=c
            A=flint.fmpz_mat(dense);rank=A.rank();attempt['rank']=rank
            if rank!=len(chosen):attempt['result']='RANK_DEFICIENT';report['attempts'].append(attempt);continue
            goal=[0]*len(touched);goal[pos[norm]]=1;At=A.transpose();y=(At*A).solve(At*flint.fmpz_mat([[v] for v in goal]));check=flint.fmpq_mat(A)*y
            if any(check[i,0]!=goal[i] for i in range(len(goal))):attempt['result']='INCONSISTENT';report['attempts'].append(attempt);continue
            yy=[Fraction(int(y[k,0].p),int(y[k,0].q)) for k in range(len(chosen))]
            if any(q<0 for q in yy):attempt['result']='SIGN';report['attempts'].append(attempt);continue
            weights={}
            for j,q in zip(chosen,yy):
                i,sign=source[j];weights[i]=weights.get(i,Fraction())+sign*q
            acc={};multipliers=[]
            for i,w in weights.items():
                if not w:continue
                row=support[i]
                if row['kind']=='ge' and w<0:raise ValueError('EXACT_GE_SIGN')
                for key,c in row['terms']:
                    key=tuple(key);acc[key]=acc.get(key,Fraction())+w*int(c)
                multipliers.append({'row':row['row'],'multiplier':str(w)})
            acc={key:q for key,q in acc.items() if q}
            if any(key[0]=='u' for key in acc):raise ValueError('UNKNOWN_NOT_CANCELLED')
            value=sum((fixed[key]*q for key,q in acc.items()),Fraction())
            if value>=0:attempt['result']='NO_NEGATIVE_SEPARATOR';report['attempts'].append(attempt);continue
            attempt['result']='EXACT';report['attempts'].append(attempt)
            report.update({'proof_found':True,'multipliers':multipliers,'base_cut':[[list(k),str(q)] for k,q in sorted(acc.items())],
              'separation_value_on_binary_float_reference':str(value),'reference_profile_float':lead['fixed_entropy_profile_float'],
              'reference_limits':'This table only records the proposed separating value; it is not asserted exactly feasible or entropic.'});break
    report['elapsed_s']=time.monotonic()-t
    with open(ROOT/sys.argv[1],'x') as f:json.dump(report,f,indent=1);f.write('\n')
    print({k:v for k,v in report.items() if k not in ('multipliers','base_cut','reference_profile_float')},flush=True)
if __name__=='__main__':main()
