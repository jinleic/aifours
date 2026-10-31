#!/usr/bin/env python3
"""Exact rational dual certificate for the compressed nested-copy-block model.

Usage: python3 script.py OUT.json POINT.json POINT_SHA
Rebuilds the model from the point's extra_single_copies, cuts and nested_copy_blocks.
IPM+crossover proposes a basic dual. An exact flint solve proves the coefficient
identity and checks signs. The generator is not the independent row checker.
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
s=spec_from_file_location('ec',ROOT/'frontier-20261029-nested-copy-block-lp-v1.py');ec=module_from_spec(s);s.loader.exec_module(ec)

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('POINT_HASH')
    res=json.loads(raw);specs=res['nested_copy_blocks'];M=ec.build(res,specs);t0=time.monotonic()
    h,status,obj,x,dt=ec.cp.solve(M)
    if status!='Optimal':raise ValueError(status)
    dual=np.array(h.getSolution().row_dual);supp=[i for i,y in enumerate(dual) if abs(y)>1e-10]
    touched=sorted({j for i in supp for j in M.rows[i]}|{M.col[('o',1023)]});pos={j:r for r,j in enumerate(touched)}
    n=len(touched);goal=[0]*n;goal[pos[M.col[('o',1023)]]]=1
    Mt=[[0]*len(supp) for _ in range(n)]
    for k,i in enumerate(supp):
        for j,a in M.rows[i].items():Mt[pos[j]][k]=int(a)
    print('support rows',len(supp),'touched coordinates',n,flush=True)
    A=flint.fmpz_mat(Mt);rank=A.rank()
    if rank!=len(supp):raise ValueError(('RANK',rank,len(supp)))
    At=A.transpose();y=(At*A).solve(At*flint.fmpz_mat([[g] for g in goal]));check=flint.fmpq_mat(A)*y
    if any(check[j,0]!=goal[j] for j in range(n)):raise ValueError('IDENTITY')
    mult=[];bound=Fraction(0)
    for k,i in enumerate(supp):
        q=y[k,0];w=Fraction(int(q.p),int(q.q))
        if not w:continue
        lo,hi=M.lo[i],M.hi[i];meta=M.meta[i]
        if lo==0 and hi==ec.cp.INF and w>0:raise ValueError(('SIGN_GE',meta))
        if hi==1:
            if w<0:raise ValueError(('SIGN_CAP',meta))
            bound+=w
        mult.append({'row':[list(v) if isinstance(v,tuple) else v for v in meta],'multiplier':str(w)})
    doc={'source_result_sha256':sys.argv[3],'branches':'gurpinar-sym','extra_single_copies':res['extra_single_copies'],
         'nested_copy_blocks':specs,'programs':[],'support_rows':len(mult),'bound':str(bound),'bound_float':float(bound),
         'float_objective':obj,'multipliers':mult,'elapsed_s':time.monotonic()-t0,
         'convention':'sum(w*row)=h(original V); >=0 rows have nonpositive w, caps nonnegative. Nested branches use original subset masks and one count per conditional-iid block. Validity is the written conditional-kernel construction, not a consequence of this arithmetic solve.'}
    with open(out,'x') as f:json.dump(doc,f);f.write('\n')
    print(json.dumps({k:v for k,v in doc.items() if k!='multipliers'},indent=1))
if __name__=='__main__':main()
