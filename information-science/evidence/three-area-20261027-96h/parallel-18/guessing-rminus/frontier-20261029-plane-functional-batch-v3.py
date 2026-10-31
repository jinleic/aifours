#!/usr/bin/env python3
"""Batch: functional LP (IPM + basic restriction) then exact rational dual.

Usage: python3 script.py OUT.jsonl CLASSES.json INDICES LIMIT_SECONDS
Version 3: reruns the listed class indices (comma-separated) with the given LP time limit;
otherwise identical to frontier-20261028-plane-functional-batch.py.
CLASSES.json holds {"colorings": ["--01-111--", ...]}. For each coloring the
floating dual support is re-solved exactly over Q (python-flint) on the support
rows; the certificate is kept only if the exact identity holds with correct
signs. Output lines: {"index","colors","status","certificate"|null}.
"""
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
from time import monotonic
import json,sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-flint'))
import flint
spec=spec_from_file_location('fl',ROOT/'frontier-20261028-plane-functional-v2-lp.py');fl=module_from_spec(spec);spec.loader.exec_module(fl)
N=fl.N;TRI=fl.TRI;V=fl.V;S=fl.S;FULL=fl.FULL

def terms(name,col):
    k=name[0]
    def H(m,b):return (m&V,b if m&S else 0)
    def vm(vs):return sum(1<<(v-1) for v in vs)
    if k=='mono':_,br,i=name;return [(*H(FULL,br),1),(*H(FULL^(1<<i),br),-1)]
    if k=='cmi':_,br,i,j,K=name;a,b=1<<i,1<<j;return [(*H(K|a,br),1),(*H(K|b,br),1),(*H(K|a|b,br),-1),(*H(K,br),-1)]
    if k=='aux-determined':return [(V,name[1],1),(V,0,-1)]
    if k=='gate':br=name[1];return [(V,0,3),(0,br,17)]+[(1<<i,br,-2) for i in range(10)]
    if k=='graph-fd':v=name[1];n=vm(N[v]);return [(n|1<<(v-1),0,1),(n,0,-1)]
    if k=='functional-neighborhood':_,v,c=name;n=vm(N[v]);return [(n,2+c,1),(n,0,-1)]
    if k=='state-neighborhood':n=vm(N[name[1]]);return [(n,1,1),(n,0,-1)]
    if k=='mixed-local-fd':
        v=name[1];L=vm({u for t,T in enumerate(TRI) if col[t] is not None and v in T for u in T if u!=v});return [(L|1<<(v-1),1,1),(L,1,-1)]
    if k=='functional-triangle':t=name[1];m=vm(TRI[t-1]);return [(m,2+col[t-1],1),(m,0,-1)]
    if k=='data-processing':_,a,j=name;return [(a,j,1),(a,1,-1)]
    if k=='pair-determines-state':_,a,j,l=name;return [(a,1,1),(a,j,-1),(a,l,-1),(a,0,1)]
    raise ValueError(name)

def exact(r):
    col=r['colors'];acts=[(tuple(p),tuple(cp)) for p,cp in r['actions']]
    def tr(a,b,p,cp):return (fl.move(a,p),2+cp[b-2] if b>=2 else b)
    def canon(a,b):return min(tr(a,b,p,cp) for p,cp in acts)
    keys=[tuple(k) for k in r['keys']];ix={k:i for i,k in enumerate(keys)};n=len(keys);dd=r['dual_support'];k=len(dd)
    M=[[0]*k for _ in range(n)]
    for j,z in enumerate(dd):
        for a,b,w in terms(z['name'],col):
            if a or b:M[ix[canon(a,b)]][j]+=w
    t=[0]*n;t[ix[canon(V,0)]]+=3
    for i in range(10):t[ix[canon(1<<i,0)]]-=2
    Mf=flint.fmpz_mat(M)
    if Mf.rank()!=k:return None,'RANK_DEFICIENT'
    Mt=Mf.transpose();y=(Mt*Mf).solve(Mt*flint.fmpz_mat([[x] for x in t]))
    res=flint.fmpq_mat(Mf)*y
    if any(res[i,0]!=t[i] for i in range(n)):return None,'INCONSISTENT'
    mult=[]
    for j,z in enumerate(dd):
        q=y[j,0];kind=z['name'][0]
        if q==0:continue
        if kind in ('cmi','mono') and not q<0:return None,'SIGN'
        if kind in ('gate','data-processing','pair-determines-state') and not q>0:return None,'SIGN'
        mult.append({'row':z['name'],'multiplier':str(q)})
    return {'colors':col,'actions':r['actions'],'multipliers':mult,'target':'3*Delta'},'ok'

def main():
    out=ROOT/sys.argv[1];classes=json.loads((ROOT/sys.argv[2]).read_text())['colorings'];idxs=[int(x) for x in sys.argv[3].split(',')];limit=float(sys.argv[4])
    t0=monotonic()
    with open(out,'x',encoding='utf-8') as f:
        for idx in idxs:
            text=classes[idx];col=tuple(None if ch=='-' else int(ch) for ch in text)
            r=fl.solve(col,limit);cert=None;status=r['status']
            if r['status']=='Optimal' and abs(r['objective'])<1e-7 and 'dual_support' in r:
                cert,status=exact(r)
            elif r['status']=='Optimal':status='positive_objective'
            f.write(json.dumps({'index':idx,'colors':text,'status':status,'certificate':cert,'time_limit_s':limit})+'\n');f.flush()
            print(idx,text,status,round(monotonic()-t0,1),flush=True)


if __name__=='__main__':main()
