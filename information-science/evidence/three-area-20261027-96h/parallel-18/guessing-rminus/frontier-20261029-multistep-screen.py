#!/usr/bin/env python3
"""Screen multi-step copy programs at a FLOATING central point (exploratory leads only).

Usage: python3 script.py OUT.jsonl POINT.json POINT_SHA PROGRAMS.json [START END TIME_LIMIT]
PROGRAMS.json: {"programs": [{"id": str, "steps": [{"copy": [...], "over": [...]}, ...]}]}.
References: integers 1..10 are the original variables X1..X10; strings "c0",
"c1", ... are copy variables in creation order. Each step creates one new
atomic copy per entry of "copy" (a copy of that single variable); jointly the
new tuple has the law of the copied tuple over the "over" variables and is
conditionally independent of every previously existing variable given them.
The feasibility LP fixes the original coordinates to the point's
'final_columns_float' values and asks for auxiliary coordinates satisfying
every elemental Shannon inequality of the whole variable set, every copy
marginal equality h(U Q') = h(U Q) (U a subset of the individual over-set
variables, Q a nonempty subset of the step's copied entries) and every step
independence equality. Infeasible = the central point is cut by the program
(necessary, not sufficient, for lowering the optimum); Optimal = the point
extends, so adding the program cannot lower the optimum (up to tolerances).
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
INF=highspy.kHighsInf

def compile_program(prog):
    """Return (n, steps) with steps as (new_bits list, old_bits list, over_mask, existing_mask)."""
    idx={};n=10;out=[];existing=(1<<10)-1
    def bit(ref):
        if isinstance(ref,int):
            if not 1<=ref<=10:raise ValueError(('REF',ref))
            return ref-1
        if ref not in idx:raise ValueError(('UNDEFINED',ref))
        return idx[ref]
    for st in prog['steps']:
        over=0
        for r in st['over']:over|=1<<bit(r)
        old=[bit(r) for r in st['copy']];new=[]
        for r in st['copy']:
            name=f'c{n-10}';idx[name]=n;new.append(n);n+=1
        if over&sum(1<<b for b in new):raise ValueError('OVERLAP')
        out.append((new,old,over,existing));existing|=sum(1<<b for b in new)
    return n,out

def rows_for(n,steps):
    allm=(1<<n)-1;rows=[]
    def add(terms,eq):
        full={}
        for m,c in terms:
            if m:full[m]=full.get(m,0)+c
        full={m:c for m,c in full.items() if c}
        if full and any(m>=1024 for m in full):rows.append((full,eq))
    for i in range(n):add(((allm,1),(allm^(1<<i),-1)),False)
    for i,j in combinations(range(n),2):
        rest=allm^(1<<i)^(1<<j);z=rest
        while True:
            if i>=10 or j>=10 or z>=1024:add(((z|1<<i,1),(z|1<<j,1),(z|1<<i|1<<j,-1),(z,-1)),False)
            if not z:break
            z=(z-1)&rest
    for new,old,Y,E in steps:
        k=len(new);Nn=sum(1<<b for b in new)
        for q in range(1,1<<k):
            nm=sum(1<<new[a] for a in range(k) if q>>a&1);om=sum(1<<old[a] for a in range(k) if q>>a&1)
            U=Y
            while True:
                add(((U|nm,1),(U|om,-1)),True)
                if not U:break
                U=(U-1)&Y
        add(((E|Nn,1),(Y,1),(E,-1),(Y|Nn,-1)),True)
    return rows

def screen(n,rows,base,limit):
    ncol=(1<<n)-1024;starts=[];ids=[];vals=[];lo=[];hi=[]
    for full,eq in rows:
        starts.append(len(ids));rhs=-sum(c*base[m] for m,c in full.items() if m<1024)
        for m,c in full.items():
            if m>=1024:ids.append(m-1024);vals.append(float(c))
        lo.append(rhs);hi.append(rhs if eq else INF)
    lp=highspy.HighsLp();lp.num_col_=ncol;lp.num_row_=len(rows)
    lp.col_cost_=np.zeros(ncol);lp.col_lower_=np.full(ncol,-INF);lp.col_upper_=np.full(ncol,INF)
    lp.row_lower_=np.array(lo);lp.row_upper_=np.array(hi);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32)
    lp.a_matrix_.value_=np.array(vals,dtype=float)
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',limit)
    h.passModel(lp);t=time.monotonic();h.run()
    return h.modelStatusToString(h.getModelStatus()),round(time.monotonic()-t,2)

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('POINT_HASH')
    cols=json.loads(raw)['final_columns_float'];base={m:cols[repr(('o',m))] for m in range(1,1024)};base[0]=0.0
    progs=json.loads((ROOT/sys.argv[4]).read_text())['programs']
    start=int(sys.argv[5]) if len(sys.argv)>5 else 0;end=int(sys.argv[6]) if len(sys.argv)>6 else len(progs)
    limit=float(sys.argv[7]) if len(sys.argv)>7 else 120.0
    with open(out,'a',encoding='utf-8') as f:
        f.write(json.dumps({'header':True,'point_sha256':sys.argv[3],'programs_sha256':sha256((ROOT/sys.argv[4]).read_bytes()).hexdigest(),'start':start,'end':end})+'\n');f.flush()
        for i in range(start,min(end,len(progs))):
            p=progs[i];n,steps=compile_program(p);rows=rows_for(n,steps);status,dt=screen(n,rows,base,limit)
            f.write(json.dumps({'index':i,'id':p['id'],'n':n,'rows':len(rows),'status_float_unverified':status,'solve_s':dt})+'\n');f.flush()

if __name__=='__main__':main()
