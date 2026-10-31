#!/usr/bin/env python3
"""Cutting plane with DFZ instances on original AND copy-branch variable sets.

Usage: python3 script.py OUT.json MAX_ROUNDS SCAN_TAGS PRELOAD.json PRELOAD_SHA
Builds the symmetric publisher LP exactly as frontier-20261029-dfz-cutting-plane-v3.py
(branches='gurpinar-sym'), preloads every recorded cut, then in each round scans
conditional union DFZ instances on each variable set named in SCAN_TAGS
(comma list of o,b1,b2,b3; o = ten originals, b1 = originals+b'0, b2/b3 = the
13-variable branches) and adds the most violated ones. DFZ inequalities hold for
any random variables, including copy variables, so every added row is valid for
the LP's feasible set. Floating output is a proposal only.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
spec=spec_from_file_location('cp3',ROOT/'frontier-20261029-dfz-cutting-plane-v3.py');cp=module_from_spec(spec);spec.loader.exec_module(cp)
NV={'o':10,'b1':11,'b2':13,'b3':13}

def keyf(tag,m):
    if m==0:return None
    if m<1024:return ('o',m)
    return (tag,m)

class Scanner:
    def __init__(self,keys,n):
        self.n=n;self.W=np.array([[-k[0]]+list(k[1:]) for k in keys],dtype=np.float64).T
        t=8;idx=np.arange(6**t,dtype=np.int64);digs=np.stack([(idx//6**k)%6 for k in range(t)],axis=1)
        self.tail=[sum(((digs[:,k]==r).astype(np.int64)<<(k+n-t)) for k in range(t)) for r in range(6)]
    def scan(self,H,per=3,budget=1e9):
        cands=[];npre=self.n-8;t0=time.monotonic()
        for pre in range(6**npre):
            if time.monotonic()-t0>budget:break
            d=[(pre//6**k)%6 for k in range(npre)]
            m=[self.tail[r]+sum((1<<k) for k in range(npre) if d[k]==r) for r in range(6)]
            A,B,C,D,Z=m[1],m[2],m[3],m[4],m[5];ok=(A>0)&(B>0)&(C>0)&(D>0)
            if not ok.any():continue
            A,B,C,D,Z=A[ok],B[ok],C[ok],D[ok],Z[ok];h=lambda x:H[x]
            hZ=h(Z);hAZ=h(A|Z);hBZ=h(B|Z);hCZ=h(C|Z);hDZ=h(D|Z);hABZ=h(A|B|Z);hACZ=h(A|C|Z);hBCZ=h(B|C|Z)
            hADZ=h(A|D|Z);hBDZ=h(B|D|Z);hCDZ=h(C|D|Z);hABCZ=h(A|B|C|Z);hABDZ=h(A|B|D|Z);hACDZ=h(A|C|D|Z)
            MF=np.stack([hAZ+hBZ-hABZ-hZ,hACZ+hBCZ-hABCZ-hCZ,hABZ+hBCZ-hABCZ-hBZ,hABZ+hACZ-hABCZ-hAZ,
                         hADZ+hBDZ-hABDZ-hDZ,hABZ+hBDZ-hABDZ-hBZ,hABZ+hADZ-hABDZ-hAZ,hCZ+hDZ-hCDZ-hZ,hACZ+hADZ-hACDZ-hAZ],axis=1)
            for s in range(0,len(MF),500000):
                V=MF[s:s+500000]@self.W;k_=min(per,len(V)-1)
                p=np.argpartition(V,k_,axis=0)[:k_+1] if len(V)>1 else np.zeros((1,V.shape[1]),dtype=int)
                cols=np.nonzero(V[p,np.arange(V.shape[1])].min(axis=0)<-1e-9)[0]
                for kk in cols:
                    for r in p[:,kk]:
                        val=V[r,kk]
                        if val<-1e-9:cands.append((float(val),int(kk),int(A[s+r]),int(B[s+r]),int(C[s+r]),int(D[s+r]),int(Z[s+r])))
        return cands

def add_cut(M,keys,tag,kk,A,B,C,D,Z):
    t=cp.dfz_terms(keys[kk],A,B,C,D,Z)
    meta=('dfz',list(keys[kk]),A,B,C,D,Z) if tag=='o' else ('dfzb',tag,list(keys[kk]),A,B,C,D,Z)
    M.add([(keyf(tag,m),x) for m,x in t.items()],0,cp.INF,meta)

def profile(M,x,tag):
    n=NV[tag];H=np.zeros(1<<n)
    for m in range(1,1<<n):H[m]=x[M.col[keyf(tag,m)]]
    return H

def main():
    out=ROOT/sys.argv[1];rounds=int(sys.argv[2]);tags=sys.argv[3].split(',')
    t0=time.monotonic();coeff=cp.coefficients();keys=sorted(coeff);M=cp.build('gurpinar-sym')
    raw=(ROOT/sys.argv[4]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[5]:raise ValueError('PRELOAD_HASH')
    seen=set();cuts=[]
    for c in json.loads(raw)['cuts']:
        tag=c.get('tag','o');kk=keys.index(tuple(c['coefficients']));key=(tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        if key in seen:continue
        seen.add(key);add_cut(M,keys,tag,kk,c['A'],c['B'],c['C'],c['D'],c['Z'])
        cuts.append({'tag':tag,'coefficients':list(keys[kk]),'A':c['A'],'B':c['B'],'C':c['C'],'D':c['D'],'Z':c['Z'],'violation_at_add':'preloaded'})
    scanners={t:Scanner(keys,NV[t]) for t in tags}
    print('columns',len(M.col),'rows',len(M.rows),'preloaded',len(cuts),flush=True)
    h,status,obj,x,dt=cp.solve(M);log=[{'round':0,'status':status,'objective':obj,'rows':len(M.rows),'solve_s':round(dt,1)}];print(log[-1],flush=True)
    for rnd in range(1,rounds+1):
        chosen=[]
        for tag in tags:
            cands=scanners[tag].scan(profile(M,x,tag));cands.sort();per={};cnt=0
            for val,kk,A,B,C,D,Z in cands:
                key=(tag,kk,A,B,C,D,Z)
                if key in seen or per.get(kk,0)>=30:continue
                seen.add(key);per[kk]=per.get(kk,0)+1;chosen.append((val,tag,kk,A,B,C,D,Z));cnt+=1
                if cnt>=300:break
            print('round',rnd,'tag',tag,'candidates',len(cands),'chosen',cnt,'scan_elapsed',round(time.monotonic()-t0,1),flush=True)
        if not chosen:log.append({'round':rnd,'violations':0});print('no violations',flush=True);break
        start=len(M.rows)
        for val,tag,kk,A,B,C,D,Z in chosen:
            add_cut(M,keys,tag,kk,A,B,C,D,Z)
            cuts.append({'tag':tag,'coefficients':list(keys[kk]),'A':A,'B':B,'C':C,'D':D,'Z':Z,'violation_at_add':val})
        h,status,obj,x,dt=cp.solve(M,h,start)
        log.append({'round':rnd,'added':len(chosen),'most_violated':min(c[0] for c in chosen),'status':status,'objective':obj,'rows':len(M.rows),'solve_s':round(dt,2),'elapsed_s':round(time.monotonic()-t0,1)})
        print(log[-1],flush=True)
    res={'branches':'gurpinar-sym','scan_tags':tags,'tex_sha256':cp.TEX_SHA,'inequalities':len(keys),'log':log,'final_objective_float':obj,'cuts':cuts,
         'final_original_profile_float':[float(v) for v in profile(M,x,'o')[1:]],
         'limits':'Floating cutting-plane proposal only. A bound is claimed only after an exact rational dual certificate is reconstructed and independently checked.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(res,f);f.write('\n')

if __name__=='__main__':main()
