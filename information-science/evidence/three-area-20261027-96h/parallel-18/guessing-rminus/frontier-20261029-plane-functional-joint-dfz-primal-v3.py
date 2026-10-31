#!/usr/bin/env python3
"""Version 3 uses crossover and exports an available finite solver point even
when no exact grid is reconstructed; non-Optimal status is NEVER promoted to
an exact feasibility claim. Version 2 nocrossover returned Unknown and no
usable point; this successor repairs proposal export, not scientific acceptance.
Version 2 exports the IPM-without-crossover face point even when no exact
rational grid is reconstructed; it is ONLY a separation proposal.
Normalized exact-grid proposals for the v1 full-state-gate base PLUS full
joint Shannon closure and literal admitted joint DFZ cuts. No paused import
route and no functional-fiber Delta gates. Base-primal checking is not by
itself verification of the additional DFZ rows.
Usage: python3 script.py OUT.jsonl CLASSES.json INDICES LIMIT_SECONDS CUTS.json CUTS_SHA
Uses the byte-pinned joint-Shannon/DFZ successor of the v1 base, NOT the paused imported-gate
route. Normalize sum_v h(Y_v)=1 and maximize integer 3*Delta. Accept a positive
rational profile only after exact integer checks of every model row. Such a
profile is a RELAXATION COUNTERMODEL, not a probability law or guessing code.
An independent primal check is still required.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import chain
from math import lcm
from pathlib import Path
import json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent
MODEL='frontier-20261029-plane-functional-joint-dfz-dual-v2.py';MODEL_SHA='3d2404226d11b85b537002b6f7303571d58c9ca1f7c6057b9d32958489e5b4e3'
if sha256((ROOT/MODEL).read_bytes()).hexdigest()!=MODEL_SHA:raise ValueError('V1_MODEL_HASH')
s=spec_from_file_location('v1model',ROOT/MODEL);model=module_from_spec(s);s.loader.exec_module(model)
H=model.highspy;INF=H.kHighsInf

def find(col,limit):
    keys,acts,names,rr,lo,hi,target=model.build(col);n=len(keys);ix={k:i for i,k in enumerate(keys)}
    def canon(a,b):return min((model.move(a,p),2+cp[b-2] if b>=2 else b) for p,cp in acts)
    norm={}
    for i in range(10):j=ix[canon(1<<i,0)];norm[j]=norm.get(j,0)+1
    rr.append(list(norm.items()));lo.append(1);hi.append(1);names.append(('normalization',))
    starts=[];ids=[];values=[]
    for items in rr:
        starts.append(len(ids))
        for j,c in items:ids.append(j);values.append(c)
    lp=H.HighsLp();lp.num_col_=n;lp.num_row_=len(rr);lp.col_cost_=target;lp.sense_=H.ObjSense.kMaximize
    lp.col_lower_=np.full(n,-INF);lp.col_upper_=np.full(n,INF);lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi)
    lp.a_matrix_.format_=H.MatrixFormat.kRowwise;lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(values,dtype=float)
    h=H.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit);h.setOptionValue('solver','ipm');h.setOptionValue('run_crossover','on')
    h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-9)
    h.passModel(lp);t=time.monotonic();h.run();status=h.modelStatusToString(h.getModelStatus())
    report={'status_float':status,'objective_3Delta_float':h.getInfo().objective_function_value,'solve_s':time.monotonic()-t,'exact_grid_found':False,
       'model_scope':'V1_FULL_STATE_GATE_ONLY','variables':n,'rows':len(rr),'model_sha256':MODEL_SHA,'additional_relaxation':'Full joint 13-variable Shannon closure plus the literal admitted DFZ cuts','joint_cuts_sha256':sys.argv[6]}
    sol=h.getSolution()
    if not sol.value_valid or len(sol.col_value)!=n or not all(np.isfinite(v) for v in sol.col_value):
        report['proposal_available']=False;return report
    x=sol.col_value
    report.update({'proposal_available':True,'keys':keys,'float_values':[float(v) for v in x],'actions':[[list(p),list(cp)] for p,cp in acts],
      'proposal_method':'IPM with crossover; valid solver values are exported only as separation proposals. Solver status is preserved and is not an exact feasibility certificate.'})
    if status!='Optimal' or report['objective_3Delta_float']<=1e-7:return report
    candidates=[];qs=[Fraction(float(v)).limit_denominator(100000) for v in x];D=1
    for q in qs:
        D=lcm(D,q.denominator)
        if D.bit_length()>128:break
    if D.bit_length()<=128:candidates.append((D,[q.numerator*(D//q.denominator) for q in qs],'coordinate_fraction_reconstruction'))
    candidates=chain(candidates,((D,[int(round(float(v)*D)) for v in x],'integer_grid_rounding') for D in range(1,241)))
    for D,nums,method in candidates:
        valid=True
        for items,l,u in zip(rr,lo,hi):
            val=sum(int(c)*nums[j] for j,c in items)
            if (l!=-INF and val<int(l)*D) or (u!=INF and val>int(u)*D):valid=False;break
        if not valid:continue
        gapnum=sum(int(target[j])*nums[j] for j in range(n))
        if gapnum<=0:continue
        report.update({'exact_grid_found':True,'common_denominator':D,'keys':keys,'numerators':nums,'actions':[[list(p),list(cp)] for p,cp in acts],
          'exact_3Delta':str(Fraction(gapnum,D)),'exact_Delta':str(Fraction(gapnum,3*D)),'reconstruction':method,
          'acceptance':'All normalized-v1 model inequalities/equalities checked with Python integers; probability realizability not asserted.'});break
    return report

def main():
    data=(ROOT/sys.argv[2]).read_bytes();classes=json.loads(data)['colorings'];indices=[int(x) for x in sys.argv[3].split(',')];limit=float(sys.argv[4])
    cutsraw=(ROOT/sys.argv[5]).read_bytes()
    if sha256(cutsraw).hexdigest()!=sys.argv[6]:raise ValueError('CUTS_HASH')
    model.JOINT_CUTS=json.loads(cutsraw)['cuts']
    for c in model.JOINT_CUTS:
        masks=[c[k] for k in ('A','B','C','D','Z')]
        if tuple(c['coefficients']) not in model.ADMITTED_DFZ or not all(masks[:4]) or any(not 0<=m<8192 for m in masks) or any(masks[i]&masks[j] for i in range(5) for j in range(i+1,5)):raise ValueError('CUT_ADMISSION')
    with open(ROOT/sys.argv[1],'x') as f:
        for i in indices:
            text=classes[i];col=tuple(None if c=='-' else int(c) for c in text);r=find(col,limit);r.update({'index':i,'colors':text,'classes_sha256':sha256(data).hexdigest()})
            f.write(json.dumps(r)+'\n');f.flush();print(i,r['status_float'],r['objective_3Delta_float'],r['exact_grid_found'],r.get('exact_Delta'),flush=True)
if __name__=='__main__':main()
