#!/usr/bin/env python3
"""Screen all two-variable one-step copy structures at a central optimal point.

Usage: python3 script.py OUT.jsonl CENTRAL.json SHA [START]
For every automorphism-orbit representative (S pair, T nonempty, disjoint) the
12-variable copy LP of frontier-20261029-general-copy-scan.py (full Shannon,
all subset copy marginals, conditional independence) is solved by IPM with the
original coordinates fixed to the floating central original profile. An
'Infeasible' status is a lead for adding that copy branch; nothing else is
inferred.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
s=spec_from_file_location('gs',ROOT/'frontier-20261029-general-copy-scan.py');gs=module_from_spec(s);s.loader.exec_module(gs)

def status(rows,base):
    hs=gs.highspy;ncol=3072;starts=[];ids=[];vals=[];lo=[];hi=[]
    for full,eq,meta in rows:
        starts.append(len(ids));rhs=-sum((Fraction(c)*base[m] for m,c in full.items() if m<1024),Fraction())
        for m,c in full.items():
            if m>=1024:ids.append(m-1024);vals.append(float(c))
        r=float(rhs);lo.append(r);hi.append(r if eq else hs.kHighsInf)
    lp=hs.HighsLp();lp.num_col_=ncol;lp.num_row_=len(rows)
    lp.col_cost_=np.zeros(ncol);lp.col_lower_=np.full(ncol,-hs.kHighsInf);lp.col_upper_=np.full(ncol,hs.kHighsInf)
    lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi);lp.a_matrix_.format_=hs.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(vals,dtype=float)
    h=hs.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',60.0);h.setOptionValue('solver','ipm')
    h.passModel(lp);t=time.monotonic();h.run();return h.modelStatusToString(h.getModelStatus()),time.monotonic()-t

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    start=int(sys.argv[4]) if len(sys.argv)>4 else 0
    cols=json.loads(raw)['final_columns_float'];base={m:Fraction(cols[repr(('o',m))]) for m in range(1,1024)};base[0]=Fraction(0)
    G=gs.group();reps=gs.representatives(G,2);sh=gs.shannon_rows(base,2)
    with open(out,'x',encoding='utf-8') as f:
        f.write(json.dumps({'header':True,'central_sha256':sys.argv[3],'representatives':len(reps),'start':start})+'\n')
        for idx in range(start,len(reps)):
            S,T=reps[idx];st,dt=status(sh+gs.copy_rows(base,S,T),base)
            f.write(json.dumps({'index':idx,'S_one_based':[x+1 for x in S],'T_one_based':[x+1 for x in T],'status':st,'solve_s':round(dt,2)})+'\n');f.flush()
            if st!='Optimal':print(idx,[x+1 for x in S],[x+1 for x in T],st,flush=True)

if __name__=='__main__':main()
