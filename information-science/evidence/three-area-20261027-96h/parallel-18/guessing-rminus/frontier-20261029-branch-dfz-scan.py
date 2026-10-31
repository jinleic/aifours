#!/usr/bin/env python3
"""Standalone scan of conditional union DFZ instances on one branch variable set.

Usage: python3 script.py OUT.json V5_RESULT.json SHA TAG [PART NPARTS]
Loads every column value recorded by frontier-20261029-dfz-cutting-plane-v5.py,
builds the full joint-entropy profile of the variable set TAG (b1: 11, b2/b3: 13
variables), scans all role assignments (optionally the PART-th of NPARTS prefix
slices) for all listed DFZ inequalities and writes the most violated instances
as cuts in the result format accepted by the v5 preload. Proposals only.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
s=spec_from_file_location('cp5',ROOT/'frontier-20261029-dfz-cutting-plane-v5.py');cp5=module_from_spec(s);s.loader.exec_module(cp5)

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('HASH')
    tag=sys.argv[4];part=int(sys.argv[5]) if len(sys.argv)>5 else 0;nparts=int(sys.argv[6]) if len(sys.argv)>6 else 1
    res=json.loads(raw);cols=res['final_columns_float'];n=cp5.NV[tag];H=np.zeros(1<<n)
    for m in range(1,1<<n):
        k=('o',m) if m<1024 else (tag,m);H[m]=cols[repr(k)]
    keys=sorted(cp5.cp.coefficients());S=cp5.Scanner(keys,n);t0=time.monotonic()
    npre=n-8;pres=[p for p in range(6**npre) if p%nparts==part]
    cands=[]
    # scan only the prefix slices assigned to this part
    for pre in pres:
        d=[(pre//6**k)%6 for k in range(npre)]
        m=[S.tail[r]+sum((1<<k) for k in range(npre) if d[k]==r) for r in range(6)]
        A,B,C,D,Z=m[1],m[2],m[3],m[4],m[5];ok=(A>0)&(B>0)&(C>0)&(D>0)
        if not ok.any():continue
        A,B,C,D,Z=A[ok],B[ok],C[ok],D[ok],Z[ok];h=lambda x:H[x]
        hZ=h(Z);hAZ=h(A|Z);hBZ=h(B|Z);hCZ=h(C|Z);hDZ=h(D|Z);hABZ=h(A|B|Z);hACZ=h(A|C|Z);hBCZ=h(B|C|Z)
        hADZ=h(A|D|Z);hBDZ=h(B|D|Z);hCDZ=h(C|D|Z);hABCZ=h(A|B|C|Z);hABDZ=h(A|B|D|Z);hACDZ=h(A|C|D|Z)
        MF=np.stack([hAZ+hBZ-hABZ-hZ,hACZ+hBCZ-hABCZ-hCZ,hABZ+hBCZ-hABCZ-hBZ,hABZ+hACZ-hABCZ-hAZ,
                     hADZ+hBDZ-hABDZ-hDZ,hABZ+hBDZ-hABDZ-hBZ,hABZ+hADZ-hABDZ-hAZ,hCZ+hDZ-hCDZ-hZ,hACZ+hADZ-hACDZ-hAZ],axis=1)
        for st in range(0,len(MF),500000):
            V=MF[st:st+500000]@S.W;k_=min(3,len(V)-1)
            if len(V)<2:continue
            p=np.argpartition(V,k_,axis=0)[:k_+1]
            colsv=np.nonzero(V[p,np.arange(V.shape[1])].min(axis=0)<-1e-9)[0]
            for kk in colsv:
                for r in p[:,kk]:
                    val=V[r,kk]
                    if val<-1e-9:cands.append((float(val),int(kk),int(A[st+r]),int(B[st+r]),int(C[st+r]),int(D[st+r]),int(Z[st+r])))
    cands.sort();per={};cuts=[];seen=set()
    for val,kk,A,B,C,D,Z in cands:
        key=(kk,A,B,C,D,Z)
        if key in seen or per.get(kk,0)>=30:continue
        seen.add(key);per[kk]=per.get(kk,0)+1
        cuts.append({'tag':tag,'coefficients':list(keys[kk]),'A':A,'B':B,'C':C,'D':D,'Z':Z,'violation_at_add':val})
        if len(cuts)>=400:break
    doc={'source_result_sha256':sys.argv[3],'tag':tag,'part':part,'nparts':nparts,'candidates':len(cands),'cuts':cuts,'elapsed_s':time.monotonic()-t0,
         'limits':'Floating scan proposal; cuts are valid DFZ instances on branch variables, used only inside a re-solved LP with an exact certificate.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(doc,f);f.write('\n')
    print(tag,part,nparts,'candidates',len(cands),'cuts',len(cuts),'elapsed',round(doc['elapsed_s'],1))

if __name__=='__main__':main()
