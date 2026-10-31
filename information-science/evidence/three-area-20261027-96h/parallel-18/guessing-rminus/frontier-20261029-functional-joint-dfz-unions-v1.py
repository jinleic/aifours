#!/usr/bin/env python3
"""Bounded union-role DFZ separation, following the singleton-face plateau.
Usage: python3 script.py OUT.json POINTS.jsonl POINTS_SHA INDEX BUDGET_SECONDS [START_PREFIX]
Role assignment is {unused,A,B,C,D,Z} for each of thirteen variables. Variables
are reordered so originals 1..5 and the three functionals are in the vectorized
tail; all returned masks are translated back. Only already exactly re-derived
DFZ tuples are admitted. Candidate negatives are Fraction-replayed on the
binary-float proposal table; this is not exact primal feasibility or an
absence/optimality claim. Prefix bookkeeping permits nonduplicating continuation.
"""
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import heapq,json,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent

def load(name,path):
    s=spec_from_file_location(name,ROOT/path);m=module_from_spec(s);s.loader.exec_module(m);return m
proposal=load('proposal','frontier-20261029-functional-joint-dfz-proposal-scan-v1.py')
cp5=load('cp5union','frontier-20261029-dfz-cutting-plane-v5.py')
ORDER=(5,6,7,8,9,0,1,2,3,4,10,11,12)

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('POINT_HASH')
    idx=int(sys.argv[4]);budget=float(sys.argv[5]);start=int(sys.argv[6]) if len(sys.argv)>6 else 0
    record=next(r for r in (json.loads(l) for l in raw.decode().splitlines()) if r['index']==idx)
    originalH=proposal.joint(record);back=np.array([sum(1<<ORDER[i] for i in range(13) if m>>i&1) for m in range(8192)],dtype=np.int64);H=originalH[back]
    valid=set()
    for fn,h in proposal.VERIFY:
        data=(ROOT/fn).read_bytes()
        if sha256(data).hexdigest()!=h:raise ValueError('VERIFY_HASH')
        valid.update(tuple(r['coefficients']) for r in json.loads(data)['results'] if r['valid_exact'])
    keys=sorted(valid);S=cp5.Scanner(keys,13);W=S.W;heaps=[[] for _ in keys];t=time.monotonic();blocks=0;assignments=0;next_prefix=start;stop='complete'
    for pre in range(start,6**5):
        if time.monotonic()-t>=budget:stop='budget';next_prefix=pre;break
        d=[(pre//6**j)%6 for j in range(5)];m=[S.tail[r]+sum(1<<j for j in range(5) if d[j]==r) for r in range(6)]
        A,B,C,D,Z=m[1],m[2],m[3],m[4],m[5];ok=(A>0)&(B>0)&(C>0)&(D>0)
        if not ok.any():next_prefix=pre+1;continue
        A,B,C,D,Z=A[ok],B[ok],C[ok],D[ok],Z[ok];assignments+=len(A)
        hZ=H[Z];hAZ=H[A|Z];hBZ=H[B|Z];hCZ=H[C|Z];hDZ=H[D|Z]
        hABZ=H[A|B|Z];hACZ=H[A|C|Z];hBCZ=H[B|C|Z];hADZ=H[A|D|Z];hBDZ=H[B|D|Z];hCDZ=H[C|D|Z]
        hABCZ=H[A|B|C|Z];hABDZ=H[A|B|D|Z];hACDZ=H[A|C|D|Z]
        MF=np.stack([hAZ+hBZ-hABZ-hZ,hACZ+hBCZ-hABCZ-hCZ,hABZ+hBCZ-hABCZ-hBZ,hABZ+hACZ-hABCZ-hAZ,
                    hADZ+hBDZ-hABDZ-hDZ,hABZ+hBDZ-hABDZ-hBZ,hABZ+hADZ-hABDZ-hAZ,hCZ+hDZ-hCDZ-hZ,hACZ+hADZ-hACDZ-hAZ],axis=1)
        for st in range(0,len(MF),200000):
            V=MF[st:st+200000]@W;mins=V.min(axis=0)
            for kk in np.nonzero(mins < -1e-8)[0]:
                col=V[:,kk];pick=min(3,len(col)-1);indices=np.argpartition(col,pick)[:pick+1]
                for r in indices:
                    if col[r]>=-1e-8:continue
                    row=st+int(r);item=(-float(col[r]),int(back[A[row]]),int(back[B[row]]),int(back[C[row]]),int(back[D[row]]),int(back[Z[row]]));heap=heaps[kk]
                    if len(heap)<80:heapq.heappush(heap,item)
                    elif item[0]>heap[0][0]:heapq.heapreplace(heap,item)
        blocks+=1;next_prefix=pre+1
    @lru_cache(None)
    def F(mask):return Fraction(float(originalH[mask]))
    def I(a,b,z):return F(a|z)+F(b|z)-F(a|b|z)-F(z)
    cuts=[]
    for kk,heap in enumerate(heaps):
        k=keys[kk];kept=0
        for score,A,B,C,D,Z in sorted(heap,reverse=True):
            v=[I(A,B,Z),I(A,B,C|Z),I(A,C,B|Z),I(B,C,A|Z),I(A,B,D|Z),I(A,D,B|Z),I(B,D,A|Z),I(C,D,Z),I(C,D,A|Z)]
            value=-k[0]*v[0]+sum(k[j]*v[j] for j in range(1,9))
            if value>=0:continue
            cuts.append({'coefficients':list(k),'A':A,'B':B,'C':C,'D':D,'Z':Z,'proposal_slack_float':-score,'exact_binary_table_slack':str(value)});kept+=1
            if kept>=40:break
    doc={'points_sha256':sys.argv[3],'index':idx,'solver_status':record['status_float'],'objective_3Delta_float':record['objective_3Delta_float'],
      'variable_order_zero_based':ORDER,'start_prefix':start,'next_prefix':next_prefix,'total_prefixes':6**5,'completed_blocks':blocks,'valid_role_assignments_visited':assignments,
      'stop':stop,'elapsed_s':time.monotonic()-t,'cuts':cuts,'dfz_receipts':proposal.VERIFY,
      'limits':'Bounded floating union-role separator proposal search. Exact Fraction signs refer only to the proposal table. No exact primal feasibility, entropy realization, exhaustive absence or new bound is asserted. No paused gate-import input.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f,indent=1);f.write('\n')
    print(idx,'prefix',start,next_prefix,'cuts',len(cuts),'stop',stop,'seconds',doc['elapsed_s'],flush=True)
if __name__=='__main__':main()
