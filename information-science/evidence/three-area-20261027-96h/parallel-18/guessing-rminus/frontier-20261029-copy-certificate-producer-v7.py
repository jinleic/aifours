#!/usr/bin/env python3
"""Exact dual certificate for the v7 LP (publisher branches + extra single copies + multi-step copy programs + DFZ cuts).

Usage: python3 script.py OUT.json CENTRAL_RESULT.json SHA
Version 7: also adds every copy program recorded in the result (key 'programs', format of
frontier-20261029-multistep-screen-v4.py) as branch m<k> with variables a..j plus m<k>.c0, m<k>.c1, ...
(names are unique per program so that the checker can attribute every Shannon row).
Rebuilds the model with frontier-20261029-dfz-cutting-plane-v3.py (symmetric
publisher LP), adds the extra single-copy branches with
frontier-20261029-copy-cutting-plane-v6.py and every recorded DFZ cut, re-solves
by IPM with crossover, and solves the dual identity exactly over Q
(python-flint) on the basic support. The extra branch specifications are
embedded in the certificate for the independent checker.
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
def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
cp=load('cp3','frontier-20261029-dfz-cutting-plane-v3.py');v5=load('cp5','frontier-20261029-dfz-cutting-plane-v5.py');v6=load('cp6','frontier-20261029-copy-cutting-plane-v6.py')
ms=load('ms4','frontier-20261029-multistep-screen-v4.py')

def add_program(M,tag,prog):
    n,steps=ms.compile_program(prog);names=list('abcdefghij')+[f'{tag}.c{j}' for j in range(n-10)]
    def keyf(m):
        if m==0:return None
        return ('o',m) if m<1024 else (tag,m)
    cp.add_shannon(M,names,keyf)
    for si,(new,old,Y,E) in enumerate(steps):
        k=len(new);Nn=sum(1<<b for b in new)
        for q in range(1,1<<k):
            nm=sum(1<<new[a] for a in range(k) if q>>a&1);om=0
            for a in range(k):
                if q>>a&1:om|=old[a]
            U=Y
            while True:
                M.add([(keyf(U|nm),1),(keyf(U|om),-1)],0,0,('mcopy',tag,si,q,U))
                if not U:break
                U=(U-1)&Y
        M.add([(keyf(E|Nn),1),(keyf(Y),1),(keyf(E),-1),(keyf(Y|Nn),-1)],0,0,('mindependence',tag,si))

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    res=json.loads(raw);keys=sorted(cp.coefficients());M=cp.build('gurpinar-sym');extra=res['extra_single_copies']
    for k,(S,T) in enumerate(extra):v6.add_single_copy(M,k,S[0],T)
    progs=res.get('programs',[])
    for k,p in enumerate(progs):add_program(M,f'm{k}',p)
    seen=set()
    for c in res['cuts']:
        tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if key in seen:continue
        seen.add(key);v5.add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
    t0=time.monotonic();h,status,obj,x,dt=cp.solve(M)
    if status!='Optimal':raise ValueError(status)
    dual=np.array(h.getSolution().row_dual);supp=[i for i,y in enumerate(dual) if abs(y)>1e-10]
    touched=sorted({j for i in supp for j in M.rows[i]}|{M.col[('o',1023)]});pos={j:r for r,j in enumerate(touched)}
    ncol=len(touched);goal=[0]*ncol;goal[pos[M.col[('o',1023)]]]=1
    Mt=[[0]*len(supp) for _ in range(ncol)]
    for k,i in enumerate(supp):
        for j,a in M.rows[i].items():Mt[pos[j]][k]=int(a)
    print('support rows',len(supp),'touched coordinates',ncol,flush=True)
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
    doc={'source_result_sha256':sys.argv[3],'branches':'gurpinar-sym','extra_single_copies':extra,'programs':progs,'support_rows':len(mult),'bound':str(beta),'bound_float':float(beta),
         'float_objective':obj,'convention':'sum(multiplier*row_expression) == h(V) coefficientwise; >=0 rows carry nonpositive multipliers, cap rows nonnegative ones. Extra branch k is the variable set a..j,s\'k with s\'k a copy of X_S over X_T. Program branch m<k> is a..j plus its copies (sequential copy lemma).',
         'multipliers':mult,'elapsed_s':time.monotonic()-t0}
    with open(out,'x',encoding='utf-8') as f:json.dump(doc,f);f.write('\n')
    print(json.dumps({k:v for k,v in doc.items() if k!='multipliers'},indent=1))

if __name__=='__main__':main()
