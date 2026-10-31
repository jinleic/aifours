#!/usr/bin/env python3
"""Faster standalone scan of conditional union DFZ instances on a branch variable set.

Usage: python3 script.py OUT.json CENTRAL.json SHA TAG [PART NPARTS]
Same semantics as frontier-20261029-branch-dfz-scan.py (same coefficient list,
same role enumeration, same cut format), but each block first computes only the
column minima of the slack matrix and extracts argmin rows just for the
inequalities whose minimum is negative. Proposals only.
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
    cols=json.loads(raw)['final_columns_float'];n=cp5.NV[tag];H=np.zeros(1<<n)
    for m in range(1,1<<n):
        k=('o',m) if m<1024 else (tag,m);H[m]=cols[repr(k)]
    keys=sorted(cp5.cp.coefficients());S=cp5.Scanner(keys,n);W=S.W;t0=time.monotonic()
    npre=n-8;cands=[];blocks=0
    for pre in range(6**npre):
        if pre%nparts!=part:continue
        d=[(pre//6**k)%6 for k in range(npre)]
        m=[S.tail[r]+sum((1<<k) for k in range(npre) if d[k]==r) for r in range(6)]
        A,B,C,D,Z=m[1],m[2],m[3],m[4],m[5];ok=(A>0)&(B>0)&(C>0)&(D>0)
        if not ok.any():continue
        A,B,C,D,Z=A[ok],B[ok],C[ok],D[ok],Z[ok];h=lambda x:H[x]
        hZ=h(Z);hAZ=h(A|Z);hBZ=h(B|Z);hCZ=h(C|Z);hDZ=h(D|Z);hABZ=h(A|B|Z);hACZ=h(A|C|Z);hBCZ=h(B|C|Z)
        hADZ=h(A|D|Z);hBDZ=h(B|D|Z);hCDZ=h(C|D|Z);hABCZ=h(A|B|C|Z);hABDZ=h(A|B|D|Z);hACDZ=h(A|C|D|Z)
        MF=np.stack([hAZ+hBZ-hABZ-hZ,hACZ+hBCZ-hABCZ-hCZ,hABZ+hBCZ-hABCZ-hBZ,hABZ+hACZ-hABCZ-hAZ,
                     hADZ+hBDZ-hABDZ-hDZ,hABZ+hBDZ-hABDZ-hBZ,hABZ+hADZ-hABDZ-hAZ,hCZ+hDZ-hCDZ-hZ,hACZ+hADZ-hACDZ-hAZ],axis=1)
        blocks+=1
        for st in range(0,len(MF),200000):
            V=MF[st:st+200000]@W;mins=V.min(axis=0);bad=np.nonzero(mins<-1e-9)[0]
            for kk in bad:
                col=V[:,kk];k_=min(3,len(col)-1);p=np.argpartition(col,k_)[:k_+1]
                for r in p:
                    if col[r]<-1e-9:cands.append((float(col[r]),int(kk),int(A[st+r]),int(B[st+r]),int(C[st+r]),int(D[st+r]),int(Z[st+r])))
    cands.sort();per={};cuts=[];seen=set()
    for val,kk,A,B,C,D,Z in cands:
        key=(kk,A,B,C,D,Z)
        if key in seen or per.get(kk,0)>=30:continue
        seen.add(key);per[kk]=per.get(kk,0)+1
        cuts.append({'tag':tag,'coefficients':list(keys[kk]),'A':A,'B':B,'C':C,'D':D,'Z':Z,'violation_at_add':val})
        if len(cuts)>=400:break
    doc={'source_result_sha256':sys.argv[3],'tag':tag,'part':part,'nparts':nparts,'blocks':blocks,'candidates':len(cands),'cuts':cuts,'elapsed_s':time.monotonic()-t0,
         'limits':'Floating scan proposal; cuts are valid DFZ instances on branch variables, used only inside a re-solved LP with an exact certificate.'}
    with open(out,'x',encoding='utf-8') as f:json.dump(doc,f);f.write('\n')
    print(tag,part,nparts,'blocks',blocks,'candidates',len(cands),'cuts',len(cuts),'elapsed',round(doc['elapsed_s'],1))

if __name__=='__main__':main()
