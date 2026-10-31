#!/usr/bin/env python3
"""Produce an exact rational dual certificate for a DFZ cutting-plane LP.

Usage: python3 script.py OUT.json CUTTING_PLANE_RESULT.json SHA
Rebuilds the LP exactly as frontier-20261029-dfz-cutting-plane.py does (same
row builder, same branches flag) with the recorded DFZ cut instances, solves it
by dual simplex for a basic dual, and solves the dual identity EXACTLY over Q
(python-flint normal equations on the basic support). Every row in the support
is written with a semantic description so an independent checker can rebuild
it. The bound is beta = sum of cap multipliers; the identity proves
h(V) <= beta for every vector satisfying the rows.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-flint'))
import flint
spec=spec_from_file_location('cp',ROOT/'frontier-20261029-dfz-cutting-plane.py');cp=module_from_spec(spec);spec.loader.exec_module(cp)

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    res=json.loads(raw);M=cp.build(res['branches'])
    for c in res['cuts']:
        t=cp.dfz_terms(tuple(c['coefficients']),c['A'],c['B'],c['C'],c['D'],c['Z'])
        M.add([(('o',m),x) for m,x in t.items()],0,cp.INF,('dfz',c['coefficients'],c['A'],c['B'],c['C'],c['D'],c['Z']))
    t0=time.monotonic();h,status,obj,x,dt=cp.solve(M)
    if status!='Optimal':raise ValueError(status)
    dual=np.array(h.getSolution().row_dual);supp=[i for i,y in enumerate(dual) if abs(y)>1e-10]
    ncol=len(M.col);goal=[0]*ncol;goal[M.col[('o',1023)]]=1
    # identity: sum_i y_i * row_i = objective gradient (maximize h(V)); HiGHS minimizes -h(V)
    Mt=[[0]*len(supp) for _ in range(ncol)]
    for k,i in enumerate(supp):
        for j,a in M.rows[i].items():Mt[j][k]=int(a)
    A=flint.fmpz_mat(Mt);rank=A.rank()
    if rank!=len(supp):raise ValueError(('RANK',rank,len(supp)))
    At=A.transpose();y=(At*A).solve(At*flint.fmpz_mat([[g] for g in goal]))
    r=flint.fmpq_mat(A)*y
    if any(r[j,0]!=goal[j] for j in range(ncol)):raise ValueError('INCONSISTENT')
    mult=[];beta=Fraction(0)
    for k,i in enumerate(supp):
        q=y[k,0];qq=Fraction(int(q.p),int(q.q))
        if qq==0:continue
        lo,hi=M.lo[i],M.hi[i];meta=M.meta[i]
        if lo==0 and hi==cp.INF and qq>0:raise ValueError(('SIGN_GE',meta,str(qq)))
        if hi==1 and qq<0:raise ValueError(('SIGN_CAP',meta,str(qq)))
        if hi==1:beta+=qq
        mult.append({'row':[list(x) if isinstance(x,tuple) else x for x in meta],'multiplier':str(qq)})
    doc={'source_result_sha256':sys.argv[3],'branches':res['branches'],'support_rows':len(mult),'bound':str(beta),'bound_float':float(beta),
         'float_objective':obj,'convention':'sum(multiplier*row_expression) == h(V) coefficientwise, where row_expression is the row as stored (>=0 rows: Shannon/DFZ expression; =0 rows: equality expression; cap rows: h(v)); >=0 rows carry nonpositive multipliers and cap rows nonnegative ones, so h(V) <= sum(cap multipliers).',
         'multipliers':mult,'elapsed_s':time.monotonic()-t0}
    with open(out,'x',encoding='utf-8') as f:json.dump(doc,f);f.write('\n')
    print(json.dumps({k:v for k,v in doc.items() if k!='multipliers'},indent=1))

if __name__=='__main__':main()
