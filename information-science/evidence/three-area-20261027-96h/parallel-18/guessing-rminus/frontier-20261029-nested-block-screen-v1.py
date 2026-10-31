#!/usr/bin/env python3
"""Minimum-uniform-violation screen of compressed nested copy blocks.
Usage: python3 script.py OUT.jsonl POINT.json POINT_SHA SPECS.json SPECS_SHA [START END LIMIT]
POINT supplies a floating original entropy profile, fixed during each screen.
SPECS has branches as in nested-copy-block-lp-v1.py. Each branch is tested
separately with ALL its compressed elemental and copy rows. Introduce t>=0,
relax each inequality by t and each equality in both directions by t, minimize
t by IPM without crossover. t>1e-6 is a candidate only; a full re-solve and exact
certificate are required for any new bound. t<=1e-6 is only a tolerance-level
extension, not an exact feasibility certificate or a saturation theorem.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
s=spec_from_file_location('nb',ROOT/'frontier-20261029-nested-copy-block-lp-v1.py');nb=module_from_spec(s);s.loader.exec_module(nb)
H=nb.cp.highspy;INF=H.kHighsInf

def screen(sp,base,limit):
    M=nb.cp.Model();nb.add_branch(M,'n0',sp);aux={};original={}
    for key,j in M.col.items():
        if key[0]=='o':original[j]=base[key[1]]
        else:aux[j]=len(aux)
    tc=len(aux);starts=[];ids=[];vals=[];lo=[];hi=[]
    def push(ts,l,h):
        starts.append(len(ids))
        for j,c in ts:ids.append(j);vals.append(c)
        lo.append(l);hi.append(h)
    for i,row in enumerate(M.rows):
        rhs=-sum(c*original[j] for j,c in row.items() if j in original)
        ts=[(aux[j],float(c)) for j,c in row.items() if j in aux]
        push(ts+[(tc,1.)],rhs,INF)
        if M.hi[i]==0:push(ts+[(tc,-1.)],-INF,rhs)
    lp=H.HighsLp();lp.num_col_=tc+1;lp.num_row_=len(lo);cost=np.zeros(tc+1);cost[tc]=1.;lp.col_cost_=cost
    lower=np.full(tc+1,-INF);lower[tc]=0.;lp.col_lower_=lower;lp.col_upper_=np.full(tc+1,INF)
    lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi);lp.a_matrix_.format_=H.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(vals,dtype=float)
    h=H.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit);h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','off')
    h.passModel(lp);t=time.monotonic();h.run();status=h.modelStatusToString(h.getModelStatus())
    obj=h.getInfo().objective_function_value if status=='Optimal' else None
    return {'status_float_unverified':status,'min_uniform_violation':obj,'verdict_float':('cut' if obj>1e-6 else 'extends_within_tolerance') if obj is not None else 'unknown',
            'branch_rows':len(M.rows),'auxiliary_coordinates':tc,'solve_s':time.monotonic()-t}

def main():
    point=(ROOT/sys.argv[2]).read_bytes();specbytes=(ROOT/sys.argv[4]).read_bytes()
    if sha256(point).hexdigest()!=sys.argv[3] or sha256(specbytes).hexdigest()!=sys.argv[5]:raise ValueError('HASH')
    cols=json.loads(point)['final_columns_float'];base={m:cols[repr(('o',m))] for m in range(1,1024)};specs=json.loads(specbytes)['branches']
    start=int(sys.argv[6]) if len(sys.argv)>6 else 0;end=int(sys.argv[7]) if len(sys.argv)>7 else len(specs);limit=float(sys.argv[8]) if len(sys.argv)>8 else 600.
    with open(ROOT/sys.argv[1],'x') as f:
        f.write(json.dumps({'header':True,'point_sha256':sys.argv[3],'specs_sha256':sys.argv[5],'start':start,'end':end})+'\n');f.flush()
        for i in range(start,min(end,len(specs))):
            d=screen(specs[i],base,limit);d.update({'index':i,'id':specs[i].get('id',str(i))});f.write(json.dumps(d)+'\n');f.flush();print(i,d['id'],d['verdict_float'],d['min_uniform_violation'],flush=True)
if __name__=='__main__':main()
